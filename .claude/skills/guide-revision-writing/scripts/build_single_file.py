#!/usr/bin/env python3
"""사이트 정본(content/en/*/_index.md)을 배포용 단일 마크다운으로 합친다.

루트의 `oss-governance-guide.md`(2023-02 발간본)와 같은 성격의 파일을 개정판마다
새로 만든다. 정본을 고치고 이 스크립트를 다시 돌리는 것이 유일한 갱신 경로다 —
산출물을 직접 편집하면 다음 실행에서 덮어써진다.

Hugo shortcode 와 사이트 전용 링크는 GitHub 마크다운에서 렌더링되지 않으므로 변환한다:
  - `{{< imgproc NAME Fit "WxH" >}}<center><i>[캡션]</i></center>{{< /imgproc >}}`
      → `![캡션](content/en/SLUG/NAME.png)` + 이탤릭 캡션 줄
  - `{{% alert title="T" %}}...{{% /alert %}}` → 인용 블록
  - `](/using/#앵커)` → `](#앵커)`,  `](/using/)` → 해당 장 H1 앵커

각주 ID 는 섹션마다 독립 공간이라 합치면 충돌한다(현재 4건: ai-act, ai-omnibus,
osv-scanner, scorecard). 정의된 ID 전부에 섹션 접두어를 붙여 회피한다. 렌더링 결과는
번호라서 ID 가 길어져도 독자에게 보이지 않는다.

사용법:
    python3 .claude/skills/guide-revision-writing/scripts/build_single_file.py \
        --out oss-governance-guide-2026.md --edition "2026 개정판"
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

# 순서는 사이트 사이드바(front matter weight)와 같아야 한다.
SECTIONS = ["intro", "using", "contributing", "releasing", "ospo", "ai"]

RE_IMGPROC = re.compile(
    r"\{\{<\s*imgproc\s+(?P<name>\S+)[^>]*>\}\}(?P<body>.*?)\{\{<\s*/\s*imgproc\s*>\}\}",
    re.S,
)
RE_ALERT_OPEN = re.compile(r"^\s*\{\{[<%]\s*alert(?P<attrs>[^%>]*?)\s*[%>]\}\}\s*$")
RE_ALERT_CLOSE = re.compile(r"^\s*\{\{[<%]\s*/\s*alert\s*[%>]\}\}\s*$")
RE_FENCE = re.compile(r"^\s*(```|~~~)")
RE_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
RE_FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:")


def slugify(text: str) -> str:
    """Hugo goldmark 의 GitHub 스타일 슬러그를 재현한다."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_]{1,3}", "", text)
    out = []
    for ch in text.strip().lower():
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        elif ch.isspace():
            out.append("-")
    return "".join(out)


def read_front_matter(text: str) -> tuple[dict, str]:
    """front matter 를 떼어내고 (필드, 본문) 을 돌려준다."""
    lines = text.split("\n")
    start = 0
    while start < len(lines) and not lines[start].strip():
        start += 1
    if start >= len(lines) or lines[start].strip() != "---":
        return {}, text
    for i in range(start + 1, len(lines)):
        if lines[i].strip() == "---":
            fields = {}
            for raw in lines[start + 1 : i]:
                m = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', raw)
                if m:
                    fields[m.group(1)] = m.group(2)
            return fields, "\n".join(lines[i + 1 :])
    return {}, text


def convert_imgproc(text: str, slug: str, repo: pathlib.Path) -> tuple[str, int, list[str]]:
    """imgproc 블록을 마크다운 이미지로 바꾸고 실제 파일 경로를 해석한다."""
    missing: list[str] = []

    def repl(m: re.Match) -> str:
        name = m.group("name").strip('"')
        body = m.group("body")
        cap = re.search(r"\[(.*?)\]", re.sub(r"<[^>]+>", "", body), re.S)
        caption = cap.group(1).strip() if cap else name

        # imgproc 는 확장자 없이 참조한다. 페이지 번들에서 실제 파일을 찾는다.
        hits = sorted((repo / "content/en" / slug).glob(name + ".*"))
        hits = [h for h in hits if h.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".svg")]
        if not hits:
            missing.append(f"{slug}/{name}")
            rel = f"content/en/{slug}/{name}.png"
        else:
            rel = f"content/en/{slug}/{hits[0].name}"
        return f"![{caption}]({rel})\n\n*[{caption}]*"

    new, n = RE_IMGPROC.subn(repl, text)
    return new, n, missing


def convert_alerts(text: str) -> tuple[str, int]:
    """alert shortcode 를 인용 블록으로 바꾼다. 코드 펜스 안은 건드리지 않는다."""
    out: list[str] = []
    in_fence = False
    in_alert = False
    count = 0

    for line in text.split("\n"):
        if RE_FENCE.match(line):
            in_fence = not in_fence
            out.append(("> " + line) if in_alert else line)
            continue
        if in_fence:
            out.append(("> " + line) if in_alert else line)
            continue

        m = RE_ALERT_OPEN.match(line)
        if m and not in_alert:
            in_alert = True
            count += 1
            title = re.search(r'title="([^"]*)"', m.group("attrs"))
            if title:
                out.append(f"> **{title.group(1)}**")
                out.append(">")
            continue
        if RE_ALERT_CLOSE.match(line):
            in_alert = False
            out.append("")
            continue
        out.append(("> " + line).rstrip() if in_alert else line)

    return "\n".join(out), count


def namespace_footnotes(text: str, slug: str) -> tuple[str, int]:
    """이 섹션에서 정의된 각주 ID 에만 섹션 접두어를 붙인다.

    정의되지 않은 대괄호 표현(`[^]]` 같은 정규식)을 건드리지 않도록 정의 목록을
    먼저 모으고, 코드 펜스 밖에서만 치환한다.
    """
    defined = set()
    in_fence = False
    for line in text.split("\n"):
        if RE_FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = RE_FOOTNOTE_DEF.match(line)
        if m:
            defined.add(m.group(1))
    if not defined:
        return text, 0

    pattern = re.compile(r"\[\^(" + "|".join(re.escape(d) for d in sorted(defined, key=len, reverse=True)) + r")\]")
    out: list[str] = []
    in_fence = False
    for line in text.split("\n"):
        if RE_FENCE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        out.append(line if in_fence else pattern.sub(rf"[^{slug}-\1]", line))
    return "\n".join(out), len(defined)


def rewrite_links(text: str, chapter_anchor: dict[str, str]) -> tuple[str, int]:
    """사이트 내부 링크를 단일 파일 내부 앵커로 바꾼다.

    본문은 상대 경로(`](../using/)`)를 쓴다. 서브 경로 baseURL 에서 마크다운
    절대 경로에 서브 경로가 붙지 않아 404 가 되기 때문이다. 과거 원고에 남아
    있을 수 있는 절대 경로(`](/using/)`) 도 함께 받아 준다.
    """
    n = 0
    prefix = r"\]\((?:\.\./|/)(?:" + "|".join(SECTIONS) + r")/"
    # ../using/#앵커 → #앵커  (합쳐지면 같은 문서이므로 경로가 사라진다)
    text, k = re.subn(prefix + "#", "](#", text)
    n += k
    # ../using/ → 해당 장 H1 앵커
    for slug, anchor in chapter_anchor.items():
        text, k = re.subn(r"\]\((?:\.\./|/)" + re.escape(slug) + r"/\)", f"](#{anchor})", text)
        n += k
    return text, n


def collect_toc(body: str, level: int = 2) -> list[str]:
    """코드 펜스 밖의 H2 만 모은다."""
    items: list[str] = []
    in_fence = False
    for line in body.split("\n"):
        if RE_FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = RE_HEADING.match(line)
        if m and len(m.group(1)) == level:
            items.append(m.group(2).strip())
    return items


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".", help="저장소 루트")
    ap.add_argument("--out", required=True, help="산출 파일 경로")
    ap.add_argument("--edition", default="2026 개정판")
    ap.add_argument("--title", default="기업 오픈소스SW 거버넌스 가이드")
    args = ap.parse_args()

    repo = pathlib.Path(args.repo).resolve()

    # 1차 통과 — front matter 를 읽어 장 번호와 H1 앵커를 먼저 확정한다.
    meta: list[dict] = []
    for slug in SECTIONS:
        path = repo / "content/en" / slug / "_index.md"
        if not path.exists():
            print(f"  ! 정본 없음: {path}", file=sys.stderr)
            return 1
        raw = path.read_text(encoding="utf-8")
        fm, body = read_front_matter(raw)
        link = fm.get("linkTitle", fm.get("title", slug))
        num = link.split(".")[0].strip() if "." in link else ""
        title = fm.get("title", slug)
        h1 = f"{num}. {title}" if num else title
        meta.append({"slug": slug, "h1": h1, "anchor": slugify(h1), "body": body, "title": title})

    chapter_anchor = {m["slug"]: m["anchor"] for m in meta}

    # 2차 통과 — 변환
    chunks: list[str] = []
    toc: list[str] = []
    stats: list[tuple] = []
    missing_images: list[str] = []

    for m in meta:
        body = m["body"]
        body, n_img, miss = convert_imgproc(body, m["slug"], repo)
        missing_images += miss
        body, n_alert = convert_alerts(body)
        body, n_fn = namespace_footnotes(body, m["slug"])
        body, n_link = rewrite_links(body, chapter_anchor)

        toc.append(f"- [{m['h1']}](#{m['anchor']})")
        for h2 in collect_toc(body):
            toc.append(f"  - [{h2}](#{slugify(h2)})")

        chunks.append(f"# {m['h1']}\n{body.rstrip()}\n")
        stats.append((m["slug"], len(body.split("\n")), n_img, n_alert, n_fn, n_link))

    header = f"""# {args.title} — {args.edition}

> 이 파일은 사이트 정본을 한 파일로 합친 **배포용 통합본**이다. 스크립트가 생성하므로
> 직접 편집하지 않는다 — 내용을 고칠 때는 `content/en/<장>/_index.md` 를 고치고 다시 생성한다.
>
> - 생성: `python3 .claude/skills/guide-revision-writing/scripts/build_single_file.py --out {pathlib.Path(args.out).name}`
> - 사이트: https://NIPA-OpenUP.github.io/oss-governance-guide/
> - 이전 판: `oss-governance-guide.md` (2023년 2월)
> - 라이선스: 공공누리 제1유형

## 목차

{chr(10).join(toc)}

---
"""

    out_path = repo / args.out
    out_path.write_text(header + "\n" + "\n\n---\n\n".join(chunks), encoding="utf-8")

    total = len(out_path.read_text(encoding="utf-8").split("\n"))
    print(f"{'섹션':<14}{'행수':>7}{'이미지':>7}{'alert':>7}{'각주ID':>8}{'링크':>6}")
    for s in stats:
        print(f"  {s[0]:<12}{s[1]:>7}{s[2]:>7}{s[3]:>7}{s[4]:>8}{s[5]:>6}")
    print(f"\n{out_path.relative_to(repo)} — {total}행, {out_path.stat().st_size:,} bytes")
    if missing_images:
        print(f"! 참조 이미지 없음 {len(missing_images)}건: {missing_images}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
