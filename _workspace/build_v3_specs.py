#!/usr/bin/env python3
"""PR #123 리뷰에서 지적된 삽화 10건의 재생성 인자를 만든다.

v2(_workspace/build_v2_specs.py)는 라벨을 본문에서 가져왔지만 구조 — 화살표 방향,
담당 주체 배정, 격자 축 개수 — 는 본문과 맞는지 확인하지 않았다. 리뷰어가 20장을
본문과 대조해 찾은 어긋남을 여기서 고친다. 각 항목의 지적 사유는 주석에 적는다.

간선·행·칸을 하나씩 명시하는 것이 핵심이다. "격자를 그려라" 수준으로 두면 모델이
빈 격자나 범례와 어긋나는 채움을 만들어 내고, 그것이 v2 결함의 대부분이었다.
"""
import pathlib

STYLE = (
"Clean minimal technical diagram for a corporate governance handbook. Flat vector illustration style, "
"no gradients, no 3D, no shadows. Restrained palette: deep navy (#1F3A5F) as primary, slate gray (#6B7A8F) as "
"secondary, soft teal (#3E9C9C) as accent, warm amber (#E8A33D) for emphasis only, on pure white background. "
"Thin uniform 2px strokes, generous white space, geometric shapes with slightly rounded corners. "
"Business-document aesthetic, legible at small size, printable in grayscale. No people, no faces, no photorealism, "
"no decorative flourishes, no logos or brand marks. "
"IMPORTANT STYLE ENFORCEMENT: draw solid filled shapes with 3px navy outlines, not a thin wireframe sketch. "
"Every label sits on an opaque white plate so no stroke crosses any glyph. "
"TEXT REQUIREMENT: this diagram carries Korean text labels and the labels are the point of the diagram. "
"Render every Korean label exactly as written below, in a clean sans-serif Hangul typeface, set horizontally, "
"in dark navy on white for maximum contrast, at a generous size so it stays readable when the image is scaled down. "
"Every Hangul syllable must be a real, correctly formed Korean character. Do not invent, distort, duplicate, "
"garble or omit characters. Do not translate the labels into English. Do not add any text that is not listed. "
"Lay the diagram out with enough spacing that no label overlaps another label or a stroke. ")

SPECS = [

# 지적: LGPL 을 MPL 과 함께 '파일 단위' 분기에 넣었다. 본문 라이선스 구분 표는
# LGPL=라이브러리 교체 가능성 보장 / MPL·EPL=수정 파일 단위 공개로 가른다.
# 지적: 본문이 인정하는 Copyleft 분기가 빠졌다.
# 대응: 좌→우 이진 트리로 바꿔 간선 교차를 없애고, 간선마다 예/아니오를 명시하고,
#       LGPL 과 MPL·EPL 을 한 잎 안에서 두 줄로 갈라 적는다.
("license-decision-tree-2026",
 "Composition: a left-to-right binary decision tree. Five navy diamond decision nodes fan out from a single root "
 "diamond at the left edge toward the right, and six rectangular leaf boxes stand in one vertical column along the "
 "right edge, all left aligned on a common vertical guide. Every connector is a right-angle elbow line and no two "
 "connectors cross. Every connector carries a small Korean answer word on an opaque white plate: 예 on the upper "
 "branch, 아니오 on the lower branch. "
 "Root diamond at the far left: 제품에 포함되어 배포되는가. Its 예 branch goes up to diamond A, its 아니오 branch goes "
 "down to diamond B. "
 "Diamond A: 제품 소스까지 공개할 수 있는가. Its 예 branch ends at leaf 1, its 아니오 branch ends at leaf 2. "
 "Diamond B: 채택 극대화가 최우선인가. Its 예 branch goes to diamond C, its 아니오 branch goes to diamond D. "
 "Diamond C: 공개 후 유지보수 계획이 있는가. Its 예 branch ends at leaf 3, its 아니오 branch ends at leaf 4. "
 "Diamond D: 변경 추적이 중요한가. Its 예 branch ends at leaf 5, its 아니오 branch ends at leaf 6. "
 "Leaf boxes, top to bottom on the right column, each filled solid and carrying two stacked lines of text — a heading "
 "line and a smaller qualifier line: "
 "leaf 1 heading GPL · AGPL, qualifier 카피레프트; "
 "leaf 2 heading MIT · Apache-2.0, qualifier 허용형 — 호환성 검토; "
 "leaf 3 heading MIT · Apache-2.0, qualifier 허용형; "
 "leaf 4 drawn with a dashed slate gray stroke, heading CC0 · Unlicense, qualifier 저작권 포기; "
 "leaf 5 heading GPL · AGPL, qualifier 카피레프트; "
 "leaf 6 heading LGPL / MPL · EPL, qualifier split onto two short lines reading LGPL 라이브러리 교체 보장 and "
 "MPL·EPL 수정 파일 단위. "
 "Leaf 6 is outlined in warm amber to mark that its two families differ. "
 "Text: only the five diamond questions, the repeated answer words 예 and 아니오, and the leaf headings and qualifiers "
 "listed above. "),

# 지적: 학습 코드와 배포 코드를 한 행으로 합쳐, 하위 두 등급도 학습 코드를 공개하는 것처럼 읽힌다.
# 지적: 캡션은 4단계인데 사내용 비공개 열을 더해 5열이 되었다.
# 대응: 범례를 4행(학습 데이터/학습 코드/배포 코드/가중치)으로 분리하고, 등급별 칸 상태를 하나씩 명시하고,
#       다섯 번째 블록을 삭제한다.
("ai-openness-tiers-g7",
 "Composition: exactly four blocks of equal width placed side by side as a staircase stepping down from left to right, "
 "separated by thin vertical dividers. There must be four blocks and no fifth block anywhere in the image. The leftmost "
 "block is the tallest; each block to its right is shorter. Each block carries a Korean tier name beneath it. "
 "Tier names, left to right: 데이터 공개 오픈소스 AI, 오픈소스 AI, 가중치 공개 AI, 가중치 제공 AI. "
 "Inside every block sits a vertical column of exactly four small squares of equal size, aligned across all four blocks "
 "so they read as four horizontal rows. A legend at the top left names the four rows from top to bottom: 학습 데이터, "
 "학습 코드, 배포 코드, 가중치. Thin slate gray guide lines run from each legend entry across to its row. "
 "Square states, specified row by row. Row 학습 데이터: block 1 filled solid navy, block 2 filled with a diagonal hatch, "
 "block 3 hollow with a thin outline, block 4 hollow with a thin outline. Row 학습 코드: block 1 filled solid navy, "
 "block 2 filled solid navy, block 3 hollow, block 4 hollow. Row 배포 코드: block 1 filled solid navy, block 2 filled "
 "solid navy, block 3 filled solid navy, block 4 filled solid navy. Row 가중치: block 1 filled solid navy, block 2 "
 "filled solid navy, block 3 filled solid navy, block 4 filled solid navy. "
 "A small legend key sits at the lower left with three sample squares: a solid navy square labelled 공개, a diagonally "
 "hatched square labelled 데이터 정보로 대체, a hollow square labelled 미공개. "
 "A small closed padlock outline in warm amber sits on top of block 4 only, with the warm amber label 사용 제한 beside it. "
 "Text: only the four tier names, the four row names, the three legend key labels and the amber label. "),

# 지적: 도식에만 있는 release.yml·scorecard.yml 이 표의 일부처럼 읽힌다.
# 지적: SECURITY.md 작성 주체가 표는 사무국(보안팀)+개발자인데 도식은 사무국이다.
# 지적: 파일 위치가 표는 '루트 또는 .github/' 인데 도식은 루트로 고정했다.
# 지적: 범례 배지 네 개가 모든 행에 붙어 범례가 무의미해졌다.
# 대응: 본문 표 11행을 그대로 옮긴 표 형태로 바꾸고, 행마다 배지를 하나씩 지정한다.
("repo-file-set-2026",
 "Composition: a clean three column table of eleven rows, drawn with thin uniform horizontal rules and two light "
 "vertical column separators, on generous white space. A header row sits on top with a heavier navy rule beneath it. "
 "Header cells, left to right: 파일, 등급, 위치. "
 "The 파일 column holds a file shape — a rectangle with one folded top right corner — followed by the file name in "
 "Latin letters. Immediately to the right of each file name sits exactly one small owner badge, never more than one. "
 "Rows, top to bottom, given as (file name / 등급 cell text / 위치 cell text / owner badge): "
 "(README.md / 필수 / 루트 / teal circle), "
 "(LICENSE / 필수 / 루트 / navy circle), "
 "(NOTICE / 조건부 필수 / 루트 / navy circle), "
 "(CONTRIBUTING.md / 필수 / 루트 또는 .github/ / teal circle), "
 "(CODE_OF_CONDUCT.md / 필수 / 루트 또는 .github/ / navy circle), "
 "(SECURITY.md / 필수 / 루트 또는 .github/ / half navy half teal circle), "
 "(GOVERNANCE.md / 권장 / 루트 / navy circle), "
 "(MAINTAINERS.md / 권장 / 루트 / teal circle), "
 "(SUPPORT.md / 권장 / 루트 또는 .github/ / teal circle), "
 "(CHANGELOG.md / 권장 / 루트 / teal circle), "
 "(CODEOWNERS / 권장 / .github/ / teal circle). "
 "The SECURITY.md row is outlined in warm amber and a short warm amber connector leaves its right edge to a warm amber "
 "note reading CRA 신고 채널. "
 "A legend sits below the table in clear white space with exactly three entries in one row: a navy circle labelled "
 "사무국, a teal circle labelled 개발자, a half navy half teal circle labelled 사무국+개발자. "
 "Text: only the three header cells, the eleven file names, the eleven 등급 cells, the eleven 위치 cells, the amber note "
 "and the three legend labels. Do not add any file or directory name that is not in the list above. "),

# 지적: 격자 6개 열이 전부 비어 캡션이 약속한 내용이 그림에 없다.
# 지적: 본문은 부서별 검토 관점만 서술하고 병렬 가능 여부·선행 의존·재검토 루프를 규정하지 않는다.
# 대응: 본문에 없는 순서 규범을 그리지 않는다. 부서와 검토 관점의 대응만 그린다. 캡션도 함께 바꾼다.
("release-review-matrix-2026",
 "Composition: a vertical list of seven wide rows on an aligned grid, each row a rounded rectangle split by one thin "
 "vertical divider into a narrow left cell and a wide right cell. The left cell is filled light slate gray and holds a "
 "large navy digit followed by the Korean team name. The right cell is filled white and holds one short Korean phrase "
 "naming what that team checks. Every right cell must contain its phrase; no cell is left empty. "
 "Rows, top to bottom, given as (digit / team name / check phrase): "
 "(1 / 특허팀 / 자사 특허 포함 여부), "
 "(2 / 상표팀 / 타사 상표권 침해 여부), "
 "(3 / 보안팀 / 기밀 정보와 보안 취약점), "
 "(4 / 오픈소스SW 검수팀 / 포함된 오픈소스SW 확인), "
 "(5 / 인사팀 / 근로계약·비밀유지 예외 인지), "
 "(6 / 홍보팀·마케팅팀 / 공개 후 알리기), "
 "(7 / 법무팀 / 법적 검토와 CLA 확인). "
 "Below the seven rows, set apart in clear white space, sits one wide note box with a dashed slate gray stroke reading "
 "조직 사정에 따라 부서가 늘거나 줄 수 있다. "
 "Do not draw any arrow, brace, timeline, ordering mark or dependency line between the rows. The rows are a list, "
 "not a sequence. "
 "Text: only the seven digits, the seven team names, the seven check phrases and the one dashed note. "),

# 지적: OSI 비승인 라이선스가 본문에는 다섯인데 도식에는 셋만 있고 '등' 표시도 없다.
# 지적: 강한 카피레프트(GPL)와 네트워크 카피레프트(AGPL) 구간 색이 육안으로 같다.
# 대응: 다섯 개를 모두 적고, AGPL 구간에 대각 해칭을 얹어 회색조 인쇄에서도 갈리게 한다.
("license-spectrum-2026",
 "Composition: a horizontal spectrum bar divided into four adjacent segments of equal height running left to right, "
 "with a thin arrow beneath the whole bar pointing right. Above each segment sits a Korean heading; below each segment "
 "sits a short vertical list of license names in Latin letters. "
 "Segment 1 filled soft teal, heading 허용형, list: MIT / BSD / Apache-2.0. "
 "Segment 2 filled light slate gray, heading 약한 카피레프트, list: LGPL / MPL / EPL. "
 "Segment 3 filled medium navy, heading 강한 카피레프트, list: GPL. "
 "Segment 4 filled the darkest navy in the image and additionally overlaid with a clearly visible diagonal hatch so it "
 "is distinguishable from segment 3 even when printed in grayscale, heading 네트워크 카피레프트, list: AGPL. "
 "Under the arrow, at the left end the label 의무 적음 and at the right end the label 의무 많음. "
 "Detached at the far right beyond a clear gap, outside and below the spectrum bar, stands a separate block drawn with "
 "a dashed slate gray stroke, headed OSI 비승인 소스 공개형, listing all five names on separate lines: BUSL / SSPL / "
 "Elastic License / PolyForm / FSL, with a warm amber note beneath it reading 오픈소스SW가 아니다. "
 "Text: only the four headings, the license names, the two end labels, the detached block heading and the amber note. "),

# 지적: 8번 '신청서 확인'이 유관부서로 배정됐으나 본문은 오픈소스SW 담당자가 챙긴다고 적는다.
# 지적: 10번 '공개 준비' 산출물의 작성 주체는 본문 표에서 모두 사무국 또는 사무국+개발자다.
# 대응: 담당 밴드를 단계별로 하나씩 지정한다.
("release-journey-2026",
 "Composition: a left-to-right row of eleven slim rounded rectangular stages of equal height, evenly spaced across the "
 "full width, connected by thin arrows. Each stage carries its navy digit and a very short Korean label set on two lines "
 "inside the box. Stage 6 and stage 11 are outlined in warm amber and drawn slightly taller. "
 "Stages: (1 / 검토 주체), (2 / 역할·권한), (3 / 공개 시점), (4 / 공개 위치), (5 / 라이선스), (6 / CRA 지위), "
 "(7 / 공개 신청서), (8 / 신청서 확인), (9 / 검토), (10 / 공개 준비), (11 / 공개). "
 "Directly above the row runs an owner lane made of contiguous bars, one bar per group of consecutive stages, each bar "
 "spanning exactly the stages listed and carrying its Korean owner label centred on it. Bars, left to right: "
 "a solid navy bar spanning stages 1 to 6 labelled 사무국; "
 "a soft teal bar spanning stage 7 only labelled 개발자; "
 "a solid navy bar spanning stage 8 only labelled 사무국; "
 "a light slate gray bar spanning stage 9 only labelled 유관부서; "
 "a bar spanning stage 10 only, split diagonally into navy and soft teal halves, labelled 사무국+개발자; "
 "a solid navy bar spanning stage 11 only labelled 사무국. "
 "Every bar must carry its label and no bar may span stages other than the ones listed. "
 "Directly below the row runs a second lane of eleven small document shapes, each a rectangle with one folded top right "
 "corner, and the lane carries the single label 산출물 at its left end. "
 "Text: only the eleven digits, the eleven stage labels, the six owner labels and the word 산출물. "),

# 지적: Apache-2.0 모델에서 나가는 경로의 종착 박스에도 의무 네 항목이 그대로 붙어, 순수 Apache-2.0 조합도
#       파생하면 자동으로 의무가 생기는 것처럼 읽힌다. 본문 표는 Apache-2.0 + Apache-2.0 → 제한 조항 없음이다.
# 지적: '병합하면 조건이 사라진다는 오해' 옆 주황 점선 상자가 비어 있다.
# 대응: 순수 Apache-2.0 경로를 태그 없는 별도 갈래로 분리하고, 점선 상자 안에 라벨을 반드시 넣는다.
("model-license-inheritance",
 "Composition: a top-down genealogy graph three levels deep, rectangles for artifacts connected by thin arrows that "
 "never cross, small tag shapes for obligations. "
 "Top level: two parent rectangles side by side. The left parent is filled solid navy, labelled 제한 있는 베이스 모델, "
 "and carries a row of four small filled navy tags along its bottom edge labelled 라이선스 사본, NOTICE, 명칭 규칙, "
 "AUP 전가. The right parent is filled soft teal, labelled Apache-2.0 모델, and carries no tags at all. "
 "Middle level: three result rectangles in one row. "
 "Left result labelled 파인튜닝 receives one arrow from the left parent only and carries the same four navy tags. "
 "Middle result labelled 병합 receives two arrows, one from each parent, and carries the same four navy tags plus a "
 "short navy caption beneath it reading 제한이 섞이면 승계된다. "
 "Right result labelled 증류 receives one arrow from the right parent only, is filled soft teal, carries no tags, and "
 "has a short soft teal caption beneath it reading Apache-2.0 그대로 — 제한 조항 없음. "
 "Bottom level: one wide terminal rectangle labelled 최종 배포물 that receives arrows from the 파인튜닝 and 병합 results "
 "and carries the four navy tags plus one extra warm amber tag at its right end labelled 지역 제한. The 증류 result does "
 "not connect to it; instead a separate short arrow leaves 증류 downward to its own small soft teal terminal rectangle "
 "labelled 제한 없는 배포물. "
 "To the right of the whole graph, set apart in clear white space and joined by one thin dashed line, sits a note box "
 "with a dashed warm amber stroke. Inside that box, and it must not be left empty, sits one warm amber tag drawn faded "
 "with a diagonal strike-through line across it, and directly beneath that tag the Korean text 병합하면 조건이 "
 "사라진다는 오해 set on two lines. "
 "Text: only the labels and captions listed above. "),

# 지적: origin 리모트가 4번 '동기화'에 연결됐다. 본문 코드 블록에서 3·4번은 upstream 을 참조하고
#       origin 은 6번 Push 에서 처음 등장한다.
# 대응: upstream 은 1번과 4번에, origin 은 6번에 연결한다.
("prflow-2026",
 "Composition: a left-to-right sequence of seven rounded rectangular stages connected by thin arrows, each filled solid "
 "and carrying its navy digit and a short label. "
 "Stages: (1 / Fork), (2 / Clone), (3 / 브랜치 생성), (4 / 동기화), (5 / Commit), (6 / Push), (7 / Pull Request). "
 "Above the row sit exactly two small rounded rectangles with a heavier navy outline and a light fill, each labelled "
 "with a repository name. The rectangle labelled upstream sits above the gap between stage 1 and stage 4 and is joined "
 "by two thin vertical lines, one down to stage 1 and one down to stage 4. The rectangle labelled origin sits above "
 "stage 6 and is joined by exactly one thin vertical line down to stage 6. No line may run from origin to stage 4. "
 "One thin soft teal curved arrow returns from stage 4 back to stage 3 below the main sequence, labelled 반복. "
 "Stage 7 is outlined in warm amber and a short warm amber label 리뷰 요청 sits beneath it. "
 "Text: only the seven digits, the seven stage labels, the two repository names, the word 반복 and the amber label. "),

# 지적: 선별 격자의 축이 셋인데 본문은 판정 변수를 넷으로 규정한다. '공격 자동화 가능성'이 빠졌다.
# 지적: 조치 출력의 '버전 상향'이 본문의 '버전 고정'과 다르다. 본문 조치는 패치·버전 고정·완화·수용이다.
# 대응: 축을 넷으로 만들어 4x4 열여섯 칸을 채우고, 칸마다 기한 등급을 지정한다.
("vulnerability-triage-pipeline",
 "Composition: a left-to-right sequence of five rounded rectangular stages connected by thin arrows, each filled solid "
 "and carrying its navy digit and a Korean stage name. "
 "Stages: (1 / 탐지), (2 / 선별), (3 / 조치), (4 / 검증), (5 / 기록). "
 "From stage 1 a short downward arrow leads to one small box with a dashed stroke labelled SBOM 상시 보유. "
 "From stage 2 a pair of thin guide lines opens downward and widens into an enlarged flat grid of exactly sixteen equal "
 "square cells arranged as four rows by four columns. Two axis labels sit above the grid describing its columns, stacked "
 "on two lines and reading 인터넷 노출 and KEV 등재. Two axis labels sit along the left edge describing its rows, stacked "
 "and reading 공격 자동화 and 기술적 영향. Every one of the sixteen cells is filled; none is left blank. "
 "Cell fills, given row by row from the top row to the bottom row and within each row from the left column to the right "
 "column, using four fill levels named here as darkest, dark, mid and lightest: "
 "row 1 — darkest, darkest, darkest, mid; "
 "row 2 — darkest, dark, dark, mid; "
 "row 3 — darkest, dark, dark, lightest; "
 "row 4 — dark, mid, dark, lightest. "
 "To the right of the grid sits a vertical legend key of four sample squares with Korean labels, top to bottom: darkest "
 "labelled 3일, dark labelled 14일, mid labelled 60일, lightest labelled 업그레이드 시. "
 "Stage 3 has four small boxes stacked directly beneath it labelled, top to bottom: 패치, 버전 고정, 완화, 수용. "
 "Text: only the five digits, the five stage names, the one dashed box label, the four axis labels, the four legend "
 "labels and the four boxes under stage 3. "),

# 지적: '생산 측'으로 적혀 있으나 본문은 '생성 측'을 쓴다(원청이 소비 측, 하청이 생성 측).
# 대응: 용어만 교체하고 나머지 구조는 유지한다.
("provenance-verification-flow",
 "Composition: a row of six rounded rectangular stages connected left to right by thin arrows, each filled solid and "
 "carrying its navy digit and a Korean stage name. The row is cut in the middle by a thin vertical slate gray divider "
 "into a left group of three stages labelled 생성 측 above them and a right group of three stages labelled 소비 측 above "
 "them, joined across the divider by one long arrow tagged OIDC. The left group label must read 생성 측 and must not "
 "read 생산 측. "
 "Stages: (1 / 빌드), (2 / 서명 생성), (3 / 어테스테이션 발행), (4 / 아티팩트 수신), (5 / 신원 검증), (6 / 설치). "
 "In the left group a small circular seal shape hangs below stage 3 and a long horizontal ledger bar divided into narrow "
 "slots sits beneath that seal, labelled 투명성 로그. "
 "In the right group stage 5 is drawn noticeably larger than its neighbours and outlined in warm amber. Two arrows leave "
 "it to the right, one continuing straight to a terminal box labelled 통과 and one bending downward to a terminal box "
 "marked with a short crossing bar labelled 빌드 중단. A small warm amber triangle sits just above stage 5 with the "
 "warm amber note 신원 검증 없는 서명 확인은 무의미하다 beside it. "
 "Above the left group runs a thin ascending three step bar, each step tagged in navy with SLSA L1, SLSA L2 and SLSA L3 "
 "from left to right. "
 "Text: only the six digits, the six stage names, the two group labels, the tag OIDC, the ledger label, the two terminal "
 "labels, the one amber note and the three SLSA tags. "),
]

assert len(SPECS) == 10, f"기대 10건, 실제 {len(SPECS)}건"
names = [n for n, _ in SPECS]
assert len(set(names)) == len(names), "출력 파일명이 겹치면 마지막 작업만 살아남는다"

out = pathlib.Path("_workspace/07f_gen_args_v3.txt")
lines = []
for name, body in SPECS:
    prompt = STYLE + body
    assert "::" not in prompt, f"프롬프트에 구분자 '::' 가 들어가면 파싱이 깨진다: {name}"
    lines.append(f"{prompt}::{name}.png")
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"{out} — {len(lines)}건")
for name, body in SPECS:
    print(f"  {name:34} {len(STYLE) + len(body):5}자")
