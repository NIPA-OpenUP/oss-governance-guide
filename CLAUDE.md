# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 저장소 성격

Hugo + Docsy 로 만든 정적 문서 사이트다. 산출물은 코드가 아니라 한국어 기술 문서(NIPA 주관 「기업 오픈소스 거버넌스 가이드」)이며, 대부분의 작업은 `content/en/` 아래 마크다운 편집이다. 배포 사이트: https://NIPA-OpenUP.github.io/oss-governance-guide/

`origin` 은 fork(`revfactory/oss-governance-guide`), 원본은 `upstream`(`NIPA-OpenUP/oss-governance-guide`) 이다.

## 하네스: 가이드 2026 개정판 제작

**목표:** 가이드 전체를 2026년 7월 기준 개정판으로 다시 만든다 — 최신 규제·보안·AI 라이선스 동향 반영, 기업이 바로 쓸 수 있는 실용 산출물 확충, 삽화 신설·교체.

**트리거:** 가이드 개정·업데이트·최신 동향 반영·삽화 추가 관련 작업 요청 시 `oss-guide-2026-orchestrator` 스킬을 사용하라. 부분 작업(리서치만, 특정 섹션만, 삽화만)과 후속 재실행도 같은 스킬이 처리한다. 단순 오탈자 수정이나 한 문단 편집은 직접 처리한다.

**변경 이력:**

| 날짜 | 변경 내용 | 대상 | 사유 |
|------|----------|------|------|
| 2026-07-31 | 초기 구성 (harness v2) — 에이전트 14, 스킬 5(오케스트레이터 1 포함) | 전체 | 2026 개정판 제작 |
| 2026-07-31 | `published-edition-reconciler` 에이전트 + `published-edition-baseline` 스킬 추가, 오케스트레이터에 Phase 1.5(기준선 확정) 신설 | 에이전트 15 / 스킬 6 | 저장소 루트의 2025 발간본 PDF(180쪽, 2025-02)를 기준 원고로 편입 |

## 명령

로컬에 `hugo` 가 설치되어 있지 않다. CI 기준은 **Hugo extended 0.78.2** (Docsy 는 extended 필수).

```bash
hugo server            # 로컬 미리보기. PostCSS 를 건너뛰므로 node_modules 없이 동작
npm ci && hugo --minify  # 프로덕션 빌드. node_modules(autoprefixer) 필요
```

- `hugo server` 는 `.Site.IsServer` 분기로 SCSS 만 컴파일한다(`themes/docsy/layouts/partials/head-css.html`). 서버가 아닌 빌드에서는 `postCSS` 가 호출되므로 `npm ci` 를 먼저 하지 않으면 빌드가 깨진다.
- 테스트·린트 없음. `npm test` 는 의도적으로 실패한다(상위 템플릿 잔재).
- `deploy.sh` 는 원본 템플릿(bep/tech-doc-hugo)에서 온 잔재로, 무관한 S3 버킷에 배포한다. **실행하지 말 것.** 배포는 GitHub Actions 가 담당한다.

## CI/배포

- `.github/workflows/gh-pages-build.yml` — main 대상 PR 에서 빌드 검증만 수행.
- `.github/workflows/gh-pages.yml` — main push 시 빌드 후 `gh-pages` 브랜치로 배포.
- 두 워크플로 모두 `fetch-depth: 0` 을 쓴다. `enableGitInfo = true` 라서 페이지 하단 최종 수정일이 Git 이력에서 나온다.

## 콘텐츠 구조

섹션 하나당 **단일 `_index.md`** 다. 파일을 쪼개지 말고 해당 섹션 파일을 편집한다.

| 경로 | linkTitle | weight | 규모 |
|--|--|--|--|
| `content/en/intro/_index.md` | 0. 들어가며 | 10 | ~120줄 |
| `content/en/using/_index.md` | 1. 사용하기 | 20 | ~1300줄 |
| `content/en/contributing/_index.md` | 2. 기여하기 | 30 | ~860줄 |
| `content/en/releasing/_index.md` | 3. 공개하기 | 40 | ~690줄 |
| `content/en/ospo/_index.md` | 4. OSPO | 50 | ~300줄 |

- 사이드바·목차 순서는 front matter `weight` 로 정한다. 사이드바 표기는 `linkTitle`, 페이지 제목은 `title`.
- `contentDir = "content/en"`, `defaultContentLanguage = "en"` 이지만 **다국어 사이트가 아니다.** 내용은 전부 한국어이고 `en` 은 껍데기 경로일 뿐이다. 번역 디렉터리를 새로 만들 이유가 없다.
- 루트 `oss-governance-guide.md`(244KB)는 2023-02 에 멈춘 단일 파일 발간본이다. 정본은 `content/en/` 이므로 문서 수정 시 이 파일은 건드리지 않는다.

## 문서 작성 관례

- **이미지는 해당 섹션 디렉터리(페이지 번들) 안에** 두고 확장자 없이 참조한다. 루트 `images/` 는 README 및 레거시용이며 `static/` 이 없으므로 Hugo 가 배포하지 않는다.
  ```
  {{< imgproc compliance-process Fit "768x768" >}}
  <center><i>[오픈소스 컴플라이언스 프로세스]</i><center>
  {{< /imgproc >}}
  ```
  캡션은 위와 같이 `imgproc` 블록 안에 `<center><i>[제목]</i></center>` 로 넣는다(`markup.goldmark.renderer.unsafe = true` 라 raw HTML 이 허용된다).
- 각주는 문단 바로 뒤에 정의를 붙인다: 본문 `[^perforce2024]` → 다음 줄에 `[^perforce2024]: 보고서명 : https://...`. 외부 통계·보고서를 인용할 때는 링크와 각주를 함께 단다.
- 섹션 내부 링크는 한글 헤딩 앵커를 쓴다: `[주요 오픈소스 관리 도구 소개](#주요-오픈소스-관리-도구-소개)`.
- 사용 가능한 shortcode 는 Docsy 제공분뿐이다: `alert`, `pageinfo`, `imgproc`, `blocks`, `readfile`, `swaggerui` (`themes/docsy/layouts/shortcodes/`).
- 서술체는 **'~한다' 평서문(문어체)** 이다. 존댓말·구어체를 섞지 않는다.
- 각 장은 **'기업 편'**(오픈소스 사무국/정책 담당 관점)과 **'개발자 편'**(현업 개발자 관점)으로 나눠 서술하는 구조를 유지한다.
- 헤딩은 `##`~`#####` 까지 쓰고, `#####` 은 `##### **1. 오픈소스 라이브러리 식별**` 처럼 굵게 표기한다.

## 테마: 서브모듈이 아니라 vendored

`.gitmodules` 는 `themes/docsy` 를 서브모듈로 선언하지만 **실제로는 7,300여 파일이 저장소에 직접 커밋되어 있다**(Docsy 의 `assets/vendor/bootstrap`, `assets/vendor/Font-Awesome` 포함). 따라서:

- `git submodule status` / `update` 는 아무 일도 하지 않는다. clone 만으로 빌드 가능하다.
- `themes/docsy/` 아래를 고치면 추적 중인 파일이 변경된다. 테마 조정은 루트 `layouts/` 또는 `assets/scss/_variables_project.scss` 에서 오버라이드한다.
- 이미 오버라이드된 파일: `layouts/home.html`, `layouts/_default/{list,single,content}.html`, `layouts/404.html`, `layouts/partials/{section-index,sidebar-tree}.html`. 특히 `sidebar-tree.html` 은 트리를 `.FirstSection` 대신 `.Site.Home` 부터 그리고 `nomenu`/`toc_hide` 파라미터를 지원하도록 업스트림과 다르게 수정돼 있다. 테마 파일로 통째로 덮어쓰지 말 것.

## 기여 절차

실제 절차는 README.md 기준이다: GitHub Flow 로 PR, 또는 이슈 등록. 루트 `CONTRIBUTING.md` 는 Google CLA 를 요구하는 템플릿 잔재이며 이 프로젝트에 적용되지 않는다. 문서 라이선스는 공공누리 제1유형이다.
