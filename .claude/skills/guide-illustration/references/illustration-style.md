# 삽화 화풍 규약과 프롬프트 작성

아트 디렉터가 프롬프트를 만들 때 읽는다. 이 파일의 프리픽스를 **글자 그대로** 모든 프롬프트에 붙인다.

## 목차

1. [화풍 프리픽스](#1-화풍-프리픽스)
2. [유형별 구도 지시문](#2-유형별-구도-지시문)
3. [프롬프트 작성 예시](#3-프롬프트-작성-예시)
4. [기존 이미지와의 조화](#4-기존-이미지와의-조화)

---

## 1. 화풍 프리픽스

기업 실무 문서의 삽화다. 예술적 표현이 아니라 **정보 전달**이 목적이며, 문서 안에서 튀지 않아야 한다.

```
Clean minimal technical diagram for a corporate governance handbook.
Flat vector illustration style, no gradients, no 3D, no shadows.
Restrained palette: deep navy (#1F3A5F) as primary, slate gray (#6B7A8F) as secondary,
soft teal (#3E9C9C) as accent, warm amber (#E8A33D) for emphasis only, on pure white background.
Thin uniform 2px strokes, generous white space, geometric shapes with slightly rounded corners.
Business-document aesthetic — legible at small size, printable in grayscale.
No people, no faces, no photorealism, no decorative flourishes, no logos or brand marks.
No text labels unless explicitly specified below.
```

이 프리픽스를 그대로 붙이는 이유:

- **flat vector / no gradients** — 그라데이션과 3D는 흑백 인쇄에서 뭉개진다. 이 가이드는 PDF로도 배포된다.
- **제한된 팔레트** — 그림마다 색이 다르면 문서가 산만해진다. 강조색(amber)은 그림당 한 곳에만 쓴다.
- **printable in grayscale** — 색으로만 구분한 정보는 흑백에서 사라진다. 명도 차이나 패턴으로도 구분되어야 한다.
- **no people, no faces** — 인물 묘사는 생성 모델이 가장 자주 이상하게 만드는 대상이고, 조직도에 사람 얼굴이 필요한 경우는 없다.
- **no logos or brand marks** — 모델이 실제 로고를 흉내 내면 위조 상표가 된다.
- **no text labels unless specified** — 기본값을 텍스트 없음으로 두어야 한글 깨짐 사고를 구조적으로 막는다.

프리픽스를 바꾸면 이미 생성한 모든 그림과 화풍이 어긋난다. 바꿀 때는 전체 재생성을 전제로 판단한다.

## 2. 유형별 구도 지시문

프리픽스 뒤에 유형별 구도 지시를 붙이고, 그 뒤에 그림 내용을 쓴다.

### process — 프로세스 흐름

```
Composition: horizontal left-to-right sequence of N rounded rectangular stages,
connected by thin arrows. Each stage numbered 1..N in navy. Equal stage widths.
Optional branch shown as a downward arrow to a single side box.
```

번호는 아라비아 숫자이므로 안전하게 렌더링된다. 단계 이름은 본문 서술이 담당한다.

### structure — 계층 구조

```
Composition: top-down hierarchy of nested rectangles, 2-3 levels deep.
Parent boxes contain child boxes with clear inset margins. Aligned grid.
Level distinguished by stroke weight and fill lightness, not by hue alone.
```

계층 깊이는 3단계를 넘기지 않는다. 그림에서 4단계 이상은 읽히지 않으므로 표로 바꾸는 것이 낫다.

### relationship — 관계도

```
Composition: central node with N satellite nodes arranged radially,
connected by thin lines. Line weight indicates relationship strength.
Circles for actors, rectangles for artifacts. No crossing lines.
```

노드가 7개를 넘으면 선이 교차하며 읽을 수 없게 된다. 그룹으로 묶어 노드 수를 줄인다.

### comparison — 비교

```
Composition: two symmetric columns side by side, separated by a thin vertical divider.
Identical row structure on both sides for direct comparison.
Left column in slate gray, right column in navy.
```

3열 이상 비교는 표가 낫다. 그림 비교는 2개 대안일 때만 유효하다.

### timeline — 시간 축

```
Composition: single horizontal axis with tick marks and milestone markers above the line.
Milestones as small filled circles with vertical connector lines to labels.
Year numbers on the axis in navy. Intervals proportional to actual time gaps.
```

연도 숫자는 안전하게 렌더링된다. **간격을 실제 시간에 비례시키는 지시가 중요하다** — 등간격으로 그리면 시행 일정의 급박함이 왜곡된다.

## 3. 프롬프트 작성 예시

### 예시 1 — process, 텍스트 없음

내용 명세: 오픈소스 컴플라이언스 7단계 프로세스 (식별 → 감사 → 이슈 해결 → 아키텍처 리뷰 → 승인 → 고지 → 검증), 3단계에서 1단계로 되돌아가는 재검사 루프

```
[프리픽스]
Composition: horizontal left-to-right sequence of 7 rounded rectangular stages,
connected by thin arrows. Each stage numbered 1 to 7 in navy. Equal stage widths.
A curved return arrow flows from stage 3 back to stage 1, drawn below the main sequence
in soft teal to indicate a re-scan loop.
Content: seven identical empty stage boxes, the third box outlined in warm amber
to mark it as the decision point. No text inside boxes.
```

`text_strategy: "numbers-only"`. 단계 이름은 캡션과 본문 `##### **1. 오픈소스 라이브러리 식별**` 헤딩이 담당한다.

### 예시 2 — relationship, 영문 약어 허용

내용 명세: SBOM을 중심으로 생성 도구·취약점 DB·VEX·관리 플랫폼이 연결되는 구조

```
[프리픽스]
Composition: central node with 4 satellite nodes arranged radially,
connected by thin lines. Circles for actors, rectangles for artifacts. No crossing lines.
Content: central rectangle labeled "SBOM" in navy uppercase.
Four satellites: rectangle "SPDX", rectangle "VEX", circle "CVE DB", circle "SCANNER".
Text: only these short Latin uppercase words, sans-serif, no other text anywhere.
```

`text_strategy: "latin-only"`. 이미 영문 약어가 표준인 용어만 그림에 넣는다.

### 예시 3 — timeline

내용 명세: 규제 시행 일정 (2024, 2026, 2027 마일스톤, 간격이 실제와 비례)

```
[프리픽스]
Composition: single horizontal axis with tick marks and milestone markers above the line.
Milestones as small filled circles with vertical connector lines.
Year numbers on the axis in navy. Intervals proportional to actual time gaps.
Content: axis spanning 2024 to 2028. Three milestone circles at 2024, 2026, 2027.
The 2027 milestone filled in warm amber and slightly larger to mark full applicability.
Text: only the four-digit year numbers on the axis. No other text.
```

### 프롬프트 작성 시 주의

- **셸 특수문자를 넣지 않는다.** `"`, `` ` ``, `$`, `\`는 명령 문자열을 깨뜨린다. 따옴표가 필요하면 단어를 그냥 쓴다.
- **부정 지시를 남기지 않는다.** 프리픽스의 `no text labels unless specified`가 기본값이므로, 텍스트를 넣으려면 명시적으로 허용해야 한다. 반대로 `no Korean text`처럼 부정형으로 막으려 하면 모델이 오히려 텍스트를 시도한다.
- **내용은 구조로 기술한다.** "컴플라이언스의 중요성을 보여주는 그림"이 아니라 "7개 박스가 좌에서 우로 화살표로 연결"처럼 형태를 지정한다.

## 4. 기존 이미지와의 조화

원고에는 이전 판에서 만든 이미지가 40여 개 있다. 전부 교체하는 것은 비용이 크고 이득이 불확실하다.

| 기존 이미지 상태 | 판단 |
|-----------------|------|
| 내용이 정확하고 도해가 명료함 | **유지.** 화풍이 달라도 정보가 맞으면 교체 이득이 없다 |
| 내용이 낡음 (프로세스 변경, 수치 변경) | **교체.** `-2026` 접미사로 새 파일 |
| 화면 캡처 (GitHub UI 등) | **재캡처 대상.** 생성 이미지로 대체하지 않는다 — UI 캡처를 그림으로 만들면 실제와 다른 화면이 된다 |
| 제품·기업 로고 | **공식 로고 확보 대상.** 생성 금지 |
| 흐리거나 저해상도 | 내용이 맞으면 유지. 해상도만으로 교체하면 작업량 대비 이득이 작다 |

교체를 결정하면 이유를 남긴다. "화풍이 다르다"만으로 교체하면 40개를 모두 교체해야 하는 근거가 되므로, 내용 갱신 필요와 결합될 때만 교체한다.

신규 삽화는 모두 이 프리픽스로 만들어 **신규분끼리는 화풍이 통일**되게 한다. 문서 안에서 구판 그림과 신판 그림이 구분되는 것은 개정판임을 드러내는 효과도 있어 허용 가능한 상태다.
