#!/usr/bin/env python3
"""'오픈소스' → '오픈소스SW' 잔여 통일 + 앵커 링크 동기화.

교정 단계에서 에이전트가 헤딩을 건드리지 않도록 지시했기 때문에 헤딩 98개가
'오픈소스'로 남았다. 발간본은 헤딩도 '오픈소스SW'를 쓰므로 여기서 맞춘다.
헤딩을 바꾸면 그것을 가리키는 앵커 링크가 죽으므로 링크를 함께 갱신한다.

예외는 발간본의 실제 용례로 정했다:
  - '오픈소스 프로그램'  발간본 14회 vs '오픈소스SW 프로그램' 2회 → OSPO 번역이라 SW를 붙이지 않는다
  - '오픈소스 AI'        OSAID 정의 용어. 모델·데이터셋은 소프트웨어가 아니다
  - 코드블록 / URL / front matter 이외의 인용 블록 / 각주 정의의 문서 제목
"""
from __future__ import annotations
import re, sys, pathlib

KEEP = [
    '오픈소스 AI',            # OSAID 정의 용어
    '오픈소스 프로그램',       # OSPO(Open Source Program Office) 번역 — 발간본 용례
    '오픈소스 이니셔티브',     # Open Source Initiative 기관명
    '오픈소스 서밋',
]
SENT = '\x00KEEP%d\x00'


def protect(text: str) -> str:
    for i, k in enumerate(KEEP):
        text = text.replace(k, SENT % i)
    return text


def restore(text: str) -> str:
    for i, k in enumerate(KEEP):
        text = text.replace(SENT % i, k)
    return text


RE_ANCHOR_TARGET = re.compile(r'\]\((?:/[a-z-]+/)?#[^)]*\)')


def sub_term(text: str) -> str:
    """'오픈소스' → '오픈소스SW' (이미 SW가 붙은 것과 보호어는 건드리지 않는다).

    앵커 링크 대상(`](#슬러그)`)은 치환에서 제외한다. 슬러그는 헤딩에서 소문자화되어
    생성되므로('오픈소스SW 배포' → '오픈소스sw-배포'), 본문 규칙으로 대문자 SW를 넣으면
    실제 슬러그와 어긋나 링크가 죽는다. 앵커는 뒤에서 slug_map 으로 일괄 갱신한다.
    """
    anchors: list[str] = []

    def stash(m: re.Match) -> str:
        anchors.append(m.group(0))
        return '\x01A%d\x01' % (len(anchors) - 1)

    text = RE_ANCHOR_TARGET.sub(stash, text)
    text = protect(text)
    text = re.sub(r'오픈소스(?!SW)', '오픈소스SW', text)
    text = restore(text)
    for i, a in enumerate(anchors):
        text = text.replace('\x01A%d\x01' % i, a)
    return text


def slugify(t: str) -> str:
    t = re.sub(r'`([^`]*)`', r'\1', t)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'[*_]{1,3}', '', t)
    out = []
    for ch in t.strip().lower():
        if ch.isalnum() or ch in '-_':
            out.append(ch)
        elif ch.isspace():
            out.append('-')
    return ''.join(out)


def process(path: pathlib.Path, dry: bool = False):
    lines = path.read_text(encoding='utf-8').splitlines()

    # front matter 경계
    fm_end = 0
    start = 0
    while start < len(lines) and not lines[start].strip():
        start += 1
    if start < len(lines) and lines[start].strip() == '---':
        for i in range(start + 1, len(lines)):
            if lines[i].strip() == '---':
                fm_end = i
                break

    slug_map: dict[str, str] = {}   # 옛 슬러그 → 새 슬러그
    n_head = n_body = n_fm = 0
    in_fence = False
    out = []

    for idx, line in enumerate(lines):
        # front matter: title / linkTitle 만 치환
        if idx <= fm_end:
            m = re.match(r'^(title|linkTitle):\s*(.*)$', line)
            if m and '오픈소스' in line:
                new = sub_term(line)
                if new != line:
                    n_fm += 1
                out.append(new)
            else:
                out.append(line)
            continue

        if re.match(r'^\s*(```|~~~)', line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue

        # 각주 정의는 인용 문서 제목이므로 건드리지 않는다
        if re.match(r'^\[\^[^\]]+\]:', line):
            out.append(line)
            continue

        hm = re.match(r'^(#{2,6}\s+)(.*)$', line)
        if hm and '오픈소스' in hm.group(2):
            old_text = hm.group(2)
            new_text = sub_term(old_text)
            if new_text != old_text:
                slug_map[slugify(old_text)] = slugify(new_text)
                n_head += 1
            out.append(hm.group(1) + new_text)
            continue

        if '오픈소스' in line:
            new = sub_term(line)
            if new != line:
                n_body += 1
            out.append(new)
        else:
            out.append(line)

    text = '\n'.join(out) + '\n'

    # 앵커 링크 동기화 — 같은 파일 #슬러그, 타 섹션 /slug/#슬러그 모두
    n_anchor = 0
    for old, new in slug_map.items():
        if old == new:
            continue
        pat = re.compile(r'(\]\((?:/[a-z-]+/)?#)' + re.escape(old) + r'(\))')
        text, k = pat.subn(r'\g<1>' + new + r'\g<2>', text)
        n_anchor += k

    if not dry:
        path.write_text(text, encoding='utf-8')
    return n_fm, n_head, n_body, n_anchor, slug_map


if __name__ == '__main__':
    dry = '--dry' in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith('--')]
    all_map: dict[str, str] = {}
    print(f"{'파일':<28}{'FM':>4}{'헤딩':>6}{'본문':>6}{'앵커':>6}")
    for f in files:
        p = pathlib.Path(f)
        fm, h, b, a, m = process(p, dry)
        all_map.update(m)
        print(f"  {p.name:<26}{fm:>4}{h:>6}{b:>6}{a:>6}")
    print(f"\n변경된 헤딩 슬러그 {len(all_map)}개")
    if dry:
        print('(dry-run — 파일 미변경)')
