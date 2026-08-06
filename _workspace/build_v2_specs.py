#!/usr/bin/env python3
"""한글 라벨을 넣은 삽화 20건의 생성 인자를 만든다.

원본(_workspace/07_illustration_specs.json)의 구도는 유지하고, 텍스트 회피 전략
(none/numbers-only/latin-only)을 폐기해 본문에서 확인한 한글 라벨을 넣는다.
라벨은 모두 원고에 실재하는 문구에서 가져온다.
"""
import pathlib

STYLE = (
"Clean minimal technical diagram for a corporate governance handbook. Flat vector illustration style, "
"no gradients, no 3D, no shadows. Restrained palette: deep navy (#1F3A5F) as primary, slate gray (#6B7A8F) as "
"secondary, soft teal (#3E9C9C) as accent, warm amber (#E8A33D) for emphasis only, on pure white background. "
"Thin uniform 2px strokes, generous white space, geometric shapes with slightly rounded corners. "
"Business-document aesthetic, legible at small size, printable in grayscale. No people, no faces, no photorealism, "
"no decorative flourishes, no logos or brand marks. "
"TEXT REQUIREMENT: this diagram carries Korean text labels and the labels are the point of the diagram. "
"Render every Korean label exactly as written below, in a clean sans-serif Hangul typeface, set horizontally, "
"in dark navy on white for maximum contrast, at a generous size so it stays readable when the image is scaled down. "
"Every Hangul syllable must be a real, correctly formed Korean character. Do not invent, distort, duplicate, "
"garble or omit characters. Do not translate the labels into English. Do not add any text that is not listed. "
"Lay the diagram out with enough spacing that no label overlaps another label or a stroke. ")

SPECS = [
("guide-structure-map-2026",
 "Composition: a vertical stack of five wide rows on an aligned grid, drawn as nested rectangles two levels deep. "
 "Each row carries a large navy digit at its left edge, reading 1 to 5 from top to bottom, and a Korean chapter title "
 "next to that digit. Rows 1, 2, 3 and 5 are each split into two equal child boxes side by side with a thin vertical "
 "divider. Row 4 is one single undivided box spanning the full width. "
 "Row titles: (1 / 오픈소스SW 사용하기), (2 / 오픈소스SW 기여하기), (3 / 오픈소스SW 공개하기), (4 / OSPO), "
 "(5 / AI와 오픈소스SW). "
 "In rows 1, 2, 3 and 5 the left child box is labelled 기업 편 and the right child box is labelled 개발자 편. "
 "Row 5 sits at the bottom, is outlined in soft teal, and four thin soft teal connector lines rise from it along the "
 "right margin to rows 1, 2, 3 and 4. A short soft teal label 모든 장을 가로지른다 sits beside those connector lines. "
 "Text: only the five digits, the five chapter titles, the repeated labels 기업 편 and 개발자 편, and the single "
 "soft teal note. "),

("governance-maturity-2026",
 "Composition: a left-to-right sequence of five rounded rectangular stages connected by thin arrows, rising like a "
 "shallow staircase from lower left to upper right, each box set slightly higher than the previous one and filled a "
 "step darker, from very light slate gray at stage 1 to solid navy at stage 5. Each box carries its navy digit and a "
 "Korean stage name. Stage 5 is outlined in warm amber. "
 "Stages: (1 / 사용), (2 / 컴플라이언스), (3 / 보안·공급망), (4 / 기여), (5 / 공개·OSPO). "
 "Below the whole sequence runs one continuous soft teal band aligned with all five stages, joined to each stage by a "
 "short vertical tick, labelled AI 자산 거버넌스 at its left end. A short slate gray note under the band reads "
 "같은 단계 위에 얹는다. "
 "Text: only the five digits, the five stage names, the band label and the one note. "),

("license-obligation-decision-tree",
 "Composition: four navy diamond decision nodes in one row along the horizontal centre line, connected left to right "
 "by thin arrows, with branches fanning downward into small rounded boxes on an aligned baseline. No branch lines cross. "
 "Each diamond carries its navy digit above it and a short Korean question inside or just below it. "
 "Diamond 1: 전달이 있는가. It sends one short downward arrow to a single small box with a dashed slate gray stroke "
 "labelled 의무 없음. "
 "Diamond 2: 라이선스 계열. It fans downward into five small boxes labelled, left to right: permissive, LGPL, MPL·EPL, "
 "GPL, AGPL. "
 "Diamond 3: 결합 방식. It fans downward into seven small boxes labelled, left to right: 정적 링크, 동적 링크, "
 "별도 프로세스, 컨테이너 동봉, 사이드카, 네트워크 API, 모델 가중치. "
 "Diamond 4: 파생저작물인가. It fans downward into three small boxes filled in increasing darkness labelled, left to "
 "right: 해당 없음, 판단 필요, 해당. "
 "At the far right edge three terminal boxes are stacked vertically with increasing fill darkness, labelled top to "
 "bottom: 고지만, 조건부 공개, 전체 소스 공개. The bottom one is outlined in warm amber. Each receives a thin arrow "
 "curving in from the branch boxes. "
 "A thin slate gray horizontal rule runs across the bottom with one long bar beneath it labelled "
 "저작권 고지와 라이선스 사본 첨부는 모든 경우에 적용된다. "
 "Text: only the four digits, the four diamond questions, the branch box labels, the three terminal labels and the "
 "one bottom bar sentence. "),

("regulation-timeline-2026",
 "Composition: a horizontal timeline. One thick navy horizontal axis runs across the middle of a wide landscape canvas, "
 "with three tick marks labelled 2026, 2027 and 2028 placed under the axis at their correct positions. Events sit above "
 "and below the axis, each joined to its exact date position on the axis by a short thin vertical stem ending in a small "
 "filled circle. Events are spaced proportionally to their dates, not evenly. Each event shows its date on one line and "
 "its Korean label on the line below. "
 "Above the axis in navy, left to right: (2026-08-02 / EU AI Act 투명성 의무), (2026-09-11 / EU CRA 보고 의무), "
 "(2026-12-02 / EU AI Act 금지 관행), (2026-12-09 / EU 제조물책임지침), (2027-12-02 / EU AI Act 고위험 Annex III), "
 "(2027-12-11 / EU CRA 전면 적용), (2028-08-02 / EU AI Act 고위험 Annex I). "
 "Below the axis in soft teal, left to right: (2026년 / 보안적합성 검증 SBOM 제출), (2027년 / 공공 정보화사업 SBOM 제출), "
 "(2028년 / 개발환경 보안 점검). "
 "A small legend in the top left corner: a navy square labelled EU, a soft teal square labelled 국내. "
 "Text: only the labels, dates, years and the two legend words. "),

("sbom-lifecycle-pipeline",
 "Composition: a left-to-right sequence of four rounded rectangular stages connected by thin arrows, each carrying its "
 "navy digit and a Korean stage name. The uppercase word SBOM in navy sits centred above the whole pipeline. "
 "Stages: (1 / 생성), (2 / 보관), (3 / 검증), (4 / 소비). "
 "Stage 1 splits into two parallel small boxes stacked vertically labelled 소스 기반 and 바이너리 기반, whose outputs "
 "merge into a pair of overlapping circles. The crescent lying outside the overlap is filled warm amber and labelled "
 "차집합 — 누락 컴포넌트. "
 "Stage 2 is a single box with a small circular seal shape at its lower right corner labelled 서명. "
 "Stage 3 is preceded by a narrow vertical gate drawn as two short parallel navy bars standing across the incoming "
 "arrow, labelled CI 게이트. "
 "Stage 4 fans out to the right into four small boxes stacked vertically labelled, top to bottom: 취약점 조인, "
 "라이선스 점검, 규제 제출, VEX. "
 "One thin soft teal curved arrow returns from stage 4 back to stage 3 below the main sequence, labelled 신규 CVE 재평가. "
 "Text: only the word SBOM, the four digits, the four stage names and the labels listed above. "),

("vulnerability-triage-pipeline",
 "Composition: a left-to-right sequence of five rounded rectangular stages connected by thin arrows, each carrying its "
 "navy digit and a Korean stage name. "
 "Stages: (1 / 탐지), (2 / 선별), (3 / 조치), (4 / 검증), (5 / 기록). "
 "From stage 1 a short downward arrow leads to one small box with a dashed stroke labelled SBOM 상시 보유. "
 "From stage 2 a pair of thin guide lines opens downward and widens into an enlarged flat grid of eight equal square "
 "cells arranged as two rows of four, filled in four steps of increasing darkness from very light slate gray at the far "
 "right of the lower row to solid navy at the far left of the upper row. Three short axis arrows run along the top edge, "
 "the left edge and the lower left corner of that grid, labelled 인터넷 노출, KEV 등재 and 기술적 영향. "
 "Three small navy tags sit beside the grid marking the response deadlines, reading 3일, 14일 and 60일, the 3일 tag "
 "beside the darkest cell and the 60일 tag beside the lightest cell. "
 "Stage 3 has four small boxes stacked directly beneath it labelled, top to bottom: 패치 적용, 버전 상향, 우회 설정, "
 "VEX 기록. "
 "Text: only the five digits, the five stage names, the one dashed box label, the three axis labels, the three day "
 "tags and the four boxes under stage 3. "),

("provenance-verification-flow",
 "Composition: a row of six rounded rectangular stages connected left to right by thin arrows, each carrying its navy "
 "digit and a Korean stage name. The row is cut in the middle by a thin vertical slate gray divider into a left group of "
 "three stages labelled 생산 측 above them and a right group of three stages labelled 소비 측 above them, joined across "
 "the divider by one long arrow tagged OIDC. "
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

("si-supply-chain-sbom-flow",
 "Composition: four wide horizontal bands stacked vertically with equal gaps, aligned on a common grid, each labelled "
 "with a Korean tier name at its left inside edge. The topmost band has the heaviest stroke and the lightest fill; each "
 "band below has a lighter stroke and a slightly darker fill. "
 "Bands, top to bottom: 발주처, 원청, 1차 협력사, 2차 협력사. "
 "In every gap between two adjacent bands sits a small square gate symbol on the centre line drawn as a square divided "
 "into three equal horizontal slots, labelled 검수 게이트. "
 "On the left side of the stack three arrows run upward, one across each gap, labelled 산출물 at the top and tagged SBOM "
 "and VEX on the two upper arrows. "
 "On the right side three arrows run downward, one across each gap, all with a dashed stroke, labelled 보안 요구사항. "
 "One continuous warm amber line starts at the bottom band, passes through the centre of every gate symbol and reaches "
 "the top band, growing slightly thicker at each level, labelled 컴포넌트 추적 at its lower end. "
 "Text: only the four band names, the words SBOM and VEX, the repeated gate label, the two side labels and the amber "
 "line label. "),

("license-spectrum-2026",
 "Composition: a horizontal spectrum bar divided into four adjacent segments of equal height running left to right, with "
 "a thin arrow beneath the whole bar pointing right. Above each segment sits a Korean heading; below each segment sits a "
 "short vertical list of license names in Latin letters. Fill darkens from left to right. "
 "Segment 1 (soft teal) heading 허용형, list: MIT / Apache-2.0. "
 "Segment 2 (slate gray) heading 약한 카피레프트, list: LGPL / MPL / EPL. "
 "Segment 3 (medium navy) heading 강한 카피레프트, list: GPL. "
 "Segment 4 (deep navy) heading 네트워크 카피레프트, list: AGPL. "
 "Under the arrow, at the left end the label 의무 적음 and at the right end the label 의무 많음. "
 "Detached at the far right beyond a clear gap, outside and below the spectrum bar, stands a separate block drawn with a "
 "dashed slate gray stroke, headed OSI 비승인 소스 공개형, listing BUSL / SSPL / Elastic License, with a warm amber note "
 "beneath it reading 오픈소스SW가 아니다. "
 "Text: only the four headings, the license names, the two end labels, the detached block heading and the amber note. "),

("prflow-2026",
 "Composition: a left-to-right sequence of seven rounded rectangular stages connected by thin arrows, each carrying its "
 "navy digit and a short label. "
 "Stages: (1 / Fork), (2 / Clone), (3 / 브랜치 생성), (4 / 동기화), (5 / Commit), (6 / Push), (7 / Pull Request). "
 "Above the row sit two small rounded rectangles with a heavier navy outline and a light fill: one above stage 1 labelled "
 "upstream, one above stage 4 labelled origin, each joined to its stage by a thin vertical line. "
 "One thin soft teal curved arrow returns from stage 4 back to stage 3 below the main sequence, labelled 반복. "
 "Stage 7 is outlined in warm amber and a short warm amber label 리뷰 요청 sits beneath it. "
 "Text: only the seven digits, the seven stage labels, the two repository names, the word 반복 and the amber label. "),

("release-journey-2026",
 "Composition: a left-to-right row of eleven slim rounded rectangular stages of equal height, evenly spaced across the "
 "full width, connected by thin arrows. Each stage carries its navy digit and a very short Korean label set on two lines "
 "inside the box. Stage 6 and stage 11 are outlined in warm amber and drawn slightly taller. "
 "Stages: (1 / 검토 주체), (2 / 역할·권한), (3 / 공개 시점), (4 / 공개 위치), (5 / 라이선스), (6 / CRA 지위), "
 "(7 / 공개 신청서), (8 / 신청서 확인), (9 / 검토), (10 / 공개 준비), (11 / 공개). "
 "Directly above the row runs a lane of grouped squares using three distinct fills to mark the owner of consecutive "
 "stages, with neighbouring squares of the same fill merged into one longer square: the group over stages 1 to 6 is "
 "solid navy and labelled 사무국, the group over stage 7 is soft teal and labelled 개발자, the group over stages 8 to 11 "
 "is light slate gray and labelled 유관부서. "
 "Directly below the row runs a second lane of eleven small document shapes, each a rectangle with one folded top right "
 "corner, and the lane carries the single label 산출물 at its left end. "
 "Text: only the eleven digits, the eleven stage labels, the three owner labels and the word 산출물. "),

("release-review-matrix-2026",
 "Composition: a rectangular matrix grid of seven rows and five columns drawn with thin uniform strokes, with a long "
 "thin left-to-right arrow running beneath the grid labelled 검토 일정 to set the reading direction. Column separators "
 "are drawn slightly heavier than row separators. "
 "A narrow index column at the far left holds seven navy digits 1 to 7, each followed by the Korean team name, reading "
 "top to bottom: 1 특허팀, 2 상표팀, 3 보안팀, 4 오픈소스SW 검수팀, 5 인사팀, 6 홍보팀, 7 법무팀. "
 "The five columns to the right of the index column are empty. "
 "Rows 1 to 5 are bracketed together at the left outer margin by one tall vertical brace labelled 병렬 검토 가능. "
 "Two long thin navy arrows run outside the grid on the right side, one curving from the right edge of row 2 down to the "
 "left edge of row 6 and one curving from the right edge of row 3 down to the left edge of row 7, sharing one label "
 "선행 검토 필요. "
 "One warm amber arrow curves backward beneath the grid from the last column to the first column labelled 보완 후 재검토. "
 "Text: only the seven digits, the seven team names, and the four labels 검토 일정, 병렬 검토 가능, 선행 검토 필요 and "
 "보완 후 재검토. "),

("contributor-ladder-2026",
 "Composition: an ascending staircase of five steps rising from lower left to upper right, each step a rounded rectangle "
 "of equal size connected by short upward arrows, the fill darkening from very light slate gray at step 1 to solid navy "
 "at step 5. Each step carries its navy digit and a role name in Latin letters. "
 "Steps: (1 / Read), (2 / Triage), (3 / Write), (4 / Maintain), (5 / Admin). "
 "Beside every step on its left sits one small rounded tag, and the column of tags carries the single heading 승격 기준 "
 "above it. Beside every step on its right sits one small key shape drawn as a circle with a short rectangular stem, the "
 "keys growing slightly larger from step 1 to step 5, and the column of keys carries the single heading 권한 범위 above it. "
 "One detached step sits to the right of and slightly below step 5, drawn with a dashed slate gray stroke and labelled "
 "이머리터스. Two warm amber arrows point into it, one leaving step 5 and one leaving step 4, sharing the warm amber "
 "label 권한 회수. "
 "Two small document shapes, rectangles with one folded top right corner, sit together at the lower right corner "
 "labelled GOVERNANCE.md and MAINTAINERS.md, joined by thin light lines to all five steps. "
 "Text: only the five digits, the five role names, the two column headings, the detached step label, the amber label and "
 "the two file names. "),

("license-decision-tree-2026",
 "Composition: a top-down decision tree with five navy diamond decision nodes descending down the centre of the image on "
 "one vertical spine, connected by thin downward arrows, with side branches leaving left and right. Each diamond carries "
 "its navy digit and a short Korean question. Seven leaf boxes stand in a single row along the bottom edge, connected "
 "upward by thin lines that never cross. "
 "Diamonds, top to bottom: (1 / 제품에 포함되어 배포되는가), (2 / 특허 보호가 필요한가), (3 / 채택 극대화가 최우선인가), "
 "(4 / 유지보수 계획이 있는가), (5 / 변경 추적이 중요한가). "
 "Leaf boxes, left to right, each carrying a navy label: MIT, Apache-2.0, MPL, LGPL, GPL, AGPL, and a seventh leaf box "
 "at the far right drawn with a dashed stroke labelled CC0 · Unlicense. "
 "One extra branch leaves the right side of the spine at diamond 2 and ends in a separate box outlined in warm amber, "
 "standing apart from the tree with clear white space around it, labelled 이중 라이선스. "
 "Text: only the five digits, the five questions, the seven leaf labels and the one amber box label. "),

("repo-file-set-2026",
 "Composition: a top-down hierarchy of nested rectangles three levels deep on an aligned grid, with clear inset margins. "
 "One large outer rectangle with a heavy navy stroke is labelled 루트 at its top left corner. "
 "Inside it near the top runs a vertical list of file shapes, each a rectangle with one folded top right corner, all left "
 "aligned on a common indent guide, labelled top to bottom: README.md, LICENSE, NOTICE, CONTRIBUTING.md, "
 "CODE_OF_CONDUCT.md, SECURITY.md, GOVERNANCE.md, MAINTAINERS.md, SUPPORT.md, CHANGELOG.md. "
 "Below that list, still inside the outer rectangle, sits a second nested rectangle with a lighter fill and stroke "
 "labelled .github/ holding five file shapes labelled CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, SUPPORT.md, "
 "CODEOWNERS, and one further rectangle inset deeper labelled workflows/ holding two file shapes labelled "
 "release.yml and scorecard.yml. "
 "The file shape SECURITY.md in the root list is outlined in warm amber and a short warm amber connector leaves it "
 "toward the right margin ending at a warm amber note reading CRA 신고 채널. "
 "A small legend sits at the lower right in clear white space: a filled navy dot labelled 필수, a hollow navy ring "
 "labelled 권장, a filled soft teal square labelled 사무국, a hollow soft teal square labelled 개발자. Every file shape "
 "carries two matching small badges on its right side. "
 "Text: only the file and directory names, the word 루트, the amber note and the four legend labels. "),

("release-pipeline-2026",
 "Composition: a left-to-right sequence of seven rounded rectangular stages connected by thin arrows, each carrying its "
 "navy digit and a Korean stage name. "
 "At the far left, before stage 1, stands a tall narrow gate rectangle outlined in warm amber containing three short "
 "stacked bars, labelled 릴리스 승인, feeding by one arrow into stage 1. "
 "Stages: (1 / 태그 푸시), (2 / CI 트리거), (3 / 빌드), (4 / SBOM 생성), (5 / 서명), (6 / 프로비넌스 발행), (7 / 게시). "
 "Above stage 5 and above stage 6 sits a small key shape drawn as a circle with a short rectangular stem, each joined to "
 "its stage by a short dashed vertical line, with a small hourglass shape beside each key, sharing the single label "
 "단기 자격증명. "
 "Below stages 4, 5 and 6 runs a separate lane of three small boxes on a thin slate gray rule, each joined upward to its "
 "stage by a thin line, labelled left to right SBOM 첨부, 서명 검증, 빌더 신원, and the lane carries the heading "
 "채택자 검증 증거 at its left end. "
 "Text: only the seven digits, the seven stage names, the gate label, the credential label, the three lane box labels "
 "and the lane heading. "),

("ai-asset-governance-integration",
 "Composition: a left-to-right sequence of five rounded rectangular stages connected by thin arrows, forming a single "
 "shared spine drawn with the heaviest stroke in the image. Each stage carries its navy digit and a Korean stage name. "
 "Stages: (1 / 반입 승인), (2 / 대장 등록), (3 / SBOM), (4 / 고지), (5 / 배포 승인). "
 "From every stage box two short vertical connectors leave, one upward and one downward. The upward connectors reach an "
 "upper lane of five small boxes with a light slate gray fill, and that lane carries the single heading "
 "소프트웨어 컴포넌트 at its left end. The downward connectors reach a lower lane of five small boxes with a soft teal "
 "tint fill, and that lane carries the single heading AI 모델·데이터셋 at its left end. Both lanes occupy exactly the "
 "same five column positions as the spine. "
 "Below everything runs one separate wide band outlined in warm amber divided into three equal cells labelled left to "
 "right: 모델 버전 단위 라이선스 기록, 데이터셋 독립 자산 등록, 스니펫 매칭 게이트. The band carries the heading "
 "신규로 필요한 것 세 가지 at its left end. Three thin warm amber arrows rise from that band, two of them to stage 2 and "
 "one to stage 5. "
 "Text: only the five digits, the five stage names, the two lane headings, the band heading and the three cell labels. "),

("ai-openness-tiers-g7",
 "Composition: four blocks of equal width placed side by side as a staircase stepping down from left to right, separated "
 "by thin vertical dividers. The leftmost block is the tallest and filled solid navy; each block to its right is shorter "
 "and lighter; the rightmost is shortest and palest. Each block carries a Korean tier name beneath it. "
 "Tier names, left to right: 데이터 공개 오픈소스 AI, 오픈소스 AI, 가중치 공개 AI, 가중치 제공 AI. "
 "Inside every block sits a vertical column of three small squares of equal size. In block 1 all three are filled solid. "
 "In block 2 the top square is filled with a diagonal hatch and the lower two are solid. In block 3 the top square is "
 "hollow and the lower two are solid. In block 4 the top and middle squares are hollow and only the bottom is solid. "
 "A small legend at the top left names the three squares from top to bottom: 학습 데이터, 학습·배포 코드, 가중치. "
 "A small open padlock outline in warm amber sits on top of block 4 only, with the warm amber label 사용 제한 beside it. "
 "Detached at the far right beyond a clear gap and outside the staircase stands a fifth narrow block with a dashed slate "
 "gray stroke containing three hollow squares, labelled 비공개 — 벤더 API만 제공. "
 "Text: only the four tier names, the three legend labels, the amber label and the detached block label. "),

("model-license-inheritance",
 "Composition: a top-down genealogy graph three levels deep, rectangles for artifacts connected by thin arrows that never "
 "cross, small tag shapes for obligations. "
 "Top level: two parent rectangles side by side. The left parent is labelled 제한 있는 베이스 모델 and carries a row of "
 "four small filled navy tags along its bottom edge labelled 라이선스 사본, NOTICE, 명칭 규칙, AUP 전가. The right "
 "parent is labelled Apache-2.0 모델 and carries no tags. "
 "Middle level: three result rectangles in one row labelled 파인튜닝, 증류, 병합. The left result receives one arrow "
 "from the left parent, the middle result receives one thinner arrow from the left parent, and the right result receives "
 "two arrows, one from each parent. All three result rectangles carry the same row of four small filled navy tags. "
 "Bottom level: one wide terminal rectangle labelled 최종 배포물 that receives arrows from all three results and carries "
 "the same four navy tags plus one extra warm amber tag at its right end labelled 지역 제한. One further arrow leaves it "
 "downward to a small outline rectangle labelled 최종 사용자. "
 "To the right of the whole graph, set apart in clear white space, sits a small note shape with a dashed slate gray "
 "stroke containing one warm amber tag drawn faded and broken, joined to the graph by a thin dashed line, and the note "
 "reads 병합하면 조건이 사라진다는 오해. "
 "Text: only the labels listed above. "),

("ai-code-release-triple-gate",
 "Composition: one long horizontal navy arrow running from a small file shape at the left edge labelled 변경분 diff to a "
 "terminal rounded rectangle at the right edge labelled 릴리스. Three tall narrow gate bars stand across that arrow at "
 "even intervals, each drawn as a rectangle divided by two short parallel lines, each carrying its navy digit and a "
 "Korean gate name set vertically beside it. "
 "Gates, left to right: (1 / 의존성 SCA), (2 / 스니펫 매칭), (3 / AI 도구 로그). "
 "Under each gate bar sit two small stacked tags, the upper filled solid navy and the lower hollow with a dashed stroke. "
 "Under gate 1 they read 의존성 변경 PR and 의존성 교체. Under gate 2 they read diff 기준 and 제거·재작성. Under gate 3 "
 "they read 릴리스 전 and 로그 보존. "
 "Below the pipeline sits a group of three overlapping circles of equal size arranged in a triangle, drawn with thin "
 "strokes and very light fills, labelled 의존성 SCA, 스니펫 매칭 and AI 도구 로그, their three pairwise overlap regions "
 "shaded one step darker and the small central region left pure white. A small warm amber wedge marks one region just "
 "outside all three circles, labelled 미검출 영역. "
 "One separate thin slate gray arrow leaves the pipeline just before the terminal rectangle, bends downward and ends at "
 "a small box with a dashed stroke standing apart from the three gates, labelled 패키지 환각 — 공급망 보안 주제. "
 "Text: only the three digits, the three gate names, the six tag labels, the three circle labels, the two end labels, "
 "the amber label and the dashed box label. "),
]

assert len(SPECS) == 20, len(SPECS)
names = [n for n, _ in SPECS]
assert len(set(names)) == 20, "출력 파일명 중복"
for n, b in SPECS:
    assert '::' not in b, n

out = pathlib.Path('_workspace/07c_gen_args_v2.txt')
out.write_text("\n".join(f"{STYLE}{b}::{n}.png" for n, b in SPECS) + "\n", encoding='utf-8')
print(f"{len(SPECS)}건 기록 → {out}")
print(f"프롬프트 길이 min={min(len(STYLE)+len(b) for _,b in SPECS)} max={max(len(STYLE)+len(b) for _,b in SPECS)}")
