# Hugo / Docsy 마크업 상세 규약

SKILL.md의 보충. 마크업 판단이 애매할 때, 신규 섹션을 만들 때, 빌드를 확인할 때 읽는다.

## 목차

1. [프로젝트 구조 전제](#1-프로젝트-구조-전제)
2. [앵커 슬러그 규칙](#2-앵커-슬러그-규칙)
3. [imgproc 상세](#3-imgproc-상세)
4. [신규 섹션 추가 절차](#4-신규-섹션-추가-절차)
5. [빌드 확인](#5-빌드-확인)
6. [테마 커스터마이징 주의](#6-테마-커스터마이징-주의)

---

## 1. 프로젝트 구조 전제

집필자가 알아야 할 이 프로젝트의 비표준 사항.

| 사항 | 내용 | 집필에 미치는 영향 |
|------|------|------------------|
| `contentDir = "content/en"` | `defaultContentLanguage = "en"`이지만 **다국어 사이트가 아니다.** 내용은 전부 한국어이고 `en`은 껍데기 경로다 | 번역 디렉토리를 만들지 않는다. 한국어를 `content/en/` 아래에 쓴다 |
| `static/` 없음 | 정적 파일 디렉토리가 없다 | 이미지는 페이지 번들(`content/en/{section}/`) 안에만 둔다. 루트 `images/`는 README·레거시용이며 배포되지 않는다 |
| 섹션당 단일 `_index.md` | 각 장이 파일 하나(최대 1300줄) | 절을 새 파일로 분리하지 않는다. 해당 섹션 `_index.md`를 편집한다 |
| 테마 vendored | `themes/docsy`가 `.gitmodules`에 선언되어 있지만 실제로는 저장소에 직접 커밋되어 있다 | 테마 파일을 고치면 추적 파일이 변경된다. 절대 건드리지 않는다 |
| `enableGitInfo = true` | 페이지 하단 최종 수정일이 Git 이력에서 나온다 | 원고를 커밋하면 날짜가 갱신된다 |
| 루트 `oss-governance-guide.md` | 2023-02에 멈춘 단일 파일 발간본 | **정본이 아니다.** 개정 시 건드리지 않는다 |

## 2. 앵커 슬러그 규칙

내부 링크(`](#...)`)가 가리키는 앵커는 헤딩 텍스트에서 자동 생성된다. Hugo goldmark의 GitHub 스타일 슬러그 규칙:

1. 소문자로 변환 (한글은 변화 없음)
2. 공백을 하이픈으로 변환
3. 마크다운 강조 기호(`*`, `_`)와 대부분의 구두점 제거
4. 한글·영숫자·하이픈·언더스코어만 남음

예시:

| 헤딩 | 슬러그 |
|------|--------|
| `#### 주요 오픈소스 관리 도구 소개` | `주요-오픈소스-관리-도구-소개` |
| `##### **1. 오픈소스 라이브러리 식별**` | `1-오픈소스-라이브러리-식별` |
| `### SBOM 관리` | `sbom-관리` |
| `#### OSPO의 인원 구성과 역할` | `ospo의-인원-구성과-역할` |

**영문이 섞인 헤딩은 소문자로 변환된다.** `### SBOM 관리`를 가리킬 때는 `](#sbom-관리)`라고 써야 한다. 대문자로 쓰면 링크가 죽는다.

헤딩을 수정할 때는 반드시 참조를 함께 찾는다:

```bash
grep -rn "](#" content/en/ | grep "고칠-슬러그"
```

같은 파일 안에 동일한 텍스트의 헤딩이 두 개 있으면 두 번째에 `-1`이 붙는다. 중복 헤딩은 만들지 않는다.

## 3. imgproc 상세

`imgproc`는 Docsy가 제공하는 Hugo 이미지 처리 shortcode다. **페이지 리소스만 처리한다** — 대상 이미지가 같은 페이지 번들(`content/en/{section}/`)에 없으면 빌드가 실패한다.

```markdown
{{< imgproc <파일명-확장자없이> <명령> "<크기>" >}}
<center><i>[캡션]</i><center>
{{< /imgproc >}}
```

명령은 Hugo 이미지 처리 명령이다. 기존 원고는 `Fit`과 `Resize`를 쓴다.

- `Fit "768x768"` — 비율 유지하며 박스 안에 맞춤. 도해 기본값
- `Fit "384x384"` — 로고
- `Fit "1024x768"` — 넓은 표, 화면 캡처
- `Resize "300x"` — 폭 고정 (홈 페이지에서 사용)

자기 닫는 형태(`{{< imgproc X Resize "300x" />}}`)도 유효하지만 캡션을 넣을 수 없다. 캡션이 있으면 열고 닫는 형태를 쓴다.

**캡션 마크업의 기존 관례가 불완전하다.** 원고는 `<center><i>[제목]</i><center>`처럼 닫는 태그가 `</center>`가 아닌 경우가 있다. 브라우저가 관대하게 처리하므로 렌더링은 되지만, 신규 작성 시에는 올바르게 닫는다:

```markdown
<center><i>[오픈소스 컴플라이언스 프로세스]</i></center>
```

기존 블록을 고칠 필요는 없다 — 개정 범위와 무관한 마크업 정리는 diff를 키우고 리뷰를 어렵게 한다.

출처 표기가 필요한 그림은 캡션 아래 별도 줄:

```markdown
{{< imgproc compliance-process-2026 Fit "768x768" >}}
<center><i>[오픈소스 컴플라이언스 프로세스]</i></center>
<center>Linux Foundation, 문서명 : https://example.org</center>
{{< /imgproc >}}
```

## 4. 신규 섹션 추가 절차

개정에서 장을 신설할 때(예: AI 거버넌스 장):

1. 디렉토리 생성: `content/en/{slug}/`
2. `_index.md` 작성 — front matter의 `weight`가 사이드바 순서를 정한다. 기존 값(10/20/30/40/50)과 충돌하지 않게 배정한다. 기존 장 사이에 넣어야 하면 앞뒤 장의 weight를 함께 조정해야 하므로, 가능하면 뒤에 붙인다(60).
   ```yaml
   ---
   title: "AI와 오픈소스"
   linkTitle: "5. AI와 오픈소스"
   weight: 60
   description: >
      
   ---
   ```
3. 이미지는 같은 디렉토리에 둔다.
4. 홈 페이지(`content/en/_index.md`)의 주석 처리된 목차에 장이 나열되어 있다. 활성화되어 있지 않으므로 수정 불필요하지만, 활성화 여부를 확인한다.
5. 다른 장에서 새 장을 참조하는 링크는 섹션 상대 경로를 쓴다: `[AI와 오픈소스](../ai-governance/)`.

`weight`를 빠뜨리면 사이드바에서 순서가 불안정해진다.

## 5. 빌드 확인

로컬에 `hugo`가 설치되어 있지 않을 수 있다. 확인 후 분기한다.

```bash
hugo version    # 없으면 정적 검사만 수행하고 그 사실을 보고한다
```

설치되어 있으면 CI와 같은 조건이 **Hugo extended 0.78.2**다. Docsy는 extended(SCSS 지원) 빌드를 요구한다.

```bash
# 빠른 검증 — 파일을 쓰지 않고 메모리에서 렌더링
hugo --renderToMemory

# 개발 서버 — PostCSS를 건너뛰므로 node_modules 없이 동작
hugo server

# CI와 동일한 프로덕션 빌드 — node_modules(autoprefixer) 필수
npm ci && hugo --minify
```

`hugo server`가 PostCSS를 건너뛰는 것은 Docsy의 `head-css.html`이 `.Site.IsServer`로 분기하기 때문이다. 따라서 **원고 검증 목적이면 `--minify`가 불필요하다** — node_modules가 없어서 실패한 빌드를 원고 결함으로 오해하지 않도록, 실패 시 원인을 구분해 보고한다.

빌드 에러 메시지에서 확인할 것:

| 메시지 유형 | 원인 |
|------------|------|
| `failed to extract shortcode` | 존재하지 않는 shortcode 또는 닫는 태그 누락 |
| `resource not found` (imgproc) | 페이지 번들에 이미지 파일이 없음 |
| `unmarshal failed` | front matter YAML 문법 오류 |

## 6. 테마 커스터마이징 주의

이 프로젝트는 루트 `layouts/`에서 테마를 오버라이드한다. 이미 오버라이드된 파일:

- `layouts/home.html`, `layouts/404.html`
- `layouts/_default/{list,single,content}.html`
- `layouts/partials/{section-index,sidebar-tree}.html`

`sidebar-tree.html`은 트리를 `.FirstSection`이 아니라 `.Site.Home`부터 그리고 `nomenu`/`toc_hide` 파라미터를 지원하도록 업스트림과 다르게 수정되어 있다. **테마 파일로 덮어쓰면 사이드바 구조가 바뀐다.**

집필 작업은 레이아웃을 건드릴 이유가 없다. 렌더링 문제가 레이아웃 때문이라고 판단되면 고치지 말고 보고한다 — 레이아웃 변경은 전체 사이트에 영향을 미치므로 개정 작업의 범위를 넘는다.
