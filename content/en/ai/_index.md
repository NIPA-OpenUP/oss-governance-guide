---
title: "AI와 오픈소스SW"
linkTitle: "5. AI와 오픈소스SW"
weight: 60
description: >
   
---

이 장이 다루는 자산은 앞선 장들이 전제한 오픈소스SW 컴포넌트가 아니다. AI 모델, 학습·평가에 사용하는 데이터셋, 그리고 AI 코딩 도구가 만들어 낸 코드 세 가지다. 이 세 자산은 라이선스가 부착되는 방식도, 의무가 파생물로 전파되는 경로도 라이브러리와 다르다.

그럼에도 이 장의 대전제는 'AI 자산을 위한 관리 체계를 새로 만들지 않는다'이다. 이미 운영 중인 오픈소스SW 거버넌스 프로세스에 자산 유형을 하나 더하는 편이 현실적이라고 이 가이드는 판단한다. 새 체계를 세우면 승인 경로가 둘로 갈라지고, 두 체계 사이에 끼는 자산(예: 오픈소스SW 라이브러리로 배포되는 모델 런타임)에서 관리 공백이 생긴다.

이 장도 다른 장과 같이 두 트랙으로 나뉜다. 기업 편은 정책·라이선스·규제를 다루고, 개발자 편은 AI 코딩 도구 사용과 모델 반입 실무를 다룬다. 같은 주제를 다룰 때 기업 편은 근거와 승인 기준을 서술하고 개발자 편은 배포 직전에 손으로 확인할 행위만 서술하며, 라이선스 원문과 규제 조항 같은 사실관계는 기업 편에 두고 반복하지 않는다. 정책을 세우는 독자는 기업 편을, 커밋과 배포를 직접 하는 독자는 개발자 편을 먼저 읽는다.

{{% alert color="success" %}}
본 장의 라이선스 해석은 법률 자문이 아니다. 라이선스 원문과 법령을 근거로 확인 가능한 사실과 실무 판단 기준을 제시하는 데 목적이 있으며, 최종 판단은 각 사 법무 검토를 거친다.
{{% /alert %}}

## AI 오픈소스SW 가이드 - 기업 편

### AI 자산을 기존 오픈소스SW 거버넌스에 편입한다

#### 새 체계를 만들지 않는다 — 반입 승인·대장 등록·SBOM·고지·배포 승인 5단계에 '자산 유형'을 추가한다

이미 오픈소스SW 거버넌스를 운영 중인 기업이라면 AI 자산을 위해 프로세스를 새로 설계할 필요가 없다. 기존 5단계는 그대로 두고 각 단계에서 확인할 항목만 자산 유형별로 나눈다. 다음 표는 각 단계에서 소프트웨어 컴포넌트와 AI 모델·데이터셋의 확인 항목이 어떻게 갈라지는지 대조한 것이다. 자사 프로세스 문서와 나란히 놓고 빠진 항목을 찾는 용도로 쓴다.

| 기존 단계 | 소프트웨어 컴포넌트일 때 | AI 모델·데이터셋일 때 | 이 가이드의 참조 위치 |
|---|---|---|---|
| 반입 승인 | 컴포넌트 단위 라이선스 확인과 승인 요청 | 모델 라이선스·AUP<sub>Acceptable Use Policy</sub>·지역 제한 확인 | [모델 라이선스 실사](#모델-라이선스-실사), [「오픈소스SW 사용하기」](../using/) |
| 대장 등록 | 컴포넌트명·버전·라이선스 기록 | 개방성 등급, 베이스 모델 계보, 데이터셋 참조를 추가 기록 | [사내 표기 규칙 — 모델 대장의 '개방성 등급' 컬럼](#사내-표기-규칙--모델-대장의-개방성-등급-컬럼) |
| SBOM | SPDX·CycloneDX 컴포넌트 항목으로 표현 | SPDX AIPackage 또는 CycloneDX modelCard로 표현 | [「오픈소스SW 사용하기」](../using/)의 SBOM 관리 절 |
| 고지 | NOTICE 파일과 라이선스 전문 고지 | NOTICE 문구, 'Built with Llama' 류 표시, AI 기본법 고지를 함께 처리 | [한국 AI 기본법의 고지·표시 의무 — 오픈소스SW 모델도 면제되지 않는다](#한국-ai-기본법의-고지표시-의무--오픈소스sw-모델도-면제되지-않는다) |
| 배포 승인 | 배포 형태별 의무 이행 확인 | 파생 모델 명명 규칙, 라이선스 사본 동봉, AUP 전가 확인 | [파인튜닝 결과물의 라이선스 승계 — 5개 항목 배포 승인 체크리스트](#파인튜닝-결과물의-라이선스-승계--5개-항목-배포-승인-체크리스트), [「오픈소스SW 공개하기」](../releasing/) |

기존 컴포넌트 관리 대장에 '자산 유형' 컬럼(라이브러리 / 모델 / 데이터셋)을 추가하고 유형별 필수 필드를 다르게 정의하면 위 표가 그대로 대장 스키마가 된다.

승인 권한도 새로 만들지 않는다. AI 자산의 반입·배포 승인은 기존 오픈소스SW 승인 주체가 그대로 맡고 자산 유형별 확인 항목만 더한다. 다만 판단에 필요한 지식이 갈리므로 두 가지를 별도로 지정한다. 첫째, 모델·데이터셋 라이선스 원문 판정과 개방성 등급 기록의 소유자를 정한다 — 대장의 등급 값이 조달 문서와 제품 고지에 그대로 인용되기 때문이다. 둘째, 커스텀 라이선스 모델의 상업적 사용과 파생물 배포는 법무 검토를 거치는 경로로 고정한다. 오픈소스 프로그램을 운영하는 조직이라면 이 두 항목을 담당 업무 목록에 더하고, 조직을 어떻게 구성하고 인원을 배치할지는 [「OSPO」](../ospo/)에서 다룬다.

{{< imgproc ai-asset-governance-integration Fit "768x768" >}}
<center><i>[AI 자산의 기존 오픈소스SW 거버넌스 편입 구조]</i></center>
{{< /imgproc >}}

#### 신규로 필요한 것은 세 가지뿐이다 — 모델 버전 단위 라이선스 기록, 데이터셋의 독립 자산 등록, 스니펫 매칭 게이트

기존 프로세스에 없던 항목은 다음 세 가지다. 이 셋 외의 신규 단계를 임의로 늘리지 않는다.

1. **모델 버전 단위 라이선스 기록** — 같은 제품군 안에서 세대별로 라이선스가 갈리므로 '모델군' 단위로 기록하면 오판이 생긴다. 실제 사례는 [Gemma — 같은 제품군 안에서 라이선스가 갈린다(Gemma 3 이하 vs Gemma 4)](#gemma--같은-제품군-안에서-라이선스가-갈린다gemma-3-이하-vs-gemma-4)에서 다룬다.
2. **데이터셋의 독립 자산 등록** — 모델 라이선스와 데이터셋 라이선스는 별개이고, 데이터셋 라이선스 표기 자체의 신뢰도가 낮다. 근거와 등록 필드는 [데이터셋 거버넌스](#데이터셋-거버넌스)에서 다룬다.
3. **스니펫 매칭 게이트** — 기존 SCA<sub>Software Composition Analysis</sub>는 package manifest를 근거로 삼기 때문에 코드에 직접 써 넣어진 복사 조각을 보지 못한다. 검출 원리의 차이는 [의존성 SCA는 복사된 코드 조각을 보지 못한다 — 스니펫 매칭이 필요한 이유](#의존성-sca는-복사된-코드-조각을-보지-못한다--스니펫-매칭이-필요한-이유)에서 다룬다.

### '오픈소스 AI'라는 말의 기준

이 절의 목적은 사내 문서·조달 문서·제품 고지에서 어떤 모델을 '오픈소스SW'로 부를 수 있는지 판정하는 것이다.

#### OSAID 1.0의 3요소 — 데이터 정보·코드·파라미터

OSI<sub>Open Source Initiative</sub>의 Open Source AI Definition(OSAID) 1.0은 다음 세 요소를 '수정을 위한 선호 형태(preferred form to make modifications)'로 요구한다[^ai-osaid].

- **데이터 정보(Data Information)** : 'Sufficiently detailed information about the data used to train the system so that a skilled person can build a substantially equivalent system'
- **코드(Code)** : 'The complete source code used to train and run the system'
- **파라미터(Parameters)** : 'The model parameters, such as weights or other configuration settings'

두 가지 사실을 함께 확인한다. 첫째, OSAID는 2024-10-28 공개된 1.0이 2026-07-31 현재도 유일한 안정판이며 v1.1과 v2.0은 미발표다. 둘째, OSI는 개별 AI 시스템을 인증하지 않는다 — 정의 수립 과정의 검증 단계에서 Pythia(EleutherAI), OLMo(AI2), Amber·CrystalCoder(LLM360), T5(Google)가 통과했으나 OSI는 'These results should be seen as part of the definitional process... they are not certifications of any kind. OSI will continue to validate only legal documents and will not validate or review individual AI systems'라고 명시했다[^ai-osaid-faq]. 인증 제도가 존재하지 않으므로 '오픈소스SW 인증 모델'이라는 표현을 사내 금지 어휘로 등록한다.

[^ai-osaid]: Open Source Initiative, The Open Source AI Definition – 1.0 : https://opensource.org/ai/open-source-ai-definition
[^ai-osaid-faq]: Open Source Initiative, OSAID FAQs : https://opensource.org/ai/faq

#### 결론이 나지 않은 논쟁 — SFC·FSF·Debian의 비판

OSAID를 확정된 표준처럼 인용하면 사내 정책이 한쪽 입장에만 서게 된다. 세 진영의 비판이 남아 있다. Software Freedom Conservancy의 Bradley Kuhn은 2024-10-31 블로그에서 'the OSAID fails to place sufficient requirements on the licensing and public disclosure of training sets'라고 비판했다[^ai-sfc-osaid]. FSF는 학습 데이터와 그 처리 스크립트까지 자유 소프트웨어여야 한다는 더 엄격한 입장으로 알려져 있으나, 2026-08 기준 확정 공개된 기준 문서는 확인되지 않았다. Debian에서는 개발자 Mo Zhou가 OSAID-1.0-RC2 단계에서 데이터 정보만 요구하면 오픈소스 AI가 원본 학습 데이터를 감출 수 있게 된다는 반대 의견을 debian-project 메일링 리스트에 제출하고, 이 문제에 대한 프로젝트 차원의 합의 절차를 제안했다[^ai-debian-osaid].

세 비판의 공통 쟁점은 원본 학습 데이터가 아니라 데이터 정보만 요구한 타협이다. 이 논쟁은 종결되지 않았다. 따라서 사내 정책에서 'OSAID 준수'를 단일 판정 기준으로 삼지 않고, 최소 요건(라이선스 조항 실사)과 권고 요건(데이터 출처 공개 수준)을 분리해 규정한다.

[^ai-sfc-osaid]: Software Freedom Conservancy, Open Source AI Definition Erodes the Meaning of "Open Source" : https://sfconservancy.org/blog/2024/oct/31/open-source-ai-definition-osaid-erodes-foss/
[^ai-debian-osaid]: debian-project 메일링 리스트, Concerns regarding the "Open Source AI Definition" 1.0-RC2 : https://lists.debian.org/debian-project/2024/10/msg00005.html

#### G7 개방성 4단계 표기 체계 (2026-05-29)

2026-05-29 파리에서 열린 G7 디지털·기술 장관회의는 'G7 Vision on AI openness opportunities and shared language'를 승인해 AI 개방성을 4단계로 구분했다[^ai-g7-openness]. 아래 표는 각 등급이 무엇을 공개하고 어떤 제한을 두는지 대조한 것으로, 사내 용어 표준과 모델 대장의 값 목록을 이 4단계에 맞춘다.

| 등급 | 공개 범위 | 사용 제한 | 적용 예 (이 가이드의 판단) |
|---|---|---|---|
| 데이터 공개 오픈소스 AI | 가중치·배포 코드·학습 코드·전체 학습 데이터를 모두 오픈소스SW 라이선스로 무상 공개 | 없음 | 해당 예를 특정하지 않음 |
| 오픈소스 AI | 가중치·배포 코드·학습 코드를 무상 공개하고 학습 데이터도 전체 공개가 원칙이나, 법적·기술적으로 공유가 불가능한 경우에 한해 그 데이터에 관한 데이터 정보로 대체 | 없음 | 해당 예를 특정하지 않음 |
| 가중치 공개 AI | 가중치와 배포 코드를 오픈소스SW 라이선스로 무상 공개 | 없음 | Gemma 4, Qwen3, gpt-oss |
| 가중치 제공 AI[^ai-g7-weights-available] | 가중치와 배포 코드를 무상 공개하나 라이선스에 사용 제한 포함 | 상업·지역·용도 제한 | Llama 4, Gemma 3 |

마지막 열은 G7 문서에서 온 것이 아니다. G7 문서 본문에는 모델명이 한 건도 등장하지 않는다. 위 '적용 예'는 각 모델의 라이선스와 공개 구성요소를 이 가이드가 등급 정의에 대조해 넣은 것이다. 따라서 사내 문서나 조달 문서에 인용할 때는 등급 정의와 공개 범위까지만 국제 준거로 쓰고, 특정 모델의 등급은 그 모델의 라이선스 원문을 직접 확인해 판정한다. 모델 라이선스는 개정되므로 등급도 함께 바뀐다.

이 문서는 'This document constitutes a non-binding reference'라고 스스로 밝힌 비구속 준거이며, 법적 의무를 만들지 않는다. 그럼에도 사내 표기 기준으로 쓸 가치가 있는 이유는 원칙 4에 있다 — 'any description of an AI as "open" should clearly state which components are made available, whether with or without restrictions, rather than using the term "open" as a blanket characterization'. 문서는 목적에 open washing 방지를 명시한다[^ai-g7-declaration].

[^ai-g7-openness]: G7, Vision on AI openness opportunities and shared language (PDF) : https://www.entreprises.gouv.fr/files/files/Actualites/2026/g7/vision-AI-openness-opportunities-and-shared-language.pdf
[^ai-g7-weights-available]: '가중치 제공 AI'는 가중치와 배포 코드를 무상으로 받을 수는 있으나 상업·지역·용도 등 사용 제한이 라이선스에 붙는 등급이다. G7 문서의 'Weights Available AI'에 대응하며, 한글 정착 표기가 없어 이 가이드에서 정한 표기다. 출처는 위 G7 문서와 같다.
[^ai-g7-declaration]: GOV.UK, G7 Digital and Technology Ministerial Declaration, 29 May 2026 : https://www.gov.uk/government/publications/g7-digital-and-technology-ministerial-declaration-29-may-2026/g7-digital-and-technology-ministerial-declaration-29-may-2026

{{< imgproc ai-openness-tiers-g7 Fit "768x768" >}}
<center><i>[G7 AI 개방성 4단계와 공개 구성요소]</i></center>
{{< /imgproc >}}

#### 사내 표기 규칙 — 모델 대장의 '개방성 등급' 컬럼

앞의 두 기준을 사내에서 실제로 운영하려면 모델 등록 대장에 '개방성 등급' 컬럼을 필수 항목으로 둔다. 값은 자유 입력을 막고 다음 다섯 개로 고정한다. G7 4단계를 그대로 채택하는 이유는 그것이 국제 준거이기 때문이며, 벤더 API만 사용하는 경우를 담기 위해 '비공개' 하나를 더한다.

```text
[모델 등록 대장 — '개방성 등급' 컬럼 정의]

컬럼명     : 개방성 등급 (필수)
입력 방식   : 드롭다운 (자유 입력 금지)
허용 값     : 1) 데이터 공개 오픈소스 AI
             2) 오픈소스 AI
             3) 가중치 공개 AI
             4) 가중치 제공 AI
             5) 비공개 (벤더 API만 제공)
함께 기록   : 라이선스 원문 URL, 원문 확인 일자, 판정자
```

이 컬럼을 강제하는 이유는 두 가지 실무 위험 때문이다. 첫째, 조달 문서에 '오픈소스 AI 사용'으로 기재해 발주처의 오픈소스SW 정책 심사를 통과했으나 실제로는 사용 제한이 있는 커스텀 라이선스인 경우가 있다. 둘째, 같은 오인이 사내 오픈소스SW 승인 프로세스를 우회하는 통로가 된다. '라이선스 미표기'가 곧 '오픈소스SW'로 읽히기 쉬운 배경에는 Hugging Face 모델의 약 70%가 라이선스 표기 자체가 없다는 실태가 있다[^ai-redmonk-hf]. 상세 수치와 개발자 단계의 대응은 [라이선스 미표기는 '오픈소스SW'가 아니라 '모든 권리 유보'다 — Hugging Face 실태](#라이선스-미표기는-오픈소스sw가-아니라-모든-권리-유보다--hugging-face-실태)에서 다룬다.

[^ai-redmonk-hf]: RedMonk, License Distribution on Hugging Face (2026-05-12, 2차 출처 — 저자는 저작권 위반 모델을 걸러낼 수 없고 라이선스 분류 정확도를 보장할 수 없다는 한계를 명시했다) : https://redmonk.com/sogrady/2026/05/12/hugging-face-licensing/

### 모델 라이선스 실사

이 절은 모델을 반입할 때 라이선스 원문에서 무엇을 확인하는가를 벤더별로 정리한다.

#### Llama 4 — 700M MAU 임계, 'Built with Llama' 표시, 파생 모델 명칭 접두어

Llama 4 Community License(Version Effective Date: April 5, 2025)는 OSI 승인 라이선스가 아니다. 반입 시 확인할 의무는 다음 네 가지다[^ai-llama4-license].

1. **사용자 수 임계** — 'If, on the Llama 4 version release date, the monthly active users of the products or services made available by or for Licensee, or Licensee's affiliates, is greater than 700 million monthly active users in the preceding calendar month, you must request a license from Meta'(제2조).
2. **계약서 사본 동봉과 표시 의무** — 배포 시 계약서 사본을 함께 제공하고, 관련 웹사이트·사용자 인터페이스·블로그 게시물·about 페이지·제품 문서 가운데 한 곳에 'Built with Llama'를 눈에 띄게 표시한다(제1.b.i).
3. **파생 모델 명칭 접두어** — Llama Materials나 그 출력물·결과물로 AI 모델을 만들거나 학습·파인튜닝해 배포하는 경우 그 모델 명칭 앞에 'Llama'를 붙인다(제1.b.i 후단).
4. **NOTICE 문구** — NOTICE 파일에 'Llama 4 is licensed under the Llama 4 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved.'를 그대로 삽입한다.

제5조는 상표 라이선스를 원칙적으로 부여하지 않으면서 'Llama' 표장 사용을 위 명칭 의무 이행 목적으로만 허여하고 Meta의 브랜드 가이드라인 준수를 요구한다. 제1.b.iv는 Acceptable Use Policy 준수를 의무화한다. 700M MAU 임계는 국내 대부분 기업에 걸리지 않는다. 다만 조항이 'Licensee, or Licensee's affiliates'를 함께 세므로 계열사 합산 기준을 확인한다.

[^ai-llama4-license]: Meta, LLAMA 4 COMMUNITY LICENSE AGREEMENT : https://github.com/meta-llama/llama-models/blob/main/models/llama4/LICENSE

#### 라이선스 본문 밖에 있는 제한 — Llama 4 멀티모달의 EU 조항

Llama 4의 멀티모달 모델에 대해서는 'the rights granted under Section 1(a) of the Llama 4 Community License Agreement are not being granted to you if you are an individual domiciled in, or a company with a principal place of business in, the European Union'이라는 제한이 붙는다. 이 제한은 LICENSE 파일이 아니라 USE_POLICY.md(Acceptable Use Policy)에 있다[^ai-llama4-aup].

같은 조항은 'This restriction does not apply to end users of a product or service that incorporates any such multimodal models'라고 이어진다. 즉 EU 밖 법인이 만든 제품을 EU 최종 사용자가 사용하는 것은 허용된다. 이 구분을 빠뜨리면 필요 이상으로 넓은 금지 정책을 만들게 된다. 국내 기업에 실제로 문제가 되는 경우는 EU 자회사, EU 소재 연구소, EU 소재 외주 개발사를 통해 해당 모델을 다루는 때다.

이 사례의 교훈은 특정 벤더가 아니라 절차에 있다. 모델 승인 프로세스에 '라이선스 본문 외 부속 문서(AUP / Use Policy / Prohibited Use Policy) 확인' 단계를 필수화한다. 모델 대장에는 '지역 제한'과 '개발 수행 법인 소재지' 컬럼을 추가한다.

[^ai-llama4-aup]: Meta, Llama 4 Acceptable Use Policy (USE_POLICY.md) : https://github.com/meta-llama/llama-models/blob/main/models/llama4/USE_POLICY.md

#### 흔한 오해 정정 — 증류 금지 조항은 Llama 3.1부터 삭제됐다

Llama 2와 Llama 3 라이선스에는 'You will not use the Llama Materials or any output or results of the Llama Materials to improve any other large language model (excluding Meta Llama 3 or derivative works thereof)'라는 조항이 있었다[^ai-llama3-license]. 이 문장은 2024-07-23 공개된 Llama 3.1부터 삭제되었고 Llama 4 LICENSE에도 없다[^ai-llama4-license]. 출력물로 다른 모델을 학습시킬 때 남는 의무는 파생 모델 명칭 앞에 'Llama'를 붙이는 것뿐이다.

2차 해설 가운데 Llama 4에 학습 금지나 경쟁사 제한이 있다고 서술한 것이 다수 있으나 원문과 일치하지 않는다. 여기서 얻을 일반 교훈은 하나다 — 버전별 LICENSE 원문을 직접 대조하고, 사내 위키에 요약본만 두는 대신 버전별 원문 스냅샷을 보관한다.

[^ai-llama3-license]: Meta, llama3/LICENSE at main (meta-llama/llama3) : https://github.com/meta-llama/llama3/blob/main/LICENSE

#### Gemma — 같은 제품군 안에서 라이선스가 갈린다(Gemma 3 이하 vs Gemma 4)

Gemma 4는 Apache-2.0으로 공개됐다. Google Open Source Blog는 2026-04-02 게시글에서 'Gemma 4 models are the first in the Gemmaverse to be released under the OSI-approved Apache 2.0 license'라고 밝혔다[^ai-gemma4]. 반면 Gemma 3 이하에는 커스텀 Gemma Terms of Use(최종 수정 2026-04-01)와 Prohibited Use Policy가 그대로 적용된다[^ai-gemma-terms]. 구세대에 남는 의무는 다음 네 가지다.

1. **계약서 사본 제공** — 'You must provide all third party recipients of Gemma or Model Derivatives a copy of this Agreement'.
2. **NOTICE 파일 동봉** — Hosted Service를 통하지 않는 모든 배포에 'Gemma is provided under and subject to the Gemma Terms of Use found at ai.google.dev/gemma/terms' 문구를 담은 'Notice' 텍스트 파일을 동봉한다.
3. **원격 사용 제한권** — Google은 계약 위반이라고 합리적으로 판단하는 Gemma Services의 사용을 원격으로 제한할 권리를 유보한다.
4. **상표 권리 불허여** — 계약은 Google의 상표·상호·로고에 대한 어떤 권리도 부여하지 않는다.

'Model Derivatives' 정의는 가중치·파라미터·연산의 전이로 만들어진 다른 머신러닝 모델까지 포함하므로 증류 결과물도 포섭된다. 반면 출력물에 대해서는 'Google claims no rights in Outputs you generate using Gemma'로 권리를 주장하지 않는다. 실무 결론은 [신규로 필요한 것은 세 가지뿐이다 — 모델 버전 단위 라이선스 기록, 데이터셋의 독립 자산 등록, 스니펫 매칭 게이트](#신규로-필요한-것은-세-가지뿐이다--모델-버전-단위-라이선스-기록-데이터셋의-독립-자산-등록-스니펫-매칭-게이트)의 첫 항목과 직결된다. Gemma 3 이하 파생물은 Apache-2.0으로 재배포할 수 없다.

[^ai-gemma4]: Google Open Source Blog, Gemma 4: Expanding the Gemmaverse with Apache 2.0 (게시글에 표기된 게시일은 2026-04-02이나 URL 경로에는 2026/03이 들어 있어 서로 어긋난다. 이 가이드는 게시글 표기를 인용했다) : https://opensource.googleblog.com/2026/03/gemma-4-expanding-the-gemmaverse-with-apache-20.html
[^ai-gemma-terms]: Google AI for Developers, Gemma Terms of Use : https://ai.google.dev/gemma/terms

#### Mistral — 한 벤더 안의 3원 구조와 PoC→프로덕션 전환 게이트

Mistral은 모델별로 Apache-2.0, Mistral Research License, Mistral AI Non-Production License(MNPL)를 섞어 쓴다. 벤더 이름만으로 라이선스를 추정할 수 없다는 뜻이다. MNPL-0.1의 제한은 다음과 같이 보고된다[^ai-mnpl].

- 사용 범위는 'testing, research, Personal, or evaluation purposes in Non-Production Environments'로 한정된다.
- 'Subject to the foregoing, You shall not supply the Mistral Models or Derivatives in the course of a commercial activity, whether in return for payment or free of charge, in any medium or form, including but not limited to through a hosted or managed service (e.g. SaaS, cloud instances, etc.), or behind a software layer.' (제3.2조) — 다만 같은 라이선스는 'Outputs are not considered as Derivatives'(정의 조항)와 'We claim no ownership rights in and to the Outputs'(제4.2조)를 함께 두므로, 출력물 자체의 취급은 이 금지 조항과 구분해 판단한다.
- 파생물 배포 시 수정 사실을 눈에 띄게 고지한다.
- 특허 소송을 제기하면 라이선스가 즉시 종료된다.
- 상업적 사용은 license@mistral.ai로 별도 요청한다.

이 절의 결론은 벤더 소개가 아니라 게이트 설계다. 'PoC 단계에서 사용한 모델의 라이선스를 프로덕션 전환 시점에 재확인한다'를 승인 프로세스의 항목으로 명시한다. 가장 흔한 위반 경로는 '연구용으로 받았으니 그대로 서비스한다'이다.


[^ai-mnpl]: Mistral AI, Mistral AI Non-Production License (MNPL-0.1), 2026-07-31 확인 : https://mistral.ai/licenses/MNPL-0.1.md

#### 자사 모델을 공개할 때의 라이선스 선택 — Apache-2.0 / OpenMDW / 커스텀 3택 결정 트리

여기까지가 외부 모델을 가져다 쓰는 관점이었다면, 이 항은 자사 모델을 내보내는 관점이다. 배포물의 구성과 사용 제한 필요 여부에 따라 다음 세 갈래로 판단한다.

| 조건 | 선택 | 유의 사항 |
|---|---|---|
| 코드 중심 배포이고 사용 제한이 필요 없다 | Apache-2.0 | OSI 승인 라이선스이며 특허 조항을 포함한다 |
| 모델 가중치·코드·데이터·문서를 한 배포물로 내보내 라이선스 조각화를 피하려 한다 | OpenMDW | 승인 여부는 아래 서술 참조. 배포물 구성 요소를 'Model Materials' 하나로 덮는다 |
| 사용 제한이 반드시 필요하다 | 커스텀 라이선스 | 법무 승인 필수. EU AI Act 오픈소스SW 예외를 받지 못한다 |

OpenMDW는 Linux Foundation이 2026-05-28 OpenMDW-1.1을 공개했고, NVIDIA가 Cosmos·Isaac GR00T·Ising·Nemotron 모델군의 '향후 릴리스'부터 채택하겠다고 발표했다(현재 배포본의 적용 여부는 모델별로 확인한다)[^ai-openmdw-lf]. SPDX License List 최신판 3.28.0(2026-02-20)에는 OpenMDW-1.0만 등재되어 있어 1.1에는 아직 표준 식별자가 없다 — SBOM에는 LicenseRef- 형태로 기록하고 라이선스 원문을 첨부한다[^ai-spdx-list]. 다만 OSI 승인 여부는 공식 페이지에 언급이 없어 확인되지 않는다 — 'OSI 승인 라이선스다'라고 표기하지 않는다[^ai-openmdw].

커스텀 라이선스를 선택하면 [EU AI Act의 오픈소스SW 예외는 좁다 — 무엇이 예외를 깨는가](#eu-ai-act의-오픈소스sw-예외는-좁다--무엇이-예외를-깨는가)에서 다루는 예외가 깨진다. 공개 절차 자체(공개 심의, 저장소 준비, 커뮤니티 운영)는 [「오픈소스SW 공개하기」](../releasing/)에서 다룬다.


[^ai-openmdw-lf]: Linux Foundation, Linux Foundation Releases OpenMDW-1.1; NVIDIA Adopts OpenMDW : https://www.linuxfoundation.org/press/linux-foundation-releases-openmdw-1.1-nvidia-adopts-openmdw-for-cosmos-isaac-gr00t-ising-and-nemotron-ai-model-families
[^ai-spdx-list]: SPDX License List 3.28.0 : https://spdx.org/licenses/
[^ai-openmdw]: OpenMDW 공식 사이트 : https://openmdw.ai/

#### 행위 제한형 라이선스(OpenRAIL) — 제한이 파생물과 최종 사용자까지 전파된다

OpenRAIL 계열 라이선스는 상업적 사용을 허용하면서도 감시·추적, 허위정보 생성, 차별 등의 용도를 금지하고, 그 제한을 파생물에도 같거나 더 엄격한 형태로 부착할 것을 요구한다[^ai-openrail]. 사용 제한이 있으므로 OSI 승인 라이선스가 아니다. OSI는 'Should OpenRAIL licenses be considered OS AI Licenses?' 웨비나를 열어 이 문제를 논의했으나 승인하지 않았다[^ai-openrail-osi]. RedMonk의 2026-05-12 분석은 OpenRAIL을 OSI 비승인·모델 비특정 라이선스 가운데 가장 큰 카테고리로 분류했다[^ai-redmonk-hf].

실무 결론은 하나다. 행위 제한 조항을 자사 서비스 이용약관에 그대로 전가(pass-through)해야 하는지를 법무 검토 항목으로 등록한다. 제한이 파생물과 최종 사용자까지 전파되도록 설계되어 있으므로 약관 미반영은 계약 위반 소지가 된다. 이미지·음성 생성 모델을 제품에 탑재하는 조직이 주 대상이다.

[^ai-openrail]: Responsible AI Licenses (RAIL) FAQ : https://www.licenses.ai/faq-2
[^ai-openrail-osi]: Open Source Initiative, Should OpenRAIL licenses be considered OS AI Licenses? (웨비나) : https://opensource.org/ai/webinars/should-openrail-licenses-be-considered-os-ai-licenses

#### 파인튜닝 결과물의 라이선스 승계 — 5개 항목 배포 승인 체크리스트

파인튜닝 결과물은 베이스 모델 라이선스의 파생물 정의에 포섭되는 것이 일반적이다. Llama 4는 '(or any derivative works thereof)'와 '(including another AI model) that contains any of them'으로 파생 AI 모델을 명시적으로 포섭하고[^ai-llama4-license], Gemma Terms of Use의 'Model Derivatives'는 가중치·파라미터·연산의 전이로 만들어진 모델까지 포함한다[^ai-gemma-terms]. 배포 승인 시 다음 다섯 항목을 확인한다.

| 확인 항목 | 어디를 보는가 |
|---|---|
| 베이스 모델 라이선스 사본 동봉 | Llama 4 제1.b.i, Gemma Terms of Use의 제3자 수령인 조항 |
| NOTICE 파일 문구 | Llama 4 NOTICE 지정 문구, Gemma Terms of Use의 Notice 텍스트 파일 요구 |
| 모델 명칭 규칙 | Llama 4 제1.b.i 후단(명칭 접두어) |
| AUP 전가 여부 | Llama 4 제1.b.iv, Gemma Prohibited Use Policy |
| 지역 제한 여부 | Llama 4 USE_POLICY.md의 EU 조항 |

서술 강도에 주의한다. 이들 라이선스의 강제력은 저작권이 아니라 계약(약관 수락)에 근거한다는 해석이 유력하다. 또한 미국 저작권청이 순수 AI 생성물의 저작물성을 부정하는 입장이어서 가중치의 저작물성 자체가 다투어질 수 있다[^ai-uscopyright]. 따라서 '저작권 침해가 된다'로 단정하지 않고 '계약 위반 리스크가 실재한다' 수준으로 판단한다. 개발자가 배포 직전에 손으로 확인할 항목은 [파인튜닝 결과물을 배포하기 전에 확인할 것](#파인튜닝-결과물을-배포하기-전에-확인할-것)에 별도로 두었다.

{{< imgproc model-license-inheritance Fit "768x768" >}}
<center><i>[파생 모델의 라이선스 의무 승계 경로]</i></center>
{{< /imgproc >}}

#### 모델 라이선스 검토 체크리스트 (종합)

- [ ] 라이선스 원문을 모델 **버전별로** 직접 확인했는가 → [흔한 오해 정정 — 증류 금지 조항은 Llama 3.1부터 삭제됐다](#흔한-오해-정정--증류-금지-조항은-llama-31부터-삭제됐다)
- [ ] LICENSE 외 부속 문서(AUP·Use Policy·Prohibited Use Policy)를 확인했는가 → [라이선스 본문 밖에 있는 제한 — Llama 4 멀티모달의 EU 조항](#라이선스-본문-밖에-있는-제한--llama-4-멀티모달의-eu-조항)
- [ ] 사용자 수 임계나 매출 임계 조항이 있는가 → [Llama 4 — 700M MAU 임계, 'Built with Llama' 표시, 파생 모델 명칭 접두어](#llama-4--700m-mau-임계-built-with-llama-표시-파생-모델-명칭-접두어)
- [ ] 지역 제한이 있는가 → [라이선스 본문 밖에 있는 제한 — Llama 4 멀티모달의 EU 조항](#라이선스-본문-밖에-있는-제한--llama-4-멀티모달의-eu-조항)
- [ ] 파생물·증류물이 파생 정의에 포섭되는가 → [Gemma — 같은 제품군 안에서 라이선스가 갈린다(Gemma 3 이하 vs Gemma 4)](#gemma--같은-제품군-안에서-라이선스가-갈린다gemma-3-이하-vs-gemma-4)
- [ ] 배포 시 명칭 규칙·표시 의무·NOTICE 문구가 있는가 → [파인튜닝 결과물의 라이선스 승계 — 5개 항목 배포 승인 체크리스트](#파인튜닝-결과물의-라이선스-승계--5개-항목-배포-승인-체크리스트)
- [ ] 상표 사용 조건이 있는가 → [Llama 4 — 700M MAU 임계, 'Built with Llama' 표시, 파생 모델 명칭 접두어](#llama-4--700m-mau-임계-built-with-llama-표시-파생-모델-명칭-접두어)
- [ ] 행위 제한을 자사 약관에 전가해야 하는가 → [행위 제한형 라이선스(OpenRAIL) — 제한이 파생물과 최종 사용자까지 전파된다](#행위-제한형-라이선스openrail--제한이-파생물과-최종-사용자까지-전파된다)
- [ ] 상업 사용이 별도 요청 대상인가 → [Mistral — 한 벤더 안의 3원 구조와 PoC→프로덕션 전환 게이트](#mistral--한-벤더-안의-3원-구조와-poc프로덕션-전환-게이트)
- [ ] 모델 대장의 개방성 등급을 무엇으로 기록하는가 → [사내 표기 규칙 — 모델 대장의 '개방성 등급' 컬럼](#사내-표기-규칙--모델-대장의-개방성-등급-컬럼)

### 데이터셋 거버넌스

데이터셋은 모델에 딸린 부속물이 아니라 별도 자산이다. 모델을 승인했다는 사실이 그 모델의 학습 데이터셋을 승인했다는 뜻은 아니다.

#### 모델 라이선스와 데이터셋 라이선스는 별개다 — 누락률 70% 이상, 오류율 50% 이상

Data Provenance Initiative는 1,800개 이상의 텍스트 AI 데이터셋을 감사해 인기 데이터셋 호스팅 사이트에서 'licence omission rates of more than 70% and error rates of more than 50%'를 확인했다고 보고했다[^ai-dpi-audit]. 실무 함의는 세 가지다.

1. 모델이 Apache-2.0이어도 학습에 사용한 데이터셋이 CC-BY-NC이거나 출처 불명일 수 있다.
2. 데이터셋 카드의 라이선스 필드를 그대로 SBOM에 옮기면 오류가 그대로 전파된다.
3. 저자원 언어, 창작 태스크, 합성 데이터는 제한적으로 라이선스되는 경향이 강하다.

EU 시장에 모델을 출하하는 경우 학습 콘텐츠 공개 요약 의무와 직결되므로 [EU AI Act의 오픈소스SW 예외는 좁다 — 무엇이 예외를 깨는가](#eu-ai-act의-오픈소스sw-예외는-좁다--무엇이-예외를-깨는가)를 함께 확인한다.

[^ai-dpi-audit]: Nature Machine Intelligence(피어리뷰, 2024-08), A large-scale audit of dataset licensing and attribution in AI : https://www.nature.com/articles/s42256-024-00878-8

#### 데이터셋 등록 필수 5개 필드 — 출처 URL·라이선스·취득일·사용 목적·재배포 가부

다음 다섯 필드는 데이터셋을 독립 자산으로 등록할 때의 최소 단위다. 사내 자산 대장 스키마에 그대로 옮겨 쓴다.

| 필드 | 기록 규칙 | 확인 방법 |
|---|---|---|
| 출처 URL | 데이터셋 카드 주소가 아니라 원 배포처 URL을 기록한다 | 카드에 적힌 원 배포처 링크를 따라가 접속 확인 |
| 라이선스 | 데이터셋 카드 표기를 그대로 옮기지 않는다 | 원 배포처의 라이선스 표기와 교차 확인하고 불일치 시 원 배포처를 따른다 |
| 취득일 | 버전 대신 스냅샷 기준일을 기록한다(데이터셋은 갱신된다) | 내려받은 날짜와 커밋·리비전 식별자를 함께 남긴다 |
| 사용 목적 | 학습 / 평가 / 파인튜닝을 구분해 기록한다 | 목적별로 허용 범위가 달라지므로 용도 변경 시 재등록한다 |
| 재배포 가부 | 모델과 함께 배포할 수 있는지 여부를 가/부로 기록한다 | 라이선스 원문의 재배포 조항을 확인하고 근거 조항 번호를 남긴다 |

SBOM에 표기할 때는 SPDX AIPackage 또는 CycloneDX modelCard를 사용한다. 단계별 대응은 [새 체계를 만들지 않는다 — 반입 승인·대장 등록·SBOM·고지·배포 승인 5단계에 '자산 유형'을 추가한다](#새-체계를-만들지-않는다--반입-승인대장-등록sbom고지배포-승인-5단계에-자산-유형을-추가한다)의 표를 참조한다.

#### 코드 학습 데이터셋의 라이선스 혼입 — The Stack v2 사례

The Stack v2는 600개 이상의 언어, 67.5TB 규모로 '허용적 라이선스 또는 라이선스 없음' 코드를 수집한다[^ai-bigcode-stack]. '라이선스 없음(no license)'은 저작권상 모든 권리가 유보된 상태이므로 포함 자체가 쟁점이다.

'Cracks in The Stack' 연구는 'Misidentified blob origins present an additional challenge, as they lead to the inclusion of non-permissively licensed code, raising serious compliance concerns'라고 보고했다. 같은 연구는 중복 제거 후에도 알려진 CVE 6,947건에 취약한 blob이 남아 있으며 코드 버전의 17%가 구버전이라고 밝혔다[^ai-stack-cracks]. BigCode는 저장소 소유자를 위한 opt-out 절차와 'Am I in The Stack' 도구를 운영한다[^ai-bigcode-optout].

이 사례에서 정할 것은 벤더 주장에 대한 태도다. 'AI 도구가 허용적 라이선스 코드만 학습했다'는 주장을 리스크 제거의 근거로 채택하지 않는다. 대신 스니펫 매칭 검사를 릴리스 게이트에 넣는다. 검사 구성은 [릴리스 전 3중 검사 — 의존성 SCA / 스니펫 매칭(diff 기준) / AI 도구 로그](#릴리스-전-3중-검사--의존성-sca--스니펫-매칭diff-기준--ai-도구-로그)에서 다룬다.

[^ai-bigcode-stack]: BigCode, The Stack v2 데이터셋 카드(658개 언어, full 67.53TB, '허용적 라이선스 또는 라이선스 없음') : https://huggingface.co/datasets/bigcode/the-stack-v2
[^ai-stack-cracks]: Cracks in The Stack: Hidden Vulnerabilities and Licensing Risks in LLM Pre-Training Datasets (arXiv 2501.02628, LLM4Code 2025 워크숍 채택, 피어리뷰) : https://arxiv.org/abs/2501.02628
[^ai-bigcode-optout]: bigcode-project/opt-out-v2 : https://github.com/bigcode-project/opt-out-v2

### AI 규제와 미확정 쟁점

이 절은 확정된 의무(EU·한국)와 미확정 쟁점(저작물성·소송·벤더 면책)을 분리해 다룬다.

#### EU AI Act의 오픈소스SW 예외는 좁다 — 무엇이 예외를 깨는가

집행위의 2025-07-18 'Guidelines on the scope of obligations for general-purpose AI models'는 GPAI 오픈소스SW 예외의 범위를 아래와 같이 해석한다[^ai-eu-gpai-guidelines]. 왼쪽에 해당하는 조건이 하나라도 있으면 예외를 주장할 수 없다.

| 예외를 깨는 것 | 예외를 깨지 않는 것 |
|---|---|
| 비상업·연구 전용 제한 | 귀속 표시 요구 |
| 재배포 금지 | 동일 라이선스 재배포 요구 |
| 사용자 수 임계(user-size thresholds) | 공공 안전 등 고위험 사용에 대한 합리적·비례적·비차별적 안전장치 |
| 상업 라이선스 강제 | 핵심 기능 무료 접근을 제한하지 않는 선택적 프리미엄 서비스 |
| 이중 라이선스(학술 무료 / 상업 유료) | |
| 지원·유지보수·업데이트·호스팅 접근 유료화 | |
| 핵심 기능에 대한 필수 결제 | |

세 가지를 함께 확인한다. 첫째, 체계적 위험(systemic risk) GPAI는 오픈소스SW여도 예외 없이 전 의무를 진다. 둘째, 예외가 적용되어도 학습 콘텐츠 공개 요약과 EU 저작권법 준수 정책 의무는 남는다[^ai-eu-article53]. 셋째, 그 직접 결과로 700M MAU 임계를 둔 Llama 4는 이 예외를 받지 못한다.

GPAI 제공자가 관리할 시행 일자는 세 개다[^ai-act]. 이 세 일자는 2026-07-27 발효한 Digital Omnibus로 변경되지 않았다[^ai-omnibus].

- **2025-08-02** — GPAI 제공자 의무(제53·54·55조) 적용 개시(제113조 셋째 문단 (b)).
- **2026-08-02** — 집행위와 AI Office의 GPAI 집행 권한·과징금 부과 개시(제101조 및 제88~94조). AI Office 자체는 2025-08-02부터 존재하며, 이 날 시작되는 것은 조사·과징금 권한이다.
- **2027-08-02** — 2025-08-02 이전 EU 시장에 출시된 기존 GPAI 모델의 소급 준수 기한(제111조(3)).

고위험 시스템 의무의 적용 일자는 같은 개정으로 연기되었으므로 GPAI 일정과 같은 기준일로 관리하지 않는다. 전체 규제 기한은 [「오픈소스SW 사용하기」의 글로벌 SBOM 규제 동향](../using/#글로벌-sbom-규제-동향) 기한표를 단일 기준으로 삼는다.

[^ai-eu-gpai-guidelines]: artificialintelligenceact.eu, Overview of Guidelines for GPAI Models (2차 출처 — 집행위 가이드라인 해설) : https://artificialintelligenceact.eu/gpai-guidelines-overview/
[^ai-eu-article53]: artificialintelligenceact.eu, Article 53: Obligations for Providers of General-Purpose AI Models (2차 출처) : https://artificialintelligenceact.eu/article/53/
[^ai-act]: Regulation (EU) 2024/1689 (AI Act) : https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
[^ai-omnibus]: Regulation (EU) 2026/1744 of 8 July 2026 (Digital Omnibus on AI), OJ L, 2026/1744, 24.7.2026 : https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng

#### 한국 AI 기본법의 고지·표시 의무 — 오픈소스SW 모델도 면제되지 않는다

「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」은 2026-01-22 시행됐다[^ai-kr-aiact]. 제31조(투명성 확보 의무)는 두 가지를 요구한다. 첫째, 고영향 AI 또는 생성형 AI 기반 제품·서비스를 제공할 때 해당 제품·서비스가 그러한 인공지능에 기반해 운용된다는 사실을 이용자에게 사전 고지한다. 둘째, 생성형 AI 결과물에는 그 결과물이 생성형 인공지능에 의해 생성되었다는 사실을 표시한다.

표시 방식은 결과물의 성격에 따라 갈린다. 딥페이크 결과물은 사람이 명확히 인식할 수 있는 가시적 표시가 필요하다. 일반 생성물은 사람 인식 방식과 기계 판독 방식(워터마크·메타데이터) 중에서 선택할 수 있으나, 기계 판독 방식을 택하면 안내 문구나 음성을 최소 1회 제공해야 한다[^ai-kr-aiact-decree].

핵심은 예외의 부재다. 제31조 제4항과 시행령 제23조에 일부 예외(사용이 명백한 경우, 내부 업무 목적 사용 등)가 있으나, 오픈소스 AI를 대상으로 한 예외는 확인되지 않았다. 제재가 붙는 대상은 제31조 제1항의 사전 고지다. 이를 이행하지 않으면 3천만원 이하 과태료이며(법 제43조 제1항 제1호)[^ai-kr-aiact], 같은 항 제2호는 고지가 아니라 국내대리인 미지정을 잡는다. 다만 과학기술정보통신부는 시행령 입법예고 단계에서 '과태료 계도기간을 최소 1년 이상 운영할 계획'이라고 밝혔으므로 실제 부과는 2027년 이후가 될 가능성이 크다[^ai-kr-grace].

실행 지시는 하나다. AI 고지·표시를 기존 오픈소스SW 고지 화면과 같은 위치에 배치해 운영 부담을 줄이고, 오픈소스SW 모델 사용이 면제 사유가 아님을 정책 문서에 명시한다.

[^ai-kr-aiact]: 국가법령정보센터, 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 : https://www.law.go.kr/lsInfoP.do?lsiSeq=268543
[^ai-kr-aiact-decree]: 국가법령정보센터, 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 시행령(시행 2026-01-22) : https://www.law.go.kr/LSW/lsInfoP.do?efYd=20260122&lsiSeq=282879
[^ai-kr-grace]: 대한민국 정책브리핑, "'AI로 생성된 결과물' 고지해야…AI기본법 시행령 입법예고" (과학기술정보통신부, 2025-11-12) : https://www.korea.kr/news/policyNewsView.do?newsId=148954629

#### AI 생성 코드에 저작권이 있는가 — 미국 저작권청의 입장과 국내 미확립

미국 저작권청은 2025-01-29 발표한 Part 2(Copyrightability)에서 프롬프트 입력만으로 만든 순수 AI 생성물의 저작물성을 부정하고 'prompts alone do not provide sufficient human control'이라고 밝혔다. 인간이 선택·배열·실질적 수정을 가한 부분은 사안별로 보호될 수 있다는 입장이다[^ai-uscopyright]. 2025-05-09 사전공개된 Part 3(Generative AI Training)은 학습 목적 이용의 공정이용을 추정할 수 없고 사안별로 판단해야 한다고 보았으며, 새로운 법정 예외의 신설은 불필요하다고 결론지었다[^ai-uscopyright-part3].

한국 저작권법에는 이에 대응하는 유권해석이 별도로 정리되어 있지 않아 국내 적용은 미확립이다. 실무에서는 릴리스 검토 항목 하나로 다룬다 — AI 생성 비중이 높은 산출물을 오픈소스SW로 사외 공개할 때 저작권이 성립하지 않아 라이선스 부여가 무의미해질 수 있다는 점을 검토하고, 인간 기여 기록(리뷰·수정 이력)을 남긴다. 공개 절차는 [「오픈소스SW 공개하기」](../releasing/)에서 다룬다.


[^ai-uscopyright]: U.S. Copyright Office, Copyright and Artificial Intelligence (Part 2: Copyrightability, 2025-01-29) : https://www.copyright.gov/ai/
[^ai-uscopyright-part3]: U.S. Copyright Office, Copyright and Artificial Intelligence Part 3: Generative AI Training (Pre-Publication Version, 2025-05-09, PDF) : https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf

#### Doe v. GitHub — 진행 중이며 결론이 아니다

이 사건은 결론이 아니라 진행 상태로 인용한다. 경과는 다음과 같다[^ai-copilot-litigation].

- 2023-05-11 : 미국 캘리포니아 북부지방법원(Judge Jon S. Tigar)이 오픈소스SW 라이선스 위반(계약 위반) 청구의 기각을 전부 기각하고 DMCA §1202(b)(1)·(b)(3) 청구도 유지했다.
- 2024-12 : §1202(b)가 '동일성(identicality)' 요건을 요구하는지에 대한 중간항소를 제9순회 항소법원이 수리했다.
- 2025-04-09 : 원고 측 opening brief가 제출됐다.
- 2026-02-11 : 구두변론이 열렸고, 2026-07-31 현재 계류 중이며 지방법원 절차는 정지 상태다.

쟁점은 AI 출력물이 원본과 동일하지 않아도 저작권 관리정보(CMI) 제거 책임이 성립하는가이다. 사내 정책 문서에는 이 사안을 '미확정 쟁점'으로 표시하고, 판결 확정 시 정책 재검토를 트리거할 모니터링 담당자를 지정한다.


[^ai-copilot-litigation]: GitHub Copilot litigation — Case updates : https://githubcopilotlitigation.com/case-updates.html

#### 벤더 면책은 제품별·시점별로 다르다 — Customer Copyright Commitment

Microsoft Learn은 GitHub Offerings에 대해 'as of April 3, 2026, there are no additional required mitigations. Use of the Duplicate Detection filter feature is no longer required for CCC coverage. This feature remains available for optional use.'라고 밝힌다. 반면 다른 제품에는 요구가 남아 있다 — Azure OpenAI 코드 생성 시나리오는 protected material code model을 annotate 또는 filter 모드로 설정해야 한다. annotate 모드를 택하면 출력물에 인용된 라이선스를 준수해야 CCC가 적용된다(2023-12-01 발효). 비동기 필터를 사용해 사후 플래그된 출력물도 인용 라이선스를 준수하지 않으면 CCC가 적용되지 않는다(2024-05-21 발효). Copilot Studio는 외부 호스팅 모델을 연결하면 CCC가 적용되지 않는다(2025-06-01 발효)[^ai-ccc].

벤더 면책 조건을 계약 갱신 주기마다 재확인하는 항목을 계약 관리 대장에 넣는다. 필터 요구가 사라졌다고 해서 사내 필터 정책까지 해제하지 않는다 — 면책과 위험 감소는 별개다.

[^ai-ccc]: Microsoft Learn, Customer Copyright Commitment Required Mitigations : https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/customer-copyright-commitment

## AI 오픈소스SW 가이드 - 개발자 편

기업 편이 정책과 승인 기준을 다뤘다면, 개발자 편은 개인이 커밋 전과 배포 전에 직접 수행하는 확인을 다룬다. 조직의 정책이 아무리 촘촘해도 실제 코드와 모델을 다루는 손은 개발자의 것이다.

이 트랙은 두 상황을 다룬다. 하나는 AI 코딩 도구를 사용해 코드를 만들 때이고, 다른 하나는 외부 모델을 직접 내려받아 사용하거나 파생물을 만들 때다. 정책의 근거와 라이선스 원문 해석은 기업 편에 있으므로 필요할 때 해당 소절로 이동한다.

### AI 코딩 도구를 쓸 때

#### 코드 참조 필터가 잡지 못하는 것 — 약 150자 임계, GitHub 공개 저장소 색인 한정, 수개월 갱신 주기

GitHub Copilot의 code referencing은 공식 문서에 다음과 같이 규정되어 있다 — 'Copilot code referencing compares potential code suggestions and the surrounding code of about 150 characters against an index of all public repositories on GitHub.com'[^ai-copilot-ref]. 같은 문서가 한계도 함께 밝힌다.

- **GitHub 밖 코드와 비공개 저장소 코드는 검색 대상이 아니다** — 'Code in private GitHub repositories, or code outside of GitHub, is not included in the search process'.
- **임계 미만의 짧은 조각은 통과한다** — 비교 단위가 약 150자이므로 그보다 짧은 일치는 걸리지 않는다.
- **색인이 수개월 주기로 갱신된다** — 'The search index is refreshed every few months'. 최근에 공개된 코드는 색인에 없을 수 있다.

일치가 발견되면 로그에 'the URLs of files containing matching code, and the name of the license that applies to that code, if any was found'가 기록된다. 조직 정책으로 개인 설정을 상속·강제할 수 있으며, 2026-02-18부터 Copilot coding agent도 code referencing을 지원한다[^ai-copilot-agent-ref].

**필터를 켰다고 라이선스 리스크가 제거되지 않는다.** 위 세 한계가 겹치는 구간은 필터가 보지 못하는 사각지대다. 따라서 두 가지를 함께 한다 — 조직 정책에서 '공개 코드와 일치하는 제안 차단'을 강제 설정하고, code referencing 로그를 감사 증적으로 보존한다.

[^ai-copilot-ref]: GitHub Docs, GitHub Copilot code referencing : https://docs.github.com/en/copilot/concepts/completions/code-referencing
[^ai-copilot-agent-ref]: GitHub Changelog(2026-02-18), Copilot coding agent supports code referencing : https://github.blog/changelog/2026-02-18-copilot-coding-agent-supports-code-referencing/

#### 의존성 SCA는 복사된 코드 조각을 보지 못한다 — 스니펫 매칭이 필요한 이유

기존 SCA는 package manifest를 근거로 삼는다. 선언된 의존성만 목록화하므로, AI 코딩 도구가 패키지를 추가하지 않고 코드를 직접 써 넣으면 manifest에 아무 흔적도 남지 않는다. 검출 원리가 다른 검사가 필요한 이유가 여기에 있다. 세 검사가 각각 무엇을 보고 무엇을 놓치는지 아래 표로 대조한다.

| 검사 종류 | 검출 대상 | 놓치는 것 |
|---|---|---|
| 의존성 SCA | package manifest에 선언된 의존성 컴포넌트와 버전 | 코드에 직접 써 넣어진 복사 조각 |
| 스니펫 매칭 | 소스 파일 안에 복사된 코드 조각과 그 원본 라이선스 | 도구가 어떤 원본을 참조했는지에 대한 이력 |
| AI 도구 자체 로그(code referencing) | 도구가 감지한 공개 코드 일치와 해당 라이선스명 | GitHub 밖 코드, 약 150자 미만 조각, 색인 갱신 이전 코드 |

2026년 기준 스니펫 매칭의 대표 사례는 두 가지다. FOSSA는 2026-01 SCANOSS와 기술 제휴를 맺어 SCANOSS의 스니펫 탐지와 FOSSA의 라이선스 지식베이스를 결합했다[^ai-fossa-scanoss]. Black Duck은 Snippet Analysis를 API로 제공해 AI 생성 코드를 대량 분석할 수 있게 했다[^ai-blackduck-snippet]. 제품 간 우열이나 가격은 이 가이드에서 비교하지 않는다.

학습 데이터에서 라이선스가 새어 나오는 구조적 배경은 [코드 학습 데이터셋의 라이선스 혼입 — The Stack v2 사례](#코드-학습-데이터셋의-라이선스-혼입--the-stack-v2-사례)에 있다.

[^ai-fossa-scanoss]: SCANOSS(벤더 발표, 2차 출처), FOSSA Partners With SCANOSS To Help Organisations Manage AI Coding Risks : https://scanoss.com/fossa-partners-with-scanoss-to-help-organisations-manage-ai-coding-risks/
[^ai-blackduck-snippet]: Black Duck(벤더 발표, 2차 출처), Analyze AI-Generated Code with the Black Duck Snippet API : https://www.blackduck.com/blog/analyze-ai-generated-code-black-duck-snippet-api.html

#### 릴리스 전 3중 검사 — 의존성 SCA / 스니펫 매칭(diff 기준) / AI 도구 로그

세 검사는 커버리지가 서로 다르므로 하나로 대체되지 않는다. 릴리스 게이트에 다음 순서로 배치한다.

| 단계 | 무엇을 확인하는가 | 언제 돌리는가 | 실패 시 무엇을 하는가 |
|---|---|---|---|
| ① 의존성 SCA | manifest에 선언된 의존성의 라이선스와 취약점 | 의존성 변경이 포함된 모든 PR과 릴리스 전 | 문제 의존성을 교체하거나 승인 예외를 신청한다 |
| ② 스니펫 매칭 | 변경분(diff)에 포함된 복사 코드 조각과 그 원본 라이선스 | 릴리스 전, **전체 리포지토리가 아니라 diff 기준**으로 | 해당 조각을 제거·재작성하거나 원본 라이선스 의무를 이행한다 |
| ③ AI 도구 로그 | code referencing이 기록한 일치 파일 URL과 라이선스명 | 릴리스 전, 해당 기간 로그를 일괄 확인 | 일치 항목의 라이선스 의무를 확인하고 로그를 감사 증적으로 보존한다 |

②를 diff 기준으로 제한하는 것은 비용 통제 지침이다. 전체 리포지토리 상시 스캔은 검출량 대비 비용이 급격히 커진다. ③의 로그 보존은 [코드 참조 필터가 잡지 못하는 것 — 약 150자 임계, GitHub 공개 저장소 색인 한정, 수개월 갱신 주기](#코드-참조-필터가-잡지-못하는-것--약-150자-임계-github-공개-저장소-색인-한정-수개월-갱신-주기)의 실행 지시와 같은 항목이다.

이 3중 검사는 릴리스 절차 안에 놓이는 게이트이며, 릴리스 게이트 자체의 구성과 승인 흐름은 [「오픈소스SW 공개하기」](../releasing/)에서 다룬다. AI가 존재하지 않는 패키지명을 만들어 내는 패키지 환각과 그것을 노린 슬롭스쿼팅은 공급망 보안 주제이므로 이 장에서 다루지 않는다 — [「오픈소스SW 사용하기」](../using/)의 보안 절을 참조한다.

{{< imgproc ai-code-release-triple-gate Fit "768x768" >}}
<center><i>[릴리스 전 3중 검사의 커버리지 구조]</i></center>
{{< /imgproc >}}

### 모델을 가져다 쓸 때

이 소절은 Hugging Face 등에서 모델을 직접 내려받는 개발자가 커밋 전에 확인할 것을 다룬다.

#### 라이선스 미표기는 '오픈소스SW'가 아니라 '모든 권리 유보'다 — Hugging Face 실태

RedMonk는 2026-05-12 약 290만 개 모델을 스캔해 약 100만 개만 라이선스가 표기되어 있다고 보고했다. 표기된 모델 가운데 'better than two thirds carried an OSI-approved license'였고, Apache-2.0이 2위인 MIT의 약 2.5배였다[^ai-redmonk-hf]. 별도로 Stalnaker 외의 ACM TOSEM 게재 논문은 모델 760,460개와 데이터셋 175,000개를 분석해 ML 모델·데이터셋의 라이선스 관리, 문서화 지원, 자동 불일치 검증이 필요하다고 결론지었다[^ai-hf-tosem].

라이선스 미표기는 오픈소스SW가 아니라 '모든 권리 유보'다. 미표기 모델의 사용 금지를 기본 정책으로 하고, 예외로 사용해야 할 때는 법무 검토를 거친다.

[^ai-hf-tosem]: ACM TOSEM(피어리뷰), An Empirical Analysis of ML Model and Dataset Documentation, Supply Chain, and Licensing Challenges on Hugging Face : https://dl.acm.org/doi/10.1145/3776739

#### base_model 계보를 거슬러 올라간다 — 표기된 라이선스를 믿지 않는 이유

Laufer·Oderinwale·Kleinberg의 Hugging Face 186만 모델 분석은 '라이선스가 직관과 반대로 제한적인 상업 라이선스에서 허용형 또는 카피레프트 라이선스로 표류하며, 그것이 흔히 상류 라이선스의 조항을 위반한다(Licenses counter-intuitively drift from restrictive, commercial licenses towards permissive or copyleft licenses, often in violation of upstream license's terms)'고 관측했다[^ai-hf-anatomy]. 승계되어야 할 제한이 파생 과정에서 사라지고 있고, 그 사라짐 자체가 이미 라이선스 위반이라는 뜻이다. 파생 모델에 표기된 라이선스를 그대로 믿지 않는 이유가 여기에 있다.

확인 절차는 다음과 같다.

1. 모델 카드의 `base_model` 필드를 확인한다.
2. 그 베이스 모델의 카드로 이동한다.
3. 원 베이스에 도달할 때까지 1~2를 반복한다.
4. 최종 원 베이스의 LICENSE 원문과 부속 문서(AUP)를 확인한다.

계보가 중간에 끊기거나 `base_model` 표기가 아예 없으면 그 모델을 사용하지 않거나 법무 검토로 보낸다.

[^ai-hf-anatomy]: Anatomy of a Machine Learning Ecosystem: 2 Million Models on Hugging Face (arXiv 2508.06811, NeurIPS 2025 Regulatable ML 워크숍 포스터 — 본회의 피어리뷰 논문이 아닌 프리프린트) : https://arxiv.org/abs/2508.06811

#### 모델 병합 시 '가장 제한적 조건 채택' 원칙

mergekit 등으로 서로 다른 라이선스의 모델을 병합하면 결과물은 가장 제한적인 조건을 따른다고 보고 운영한다. 상호 배타적인 조항이 걸리면 병합 자체가 불가능해질 수 있다. 조합별 판단은 다음과 같다.

| 병합 조합 | 결과물에 적용할 조건 | 근거 |
|---|---|---|
| Apache-2.0 + Apache-2.0 | Apache-2.0 | 제한 조항이 없다 |
| Apache-2.0 + Llama 커스텀 | 명칭 접두어·NOTICE·AUP·지역 제한을 모두 승계 | Apache-2.0이 커스텀 조건을 씻어내지 못한다 |
| Apache-2.0 + Gemma 3 이하 커스텀 | 계약서 사본 제공·NOTICE·Prohibited Use Policy를 승계 | Model Derivatives 정의가 가중치·파라미터 전이 결과물을 포섭한다 |
| 커스텀 + 커스텀(조항 충돌) | 병합 불가로 판정하고 법무 검토로 보낸다 | 상호 배타적 조항을 동시에 충족할 수 없다 |

이 원칙은 법적으로 확정된 규칙이 아니라 계약 위반 리스크를 피하기 위한 보수적 운영 규칙이다. 병합 승인 절차에 '가장 제한적 조건 채택'을 명문화하고, 승인 기준 자체는 [파인튜닝 결과물의 라이선스 승계 — 5개 항목 배포 승인 체크리스트](#파인튜닝-결과물의-라이선스-승계--5개-항목-배포-승인-체크리스트)를 따른다.

#### 파인튜닝 결과물을 배포하기 전에 확인할 것

- [ ] 베이스 모델의 LICENSE 파일을 배포물에 포함했는가 → [파인튜닝 결과물의 라이선스 승계 — 5개 항목 배포 승인 체크리스트](#파인튜닝-결과물의-라이선스-승계--5개-항목-배포-승인-체크리스트)
- [ ] NOTICE 파일에 지정 문구를 넣었는가(Llama 4와 Gemma 3 이하는 문구가 지정되어 있다) → [Llama 4 — 700M MAU 임계, 'Built with Llama' 표시, 파생 모델 명칭 접두어](#llama-4--700m-mau-임계-built-with-llama-표시-파생-모델-명칭-접두어)
- [ ] 모델 이름이 명명 규칙을 지키는가(Llama 파생물은 'Llama' 접두어) → [Llama 4 — 700M MAU 임계, 'Built with Llama' 표시, 파생 모델 명칭 접두어](#llama-4--700m-mau-임계-built-with-llama-표시-파생-모델-명칭-접두어)
- [ ] AUP를 모델 카드에 링크했는가 → [라이선스 본문 밖에 있는 제한 — Llama 4 멀티모달의 EU 조항](#라이선스-본문-밖에-있는-제한--llama-4-멀티모달의-eu-조항)
- [ ] 지역 제한이 있는 모델을 제한 지역 조직에서 다루지 않았는가 → [라이선스 본문 밖에 있는 제한 — Llama 4 멀티모달의 EU 조항](#라이선스-본문-밖에-있는-제한--llama-4-멀티모달의-eu-조항)
- [ ] 배포물에 포함된 데이터셋이 재배포 가능한가 → [데이터셋 등록 필수 5개 필드 — 출처 URL·라이선스·취득일·사용 목적·재배포 가부](#데이터셋-등록-필수-5개-필드--출처-url라이선스취득일사용-목적재배포-가부)

---

여기까지 AI 모델·데이터셋·AI 생성 코드를 오픈소스SW 거버넌스 안에서 다루는 방법을 살펴보았다. 기업 편에서는 반입 승인·대장 등록·SBOM·고지·배포 승인 5단계에 '자산 유형'을 더하는 편입 방식, '오픈소스 AI'라는 말의 판정 기준, 벤더별 모델 라이선스 실사, 데이터셋 등록 5개 필드, EU AI Act와 한국 AI 기본법이 부과하는 의무를 다뤘다. 개발자 편에서는 릴리스 전 3중 검사, `base_model` 계보 추적, 모델 병합 시 '가장 제한적 조건 채택' 원칙을 다뤘다.

지금 착수할 것은 세 가지다.

1. **모델·데이터셋 대장을 먼저 만든다.** 기존 컴포넌트 대장에 '자산 유형'과 '개방성 등급' 컬럼을 추가하고, 이미 사용 중인 모델을 버전 단위로 채워 넣는다. 어떤 모델이 어느 라이선스로 들어와 있는지 목록이 없으면 그다음의 어떤 판정도 시작할 수 없다.
2. **릴리스 게이트에 스니펫 매칭을 diff 기준으로 넣는다.** 의존성 SCA만 돌리는 상태에서는 AI 코딩 도구가 직접 써 넣은 코드 조각이 검사 대상에서 빠진다. 전체 리포지토리 상시 스캔이 아니라 변경분 기준으로 시작한다.
3. **AI 고지·표시 의무 대응 상태를 확인한다.** 한국 AI 기본법 제31조는 2026-01-22부터 시행 중이고, EU 시장에 GPAI를 공급하는 경우 2026-08-02에 집행 권한이 개시된다. 오픈소스SW 모델을 쓴다는 사실이 면제 사유가 아니라는 점을 정책 문서에 명시한다.

이 장으로 가이드를 마친다. 다섯 장은 오픈소스SW 사용·기여·공개와 OSPO, 그리고 AI 자산이라는 서로 다른 국면을 다루지만 같은 구조를 공유한다 — 무엇을 쓰고 있는지 목록으로 확보하고, 라이선스와 규제가 요구하는 의무를 프로세스 단계에 넣고, 판정의 근거를 기록으로 남기는 것이다. 관리해야 할 자산의 종류는 앞으로도 늘어난다. 목록·프로세스·기록 세 축이 서 있는 조직은 새로운 자산 유형을 컬럼 하나와 확인 항목 몇 개로 흡수할 수 있고, 그렇지 않은 조직은 자산 유형마다 체계를 새로 세우게 된다. 이 가이드는 그 세 축을 세우는 데 필요한 판단 기준과 양식을 제공하는 데 목적이 있다.
