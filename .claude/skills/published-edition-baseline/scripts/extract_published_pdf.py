#!/usr/bin/env python3
"""발간본 PDF에서 본문 텍스트를 추출하고 조판 흔적을 정규화한다.

발간본은 조판된 결과물이라 그대로 추출하면 저장소 원고와 대조할 수 없다:
  - 문장이 조판 폭에 맞춰 중간에서 줄바꿈된다
  - 페이지마다 머리말·꼬리말·쪽번호가 본문에 섞인다
  - 각주가 페이지 하단에 `*` 기호로 흩어진다
이 스크립트는 그 셋을 정리해 문단 단위 텍스트로 되돌린다. 의미 판단은 하지 않는다 —
장 대응과 차이 판정은 reconciler 에이전트의 몫이다.

사용법:
    extract_published_pdf.py <pdf> [-o OUT.md] [--pages 1-180] [--keep-linebreaks]
                                   [--min-repeat N] [--report]

기본 동작:
    - pdftotext -layout 로 추출 (없으면 pypdf 폴백)
    - 페이지 전반에 반복 출현하는 짧은 줄을 머리말/꼬리말로 보고 제거
    - 쪽번호만 있는 줄 제거
    - 문장 중간 줄바꿈을 병합 (한글 문장은 종결어미 기준)
    - 페이지 경계를 <!-- page:N --> 주석으로 보존 (원문 대조 시 위치 추적용)
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

# 한국어 문어체 종결: '~한다.', '~이다.', '~된다.' 등 + 문장부호
RE_SENTENCE_END = re.compile(r"[.!?…”\"’')\]】」』]\s*$|다\.\s*$|음\.\s*$|임\.\s*$")
RE_PAGENUM_ONLY = re.compile(r"^\s*[-–—]?\s*\d{1,3}\s*[-–—]?\s*$")
RE_BULLET_START = re.compile(r"^\s*([•·▪◦‣∙\-*]|\d+[.)]|[가-힣][.)]|\([0-9가-힣]+\))\s+")
RE_HEADING_LIKE = re.compile(r"^\s*(제?\s*\d+\s*[장절]|[0-9]+(\.[0-9]+)*\s+\S)")


def extract_pages(pdf: Path, page_range: str | None) -> list[str]:
    """페이지별 텍스트 목록을 반환한다."""
    if shutil.which("pdftotext"):
        cmd = ["pdftotext", "-layout", "-enc", "UTF-8"]
        if page_range:
            first, _, last = page_range.partition("-")
            cmd += ["-f", first, "-l", last or first]
        cmd += [str(pdf), "-"]
        out = subprocess.run(cmd, capture_output=True, check=True).stdout.decode("utf-8", "replace")
        return out.split("\f")

    try:
        import pypdf
    except ImportError:
        print("pdftotext 도 pypdf 도 없다. brew install poppler 또는 pip install pypdf", file=sys.stderr)
        raise SystemExit(2)

    reader = pypdf.PdfReader(str(pdf))
    pages = [p.extract_text() or "" for p in reader.pages]
    if page_range:
        first, _, last = page_range.partition("-")
        lo = int(first) - 1
        hi = int(last) if last else int(first)
        pages = pages[lo:hi]
    return pages


def find_running_heads(pages: list[str], min_repeat: int) -> set[str]:
    """여러 페이지에 반복되는 짧은 줄 = 머리말/꼬리말."""
    counter: Counter[str] = Counter()
    for page in pages:
        lines = [ln.strip() for ln in page.splitlines() if ln.strip()]
        if not lines:
            continue
        # 페이지 상단 2줄과 하단 2줄만 후보로 본다 — 본문 문장이 우연히 반복되는 것을 피한다
        for ln in lines[:2] + lines[-2:]:
            if len(ln) <= 40:
                counter[ln] += 1
    return {ln for ln, c in counter.items() if c >= min_repeat}


def merge_wrapped_lines(lines: list[str]) -> list[str]:
    """조판 폭에 맞춰 끊긴 줄을 문단으로 되돌린다."""
    merged: list[str] = []
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            merged.append("")
            continue
        if not merged or not merged[-1].strip():
            merged.append(line.strip())
            continue
        prev = merged[-1]
        # 이어 붙이지 않는 경우: 이전 줄이 문장으로 끝났거나, 현재 줄이 새 항목/제목으로 시작
        if (RE_SENTENCE_END.search(prev)
                or RE_BULLET_START.match(line)
                or RE_HEADING_LIKE.match(line)
                or line.startswith("<!--")):
            merged.append(line.strip())
            continue
        # 조판 줄바꿈은 어절 경계에서 일어나므로 공백 하나로 잇는다.
        tail_token = prev.rsplit(None, 1)[-1] if prev.split() else ""
        in_url = tail_token.startswith("http") or "://" in tail_token
        if prev.endswith(("-", "/")) and (in_url or line[:1].isascii()):
            # URL 이 하이픈/슬래시에서 접힌 경우: 구분자를 살려 그대로 붙인다.
            # 영문 하이프네이션(`compli-` + `ance`)만 하이픈을 지운다 — URL 하이픈은 의미가 있다.
            if in_url or not re.search(r"[A-Za-z]-$", prev):
                merged[-1] = prev + line.strip()
            else:
                merged[-1] = prev[:-1] + line.strip()
        else:
            merged[-1] = prev + " " + line.strip()
    return merged


def repair_urls(text: str) -> str:
    """조판 과정에서 URL 안에 끼어든 공백을 제거한다.

    `https://example.org/blog/ossra-license-compliance- risks.html` 처럼
    하이픈이나 슬래시 뒤에서 줄이 접히면 각주 URL 이 통째로 죽는다.

    URL 뒤에 이어지는 한국어 문장까지 삼키면 본문이 망가지므로, 끊긴 자리가
    `-` 또는 `/` 이고 이어지는 조각이 ASCII 로 시작할 때만 붙인다.
    """
    pattern = re.compile(r"(https?://\S*[-/])[ \t]+(?=[A-Za-z0-9])")
    prev = None
    while prev != text:            # 한 URL 이 두 번 이상 접힌 경우까지 처리
        prev = text
        text = pattern.sub(r"\1", text)
    return text


def clean_page(text: str, heads: set[str]) -> list[str]:
    out: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            out.append("")
            continue
        if line in heads:
            continue
        if RE_PAGENUM_ONLY.match(line):
            continue
        out.append(line)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="발간본 PDF 본문 추출·정규화")
    ap.add_argument("pdf", type=Path)
    ap.add_argument("-o", "--out", type=Path, help="출력 마크다운 (생략 시 stdout)")
    ap.add_argument("--pages", help="페이지 범위, 예: 5-180")
    ap.add_argument("--keep-linebreaks", action="store_true",
                    help="줄바꿈 병합을 하지 않는다 (표·코드가 많은 구간 확인용)")
    ap.add_argument("--min-repeat", type=int, default=5,
                    help="머리말/꼬리말로 판정할 최소 반복 횟수 (기본 5)")
    ap.add_argument("--report", action="store_true", help="제거한 머리말/꼬리말 목록을 stderr 로 출력")
    args = ap.parse_args()

    if not args.pdf.is_file():
        print(f"파일 없음: {args.pdf}", file=sys.stderr)
        return 2

    pages = extract_pages(args.pdf, args.pages)
    heads = find_running_heads(pages, args.min_repeat)

    if args.report:
        print(f"[머리말/꼬리말 {len(heads)}종 제거]", file=sys.stderr)
        for h in sorted(heads):
            print(f"  - {h}", file=sys.stderr)

    chunks: list[str] = []
    for idx, page in enumerate(pages, start=1):
        lines = clean_page(page, heads)
        if not args.keep_linebreaks:
            lines = merge_wrapped_lines(lines)
        body = "\n".join(lines).strip()
        if not body:
            continue
        chunks.append(f"<!-- page:{idx} -->\n{body}")

    result = "\n\n".join(chunks) + "\n"
    # 빈 줄 3개 이상을 2개로 — 조판 여백이 그대로 넘어온 것을 정리
    result = re.sub(r"\n{3,}", "\n\n", result)
    result = repair_urls(result)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(result, encoding="utf-8")
        print(f"{args.out} 생성: {len(pages)}페이지 → {len(result.splitlines())}행, "
              f"{len(result)}자", file=sys.stderr)
    else:
        sys.stdout.write(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
