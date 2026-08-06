#!/usr/bin/env python3
"""가이드 원고의 기계적 정합성 검사.

Hugo 빌드가 통과해도 렌더링이 깨지는 항목까지 함께 본다:
  - front matter 필수 필드
  - 각주 사용/정의 양방향 대조
  - imgproc 참조 이미지의 페이지 번들 내 존재 (static/ 이 없으므로 번들 밖 이미지는 배포되지 않는다)
  - 내부 앵커 링크 ↔ 헤딩 슬러그 대조 (한글 헤딩을 앵커로 쓰므로 헤딩 수정 시 조용히 깨진다)
  - shortcode 열고 닫기 균형
  - 표 헤더/구분선 열 수 일치

사용법:
    check_guide_integrity.py [파일 ...] [--json] [--strict]

파일을 주지 않으면 content/en 아래의 모든 _index.md 를 검사한다.
_workspace/ 의 초안(05_draft_*.md, 06_edited_*.md)을 검사할 때는 --bundle 로
이미지 조회 기준 디렉토리를 지정한다 (초안은 페이지 번들 밖에 있으므로).

종료 코드: 0 = blocking 없음, 1 = blocking 있음, 2 = 사용법/입력 오류
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")

RE_FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:")
RE_FOOTNOTE_USE = re.compile(r"\[\^([^\]]+)\]")
RE_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
RE_ANCHOR_LINK = re.compile(r"\]\(#([^)]+)\)")
RE_IMGPROC_OPEN = re.compile(r"\{\{<\s*imgproc\s+([A-Za-z0-9_.-]+)")
RE_IMGPROC_SELFCLOSE = re.compile(r"/\s*>\}\}\s*$")
RE_IMGPROC_CLOSE = re.compile(r"\{\{<\s*/\s*imgproc\s*>\}\}")
RE_SHORTCODE_PCT_OPEN = re.compile(r"\{\{%\s*(alert|pageinfo)\b")
RE_SHORTCODE_PCT_CLOSE = re.compile(r"\{\{%\s*/\s*(alert|pageinfo)\s*%\}\}")
RE_TABLE_SEP = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
RE_FENCE = re.compile(r"^\s*(```|~~~)")

KNOWN_SHORTCODES = {"alert", "pageinfo", "imgproc", "blocks", "readfile", "swaggerui"}
RE_ANY_SHORTCODE = re.compile(r"\{\{[<%]\s*/?\s*([A-Za-z0-9_/-]+)")


def slugify(text: str) -> str:
    """Hugo goldmark(github 스타일) 헤딩 슬러그. 한글은 그대로 남는다."""
    text = re.sub(r"`([^`]*)`", r"\1", text)                    # 인라인 코드
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)        # 링크 → 텍스트
    text = re.sub(r"<[^>]+>", "", text)                          # html 태그 제거, 내부 텍스트 유지
    text = re.sub(r"[*_]{1,3}", "", text)                        # 강조 기호
    out = []
    for ch in text.strip().lower():
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        elif ch.isspace():
            out.append("-")
    return "".join(out)


def split_front_matter(lines: list[str]) -> tuple[dict, int]:
    """--- 로 감싼 YAML front matter 를 얕게 파싱한다. (fields, 본문 시작 인덱스)

    Hugo 는 구분자 앞의 빈 줄을 허용한다 (content/en/_index.md 가 그 상태로 배포되고 있다).
    빈 줄을 이유로 front matter 없음이라 판정하면 오탐이 된다.
    """
    start = 0
    while start < len(lines) and not lines[start].strip():
        start += 1
    if start >= len(lines) or lines[start].strip() != "---":
        return {}, 0
    for i in range(start + 1, len(lines)):
        if lines[i].strip() == "---":
            fields = {}
            for raw in lines[start + 1:i]:
                m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", raw)
                if m:
                    fields[m.group(1)] = m.group(2).strip()
            return fields, i + 1
    return {}, 0


def body_line_map(lines: list[str], start: int) -> list[tuple[int, str]]:
    """코드 펜스 안을 제외한 (1-based 줄번호, 내용) 목록."""
    result = []
    in_fence = False
    for idx in range(start, len(lines)):
        line = lines[idx]
        if RE_FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        result.append((idx + 1, line))
    return result


def check_file(path: Path, bundle_dir: Path | None) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    fm, body_start = split_front_matter(lines)
    body = body_line_map(lines, body_start)
    rel = str(path)

    issues: list[dict] = []

    def add(kind, line, detail, blocking):
        issues.append({"kind": kind, "file": rel, "line": line, "detail": detail, "blocking": blocking})

    # --- front matter -------------------------------------------------
    if not fm:
        add("front_matter", 1, "front matter 가 없다 (--- 로 감싼 YAML 필요)", True)
    else:
        for field in ("title",):
            if field not in fm:
                add("front_matter", 1, f"필수 필드 누락: {field}", True)
        # 섹션 페이지(_index.md)는 사이드바 표기와 순서가 필요하다
        if path.name == "_index.md" and path.parent.name != "en":
            for field in ("linkTitle", "weight"):
                if field not in fm:
                    add("front_matter", 1, f"섹션 페이지 필수 필드 누락: {field}", False)

    # --- 각주 ---------------------------------------------------------
    defs: dict[str, int] = {}
    uses: dict[str, int] = {}
    for ln, line in body:
        m = RE_FOOTNOTE_DEF.match(line)
        if m:
            label = m.group(1)
            if label in defs:
                add("footnote", ln, f"각주 정의 중복: [^{label}] (앞선 정의 {defs[label]}행)", False)
            defs[label] = ln
            continue
        for label in RE_FOOTNOTE_USE.findall(line):
            uses.setdefault(label, ln)

    for label, ln in uses.items():
        if label not in defs:
            add("undefined_footnote", ln, f"정의 없는 각주 [^{label}] — 본문에 원문 노출됨", True)
    for label, ln in defs.items():
        if label not in uses:
            add("unused_footnote_def", ln, f"사용되지 않는 각주 정의 [^{label}]", False)

    # --- 헤딩 슬러그 / 앵커 -------------------------------------------
    slugs: dict[str, int] = {}
    slug_counts: dict[str, int] = {}
    for ln, line in body:
        m = RE_HEADING.match(line)
        if not m:
            continue
        base = slugify(m.group(2))
        if not base:
            continue
        n = slug_counts.get(base, 0)
        slug_counts[base] = n + 1
        slug = base if n == 0 else f"{base}-{n}"
        slugs[slug] = ln
        if n > 0:
            add("duplicate_heading", ln, f"헤딩 텍스트 중복 — 슬러그가 '{slug}' 로 밀림", False)

    for ln, line in body:
        for anchor in RE_ANCHOR_LINK.findall(line):
            anchor = anchor.strip()
            if anchor in slugs:
                continue
            hint = ""
            lowered = anchor.lower()
            if lowered != anchor and lowered in slugs:
                hint = f" (대소문자 문제 — '{lowered}' 로 써야 한다)"
            add("dead_anchor", ln, f"대상 헤딩이 없는 앵커 링크: #{anchor}{hint}", True)

    # --- imgproc 참조 이미지 ------------------------------------------
    img_dir = bundle_dir if bundle_dir is not None else path.parent
    open_imgproc: list[tuple[int, str]] = []
    for ln, line in body:
        m = RE_IMGPROC_OPEN.search(line)
        if m:
            name = m.group(1)
            found = None
            for ext in IMAGE_EXTS:
                for cand in (img_dir / f"{name}{ext}", img_dir / f"{name}{ext.upper()}"):
                    if cand.exists():
                        found = cand
                        break
                if found:
                    break
            if not found:
                add("missing_image", ln,
                    f"imgproc 참조 이미지 없음: {name} (조회 위치 {img_dir}/{name}.{{png,jpg,...}})", True)
            if not RE_IMGPROC_SELFCLOSE.search(line):
                open_imgproc.append((ln, name))
        if RE_IMGPROC_CLOSE.search(line):
            if open_imgproc:
                open_imgproc.pop()
            else:
                add("shortcode", ln, "짝이 없는 {{< /imgproc >}}", True)
    for ln, name in open_imgproc:
        add("shortcode", ln, f"닫히지 않은 imgproc 블록: {name}", True)

    # --- alert / pageinfo 균형 ---------------------------------------
    pct_stack: list[tuple[int, str]] = []
    for ln, line in body:
        for name in RE_SHORTCODE_PCT_OPEN.findall(line):
            pct_stack.append((ln, name))
        for name in RE_SHORTCODE_PCT_CLOSE.findall(line):
            if pct_stack and pct_stack[-1][1] == name:
                pct_stack.pop()
            else:
                add("shortcode", ln, f"짝이 없는 {{{{% /{name} %}}}}", True)
    for ln, name in pct_stack:
        add("shortcode", ln, f"닫히지 않은 {name} 블록", True)

    # --- 미지의 shortcode --------------------------------------------
    for ln, line in body:
        for name in RE_ANY_SHORTCODE.findall(line):
            base = name.strip("/").split("/")[0]
            if base and base not in KNOWN_SHORTCODES:
                add("unknown_shortcode", ln,
                    f"Docsy 가 제공하지 않는 shortcode: {base} — 빌드 실패한다", True)

    # --- 표 열 수 -----------------------------------------------------
    for i in range(len(body) - 1):
        ln, line = body[i]
        nxt = body[i + 1][1]
        if not line.strip().startswith("|") or not RE_TABLE_SEP.match(nxt):
            continue
        head_cols = len([c for c in line.strip().strip("|").split("|")])
        sep_cols = len([c for c in nxt.strip().strip("|").split("|")])
        if head_cols != sep_cols:
            add("table", ln, f"표 헤더 {head_cols}열 / 구분선 {sep_cols}열 불일치", True)

    return {
        "file": rel,
        "front_matter": fm,
        "counts": {
            "lines": len(lines),
            "headings": len(slugs),
            "footnote_defs": len(defs),
            "footnote_uses": len(uses),
        },
        "issues": issues,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="가이드 원고 정합성 검사")
    ap.add_argument("files", nargs="*", help="검사할 마크다운 파일 (생략 시 content/en/**/_index.md)")
    ap.add_argument("--json", action="store_true", help="JSON 으로 출력")
    ap.add_argument("--bundle", metavar="DIR",
                    help="imgproc 이미지 조회 디렉토리 (_workspace/ 초안 검사 시 지정)")
    ap.add_argument("--strict", action="store_true",
                    help="non-blocking 항목도 종료 코드에 반영")
    args = ap.parse_args()

    if args.files:
        paths = [Path(f) for f in args.files]
    else:
        root = Path("content/en")
        if not root.is_dir():
            print("content/en 이 없다. 저장소 루트에서 실행하거나 파일을 직접 지정하라.", file=sys.stderr)
            return 2
        paths = sorted(root.glob("**/_index.md"))

    missing = [p for p in paths if not p.is_file()]
    if missing:
        for p in missing:
            print(f"파일 없음: {p}", file=sys.stderr)
        return 2

    bundle = Path(args.bundle) if args.bundle else None
    if bundle is not None and not bundle.is_dir():
        print(f"--bundle 디렉토리 없음: {bundle}", file=sys.stderr)
        return 2

    reports = [check_file(p, bundle) for p in paths]
    all_issues = [i for r in reports for i in r["issues"]]
    blocking = [i for i in all_issues if i["blocking"]]

    if args.json:
        print(json.dumps({
            "reports": reports,
            "summary": {
                "files": len(reports),
                "issues": len(all_issues),
                "blocking": len(blocking),
                "verdict": "pass" if not blocking else "fail",
            },
        }, ensure_ascii=False, indent=2))
    else:
        for r in reports:
            c = r["counts"]
            print(f"\n=== {r['file']} ({c['lines']}행, 헤딩 {c['headings']}, "
                  f"각주 {c['footnote_uses']}사용/{c['footnote_defs']}정의) ===")
            if not r["issues"]:
                print("  문제 없음")
                continue
            for i in sorted(r["issues"], key=lambda x: (not x["blocking"], x["line"])):
                mark = "BLOCK" if i["blocking"] else "warn "
                print(f"  [{mark}] {i['line']:>5}  {i['kind']}: {i['detail']}")
        print(f"\n요약: {len(reports)}개 파일, 문제 {len(all_issues)}건 "
              f"(blocking {len(blocking)}건) → {'pass' if not blocking else 'FAIL'}")

    if blocking:
        return 1
    if args.strict and all_issues:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
