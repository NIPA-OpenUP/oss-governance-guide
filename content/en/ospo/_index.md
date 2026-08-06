---
title: "OSPO"
linkTitle: "4. OSPO"
weight: 50
description: >
   
---

현대의 ICT 기업은 소프트웨어 제품과 서비스 개발을 위해 오픈소스SW를 필수로 사용한다. 기업이 오픈소스SW 거버넌스 체계를 수립하는 목적은 세 가지다. 첫째, 오픈소스SW로부터 최대한의 가치를 창출한다. 둘째, 라이선스 의무를 지키지 못해 발생하는 법적 리스크를 완화한다. 셋째, 공급망 보안과 규제가 요구하는 의무를 이행한다. 앞의 두 축은 오래전부터 오픈소스SW 거버넌스의 목적이었다. 여기에 더해 규제 대응은 2026년 기업이 OSPO를 설립하는 강한 동인이 되었으며, 그 실행을 책임지는 조직이 OSPO다. 규제별 요구사항과 시행 일정은 [오픈소스SW 사용하기](../using/)의 규제 동향 절에서 다룬다.

글로벌 ICT 기업은 오픈소스SW 거버넌스 체계를 구축하고 이를 성장시키기 위해 OSPO<sub>Open Source Program Office</sub>라는 조직을 운영하고 있다. OSPO는 기업의 오픈소스SW 거버넌스 체계를 구축할 뿐만 아니라 기업의 성공을 위한 오픈소스SW 전략을 수립하고 실행하는 데 필요한 정책, 프로세스 및 도구를 제공한다.

세 번째 축이 OSPO의 실제 업무로 자리 잡았다는 점은 조사로도 확인된다. OSPO를 보유한 조직의 92%가 오픈소스SW 보안에 관여한다. 42%는 OSPO가 직접 보안 의사결정을 내리고, 50%는 담당 조직에 자문하며, 보안을 다루지 않는다는 응답은 7%에 그쳤다. 또한 79%는 생성형 AI 리스크 관리에 OSPO가 효과적이라고 답했다. 이 값은 2024년 조사의 65%에서 오른 것이다[^ospo-survey-2025].

Microsoft, Google, Meta와 같은 소프트웨어 리더 기업뿐만 아니라 Comcast, Bosch와 같은 전통 제조·통신 기업도 OSPO를 운영하고 있다(Meta·Microsoft·Comcast는 TODO Group 사례집[^case-index], Bosch는 자사 오픈소스SW 포털에서 확인된다). 국내에서도 전담 조직을 두는 기업이 늘고 있다. 공개된 자료로 확인되는 예를 들면 SK텔레콤은 자사 OSPO 소개 페이지를 운영하고 있고[^sktospo], 삼성전자·LG전자·카카오·LINE은 오픈소스SW 전담 조직 또는 그에 준하는 기능을 두고 있다. 다만 국내 기업의 OSPO 운영 여부를 한자리에 모아 둔 1차 출처는 없으므로, 특정 기업의 조직 형태는 그 기업의 공개 자료로 각자 확인해야 한다.


기업 규모와 지역에 따라 OSPO 보유 현황은 크게 갈린다. 다음은 2025년 8월 발간된 LF Research 조사(2025년 5~6월 실시, 총 응답 338건, 문항별 분석 표본 283~337건)가 보고한 OSPO 보유 현황이다[^ospo-survey-2025]. 연도별 추이는 표본 규모가 다른 별개 조사의 결과를 이어 붙인 것이다(2022년 950건, 2023년 472건, 2024년 222건, 2025년 285건).

| 구분 | 조사 결과 |
|------|-----------|
| 정식 OSPO 보유율 추이(전체, 연도별) | 2022년 30% → 2023년 43% → 2024년 26% → 2025년 32% |
| 비정식 OSPO 보유율 추이(전체, 연도별) | 2023년 23% → 2025년 18% |
| 규모별(보고서 본문 서술) | 중소조직의 72%가 OSPO를 보유하며 그중 대부분(55%)은 비공식으로 운영한다 — 보고서 본문 문장이며, 본문 Figure 6에서 도출한 값이 아니다[^ospo-figure6] |
| 지역별 보유율(정식+비정식 합계, 부록 A2·표본 337) | 아시아태평양 50%(정식 37%+비정식 13%) / 아메리카 46%(정식 29%+비정식 17%) / 유럽 36%(정식 22%+비정식 14%) / 그 외 지역 28%(정식 17%+비정식 11%) |

규모별과 지역별은 같은 지표가 아니므로 나란히 비교하지 않는다. 규모별은 보고서 본문의 서술 한 문장이 근거이고, 지역별은 부록 A2의 응답 비율이 근거다. 특히 규모별 도표(Figure 6)에서 '대·초대형 83%' 같은 보유율을 읽어 내면 안 된다. 그 83%는 정식 OSPO라고 답한 응답자 가운데 대·초대형 조직이 차지하는 비중이다.

한국 단독 수치는 이 보고서에 없다. 아시아태평양은 부록 A2 기준으로 정식 OSPO 비율(37%)과 정식+비정식 합계(50%) 모두 4개 지역·그룹 중 가장 높다[^ospo-region-a2]. 다만 이 조사의 표본은 오픈소스SW 거버넌스에 이미 관심이 있는 응답자 중심이므로 지역 모집단 전체의 보유율로 확대 해석해서는 안 된다.

[^ospo-survey-2025]: The 2025 State of OSPOs and Open Source Management, Linux Foundation Research, 2025년 8월 발간 : https://www.linuxfoundation.org/hubfs/Research%20Reports/LFResearch_StateofOSPO_082825.pdf
[^ospo-figure6]: 보고서 본문 Figure 6은 규모별 보유율이 아니라 항목별 규모 구성비다. 다섯 항목 모두 대·초대형과 중소 두 그룹의 합이 정확히 100%(17/83, 55/45, 68/32, 50/50, 68/32)이므로 보유율로 읽을 수 없고, 단일 선택 문항인데 중소조직 쪽 값을 모두 더하면 258%가 된다. 본문 Figure 7도 같은 방식으로 정규화되어 있다(정식 OSPO: 아메리카 43 + 유럽 32 + 아시아태평양 21). 따라서 이 가이드는 Figure 6에서 규모별 보유율을 도출하지 않고 보고서 본문 문장만 인용한다. 같은 보고서 29쪽이 전체 정식 OSPO 27%, 도입 계획 중 7%로 보고하므로 Figure 6의 중소조직 68%를 '계획 중 비율'로 읽는 해석도 성립하지 않는다.
[^ospo-region-a2]: 위 지역별 수치는 이 보고서 부록 Appendix A2(32쪽, 표본 337)를 근거로 한다. 같은 보고서 11쪽 본문 Figure 7(표본 285, Rest of World 제외)은 반대로 아메리카 89%·유럽 68%·아시아태평양 35%로 아시아태평양이 가장 낮다고 서술해 보고서 내부적으로 상충한다. 부록 A2 수치를 지역별 응답 비중(아메리카 39%·유럽 38%·아시아태평양 16%·그 외 7%, 표본 338)으로 가중평균하면 26.8%가 되어 보고서가 별도로 명시한 전체 정식 OSPO 비율 27%(29쪽)와 사실상 일치한다. 반면 11쪽 수치로 같은 방식의 계산을 하면 정식+비정식 합계가 약 71%가 되어 보고서의 전체 수치 42%(29쪽)와 크게 어긋난다. 이 가이드는 이 교차검증에 따라 부록 A2 수치를 기준으로 삼았다. 원문을 함께 확인하는 독자는 11쪽 값이 다르다는 점에 유의한다.

이 장에서는 OSPO의 역할 및 책임을 알아보고 국내 기업이 OSPO를 설립하기 위한 방법을 설명한다.

> 이 장의 내용은 TODO Group의 [How to create an open source program office](https://todogroup.org/resources/guides/how-to-create-an-open-source-program-office/)[^howtoospo]를 기반으로 작성하였으며, 2026년 7월 기준 판본을 참조하였다.

[^howtoospo]: How to create an open source program office, TODO Group (2026년 7월 참조) : https://todogroup.org/resources/guides/how-to-create-an-open-source-program-office/

## OSPO 정의와 역할

### 오픈소스 프로그램이란?

먼저, 오픈소스 프로그램이란 용어를 살펴보자. 오픈소스 프로그램<sub>Open Source Program</sub>이란 기업이 오픈소스SW를 활용하면서 (1) 라이선스 위반, 보안 취약점 리스크는 완화하고 (2) 오픈소스SW에서 최고의 가치를 창출하기 위한 프로그램이다. 여기에는 오픈소스SW 정책과 프로세스 수립, 그리고 이를 자동화·효율화할 수 있는 도구를 지원하는 일이 포함된다.

{{< imgproc osp Fit "768x768" >}}
<center>[오픈소스 프로그램]</center>
{{< /imgproc >}}


### OSPO란?

OSPO<sub>Open Source Program Office</sub>는 오픈소스 프로그램을 만들고 운영하기 위한 조직이다. 어떻게 기업의 오픈소스SW 컴플라이언스를 관리할지, 개발자가 외부 오픈소스SW 프로젝트에 기여하기 위한 절차는 무엇인지, 사내의 프로젝트를 오픈소스SW로 공개하기 위한 절차는 무엇인지는 모두 OSPO가 수행해야 할 전략적 결정이다.

기업이 오픈소스SW에서 최대의 이익을 창출하기 위해서는 OSPO를 만들고 이를 통해 기업의 오픈소스SW 활동을 관리 및 지원해야 한다. 기업이 OSPO를 운영하며 오픈소스SW를 적극적으로 활용한다면 아래와 같은 효과를 기대할 수 있다고 알려져 있다.

- 소프트웨어 개발 인재를 유치하고, 기존 인력의 유출을 방지할 수 있다.
- 비즈니스 가치 창출과 혁신 추진을 가속화할 수 있다.
- 개발자가 비즈니스 로직 작성에 집중함으로써 비용 절감과 효율 향상을 기대할 수 있다.
- 제품 리더십을 통해 수익 창출과 시장 점유율 확보를 기대할 수 있다.

> TODO Group에서는 [OSPO의 정의](https://github.com/todogroup/ospodefinition.org)[^ospodefinition]에 대해 설명하는 글을 게시하였다. 한국어 자료로는 OpenChain 한국 워킹그룹의 [ISO 표준 기반 기업 오픈소스SW 관리 가이드 2026판](https://openchain-project.github.io/OpenChain-KWG/guide/opensource_for_enterprise/)[^kwg-guide-2026] 중 조직 구성 절을 참고할 수 있다.

[^ospodefinition]: Open Source Program Office (OSPO) Definition and Guide : https://github.com/todogroup/ospodefinition.org
[^kwg-guide-2026]: OpenChain 한국 워킹그룹, ISO 표준 기반 기업 오픈소스 관리 가이드 2026판 (2026-06-02 갱신) : https://openchain-project.github.io/OpenChain-KWG/guide/opensource_for_enterprise/

### OSPO 역할

OSPO의 세 가지 주요 역할은 다음과 같다.

{{< imgproc ospo Fit "768x768" >}}
<center>[OSPO 주요 역할]</center>
{{< /imgproc >}}


#### 1. 오픈소스SW의 올바른 사용

OSPO는 기업이 오픈소스SW를 사용하면서 라이선스 의무 사항을 준수할 수 있도록 오픈소스SW 정책과 프로세스를 수립해야 한다. 기업은 제품과 서비스 개발 시 사용한 오픈소스SW의 라이선스가 요구하는 바를 준수해야 하는데 이를 위한 활동을 오픈소스SW 컴플라이언스라고 한다. 기업은 올바른 오픈소스SW 컴플라이언스 활동을 통해 저작권 침해 리스크를 관리할 뿐만 아니라 오픈소스SW 커뮤니티에서 기업 브랜드 평판을 높일 수 있다.

이를 위한 세부 사항은 [오픈소스SW 사용하기](../using/)에서 자세히 다루었다.

#### 2. 외부 오픈소스SW 프로젝트로의 기여

기업 내 구성원에게 외부 오픈소스SW 프로젝트에 기여하도록 장려하는 것도 오픈소스SW를 전략적으로 활용하는 좋은 방법이다. OSPO는 오픈소스SW 기여 문화를 확산하면서도 기업의 지식재산은 보호할 수 있는 오픈소스SW 기여 정책을 수립해야 한다.

오픈소스SW 기여 활동으로 취할 수 있는 혜택과 고려 사항 및 세부 방법은 [오픈소스SW 기여하기](../contributing/)에서 자세히 다루었다.

#### 3. 사내 프로젝트의 오픈소스SW 공개

오픈소스SW를 적극적으로 활용하는 기업이라면 오픈소스SW를 단순히 사용하는 데 그치지 않고, 사내 프로젝트를 오픈소스SW로 공개하고 커뮤니티를 활성화하여 최대의 가치를 창출한다. OSPO는 기업의 비즈니스 전략을 고려하여 오픈소스SW 공개 정책을 수립하고, 이를 활성화하기 위한 실행 방안을 마련해야 한다.

이를 위한 세부 절차 및 방법은 [오픈소스SW 공개하기](../releasing/)에서 자세히 다루었다.


## OSPO 구성

### OSPO 구성 절차

그러면 기업이 OSPO를 만들기 위한 절차를 알아보자.

{{< imgproc feedback Fit "768x768" >}}
<center>[OSPO 구성 절차]</center>
{{< /imgproc >}}

#### 1. 리더를 임명하라

먼저 OSPO를 만들고 운영할 수 있는 적합한 리더를 찾는 것이 중요하다. 다음과 같은 역량을 갖고 있다면 OSPO의 리더로 적합하다.

- 오픈소스SW의 가치와 발전 가능성에 공감하고, 이를 사내에 전파하고자 하는 열정이 있다.
- 오픈소스SW 프로젝트에 개발자, 기여자로 참여한 경험이 있고, 오픈소스SW 개발 방법론을 충분히 이해한다.
- 기업의 비즈니스 전략과 일치하는 방향의 오픈소스SW 전략을 수립할 수 있도록 기업의 비즈니스를 폭넓게 이해한다.
- 오픈소스SW 전략과 정책을 모든 구성원이 이해하도록 전파할 수 있는 커뮤니케이션 역량을 갖추었다.
- 여러 기술 분야를 폭넓게 이해하여 개발자와 기술적인 소통이 가능하다.

누군가 임시로 역할을 맡아서 시작할 수도 있다. 하지만 OSPO가 조기에 올바른 역할을 수행하고 견고히 자리 잡기를 바란다면 전담하여 책임질 수 있는 리더를 임명해야 한다.

#### 2. OSPO의 역할을 정의하라

기업의 OSPO가 어떤 역할을 수행할지 정의한다. 기업마다 규모나 업종이 다르고, 오픈소스SW를 통해 얻고자 하는 목적이 다르므로 OSPO의 역할이 달라질 수 있다.

일반적으로 OSPO는 오픈소스SW 정책을 수립하고 이를 실행하기 위한 프로세스를 구성한다. 또한 프로세스 활동을 가능한 한 자동화하기 위한 도구를 개발하여 제공하는 역할을 수행한다. 이 과정에서 부서 간 협업을 유도하고, 발생하는 이슈를 해결한다.

OSPO는 구조화된 정책과 프로세스를 제공해야 하지만, 유연성도 유지해야 한다. OSPO가 모든 분야에 전문성을 갖고 모든 의사결정을 내리는 것은 현실적으로 불가능하다. OSPO는 오픈소스SW 사용자와 기여자에게 도움이 필요할 때 컨설팅을 제공하고 구성원이 스스로 개인 또는 기업의 비즈니스 결정을 내릴 수 있도록 허용해야 한다. 궁극적으로는 기업과 구성원의 요구를 모두 충족하기 위한 역할과 책임의 적절한 균형을 설정하는 것이 중요하다.


#### 3. 피드백을 수렴하라

한 번에 OSPO의 모든 것을 구축하기는 쉽지 않다. 우선 기본적인 사항을 준비한 후 기업 내부의 모든 관련 당사자로부터 피드백을 받아서 보완해나가는 것이 필요하다.

경영진으로부터 개발자에 이르기까지 모든 구성원의 피드백을 수렴한다. 기업의 비즈니스 전략이나 구성원의 요구 사항을 고려하지 않고 OSPO가 단독으로 수립한 정책이 장기적으로 성공하기를 기대할 수는 없다.


### OSPO 구성 방법

#### 어느 조직 내에 OSPO를 만들어야 하나?

OSPO는 기업의 어느 부서 내에 만드는 것이 적합하냐는 질문이 나올 수 있다. 개발 조직 내에 만들지, 아니면 법무 조직에 있어야 하는지를 고민할 수 있는데, 이는 기업의 비즈니스와 오픈소스SW 전략에 따라 달라진다.

##### 개발 조직 속에서의 OSPO

오픈소스SW를 활용하는 부서는 주로 소프트웨어 개발 조직이기 때문에 일반적으로 OSPO를 개발 조직 내에 만든다. 이를 통해 개발자가 더 효과적이고 생산적으로 오픈소스SW를 활용하도록 지원한다.

##### 법무 조직 속에서의 OSPO

대규모의 IP(지식 재산) 포트폴리오를 보유한 기업이라면 OSPO가 법무 조직 내에 있는 것이 유리할 수 있다. 오픈소스SW를 활용하면서 법무 조직과 긴밀하게 협력하여 IP 관련 법적 문제가 발생할 가능성을 사전에 점검하고 대응할 수 있다. 주로 칩세트와 같이 IP 집약적인 하드웨어 개발 회사에 적합하다.

##### 마케팅 조직 속에서의 OSPO

기업이 오픈소스SW를 사용하여 개발한 제품이나 서비스를 판매하는 비즈니스를 주력으로 한다면 마케팅 부서 내부에 OSPO를 만들어서 오픈소스SW 제품의 홍보와 마케팅에 집중하는 것이 유리할 수 있다.

#### OSPO에는 어떤 인원이 필요한가?

OSPO의 인원 구성과 각 역할 및 책임을 알아보자.

미리 한 가지 첨언하면 아래의 인원 구성은 전략적으로 OSPO에 충분한 리소스를 투입해야 할 이유가 명확히 있는 기업을 고려하여 설명하였다. 기업의 규모가 크지 않고, 오픈소스SW 활용을 이제 시작하는 기업이라면, 처음부터 아래의 모든 인원과 역할을 지정할 필요는 없다. 한 명의 오픈소스 프로그램 매니저를 임명하고, 관련 부서와의 협업을 통해 OSPO의 역할을 수행하면서 점차 규모를 키워갈 것을 권장한다.


{{< imgproc role Fit "768x768" >}}
<center>[OSPO의 인원 구성과 역할]</center>
{{< /imgproc >}}


##### 오픈소스 프로그램 매니저

오픈소스 프로그램 매니저는 오픈소스 프로그램을 관리하고 전략을 수립하는 전담 인원으로서 다음의 역할을 담당한다.
* 기업의 수익, 브랜드 인지도, 개발자 역량, 채용 등 비즈니스 목표에 부합하는 오픈소스SW 전략을 수립한다.
* 기업의 모든 오픈소스SW 활동을 감독한다.
* 효과적인 오픈소스SW 활동을 위한 정책을 수립하고 프로세스를 구축한다.

오픈소스 프로그램 매니저는 이처럼 기업 전반에 걸쳐 영향력을 미칠 수 있는 역할이기 때문에 효율성을 극대화하기 위해서 가능하다면 임원급 직책을 가진 자가 맡는 것이 좋다.

##### 컴플라이언스 담당

외부로 배포 혹은 서비스하는 제품 소프트웨어 및 서비스를 개발하는 조직은 오픈소스SW 컴플라이언스 활동을 수행해야 한다. 즉, 배포 소프트웨어에 포함된 오픈소스SW가 무엇인지 확인하고, 해당 오픈소스SW 라이선스의 의무 사항을 준수해야 한다. 컴플라이언스 담당은 기업의 오픈소스SW 컴플라이언스를 보장하기 위한 역할을 담당한다.

##### 법무 담당

오픈소스SW를 사용하거나 외부에 기여하는 활동은 저작권에 기반하여 라이선스를 받거나 부여하는 활동이다. 결국 법적인 판단이 필요한 일이 발생할 수밖에 없다. 따라서, OSPO는 법률 전문가를 포함해야 한다. 직접 포함할 수 없으면 법률 조언을 받을 수 있는 창구를 마련해야 한다.

OSPO의 법률 담당은 다음의 역할을 수행한다.
* 오픈소스SW 라이선스 및 기타 법적 자문을 제공한다.
* 외부 오픈소스SW 프로젝트에 기여 활동이 법적인 문제를 발생시킬 우려는 없는지 점검한다. 여기에는 CLA (Contributor License Agreement) 검토 등의 활동을 포함한다.

대기업의 경우 오픈소스SW 전문 변호사를 고용하는 경우도 있지만, 그렇지 않을 경우, 외부 컨설팅 업체를 활용하는 것도 고려할 수 있다.

참고로 오픈업 센터(Open UP)는 오픈소스SW 활용을 위한 [컨설팅 서비스](https://www.oss.kr/pages/5)[^plaza]를 제공한다. 사용 중인 오픈소스SW의 라이선스 의무 사항을 외부에서 점검받고자 하는 기업은 [라이선스 검증 신청](https://www.oss.kr/pages/14)[^oss-license-check] 창구를 이용할 수 있다[^nipa-reorg].

[^plaza]: 오픈업 센터(Open UP) 소개 : https://www.oss.kr/pages/5
[^oss-license-check]: 오픈업 센터 라이선스 검증 신청 : https://www.oss.kr/pages/14
[^nipa-reorg]: 2024년 3월 NIPA 조직개편으로 SW산업본부 산하 공개소프트웨어팀이 SW미래본부 SW산업팀으로 통합되었다. 컨설팅을 신청할 때 담당 창구를 확인한다. 출처 : AI 시대 더 중요해진 오픈소스SW, 하지만…NIPA '공개소프트웨어팀' 사라져, 디지털데일리, 2024-03-26 : https://m.ddaily.co.kr/page/view/2024032606541480965

##### IT 지원 담당

오픈소스 프로그램을 효율적으로 운영하기 위해서는 가능한 한 자동화해야 한다. IT 지원 담당은 도구를 활용하여 오픈소스SW 컴플라이언스와 오픈소스SW 보안 취약점 점검을 자동화하기 위한 역할을 담당한다.

##### 오픈소스SW 에반젤리스트

기업의 프로젝트를 오픈소스SW로 공개하고, 외부 프로젝트에 기여하는 활동을 장려하는 기업이라면 이를 외부에 홍보하기 위한 오픈소스SW 에반젤리스트의 역할이 중요하다. 오픈소스SW 에반젤리스트는 오픈소스SW 콘퍼런스 참여, 발표, 프로젝트 후원, 주기적인 홍보 문서 배포 등의 방법으로 기업의 오픈소스SW 활동을 외부에 알리는 역할을 담당한다.


#### 구체적으로 OSPO는 무엇을 해야 하는가?

##### 정책을 수립하라

오픈소스SW를 사용하면서 오픈소스SW 라이선스를 준수하지 않을 경우, 비즈니스 기회를 놓치거나 수익 손실(판매 손실, 인수 실패 등), 법적 피해(IP 소유권 손실, 수익 또는 파트너십 악화, 벌금 등) 및 브랜드 손상의 위험이 발생한다. 올바른 오픈소스SW 사용을 위한 정책을 수립해야 한다. 또, 올바른 오픈소스SW 커뮤니티에 구성원이 기여하는 방법, 내부 프로젝트를 오픈소스SW 커뮤니티에 공개하기 위한 방법도 포함해야 한다. 즉, OSPO는 다음을 다루는 오픈소스SW 정책을 수립해야 한다.

1. 오픈소스SW 사용 정책 : 구성원이 GitHub 등 외부 저장소에서 찾은 소스 코드를 컴플라이언스와 보안 취약점 관점에서 올바르게 사용하기 위한 방법
2. 오픈소스SW 기여 정책 : 구성원이 외부 오픈소스SW 프로젝트에 기여하기 위한 방법
3. 오픈소스SW 공개 정책 : 사내 프로젝트를 오픈소스SW로 공개하기 위한 방법

오픈소스SW 커뮤니티에서는 이러한 오픈소스SW 정책을 위한 템플릿 문서를 작성하여 공개하고 있다. 아직 오픈소스SW 정책이 없는 기업은 이러한 템플릿 문서를 참고하면서 기업에 맞게 개선하면 더 수월하게 정책을 수립할 수 있다. 한 번에 다 하려고 하기보다 계획을 수립하여 순차적으로 진행하는 것이 좋다.

- Google의 [오픈소스SW 정책 레퍼런스](https://opensource.google/documentation/reference)[^samplepolicy]
- OpenChain 한국 워킹그룹의 [오픈소스SW 정책 템플릿](https://openchain-project.github.io/OpenChain-KWG/guide/templates/1-policy/)[^policy-template]
- OpenChain 한국 워킹그룹의 [ISO 표준 기반 기업 오픈소스SW 관리 가이드 2026판](https://openchain-project.github.io/OpenChain-KWG/guide/opensource_for_enterprise/)[^kwg-guide-2026]

[^samplepolicy]: Google 오픈소스 정책 레퍼런스 : https://opensource.google/documentation/reference
[^policy-template]: OpenChain 한국 워킹그룹 오픈소스 정책 템플릿 : https://openchain-project.github.io/OpenChain-KWG/guide/templates/1-policy/

##### 정책을 전파하라

오픈소스SW 정책을 수립하는 것에 그쳐서는 안 되며, 이를 전사에 확산하는 노력을 병행해야 한다. 효과적인 확산을 위해서는 기업 내 고위 임원의 장기적인 지원이 필요하다. 이를 위해 CTO 또는 CIO에게 오픈소스SW 정책의 중요성을 설득력 있게 설명하고 지원을 요청한다.

모든 개발자가 오픈소스SW 정책의 존재를 알 수 있도록 해야 한다. 또한 법무팀, 구매팀과 같은 비개발 조직에서도 오픈소스SW 정책 활동에 참여하도록 환경을 조성한다.

다음은 오픈소스SW 정책과 문화를 확산하기 위한 한 예이다.

1. 오픈소스SW 교육 과정을 개설하여 기업 내 모든 개발자가 오픈소스SW 사용 및 기여를 이해하고, 참여하게 한다.
2. 기업 내 오픈소스SW 전문가로 구성된 커뮤니티를 만든다.
  * 오픈소스SW 커뮤니티 활동을 경험한 전문가들이 먼저 참여하게 한다.
  * 전문가들은 정기적으로 세미나 등을 통해 다른 개발자들에게 오픈소스SW 활동을 알린다.


##### 프로세스를 구축하라

정책이 기업의 올바른 오픈소스SW 활동을 위한 요구 사항 및 규칙이라고 한다면, 프로세스는 각 소프트웨어 개발 단계에서 정책을 준수하기 위해 수행해야 하는 일련의 절차이다.

Linux Foundation이 출간한 Open Source Compliance in the Enterprise에서는 이러한 프로세스를 설명하고 있다.

{{< imgproc process Fit "768x768" >}}
<center>Linux Foundation, 오픈소스SW 컴플라이언스 프로세스 : https://www.linuxfoundation.org/compliance-and-security/2018/12/open-source-compliance-in-the-enterprise</center>
{{< /imgproc >}}


더불어 OpenChain 프로젝트에서 제공하는 Curriculum 문서에서도 유사하게 단계별 프로세스와 주요 활동을 설명하고 있다.

{{< imgproc process2 Fit "768x768" >}}
<center>OpenChain, 오픈소스SW 컴플라이언스 프로세스 및 주요 활동 : https://www.openchainproject.org/resources</center>
{{< /imgproc >}}

OpenChain 한국 워킹그룹은 ISO/IEC 5230:2020 기반의 [샘플 오픈소스SW 컴플라이언스 프로세스 템플릿](https://openchain-project.github.io/OpenChain-KWG/guide/templates/2-process-template/)[^process-template]을 제공한다.

[^process-template]: OpenChain 한국 워킹그룹 샘플 오픈소스SW 컴플라이언스 프로세스 템플릿 : https://openchain-project.github.io/OpenChain-KWG/guide/templates/2-process-template/

기업은 이러한 자료를 참고하여 기업의 환경에 맞게 오픈소스SW 프로세스를 구축할 수 있다. 다만 프로세스 활동이 소프트웨어 개발의 병목 현상을 유발해서는 안 된다는 점에 유의한다. 아무리 프로세스가 충실하게 구축되었다고 할지라도 실제 활동을 수행해야 할 소프트웨어 개발 조직에 과부하가 발생한다면, 프로세스는 곧 아무 역할도 하지 못하는 한 장의 종이로 전락할 수 있음을 유념한다.

반복적으로 검토하여 불필요한 절차를 제거하고, 가능한 모든 과정을 자동화하기 위해 지속해서 개선한다. 또한 기업의 비즈니스 전략 및 오픈소스SW 개발 환경이 변화되는 상황에 맞춰서 정책과 프로세스도 역시 발전시켜야 한다.

##### 자동화 도구를 지원하라

프로세스를 자동화하고 간소화하기 위한 도구를 지원한다.

자동화 도구를 도입하는 방법으로는 (1) 자체 개발, (2) 상용도구 구매 및 (3) 오픈소스SW 도구 도입 등이 있을 수 있다. 오픈소스SW 도구에는 라이선스 비용이 발생하지 않는다. 다만 라이선스 비용이 없다는 사실과 총소유비용<sub>TCO, Total Cost of Ownership</sub>이 낮다는 사실은 구분해야 한다. 도입과 연동, 탐지 규칙 조정, 오탐 정리, 운영 인력에서 비용이 발생하며 그 합이 상용 도구 구독료를 넘는 경우도 있다. 한편 오픈소스SW 도구를 사용하면서 기업이 자체적으로 수정 및 추가한 부분을 다시 커뮤니티에 기여함으로써 오픈소스SW 생태계 발전에 기여할 수도 있다.

도구를 선택할 때는 다음 여섯 가지 기준을 각각 확인한다.

| 기준 | 확인 방법 |
|------|-----------|
| 스캔 정확도(오탐률·미탐률) | 자사 저장소 중 구성이 알려진 프로젝트 하나를 표본으로 스캔해 실제 사용 목록과 대조한다 |
| 지원 SBOM 포맷(SPDX·CycloneDX) | 산출된 SBOM 파일을 각 포맷의 공식 검증 도구로 통과시켜 본다 |
| VEX 발행 지원 | 탐지된 취약점에 '영향 없음' 판정을 기록하고 VEX 문서로 내보낼 수 있는지 확인한다 |
| 스캔 대상 범위(소스·바이너리·컨테이너·모델) | 배포 산출물의 실제 형태를 나열하고 그중 몇 가지를 스캔할 수 있는지 센다 |
| CI/CD 연동성 | 사내에서 쓰는 빌드 파이프라인에 시험 잡을 하나 붙여 실패 조건과 리포트 형식을 확인한다 |
| 운영 인력 확보 가능성 | 도구를 설치·갱신하고 오탐을 판정할 담당자와 그 업무 시간을 배정할 수 있는지 확인한다 |

초기에는 오픈소스SW 도구로 시작하되, 운영 인력을 확보할 수 있는지를 먼저 따진다.

개별 도구의 세부 내용은 [오픈소스SW 사용하기](../using/#오픈소스sw-관리-도구-소개)에서 다룬다.

## OSPO 참고 자료

### OSPO 가이드

TODO Group은 기업이 OSPO를 설립하고 운영하기 위한 가이드를 제공하고 있어서 이를 소개한다.

* [How to create an open source program office](https://todogroup.org/resources/guides/how-to-create-an-open-source-program-office/)[^howtoospo]
* [Measuring your open source program's success](https://todogroup.org/resources/guides/measuring-your-open-source-programs-success/)[^measuring]
* [Tools for managing open source programs](https://todogroup.org/resources/guides/tools-for-managing-open-source-programs/)[^tools]

[^measuring]: Measuring your open source program's success, TODO Group : https://todogroup.org/resources/guides/measuring-your-open-source-programs-success/
[^tools]: Tools for managing open source programs, TODO Group : https://todogroup.org/resources/guides/tools-for-managing-open-source-programs/


### OSPO 기업 사례

또한, TODO Group은 Microsoft, Meta, Uber 등 오픈소스SW를 효과적으로 활용하는 기업들이 어떻게 OSPO를 운영하고 있는지, 각 기업의 사례를 취합하여 공개하였다. 이를 참고하면 더 구체적인 인사이트를 얻을 수 있다.

* [Meta](https://todogroup.org/resources/case-studies/meta/)[^meta]
* [Microsoft](https://todogroup.org/resources/case-studies/microsoft/)[^microsoft]
* [Comcast](https://todogroup.org/resources/case-studies/comcast/)[^comcast]
* [Capital One](https://todogroup.org/resources/case-studies/capital-one/)[^capitalone]
* [Porsche](https://todogroup.org/resources/case-studies/porsche/)[^porsche]

[^meta]: Meta's OSPO : https://todogroup.org/resources/case-studies/meta/
[^microsoft]: Microsoft's OSPO : https://todogroup.org/resources/case-studies/microsoft/
[^comcast]: Comcast's OSPO : https://todogroup.org/resources/case-studies/comcast/
[^capitalone]: Capital One's OSPO : https://todogroup.org/resources/case-studies/capital-one/
[^porsche]: Porsche's OSPO : https://todogroup.org/resources/case-studies/porsche/

이 외의 사례는 [TODO Group 사례 인덱스](https://todogroup.org/resources/case-studies/)[^case-index]에서 전체 목록을 볼 수 있다.

[^case-index]: TODO Group Case Studies : https://todogroup.org/resources/case-studies/

끝으로, SK텔레콤의 OSPO에 대한 글을 소개하며 글을 마친다: [SK텔레콤 OSPO](https://sktelecom.github.io/about/ospo/)[^sktospo]
[^sktospo]: SK텔레콤 OSPO : https://sktelecom.github.io/about/ospo/

{{% alert color="success" %}}

지금까지 OSPO가 무엇인지, 구성 절차, 인원 구성과 역할에 대해 알아보았다. 소프트웨어 제품 및 서비스를 개발하는 기업이라면 많은 오픈소스SW를 사용하고 있을 것이다. 그런데도 오픈소스SW 거버넌스 체계가 전혀 없거나 주먹구구식으로 관리하고 있다면 이번 기회에 OSPO를 준비해보자. 하루아침에 팀장을 세우고 그럴싸한 팀을 꾸리라는 것은 아니다. 처음부터 OSPO의 모든 역할을 담당할 조직을 세우는 것보다는 한 명의 오픈소스 프로그램 매니저를 임명하는 것부터 시작하는 것이 중요하다. 한 명이라도 전담 인력을 지정하여 OSPO의 역할을 차근차근 수행할 수 있게 한다면 오픈소스SW의 진정한 가치를 발견할 수 있는 가능성이 열릴 것이다.

{{% /alert %}}
