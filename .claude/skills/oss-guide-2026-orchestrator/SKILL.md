---
name: oss-guide-2026-orchestrator
description: "「기업 오픈소스 거버넌스 가이드」 2026 개정판 제작을 조율하는 오케스트레이터. 최신 동향 리서치(규제·공급망 보안·AI 라이선스·시장 통계·관리 도구) → 기존 원고 감사 → 개정 계획 승인 → 섹션별 집필·사실검증·문체교정 → 삽화 생성 → 통합 검수 → 원고 반영까지 14개 전문 에이전트를 단계별로 운용한다. '가이드 개정', '2026 개정판', '가이드 업데이트', '최신 트렌드 반영', '원고 개정', '삽화 추가', '가이드 리뉴얼' 요청 시 반드시 이 스킬을 사용. 후속 작업에도 반드시 사용: 개정 재실행, 특정 섹션만 다시, 리서치만 갱신, 삽화만 재생성, 검증 결과 반영, 이전 개정 결과 보완, 개정 계획 수정, 부분 재실행. 단, 단순 오탈자 수정이나 한 문단 편집은 이 스킬 없이 직접 처리한다."
---

# OSS Guide 2026 Orchestrator — 개정판 제작 조율

「기업 오픈소스 거버넌스 가이드」를 2026년 7월 기준 개정판으로 제작한다. 산출물은 `content/en/` 아래 Hugo 원고와 페이지 번들 이미지다.

## 실행 모드: 하이브리드

| Phase | 모드 | 이유 |
|-------|------|------|
| 0. 컨텍스트 확인 | 인라인 | 초기/부분/새 실행 판별 |
| 1. 정찰 | 인라인 | 섹션·각주·이미지 인벤토리와 발간본 텍스트를 확보한다 |
| 1.5. 기준선 확정 | 서브에이전트 | 발간본과 저장소 중 섹션별 기준 원고를 판정. 감사가 잘못된 원본을 훑는 것을 막는 직렬 관문 |
| 2. 리서치 + 감사 | **워크플로우** | 5개 축 × 5개 섹션이 사전 열거 가능한 결정적 팬아웃 |
| 3. 개정 계획 + **승인 게이트** | 인라인 | 구조 변경은 사용자 결정이 필요하다 |
| 4. 집필 + 검증 + 교정 | **워크플로우** | 섹션별 독립 파이프라인 + 주장별 적대적 검증 |
| 5. 삽화 | **워크플로우** | 목록 확정 후 5개씩 배치 병렬 |
| 6. 통합 검수 | **워크플로우** | 정합성 비평 + 기계 검증 |
| 7. 반영 | 인라인 | `content/en/` 쓰기는 사용자 확인 후 |

사용자가 이 스킬을 트리거한 것이 Workflow 옵트인에 해당한다. **기본 규모는 절제한다** — Phase 2는 10개, Phase 4는 섹션 수 × (1 집필 + 3 검증 + 1 교정), Phase 5는 삽화 수, Phase 6은 2개. 사용자가 "철저히/전수/최대한"을 요청하면 검증 반박자를 3명에서 5명으로, 리서치 축당 에이전트를 1개에서 2개로 확장한다.

## 에이전트 구성 (15개)

| 계층 | 에이전트 | 모델 | 담당 |
|------|---------|------|------|
| 기준선 | `published-edition-reconciler` | opus | 2025 발간본 ↔ 저장소 원고 대조, 섹션별 기준 원고 확정 |
| 리서치 | `oss-regulation-analyst` | opus | 규제·표준 (CRA, AI Act, ISO/IEC 5230, 국내 정책) |
| | `oss-supplychain-security-researcher` | opus | 공급망 보안 (SLSA, Sigstore, VEX, 사고 사례) |
| | `ai-oss-governance-researcher` | opus | AI 라이선스 (OSAID, 모델·데이터셋, 생성 코드 리스크) |
| | `oss-market-case-collector` | sonnet | 시장 통계·기업 사례 |
| | `oss-tooling-researcher` | sonnet | 관리 도구 현황 |
| 감사·기획 | `guide-content-auditor` | opus | 섹션별 노후도 감사 (읽기 전용) |
| | `revision-planner` | opus | 개정 계획·목차 설계 |
| 집필·편집 | `guide-section-writer` | opus | 섹션 개정 집필 |
| | `citation-fact-verifier` | opus | 인용·통계 적대적 검증 (읽기 전용) |
| | `korean-prose-editor` | sonnet | 문체 교정 |
| 삽화 | `illustration-art-director` | opus | 삽화 기획·프롬프트 설계 |
| | `illustration-producer` | sonnet | codex 이미지 생성·검수 |
| 품질 | `hugo-docsy-validator` | sonnet | 마크업·빌드 검증 (읽기 전용) |
| | `guide-coherence-critic` | opus | 전체 정합성·완전성 비평 (읽기 전용) |

모델은 업무 특성으로 배정했다 — 판단의 여지가 크고 앞 단계 결과가 다음을 바꾸는 업무(리서치 분석, 설계, 집필, 검증, 비평)는 opus, 절차와 양식이 고정된 업무(수집, 도구 대조, 문체 교정, 정적 검사, 명령 실행)는 sonnet.

## 스킬 연결

| 스킬 | 사용 에이전트 |
|------|-------------|
| `published-edition-baseline` | `published-edition-reconciler` |
| `oss-trend-research` | 리서치 5개 |
| `guide-revision-writing` | `guide-section-writer` |
| `guide-illustration` | `illustration-art-director`, `illustration-producer` |
| `guide-quality-check` | `citation-fact-verifier`, `hugo-docsy-validator` |
| `korean-nonfiction-editor` (글로벌) | `korean-prose-editor` |

## 워크플로우

### Phase 0: 컨텍스트 확인

1. `_workspace/` 존재 여부와 내용을 확인한다.
   - 미존재 → **초기 실행** (Phase 1부터)
   - 존재 + 부분 수정 요청("using 섹션만 다시", "삽화만 재생성") → **부분 재실행** (해당 Phase만)
   - 존재 + 전체 재실행 요청 → 기존 `_workspace/`를 `_workspace_{타임스탬프}/`로 이동 후 초기 실행. 타임스탬프는 `date +%Y%m%d-%H%M%S`로 셸에서 얻는다
2. `_workspace/run_meta.json`에서 직전 워크플로우의 `runId`를 읽는다. 부분 재실행이면 스크립트의 해당 단계만 수정하고 `resumeFromRunId`로 재개한다 — 변경 없는 `agent()` 호출은 캐시에서 즉시 반환되므로 부분 재실행이 저렴하다.
3. 새 실행이면 각 Phase의 워크플로우 `runId`를 `run_meta.json`에 기록한다.

```json
{"phase2_runId": "wf_...", "phase4_runId": "wf_...", "phase5_runId": "wf_...", "phase6_runId": "wf_...", "started": "2026-07-31"}
```

### Phase 1: 정찰 (인라인)

워크플로우에 넘길 목록을 확정한다. 목록을 스크립트에 하드코딩하지 않고 `args`로 주입한다.

```bash
mkdir -p _workspace/images
ls content/en/*/_index.md                                   # 섹션 목록
wc -l content/en/*/_index.md                                # 현재 분량 (분량 배분 기준)
python3 .claude/skills/guide-quality-check/scripts/check_guide_integrity.py --json > _workspace/01_baseline_integrity.json

# 발간본 PDF 가 있으면 본문을 추출한다 (저장소 루트의 *.pdf)
python3 .claude/skills/published-edition-baseline/scripts/extract_published_pdf.py \
  '[2025] 기업 오픈소스SW 거너번스 가이드.pdf' \
  -o _workspace/00_published_2025.md --report
```

기준선 정합성 검사를 먼저 남기는 이유: 개정 후 검사에서 나온 문제가 **개정이 만든 것인지 원래 있던 것인지** 구분해야 한다. 이 저장소에는 개정 전부터 존재하는 blocking 결함이 있다(죽은 앵커 3건, 정의 없는 각주 2건). 기준선 없이 비교하면 개정 탓으로 오판한다.

확정할 것: 섹션 slug 목록, 섹션별 현재 줄 수, 기존 blocking 목록, 기존 이미지 파일 목록, 발간본 추출 성공 여부.

발간본 PDF가 없거나 추출이 실패하면 Phase 1.5를 건너뛰고 `content/en/`을 기준으로 진행한다. 그 사실을 최종 보고서에 명시한다 — 추출 실패를 "발간본에 내용 없음"으로 처리하면 발간본의 갱신분이 통째로 유실된다.

### Phase 1.5: 기준선 확정 (서브에이전트)

발간본 추출에 성공한 경우에만 실행한다. `published-edition-reconciler`를 단일 동기 호출(`run_in_background: false`)한다 — 이후 감사가 그 판정에 의존하므로 병렬화할 수 없는 직렬 관문이다.

입력: `_workspace/00_published_2025.md`, `content/en/*/_index.md`
출력: `_workspace/01_baseline_reconciliation.{json,md}`

결과에서 확인할 것:
- `sections[].baseline_source` — 섹션별로 `repo` / `published` / `merge` 중 무엇인지
- `unmapped` — 대응되지 않은 장이 있으면 사용자에게 알린다. 조용히 빠지면 개정판에서 한 장이 사라진다
- `editorial_substitutions` — 용어 표기 차이("오픈소스" vs "오픈소스SW"). 최종 표기 결정은 Phase 3 승인 게이트로 넘긴다

`baseline_source`가 `published` 또는 `merge`인 섹션은 Phase 2 감사에 발간본 텍스트 경로를 함께 전달한다.

### Phase 2: 리서치 + 감사 (워크플로우)

`args`: `{sections: [...], researchAxes: [...], baseline: {...}, reconciliation: '_workspace/01_baseline_reconciliation.json', publishedText: '_workspace/00_published_2025.md'}`

- `meta.phases`: `[{title: '리서치'}, {title: '감사'}]`
- **리서치**: 5개 축을 `pipeline`으로 흘린다. 각 축은 해당 `agentType`과 `schema`(축별 발견 shape)로 호출. 축 간 의존이 없으므로 배리어를 두지 않는다.
- **감사**: 5개 섹션을 `pipeline`으로 흘린다. `agentType: 'guide-content-auditor'`, `schema`로 issues 반환. **각 섹션의 `baseline_source`를 프롬프트에 함께 넘긴다** — `published`/`merge` 섹션은 발간본 텍스트도 읽고 감사해야 한다. 이 값을 넘기지 않으면 감사가 낡은 원본만 훑는다.
- 두 그룹은 서로 독립이므로 하나의 `parallel`에 두 `pipeline`을 넣거나 순차로 흘린다. 배리어는 두지 않는다 — 감사가 리서치 결과를 필요로 하지 않는다.
- 반환: `{research: [...], audits: [...]}`. `.filter(Boolean)` 적용 후 드랍 수를 `log()`.

워크플로우 완료 후 메인이 결과를 `_workspace/02_research_{axis}.json`, `_workspace/03_audit_{slug}.json`으로 저장한다. 리서치 에이전트도 자체적으로 같은 경로에 쓰므로 중복이 정상이다 — 파일이 이미 있으면 반환값을 우선한다.

### Phase 3: 개정 계획 + 승인 게이트

1. `revision-planner`를 단일 호출한다 (`Agent`, `run_in_background: false`). 입력은 `_workspace/`의 리서치·감사 결과 경로 **+ `01_baseline_reconciliation.json`** (발간본에만 있는 내용 중 `worth_keeping: true` 항목이 개정 지시로 변환되어야 한다).
2. 산출물 `_workspace/04_revision_plan.md`를 읽고 사용자에게 다음을 제시한다:
   - **기준선 판정** (섹션별 `repo`/`published`/`merge`와 근거, 대응 안 된 장이 있으면 함께)
   - **용어 표기 결정** ("오픈소스" vs "오픈소스SW" — 발간본은 후자를 쓴다. 개정판이 무엇을 따를지 여기서 확정한다)
   - 구조 결정 (신규 장 신설 여부와 근거)
   - 섹션별 개정 규모 (지시 건수, 목표 분량 증감)
   - 삽화 목록 (개수, 교체 대상)
   - `open_questions` — 사용자 결정이 필요한 항목
3. **승인을 받는다.** 승인 없이 Phase 4로 넘어가지 않는다. 개정은 원고 수천 줄을 바꾸는 작업이고, 구조 결정이 틀리면 이후 전부가 낭비된다.
4. 사용자가 계획을 수정하면 `revision-planner`를 재호출해 해당 지시만 갱신한다 (`id` 유지 — 캐시 무효화를 막는다).

### Phase 4: 집필 + 검증 + 교정 (워크플로우)

`args`: `{plan: '_workspace/04_revision_plan.json', sections: [...], verifierCount: 3}`

섹션별 `pipeline` 3단계. **배리어를 두지 않는다** — 섹션 A가 교정 중일 때 섹션 B가 집필 중이어도 무관하다.

1. **집필** — `agentType: 'guide-section-writer'`, `schema`로 draft 경로와 실행 이력 반환
2. **검증** — 집필 결과에서 검증 대상 주장을 뽑아 주장별로 `citation-fact-verifier`를 `verifierCount`명 병렬 호출. 각 반박자에게 **서로 다른 렌즈**를 준다(수치 정확성 / 출처 실질 지지 / 시점 유효성) — 동일 프롬프트 3회보다 다양성이 많이 잡는다. 과반이 반박하면 확정 결함.
3. **교정** — `agentType: 'korean-prose-editor'`, 확정 결함 목록을 함께 전달해 사실 수정이 필요한 문장은 건드리지 않게 한다

확정 결함이 있으면 해당 섹션의 집필 단계를 1회 재호출해 수정한다 (파이프라인 내부 루프, 최대 1회 — 무한 루프 방지).

반환: `{sections: [{slug, draft, edited, confirmedDefects, unresolved}]}`

`.filter(Boolean)` 필수. 섹션 하나가 null이면 그 섹션은 개정 없이 진행하고 보고서에 명시한다.

### Phase 5: 삽화 (워크플로우)

`args`: `{plan: '...', workDir: '_workspace/images'}`

1. **기획** — `illustration-art-director` 단일 호출. `style_prefix`와 전체 `specs`를 한 번에 만든다. **여기를 병렬화하지 않는다** — 화풍 통일은 전체를 함께 판단해야 나온다.
2. **생성** — `specs`를 5개씩 나눠 `illustration-producer`를 배치 호출. 각 producer가 자기 배치를 `.claude/skills/guide-illustration/scripts/gen_illustrations.sh`로 실행한다. 6개 이상 동시는 큐잉으로 분산이 커진다.
3. **검수** — producer가 자체 검수한다. 실패 항목은 아트 디렉터에게 프롬프트 수정을 요청하고 **1회만** 재생성한다.

반환: `{generated: [...], failed: [...], retired: [...]}`

실패한 삽화가 있으면 해당 `imgproc` 블록을 원고에서 제거할지 사용자에게 확인한다 — 참조만 남으면 빌드가 실패한다.

### Phase 6: 통합 검수 (워크플로우)

`args`: `{editedPaths: [...], plan: '...', baseline: '_workspace/01_baseline_integrity.json'}`

`parallel` 배리어가 정당한 유일한 곳이다 — 정합성 비평은 모든 섹션을 함께 읽어야 한다.

1. `guide-coherence-critic` — 전체 섹션 통독. 상충·중복·용어 불일치·계획 미이행·누락 주제
2. `hugo-docsy-validator` — 기계 검증 + 빌드. **기준선과 비교**해 개정이 만든 문제만 blocking으로 판정

반환: `{critic: {...}, validator: {...}, verdict: 'ready|needs_revision', newDefectsVsBaseline: [...]}`

`needs_revision`이면 `top_priority` 항목을 Phase 4로 되돌린다 (해당 섹션만, `resumeFromRunId` 활용).

### Phase 7: 반영 (인라인)

**사용자 확인 후에만 `content/en/`을 수정한다.** 여기까지 모든 산출물은 `_workspace/`에 있으므로 이 지점이 유일한 되돌릴 수 없는 단계다.

1. 사용자에게 반영 계획을 제시: 변경 섹션, 줄 수 변화, 신규·교체 이미지, 신규 섹션 디렉토리
2. 확인 후 브랜치를 만든다 — `main`에 직접 쓰지 않는다:
   ```bash
   git checkout -b revision/2026-edition
   ```
3. `_workspace/06_edited_{slug}.md` → `content/en/{slug}/_index.md` 복사
4. 신규 섹션은 디렉토리 생성 후 배치
5. 이미지는 이미 Phase 5에서 페이지 번들에 배치됨. `replaces` 대상 기존 파일 삭제는 **여기서** 판단한다 (참조가 남아 있는지 먼저 확인)
6. 반영 후 최종 검사:
   ```bash
   python3 .claude/skills/guide-quality-check/scripts/check_guide_integrity.py
   git status --porcelain themes/docsy   # 테마가 변경되었으면 개정 부작용
   ```
7. 커밋은 사용자가 요청할 때만 한다. 커밋 메시지는 한글로 쓴다.
8. `_workspace/`를 보존한다 (사후 검증·감사 추적용).

## 데이터 흐름

```
발간본 PDF ──[Phase 1 추출]──→ _workspace/00_published_2025.md ─┐
                                                                 ├→ [Phase 1.5 대조]
content/en/*/_index.md ─────────────────────────────────────────┘        ↓
        │                                          _workspace/01_baseline_reconciliation.json
        │                                                                 │
        ├→ [Phase 2 리서치] → _workspace/02_research_{axis}.json ─┐       │
        └→ [Phase 2 감사]   → _workspace/03_audit_{slug}.json  ─┤←──────┘ (baseline_source 주입)
                                                                  ↓
                                         [Phase 3] → _workspace/04_revision_plan.{json,md} → 승인
                                                                                  ↓
                        ┌─────────────────────────────────────────────────────────┤
                        ↓                                                         ↓
   [Phase 4 집필] → 05_draft_{slug}.md                          [Phase 5 기획] → 07_illustration_specs.json
        ↓ 검증 (주장별 3명 병렬)                                        ↓ 생성 (5개씩 배치)
        ↓ 교정 → 06_edited_{slug}.md                             _workspace/images/*.png → content/en/{slug}/
        └─────────────────────────┬───────────────────────────────────────────────┘
                                  ↓
                        [Phase 6 통합 검수] ── needs_revision ──→ Phase 4 (해당 섹션만)
                                  ↓ ready
                        [Phase 7 반영] → content/en/ (브랜치, 사용자 확인 후)
```

## 파일 컨벤션

| 경로 | 내용 |
|------|------|
| `_workspace/00_published_2025.md` | 발간본 PDF 추출·정규화 텍스트 (`<!-- page:N -->` 보존) |
| `_workspace/01_baseline_reconciliation.{json,md}` | 섹션별 기준 원고 판정 (json=기계, md=승인용) |
| `_workspace/01_baseline_integrity.json` | 개정 전 정합성 기준선 |
| `_workspace/02_research_{axis}.json` | 축별 리서치 (regulation/security/ai/market/tooling) |
| `_workspace/03_audit_{slug}.json` | 섹션별 감사 |
| `_workspace/04_revision_plan.{json,md}` | 개정 계획 (json=기계, md=승인용) |
| `_workspace/05_draft_{slug}.md` | 집필 초안 |
| `_workspace/06_edited_{slug}.md` | 교정본 (Phase 7 반영 원본) |
| `_workspace/07_illustration_specs.json` | 삽화 프롬프트 명세 |
| `_workspace/images/*.png` | 생성 이미지 (페이지 번들 복사 전) |
| `_workspace/run_meta.json` | Phase별 runId |

## 에러 핸들링

| 상황 | 전략 |
|------|------|
| 발간본 PDF 없음 / 추출 실패 | Phase 1.5 생략, `content/en/` 기준으로 진행. **"발간본에 내용 없음"으로 처리하지 않는다** — 실패로 보고서에 명시 |
| 장 대응 실패 (`unmapped` 존재) | 억지 매핑하지 않고 사용자에게 알린다. 대응 안 된 장이 조용히 빠지면 개정판에서 한 장이 사라진다 |
| `agent()` 개별 실패 (null) | `.filter(Boolean)`로 제외, 드랍 수 `log()`, 최종 보고서에 누락 명시 |
| 리서치 축 1개 실패 | 그 축을 근거로 하는 지시는 만들지 않는다. 계획에 누락 축 명시 — 빈 축을 자체 지식으로 메우면 검증 안 된 서술이 계획부터 들어간다 |
| 섹션 집필 실패 | 그 섹션은 개정 없이 진행. 다른 섹션을 막지 않는다 |
| 검증에서 critical 다수 | Phase 4 집필 1회 재호출. 재실패 시 사용자에게 보고하고 해당 서술 삭제를 제안 |
| 삽화 생성 실패 | 1회 재시도. 재실패 시 원고의 `imgproc` 블록 제거 여부를 사용자에게 확인 (참조만 남으면 빌드 실패) |
| `codex login` 미인증 | Phase 5 전체 중단. 사용자에게 `codex login` 요청. 다른 Phase는 영향 없음 |
| hugo 미설치 | 정적 검사만 수행하고 그 사실을 명시. **빌드하지 않고 통과로 보고하지 않는다** |
| 워크플로우 전체 실패 | transcript 디렉토리의 journal에서 각 에이전트의 실제 반환값을 확인한 뒤 실패 단계만 수정해 `resumeFromRunId`로 재개. 빈 결과를 성공으로 오독하지 않는다 |
| 상충 데이터 | 삭제하지 않고 출처 병기. 판단 근거가 없으면 판단하지 않는 것이 정확하다 |
| 기준선에 있던 결함 | 개정 탓으로 보고하지 않는다. 별도 항목으로 "기존 결함 — 함께 고칠지 확인" |

## 테스트 시나리오

### 정상 흐름
1. 사용자가 "가이드 2026 개정판 만들어줘" → Phase 0에서 `_workspace/` 미존재 확인 → 초기 실행
2. Phase 1: 5개 섹션 확정, 기준선 blocking 5건 기록, 발간본 180쪽 → 3061행 추출
3. Phase 1.5: 대조 결과 `intro`/`using`은 `merge`, 나머지는 `repo`. 용어 치환 "오픈소스↔오픈소스SW" 검출
4. Phase 2: 리서치 5축 + 감사 5섹션 = 10 에이전트 → 발견 약 100건, 감사 이슈 약 80건
5. Phase 3: 계획 생성 → 사용자에게 기준선 판정 + 용어 표기 결정 + "AI 거버넌스 신규 장 신설(weight 60)" 제시 → 승인
6. Phase 4: 6개 섹션 × (집필 1 + 검증 3n + 교정 1) → 확정 결함 12건 수정
7. Phase 5: 삽화 18건 기획 → 4배치 생성 → 17건 성공, 1건 실패
8. Phase 6: 비평 결과 `needs_revision`, top_priority 3건 → Phase 4 부분 재실행 → `ready`
9. Phase 7: 사용자 확인 → `revision/2026-edition` 브랜치에 반영 → 최종 검사 blocking 0
10. 예상 결과: `content/en/` 6개 섹션 갱신, 신규 이미지 17개, `_workspace/` 보존

### 에러 흐름 (리서치 축 실패)
1. Phase 2에서 `ai` 축 에이전트가 null 반환
2. `.filter(Boolean)` 후 4축으로 진행, `log("리서치 1축 드랍: ai")`
3. Phase 3: `revision-planner`가 AI 관련 지시를 만들지 않고 `structure_decision.rationale`에 "ai 축 누락으로 AI 거버넌스 장 신설 판단 보류" 기록
4. 사용자에게 "ai 축 재실행 후 계획 갱신" 또는 "AI 장 없이 진행" 선택 제시
5. 재실행 선택 시 `resumeFromRunId`로 Phase 2 재개 — 성공한 4축은 캐시에서 즉시 반환

### 에러 흐름 (삽화 실패)
1. Phase 5에서 `IL-07`이 0바이트 PNG 생성
2. producer가 1회 재시도 → 재실패 → `failed` 반환, `failure_reason`에 codex 로그 인용
3. 아트 디렉터가 원인 확인 — 프롬프트가 한글 라벨을 요구했음 → `text_strategy`를 `numbers-only`로 변경
4. 1회 재생성 → 성공. 실패가 반복되면 해당 삽화를 표로 대체할 것을 제안한다
