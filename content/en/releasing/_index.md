---
title: "오픈소스 공개하기"
linkTitle: "3. 공개하기"
weight: 40
description: >
   
---

{{% alert color="success" %}}

본 책에서는 기업에서 오픈소스를 공개하는 과정에서 '일반적으로' 발생할 수 있는 과정에 관해 서술한다. 특정 기업의 예외 사항을 모두 다루지 않으니 유의한다.

{{% /alert %}}


이번 장에서는 두 가지 입장에 따라 오픈소스 공개 과정을 서술한다.

1. 오픈소스 공개 가이드 - 기업 편:  
   오픈소스 사무국을 운영하는 입장을 위한 가이드이다. 기업의 구성원으로부터 오픈소스 공개 요청이 있을 경우, 혹은 기업의 사업 차원에서 오픈소스 공개를 진행하는 경우에 고려해야 할 내용을 다룬다.
2. 오픈소스 공개 가이드 - 개발자 편:  
   기업에 속한 개발자의 입장을 위한 가이드이다. 회사 업무의 목적으로 오픈소스를 공개하는 경우, 신경 쓰면 좋을 부분에 관한 내용을 다룬다.

## 오픈소스 공개, 왜?

오픈소스 공개와 운영은 여러 명의 의지가 필요한 일이다. 물론 한 명의 **강력한** 의지로 성공하는 경우도 많다. 하지만 우리는 기업에서의 오픈소스 공개에 관한 내용을 다루고 있으므로 지극히 일상적인 환경을 상상해보도록 한다. 우선 오픈소스 공개의 의지가 있는 몇몇 사람들이 모이고, 의지가 없었던 다른 구성원들의 동의를 얻었을 때 비로소 본격적으로 오픈소스 공개 절차를 시작하게 될 것이다. 실제로 어떤 과정을 거쳐서 새로운 오픈소스를 공개하는가에 대한 이야기를 하기 전에, 다른 사람들을 설득할 때 도움이 될만한 '기업에서 오픈소스를 공개해서 얻을 수 있는 이점'에 대해서 먼저 정리한다.

### 기업에서 얻는 이점

기업의 입장에서는 특히나 "왜 우리가 힘들여서 소스 코드를 공개해야 하는데? 그냥 손해 아닌가?"라는 물음에 답을 하기 어려울 것이다. 하지만 분명 기업에서도 얻는 이점이 있다. 많다!

#### 기술 브랜드 인지도 향상

개발자를 채용하는 기업이라면 어디나 채용이 어렵다고들 한다. 기업이 원하는 인재가 어디에 있는지 찾기도 어렵고, 원하는 인재가 이 기업을 맘에 들어 하기는 더더욱 어려우니 말이다. 이런 상황에서 좋은 개발자를 채용하기 위해서 기업은 여러 가지 노력을 한다. 우리 기업은 어떤 개발 문화를 가졌는지 설명하기 위해 간단하게는 소책자를 제작하는 일에서부터 시작해서 소셜 광고, 동영상 제작, 혹은 채용 설명회에서 장대하게 발표를 한다. 이런 많은 노력 중에서 오픈소스 공개에 대한 소식은 참 매력적인 소재가 된다. 예를 들어 안드로이드 애플리케이션 개발에 사용되는 라이브러리를 오픈소스로 공개했다면 구직 중인 안드로이드 개발자들에게 다양한 내용을 함축적으로 전달할 수 있을 것이다.

- 기업에서 안드로이드 개발을 할 때 어떤 부분에 신경 쓰는지
- 기업에서 이미 근무 중인 안드로이드 개발자들이 어떻게 개발하고 있는지
- 기업에서 이미 근무 중인 안드로이드 개발자들이 얼마나 열정적인지

백문이 불여일견인 법. 이 내용을 설명으로 전달할 수도 있겠지만, 오픈소스로 직접 보여주는 것은 전달력이 한 차원 다를 것이다.

#### 직원 리텐션 효과

오픈소스를 공개하고 난 뒤 얻는 성취감이 있다. 평소에 서비스/제품을 개발하고 난 뒤의 성취감과는 확연히 다른 느낌일 것이다. 유능한 직원이 회사에 머물게 하기 위해서도 여러 가지 노력을 하겠지만, 이렇게 업무 만족도를 높여 자긍심을 갖도록 하는 일 또한 오픈소스 공개를 통해 할 수 있는 일이다.

#### 직원들 기술 역량 향상

직원들이 알아서 성장하면 좋겠지만 쉬운 일이 아니다. 새로운 기술은 쏟아지는데 제자리에 침체된 분위기 속에서는 좋은 결과물을 내기 어려운 법이다. 사내 교육 프로그램을 잘 구성하는 것도 중요하지만 오픈소스를 공개하고 운영하는 과정에서 배우게 되는 기술들은 교육으로 해결하기엔 어려운 것들이다. 어떤 기술들이 있는지는 바로 뒤에 나올 *개발자로서 얻는 이점* 을 참고하자.

#### 오픈소스 커뮤니티로부터 받는 지지 (오픈소스 생태계 선순환)

이 이점을 실제로 체감하기까지는 쉽지 않을 수도 있다. 하지만 먼 미래를 내다보았을 때 결정적인 큰 도움을 받을 기회가 있다면 바로 이런 경우일 것이다. 설명을 위해 동일한 오픈소스를 사용하는 다음과 같은 두 기업이 있다고 가정해보자.

- 기업 A: 오픈소스를 단순히 사용한다. 물론 사용하는 오픈소스들에서 요구하는 라이선스 의무사항은 꼼꼼히 지켰다. 이 오픈소스를 사용하여 개발한 프로그램으로 수익을 만든다.
- 기업 B: 기업 A처럼 오픈소스에 많이 의지하면서도 필요한 플러그인을 직접 개발하고 오픈소스로 공개했다. 아주 많은 사람은 아니지만 몇몇 외부 사람들이 이 오픈소스의 목적이나 주요 기능에 대해 알고 있다.

만약 두 기업이 각각 이 오픈소스를 사용하다가 어떤 문제를 맞닥뜨려 커뮤니티에 해결 방안을 문의한다면? 그동안 관계를 잘 쌓아왔던 기업 B의 물음에 더 우호적으로 반응할 가능성이 크다. 가능한 경우에는 단순히 질문의 대답을 얻을 뿐 아니라 직접적인 해결책을 제시하는 것까지도 기대해볼 수 있을 것이다. 정리하면 오픈소스로부터 도움을 받은 것을 시작으로 새로운 오픈소스가 탄생했으며, 서로에게 도움을 주는 단계에 이르렀다. 이것이야말로 선순환하는 좋은 예시가 아닐까?

#### 커뮤니티 리소스 유입

사실 위에서 언급한 장점을 모두 제치고 가장 강력한 설득 포인트가 될 부분이다. 이 장점을 제대로 이해하기 위해서 오픈소스가 잘 운영되는 방식을 보자.

오픈소스가 공개되고 성공적으로 궤도에 오른다면 다음과 같은 순환을 기대해볼 수 있다. 사람들이 채택할 만큼 충분히 매력이 있다면 사용자들이 늘어날 것이고, 그 사용자들이 뭔가 문제에 맞닥트릴 때마다 버그를 제보하거나 새로운 기능에 대한 아이디어를 제공할지도 모른다. 더 나아가서는 사용자들이 기여자가 되어 직접 개발에 참여하게 된다면 프로젝트는 또다시 성장이 가속화될 것이다.  

{{< imgproc community-resource Fit "768x768" >}}
{{< /imgproc >}}


오픈소스로 공개하지 않은 내부 프로그램의 경우와 비교해본다면 다음과 같이 요약할 수 있을 것이다.
- 훨씬 더 많은 사람으로부터 제공되는 피드백, 아이디어
- 훨씬 더 다양한 환경에서의 활용으로 얻게 되는 안정성(미처 발견하지 못했던 오류를 발견할 가능성이 커짐)
- 훨씬 더 많은 사람의 자발적인 참여로 기업에서 투자하는 리소스를 감소시킴

#### 제품의 셀링 포인트<sub>Selling Point</sub>로 작용

기업이란 이윤을 추구하는 단체이다. 어떤 행동이라도 그 결과가 이윤으로 이어지게 될 때 결정을 내린다. 기업이 판매하는 제품의 고객층이 개발자라면, 기업의 오픈소스 공개는 제품 판매에 도움이 될 수 있다. 예를 들어 제품의 SDK<sub>Software Development Kit</sub>를 제공하는 상황이라고 가정해보자. SDK를 배포하는 이유는 다른 개인이나 기업이 이 SDK를 잘 사용하도록 해서 제품의 활용도와 의존도를 높이기 위함이다. SDK를 배포할 때에는 사용 가이드뿐만 아니라 설명을 위해 샘플 코드를 함께 제공하는 경우가 많다. 그럼에도 불구하고 사용자들은 문제 상황과 마주하게 되고, 질문을 남기는 경우가 많을 것이다. 혹은 버그를 발견해 제보하기도 하도, SDK와 샘플 코드를 다운로드하기 전에는 사용 규칙 동의서에도 서명할 것이다. 그런데 찬찬히 생각해 보면 이 모든 상황은 오픈소스의 개발과 크게 다르지 않다. 오히려 사용자들이 친숙한 환경에 소스 코드를 공개하고, 질문을 받고, 공지 사항을 게시하는 것이 이해에 더 큰 도움이 될 수 있다. 결과적으로는 개발자가 사용자인 제품의 경우에는 사용자들과 오픈소스의 환경에서 소통하여 사용자 친화적인 제품을 만들고 커뮤니티를 형성하며 제품 판매에도 도움이 될 수 있다.

---

이 모든 장점을 단기적으로는 체감하기 어렵다는 점을 꼭 덧붙이고 싶다. 처음 몇 년 동안은 사막에서 오아시스를 찾는 것처럼 허무하게 느껴지겠지만 두고 보시라. 언젠가는 사람들이 끊임없이 찾는 사막의 아름다운 호수가 될지도 모른다!

### 개발자로서 얻는 이점

두 가지 선택지 중에서 하나만을 골라보자. 학생 시절로 돌아가 과제를 한다면? (1) 혼자 하는 과제 vs (2) 조별 과제 중에서 어떤 과제를 선택할 것인가? 누구나 한 번쯤은 조별 과제에서 크게 고생했던 기억이 있을 것이다. 그만큼 다른 사람과 어떤 것을 같이 한다는 것은 쉬운 일이 아니다. 하지만 오픈소스의 경우에는 다른 사람(심지어 전혀 만난 적도, 만날 일도 없을 것 같은 사람)과 함께 했을 때 비로소 그 장점들이 빛을 발하는 것인데 이를 위해서 다양한 노력이 필요하다. 이런 노력을 통해 어떤 실력이 향상되는지 정리한다.

#### 가독성 높은 코드의 작성 실력

만약 혼자만 알아볼 수 있는 코드를 작성했고, 다른 누군가가 사용하다가 예상한 대로 동작하지 않는다고 생각해 보자. 사용자는 직접 어느 부분이 문제인지 알아내지 못하고 단순히 질문만 남기거나, 다른 제품으로 아예 대체해버릴지도 모른다. 반대로 다른 사람들이 읽기 쉬운 코드를 작성한 경우에는? 사용하다 문제가 있는 사람은 직접 문제의 원인을 찾고 해결하는 Pull Request를 보낼지도 모른다. 따라서 미래의 나에게 주어질 숙제를 줄이기 위해서는 다른 사람들이 쉽게 이해할 수 있는 코드를 작성해야 한다.

#### 문서 작성 실력

코드 작성 이외에도 오픈소스의 동작 방식을 잘 설명하는 문서와 주석을 적절히 추가해야 할 것이다. 너무 길고 상세하게만 작성한 글은 가독성을 떨어트린다. 그렇다고 너무 불친절하게 짧게 쓴 글은 이해도를 낮춘다. 본인의 의도를 설명하기 위한 내용을 적절한 순서로 글을 작성하는 연습을 할 것이다. 만약 사용자들이 궁금해하는 내용을 글에서 찾지 못했다면 질문을 남길 것이고, 이를 통해 글에서 부족한 부분을 보완할 수 있다.

#### 커뮤니케이션 실력

오픈소스 개발을 할 때에는 코딩보다도 커뮤니케이션에 더 많은 시간을 쏟게 되는 경우도 있다. 소통할 사람들이 서로 다른 지식을 가졌고, 서로 다른 언어를 사용하고, 또 서로 다른 시간대에 있기 때문이다. 따라서 하나의 문제를 해결하기 위해서는 효율적으로 설명하고, 질문하는 연습을 하게 된다. 꼭 기술적인 커뮤니케이션 스킬뿐만 아니라 다른 사람의 입장을 이해하고, 자만하거나 소극적이지 않은 자세 또한 효율적인 커뮤니케이션에 필수적이다. 따라서 오픈소스를 공개하고 운영하는 과정에서 다양한 방면의 커뮤니케이션 스킬을 익힐 수 있다.

#### 오픈소스의 동작 원리 이해

오픈소스를 잘 사용하는 방법을 누군가가 친절하게 알려주면 좋겠지만 대부분은 스스로 검색하고 찾아보고 공부해야 하는 경우가 많을 것이다. 만약 어떤 오픈소스의 사용법을 익혀서 잘 사용하다가 어떤 문제에 맞닥트렸다고 해보자. 오픈소스의 동작 방식을 모른다면 어디에 질문하고 어떻게 답을 얻는지 알기 어려울 것이다. 다양한 경우에서 오픈소스의 동작 원리를 이해하는 사람에게는 유익한 경우가 많다.

#### 포트폴리오

최근 경력 개발자 채용 공고에서는 특정 대형 오픈소스 사용 경험이나 오픈소스 활동 경험을 우대 사항으로 명시하는 것을 심심치 않게 볼 수 있다. 기업에서 이미 사용하고 있는 오픈소스와 관련된 활동을 한 사람은 이직을 하고 나서도 실무에 바로 투입이 가능하다고 기대하기 때문이다. 또 면접관이 이력서를 볼 때 이전 직장에서의 경력들은 지원자의 설명에만 의존해서 이해하지만, 오픈소스 경력은 직접 확인하여 직관적으로 이해할 수도 있는 이유 때문이기도 하다. 오픈소스를 직접 공개하고 운영한 경험은 바로 위에서 나열한 여러 가지 실력을 쌓아왔다는 증거가 되어 더욱 화려한 이력서를 작성할 수 있을 것이다.



## 오픈소스 공개 가이드 - 기업 편

이제 '왜?' 에 대한 대답이 채워졌다. 그렇다. 아직 5개의 물음이 더 남았다는 뜻이다. 누가? 언제? 어디서? 무엇을? 어떻게? 앞으로는 이 다섯 개의 물음에 답하며 오픈소스 공개의 여정을 알아본다.

### 공개 규칙 마련하기

#### 누가?(1):누가 검토할 것인가? 유관부서들에 오픈소스 공개에 관해 설명하기

오픈소스와 관련이 있을지도 모르는 부서를 상세하게 나열한다면 7개-특허팀, 상표팀, 보안팀, 오픈소스 검수팀(컴플라이언스), 인사팀, 홍보팀&마케팅팀, 법무팀-로 꼽을 수 있다. 물론 인사 사정에 따라 미리 만나야 할 팀이 더 많거나 적을 수도 있다. 요점은 "저희가 이제 오픈소스를 공개하려고 하는데요..." 라고 운을 떼었을 때, 다들 갸우뚱하며 나와는 상관없는 일이라고 흥미를 잃기 전에 특정 부서에서 어떤 점을 주로 고민해주었으면 하는지 미리 잘 설명하자.

##### 1. 특허팀: 공개하려는 프로그램에 자사의 특허가 포함되어있지는 않은지 확인한다.
특허가 포함되었다면 특허에 우선권을 주는 것과 오픈소스 공개로 가져올 혜택 중 어느 쪽을 선택할지 고민이 필요할 것이다. 방어적인 목적의 특허가 포함된 경우라면 사업 이익과는 거리가 먼 경우일 가능성이 높으니 오픈소스 공개로 얻게 될 혜택에 대해서 잘 설명할 필요가 있다.
공개하려는 프로그램에 특허로 출원할 부분이 없을지도 함께 검토가 된다면 좋을 것이다. 오픈소스에 특허가 포함된 경우에는 특허권을 보호해주는 오픈소스 라이선스를 선택해야 할 것이다. 라이선스 선택에 관한 자세한 내용은 오픈소스 공개 가이드 - 기업 편 [어떻게?:어떤 조건으로 공개할 것인가? 공개에 적합한 라이선스 후보군 정하기](#어떻게?:어떤-조건으로-공개할-것인가?-공개에-적합한-라이선스-후보군-정하기)에서 다룬다.

##### 2. 상표팀: 공개하려는 프로그램의 명칭이 타사의 상표권을 침해하지 않는지 확인한다.
부르기 쉽고 의미도 알기 쉬운 이름은 오픈소스가 잘 알려지는 데에 중요한 역할을 한다. 그러나 이 세상에는 이미 출시된 상표가 너무나도 많다. 게다가 오픈소스가 어떤 국가의 사람들이 사용하게 될지는 특정할 수 없기 때문에 광범위한 조사가 필요하다. 만약에 공개한 오픈소스의 명칭이 다른 상표권을 침해한 경우에 발생하게 될 비용과 상표권 출원에 쓰는 비용 중 어느 쪽을 선택할지 고민이 필요하다. 어떤 명칭이 타사 상표와 동일할 경우를 아주 긍정적으로 가정해본다면 실제로는 기존 상표의 브랜드에 '오점'이 될만한 나쁜 일을 한 것은 아닐 것이다. 오히려 사회에 오픈소스를 기부했으므로 긍정적인 이미지라고 해석하는 경우도 있다. 반대로  몹시 부정적으로 가정해본다면 상표 침해로 인한 피해 보상, 그리고 기업 이미지의 타격까지 생각하는 경우도 있을 것이다. 따라서 공개할 오픈소스의 운영 기간과 전파 범위에 따라서 상표 출원까지 할 것인지, 아니면 상표 조사만을 통해 현 시점에서 상표권 침해 리스크가 없는 명칭으로 선택하는 것에서 그칠지 현실적으로 고민해볼 필요가 있다.
명칭의 모든 후보를 다 검토하기에는 많은 시간이 걸리기 때문에 상표의 후보들을 직접 출원되었는지 검색해보는 것도 좋은 방법이다. 한국의 경우에는 [KIPRIS의 상표 검색 서비스](http://kdtj.kipris.or.kr/kdtj/searchLogina.do?method=loginTM)[^kipris]를 이용할 수 있다.

[^kipris]: KIPRIS의 상표 검색 서비스 : http://kdtj.kipris.or.kr/kdtj/searchLogina.do?method=loginTM

##### 3. 보안팀: 공개하려는 프로그램에 기업의 기밀 정보가 포함되어있지는 않은지, 그리고 보안 취약점이 없는지 확인한다.
소스 코드가 직접 공개되는 경우이기 때문에 특정 키워드(민감한 IP 주소, 내부 시스템과 관련된 정보, 직원 개인 정보 등)가 포함되어있지는 않은지 확인이 필요하다. 또 공개하려는 프로그램이 널리 사용되려면 그 안정성을 보장해주어야 할 것이다. 이를 위해 보안 취약점이 없는지 확인이 필요하다.

##### 4. 오픈소스 검수팀: 공개하려는 프로그램에 어떤 오픈소스가 포함되었는지 확인한다.
공개할 소스 코드에 포함된 오픈소스 라이선스의 준수 여부를 확인하기 위해서는 평소와는 조금 다른 접근이 필요하다. 기존에 기업에서 하던 배포 형식과는 조금 다르기 때문이다. 응용 프로그램을 배포하는 것이 아니고 소스 코드를 배포하는 경우를 확인해야 한다. 따라서 소스 코드 형태로 재배포되는 오픈소스들이 있는지, 그리고 의존성 들은 어떻게 배포되는지 확인해야 한다. 또 공개할 오픈소스를 npm, pip, maven central 등을 통해 패키지로도 배포하는 경우에는 어떤 것들이 패키지 배포에 포함되는지 확인해야 한다. 마지막으로 새 오픈소스에 적용할 라이선스와 소스 코드 안에 포함된 오픈소스들의 라이선스들이 서로 상충하지는 않는지도 함께 확인이 필요하다. 이런 다양한 배포 형태를 고려하여 고지문을 작성한다.

##### 5. 인사팀: 직원이 입사할 때 작성한 근로계약서, 비밀유지서약서 등에서 오픈소스 공개는 예외로 간주됨을 인지한다.
모든 직원들은 기업에 입사하게되면 근로계약서를 작성해야 한다. 소프트웨어 개발 직군은 아마 '업무 중에 작성한 소스 코드는 기업의 자산임', '기업에서 작성한 소스 코드는 정해진 곳에만 게시함'이라는 내용의 동의서도 작성했을 것이다. 오픈소스로 공개하는 경우를 생각해보면 자칫 업무 중에 작성한 기업의 자산을 외부의 서버에 게시하는 행위로 오해할 수 있다. 하지만 실제로는 기업의 이름으로, 기업에서 정한 장소에 소스 코드를 올린다는 점을 잘 설명할 필요가 있다.
오픈소스를 공개하고 운영하는 데에는 적지 않은 시간과 노력이 필요하다. 이 과정이 다른 직원들에게 '업무가 아닌 일'을 하는 것처럼 비추어지지 않도록 균형을 잘 맞추어줄 필요가 있다. 예를 들면, 기업에서 공개한 오픈소스를 외부의 사람이 사용하다가 어떤 문제를 마주해 질문을 남겼다고 해보자. 그 질문에 대해서 꼭 메인테이너가 답장을 해줄 의무는 없지만, 고객을 잘 유지하는 것 또한 오픈소스에서는 필수적인 작업이기 때문에 대부분의 경우에는 답장을 하기 위해 시간을 쓰게 된다. 이럴 때에도 사실은 기업의 자산을 더욱 높은 품질로 발전시키는 일을 하는 것이기 때문에 이 또한 업무의 범위에 포함된다는 공감대를 형성해야 한다. 이 공감대가 잘 형성되지 않을 때에는 그 누구도 개인 시간을 들여 기업의 오픈소스를 개발하려고 하지 않을 것이기 때문에 세심한 주의가 필요하다.

##### 6. 홍보팀&마케팅팀: 공개한 오픈소스가 세상에 널리 알려지도록 노력한다.
이제 오픈소스를 공개했다고 해보자. 사람들이 저절로 모여서 이 오픈소스를 구경하고 사용해보고 발전시켜줄 것인가? 냉정하게도 절대 그렇지 않다. 세상에 이런 오픈소스가 새로 탄생했다는 것을 꾸준히 알릴 필요가 있다. 소셜 미디어, 동영상, 기사, 블로그 등 다양한 매체를 통해 오픈소스의 기능을 설명해야 사용자들에게 인식이 될 것인데 이런 작업이 앞으로 꾸준히 있을 것이라는 내용을 홍보팀에서 인지해야 한다. 
오픈소스 그 자체의 홍보에 더해 기업에서 오픈소스 활동을 적극적으로 지원하고 있다는 이미지를 노출하는 내용의 매체 인터뷰에 응한다면 기업 브랜딩의 좋은 수단이 될 것이다.

##### 7. 법무팀: 법적인 부분을 검토하고 오픈소스를 접하는 사람들이 안전한 환경에 있도록 보장한다.
소스 코드를 공개하고 사람들이 널리 활용하는 것. 그리고 여러 사람이 개발에 함께 참여하는 것. 그 과정 이면에는 일상생활에서는 쉽게 이해하기 어려운 규칙이 따른다. 법무팀에서는 대표적으로 다음 두 가지의 상황에서 어떤 리스크가 있을지 법적으로 보장해줄 필요가 있다.
- 소스 코드를 공개하는 시각: 소스 코드를 공개하는 과정에는 여러 가지 리스크가 따른다. 예를 들면, 오픈소스에 자사의 특허가 포함된 경우에는 특허 침해로 손해를 입을 일은 없어야 할 것이다. 혹은 오픈소스에 심각한 결함이 있어 사용자들에게 피해를 준 경우를 생각해보면, 오픈소스를 공개한 쪽에서 배상을 하느라 손해가 발생하는 일도 없어야 할 것이다. 이런 내용은 라이선스에 명시되어 있으며, 법적으로 기업에 피해가 발생하지 않도록 보장해야 한다. 라이선스 선택에 관한 자세한 내용은 오픈소스 공개 가이드 - 기업 편 [어떻게?:어떤 조건으로 공개할 것인가? 공개에 적합한 라이선스 후보군 정하기](#어떻게?:어떤-조건으로-공개할-것인가?-공개에-적합한-라이선스-후보군-정하기)에서 다룬다.
- 오픈소스에 기여를 받는 시각: 기업에서 공개한 오픈소스에 외부로부터 기여를 받는 상황을 가정해보자. 만약 기여자가 작성한 코드만 공개 규칙(라이선스)을 다르게 적용한다면? 나중에 오픈소스를 사용하는 사람들은 혼란에 빠질 것이다. 혹은 더욱 심각하게 이전에 기여한 내용을 다시 회수해가고 싶다고 한다면? 이렇게 오픈소스에 기여를 받을 때(기여할 때)의 규칙은 기여자 라이선스 동의서(Contributor License Agreement, 이하 CLA)에서 명시한다. 개인의 기여에 대해서는 ICLA(Individual CLA), 기업이나 단체를 대표한 기여에 대해서는 CCLA(Company CLA)로 각각 정의한다. 규모가 큰 오픈소스 재단에서 작성한 라이선스를 적용하는 경우에는 이와 상응하는 CLA가 있는 경우가 많다. 따라서 법무팀에서는 이 CLA의 내용을 검토하고 리스크가 없을지 보장해야 한다.

가장 대표적인 CLA의 양식은 다음을 참고한다.
- [Apache Software Foundation Contributor License Agreement](https://www.apache.org/licenses/contributor-agreements.html)[^apache-cla]
- [Cloud Native Computing Foundation Contributor License Agreement](https://github.com/kubernetes/community/blob/master/CLA.md)[^k8s-cla]
- [Python Software Foundation Contributor Agreement](https://www.python.org/psf/contrib/)[^python-cla]

[^apache-cla]: Apache Software Foundation Contributor License Agreement : https://www.apache.org/licenses/contributor-agreements.html
[^k8s-cla]: loud Native Computing Foundation Contributor License Agreement : https://github.com/kubernetes/community/blob/master/CLA.md
[^python-cla]: Python Software Foundation Contributor Agreement : https://www.python.org/psf/contrib/

최근 CLA를 대체하는 DCO(Developer Certificate of Origin, 이하 DCO)를 채택하는 오픈소스들이 늘어나고 있다. CLA는 계약서에 직접 서명하여 제출하는 등 번거로움이 있는 반면에 개발자들이 git commit을 통해 간단히 서명하는 방식이다. 본문도 아주 짧기 때문에 읽기도 쉽고 개발자들이 따르기에도 쉽다는 장점이 있다. 하지만 짧은 내용 안에 담을 수 있는 내용은 제한적이므로 이로는 부족하다는 시각이 있기도 하다. 따라서 공개하려는 프로젝트의 특성에 따라 기여 규칙으로 어떤 것을 선택할지 고민해볼 필요가 있다.

CLA와 DCO에 대한 더욱 자세한 내용은 **기업을 위한 오픈소스 기여 가이드 - CLA (Contributor License Agreement)** 를 참고한다.

#### 누가?(2):누가 공개하고 운영할 것인가? 멤버 역할과 권한 설정 규칙 정하기

오픈소스가 잘 운영되기 위해서는 특정 역할을 맡은 사람이 있어야 한다. 만약 한 명의 메인테이너만 있는 오픈소스에서 그 한 명이 퇴사를 한다면? 그 오픈소스에 이미 커뮤니티가 강력하게 형성이 되어있다면 좋겠지만 그렇지 않다면 오픈소스는 점차 기억 속에서 사라지게 될 것이다. 혹은 너무 많은 사람에게 소유자 권한을 부여한다면? 누군가가 실수로 설정을 바꾸는 경우가 발생할 수 있을 것이다. 따라서 프로젝트의 규모에 따라 최소 몇 명의 멤버가 어떤 권한을 가지게 될지 사전에 정하는 것을 권한다. GitHub을 기준으로 역할별로 갖게 되는 권한을 참고하자.

|역할|권한|
|---|---|
|Read|저장소에 접근하고 clone 하기<br>issue 생성하고 의견남기기<br>pull request를 생성하고 의견남기기<br>`@` 기호로 언급할 수 있는 후보에 등록|
|Triage|Read 역할의 권한 전부<br>issue 관리하기|
|Write|Triage 역할의 권한 전부<br>저장소에 push하기<br>pull request 관리하기|
|Maintain|Write 역할의 권한 전부<br>저장소 설정 중 일부에 접근하기|
|Admin|Maintain 역할의 권한 전부<br>멤버 관리를 포함한 저장소 설정의 전부에 접근하기|

#### 언제?:언제 공개할 것인가? 공개 시점 정하기

오픈소스를 공개할 때는 너무 완성도가 떨어진 소스 코드를 공개하면 안 된다는 것은 많이들 알고 있다. 그렇지만 너무 완벽하게(소프트웨어 개발에서 완벽이란 있을까 싶지만) 공개하는 것도 좋은 전략은 아니다. 공개 이후에 코드 변경이나 문서 작성, 혹은 이슈 관리까지도 포함해서 꾸준히 활동하지 않으면 관리되지 않고 정체되었다는 인상을 주기 때문이다. 따라서 적당한 시점에 오픈소스로 내놓고 발전시키는 과정이 필요하다. 정량적으로 어느 정도의 완성이라고 표현하기는 어렵기 때문에 공개하는 과정마다 이 점을 인지하고 공개 시점을 정할 것을 권한다. 예를 들면 홍보 시점은 자사의 개발자 콘퍼런스 등 시선을 많이 끌 수 있는 시점 등이 될 수 있다.

#### 어디서?:어디에 공개할 것인가? 공개 위치 선정하기

기업에서 처음 오픈소스를 공개하는 경우라면 GitHub 혹은 GitLab 등 인기 있는 오픈소스 저장소에 기업 이름으로된 조직(Organization)을 생성할 수 있는지 확인해야 한다. 미리 선점하는 사람이 우선이기 때문에 모든 절차 중에서 가장 먼저 선점해놓는 것도 좋은 방법이다.
라이브러리를 오픈소스로 공개하는 경우 사람들이 손쉽게 라이브러리를 사용할 수 있도록 패키지 저장소에 배포할 필요가 있다. 잘 알려진 패키지 저장소로는 Maven Central, npm, PyPI 등 프로젝트 성격에 따라 다른데, 소스 코드 저장소와 마찬가지로 Organization 개념으로 동작하는 경우가 많으므로 미리 권한을 얻어두자.
소스를 공개할 때는 언제나 해당 소스에 대한 소개 홈페이지, 기술 블로그 등을 같이 공개하고 그 링크를 소스 저장소에서 접근 가능하도록 하는 것이 좋다.

#### 어떻게?:어떤 조건으로 공개할 것인가? 공개에 적합한 라이선스 후보군 정하기

오픈소스에 적용할 라이선스를 고르기 위해서는 다양한 상황과 우선순위를 고려해야 한다.

##### 공개할 오픈소스가 제품에 포함되고, 제3자에게 이 제품이 배포되는 경우
- 이 오픈소스에 만약 Copyleft licesne를 적용한다고 해도 저작권자와 사용자(라이선스 의무사항을 지켜야 할 사람)이 동일하므로 법적인 이슈가 생길 가능성은 없을 것이다. 하지만 커뮤니티에서는 제품의 소스 코드 또한 공개하는 것을 기대할 수도 있다.
- 이 오픈소스에 만약 Permissive license를 적용한다면 제품에 포함될 법적 고지문에 라이선스와 저작권 표기를 추가하면 된다. 그러나 만약에 대비하여 제품에 포함된 다른 오픈소스들과의 호환성을 고려해볼 것을 추천한다.
##### 공개할 오픈소스가 널리 사용되는 것이 최우선의 목표일 경우
- 사용자들의 진입 장벽을 낮추기 위해서는 Permissive license를 적용하는 것이 유리할 것이다.
- 공개한 이후에 유지보수 계획도 없는 경우에는 Public domain, CC0, Unlicense 등 저작권을 포기하는 쪽도 고려해볼 만 하다. (발표/데모에서 사용하는 code snippet 등)
##### 공개할 오픈소스의 변경 사항을 추적하는 것이 중요할 경우
- 만약 오픈소스 버전과 상용 버전으로 나누어 사업을 하는 경우에는 오픈소스의 변경을 추적하는 것이 중요할 것이다. 어떠한 제한을 두지 않는 경우에는 수익에 지장을 줄 수 있기 때문이다. 이런 경우에는 Copyleft license를 적용하는 편이 유리할 것이다. 물론 변경 사항 이외에 특허권 등을 두루 보호할 수 있는 라이선스를 선택해야 한다.

### 문서화하기

오픈소스 공개를 위한 기반의 마지막 관문에 도착했다. 바로 명확한 문서 작성이다. 그동안 고민했던 왜? 누가? 언제? 어디서? 무엇을? 어떻게? 에 해당하는 내용을 이해하기 쉬운 문서로 작성한다. 특히 문서를 읽는 대상은 주로 오픈소스 공개를 신청하는 개발자들이 될 것이므로 개발자의 시점에 맞춰서 작성하도록 한다. 문서에는 다음과 같은 내용이 들어가면 좋다.

- [ ] 기업에서 오픈소스 공개를 하는 취지와 포부
- [ ] 신청서 작성부터 공개까지 걸리는 전체 예상 시간과 과정
- [ ] 오픈소스 공개 신청서 작성 방법
- [ ] 오픈소스를 공개하기 위해 필요한 검토의 종류와 순서
- [ ] 검토의 목적
- [ ] 각 검토에 걸리는 예상 시간
- [ ] 도움을 받을 수 있는 연락처
- [ ] 오픈소스를 공개하기 전에 개발자들이 알아두면 좋을 내용(미래의 사용자를 위한 문서 작성, 필요하게 될 인프라 등)

#### 오픈소스 공개 신청서

어라, 아직 신청서 양식이 없는데? 아직까지 신청서 양식을 만들지 않은 이유는 검토 과정을 어떻게 정하느냐에 따라 달라지기 때문이다. 오픈소스 공개 검토에 필요한 내용을 각 부서에 확인하고 신청서에 담도록 한다. 예를 들면 상표 검토를 위해 오픈소스의 명칭, 명칭 후보, 명칭을 정하게 된 이유를 제출하게 하거나 보안 검토를 위해 소스 코드 저장소 위치 등을 물어볼 수 있을 것이다. 혹은 신청서에서 검토 내용을 나열하지 않고, 신청자가 직접 각 항목에 대해서 검토를 신청할 수 있도록 그 과정을 안내할 수도 있을 것이다. 따라서 신청서의 내용은 각 기업과 부서의 상황에 따라 편차가 심할 것이므로 특별히 항목을 나열하진 않는다.

하지만 검토를 위한 정보 이외에 신청서의 항목으로 추가하면 도움이 될 만한 내용을 정리한다.

- 공개 목적: 공개 목적이라는 항목에는 대부분 교과서에서 나올 법한 내용을 적는 경우가 많다. 이 항목을 적으면서 오픈소스 생태계에 기여한다는 의지를 더욱 다지게 될지도 모른다. 하지만 특수한 목적을 위해 공개하는 경우도 있다. 예를 들면 어떤 발표의 데모 코드를 공개하거나, 더 이상 유지보수되지 않는 다른 오픈소스를 fork하는 등 여러 가지 이유가 있을 수 있다. 이 경우에는 오픈소스 운영 방침이 조금 달라질 수 있으므로 목적을 확인한다.
- 유사 오픈소스와의 비교: 보통 코드를 작성하는 이유는 어떤 문제를 해결하기 위함이다. 그렇다면 그 문제를 그 개발자만 겪었는가? 이 세상 누군가도 똑같은 문제를 겪고나서 오픈소스로 공개했을지도 모르는 일이다. 따라서 이미 공개되어있는 다른 오픈소스와의 차별점을 명확히 하는 것이 좋다.
- 로드맵: [언제?:언제 공개할 것인가? 공개 시점 정하기](#언제?:언제-공개할-것인가?-공개-시점-정하기) 에서 언급한 것처럼 공개 이후에도 꾸준히 기능을 개선하는 등의 관리가 필요하다. 침체된 오픈소스로 사람들의 기억 속에서 잊혀지기 전에 아주 간단한 계획이라도 고민해볼 필요가 있다.
- 기술 평가 의견: 오픈소스 담당자가 기술적인 측면까지 모두 확인하기는 어렵다. 특히 이 오픈소스가 공개되었을 때 해당 분야의 사람들에게 받게 될 평가가 어떨지는 그 분야의 사람들에게 들어본다면 좋을 것이다. 공개를 신청하는 개발자의 상위 리더로부터 받은 평가 의견이 있다면 프로젝트를 이해하고 홍보하는 데 큰 도움이 될 것이다.
- 리소스 운영 계획: 로드맵이 있다면 개발자들도 깨닫게 될 것이다. 소스 코드 공개에서 끝나는 것이 아니라 앞으로도 계속 꾸준히 시간을 들여야 한다는 것! 현실적으로 생각했을 때 리소스 운영 계획은 앞으로 다른 업무에 매우 의존적으로 결정될 것이다. 따라서 구체적인 계획을 세우기보다는 앞으로 이 오픈소스도 잊지 않고 계속해서 시간을 할애할 것을 인지할 수 있도록 한다.


### 공개하기

드디어! 누군가가 신청서를 제출했다고 가정해보자. 우선 신청서 양식이 빠짐없이, 항목의 목적에 따라 잘 작성이 되었는지 확인한다. 그리고 절차에 따라 검토를 진행한다. 오픈소스 담당자는 검토가 순서와 일정에 따라 잘 진행되고 있는지, 혹시 변수는 없는지 확인하고 챙긴다.

#### 신청서 확인

신청서 양식의 항목에는 알고자 하는 내용이 있을 것이다. 혹시 신청서에서 의도와 다른 내용이 있거나 빠진 내용은 없는지 확인한다.

#### 검토

문서에서 이미 서술한 검토 단계에 따라 진행한다. 오픈소스 담당자는 검토가 일정에 따라 잘 진행되고 있는지, 어떤 변수는 없는지 확인한다.

#### 공개 준비

검토를 모두 마쳤다면 이론적으로는 공개의 준비를 마친 셈이다. 이제는 진짜로 소스 코드를 밖으로 내놓기 위해 해야 할 것들을 설명한다. GitHub과 GitLab을 기준으로 참고 링크를 덧붙였다.

##### 오픈소스 거버넌스 문서 추가

거버넌스는 오픈소스 커뮤니티를 형성하고 사람들이 문제없이 어울리기 위해 필요하다. 사용 규칙은 License에서, 커뮤니티에서 지켜야 할 행동 강령은 Code of conduct에서, 그리고 기여 규칙은 Contributing 에서 정의한다. 이 형식을 따라야 사람들이 쉽게 규칙을 찾아볼 수 있다. 각 문서에 대한 자세한 설명은 *개발자를 위한 오픈소스 기여 가이드 - 오픈소스 프로젝트는 어떤 문서를 제공하는가?* 를 참고한다.

GitHub에서는 다음의 7가지를 설정할 것을 권장한다.

{{< imgproc community-profile Fit "768x768" >}}
<center><i>GitHub Docs, About community profiles for public repositories</i></center>
{{< /imgproc >}}

오픈소스의 거버넌스 문서들이 모두 마련되었는지 확인해주는 도구도 있으니 참고한다.

- [Repolinter](https://github.com/todogroup/repolinter)[^repolinter]

[^repolinter]: Repolinter : https://github.com/todogroup/repolinter

`README.md`, `CONTRIBUTING.md` 의 내용은 프로젝트를 운영할 개발자가 작성하는 것이 더 정확하다. 따라서 작성 요령에 대한 자세한 내용은 _오픈소스 공개 가이드 - 개발자 편: 공개를 준비할 때 알면 좋을 팁_ 에서 다룬다.

CLA는 기여 과정의 하나이기 때문에 Contributing 에서 다루면 좋다. CLA의 양식은 이미 정해두었지만 사람들에게 이 양식을 서면으로 제출하게 한다면 굉장히 불편할 것이다. 따라서 대부분은 전자 서명으로 운영하고 있다. CLA를 관리하는 도구와 관리 운영 사례는 다음을 참고한다.

- [CLA assistant](https://github.com/cla-assistant/cla-assistant)[^cla-assistant]
- [cla-bot](https://colineberhardt.github.io/cla-bot)[^cla-bot]
- [Google Developers Contributor License Agreements](https://cla.developers.google.com/clas)[^clas]
- [Microsoft Contributor License Agreement](https://cla.opensource.microsoft.com)[^mscla]

[^cla-assistant]: CLA assistant : https://github.com/cla-assistant/cla-assistant
[^cla-bot]: cla-bot : https://colineberhardt.github.io/cla-bot
[^clas]: Google Developers Contributor License Agreements : https://cla.developers.google.com/clas
[^mscla]: Microsoft Contributor License Agreement : https://cla.opensource.microsoft.com


오픈소스 생태계에서는 물론 자유와 존중을 가장 중요한 가치로 두고 있지만 얼마든지 익명으로 활동할 수 있는 공간이기도 하다. 따라서 발생할지도 모르는 차별의 상황을 미리 제한하고 혹시 누구에게든지 불편한 상황이 발생했을 때 도움을 청할 수 있는 연락처를 제공해야 한다. 오픈소스 커뮤니티에서 제한하는 언행을 나열하고 이를 어기는 상황이 발생했을 때 조치를 요구할 수 있는 연락처를 제시하는 문서가 바로 Code of conduct 이다.

다음은 가장 대중적인 Code of conduct의 예시이다.

- [Contributor Covenant, A Code of Conduct for Open Source Projects](https://www.contributor-covenant.org)[^contributor-covenant]
- [Django Code of Conduct](https://www.djangoproject.com/conduct/)[^django-coc]
- [Geek Feminizm Code of Conduct](https://geekfeminismdotorg.wordpress.com/about/code-of-conduct/)[^geekcoc]

[^contributor-covenant]: Contributor Covenant, A Code of Conduct for Open Source Projects : https://www.contributor-covenant.org
[^django-coc]: Django Code of Conduct : https://www.djangoproject.com/conduct/
[^geekcoc]: Geek Feminizm Code of Conduct : https://geekfeminismdotorg.wordpress.com/about/code-of-conduct/

##### 저장소 생성, 멤버 권한 설정

검토 과정에서 정해진 이름으로 비공개 저장소를 생성한다. 개발에 필요한 멤버들의 username을 취합하고 비공개 저장소에 접근 권한을 부여한다. Description과 Topics를 추가하면 오픈소스의 개요를 더 간략하게 표현할 수 있다.

- [GitHub - 저장소 생성하기](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-new-repository)[^new-repository]
- [GitHub - 접근 권한 설정하기](https://docs.github.com/en/github/administering-a-repository/managing-teams-and-people-with-access-to-your-repository)[^access-repository]
- [GitHub - Topics 추가하기](https://docs.github.com/en/github/administering-a-repository/classifying-your-repository-with-topics#adding-topics-to-your-repository)[^add-topics]
- [GitLab - 저장소 생성하기](https://docs.gitlab.com/ee/user/project/working_with_projects.html#create-a-project)[^create-repository]
- [GitLab - 접근 권한 설정하기](https://docs.gitlab.com/ee/user/project/settings/index.html#sharing-and-permissions)[^setting-permission]
- [GitLab - 저장소의 Description과 Topics 추가하기](https://docs.gitlab.com/ee/user/project/settings/#general-project-settings)[^general-settings]

[^new-repository]: GitHub - 저장소 생성하기 : https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-new-repository)
[^access-repository]: GitHub - 접근 권한 설정하기 : https://docs.github.com/en/github/administering-a-repository/managing-teams-and-people-with-access-to-your-repository
[^add-topics]: GitHub - Topics 추가하기 : https://docs.github.com/en/github/administering-a-repository/classifying-your-repository-with-topics#adding-topics-to-your-repository
[^create-repository]: GitLab - 저장소 생성하기 : https://docs.gitlab.com/ee/user/project/working_with_projects.html#create-a-project
[^setting-permission]: GitLab - 접근 권한 설정하기 : https://docs.gitlab.com/ee/user/project/settings/index.html#sharing-and-permissions
[^general-settings]: GitLab - 저장소의 Description과 Topics 추가하기 : https://docs.gitlab.com/ee/user/project/settings/#general-project-settings



##### 코드 이전

코드를 옮기기 전에 commit 이력을 모두 공개할 것인지, 삭제할 것인지 정해야 한다. 하지만 검토 과정에서 보안 권고에 따라, 혹은 명칭을 변경하는 등 코드가 수정되었다면 commit 이력을 공개하지 않는 것이 안전하다.

##### 배포 준비

소스 코드를 공개한 이후에 패키지 배포까지 생각하고 있는 경우에는 배포를 어떻게 할지 정해야 한다. 패키지 저장소마다 사용 방법이 다르니 개발자와 상의한다. 배포와 관련한 상세 내용은 오픈소스 공개하기 - 개발자 편: 배포하기 를 참고한다. 

#### 공개

더이상 설정하고 확인할 것이 없다면 이제 비공개 저장소를 공개 저장소로 전환한다.

- [GitHub - 공개 저장소로 전환하기](https://docs.github.com/en/github/administering-a-repository/setting-repository-visibility#changing-a-repositorys-visibility)[^github-chaging-repo]
- [GitLab - 공개 저장소로 전환하기](https://docs.gitlab.com/ee/public_access/public_access.html#how-to-change-project-visibility)[^gitlab-change-repo]

[^github-chaging-repo]: GitHub - 공개 저장소로 전환하기 : https://docs.github.com/en/github/administering-a-repository/setting-repository-visibility#changing-a-repositorys-visibility
[^gitlab-change-repo]: GitLab - 공개 저장소로 전환하기 : https://docs.gitlab.com/ee/public_access/public_access.html#how-to-change-project-visibility

### 공개만 하면 끝인가요? 그 이후에 해야 할 일

소스 코드를 공개하기까지 참 여러 사람의 손길을 거쳐왔지만 아직은 오픈소스를 만들었다고 이야기하기는 이르다. 지금까지는 사람들이 저장소에 방문했을 때 가장 먼저 보이는 부분을 잘 포장하여 첫인상을 만들었다고 볼 수 있다. 그렇다면 단순히 공개되어있는 소스 코드에서 사랑받는 오픈소스로 거듭나기 위해서는 어떻게 해야 할까? 앞으로의 과정이 정말 정말! 중요하다. 앞으로는 커뮤니티를 활성화하고 오픈소스를 성장시키는 과정에 대해 알아본다.

#### 소통하기

현 상태에서 가장 먼저 보이는 문제는 무엇일까? 일단 사람들이 이런 오픈소스가 세상에 있다는 것을 모른다는 것이다. 세상에 새로운 오픈소스가 탄생했다는 것을 적극적으로 알리자.

##### 소셜 미디어

만약 회사를 대표하는 소셜 미디어 계정이 있다면 새로운 오픈소스의 공개 소식을 알리자. 개발자들을 타깃으로 한 개발자 전용 계정이 있다면 더욱 좋다.

{{< imgproc twitter-line Fit "768x768" >}}
<center><i>LINE Developers Twitter : https://twitter.com/line_developers/status/1330773983873011712?s=20</i></center>
{{< /imgproc >}}


{{< imgproc twitter-facebook Fit "768x768" >}}
<center><i>Facebook Open Source Twitter : https://twitter.com/fbOpenSource/status/1356301287026028552?s=20</i></center>
{{< /imgproc >}}

##### 기술 블로그

회사에 기술 블로그가 있는가? 기술 블로그에서는 이 오픈소스를 이용해서 어떤 문제를 해결했는지, 주요 기능은 무엇이 있는지 등을 더 자세히 이야기할 수 있다.

- 새로 공개한 오픈소스를 소개하는 블로그 글: [LINE 기술 블로그 - Mono-repo, Multi-project를 Gradle 플러그인으로 손쉽게 관리하기](https://engineering.linecorp.com/ko/blog/mono-repo-multi-project-gradle-plugin/)[^line-mono]
- 오픈소스의 기능을 소개하는 블로그 글: [LINE 기술 블로그 - Armeria의 서킷 브레이커 사용해 보기](https://engineering.linecorp.com/ko/blog/try-armeria-circuit-breaker/)[^line-armeria]
- 새로 공개한 오픈소스를 도입한 사례를 전하는 블로그 글: [LINE 기술 블로그 - Kafka를 이용한 작업 큐 라이브러리 'Decaton' 활용 사례](https://engineering.linecorp.com/ko/blog/decaton-case-studies/)[^line-kafka]

[^line-mono]: LINE 기술 블로그 - Mono-repo, Multi-project를 Gradle 플러그인으로 손쉽게 관리하기 : https://engineering.linecorp.com/ko/blog/mono-repo-multi-project-gradle-plugin/
[^line-armeria]: LINE 기술 블로그 - Armeria의 서킷 브레이커 사용해 보기 : https://engineering.linecorp.com/ko/blog/try-armeria-circuit-breaker/
[^line-kafka]: LINE 기술 블로그 - Kafka를 이용한 작업 큐 라이브러리 'Decaton' 활용 사례 : https://engineering.linecorp.com/ko/blog/decaton-case-studies/

블로그 글을 업로드하는 것에서 그치지 않고 다시 소셜 미디어로 공유하면 글 확산에 큰 도움이 된다.

{{< imgproc ine-facebook Fit "768x768" >}}
<center><i>https://engineering.linecorp.com/ko/blog/try-armeria-circuit-breaker/</i></center>
{{< /imgproc >}}

##### 웹사이트 제작

오픈소스의 사용법 등을 담은 문서를 단순하게 markdown으로 작성할 수도 있지만 조금 더 시간을 들여 웹사이트를 제작할 수도 있다. 웹사이트가 있는 경우에는 방문자 추척을 할 수 있기 때문에 조금 더 심화된 마케팅까지 진행이 가능하다. 프로젝트의 규모에 따라 웹사이트 제작을 고려한다.

##### 다양한 커뮤니케이션 수단 마련

Issue tracker를 이용해서 사용자들과 소통할 수 있겠지만 사람들은 Issue tracker를 질의응답의 수단으로 잘 생각하지 않는다. 조금 더 가볍게 소통할 수 있도록 [Slack](https://slack.com/intl/ko-kr)[^slack]이나 [Gitter](https://gitter.im)[^glitter]등 대화형 커뮤니케이션을 위한 도구를 사용할 수도 있다. 역시 프로젝트의 규모에 따라 고려한다.

[^slack]: Slack : https://slack.com/intl/ko-kr
[^glitter]: Gitter : https://gitter.im


##### 기술 콘퍼런스 참여

이 세상에는 기술 행사가 많다. 규모도 제각각이고 주제도 다양하다. 그동안은 해외에서 열리는 콘퍼런스에 참여하기 위해서 적지 않은 시간과 비용, 그리고 노력을 들여야 했지만 2020년부터는 대부분의 행사가 온라인으로 전환했다. 온라인 콘퍼런스의 좋은 점은 참석자와 발표자의 다양성이 커진다는 점이다.

##### 로고 제작

오픈소스 프로젝트 하나를 완성도 높은 하나의 제품으로 보이기 위한 효과적인 방법이다. 프로젝트의 특징을 보여주는 로고(symbol)을 제작하여 발표 자료, 홈페이지, 문서 등에서 활용한다면 오픈소스의 브랜드 이미지를 훨씬 강조할 수 있다.

#### 사용자 늘리기

이 오픈소스가 존재한다는 것을 사람들에게 전하긴 했지만 실제로 사용자는 늘지 않을 수도 있다. 다시 사용자의 관점으로 돌아가서 어떤 오픈소스를 채택하기까지 고려해야 할 사항들을 다시 한 번 확인해보자. (_오픈소스 사용 가이드 - 개발자 편: 오픈소스 선택 기준_ 에서 자세히 다루고 있다.) 이를 역으로 이용해보면 다음과 같다.

1. 많이 쓰이고 있는 오픈소스인가? ☞ 사내의 다른 제품/프로젝트에서 도입할 수 있도록 사내에서 이미 적용하고 있는 유즈 케이스를 보여준다. 이후 사용자가 생길 때마다 유즈 케이스를 공유할 수 있도록 독려한다.

2. 팀에서 오픈소스를 배우는데 어렵진 않은가? ☞ 쉽게 읽고 따라 할 수 있는 문서를 제공한다.

3. 유지보수가 잘 되고 있는가? ☞ 꾸준히 기능을 개선한다. 사용자들의 의견에 귀를 기울이고 반영하도록 노력한다.

4. 유사 오픈소스와의 차이점은 무엇인가? (얼마나 효율적인가?) ☞ 이 오픈소스만의 특장점을 README 혹은 다른 문서에서 설명한다.

5. 커뮤니티는 활성화되어 있는가? ☞ 사람들의 참여를 독려하고 커뮤니티를 형성할 수 있도록 분위기를 조성한다.

이 다섯 가지를 효과적으로 이행하기 위해서는 다시 소통하기로 돌아간다.

- 1번과 4번을 위해서는 기술 블로그, 소셜 미디어, 기술 콘퍼런스 등을 통해 지속해서 유즈 케이스와 레퍼런스를 노출하도록 한다.
- 2번을 위해서는 아주 처음 접하는 개발자를 섭외하여 문서를 읽고 따라 해보도록 부탁한다. 만약 잘 안되는 부분이 있다면 그 부분을 설명하는 문서를 보완한다. 홈페이지를 제작하고 튜토리얼을 강화한다.
- 3번과 5번을 위해서는 커뮤니케이션 채널, 이슈 트래커, Pull request에서 적극적으로 소통한다. 그들에게 역으로 질문하며 먼저 다가간다면 생각보다 열린 마음으로 왜 아직 도입을 망설이는지 대답해주기도 한다.

### 요약

지금까지 기업의 오픈소스 담당자의 관점에서 공개 정책을 설정하는 것부터 시작해서 새로운 오픈소스를 공개하기까지의 과정을 살펴보았다. 그 과정을 요약하면 다음과 같다.

**공개 정책 설정**

- 기업에서 오픈소스를 공개하는 목적을 설정한다.
- 오픈소스 공개를 검토할 유관 부서들과 상의한다.
- 오픈소스를 운영할 주체를 결정한다.
- 언제, 어디에 공개할지 장소를 마련한다.
- 어떤 조건으로 공개할지 결정한다. (라이선스 적용)
- 설정한 정책을 바탕으로 공개 신청서와 신청서 작성 가이드를 문서화한다.

**공개하기**

- 신청서를 확인하고 미비한 부분이 없는지 검토한다.
- 공개 정책에서 결정한 검토 과정을 따른다.
- 거버넌스 문서를 추가한다.
- 비공개 저장소를 생성하고 권한을 설정한다.
- 코드를 옮긴다.
- 배포를 준비한다.
- 공개 저장소로 전환한다.

오픈소스 공개와 운영은 마치 다이어트와 같다. 여기까지만 진행한다면 오픈소스 공개를 할 수 없었던 기업에서 얼마든지 훌륭한 오픈소스를 배출해낼 수 있는 기업으로 성장한 것이다. 그러나 소스 코드 공개에 그친다면 지금까지의 노력이 모두 허사가 된다. 꾸준한 노력과 관리, 그리고 마케팅! 앞으로 할 일이 무궁무진하다. 오픈소스 운영의 장점이기도 하고 단점이 될 수도 있는 점이 바로 일정에 덜 쫓긴다는 것이다. 품질이 중요하기 때문에 어떤 구멍을 빨리 메꾼다는 마음가짐이 아닌 구멍을 제대로 메꾼다는 자세로 임하게 된다. 또 성과가 눈에 가시적으로 드러나기 어려운 점도 있다. 그러니 너무 막막하게 생각하고 지쳐 떨어지지 말고, 꾸준히 임할 것을 당부한다.

## 오픈소스 공개 가이드 - 개발자 편

개발자 개인의 입장에서 오픈소스를 공개하면 왜 좋은지에 대해서 공감을 했다면 오픈소스 공개에 도전하는 마음가짐은 완성이다. 그러나 아무리 공개 과정을 설명하는 문서가 읽기 쉬운 글로 작성이 되어있다고 하더라도 어디서부터 무엇을 고민해야 할지 잘 감이 안 올 수도 있다. 이번 장에서는 기업의 일원이 오픈소스 공개를 결심하고 운영하는 과정의 전반에 걸쳐서 미리 알고 있으면 좋을 팁을 정리한다.

### 오픈소스 공개를 준비하기

#### 기업의 입장에서 오픈소스를 판단하는 기준을 생각해보기

그동안 오픈소스를 공개하면 좋은 점에 대해서 장대하게 설명했지만 사실 어떤 오픈소스를 공개하느냐도 빠질 수 없는 성공의 요소이다. "우리 기업에서 왜 이 프로젝트를 오픈소스로 공개해야 하나요?" 라는 질문에 대답하기 위해서는 다음을 미리 고민해보면 도움이 된다.

##### 실력 있는 개발자들의 관심을 끌 수 있는가?
  - 채용과 관련 있는 프로젝트인가?
##### 프로젝트를 사내에서만 개발하는 것 보다 외부의 리소스를 활용하는 것이 더 효율적인가?
  - 실력 있는 개발자들이 참여해서 오픈소스의 품질을 높일 수 있을 것인가?
  - 대중적인 요구 사항을 해결하는 프로젝트인가?
##### 프로젝트가 지속 가능한가?
  - 공개 이후 중장기적으로 지속해서 발전할 수 있는 프로젝트인가? 단순 공개에서 그치진 않을 것인가?

#### 공개 이후 운영 계획에 대해 생각해보기

바로 위에서도 언급했던 '프로젝트의 지속 가능성'에 대해 이야기하려고 한다. 아무리 좋은 프로젝트라도 적절히 돌봐주지 않으면 도태되기 때문이다. 가시적으로도 기업의 Organization에 등록된 저장소가 업데이트된 순서대로 정렬되기 때문에 변경이 없다면 저장소는 페이지 2로 넘어가게 된다. 

사람들이 오픈소스를 선택하는 중요한 기준 중의 하나가 잘 관리되고 있는가? 이다. 따라서 앞으로의 변경을 예고하기 위해서 소스 코드 공개 이후에 발전해나갈 마일스톤을 계획한다. 또 마일스톤을 누구든지 알 수 있도록 이슈트래커에 등록해둔다. 특히 다른 업무에서 이 오픈소스를 사용하는 경우라면 아주 좋다. 사용하면서 필요한 기능을 지속해서 오픈소스에 반영할 수 있도록 한다. 오픈소스 공개 전부터 앞으로 투자하게 될 시간에 대해 미리 인지하고 있어야 한다. 

외부 개발자의 기여를 유도하기 위해서는 지속적인 관리와 기술적인 또 사업적인 홍보도 필요하다. 또한 커뮤니티와의 모든 소통, 이슈에 대한 대응, 기여의 수용 절차에 관한 정책도 준비되어야 한다. 

#### 오픈소스 운영에 필요한 도구 탐색하고 공부하기

오픈소스를 운영하면서 모든 것을 다 수작업으로 할 필요는 없다. 저장소와 연동되는 다양한 도구들이 많으니 미리 탐색해볼 것을 추천한다. 상용 도구에도 오픈소스에 사용하면 가격을 할인해주는 경우가 많다. 그러나 역시 오픈소스에서 무료로 사용할 수 있는 도구들이 더 대중적으로 쓰이고 있다. 오픈소스에서 무료로 사용할 수 있으며, GitHub/GitLab과 연동이 가능한 몇 가지 도구들을 나열한다.

- Contiuous Integration - [Travis CI](https://www.travis-ci.com)[^travis-ci]
- Contiuous Integration - [CircleCI](https://circleci.com)[^circleci]
- Test coverage management - [Codecov](https://about.codecov.io)[^codecov]
- Pull request management - [Pull Panda](https://pullpanda.com)[^pullpanda]
- Dependency update management - [Dependabot](https://dependabot.com)[^dependabot]

[^travis-ci]: Travis CI : https://www.travis-ci.com
[^circleci]: CircleCI : https://circleci.com
[^codecov]: Codecov : https://about.codecov.io
[^pullpanda]: Pull Panda : https://pullpanda.com
[^dependabot]: Dependabot : https://dependabot.com


#### README.md 작성 요령

`README.md`는 오픈소스의 표지이다. 저장소에 방문한 모든 사람에게 가장 먼저 보이는 문서이기 때문이다. 모든 방문자에게 알리고 싶은 내용을 쓰거나 방문자들이 궁금해할 만한 내용을 적어야 한다. 하지만 분량이 너무 길 경우 사람들이 읽지 않고 지나쳐버리는 경우도 있으므로 적당한 분량을 유지한다. 잘 쓴 README의 형식은  [Make a README](https://www.makeareadme.com)[^makeareadme]에 정리되어 있다. 아래는 그 내용 중 일부이다.

[^makeareadme]: Make a README : https://www.makeareadme.com

{{% alert title="Make a README" color="warning" %}}
{{% /alert %}}

> ##### Name
>
> 프로젝트를 잘 설명하는 이름을 선택하고 적는다.
>
> ##### Description
>
> 프로젝트가 무엇을 하는지 설명한다. 방문자들에게 익숙하지 않을 것 같은 개념은 레퍼런스 링크를 추가해둔다. 특징이나 프로젝트의 탄생 배경을 나열해도 좋다. 만약 유사 프로젝트가 있다면 강조하고 싶은 차이점을 나열해도 좋다.
>
> ##### Badges
>
> 다른 README를 보면 특정 정보를 전달하는 작은 이미지들이 나열된 것을 본 적이 있을 것이다. 이 이미지들은 테스트가 통과되었는지 아닌지를 나타내기도 한다. [Shields](https://shields.io)[^shields] 를 이용하여 배지를 만들 수 있다.
[^shields]: Shields : https://shields.io
>
> ##### Visuals
>
> 무엇을 만들든지 스크린숏이나 비디오를 첨부하는 것이 좋다. GIF 형식이 더 많이 이용된다. [ttygif](https://github.com/icholy/ttygif)[^ttygif]를 활용하거나 더 정교한 작업을 위해서는 [Asciinema](https://asciinema.org)[^asciinema]도 참고할만하다.
[^ttygif]: ttygif : https://github.com/icholy/ttygif
[^asciinema]: Asciinema : https://asciinema.org
>
> ##### Installation
>
> [Yarn](https://yarnpkg.com)[^yarnpkg], [NuGet](https://www.nuget.org)[^nuget], 혹은 [Homebrew](https://brew.sh)[^brew]와 같이 특정 생태계 안에서 설치하는 대중적인 방법이 있을 수도 있다. 그러나 이 README를 읽는 사람들이 아주 초심자일 경우를 위해 조금 더 상세한 가이드를 제공하기를 추천한다. 각 단계를 명확하게 나열하는 것은 모호함을 제거하고 사람들이 빠르게 프로젝트를 사용해 볼 수 있도록 한다. 만약 특정 버전의 프로그래밍 언어나 운영체제에서 실행할 수 있는 경우, 혹은 의존성 들을 수작업으로 설치해야 하는 경우라면 **Requirements** 라는 소 목차를 추가하는 것이 좋다.
[^yarnpkg]: Yarn : https://yarnpkg.com
[^nuget]: NuGet : https://www.nuget.org
[^brew]: Homebrew : https://brew.sh
>
> ##### Usage
>
> 예시를 충분히 보여주고 예상되는 결과를 보여준다. 정교한 예시를 README에 모두 나열하지 못해서 링크로 제시하는 것보다 직접 실행해볼 수 있는 가장 작은 단위의 예시를 제공하는 것이 더 낫다.
>
> ##### Support
>
> 사람들이 도움을 구할 방법을 제시한다. 이슈 트래커가 될 수도 있고 채팅이나 이메일 등이 될 수도 있다.
>
> ##### Roadmap
>
> 앞으로의 배포에 대한 어떤 아이디어가 있다면 README에 나열하는 것이 좋다.
>
> ##### Contributing
>
> 만약 다른 사람의 기여를 받아들일 의향이 있다면 기여를 제출하기 전에 따라야 할 것을 설명한다.
>
> 프로젝트를 직접 변경하고 싶어 하는 사람들을 위해서는 어디서부터 시작해야 할지를 설명하는 문서를 제공하는 것이 도움이 된다. 혹은 실행해야 하는 스크립트나 환경 변수 설정에 관한 내용이 들어갈 수도 있다. 모든 단계를 명확히 나열한다. 이 설명은 미래의 자신에게도 도움이 될 수도 있다.
>
> [코드를 정렬(lint the code)](https://stackoverflow.com/questions/8503559/what-is-linting)[^lint-code]하거나 [테스트를 실행(run tests)](https://en.wikipedia.org/wiki/Test_automation)[^run-teat]하기 위한 명령에 대해서도 문서로 남기는 것도 좋다. 이 단계들은 높은 품질의 코드를 유지할 수 있도록 도와주고 변경한 내용이 의도치 않게 어떤 것을 망가트릴 가능성을 줄여준다. 예를 들면 브라우저에서 테스트를 하기 위해 [Selenium](https://selenium.dev)[^selenium] 서버를 사용해야 하는 상황처럼 테스트를 실행하기 위해서 외부 설정이 필요하다면, 이를 위한 설명이 특히나 도움이 될 것이다.
[^lint-code]: lint the code : https://stackoverflow.com/questions/8503559/what-is-linting
[^run-teat]: run tests : https://en.wikipedia.org/wiki/Test_automation
[^selenium]: Selenium : https://selenium.dev
>
> ##### Authors and acknowledgment
>
> 이 프로젝트에 기여한 사람들에게 감사를 표시한다.
>
> ##### License
>
> 오픈소스 프로젝트라면 [어떤 라이선스를 적용했는지](https://www.makeareadme.com/#license-1)[^license-1] 표시한다.
[^license-1]: 라이선스 적용 : https://www.makeareadme.com/#license-1
>
> ##### Project status
>
> 만약 이 프로젝트를 위해 쏟을 시간이나 여력이 더 이상 없다면 README에 개발이 느릴 수 있다거나 혹은 아예 더 이상 개발을 하지 않는다는 메모를 남긴다. 누군가가 이 프로젝트를 fork하거나, 메인테이너/오너로 자원해서 프로젝트를 유지할 수도 있다. 메인테이너를 위한 명시적인 요청을 남길 수도 있다.

이 모든 내용을 다 기재하기 어렵다면 상황에 따라 적절히 생략하거나 추가한다.

잘 작성된 README의 예시들은 [Awesome README](https://github.com/matiassingers/awesome-readme)[^awesome-readme]에서 확인할 수 있다.
[^awesome-readme]: Awesome README : https://github.com/matiassingers/awesome-readme

#### CONTRIBUTING.md 작성 요령

 `CONTRIBUTING.md` 의 작성은 사람들로부터 도움을 받을 수 있는 방법 중 하나이다. 보통 사람들은 정확한 요구를 인지했을 때 도움을 줄 생각을 하기 때문이다. 또 다양한 사람들로부터 기여를 받아 개발을 할 때에 지켜야 할 규칙을 미리 안내할 수 있는 문서이기도 하다. 그렇다면 어떤 내용이 들어가야 미래의 기여자에게도, 메인테이너에게도 도움이 될지 정리한다.

- 받고자 하는 기여의 종류
  - 코드 작성만이 기여는 아니다. 질문을 남기는 방법, 버그를 제보하는 방법, 새로운 기능을 제안하는 방법 등 기대하는 기여의 종류를 나열한다.
- 코드 기여 방법
  - 전체적인 코드 기여 방법을 설명한다. 개발 환경 설정, 저장소 fork 부터 시작해서 변경 사항을 제출하고 받아들여지기까지의 과정을 설명한다. 
- 개발 환경 설정 방법
  - 사람들이 직접 코드를 작성하고 기여를 하기 위한 개발 환경을 설정하는 방법을 설명한다. 
- 코딩 컨벤션 / 스타일 가이드
- Commit 메시지 규칙
- Code of Conduct
  - 커뮤니티 활동을 하면서 지켜야 할 행동 규범에 대해서 언급한다.
- CLA/DCO
  - 기여를 제출할 때 서명해야 할 문서에 대해 안내하고 서명 방법도 함께 설명한다.

`CONTRIBUTING.md`의 예시는 다음을 참고한다.

- [Atom - Contributing to Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md)[^atom-contributing]
- [Kubernetes - Contributor's Guide](https://github.com/kubernetes/community/tree/master/contributors/guide)[^k8s-contributing]    
- [Armeria - Developer guide](https://armeria.dev/community/developer-guide)[^armeria-guide]

[^atom-contributing]: Atom - Contributing to Atom : https://github.com/atom/atom/blob/master/CONTRIBUTING.md
[^k8s-contributing]: Kubernetes - Contributor's Guide : https://github.com/kubernetes/community/tree/master/contributors/guide
[^armeria-guide]: Armeria - Developer guide : https://armeria.dev/community/developer-guide


### 오픈소스 운영하기

오픈소스 공개의 꽃! 바로 커뮤니티와 함께 프로젝트를 운영하는 일이다. 처음에는 단독으로 운영을 시작하겠지만 계속해서 커뮤니티에서 참여할만한 빈 틈을 만들어주어야 한다. 나중에는 나를 대신하여 활동을 해줄 커뮤니티를 만들기 위한 씨앗이라고 생각하면 좋다. 

열정적으로 오픈소스를 운영하는 것은 좋지만 계속해서 혼자 짐을 지면 프로젝트를 오래 지속하기 어렵다. 가능한 선에서 메인테이너가 혼자 짐을 지는 것을 줄여나가도록 한다. 

#### 오픈소스 배포하기

소스 코드를 배포하고 나면 사용이 용이하도록 하기 위해 패키지 배포도 함께 진행할 가능성이 높다. 그러나 평소 업무에서 배포하는 환경과 다른 환경에서 배포를 하게 될 터라 시행착오가 있을 수 있다. 가장 대중적인 오픈소스 패키지 배포의 방법과 자동화 방법은 아래를 참고한다. 

- [Maven Central에 배포하기](https://dzone.com/articles/publish-your-artifacts-to-maven-central)[^maven-central]
- [npm에 배포하기](https://docs.npmjs.com/creating-and-publishing-scoped-public-packages)[^npm]
- [PyPI에 배포하기](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects)[^pypi]
- [자동화: 유용한 GitHub Actions workflow 모음](https://github.com/sdras/awesome-actions)[^actions]

[^maven-central]: Maven Central에 배포하기 : https://dzone.com/articles/publish-your-artifacts-to-maven-central
[^npm]: npm에 배포하기 : https://docs.npmjs.com/creating-and-publishing-scoped-public-packages
[^pypi]: PyPI에 배포하기 : https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects
[^actions]: 유용한 GitHub Actions workflow 모음 : https://github.com/sdras/awesome-actions


#### Issue tracker 활용 best practice

Issue tracker는 현업에서도 많이 사용하고 있는데 오픈소스에서도 똑같이 사용하면 된다고 생각할 수 있다. 그러나 이 Issue tracker를 들여다보는 대상이 사뭇 다르다는 것을 알아야 한다. 현업에서는 주로 회의 등을 통해 선별된 이슈를 Issue tracker에 등록하고, 이에 맞추어 개발 일정을 관리한다. 그러나 오픈소스에서는 의견 교환을 즉시 할 수가 없다. 어떤 의견을 적어놓고 다른 사람이 다른 동의하거나 다른 의견을 제시할 때까지 기다려야한다. 사람들이 궁금한 부분이 있을 때 이 Issue tracker에서 도움을 받지 못한다면 이 일거리는 고스란히 메인테이너에게 돌아온다. 또 사람들은 구체적인 어떤 도움의 요청을 보았을 때 비로소 움직일지 고민한다. 그 고민을 통해 일부는 기여로 이어지게 된다.  

이렇게 다양한 기능을 하는 Issue tracker에서 커뮤니케이션을 조금 더 효율적으로 하기 위한 팁들을 정리한다. 

##### 이슈 템플릿 활용

새 이슈를 생성하려고 New issue 버튼을 클릭하고 빈 화면을 마주하면 어떤 내용을 써야 할지 막막한 경우가 있다. 이슈 템플릿은 프로젝트에서 이슈를 처음 생성하는 사람들에게 이슈 작성 방법을 안내한다. 사람들이 오픈소스 프로젝트를 탐색하고 사용하면서 마주한 질문 거리를 마음속에 쌓아두지 않고 적극적으로 소통하도록 돕는다. 템플릿 예시들에서 체크 리스트를 제공하는 경우를 흔히 볼 수 있다. 이는 이슈를 해결하는 데 필요한 정보들을 미리 제공하도록 유도하는데, 부족한 정보를 묻고 답하느라 사용하는 커뮤니케이션을 줄이고 문제 해결에만 집중하도록 돕는다. 

- [GitHub에서 Issue template를 만드는 방법](https://docs.github.com/en/github/building-a-strong-community/manually-creating-a-single-issue-template-for-your-repository#adding-an-issue-template)[^github-issue]
- [GitLab에서 Issue template를 만드는 방법](https://docs.gitlab.com/ee/user/project/description_templates.html#create-an-issue-template)[^gitlab-issue]
- [이슈 템플릿 예시 모음](https://github.com/stevemao/github-issue-templates)[^issue-templates]

[^github-issue]: GitHub에서 Issue template를 만드는 방법 : https://docs.github.com/en/github/building-a-strong-community/manually-creating-a-single-issue-template-for-your-repository#adding-an-issue-template
[^gitlab-issue]: GitLab에서 Issue template를 만드는 방법 : https://docs.gitlab.com/ee/user/project/description_templates.html#create-an-issue-template
[^issue-templates]: 이슈 템플릿 예시 모음 : https://github.com/stevemao/github-issue-templates

##### Label 활용

이슈의 제목을 명확하게 작성하는 것도 중요하지만 아무래도 문장은 한눈에 어떤 내용인지 파악하기 어렵다. 이슈에 라벨을 달아 필터가 작동할 수 있도록 하고, 이슈의 종류를 한눈에 파악할 수 있게 한다. 

{{< imgproc issue-label Fit "768x768" >}}
<center><i>https://github.com/line/armeria/issues/</i></center>
{{< /imgproc >}}


기여를 염두에 두고 있는 사람들에게는 이런 라벨들이 도전할만한 일감을 탐색하기에 아주 좋을 것이다.

##### 초심자를 위한 이슈 

많은 개발자들은 오픈소스에 기여하는 일을 '언젠간 해보고 싶은 것' 목록에 넣어두는 경우가 많다. 직접 나서지 않는 이유는 여러 가지가 있겠지만 보통 시간이 없어서 다음으로 많이 꼽히는 이유는 '자신이 없어서' 이다. 바로 이런 사람들을 오픈소스 기여의 세계로 불러오는 방법 중 하나가 바로 초심자를 위한 이슈 라벨이다. 

주로 `good first issue` 혹은 `first timers only` 라는 이름으로 지어진 이 라벨은 메인테이너나 기존 커미터들이 해결할 수 있지만 초심자를 위해 남겨두었다는 표식으로 사용된다. 따라서 기존 다른 이슈보다 해결 방안에 대한 더 자세한 설명이나 힌트를 달아놓는 경우가 많다. 이렇게 작은 이슈부터 시작할 수 있는 환경을 만들어 조금씩 어려운 이슈에도 도전할 수 있도록 자신감을 키워주는 과정을 거치도록 한다. 이 과정을 통해 꾸준한 커미터를 만들 수 있다. 

GitHub에서는 사진과 같이 good first issue의 탐색을 장려하는 메시지를 띄워주기도 한다. 

{{< imgproc github-good-first-issue Fit "768x768" >}}
<center><i>https://github.com/line/armeira/issues</i></center>
{{< /imgproc >}}


#### Pull request 운영 best practice

이슈를 둘러보며 기여를 할지 고민만 하던 한 사람이 드디어 Pull request를 만들 결심을 했다고 가정해보자! 이 사람이 헤매지 않고 정기 기여자로 정착하기 위해서는 커뮤니케이션 과정에서 발생할 수 있는 불편함을 최소한으로 줄여야 할 것이다. 물론 CONTRIBUTING 에서 많은 부분을 다루고 있겠지만, 기여 과정을 효율적으로 하기 위한 팁들을 정리한다. 

#####  Pull request 템플릿 활용

각기 다른 생각을 가진 사람들이 어떤 변경을 반영하려고 할 때에는 다른 사람의 동의를 얻어야 할 것이다. 동의를 구하기 위해서는 어떤 문제의식이 있었고, 어떤 변경을 했고, 이로 인해 어떤 결과가 나왔는지에 대한 설명이 필요하다. 하지만 어떤 방식으로 이 논리를 작성해야 할지 모르는 사람들을 위해 Pull request 템플릿을 제공한다. 개발 과정이 익숙한 메인테이너들도 동일한 템플릿대로 작성한다. 다른 사람들이 템플릿을 처음 사용할 때 작성 예시로 참고할 수 있기 때문이다.

문제 해결 이외에도 CONTRIBUTING에서 제시한 각종 개발 규칙이 있을 것이다. 이 내용은 Pull request 템플릿에서 체크리스트로 제공하여 코드리뷰 과정에서 문제 해결에 집중할 수 있도록 돕는다. 

- [GitHub에서 Pull request template를 만드는 방법](https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository)[^github-pr-template]
- [GitLab에서 Merge request template를 만드는 방법](https://docs.gitlab.com/ee/user/project/description_templates.html#create-a-merge-request-template)[^gitlab-pr-template]
- [Pull request 템플릿 예시 모음](https://github.com/stevemao/github-issue-templates)[^pr-template]

[^github-pr-template]: GitHub에서 Pull request template를 만드는 방법 : https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository
[^gitlab-pr-template]: GitLab에서 Merge request template를 만드는 방법 : https://docs.gitlab.com/ee/user/project/description_templates.html#create-a-merge-request-template)
[^pr-template]: Pull request 템플릿 예시 모음 : https://github.com/stevemao/github-issue-templates

##### 적극적으로 댓글을 활용

사람들은 글자로만 소통했을 때 그 어감을 부정적으로 해석하는 경향이 있다. 누군가가 열심히 기여를 했는데 환영받지 못한다고 느낀다면 이 사람은 지속해서 기여하지 않을 가능성이 높다. 따라서 어떤 것이든 긍정적인 반응을 댓글에 남겨두도록 한다. 이모지를 활용하는 것도 좋은 방법이 될 수 있다. 

또 어떤 변경에 대해서 기존에 다른 사람이 개발한 것과 연관이 된다면 이전에 개발했던 사람을 언급하여 확인할 수 있도록 안내한다. 기존 개발자는 해당 코드에 대해 주인 의식을 느낄 수도 있고, 또 새로운 변경이 기존 코드에서 의도했던 것을 헤칠 수도 있기 때문이다. 여러 사람이 참여할수록 커뮤니케이션 비용도 들고 시간도 더 많이 사용하겠지만, 결과적으로는 더 건강하고 적극적인 커뮤니티를 만드는 데 큰 도움이 된다. 이 커뮤니티는 나중에 메인테이너의 많은 일을 줄여주게 된다. 

##### 부드러운 재촉

여러 사람이 함께 개발하고 코드리뷰 과정에 참여하다 보면 누군가의 응답이 늦어져 일이 진행이 안되는 경우가 종종 발생한다. 다른 일을 하느라 오픈소스에 몰두하기 어려운 경우가 대부분이다. 하지만 하염없이 그 사람의 반응을 기다렸다간 다른 의존적인 작업까지 지연이 될 수 있다. 이때에는 당사자를 다시 한 번 언급하여 특정 행동을 요구한다. 어떤 행동을 해달라고 다그치는 것이 아니라 "바쁠 것으로 생각되는데 혹시 이렇게 진행해도 괜찮겠어요?" 혹은 "혹시 이것에 대해 더 의견이 없으신가요?" 등 부드럽게 이야기한다. 

### 요약

지금까지 기업에 속한 개발자들이 오픈소스 공개를 준비하고 운영하는 데에 미리 알면 좋을 팁들을 살펴보았다. 요약하면 다음과 같다. 

**오픈소스 공개를 준비하기**

- 왜 나의 프로젝트를 오픈소스로 공개해야 할지 기업의 입장에서 생각해보기
- 공개 이후에 운영 계획에 대해서 생각해보기
- 오픈소스 운영에 필요한 각종 도구를 탐색하고 공부하기
- `README.md` 잘 작성하기 
- `CONTRIBUTING.md` 잘 작성하기

**오픈소스 운영하기**

- 패키지 배포 방법 탐색하고 공부하기
- Issue tracker 잘 활용하기
  - 이슈 템플릿의 활용
  - 이슈 라벨 활용
  - 초심자를 위한 이슈
- Pull request 잘 활용하기
  - Pull request 템플릿의 활용
  - 댓글 활용
  - 사람들을 부드럽게 재촉하기

이 내용은 오픈소스 담당자의 시각으로 여러 프로젝트가 운영되는 모습을 살펴보면서 "개발자들이 이 점을 조금 더 고려해줬다면 커뮤니티를 더 잘 형성했을 텐데..." 라는 아쉬운 마음이 들었던 상황을 정리한 것이다. 따라서 기술적인 부분과는 거리가 멀다. 하지만 오픈소스에서 기술만큼 중요한 것은 커뮤니케이션이다. 온화한 커뮤니케이션은 더 강력한 커뮤니티를 형성한다. 강력한 커뮤니티는 다시 기술력 향상이 될 밑거름이 되고, 오픈소스가 성장하는 선순환의 고리가 시작된다. 

이 뿐만 아니라 _오픈소스 공개 가이드 - 기업 편: 공개만 하면 끝인가요? 그 이후에 해야 할 일_ 에서 나열된 일에도 관심을 가질 것을 추천한다. 사실 오픈소스를 가장 잘 설명할 수 있는 사람은 개발한 사람이기 때문이다. 하지만 메인테이너에게 너무 많은 짐이라고 생각할 수도 있다. 이럴 때를 위해서! 커뮤니티를 잘 형성해야 한다. 그들이 메인테이너를 대신하여 오픈소스 프로젝트를 바깥에 더 널리 알리는 역할을 할 것이다. 

앞으로 성공적으로 커뮤니티를 형성한 개발자의 경험을 통해 이 가이드의 업데이트에도 도움을 받는 날이 오기를 기원한다. 