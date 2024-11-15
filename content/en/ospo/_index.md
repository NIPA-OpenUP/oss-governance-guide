---
title: "OSPO"
linkTitle: "4. OSPO"
weight: 50
description: >
   
---

현대의 ICT 기업은 소프트웨어 제품과 서비스 개발을 위해 오픈소스를 필수로 사용한다. 기업은 오픈소스로부터 최대한의 가치를 창출하고 동시에 법적인 리스크를 완화하기 위한 오픈소스 거버넌스 체계 수립이 필요하다. 글로벌 ICT 기업은 오픈소스 거버넌스 체계를 구축하고 이를 성장시키기 위해 OSPO<sub>Open Source Program Office</sub>라는 조직을 운영하고 있다. OSPO는 기업의 오픈소스 거버넌스 체계를 구축할 뿐만 아니라 기업의 성공을 위한 오픈소스 전략을 수립하고 실행하는데 필요한 정책, 프로세스 및 도구를 제공한다.

Microsoft, Google, Twitter, Netflix와 같은 소프트웨어 분야 리더 기업뿐만 아니라 삼성전자, Comcast, Intel과 같은 전통 IT 기업도 OSPO를 운영하고 있다. 이러한 거대 기업이 아니더라도 IT, 가전, 금융 및 통신 분야에서의 50% 이상 기업이 OSPO를 만들었거나 만들 예정이라는 [조사 결과](https://github.com/todogroup/survey/tree/master/2019)[^todo-survey]도 있다.

[^todo-survey]: TODO Group survey : https://github.com/todogroup/survey/tree/master/2019

이 장에서는 OSPO의 역할 및 책임을 알아보고 국내 기업이 OSPO를 설립하기 위한 방법을 설명한다.

> 이 장의 내용은 TODO Group의 [How to create an open source program](https://todogroup.org/guides/create-program/)[^howtoospo]의 내용을 기반으로 작성하였다.

[^howtoospo]: How to create an open source program : https://todogroup.org/guides/create-program/

## OSPO 정의와 역할

### 오픈소스 프로그램이란?

먼저, 오픈소스 프로그램이란 용어를 살펴보자. 오픈소스 프로그램<sub>Open Source Program</sub>이란 기업이 오픈소스를 활용하면서 (1) 라이선스 위반, 보안취약점 리스크는 완화하고 (2) 오픈소스로부터 최고의 가치를 창출하기 위한 프로그램이다. 여기에는 오픈소스 정책과 프로세스 수립, 그리고 이를 자동화/효율화할 수 있는 도구를 지원하는 일이 포함된다.

{{< imgproc osp Fit "768x768" >}}
<center>[오픈소스 프로그램]</center>
{{< /imgproc >}}


### OSPO란?

OSPO<sub>Open Source Program Office</sub>는 오픈소스 프로그램을 만들고 운영하기 위한 조직이다. 어떻게 기업의 오픈소스 컴플라이언스를 관리할지, 개발자가 외부 오픈소스 프로젝트에 기여하기 위한 절차는 무엇인지, 사내의 프로젝트를 오픈소스로 공개하기 위한 절차는 무엇인지는 모두 OSPO가 수행해야 할 전략적 결정이다.

기업이 오픈소스에서 최대의 이익을 창출하기 위해서는 OSPO를 만들고 이를 통해 기업의 오픈소스 활동을 관리 및 지원해야 한다. 기업이 OSPO를 운영하며 오픈소스를 적극적으로 활용한다면 아래와 같은 효과를 기대할 수 있다고 알려져 있다.

- 소프트웨어 개발 인재를 유치하고, 기존 인력의 유출을 방지할 수 있다.
- 비즈니스 가치 창출, 혁신 추진을 가속화할 수 있다.
- 개발자가 비즈니스 로직 작성에 집중함으로 비용 절감과 효율 향상을 기대할 수 있다.
- 제품 리더십을 통해 수익 창출과 시장 점유율 확보를 기대할 수 있다.

> TODO Group에서는 [OSPO의 정의](https://github.com/todogroup/ospodefinition.org)[^ospodefinition]에 대해 설명하는 글을 게시하였고, 다음 [블로그](https://sktelecom.github.io/blog/2021/20210418-ospo-definition/)[^ospodefinitionkorean]에서는 이 글을 한국어로 번역하여 소개하였으니 참고하기를 바란다. 

[^ospodefinition]: Open Source Program Office (OSPO) Definition and Guide : https://github.com/todogroup/ospodefinition.org
[^ospodefinitionkorean]: OSPO란? : https://sktelecom.github.io/blog/2021/20210418-ospo-definition/

### OSPO 역할

OSPO의 세 가지 주요 역할은 다음과 같다.

{{< imgproc ospo Fit "768x768" >}}
<center>[OSPO 주요 역할]</center>
{{< /imgproc >}}


#### 1. 오픈소스의 올바른 사용

OSPO는 기업이 오픈소스를 사용하면서 라이선스 의무 사항을 준수할 수 있도록 오픈소스 정책과 프로세스를 수립해야 한다. 기업은 제품과 서비스 개발 시 사용한 오픈소스의 라이선스가 요구하는 바를 준수해야 하는데 이를 위한 활동을 오픈소스 컴플라이언스라고 한다. 기업은 올바른 오픈소스 컴플라이언스 활동을 통해 저작권 침해 리스크를 관리할 뿐만 아니라 오픈소스 커뮤니티에서 기업 브랜드 평판을 높일 수 있다.

이를 위한 세부 사항은 [오픈소스 사용하기](../using/)에서 자세히 다루었다.

#### 2. 외부 오픈소스 프로젝트로의 기여

기업 내 구성원에게 외부 오픈소스 프로젝트에 기여하도록 장려하는 것도 오픈소스를 전략적으로 활용하는 좋은 방법이다. OSPO는 오픈소스 기여 문화를 확산하면서도 기업의 지식재산은 보호할 수 있는 오픈소스 기여 정책을 수립해야 한다.

오픈소스 기여 활동으로 취할 수 있는 혜택과 고려 사항 및 세부 방법은 [오픈소스 기여하기](../contributing)에서 자세히 다루었다.

#### 3. 사내 프로젝트의 오픈소스 공개

오픈소스를 적극적으로 활용하는 기업이라면 오픈소스를 단순히 사용하는 데 그치지 않고, 사내 프로젝트를 오픈소스로 공개하고 커뮤니티를 활성화하여 최대의 가치를 창출한다. OSPO는 기업의 비즈니스 전략을 고려하여 오픈소스 공개 정책을 수립하고, 이를 활성화하기 위한 실행 방안을 마련해야 한다.

이를 위한 세부 절차 및 방법은 [오픈소스 공개하기](../releasing/)에서 자세히 다루었다.


## OSPO 구성

### OSPO 구성 절차

그러면 기업이 OSPO를 만들기 위한 절차를 알아보자. 

{{< imgproc feedback Fit "768x768" >}}
<center>[OSPO 구성 절차]</center>
{{< /imgproc >}}

#### 1. 리더를 임명하라

먼저 OSPO를 만들고 운영할 수 있는 적합한 리더를 찾는 것이 중요하다. 다음과 같은 역량을 갖고 있다면 OSPO의 리더로 적합하다.

- 오픈소스의 가치와 발전 가능성에 공감하고, 이를 사내에 전파하고자 하는 열정이 있다.
- 오픈소스 프로젝트에 개발자, 기여자로 참여한 경험이 있고, 오픈소스 개발 방법론을 충분히 이해한다.
- 기업의 비즈니스 전략과 일치하는 방향의 오픈소스 전략을 수립할 수 있도록 기업의 비즈니스를 폭넓게 이해한다.
- 오픈소스 전략과 정책을 모든 구성원이 이해하도록 전파할 수 있는 커뮤니케이션 역량을 갖추었다.
- 여러 기술 분야를 폭넓게 이해하여 개발자와 기술적인 소통이 가능하다.

누군가 임시로 역할을 맡아서 시작할 수도 있다. 하지만 OSPO가 조기에 올바른 역할을 수행하고 견고히 자리 잡기를 바란다면 전담하여 책임질 수 있는 리더를 임명해야 한다.

#### 2. OSPO의 역할을 정의하라

기업의 OSPO가 어떤 역할을 수행할지 정의한다. 기업마다 규모나 업종이 다르고, 오픈소스를 통해 얻고자 하는 목적이 다르므로 OSPO의 역할이 달라질 수 있다. 

일반적으로 OSPO는 오픈소스 정책을 수립하고 이를 실행하기 위한 프로세스를 구성한다. 또한 프로세스 활동을 가능한 자동화하기 위한 도구를 개발하여 제공하는 역할을 수행한다. 이 과정에서 부서 간 협업을 유도하고, 발생하는 이슈를 해결한다.

OSPO는 구조화된 정책과 프로세스를 제공해야 하지만, 유연성도 유지해야 한다. OSPO가 모든 분야에 전문성을 갖고 모든 의사결정을 내리는 것은 현실적으로 불가능하다. OSPO는 오픈소스 사용자와 기여자에게 도움이 필요할 때 컨설팅을 제공하고 구성원이 스스로 개인 또는 기업의 비즈니스 결정을 내일 수 있도록 허용해야 한다. 궁극적으로는 기업과 구성원의 요구를 모두 충족하기 위한 역할과 책임의 적절한 균형을 설정하는 것이 중요하다.


#### 3. 피드백을 수렴하라

한 번에 OSPO의 모든 것을 구축하기는 쉽지 않다. 우선 기본적인 사항을 준비한 후 기업 내부의 모든 관련 당사자로부터 피드백을 받아서 보완해나가는 것이 필요하다. 

경영진으로부터 개발자에 이르기까지 모든 구성원의 피드백을 수렴한다. 기업의 비즈니스 전략이나 구성원의 요구 사항을 고려하지 않고 OSPO가 단독으로 수립한 정책이 장기적으로 성공하기를 기대할 수는 없다.


### OSPO 구성 방법

#### 어느 조직 내에 OSPO를 만들어야 하나?

OSPO는 기업의 어느 부서 내에 만드는 것이 적합하냐는 질문이 나올 수 있다. 개발 조직 내에 만들지, 아니면 법무 조직에 있어야 하는지를 고민할 수 있는데, 이는 기업의 비즈니스와 오픈소스 전략에 따라 달라진다.

##### 개발 조직 속에서의 OSPO

오픈소스를 활용하는 부서는 주로 소프트웨어 개발 조직이기 때문에 일반적으로 OSPO를 개발 조직 내에 만든다. 이를 통해 개발자가 더 효과적이고 생산적으로 오픈소스를 활용하도록 지원한다.

##### 법무 조직 속에서의 OSPO

대규모의 IP(지식 재산) 포트폴리오를 보유한 기업이라면 OSPO가 법무 조직 내에 있는 게 유리할 수 있다. 오픈소스를 활용하면서 법무 조직과 긴밀하게 협력하여 IP 관련 법적 문제가 발생할 가능성을 사전에 점검하고 대응할 수 있다. 주로 칩세트와 같이 IP 집약적인 하드웨어 개발 회사에 적합하다.

##### 마케팅 조직 속에서의 OSPO

기업이 오픈소스를 사용하여 개발한 제품이나 서비스를 판매하는 비즈니스를 주력으로 한다면 마케팅 부서 내부에 OSPO를 만들어서 오픈소스 제품의 홍보와 마케팅에 집중하는 것이 유리할 수 있다.

#### OSPO에는 어떤 인원이 필요한가?

OSPO의 인원 구성과 각 역할 및 책임을 알아보자.

미리 한가지 첨언하면 아래의 인원 구성은 전략적으로 OSPO에 충분한 리소스를 투입해야 할 이유가 명확히 있는 기업을 고려하여 설명하였다. 기업의 규모가 크지 않고, 오픈소스 활용을 이제 시작하는 기업이라면, 처음부터 아래의 모든 인원과 역할을 지정할 필요는 없다. 한 명의 오픈소스 프로그램 매니저를 임명하고, 관련 부서와의 협업을 통해 OSPO의 역할을 수행하면서 점차 규모를 키워갈 것을 권장한다.


{{< imgproc role Fit "768x768" >}}
<center>[OSPO의 인원 구성과 역할]</center>
{{< /imgproc >}}


##### 오픈소스 프로그램 매니저

오픈소스 프로그램 매니저는 오픈소스 프로그램을 관리하고 전략을 수립하는 전담 인원으로서 다음의 역할을 담당한다.
* 기업의 수익, 브랜드 인지도, 개발자 역량, 채용 등 비즈니스 목표에 부합하는 오픈소스 전략을 수립한다.
* 기업의 모든 오픈소스 활동을 감독한다.
* 효과적인 오픈소스 활동을 위한 정책을 수립하고 프로세스를 구축한다.

오픈소스 프로그램 매니저는 이처럼 기업 전반에 걸쳐 영향력을 미칠 수 있는 역할이기 때문에 효율성을 극대화하기 위해서 가능하다면 임원급 직책을 가진 자가 맡는 게 좋다.

##### 컴플라이언스 담당

외부로 배포 혹은 서비스하는 제품 소프트웨어 및 서비스를 개발하는 조직은 오픈소스 컴플라이언스 활동을 수행해야 한다. 즉, 배포 소프트웨어에 포함된 오픈소스가 무엇인지 확인하고, 해당 오픈소스 라이선스의 의무사항을 준수해야 한다. 컴플라이언스 담당은 기업의 오픈소스 컴플라이언스를 보장하기 위한 역할을 담당한다.

##### 법무 담당

오픈소스를 사용하거나 외부에 기여하는 활동은 저작권에 기반하여 라이선스를 받거나 부여하는 활동이다. 결국 법적인 판단이 필요한 일이 발생할 수밖에 없다. 따라서, OSPO는 법률 전문가를 포함해야 한다. 직접 포함할 수 없으면 법률 조언을 받을 수 있는 창구를 마련해야 한다.

OSPO의 법률 담당은 다음의 역할을 수행한다.
* 오픈소스 라이선스 및 기타 법적 자문을 제공한다.
* 외부 오픈소스 프로젝트에 기여 활동이 법적인 문제를 발생시킬 우려는 없는지 점검한다. 여기에는 CLA (Contributor License Agreement) 검토 등의 활동을 포함한다.

대기업의 경우 오픈소스 전문 변호사를 고용하는 경우도 있지만, 그렇지 않을 경우, 외부 컨설팅 업체를 활용하는 것도 고려할 수 있다.

참고로 NIPA의 오픈업(오픈소스 통합지원센터)에서는 오픈소스 활용을 위한 신뢰성 있는 [컨설팅 서비스](https://www.oss.kr/plaza_intro)[^plaza]를 제공하고 있다.

[^plaza]: 오픈업 컨설팅 서비스 : https://www.oss.kr/plaza_intro

##### IT 지원 담당

오픈소스 프로그램을 효율적으로 운영하기 위해서는 가능한 자동화해야 한다. IT 지원 담당은 도구를 활용하여 오픈소스 컴플라이언스와 오픈소스 보안 취약점 점검을 자동화하기 위한 역할을 담당한다.

##### 오픈소스 에반젤리스트

기업의 프로젝트를 오픈소스로 공개하고, 외부 프로젝트에 기여하는 활동을 장려하는 기업이라면 이를 외부에 홍보하기 위한 오픈소스 에반젤리스트의 역할이 중요하다. 오픈소스 에반젤리스트는 오픈소스 콘퍼런스 참여, 발표, 프로젝트 후원, 주기적인 홍보 문서 배포 등의 방법으로 기업의 오픈소스 활동을 외부에 알리는 역할을 담당한다.


#### 구체적으로 OSPO는 무엇을 해야 하는가?

##### 정책을 수립하라

오픈소스를 사용하면서 오픈소스 라이선스를 준수하지 않을 경우, 비즈니스 기회를 놓치거나 수익 손실 (판매 손실, 인수 실패 등), 법적 피해 (IP 소유권 손실, 수익 또는 파트너십 악화, 벌금 등) 및 브랜드 손상의 위험이 발생한다. 올바른 오픈소스 사용을 위한 정책을 수립해야 한다. 또, 올바른 오픈소스 커뮤니티에 구성원이 기여하는 방법, 내부 프로젝트를 오픈소스 커뮤니티에 공개하기 위한 방법도 포함해야 한다. 즉, OSPO는 다음을 다루는 오픈소스 정책을 수립해야 한다.

1. 오픈소스 사용 정책 : 구성원이 Github 등 외부 저장소에서 찾은 소스 코드를 컴플라이언스와 보안 취약점 관점에서 올바르게 사용하기 위한 방법
2. 오픈소스 기여 정책 : 구성원이 외부 오픈소스 프로젝트에 기여하기 위한 방법
3. 오픈소스 공개 정책 : 사내 프로젝트를 오픈소스로 공개하기 위한 방법

오픈소스 커뮤니티에서는 이러한 오픈소스 정책을 위한 템플릿 문서를 작성하여 공개하고 있다.  아직 오픈소스 정책이 없는 기업은 이러한 템플릿 문서를 참고하면서 기업에 맞게 개선하면 더 수월하게 정책을 수립할 수 있다. 한 번에 다 하려고 하기보다 계획을 수립하여 순차적으로 진행하는 곳이 좋다.

- Linux Foundation의 [Generic FOSS Policy](https://wiki.linuxfoundation.org/_media/openchain/lf_compliance_generic_foss_policy.pdf)[^fosspolicy]
- Google의 [Sample Policy](https://opensource.google.com/docs/)[^samplepolicy]
- NIPA의 [기업 오픈소스 거버넌스 OpenChain 해설서](https://openchain-project.github.io/OpenChain-KWG/guide/nipa_openchain/appendix/1-policy-template/)[^policy-template]

[^fosspolicy]: Linux Foundation의 Generic FOSS Policy : https://wiki.linuxfoundation.org/_media/openchain/lf_compliance_generic_foss_policy.pdf
[^samplepolicy]: Google의 Sample Policy : https://opensource.google.com/docs/
[^policy-template]:  NIPA의 기업 오픈소스 거버넌스 OpenChain 해설서 : https://openchain-project.github.io/OpenChain-KWG/guide/nipa_openchain/appendix/1-policy-template/

##### 정책을 전파하라

오픈소스 정책을 수립하는 것에 그쳐서는 안 되며, 이를 전사에 확산하는 노력을 병행해야 한다. 효과적인 확산을 위해서는 기업 내 고위 임원의 장기적인 지원이 필요하다. 이를 위해 CTO 또는 CIO에게 오픈소스 정책의 중요성을 설득력 있게 설명하고 지원을 요청한다.

모든 개발자가 오픈소스 정책의 존재를 알 수 있도록 해야 한다. 또한 법무팀, 구매팀과 같은 비개발 조직에서도 오픈소스 정책 활동에 참여하도록 환경을 조성한다.

다음은 오픈소스 정책과 문화를 확산하기 위한 한 예이다.

1. 오픈소스 교육 과정을 개설하여 기업 내 모든 개발자가 오픈소스 사용 및 기여를 이해하고, 참여하게 한다.
2. 기업 내 오픈소스 전문가로 구성된 커뮤니티를 만든다.
  * 오픈소스 커뮤니티 활동을 경험한 전문가들 먼저 참여하게 한다.
  * 전문가들은 정기적으로 세미나 등을 통해 다른 개발자들에게 오픈소스 활동을 알린다.


##### 프로세스를 구축하라

정책이 기업의 올바른 오픈소스 활동을 위한 요구 사항 및 규칙이라고 한다면, 프로세스는 각 소프트웨어 개발 단계에서 정책을 준수하기 위해 수행해야 하는 일련의 절차이다.

Linux Foundation이 출간한 Open Source Compliance in the Enterprise에서는 이러한 프로세스를 설명하고 있다.

{{< imgproc process Fit "768x768" >}}
<center>Linux Foundation, 오픈소스 컴플라이언스 프로세스 : https://www.linuxfoundation.org/compliance-and-security/2018/12/open-source-compliance-in-the-enterprise</center>
{{< /imgproc >}}


더불어 OpenChain 프로젝트에서 제공하는 Curriculum 문서에서도 유사하게 단계별 프로세스와 주요 활동을 설명하고 있다.

{{< imgproc process2 Fit "768x768" >}}
<center>OpenChain, 오픈소스 컴플라이언스 프로세스 및 주요활동 : https://www.openchainproject.org/resources</center>
{{< /imgproc >}}

위에서 한번 언급한 NIPA의 기업 오픈소스 거버넌스 OpenChain 해설서에서도 [샘플 오픈소스 컴플라이언스 프로세스](https://openchain-project.github.io/OpenChain-KWG/guide/nipa_openchain/appendix/2-process-template/)[^process-template]를 제공한다. 

[^process-template]: 샘플 오픈소스 컴플라이언스 프로세스 : https://openchain-project.github.io/OpenChain-KWG/guide/nipa_openchain/appendix/2-process-template/

기업은 이러한 자료를 참고하여 기업의 환경에 맞게 오픈소스 프로세스를 구축할 수 있다. 주의할 점은 프로세스 활동이 소프트웨어 개발의 병목 현상을 유발하게 해서는 안 된다. 아무리 프로세스가 충실하게 구축되었다고 할지라도 실제 활동을 수행해야 할 소프트웨어 개발 조직에 과부하가 발생한다면, 프로세스는 곧 아무 역할도 하지 못하는 단지 한 장의 종이로 전락할 수 있음을 유념한다.

반복적으로 검토하여 불필요한 절차를 제거하고, 가능한 모든 과정을 자동화하기 위해 지속해서 개선한다. 또한 기업의 비즈니스 전략 및 오픈소스 개발 환경이 변화되는 상황에 맞춰서 정책과 프로세스도 역시 발전시켜야 한다.

##### 자동화 도구를 지원하라

프로세스를 자동화하고 간소화하기 위한 도구를 지원한다.

자동화 도구를 도입하는 방법으로는 (1) 자체 개발, (2) 상용도구 구매 및 (3) 오픈소스 도구 도입 등이 있을 수 있다. 초기에는 오픈소스로 공개된 도구를 도입하는 것이 여러 측면에서 유리할 수 있다. 우선 오픈소스 도구는 무료로 사용할 수 있기 때문에 비용이 발생하지 않는다. 그리고 오픈소스 도구를 사용하면서 기업이 자체적으로 수정 및 추가한 부분을 다시 오픈소스 커뮤니티에 기여함으로써 오픈소스 생태계 발전 및 확산에 기여할 수도 있다.

오픈소스 도구의 세부 내용은 1. 사용하기 의 '오픈소스 관리 도구 소개'를 참고할 수 있다. 

## OSPO 참고 자료

### OSPO 가이드

TODO Group은 기업이 OSPO를 설립하고 운영하기 위한 가이드를 제공하고 있어서 이를 소개한다. 

* [How to Create an Open Source Program](https://todogroup.org/guides/create-program)[^howtocreate]
* [Measuring Your Open Source Program](https://todogroup.org/guides/measuring)[^measuring]
* [Tools for Managing Your Open Source Program](https://todogroup.org/guides/management-tools)[^tools]

[^howtocreate]: How to Create an Open Source Program : https://todogroup.org/guides/create-program
[^measuring]: Measuring Your Open Source Program : https://todogroup.org/guides/measuring
[^tools]: Tools for Managing Your Open Source Program : https://todogroup.org/guides/management-tools


### OSPO 기업 사례

또한, TODO Group은 Microsoft, Facebook, Uber 등 오픈소스를 효과적으로 활용하는 기업들이 어떻게 OSPO를 운영하고 있는지, 각 기업의 사례를 취합하여 공개하였다. 이를 참고하면 보다 구체적인 인사이트를 얻을 수 있다. 

* [Autodesk](https://github.com/todogroup/todogroup.github.io/blob/master/content/en/guides/casestudies/autodesk.md)[^autodesk]
* [Capital One](https://github.com/todogroup/todogroup.github.io/blob/master/content/en/guides/casestudies/capitalone.md)[^capitalone]
* [Comcast](https://github.com/todogroup/todogroup.github.io/blob/master/content/en/guides/casestudies/comcast.md)[^comcast]
* [Facebook](https://github.com/todogroup/todogroup.github.io/blob/master/content/en/guides/casestudies/facebook.md)[^facebook]
* [Microsoft](https://github.com/todogroup/todogroup.github.io/blob/master/content/en/guides/casestudies/microsoft.md)[^microsoft]
* [Red Hat](https://github.com/todogroup/todogroup.github.io/blob/master/content/en/guides/casestudies/redhat.md)[^redhat]
* [Salesforce](https://github.com/todogroup/todogroup.github.io/blob/master/content/en/guides/casestudies/salesforce.md)[^salesforce]
* [SAP](https://github.com/todogroup/todogroup.github.io/blob/master/content/en/guides/casestudies/sap.md)[^sap]
* [Uber](https://github.com/todogroup/todogroup.github.io/blob/master/content/en/guides/casestudies/uber.md)[^uber]
* [Yahoo/Verizon Media](https://github.com/todogroup/todogroup.github.io/blob/master/content/en/guides/casestudies/oath.md)[^yahoo]

[^autodesk]: Autodesk's OSPO : https://bit.ly/3mVdi0I
[^capitalone]: Capital One's OSPO : https://bit.ly/3sxbf4e
[^comcast]: Comcast's OSPO : https://bit.ly/2RAIw1A
[^facebook]: Facebook's OSPO : https://bit.ly/3gkwOmg
[^microsoft]: Microsoft's OSPO : https://bit.ly/3eajxKm
[^redhat]: Red Hat : https://bit.ly/3xfk3iW
[^salesforce]: Salesforce's OSPO : https://bit.ly/3akfzgR
[^sap]: SAP's OSPO : https://bit.ly/32sVznS
[^uber]: Uber's OSPO : https://bit.ly/2Qcxwar
[^yahoo]: Yahoo/Verizon Media's OSPO : https://bit.ly/3mYRmBP

끝으로, SK텔레콤의 OSPO에 대한 글을 소개 하며 글을 마친다. : [SK텔레콤 OSPO](https://sktelecom.github.io/about/ospo/)[^sktospo]
[^sktospo]: SK텔레콤 OSPO : https://sktelecom.github.io/about/ospo/

{{% alert color="success" %}}

지금까지 OSPO가 무엇인지, 구성 절차, 인원 구성과 역할에 대해 알아보았다. 소프트웨어 제품 및 서비스를 개발하는 기업이라면 많은 오픈소스를 사용하고 있을 것이다. 그런데도 오픈소스 거버넌스 체계가 전혀 없거나 주먹구구식으로 관리하고 있다면 이번 기회에 OSPO를 준비해보자. 하루아침에 팀장을 세우고 그럴싸한 팀을 꾸리라는 것은 아니다. 처음부터 OSPO의 모든 역할을 담당할 조직을 세우는 것보다는 한 명의 오픈소스 프로그램 매니저를 임명하는 것부터 시작하는 게 중요하다. 한 명이라도 전담 인력을 지정하여 OSPO의 역할을 차근차근 수행할 수 있게 한다면 오픈소스의 진정한 가치를 발견할 수 있는 가능성이 열릴 것이다.

{{% /alert %}}
