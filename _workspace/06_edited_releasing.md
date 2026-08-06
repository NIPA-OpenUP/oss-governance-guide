---
title: "오픈소스SW 공개하기"
linkTitle: "3. 공개하기"
weight: 40
description: >
   
---

{{% alert color="success" %}}

이 책에서는 기업이 오픈소스SW를 공개하는 과정에서 일반적으로 발생하는 일을 다룬다. 특정 기업의 예외 사항까지 모두 다루지는 않는다.

{{% /alert %}}


이번 장에서는 두 가지 입장에 따라 오픈소스SW 공개 과정을 서술한다.

1. 오픈소스SW 공개 가이드 - 기업 편:  
   OSPO을 운영하는 입장을 위한 가이드이다. 기업 구성원으로부터 오픈소스SW 공개 요청이 있을 때, 혹은 기업의 사업 차원에서 오픈소스SW 공개를 진행할 때 고려해야 할 내용을 다룬다.
2. 오픈소스SW 공개 가이드 - 개발자 편:  
   기업에 속한 개발자 입장을 위한 가이드이다. 회사 업무 목적으로 오픈소스SW를 공개하는 경우 신경 쓰면 좋을 내용을 다룬다.

## 오픈소스SW 공개, 왜?

오픈소스SW 공개와 운영에는 여러 사람의 의지가 필요하다. 물론 한 사람의 강력한 의지만으로 성공하는 경우도 있다. 다만 이 가이드에서는 기업의 오픈소스SW 공개를 다루므로 좀 더 일반적인 상황을 가정한다. 오픈소스SW 공개 의지가 있는 몇몇 사람이 먼저 모이고, 의지가 없던 다른 구성원의 동의를 얻은 뒤에야 공개 절차가 본격적으로 시작된다. 어떤 과정을 거쳐 새로운 오픈소스SW를 공개하는지 설명하기 전에, 다른 사람을 설득할 때 도움이 되는 '오픈소스SW를 공개해서 얻을 수 있는 이점'을 먼저 정리한다.

### 기업에서 얻는 이점

기업 입장에서는 힘들여 만든 소스 코드를 공개하는 이유에 의문을 가지기 쉽다. 당장 손해로만 보일 수 있기 때문이다. 그러나 기업이 얻는 이점도 분명히 있다.

#### 1. 기술 브랜드 인지도 향상

개발자를 채용하는 기업은 대부분 채용이 어렵다고 말한다. 원하는 인재를 찾기도 어렵고, 그 인재가 자사를 마음에 들어 하게 만들기는 더 어렵기 때문이다. 좋은 개발자를 채용하려고 기업은 여러 방법을 시도한다. 자사의 개발 문화를 알리기 위해 소책자를 만들기도 하고, 광고나 동영상을 제작하거나 채용 설명회에서 발표하기도 한다. 이런 여러 방법 중에서 오픈소스SW 공개 소식은 특히 매력적인 소재가 된다. 예를 들어 안드로이드 애플리케이션 개발에 쓰는 라이브러리를 오픈소스SW로 공개하면, 구직 중인 안드로이드 개발자에게 다음과 같은 내용을 함축적으로 전달할 수 있다.

- 기업에서 안드로이드 개발을 할 때 어떤 부분에 신경 쓰는지
- 기업에서 이미 근무 중인 안드로이드 개발자들이 어떻게 개발하고 있는지
- 기업에서 이미 근무 중인 안드로이드 개발자들이 얼마나 열정적인지

백문이 불여일견이다. 설명으로 전달할 수도 있지만, 오픈소스SW로 직접 보여주면 전달력이 다르다.

#### 2. 직원 리텐션 효과

오픈소스SW를 공개하고 나면 성취감을 얻는다. 평소 서비스나 제품을 개발했을 때 느끼는 성취감과는 확연히 다르다. 유능한 직원을 회사에 머물게 하려면 여러 노력이 필요한데, 업무 만족도를 높여 자긍심을 갖게 하는 일도 오픈소스SW 공개로 할 수 있다.

#### 3. 직원들 기술 역량 향상

직원이 알아서 성장하면 좋겠지만 쉬운 일이 아니다. 새로운 기술은 계속 나오는데 조직 분위기가 침체되어 있으면 좋은 결과물을 내기 어렵다. 사내 교육 프로그램을 잘 구성하는 것도 중요하지만, 오픈소스SW를 공개하고 운영하는 과정에서 배우는 기술은 교육만으로는 얻기 어렵다. 구체적으로 어떤 기술을 배우는지는 뒤에 나오는 '개발자로서 얻는 이점'에서 다룬다.

#### 4. 오픈소스SW 커뮤니티로부터 받는 지지 (오픈소스SW 생태계 선순환)

이 이점은 당장 체감하기는 어렵다. 그러나 먼 미래에 결정적인 도움을 받는다면 대개 이런 경우다. 설명을 위해 같은 오픈소스SW를 사용하는 두 기업을 가정한다.

- 기업 A: 오픈소스SW를 단순히 사용한다. 사용하는 오픈소스SW가 요구하는 라이선스 의무는 꼼꼼히 지킨다. 이 오픈소스SW로 개발한 프로그램으로 수익을 낸다.
- 기업 B: 기업 A처럼 오픈소스SW에 많이 의지하지만, 필요한 플러그인을 직접 개발해 오픈소스SW로 공개했다. 많지는 않아도 몇몇 외부 사람이 이 오픈소스SW의 목적과 주요 기능을 알고 있다.

두 기업이 각각 이 오픈소스SW를 사용하다가 문제를 만나 커뮤니티에 해결 방안을 문의하는 상황을 생각해보자. 커뮤니티는 그동안 관계를 쌓아 온 기업 B의 질문에 더 우호적으로 반응할 가능성이 크다. 단순히 답을 얻는 데서 그치지 않고 직접적인 해결책을 제시받을 수도 있다. 정리하면 오픈소스SW에서 도움을 받은 기업이 새로운 오픈소스SW를 만들어 돌려주고, 다시 서로 돕는 단계로 이어진 것이다. 이것이 선순환의 한 예다.

#### 5. 커뮤니티 리소스 유입

이 장점은 앞서 언급한 다른 장점을 모두 제치고 가장 강력한 설득 포인트가 된다. 이 장점을 이해하려면 먼저 오픈소스SW가 잘 운영되는 방식을 살펴본다.

오픈소스SW가 공개되어 성공적으로 궤도에 오르면 다음과 같은 순환이 만들어진다. 채택할 만큼 매력이 있으면 사용자가 늘어나고, 그 사용자들이 문제를 만날 때마다 버그를 제보하거나 새 기능을 제안한다. 나아가 사용자가 기여자가 되어 개발에 직접 참여하면 프로젝트의 성장은 더 가속화된다.

{{< imgproc community-resource Fit "768x768" >}}
<center>[오픈소스SW 운영]</center>
{{< /imgproc >}}


오픈소스SW로 공개하지 않은 내부 프로그램과 비교하면 다음과 같이 요약할 수 있다.
- 훨씬 더 많은 사람에게서 받는 피드백과 아이디어
- 훨씬 더 다양한 환경에서 사용되어 얻는 안정성(미처 발견하지 못한 오류를 찾을 가능성이 커짐)
- 훨씬 더 많은 사람의 자발적 참여로 기업이 투입해야 하는 리소스가 줄어듦

#### 6. 제품의 셀링 포인트<sub>Selling Point</sub>로 작용

기업은 이윤을 추구하는 조직이다. 어떤 행동이든 이윤으로 이어질 때 결정을 내린다. 제품의 고객층이 개발자라면 오픈소스SW 공개가 제품 판매에 도움이 된다. 예를 들어 제품의 SDK<sub>Software Development Kit</sub>를 제공하는 상황을 가정해보자. SDK를 배포하는 이유는 다른 개인이나 기업이 SDK를 잘 사용하게 해서 제품의 활용도와 의존도를 높이기 위해서다. SDK를 배포할 때는 사용 가이드와 함께 샘플 코드를 제공하는 경우가 많다. 그런데도 사용자는 문제 상황을 만나 질문을 남기거나 버그를 제보하고, SDK와 샘플 코드를 내려받기 전에는 사용 규칙 동의서에 서명한다. 이 모든 상황은 오픈소스SW 개발과 크게 다르지 않다. 오히려 사용자에게 친숙한 환경에서 소스 코드를 공개하고 질문을 받고 공지 사항을 게시하는 쪽이 이해에 더 도움이 된다. 결과적으로 개발자가 사용자인 제품이라면, 오픈소스SW 환경에서 사용자와 소통해 사용자 친화적인 제품을 만들고 커뮤니티를 형성하며 제품 판매에도 도움을 받을 수 있다.

---

이 모든 장점은 단기간에 체감하기 어렵다는 점도 덧붙인다. 처음 몇 년은 사막에서 오아시스를 찾는 것처럼 성과가 보이지 않을 수 있다. 그러나 시간이 지나면 사람들이 끊임없이 찾는 사막의 호수가 될 수 있다.

### 개발자로서 얻는 이점

학생 시절 과제를 예로 들어보자. 혼자 하는 과제와 조별 과제 중 하나를 고른다면 대다수는 조별 과제에서 크게 고생한 기억을 떠올릴 것이다. 그만큼 다른 사람과 무언가를 함께 한다는 것은 쉬운 일이 아니다. 그런데 오픈소스SW는 다른 사람, 심지어 만난 적도 만날 일도 없을 사람과 함께할 때 비로소 그 장점이 드러난다. 이를 위해서는 다양한 노력이 필요하다. 이런 노력을 통해 어떤 실력이 향상되는지 정리한다.

#### 1. 가독성 높은 코드의 작성 실력

혼자만 알아볼 수 있는 코드를 작성했는데 다른 사람이 사용하다가 예상과 다르게 동작한다고 가정해보자. 사용자는 어느 부분이 문제인지 스스로 찾지 못하고 질문만 남기거나 다른 제품으로 대체해 버릴 수 있다. 반대로 읽기 쉬운 코드를 작성했다면, 문제를 겪은 사람이 직접 원인을 찾아 해결하는 Pull Request를 보내기도 한다. 따라서 미래의 자신에게 돌아올 부담을 줄이려면 다른 사람이 쉽게 이해할 수 있는 코드를 작성해야 한다.

#### 2. 문서 작성 실력

코드 작성 이외에도 오픈소스SW의 동작 방식을 설명하는 문서와 주석을 적절히 갖춰야 한다. 너무 길고 상세하게만 쓴 글은 가독성이 떨어지고, 반대로 너무 짧게 쓴 글은 이해도를 낮춘다. 이 과정에서 의도를 적절한 순서로 설명하는 글쓰기 연습을 하게 된다. 사용자가 궁금해하는 내용을 문서에서 찾지 못하면 질문을 남기고, 그 질문을 통해 문서의 부족한 부분을 보완할 수 있다.

#### 3. 커뮤니케이션 실력

오픈소스SW 개발에서는 코딩보다 커뮤니케이션에 더 많은 시간을 쓰기도 한다. 소통하는 사람들이 서로 다른 지식과 언어, 시간대를 갖고 있기 때문이다. 그래서 하나의 문제를 해결하려면 효율적으로 설명하고 질문하는 연습이 필요하다. 기술적인 커뮤니케이션 능력뿐 아니라 다른 사람의 입장을 이해하고 자만하거나 소극적이지 않은 태도도 효율적인 커뮤니케이션에 필수적이다. 오픈소스SW를 공개하고 운영하는 과정에서 이런 다양한 커뮤니케이션 능력을 익힐 수 있다.

#### 4. 오픈소스SW의 동작 원리 이해

오픈소스SW를 잘 사용하는 방법을 누군가 친절하게 알려주면 좋겠지만, 대부분은 스스로 검색하고 찾아보며 익혀야 한다. 어떤 오픈소스SW의 사용법을 익혀 잘 쓰다가 문제에 부딪혔다고 가정해보자. 동작 방식을 모르면 어디에 질문하고 어떻게 답을 얻어야 할지 알기 어렵다. 오픈소스SW의 동작 원리를 이해하고 있으면 이런 상황에서 유리하다.

#### 5. 포트폴리오

최근 경력 개발자 채용 공고에서는 특정 대형 오픈소스SW 사용 경험이나 오픈소스SW 활동 경험을 우대 사항으로 명시하는 경우를 흔히 볼 수 있다. 기업이 이미 쓰고 있는 오픈소스SW와 관련된 활동을 한 사람은 이직 후에도 바로 실무에 투입될 수 있다고 기대하기 때문이다. 또한 면접관이 이력서를 볼 때 이전 직장 경력은 지원자의 설명에만 의존해 이해해야 하지만, 오픈소스SW 활동 경력은 직접 확인해 직관적으로 이해할 수 있다는 이유도 있다. 오픈소스SW를 직접 공개하고 운영한 경험은 앞서 나열한 여러 실력을 쌓아왔다는 증거가 되어 더 설득력 있는 이력서로 이어진다.



## 오픈소스SW 공개 가이드 - 기업 편

지금까지 '왜?'라는 물음에 답했다. 이제 누가, 언제, 어디서, 무엇을, 어떻게라는 다섯 개의 물음이 남았다. 앞으로는 이 다섯 물음에 답하며 오픈소스SW 공개의 여정을 살펴본다.

{{< imgproc release-journey-2026 Fit "768x768" >}}
<center><i>[오픈소스SW 공개 여정 — 단계별 담당 주체와 산출물]</i></center>
{{< /imgproc >}}

### 공개 규칙 마련하기

#### 누가?(1) — 누가 검토할 것인가? 유관부서들에 오픈소스SW 공개에 관해 설명하기

오픈소스SW와 관련이 있을 부서를 상세히 나열하면 특허팀, 상표팀, 보안팀, 오픈소스SW 검수팀(컴플라이언스), 인사팀, 홍보팀·마케팅팀, 법무팀 등 7개 부서로 꼽을 수 있다. 조직 사정에 따라 미리 만나야 할 팀이 더 많거나 적을 수 있다. 요점은 오픈소스SW 공개 계획을 처음 알릴 때 유관부서가 자신과 상관없는 일이라고 여겨 관심을 잃기 전에, 각 부서가 주로 어떤 점을 검토해야 하는지 미리 설명하는 데 있다.

{{< imgproc release-review-matrix-2026 Fit "768x768" >}}
<center><i>[유관부서 검토 매트릭스 — 병렬 검토와 선행 의존]</i></center>
{{< /imgproc >}}

##### 1. 특허팀: 공개하려는 프로그램에 자사의 특허가 포함되어있지는 않은지 확인한다.
특허가 포함되어 있다면 특허에 우선권을 줄지, 오픈소스SW 공개로 얻는 혜택을 택할지 고민해야 한다. 방어 목적의 특허라면 대개 사업 이익과는 거리가 멀므로, 오픈소스SW 공개로 얻는 혜택을 잘 설명할 필요가 있다.
공개하려는 프로그램에 특허로 출원할 부분이 없는지도 함께 검토하는 것이 좋다. 오픈소스SW에 특허가 포함된 경우에는 특허권을 보호하는 오픈소스SW 라이선스를 선택해야 한다. 라이선스 선택에 관한 자세한 내용은 오픈소스SW 공개 가이드 - 기업 편 [어떻게? — 어떤 조건으로 공개할 것인가? 공개에 적합한 라이선스 후보군 정하기](#어떻게--어떤-조건으로-공개할-것인가-공개에-적합한-라이선스-후보군-정하기)에서 다룬다.

##### 2. 상표팀: 공개하려는 프로그램의 명칭이 타사의 상표권을 침해하지 않는지 확인한다.
부르기 쉽고 의미도 알기 쉬운 이름은 오픈소스SW가 널리 알려지는 데 중요한 역할을 한다. 그러나 이미 출시된 상표는 이 세상에 아주 많다. 게다가 오픈소스SW를 어느 국가의 사람들이 사용하게 될지 특정할 수 없으므로 광범위한 조사가 필요하다. 공개한 오픈소스SW의 명칭이 다른 상표권을 침해했을 때 발생하는 비용과, 상표권 출원에 드는 비용 중 어느 쪽을 선택할지 고민해야 한다. 어떤 명칭이 타사 상표와 동일한 경우를 긍정적으로 본다면, 기존 상표의 브랜드에 '오점'이 될 만한 나쁜 일을 한 것은 아니며 오히려 사회에 오픈소스SW를 기부했다는 긍정적 이미지로 해석되기도 한다. 반대로 부정적으로 본다면 상표 침해로 인한 피해 보상과 기업 이미지 타격까지 고려해야 한다. 따라서 공개할 오픈소스SW의 운영 기간과 전파 범위에 따라 상표 출원까지 할지, 아니면 상표 조사만으로 현시점에 침해 리스크가 없는 명칭을 고르는 데 그칠지 현실적으로 판단해야 한다.
명칭의 모든 후보를 다 검토하기에는 많은 시간이 걸리므로, 후보 상표가 이미 출원되었는지 직접 검색해 보는 것도 좋은 방법이다. 한국의 경우에는 [KIPRIS 상표 검색](https://www.kipris.or.kr/khome/search/searchResult.do?tab=trademark)[^kipris]을 이용할 수 있다.

[^kipris]: KIPRIS 상표 검색 : https://www.kipris.or.kr/khome/search/searchResult.do?tab=trademark

##### 3. 보안팀: 공개하려는 프로그램에 기업의 기밀 정보가 포함되어있지는 않은지, 그리고 보안 취약점이 없는지 확인한다.
소스 코드가 직접 공개되므로 민감한 IP 주소, 내부 시스템 관련 정보, 직원 개인정보 같은 특정 키워드가 포함되어 있지 않은지 확인해야 한다. 또한 공개하려는 프로그램이 널리 쓰이려면 안정성을 보장해야 하므로 보안 취약점이 없는지도 확인해야 한다.

##### 4. 오픈소스SW 검수팀: 공개하려는 프로그램에 어떤 오픈소스SW가 포함되었는지 확인한다.
공개할 소스 코드에 포함된 오픈소스SW 라이선스 준수 여부를 확인하려면 평소와는 다른 접근이 필요하다. 기존에 기업이 하던 배포 형식과 다르기 때문이다. 응용 프로그램이 아니라 소스 코드 자체를 배포하는 경우를 확인해야 한다. 따라서 소스 코드 형태로 재배포되는 오픈소스SW가 있는지, 의존성은 어떻게 배포되는지 확인한다. 또 공개할 오픈소스SW를 npm, pip, Maven Central 등으로 패키지 배포하는 경우에는 무엇이 패키지 배포에 포함되는지 확인한다. 마지막으로 새 오픈소스SW에 적용할 라이선스와, 소스 코드에 포함된 다른 오픈소스SW의 라이선스가 서로 상충하지 않는지도 확인한다. 이런 다양한 배포 형태를 고려해 고지문을 작성한다.

##### 5. 인사팀: 직원이 입사할 때 작성한 근로계약서, 비밀유지서약서 등에서 오픈소스SW 공개는 예외로 간주됨을 인지한다.
모든 직원은 입사할 때 근로계약서를 작성한다. 소프트웨어 개발 직군은 대개 '업무 중에 작성한 소스 코드는 기업의 자산이다', '기업에서 작성한 소스 코드는 정해진 곳에만 게시한다'는 내용의 동의서도 함께 작성한다. 오픈소스SW로 공개하는 일을, 업무 중 작성한 기업 자산을 외부 서버에 올리는 행위로 오해할 수 있다. 그러나 실제로는 기업 이름으로, 기업이 정한 장소에 소스 코드를 올리는 것이므로 이 점을 명확히 설명해야 한다.
오픈소스SW를 공개하고 운영하는 데는 적지 않은 시간과 노력이 든다. 이 과정이 다른 직원에게 '업무가 아닌 일'로 비치지 않도록 균형을 맞춰야 한다. 예를 들어 기업이 공개한 오픈소스SW를 외부인이 사용하다가 문제를 겪고 질문을 남겼다고 하자. 메인테이너가 반드시 답할 의무는 없지만, 사용자를 잘 유지하는 것도 오픈소스SW 운영에서 필수적인 일이므로 대부분 답변에 시간을 쓴다. 이 또한 기업 자산을 더 높은 품질로 발전시키는 업무의 일부라는 공감대를 형성해야 한다. 이 공감대가 형성되지 않으면 누구도 개인 시간을 들여 기업의 오픈소스SW를 개발하려 하지 않으므로 세심한 주의가 필요하다.

##### 6. 홍보팀&마케팅팀: 공개한 오픈소스SW가 세상에 널리 알려지도록 노력한다.
오픈소스SW를 공개했다고 가정해보자. 사람들이 저절로 모여 이 오픈소스SW를 구경하고 사용하고 발전시켜 주지는 않는다. 새로운 오픈소스SW가 탄생했다는 사실을 꾸준히 알려야 한다. 소셜 미디어, 동영상, 기사, 블로그 등 다양한 매체로 오픈소스SW의 기능을 설명해야 사용자에게 인식되며, 이런 작업이 앞으로도 꾸준히 필요하다는 점을 홍보팀이 인지해야 한다.
오픈소스SW 자체를 홍보하는 것에 더해, 기업이 오픈소스SW 활동을 적극적으로 지원한다는 이미지를 알리는 매체 인터뷰에 응하면 기업 브랜딩에도 좋은 수단이 된다.

##### 7. 법무팀: 법적인 부분을 검토하고 오픈소스SW를 접하는 사람들이 안전한 환경에 있도록 보장한다.
소스 코드를 공개해 사람들이 널리 활용하고 여러 사람이 개발에 함께 참여하는 과정에는, 일상에서 쉽게 이해하기 어려운 규칙이 따른다. 법무팀은 대표적으로 다음 두 가지 상황에서 어떤 리스크가 있는지 법적으로 검토해야 한다.
- 소스 코드를 공개하는 시각: 소스 코드를 공개하는 과정에는 여러 리스크가 따른다. 예를 들어 오픈소스SW에 자사 특허가 포함된 경우 특허 침해로 손해를 입지 않아야 한다. 또한 오픈소스SW에 심각한 결함이 있어 사용자가 피해를 본 경우, 공개한 쪽이 배상하느라 손해를 보는 일도 없어야 한다. 이런 내용은 라이선스에 명시되어 있으며, 법적으로 기업에 피해가 가지 않도록 보장해야 한다. 라이선스 선택에 관한 자세한 내용은 오픈소스SW 공개 가이드 - 기업 편 [어떻게? — 어떤 조건으로 공개할 것인가? 공개에 적합한 라이선스 후보군 정하기](#어떻게--어떤-조건으로-공개할-것인가-공개에-적합한-라이선스-후보군-정하기)에서 다룬다.
- 오픈소스SW에 기여를 받는 시각: 기업이 공개한 오픈소스SW에 외부에서 기여를 받는 상황을 가정해보자. 기여자가 작성한 코드에만 다른 공개 규칙(라이선스)이 적용되면, 이후 오픈소스SW를 사용하는 사람들이 혼란에 빠질 수 있다. 더 심각하게는 기여자가 이전에 제공한 내용을 되돌려 받고 싶다고 요구할 수도 있다. 이렇게 오픈소스SW에 기여를 받을 때(또는 기여할 때) 지켜야 할 규칙은 기여자 라이선스 동의서(Contributor License Agreement, 이하 CLA)에서 명시한다. 개인 기여에는 ICLA(Individual CLA), 기업이나 단체를 대표한 기여에는 CCLA(Company CLA)를 각각 적용한다. 규모가 큰 오픈소스SW 재단이 작성한 라이선스를 적용하는 경우에는 이에 상응하는 CLA가 있는 경우가 많다. 따라서 법무팀은 이 CLA의 내용을 검토하고 리스크가 없는지 확인해야 한다.

대표적인 CLA 양식은 다음을 참고한다.
- [Apache Software Foundation Contributor License Agreement](https://www.apache.org/licenses/contributor-agreements.html)[^apache-cla]
- [Cloud Native Computing Foundation Contributor License Agreement](https://github.com/kubernetes/community/blob/master/CLA.md)[^k8s-cla]
- [Python Software Foundation Contributor Agreement](https://www.python.org/psf/contrib/)[^python-cla]

[^apache-cla]: Apache Software Foundation Contributor License Agreement : https://www.apache.org/licenses/contributor-agreements.html
[^k8s-cla]: Cloud Native Computing Foundation Contributor License Agreement : https://github.com/kubernetes/community/blob/master/CLA.md
[^python-cla]: Python Software Foundation Contributor Agreement : https://www.python.org/psf/contrib/

기여 규칙으로는 CLA와 DCO(Developer Certificate of Origin, 이하 DCO) 두 방식이 병존한다. 따라서 공개하려는 프로젝트의 특성에 따라 어떤 기여 규칙을 적용할지 판단한다.

두 방식의 개념과 차이, 서명 부담, 기업이 검토해야 할 항목은 [오픈소스SW 기여 가이드 - 기업 편: 4. CLA / DCO에 주의하라](/contributing/#4-cla--dco에-주의하라) 를 참고한다.

#### 누가?(2) — 누가 공개하고 운영할 것인가? 멤버 역할과 권한 설정 규칙 정하기

오픈소스SW가 잘 운영되려면 특정 역할을 맡은 사람이 있어야 한다. 메인테이너가 한 명뿐인 오픈소스SW에서 그 한 명이 퇴사하면, 커뮤니티가 이미 강력하게 형성되어 있지 않은 한 그 오픈소스SW는 점차 잊힌다. 반대로 너무 많은 사람에게 소유자 권한을 주면 누군가 실수로 설정을 바꾸는 사고가 날 수 있다. 따라서 프로젝트 규모에 따라 최소 몇 명의 멤버가 어떤 권한을 가질지 사전에 정해야 한다. GitHub을 기준으로 역할별 권한을 다음 표로 정리한다.

|역할|권한|
|---|---|
|Read|저장소에 접근하고 clone 하기<br>issue 생성하고 의견남기기<br>pull request를 생성하고 의견남기기<br>`@` 기호로 언급할 수 있는 후보에 등록|
|Triage|Read 역할의 권한 전부<br>issue 관리하기|
|Write|Triage 역할의 권한 전부<br>저장소에 push하기<br>pull request 관리하기|
|Maintain|Write 역할의 권한 전부<br>저장소 설정 중 일부에 접근하기|
|Admin|Maintain 역할의 권한 전부<br>멤버 관리를 포함한 저장소 설정의 전부에 접근하기|

{{< imgproc contributor-ladder-2026 Fit "768x768" >}}
<center><i>[기여자 사다리 — 승격 기준과 권한 회수 경로]</i></center>
{{< /imgproc >}}

#### 언제? — 언제 공개할 것인가? 공개 시점 정하기

오픈소스SW를 공개할 때 완성도가 너무 떨어진 소스 코드를 내놓으면 안 된다는 것은 널리 알려져 있다. 그렇다고 지나치게 완벽한 상태(소프트웨어 개발에 완벽이란 사실상 없지만)로 공개하는 것도 좋은 전략은 아니다. 공개 이후 코드 변경, 문서 작성, 이슈 관리를 포함해 꾸준히 활동하지 않으면 관리되지 않고 정체된 인상을 주기 때문이다. 따라서 적당한 시점에 오픈소스SW로 내놓고 이후에 발전시키는 접근이 필요하다. 어느 정도가 완성인지 정량적으로 표현하기는 어려우므로, 공개할 때마다 이 점을 염두에 두고 시점을 정한다. 예를 들어 홍보 시점은 자사 개발자 콘퍼런스처럼 주목도가 높은 시점으로 잡을 수 있다.

#### 어디서? — 어디에 공개할 것인가? 공개 위치 선정하기

기업이 처음 오픈소스SW를 공개하는 경우라면 GitHub나 GitLab 등 인기 있는 저장소 플랫폼에 기업 이름으로 조직(Organization)을 만들 수 있는지 먼저 확인해야 한다. 먼저 선점하는 쪽이 이름을 갖게 되므로, 여러 절차 중에서도 가장 먼저 처리해 두는 것이 좋다.
라이브러리를 오픈소스SW로 공개할 때는 사람들이 손쉽게 사용할 수 있도록 패키지 저장소에도 배포해야 한다. 잘 알려진 패키지 저장소로는 프로젝트 성격에 따라 Maven Central, npm, PyPI 등이 있으며, 소스 코드 저장소와 마찬가지로 Organization 단위로 동작하는 경우가 많으므로 권한을 미리 확보해 둔다.
소스를 공개할 때는 소개 홈페이지, 기술 블로그 등을 함께 공개하고, 그 링크를 소스 저장소에서 확인할 수 있도록 하는 것이 좋다.

#### 어떻게? — 어떤 조건으로 공개할 것인가? 공개에 적합한 라이선스 후보군 정하기

오픈소스SW에 적용할 라이선스를 고르려면 다양한 상황과 우선순위를 고려해야 한다.

{{< imgproc license-decision-tree-2026 Fit "768x768" >}}
<center><i>[공개 라이선스 결정 트리]</i></center>
{{< /imgproc >}}

##### 공개할 오픈소스SW가 제품에 포함되고, 제3자에게 이 제품이 배포되는 경우
- 이 오픈소스SW에 Copyleft license를 적용해도 저작권자와 사용자(라이선스 의무를 지켜야 할 사람)가 동일하므로 법적 이슈가 생길 가능성은 없다. 다만 커뮤니티에서는 제품의 소스 코드까지 공개하기를 기대할 수 있다.
- 이 오픈소스SW에 Permissive license를 적용한다면 제품에 포함될 법적 고지문에 라이선스와 저작권 표기를 추가하면 된다. 다만 제품에 포함된 다른 오픈소스SW와의 호환성도 함께 검토하는 것이 좋다.
##### 공개할 오픈소스SW가 널리 사용되는 것이 최우선의 목표일 경우
- 사용자의 진입 장벽을 낮추려면 Permissive license를 적용하는 것이 유리하다.
- 공개 이후 유지보수 계획이 없다면 Public domain, CC0, Unlicense 등 저작권을 포기하는 방식도 고려할 만하다. (발표나 데모에서 쓰는 code snippet 등)
##### 공개할 오픈소스SW의 변경 사항을 추적하는 것이 중요할 경우
- 오픈소스SW 버전과 상용 버전으로 나누어 사업을 한다면 오픈소스SW의 변경 사항을 추적하는 것이 중요하다. 아무 제한을 두지 않으면 수익에 지장을 줄 수 있기 때문이다. 이런 경우에는 Copyleft license를 적용하는 편이 유리하다. 변경 사항 추적 외에 특허권까지 폭넓게 보호할 수 있는 라이선스를 선택해야 한다.

#### 우리는 CRA상 무엇인가 — 제조사·스튜어드·무의무 판정

EU 사이버복원력법<sub>Cyber Resilience Act</sub>(규정 (EU) 2024/2847, 이하 CRA)은 오픈소스SW를 공개하는 주체를 제조사<sub>manufacturer</sub>와 오픈소스SW 스튜어드<sub>open-source software steward</sub>로 나누고, 어느 쪽에도 해당하지 않는 경우를 따로 둔다[^cra-reg]. 지위에 따라 부과되는 의무와 제재가 다르므로, 공개를 결정하는 단계에서 프로젝트마다 지위를 판정한다. 다음 표를 판정 기준으로 사용한다.

| 지위 | 해당하는 배포 형태 | 부과되는 의무 | 과징금 적용 여부 | 적용 시점 |
|------|-------------------|--------------|-----------------|----------|
| **제조사** | 오픈소스SW를 포함한 디지털 요소 제품을 EU 시장에 상업적으로 공급한다 | 제품 전체에 대한 CRA 준수 책임을 진다. 제품에 통합한 FOSS 구성요소 자체의 CRA 준수 책임은 지지 않으나, 제13조(5) 실사 의무와 제13조(6) 상류 프로젝트 보고·수정 공유 의무는 진다(지침 86~88항) | 적용된다. 다만 제64조(10)(a)는 마이크로·소기업 제조사가 제14조(2)(a)·제14조(4)(a)의 신고 기한을 지키지 못한 경우에 한해 과징금을 면제하고, 같은 항 (b)는 스튜어드의 규정 위반 전반을 면제한다 | 제14조 신고 의무 2026-09-11, 전면 적용 2027-12-11(제71조) |
| **오픈소스SW 스튜어드** | 제조사가 아닌 법인으로서, 상업적 활동에 쓰이는 특정 FOSS 제품의 개발을 지속적·체계적으로 지원하고 그 제품의 존속을 보장한다(제3조(14)) | 제24조의 세 가지 의무를 진다. ① 안전한 개발과 취약점 처리를 촉진하는 사이버보안 정책을 '검증 가능한 방식으로' 수립·문서화, ② 시장감시당국의 합리적 요청 시 문서 제공·협조, ③ 개발에 관여한 범위에서 제14조(1) 악용 취약점 신고와, 제공하는 인프라가 영향받는 경우 제14조(3)·(8) 중대 사고 신고 | 원칙적으로 적용되지 않는다. 제64조(10)은 제3항부터 제9항까지의 과징금에 대한 특례로서 (b)에서 '오픈소스SW 스튜어드의 이 규정 위반'을 제외 대상으로 명시한다. 다만 제2항의 과징금(부속서 I 필수요건 및 제13조·제14조 의무 위반)은 특례 열거에 포함되어 있지 않으므로, 제24조(3)을 통해 지는 제14조 신고 의무의 위반까지 완전히 면제되는지는 특례 문언상 단정할 수 없다 | 제24조 전면 적용 2027-12-11(제24조(3)을 매개로 하는 제14조(1)·(3)·(8) 신고 의무 포함). 제71조(2)의 적용 개시 예외는 제14조(2026-09-11)와 제4장 제35~51조(2026-06-11)뿐이며 제24조는 예외에 포함되지 않는다 |
| **어느 쪽도 아님** | 상업적 활동과 무관하게 공개하며, 특정 제품의 개발을 지속적으로 지원하지도 않는다 | CRA상 의무가 발생하지 않는다. 다만 같은 코드가 제3자의 제품에 통합되면 그 제품의 제조사 의무는 별도로 발생한다 | 적용되지 않는다 | 해당 없음 |

2026-09-11부터 신고 의무가 발생하는 것은 제조사이며, 스튜어드의 신고 의무는 제24조(3)을 근거로 하므로 2027-12-11부터 적용된다. 다만 지침 80항이 밝히듯 스튜어드는 그 전에도 인지한 악용 취약점 정보를 사이버보안 정책에 따라 메인테이너와 공유하는 것이 바람직하다. 제조사와 스튜어드 모두 2027-12-11이 전면 적용일이며, 그 이전에 앞당겨 적용되는 것은 제14조(2026-09-11)와 제4장 제35~51조(2026-06-11)뿐이다[^cra-reg]. CRA 적용 일정 전체와 제조사 관점의 대응 절차는 [오픈소스SW 사용하기](/using/)에서 다룬다.

집행위는 2026-07-27 CRA 적용 지침을 채택하면서 판정 규칙 두 가지를 확정했다[^cra-guidance-news][^cra-guidance]. 판정에서 다투기 쉬운 지점이므로 표와 함께 적용한다.

- CRA의 FOSS 정의(제3조(48))는 '자유·오픈소스SW 라이선스로 배포될 것'과 '소스코드가 공개적으로 공유될 것'을 모두 충족할 것을 요구한다. 따라서 유료 고객에게만 소스코드를 제공하는 소프트웨어는 CRA상 FOSS가 아니다(지침 44~46항).
- 상업적 활동 여부는 개발 경위나 자금 조달 방식이 아니라 수익화 여부로 판정한다. 가격 청구, 실비를 초과하는 기술지원 유료화, 플랫폼을 통한 부수 서비스 수익화, 보안·호환성 개선 외의 목적으로 개인정보 처리를 요구하는 행위, 개발·제공 비용을 초과하는 기부 수령이 여기에 해당한다(지침 41~42항).

같은 법인이 프로젝트마다 다른 지위를 가질 수 있다. 커뮤니티 에디션과 엔터프라이즈 에디션을 함께 운영하는 구조에서는 한 프로젝트에 스튜어드, 다른 제품에 제조사가 되는 경우를 지침 72~74항이 명시한다. 따라서 판정은 법인 단위가 아니라 프로젝트 단위로 한다.

판정 결과는 근거와 함께 문서로 남기고 감사 대응용으로 보관한다. 스튜어드로 판정된 프로젝트에는 `SECURITY.md` 수준의 안내가 아니라 취약점 접수·처리·공개 절차와 담당자, 목표 처리 기간을 담은 사이버보안 정책 문서를 갖춘다.

[^cra-reg]: Regulation (EU) 2024/2847 (Cyber Resilience Act), 제71조 적용 일자(전면 적용 2027-12-11, 제14조 2026-09-11, 제4장 제35~51조 2026-06-11) : https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
[^cra-guidance-news]: Commission publishes new guidance to support timely Cyber Resilience Act implementation (2026-07-27) : https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
[^cra-guidance]: Commission guidance on the application of Regulation (EU) 2024/2847, C(2026) 5252 final ANNEX, 27.7.2026 : https://ec.europa.eu/newsroom/dae/redirection/document/131456

### 문서화하기

오픈소스SW 공개 기반을 다지는 마지막 단계는 명확한 문서 작성이다. 지금까지 고민한 왜, 누가, 언제, 어디서, 무엇을, 어떻게에 해당하는 내용을 이해하기 쉬운 문서로 정리한다. 이 문서를 읽는 대상은 주로 오픈소스SW 공개를 신청하는 개발자이므로 개발자의 관점에서 작성한다. 문서에는 다음 내용이 들어가면 좋다.

- [ ] 기업이 오픈소스SW를 공개하는 취지와 포부
- [ ] 신청서 작성부터 공개까지 걸리는 전체 예상 시간과 과정
- [ ] 오픈소스SW 공개 신청서 작성 방법
- [ ] 오픈소스SW를 공개하기 위해 필요한 검토의 종류와 순서
- [ ] 검토의 목적
- [ ] 각 검토에 걸리는 예상 시간
- [ ] 도움을 받을 수 있는 연락처
- [ ] 오픈소스SW를 공개하기 전에 개발자가 알아 두면 좋은 내용(미래의 사용자를 위한 문서 작성, 필요한 인프라 등)

#### 오픈소스SW 공개 신청서

신청서 양식은 검토 과정을 어떻게 정하느냐에 따라 달라지므로 이 가이드에서 고정된 양식을 제시하지 않는다. 오픈소스SW 공개 검토에 필요한 내용을 각 부서에 확인하고 신청서에 담는다. 예를 들어 상표 검토를 위해 오픈소스SW의 명칭, 명칭 후보, 명칭을 정한 이유를 제출하게 하거나, 보안 검토를 위해 소스 코드 저장소 위치 등을 물어볼 수 있다. 또는 신청서에 검토 항목을 나열하지 않고, 신청자가 각 항목의 검토를 직접 신청하도록 안내하는 방식도 있다. 신청서 내용은 기업과 부서 상황에 따라 편차가 크므로 이 가이드에서는 항목을 따로 나열하지 않는다.

다만 검토에 필요한 정보 이외에 신청서 항목으로 추가하면 도움이 될 내용을 정리한다.

- 공개 목적: 이 항목에는 흔히 교과서적인 내용을 적는 경우가 많다. 이 항목을 적으면서 오픈소스SW 생태계에 기여하겠다는 의지를 다지는 계기도 된다. 다만 특수한 목적으로 공개하는 경우도 있다. 예를 들어 발표용 데모 코드를 공개하거나, 더 이상 유지보수되지 않는 다른 오픈소스SW를 fork하는 등 다양한 이유가 있을 수 있다. 이런 경우에는 운영 방침이 달라질 수 있으므로 목적을 미리 확인한다.
- 유사 오픈소스SW와의 비교: 대개 코드를 작성하는 이유는 어떤 문제를 해결하기 위해서다. 그런데 그 문제를 겪은 사람이 그 개발자뿐이라는 보장은 없다. 세상 어딘가의 누군가가 같은 문제를 겪고 이미 오픈소스SW로 공개했을 수도 있다. 따라서 이미 공개된 다른 오픈소스SW와의 차별점을 명확히 하는 것이 좋다.
- 로드맵: [언제? — 언제 공개할 것인가? 공개 시점 정하기](#언제--언제-공개할-것인가-공개-시점-정하기)에서 언급했듯, 공개 이후에도 기능을 꾸준히 개선하는 등 지속적인 관리가 필요하다. 정체된 오픈소스SW로 사람들의 기억 속에서 잊히기 전에, 간단하게라도 계획을 세워 둔다.
- 기술 평가 의견: 오픈소스SW 담당자가 기술적인 부분까지 모두 확인하기는 어렵다. 이 오픈소스SW가 공개되었을 때 해당 분야에서 어떤 평가를 받을지는 그 분야 전문가에게 미리 들어보는 것이 좋다. 공개를 신청하는 개발자의 상위 리더에게 받은 평가 의견이 있으면 프로젝트를 이해하고 홍보하는 데 큰 도움이 된다.
- 리소스 운영 계획: 로드맵을 세우면 개발자도 자연히 깨닫는다. 소스 코드를 공개하는 데서 끝나지 않고 앞으로도 꾸준히 시간을 들여야 한다는 사실이다. 현실적으로 리소스 운영 계획은 다른 업무 상황에 크게 좌우되므로, 구체적인 계획을 세우기보다는 이 오픈소스SW에도 계속 시간을 할애해야 한다는 점을 인지시키는 데 목적을 둔다.


### 공개하기

누군가 신청서를 제출했다고 가정해보자. 먼저 신청서 양식이 빠짐없이, 항목의 목적에 맞게 작성되었는지 확인한다. 이후 절차에 따라 검토를 진행한다. 오픈소스SW 담당자는 검토가 순서와 일정대로 진행되는지, 예상하지 못한 변수는 없는지 확인하고 챙긴다.

#### 신청서 확인

신청서 양식의 각 항목에는 확인하려는 의도가 있다. 신청서에 그 의도와 다른 내용이 있거나 빠진 내용은 없는지 확인한다.

#### 검토

앞서 문서화한 검토 단계에 따라 진행한다. 오픈소스SW 담당자는 검토가 일정대로 진행되는지, 변수는 없는지 확인한다.

#### 공개 준비

검토를 모두 마쳤다면 원칙적으로는 공개 준비가 끝난 셈이다. 이제 소스 코드를 실제로 공개하기 위해 해야 할 일을 설명한다. GitHub과 GitLab을 기준으로 참고 링크를 덧붙인다.

##### 오픈소스SW 거버넌스 문서 추가

거버넌스는 오픈소스SW 커뮤니티를 형성하고 사람들이 문제없이 어울리기 위해 필요하다. 사용 규칙, 행동 강령, 기여 규칙, 취약점 신고 창구를 각각 정해진 이름의 파일에 둔다. 이 형식을 따라야 사람들이 규칙을 쉽게 찾아볼 수 있고, 자동 점검 도구도 문서의 존재를 인식할 수 있다. 각 문서에 대한 자세한 설명은 [오픈소스SW 기여 가이드 - 개발자 편: 오픈소스SW 프로젝트는 어떤 문서를 제공하는가?](/contributing/#오픈소스sw-프로젝트는-어떤-문서를-제공하는가) 를 참고한다.

공개 저장소에 두어야 할 문서 세트를 다음 표로 확정한다. 저장소 호스팅 서비스의 화면 구성은 바뀌므로 화면에 표시되는 항목 수가 아니라 이 표를 기준으로 점검한다.

{{< imgproc repo-file-set-2026 Fit "768x768" >}}
<center><i>[공개 저장소 문서 세트와 배치]</i></center>
{{< /imgproc >}}

| 문서 | 필수·권장 | 최소 항목 | 작성 주체 | 위치 |
|------|----------|----------|----------|------|
| `README.md` | 필수 | 프로젝트 이름과 한 문장 설명, 설치·사용 예시, 지원 창구, 라이선스 표기 | 개발자 | 루트 |
| `LICENSE` | 필수 | 적용 라이선스 전문. 파일명을 바꾸지 않는다 | 사무국 | 루트 |
| `NOTICE` | 조건부 필수 | 포함된 서드파티 오픈소스SW의 저작권 표기와 라이선스 고지. 고지 의무가 있는 구성요소가 하나라도 있으면 필수 | 사무국(검수팀) | 루트 |
| `CONTRIBUTING.md` | 필수 | 받고자 하는 기여의 종류, 개발 환경 설정, 제출 절차, 커밋·코딩 규칙, CLA/DCO 서명 방법 | 개발자 | 루트 또는 `.github/` |
| `CODE_OF_CONDUCT.md` | 필수 | 금지되는 언행, 신고 연락처, 위반 시 조치 절차 | 사무국 | 루트 또는 `.github/` |
| `SECURITY.md` | 필수 | ① 지원 버전 표, ② 신고 채널(저장소의 비공개 취약점 신고 기능 활성화), ③ 접수→분류→패치→공개까지의 목표 기간, ④ CVE 발급 경로(저장소 보안 권고 기능) | 사무국(보안팀)+개발자 | 루트 또는 `.github/` |
| `GOVERNANCE.md` | 권장 | 의사결정 방식, 역할 정의, 메인테이너 승격·회수 기준 | 사무국 | 루트 |
| `MAINTAINERS.md` | 권장 | 현재 메인테이너 명단과 담당 영역, 연락 방법 | 개발자 | 루트 |
| `SUPPORT.md` | 권장 | 질문 채널과 이슈 트래커의 용도 구분, 응답을 기대할 수 있는 범위 | 개발자 | 루트 또는 `.github/` |
| `CHANGELOG.md` | 권장 | 버전별 변경 사항, 호환성 깨짐 표시, 보안 수정 표시 | 개발자 | 루트 |
| `CODEOWNERS` | 권장 | 경로별 리뷰 책임자. 리뷰어 자동 지정에 사용한다 | 개발자 | `.github/` |

이 문서 세트 중 규제(CRA)상 의무의 이행 수단이 되는 것은 `SECURITY.md`다. [우리는 CRA상 무엇인가 — 제조사·스튜어드·무의무 판정](#우리는-cra상-무엇인가--제조사스튜어드무의무-판정)에서 스튜어드로 판정된 프로젝트라면, 이 파일이 취약점 접수 경로를 대외에 공표하는 실물이다. 신고 채널이 없으면 신고 의무 자체를 이행할 수 없다. `LICENSE`·`NOTICE`는 라이선스 의무의 이행 수단이며, 그 내용은 [오픈소스SW 사용하기: 오픈소스SW 고지 의무사항](/using/#오픈소스sw-고지-의무사항)에서 다룬다.

문서 세트가 모두 마련되었는지 확인하는 점검 도구는 다음과 같다.

- [OpenSSF Scorecard](https://scorecard.dev/)[^scorecard] — 보안 실천 항목을 자동 점수화한다. [GitHub Action](https://github.com/ossf/scorecard-action)[^scorecard-action]으로 릴리스마다 실행할 수 있다. 채택자가 우리 프로젝트를 평가할 때 쓰는 지표이기도 하므로 공개 전 자가 점검에 먼저 사용한다.
- [OpenSSF Allstar](https://github.com/ossf/allstar)[^allstar] — 조직 단위로 저장소 정책을 강제한다. 저장소가 늘어난 뒤에 도입한다.
- [REUSE](https://reuse.software/)[^reuse] — 파일별 라이선스·저작권 헤더와 `LICENSES/` 디렉터리 규격을 검증한다.
- [GitHub Insights > Community Standards](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)[^community-standards] — 저장소별 문서 충족 현황을 화면에서 확인한다.

[^scorecard]: OpenSSF Scorecard : https://scorecard.dev/
[^scorecard-action]: ossf/scorecard-action : https://github.com/ossf/scorecard-action
[^allstar]: OpenSSF Allstar : https://github.com/ossf/allstar
[^reuse]: REUSE : https://reuse.software/
[^community-standards]: About community profiles for public repositories — GitHub Docs : https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories

`README.md`, `CONTRIBUTING.md`의 내용은 프로젝트를 운영할 개발자가 작성하는 것이 더 적합하다. 작성 요령에 대한 자세한 내용은 [오픈소스SW 공개 가이드 - 개발자 편: 오픈소스SW 공개를 준비하기](#오픈소스sw-공개를-준비하기) 에서 다룬다.

CLA는 기여 과정의 일부이므로 Contributing 문서에서 함께 다루는 것이 좋다. CLA 양식은 이미 정해두었더라도, 이를 서면으로 제출하게 하면 번거롭다. 그래서 대부분 전자 서명으로 운영한다. CLA를 관리하는 도구와 운영 사례는 다음을 참고한다.

- [CLA assistant](https://github.com/cla-assistant/cla-assistant)[^cla-assistant]
- [cla-bot](https://colineberhardt.github.io/cla-bot)[^cla-bot]
- [Google Developers Contributor License Agreements](https://cla.developers.google.com/clas)[^clas]
- [Microsoft Contributor License Agreement](https://cla.opensource.microsoft.com)[^mscla]

[^cla-assistant]: CLA assistant : https://github.com/cla-assistant/cla-assistant
[^cla-bot]: cla-bot : https://colineberhardt.github.io/cla-bot
[^clas]: Google Developers Contributor License Agreements : https://cla.developers.google.com/clas
[^mscla]: Microsoft Contributor License Agreement : https://cla.opensource.microsoft.com


오픈소스SW 생태계는 자유와 존중을 중요한 가치로 두지만, 누구나 익명으로 활동할 수 있는 공간이기도 하다. 따라서 차별이 일어날 가능성을 미리 줄이고, 불편한 상황이 발생했을 때 도움을 청할 수 있는 연락처를 제공해야 한다. 오픈소스SW 커뮤니티에서 금지하는 언행을 나열하고, 이를 어겼을 때 조치를 요구할 수 있는 연락처를 제시하는 문서가 Code of conduct다.

다음은 널리 쓰이는 Code of conduct 예시다.

- [Contributor Covenant, A Code of Conduct for Open Source Projects](https://www.contributor-covenant.org)[^contributor-covenant]
- [Django Code of Conduct](https://www.djangoproject.com/conduct/)[^django-coc]
- [Geek Feminizm Code of Conduct](https://geekfeminismdotorg.wordpress.com/about/code-of-conduct/)[^geekcoc]

[^contributor-covenant]: Contributor Covenant, A Code of Conduct for Open Source Projects : https://www.contributor-covenant.org
[^django-coc]: Django Code of Conduct : https://www.djangoproject.com/conduct/
[^geekcoc]: Geek Feminizm Code of Conduct : https://geekfeminismdotorg.wordpress.com/about/code-of-conduct/

##### 저장소 생성, 멤버 권한 설정

검토 과정에서 정한 이름으로 비공개 저장소를 만든다. 개발에 필요한 멤버의 username을 모아 비공개 저장소 접근 권한을 부여한다. Description과 Topics를 추가하면 오픈소스SW의 개요를 더 간결하게 표현할 수 있다.

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

코드를 옮기기 전에 commit 이력을 모두 공개할 것인지, 삭제할 것인지 정해야 한다. 검토 과정에서 보안 권고에 따라, 혹은 명칭을 변경하는 등 코드가 수정되었다면 이력을 공개하지 않는 쪽을 택하는 경우가 많다. 다만 이력을 지우는 것만으로 안전해지지는 않는다. 이력을 없애고 단일 커밋으로 옮겨도 파일 내용, 주석, 테스트 픽스처, 설정 파일에 남은 값은 그대로 공개된다. 따라서 이력 공개 여부와 무관하게 아래 정제 절차를 모두 수행한다. 코드 이전은 되돌릴 수 없는 단계이므로 항목을 건너뛰지 않는다.

**공개 전 코드 정제 체크리스트**

- [ ] **(1) 전체 커밋 이력을 대상으로 시크릿 스캔을 수행한다** — 작업 트리만이 아니라 이력 전체를 훑는다. [gitleaks](https://github.com/gitleaks/gitleaks)[^gitleaks], [TruffleHog](https://github.com/trufflesecurity/trufflehog)[^trufflehog]를 사용한다. (보안팀)
- [ ] **(2) 발견된 자격증명은 이력에서 제거하고, 노출된 자격증명 자체를 즉시 폐기·회전한다** — 제거에는 [git-filter-repo](https://github.com/newren/git-filter-repo)[^filter-repo] 또는 [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)[^bfg]를 쓴다. 제거는 유출 대응이 아니다. 폐기·회전을 하지 않으면 노출된 키는 계속 유효하다. (보안팀)
- [ ] **(3) 커밋 작성자 이메일을 정리한다** — 사내 도메인 주소와 개인 메일 주소를 조직이 정한 표기(예: 호스팅 서비스가 제공하는 noreply 주소)로 통일한다. 정리 방침을 인사팀과 미리 합의한다. (개발자)
- [ ] **(4) 내부 식별자 문자열을 검색해 제거한다** — 사내 호스트명, 내부 IP 대역, 사내 저장소 경로, 조직 내부 시스템 이름을 대상으로 한다. (보안팀·개발자)
- [ ] **(5) 서드파티 코드의 출처와 라이선스를 확인하고 고지문을 작성한다** — 복사해 온 코드 조각과 벤더링된 의존성을 포함한다. 확인 결과를 `NOTICE` 또는 `THIRD_PARTY` 파일로 남긴다. (검수팀)
- [ ] **(6) 파일별 라이선스·저작권 표기를 넣는다** — REUSE 규격을 따를 경우 각 파일 헤더에 SPDX 식별자와 저작권 줄을 넣고, 사용한 라이선스 전문을 `LICENSES/` 디렉터리에 둔다[^reuse]. (검수팀·개발자)
- [ ] **(7) AI 코딩 도구로 생성된 구간의 출처를 검토한다** — 의존성 스캔은 복사된 코드 조각을 찾지 못한다. 검토 방법과 도구는 [AI와 오픈소스SW - 개발자 편](/ai/)에서 다룬다. (개발자)

[^gitleaks]: gitleaks : https://github.com/gitleaks/gitleaks
[^trufflehog]: TruffleHog : https://github.com/trufflesecurity/trufflehog
[^filter-repo]: git-filter-repo : https://github.com/newren/git-filter-repo
[^bfg]: BFG Repo-Cleaner : https://rtyley.github.io/bfg-repo-cleaner/

##### 배포 준비

소스 코드를 공개한 이후에 패키지 배포까지 생각하고 있는 경우에는 배포를 어떻게 할지 정해야 한다. 패키지 저장소마다 사용 방법이 다르니 개발자와 상의한다. 배포와 관련한 상세 내용은 [오픈소스SW 공개 가이드 - 개발자 편: 오픈소스SW 운영하기 > 오픈소스SW 배포하기](#오픈소스sw-배포하기) 를 참고한다. 

#### 공개

더 이상 설정하고 확인할 것이 없다면 비공개 저장소를 공개 저장소로 전환한다.

- [GitHub - 공개 저장소로 전환하기](https://docs.github.com/en/github/administering-a-repository/setting-repository-visibility#changing-a-repositorys-visibility)[^github-chaging-repo]
- [GitLab - 공개 저장소로 전환하기](https://docs.gitlab.com/user/public_access/#change-project-visibility)[^gitlab-change-repo]

[^github-chaging-repo]: GitHub - 공개 저장소로 전환하기 : https://docs.github.com/en/github/administering-a-repository/setting-repository-visibility#changing-a-repositorys-visibility
[^gitlab-change-repo]: GitLab - 공개 저장소로 전환하기 : https://docs.gitlab.com/user/public_access/#change-project-visibility

### 공개만 하면 끝인가요? 그 이후에 해야 할 일

소스 코드를 공개하기까지 여러 사람의 손길을 거쳤지만, 아직 오픈소스SW를 완성했다고 말하기는 이르다. 지금까지는 사람들이 저장소를 방문했을 때 가장 먼저 보는 부분을 다듬어 첫인상을 만든 것에 가깝다. 단순히 공개된 소스 코드에서 사랑받는 오픈소스SW로 거듭나려면 이후 과정이 매우 중요하다. 앞으로는 커뮤니티를 활성화하고 오픈소스SW를 성장시키는 과정을 살펴본다.

#### 소통하기

현재 가장 먼저 드러나는 문제는 사람들이 이 오픈소스SW가 존재한다는 사실 자체를 모른다는 것이다. 새로운 오픈소스SW가 탄생했다는 사실을 적극적으로 알려야 한다.

##### 소셜 미디어

회사를 대표하는 소셜 미디어 계정이 있다면 새로운 오픈소스SW의 공개 소식을 알린다. 개발자를 대상으로 한 개발자 전용 계정이 있다면 더욱 좋다.

{{< imgproc twitter-line Fit "768x768" >}}
<center><i>LINE Developers Twitter : https://twitter.com/line_developers/status/1330773983873011712?s=20</i></center>
{{< /imgproc >}}


{{< imgproc twitter-facebook Fit "768x768" >}}
<center><i>Facebook Open Source Twitter : https://twitter.com/fbOpenSource/status/1356301287026028552?s=20</i></center>
{{< /imgproc >}}

##### 기술 블로그

회사에 기술 블로그가 있다면 활용한다. 기술 블로그에서는 이 오픈소스SW로 어떤 문제를 해결했는지, 주요 기능은 무엇인지 더 자세히 설명할 수 있다.

- 새로 공개한 오픈소스SW를 소개하는 블로그 글: [LINE 기술 블로그 - Mono-repo, Multi-project를 Gradle 플러그인으로 손쉽게 관리하기](https://engineering.linecorp.com/ko/blog/mono-repo-multi-project-gradle-plugin/)[^line-mono]
- 오픈소스SW의 기능을 소개하는 블로그 글: [LINE 기술 블로그 - Armeria의 서킷 브레이커 사용해 보기](https://engineering.linecorp.com/ko/blog/try-armeria-circuit-breaker/)[^line-armeria]
- 새로 공개한 오픈소스SW를 도입한 사례를 전하는 블로그 글: [LINE 기술 블로그 - Kafka를 이용한 작업 큐 라이브러리 'Decaton' 활용 사례](https://engineering.linecorp.com/ko/blog/decaton-case-studies/)[^line-kafka]

[^line-mono]: LINE 기술 블로그 - Mono-repo, Multi-project를 Gradle 플러그인으로 손쉽게 관리하기 : https://engineering.linecorp.com/ko/blog/mono-repo-multi-project-gradle-plugin/
[^line-armeria]: LINE 기술 블로그 - Armeria의 서킷 브레이커 사용해 보기 : https://engineering.linecorp.com/ko/blog/try-armeria-circuit-breaker/
[^line-kafka]: LINE 기술 블로그 - Kafka를 이용한 작업 큐 라이브러리 'Decaton' 활용 사례 : https://engineering.linecorp.com/ko/blog/decaton-case-studies/

블로그 글을 업로드하는 것에서 그치지 않고 다시 소셜 미디어로 공유하면 글 확산에 큰 도움이 된다.

{{< imgproc line-facebook Fit "768x768" >}}
<center><i>https://engineering.linecorp.com/ko/blog/try-armeria-circuit-breaker/</i></center>
{{< /imgproc >}}

##### 웹사이트 제작

오픈소스SW의 사용법을 담은 문서를 단순히 markdown으로 작성할 수도 있지만, 시간을 더 들여 웹사이트를 제작할 수도 있다. 웹사이트가 있으면 방문자 추적이 가능해 더 심화된 마케팅도 진행할 수 있다. 프로젝트 규모에 따라 웹사이트 제작을 고려한다.

##### 다양한 커뮤니케이션 수단 마련

Issue tracker로 사용자와 소통할 수 있지만, 사람들은 Issue tracker를 질의응답 수단으로 잘 여기지 않는다. 더 가볍게 소통하려면 [Slack](https://slack.com/intl/ko-kr)[^slack]이나 [Gitter](https://gitter.im)[^glitter] 같은 대화형 커뮤니케이션 도구를 쓸 수 있다. 이 역시 프로젝트 규모에 따라 고려한다.

[^slack]: Slack : https://slack.com/intl/ko-kr
[^glitter]: Gitter : https://gitter.im


##### 기술 콘퍼런스 참여

이 세상에는 기술 행사가 많다. 규모도 제각각이고 주제도 다양하다. 예산과 인력은 한정되어 있으므로 모든 행사에 참여할 수는 없다. 프로젝트의 성격에 맞는 행사를 먼저 정하고, 그 행사의 일정에서 역산해 준비한다.

다음은 프로젝트 성격에 따른 목표 행사 유형이다. 개별 행사의 명칭과 개최 형태는 해마다 바뀌므로 유형으로 정리한다.

| 프로젝트 성격 | 목표 행사 유형 | 기대 효과 |
|--------------|--------------|----------|
| 클라우드 네이티브·인프라 계열 | 해당 기술 영역의 재단이 주관하는 프로젝트 콘퍼런스와 그 부속 데이 행사 | 같은 스택을 쓰는 채택자와 직접 접촉한다 |
| 일반 오픈소스SW·언어/프레임워크 | 대규모 오픈소스SW 종합 콘퍼런스, 커뮤니티가 주관하는 개발자 행사 | 프로젝트의 존재를 처음 알린다 |
| 국내 사용자 확보가 목표 | 국내 공개SW 진흥 기관과 커뮤니티가 주관하는 행사, 공공 기여 프로그램 | 국내 기여자를 확보하고 사용 사례를 만든다 |
| 자사 브랜드 노출이 목표 | 자체 개발자 콘퍼런스 | 발표 내용과 일정을 자사가 통제한다 |

참여 형태는 비용과 목적에 따라 다르게 결정한다. 다음을 판단 기준으로 쓴다.

| 참여 형태 | 선택하는 조건 | 확인할 것 |
|----------|-------------|----------|
| 발표(CFP 제출) | 공개할 기술적 내용이 있고 발표자를 확보할 수 있다 | 발표 자료의 사내 검토 경로(홍보·법무·상표) |
| 부스 운영 | 채용을 함께 목표로 하거나 대면 데모가 필요하다 | 상주 인력, 배포물 제작 기간, 부스 비용 대비 접촉 인원 |
| 스폰서십 | 프로젝트가 의존하는 상류 커뮤니티를 지원할 명분이 있다 | 로고 노출 외의 실질 혜택, 후원 등급별 비용 |
| 원격 참여 | 예산이 제한되거나 현지 출장 인원을 줄여야 한다 | 하이브리드 개최 여부, 발표 영상의 사후 공개 여부 |

준비 일정은 CFP 마감에서 역산한다. 다음 순서로 진행한다.

- [ ] CFP 공고 시점에 참여 후보 행사를 목록으로 만들고 우선순위를 정한다
- [ ] CFP 마감 전에 발표 초록을 작성하고 홍보·법무·상표 검토를 받는다
- [ ] 채택 통보 후 발표 자료를 완성하고 사내 리허설로 내용을 검증한다
- [ ] 행사 직후 발표 자료와 영상을 공개하고, 같은 내용을 기술 블로그 글로 전재해 재활용한다

##### 로고 제작

오픈소스SW 프로젝트를 완성도 높은 하나의 제품으로 보이게 하는 효과적인 방법이다. 프로젝트의 특징을 보여주는 로고(symbol)를 만들어 발표 자료, 홈페이지, 문서 등에서 활용하면 오픈소스SW의 브랜드 이미지를 훨씬 강조할 수 있다.

#### 사용자 늘리기

오픈소스SW가 존재한다는 사실을 알렸다고 해서 반드시 사용자가 느는 것은 아니다. 다시 사용자의 관점에서 어떤 오픈소스SW를 채택하기까지 고려하는 사항을 확인한다. ([오픈소스SW 사용 가이드 - 개발자 편: 오픈소스SW 선택 기준](/using/#오픈소스sw-선택-기준) 에서 자세히 다룬다.) 이를 거꾸로 이용하면 다음과 같다.

1. 많이 쓰이는 오픈소스SW인가? ☞ 사내 다른 제품·프로젝트에서 도입할 수 있도록, 이미 사내에서 적용 중인 유즈 케이스를 보여준다. 이후 사용자가 생길 때마다 유즈 케이스를 공유하도록 독려한다.

2. 팀에서 이 오픈소스SW를 배우기 어렵지는 않은가? ☞ 쉽게 읽고 따라 할 수 있는 문서를 제공한다.

3. 유지보수가 잘 되고 있는가? ☞ 기능을 꾸준히 개선한다. 사용자 의견에 귀를 기울이고 반영한다.

4. 유사 오픈소스SW와의 차이점은 무엇인가? (얼마나 효율적인가?) ☞ 이 오픈소스SW만의 특장점을 README나 다른 문서에서 설명한다.

5. 커뮤니티는 활성화되어 있는가? ☞ 참여를 독려하고 커뮤니티가 형성될 수 있도록 분위기를 조성한다.

이 다섯 가지를 효과적으로 이행하려면 다시 소통하기로 돌아간다.

- 1번과 4번을 위해서는 기술 블로그, 소셜 미디어, 기술 콘퍼런스 등을 통해 유즈 케이스와 레퍼런스를 지속해서 노출한다.
- 2번을 위해서는 처음 접하는 개발자를 섭외해 문서를 읽고 따라 해보도록 부탁한다. 잘 안되는 부분이 있으면 그 부분을 설명하는 문서를 보완하고, 홈페이지를 만들어 튜토리얼을 강화한다.
- 3번과 5번을 위해서는 커뮤니케이션 채널, 이슈 트래커, Pull request에서 적극적으로 소통한다. 먼저 다가가 질문하면, 사용자들이 왜 아직 도입을 망설이는지 의외로 열린 마음으로 답해 주기도 한다.

### 기업 편 요약

지금까지 기업의 오픈소스SW 담당자 관점에서, 공개 정책을 설정하는 단계부터 새로운 오픈소스SW를 공개하기까지의 과정을 살펴보았다. 이를 요약하면 다음과 같다.

**공개 정책 설정**

- 기업이 오픈소스SW를 공개하는 목적을 설정한다.
- 오픈소스SW 공개를 검토할 유관 부서와 상의한다.
- 오픈소스SW를 운영할 주체를 결정한다.
- 언제, 어디에 공개할지 정한다.
- 어떤 조건으로 공개할지 결정한다. (라이선스 적용)
- 정책을 바탕으로 공개 신청서와 작성 가이드를 문서화한다.

**공개하기**

- 신청서를 확인하고 미비한 부분이 없는지 검토한다.
- 공개 정책에서 정한 검토 과정을 따른다.
- 거버넌스 문서를 추가한다.
- 비공개 저장소를 만들고 권한을 설정한다.
- 코드를 옮긴다.
- 배포를 준비한다.
- 공개 저장소로 전환한다.

오픈소스SW 공개와 운영은 다이어트와 비슷하다. 여기까지 진행했다면, 오픈소스SW를 공개할 수 없던 기업에서 훌륭한 오픈소스SW를 만들어 낼 수 있는 기업으로 성장한 것이다. 그러나 소스 코드 공개에서 멈추면 지금까지의 노력이 허사가 된다. 꾸준한 노력과 관리, 마케팅까지 앞으로 할 일이 많다. 오픈소스SW 운영의 장점이자 단점은 일정에 덜 쫓긴다는 점이다. 품질이 중요하므로 구멍을 빨리 메우기보다 제대로 메우는 자세로 임하게 된다. 또한 성과가 눈에 잘 드러나지 않는 경우도 있다. 그러니 막막하게 여기고 지쳐 포기하기보다 꾸준히 임할 것을 당부한다.

## 오픈소스SW 공개 가이드 - 개발자 편

개발자 개인의 입장에서 오픈소스SW를 공개하면 왜 좋은지 공감했다면 도전할 마음가짐은 갖춘 셈이다. 그러나 공개 과정을 설명하는 문서가 아무리 읽기 쉽게 작성되어 있어도, 어디서부터 무엇을 고민해야 할지 감이 잘 안 올 수 있다. 이번 장에서는 기업 구성원이 오픈소스SW 공개를 결심하고 운영하는 과정 전반에서 미리 알아 두면 좋은 팁을 정리한다.

### 오픈소스SW 공개를 준비하기

#### 기업의 입장에서 오픈소스SW를 판단하는 기준을 생각해보기

지금까지 오픈소스SW를 공개하면 좋은 점을 자세히 설명했지만, 사실 어떤 오픈소스SW를 공개하느냐도 성공의 중요한 요소다. '우리 프로젝트를 왜 오픈소스SW로 공개해야 하는가'라는 물음에 답하려면 다음을 미리 고민해 보는 것이 도움이 된다.

##### 실력 있는 개발자들의 관심을 끌 수 있는가?
  - 채용과 관련 있는 프로젝트인가?
##### 프로젝트를 사내에서만 개발하는 것 보다 외부의 리소스를 활용하는 것이 더 효율적인가?
  - 실력 있는 개발자들이 참여해서 오픈소스SW의 품질을 높일 수 있는가?
  - 대중적인 요구 사항을 해결하는 프로젝트인가?
##### 프로젝트가 지속 가능한가?
  - 공개 이후 중장기적으로 지속해서 발전할 수 있는 프로젝트인가? 단순 공개에서 그치진 않을 것인가?

#### 공개 이후 운영 계획에 대해 생각해보기

앞서 언급한 '프로젝트의 지속 가능성'을 좀 더 다룬다. 아무리 좋은 프로젝트라도 적절히 관리하지 않으면 도태되기 때문이다. 실제로 기업 Organization에 등록된 저장소는 업데이트된 순서로 정렬되므로, 변경이 없으면 저장소가 뒷페이지로 밀려난다.

사람들이 오픈소스SW를 선택하는 중요한 기준 중 하나는 잘 관리되고 있는가이다. 따라서 앞으로의 변경을 예고하기 위해 소스 코드 공개 이후 발전시켜 나갈 마일스톤을 계획한다. 또한 누구나 확인할 수 있도록 마일스톤을 이슈 트래커에 등록해 둔다. 특히 다른 업무에서 이 오픈소스SW를 함께 사용한다면 유리하다. 사용하면서 필요한 기능을 지속해서 오픈소스SW에 반영할 수 있기 때문이다. 오픈소스SW를 공개하기 전부터 앞으로 투자하게 될 시간을 미리 인지하고 있어야 한다.

외부 개발자의 기여를 유도하려면 지속적인 관리와 기술적·사업적 홍보가 필요하다. 또한 커뮤니티와의 소통, 이슈 대응, 기여 수용 절차에 관한 정책도 미리 준비해야 한다.

#### 오픈소스SW 운영에 필요한 도구 탐색하고 공부하기

오픈소스SW를 운영하면서 모든 것을 다 수작업으로 할 필요는 없다. 저장소와 연동되는 도구가 많으니 미리 탐색해볼 것을 추천한다. 다만 도구의 무료 정책은 자주 바뀐다. 도구 이름을 외우기보다 '무엇을 자동화할 것인가'를 먼저 정하고, 도입 시점에 각 도구의 무료 조건을 직접 확인한다. 다음은 용도별로 널리 쓰이는 도구와 확인해야 할 무료 조건이다.

| 용도 | 도구 | 무료 조건 |
|------|------|----------|
| CI/CD | [GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-your-products/about-billing-for-github-actions)[^gh-actions-billing], [GitLab CI](https://docs.gitlab.com/ci/)[^gitlab-ci] | GitHub Actions는 공개 저장소에서 무료다. 러너 종류와 사용량 한도는 요금 문서에서 확인한다 |
| 의존성 갱신 | [Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot)[^dependabot], [Renovate](https://docs.renovatebot.com/)[^renovate] | Dependabot은 독립 서비스가 아니라 GitHub 내장 기능이다. 저장소 보안 설정에서 켜고 [`.github/dependabot.yml`](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file)[^dependabot-yml]로 갱신 주기를 정의한다. GitHub 외 환경에서는 Renovate를 쓴다 |
| 커버리지 | [Codecov](https://about.codecov.io/)[^codecov] | 오픈소스SW 플랜의 적용 조건을 도입 전에 확인한다 |
| 릴리스 자동화 | [semantic-release](https://semantic-release.gitbook.io/semantic-release/)[^semantic-release], [Release Please](https://github.com/googleapis/release-please)[^release-please] | 도구 자체가 오픈소스SW이며 CI에서 실행한다 |
| 보안 | [OpenSSF Scorecard Action](https://github.com/ossf/scorecard-action)[^scorecard-action], [CodeQL](https://codeql.github.com/)[^codeql], [gitleaks](https://github.com/gitleaks/gitleaks)[^gitleaks], [OSV-Scanner](https://github.com/google/osv-scanner)[^osv-scanner] | Scorecard·gitleaks·OSV-Scanner는 오픈소스SW다. CodeQL은 코드 스캐닝 기능으로 제공되므로 저장소 공개 여부에 따른 과금 조건을 확인한다 |
| 라이선스 | [REUSE](https://reuse.software/)[^reuse] | 도구 자체가 오픈소스SW다 |
| 기여자 관리 | [All Contributors](https://allcontributors.org/)[^all-contributors] | 도구 자체가 오픈소스SW다 |

Pull request 리뷰가 특정 인원에게 몰리거나 리뷰가 지연되는 문제는 별도 서비스를 도입하지 않고 저장소 기능으로 해결한다. 리뷰어를 자동 지정하려면 [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)[^codeowners]를 쓰고, 대기 중인 리뷰를 팀에 알리려면 [scheduled reminders](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team)[^gh-reminders]를 설정하며, 병합 충돌과 대기열은 [머지 큐](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)[^merge-queue]로 처리한다.

[^gh-actions-billing]: About billing for GitHub Actions — GitHub Docs : https://docs.github.com/en/billing/managing-billing-for-your-products/about-billing-for-github-actions
[^gitlab-ci]: GitLab CI/CD — GitLab Docs : https://docs.gitlab.com/ci/
[^dependabot]: Working with Dependabot — GitHub Docs : https://docs.github.com/en/code-security/dependabot/working-with-dependabot
[^dependabot-yml]: Configuration options for the dependabot.yml file — GitHub Docs : https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file
[^renovate]: Renovate Docs : https://docs.renovatebot.com/
[^codecov]: Codecov : https://about.codecov.io/
[^semantic-release]: semantic-release : https://semantic-release.gitbook.io/semantic-release/
[^release-please]: Release Please : https://github.com/googleapis/release-please
[^codeql]: CodeQL : https://codeql.github.com/
[^osv-scanner]: OSV-Scanner : https://github.com/google/osv-scanner
[^all-contributors]: All Contributors : https://allcontributors.org/
[^codeowners]: About code owners — GitHub Docs : https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
[^gh-reminders]: Managing scheduled reminders for your team — GitHub Docs : https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team
[^merge-queue]: Managing a merge queue — GitHub Docs : https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue


#### README.md 작성 요령

`README.md`는 오픈소스SW의 표지다. 저장소를 방문한 모든 사람에게 가장 먼저 보이는 문서이기 때문이다. 모든 방문자에게 알리고 싶은 내용이나 방문자가 궁금해할 만한 내용을 적어야 한다. 다만 분량이 너무 길면 읽지 않고 지나치는 경우도 있으므로 적당한 분량을 유지한다. 잘 쓴 README의 형식은  [Make a README](https://www.makeareadme.com)[^makeareadme]에 정리되어 있다. 다음은 그중 일부다.

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
> 오픈소스SW 프로젝트라면 [어떤 라이선스를 적용했는지](https://www.makeareadme.com/#license-1)[^license-1] 표시한다.
[^license-1]: 라이선스 적용 : https://www.makeareadme.com/#license-1
>
> ##### Project status
>
> 만약 이 프로젝트를 위해 쏟을 시간이나 여력이 더 이상 없다면 README에 개발이 느릴 수 있다거나 혹은 아예 더 이상 개발을 하지 않는다는 메모를 남긴다. 누군가가 이 프로젝트를 fork하거나, 메인테이너/오너로 자원해서 프로젝트를 유지할 수도 있다. 메인테이너를 위한 명시적인 요청을 남길 수도 있다.

이 내용을 모두 담기 어렵다면 상황에 따라 적절히 생략하거나 추가한다.

잘 작성된 README의 예시들은 [Awesome README](https://github.com/matiassingers/awesome-readme)[^awesome-readme]에서 확인할 수 있다.
[^awesome-readme]: Awesome README : https://github.com/matiassingers/awesome-readme

#### CONTRIBUTING.md 작성 요령

`CONTRIBUTING.md` 작성은 사람들에게 도움을 받을 수 있는 방법 중 하나다. 보통 사람들은 정확한 요구를 인지했을 때 도움을 주려고 하기 때문이다. 또한 다양한 사람에게 기여를 받아 개발할 때 지켜야 할 규칙을 미리 안내하는 문서이기도 하다. 어떤 내용이 들어가야 미래의 기여자와 메인테이너 모두에게 도움이 될지 정리한다.

- 받고자 하는 기여의 종류
  - 코드 작성만이 기여는 아니다. 질문을 남기는 방법, 버그를 제보하는 방법, 새로운 기능을 제안하는 방법 등 기대하는 기여의 종류를 나열한다.
- 코드 기여 방법
  - 전체적인 코드 기여 방법을 설명한다. 개발 환경 설정과 저장소 fork부터 시작해 변경 사항을 제출하고 받아들여지기까지의 과정을 설명한다.
- 개발 환경 설정 방법
  - 직접 코드를 작성하고 기여하기 위한 개발 환경 설정 방법을 설명한다.
- 코딩 컨벤션 / 스타일 가이드
- Commit 메시지 규칙
- Code of Conduct
  - 커뮤니티 활동에서 지켜야 할 행동 규범을 언급한다.
- CLA/DCO
  - 기여를 제출할 때 서명해야 할 문서를 안내하고 서명 방법도 함께 설명한다.

`CONTRIBUTING.md`의 예시는 다음을 참고한다.

- [Atom - Contributing to Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md)[^atom-contributing]
- [Kubernetes - Contributor's Guide](https://github.com/kubernetes/community/tree/master/contributors/guide)[^k8s-contributing]    
- [Armeria - Developer guide](https://armeria.dev/community/developer-guide)[^armeria-guide]

[^atom-contributing]: Atom - Contributing to Atom : https://github.com/atom/atom/blob/master/CONTRIBUTING.md
[^k8s-contributing]: Kubernetes - Contributor's Guide : https://github.com/kubernetes/community/tree/master/contributors/guide
[^armeria-guide]: Armeria - Developer guide : https://armeria.dev/community/developer-guide


### 오픈소스SW 운영하기

오픈소스SW 공개의 핵심은 커뮤니티와 함께 프로젝트를 운영하는 일이다. 처음에는 혼자 운영을 시작하더라도, 계속해서 커뮤니티가 참여할 수 있는 빈틈을 만들어야 한다. 이는 나중에 메인테이너를 대신해 활동해 줄 커뮤니티를 키우는 씨앗이라고 생각하면 좋다.

열정적으로 오픈소스SW를 운영하는 것은 좋지만, 계속 혼자 짐을 지면 프로젝트를 오래 지속하기 어렵다. 가능한 범위에서 메인테이너 혼자 짐을 지는 상황을 줄여 나간다.

#### 오픈소스SW 배포하기

소스 코드를 배포한 뒤에는 사용을 쉽게 하기 위해 패키지 배포도 함께 진행할 가능성이 높다. 다만 평소 업무 환경과 다른 환경에서 배포하게 되므로 시행착오가 있을 수 있다. 가장 널리 쓰이는 오픈소스SW 패키지 배포 방법과 자동화 방법은 다음을 참고한다.

- [Maven Central에 배포하기 (Sonatype Central Portal)](https://central.sonatype.org/publish/publish-portal-guide/)[^maven-central]
- [npm에 배포하기](https://docs.npmjs.com/creating-and-publishing-scoped-public-packages)[^npm]
- [PyPI에 배포하기](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects)[^pypi]
- [자동화: 유용한 GitHub Actions workflow 모음](https://github.com/sdras/awesome-actions)[^actions]

[^maven-central]: Publishing By Using the Portal — Sonatype Central : https://central.sonatype.org/publish/publish-portal-guide/
[^npm]: npm에 배포하기 : https://docs.npmjs.com/creating-and-publishing-scoped-public-packages
[^pypi]: PyPI에 배포하기 : https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects
[^actions]: 유용한 GitHub Actions workflow 모음 : https://github.com/sdras/awesome-actions

Maven Central 게시 경로는 Central Portal로 일원화되었다. 종전의 OSSRH(oss.sonatype.org) 경로는 2025년 6월 30일자로 종료되어 더 이상 사용할 수 없다[^ossrh-eol]. 인터넷에 남아 있는 구 안내 문서를 그대로 따라가면 배포가 되지 않으므로, 다음 네 단계를 기준으로 진행한다.

- [ ] **1. namespace 소유를 검증한다** — 도메인 기반 namespace는 해당 도메인에 DNS TXT 레코드를 추가해 소유를 증명한다. 코드 호스팅 기반 namespace는 `io.github.<사용자명>` 형태의 임시 공개 저장소를 만들어 증명한다[^central-namespace].
- [ ] **2. GPG 서명을 준비한다** — 게시할 아티팩트에 서명을 붙이고 공개키를 공개 키서버에 등록한다[^central-gpg].
- [ ] **3. 빌드 도구의 퍼블리시 설정을 맞춘다** — Maven 플러그인 또는 Gradle 설정으로 Portal이 요구하는 번들을 생성한다[^maven-central].
- [ ] **4. Portal에 업로드하고 릴리스한다** — 업로드 후 검증을 통과하면 게시한다. 한 번 게시한 구성요소는 제거·수정할 수 없으므로 버전 번호와 좌표를 먼저 확정한다[^maven-central].

[^ossrh-eol]: OSSRH End-of-Life — Sonatype Central : https://central.sonatype.org/pages/ossrh-eol/
[^central-namespace]: Choosing and Verifying Your Namespace — Sonatype Central : https://central.sonatype.org/register/namespace/
[^central-gpg]: GPG Signed Components — Sonatype Central : https://central.sonatype.org/publish/requirements/gpg/

{{< imgproc release-pipeline-2026 Fit "768x768" >}}
<center><i>[릴리스 보증 파이프라인 — SBOM·서명·프로비넌스]</i></center>
{{< /imgproc >}}

##### 안전하게 배포하기 — 서명·프로비넌스·SBOM

패키지를 올리는 것만으로는 부족하다. 채택자가 '누가 어떤 소스로 빌드했는지'를 스스로 검증할 수 있는 증거를 릴리스마다 남겨야 한다. 이 요구는 프로젝트를 알려 사용자를 늘리는 활동과는 별개다. 외부 오픈소스SW를 도입하는 쪽이 릴리스 서명과 출처 증명을 도입 심사 항목으로 확인하기 때문이다([오픈소스SW 사용 가이드 - 개발자 편: 오픈소스SW 선택 기준](/using/#오픈소스sw-선택-기준)). 검증 수단도 갖춰졌다. npm 프로비넌스, PyPI 어테스테이션, GitHub artifact attestation은 `cosign` 한 명령으로 검증할 수 있다[^cosign-verify]. 증거를 남기지 않은 릴리스는 이 심사에서 제시할 근거가 없다. 다음 다섯 가지를 릴리스 워크플로에 넣는다.

- [ ] **(1) 장기 API 토큰 대신 CI의 OIDC 기반 Trusted Publishing을 쓴다** — PyPI[^pypi-trusted]와 npm[^npm-trusted]이 지원한다. npm은 2025-12-09에 모든 classic token을 영구 폐기했고, 쓰기 권한 granular token은 최대 90일로 제한되며, 신규 패키지는 2FA가 기본값이다[^npm-token]. 채택자 확인: 프로비넌스에 기록된 빌드 워크플로.
- [ ] **(2) 아티팩트에 서명하고 프로비넌스를 발행한다** — npm은 `--provenance` 옵션으로 프로비넌스를 함께 게시한다[^npm-provenance]. GitHub Actions에서는 artifact attestation으로 빌드 증명을 만든다[^gh-attestations]. 채택자 확인: `cosign`으로 npm 프로비넌스·GitHub artifact attestation·Homebrew 프로비넌스를 단일 명령으로 검증한다[^cosign-verify].
- [ ] **(3) 릴리스마다 SBOM을 첨부한다** — SPDX 또는 CycloneDX 형식으로 생성해 릴리스 페이지에 올린다. SBOM의 개념과 최소 요구 사항은 [오픈소스SW 사용하기: SBOM 관리](/using/#sbom-관리)에서 다루므로, 공개하는 쪽은 '생성해서 붙인다'만 담당한다. 채택자 확인: 첨부된 SBOM을 자사 SCA 도구에 투입한다.
- [ ] **(4) 게시 계정에 2FA를 강제하고 릴리스 태그에 서명한다** — 메인테이너 계정 탈취가 곧 패키지 침해로 이어진다. 채택자 확인: 저장소의 서명된 태그 표시.
- [ ] **(5) 릴리스는 개인 로컬 환경이 아니라 CI에서만 수행한다** — 로컬 릴리스는 (1)~(4)의 증거를 만들지 못한다. 채택자 확인: 프로비넌스에 기록된 빌더 신원.

빌드 프로비넌스의 수준을 외부에 설명해야 한다면 SLSA 빌드 트랙의 레벨을 기준으로 삼는다. 현행 명세는 v1.2다[^slsa]. 레벨별 요구사항은 명세 본문을 따른다.

[^pypi-trusted]: Trusted Publishers — PyPI Docs : https://docs.pypi.org/trusted-publishers/
[^npm-trusted]: Trusted publishers — npm Docs : https://docs.npmjs.com/trusted-publishers
[^npm-token]: npm classic tokens revoked, session-based auth and CLI token management now available — GitHub Changelog (2025-12-09) : https://github.blog/changelog/2025-12-09-npm-classic-tokens-revoked-session-based-auth-and-cli-token-management-now-available/
[^npm-provenance]: Generating provenance statements — npm Docs : https://docs.npmjs.com/generating-provenance-statements/
[^gh-attestations]: Artifact attestations — GitHub Docs : https://docs.github.com/en/actions/concepts/security/artifact-attestations
[^cosign-verify]: cosign Verification of npm Provenance, GitHub Artifact Attestations, and Homebrew Provenance — Sigstore Blog : https://blog.sigstore.dev/cosign-verify-bundles/
[^slsa]: SLSA Specification v1.2 : https://slsa.dev/spec/v1.2/


#### Issue tracker 활용 best practice

Issue tracker는 현업에서도 많이 쓰이므로 오픈소스SW에서도 똑같이 쓰면 된다고 생각하기 쉽다. 그러나 이를 들여다보는 대상이 사뭇 다르다는 점을 알아야 한다. 현업에서는 주로 회의 등으로 선별된 이슈를 Issue tracker에 등록하고 이에 맞춰 개발 일정을 관리한다. 반면 오픈소스SW에서는 의견 교환이 즉시 이뤄지지 않는다. 어떤 의견을 남기고 다른 사람이 동의하거나 다른 의견을 낼 때까지 기다려야 한다. 사람들이 궁금한 부분을 Issue tracker에서 해결하지 못하면 그 부담은 고스란히 메인테이너에게 돌아온다. 또한 사람들은 구체적인 도움 요청을 보았을 때 비로소 움직일지 고민하며, 그 고민의 일부가 기여로 이어진다.

이처럼 다양한 기능을 하는 Issue tracker에서 커뮤니케이션을 더 효율적으로 하기 위한 팁을 정리한다.

##### 이슈 템플릿 활용

새 이슈를 만들려고 New issue 버튼을 클릭했는데 빈 화면을 마주하면 어떤 내용을 써야 할지 막막할 때가 있다. 이슈 템플릿은 프로젝트에서 처음 이슈를 등록하는 사람에게 작성 방법을 안내한다. 사람들이 오픈소스SW 프로젝트를 탐색하고 사용하면서 떠오른 질문을 마음속에 쌓아두지 않고 적극적으로 소통하도록 돕는다. 템플릿 예시는 흔히 체크리스트를 함께 제공한다. 이는 이슈 해결에 필요한 정보를 미리 제공하도록 유도해, 부족한 정보를 묻고 답하는 데 드는 커뮤니케이션을 줄이고 문제 해결에만 집중하도록 돕는다.

- [GitHub에서 Issue template를 만드는 방법](https://docs.github.com/en/github/building-a-strong-community/manually-creating-a-single-issue-template-for-your-repository#adding-an-issue-template)[^github-issue]
- [GitLab에서 Issue template를 만드는 방법](https://docs.gitlab.com/ee/user/project/description_templates.html#create-an-issue-template)[^gitlab-issue]
- [이슈 템플릿 예시 모음](https://github.com/stevemao/github-issue-templates)[^issue-templates]

[^github-issue]: GitHub에서 Issue template를 만드는 방법 : https://docs.github.com/en/github/building-a-strong-community/manually-creating-a-single-issue-template-for-your-repository#adding-an-issue-template
[^gitlab-issue]: GitLab에서 Issue template를 만드는 방법 : https://docs.gitlab.com/ee/user/project/description_templates.html#create-an-issue-template
[^issue-templates]: 이슈 템플릿 예시 모음 : https://github.com/stevemao/github-issue-templates

##### Label 활용

이슈 제목을 명확하게 작성하는 것도 중요하지만, 문장만으로는 한눈에 내용을 파악하기 어렵다. 이슈에 라벨을 달아 필터가 작동하게 하고, 이슈 종류를 한눈에 파악할 수 있게 한다.

{{< imgproc issue-label Fit "768x768" >}}
<center><i>https://github.com/line/armeria/issues/</i></center>
{{< /imgproc >}}


기여를 염두에 둔 사람들에게는 이런 라벨이 도전할 만한 일감을 찾는 데 큰 도움이 된다.

##### 초심자를 위한 이슈 

많은 개발자는 오픈소스SW에 기여하는 일을 '언젠간 해보고 싶은 것' 목록에 넣어 두곤 한다. 직접 나서지 않는 이유는 다양하지만, 시간이 없다는 이유 다음으로 많이 꼽히는 것이 '자신이 없어서'다. 이런 사람들을 오픈소스SW 기여의 세계로 불러오는 방법 중 하나가 초심자를 위한 이슈 라벨이다.

주로 `good first issue` 혹은 `first timers only` 라는 이름으로 지어진 이 라벨은 메인테이너나 기존 커미터들이 해결할 수 있지만 초심자를 위해 남겨두었다는 표식으로 사용된다. 따라서 기존 다른 이슈보다 해결 방안에 대한 더 자세한 설명이나 힌트를 달아놓는 경우가 많다. 이렇게 작은 이슈부터 시작할 수 있는 환경을 만들어 조금씩 어려운 이슈에도 도전할 수 있도록 자신감을 키워주는 과정을 거치도록 한다. 이 과정을 통해 꾸준한 커미터를 만들 수 있다.

GitHub에서는 아래 사진처럼 good first issue 탐색을 장려하는 메시지를 띄워 주기도 한다. 

{{< imgproc github-good-first-issue Fit "768x768" >}}
<center><i>https://github.com/line/armeira/issues</i></center>
{{< /imgproc >}}


#### Pull request 운영 best practice

이슈를 둘러보며 기여할지 고민만 하던 사람이 드디어 Pull request를 만들 결심을 했다고 가정해보자. 이 사람이 헤매지 않고 정기 기여자로 정착하려면 커뮤니케이션 과정에서 생길 수 있는 불편함을 최소화해야 한다. CONTRIBUTING 문서에서 많은 부분을 다루겠지만, 기여 과정을 더 효율적으로 만드는 팁을 정리한다.

#####  Pull request 템플릿 활용

각기 다른 생각을 가진 사람들이 어떤 변경을 반영하려면 다른 사람의 동의를 얻어야 한다. 동의를 구하려면 어떤 문제의식이 있었는지, 어떤 변경을 했는지, 그 결과가 무엇인지에 대한 설명이 필요하다. 그런데 이런 논리를 어떻게 작성해야 할지 모르는 사람들을 위해 Pull request 템플릿을 제공한다. 개발 과정에 익숙한 메인테이너도 같은 템플릿을 따라 작성한다. 다른 사람이 템플릿을 처음 사용할 때 작성 예시로 참고할 수 있기 때문이다.

문제 해결 이외에도 CONTRIBUTING에서 제시한 여러 개발 규칙이 있다. 이 내용을 Pull request 템플릿에서 체크리스트로 제공하면 코드 리뷰 과정에서 문제 해결에 집중하는 데 도움이 된다.

- [GitHub에서 Pull request template를 만드는 방법](https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository)[^github-pr-template]
- [GitLab에서 Merge request template를 만드는 방법](https://docs.gitlab.com/ee/user/project/description_templates.html#create-a-merge-request-template)[^gitlab-pr-template]
- [Pull request 템플릿 예시 모음](https://github.com/stevemao/github-issue-templates)[^pr-template]

[^github-pr-template]: GitHub에서 Pull request template를 만드는 방법 : https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository
[^gitlab-pr-template]: GitLab에서 Merge request template를 만드는 방법 : https://docs.gitlab.com/ee/user/project/description_templates.html#create-a-merge-request-template)
[^pr-template]: Pull request 템플릿 예시 모음 : https://github.com/stevemao/github-issue-templates

##### 적극적으로 댓글을 활용

사람들은 글자로만 소통하면 어감을 부정적으로 해석하는 경향이 있다. 열심히 기여했는데 환영받지 못한다고 느끼면 그 사람은 이후 지속해서 기여할 가능성이 낮아진다. 따라서 어떤 기여든 긍정적인 반응을 댓글로 남긴다. 이모지를 활용하는 것도 좋은 방법이다.

어떤 변경이 기존에 다른 사람이 개발한 부분과 연관된다면, 그 사람을 언급해 함께 확인하도록 안내한다. 기존 개발자는 해당 코드에 주인 의식을 느낄 수 있고, 새로운 변경이 기존 코드의 의도를 해칠 수도 있기 때문이다. 여러 사람이 참여할수록 커뮤니케이션 비용과 시간이 더 들지만, 결과적으로 더 건강하고 적극적인 커뮤니티를 만드는 데 큰 도움이 된다. 이런 커뮤니티는 나중에 메인테이너의 부담을 크게 줄여 준다.

##### 부드러운 재촉

여러 사람이 함께 개발하고 코드 리뷰에 참여하다 보면, 누군가의 응답이 늦어져 진행이 멈추는 경우가 종종 발생한다. 대개는 다른 일 때문에 오픈소스SW에 몰두하기 어려운 상황이다. 그렇다고 하염없이 반응을 기다리면 다른 의존적인 작업까지 지연될 수 있다. 이때는 당사자를 다시 한번 멘션해 특정 행동을 요청한다. 다그치듯 요구하기보다 "바쁘실 것 같은데 혹시 이렇게 진행해도 괜찮을까요?"나 "혹시 이 부분에 대해 더 의견이 없으신가요?"처럼 부드럽게 표현한다.

### 개발자 편 요약

지금까지 기업에 속한 개발자가 오픈소스SW 공개를 준비하고 운영하는 데 미리 알아 두면 좋은 팁을 살펴보았다. 요약하면 다음과 같다.

**오픈소스SW 공개를 준비하기**

- 내 프로젝트를 왜 오픈소스SW로 공개해야 하는지 기업 입장에서 생각해보기
- 공개 이후 운영 계획 생각해보기
- 오픈소스SW 운영에 필요한 도구를 탐색하고 공부하기
- `README.md` 잘 작성하기 
- `CONTRIBUTING.md` 잘 작성하기

**오픈소스SW 운영하기**

- 패키지 배포 방법 탐색하고 공부하기
- Issue tracker 잘 활용하기
  - 이슈 템플릿 활용
  - 이슈 라벨 활용
  - 초심자를 위한 이슈
- Pull request 잘 활용하기
  - Pull request 템플릿 활용
  - 댓글 활용
  - 사람들을 부드럽게 재촉하기

이 내용은 오픈소스SW 담당자의 시각에서 여러 프로젝트가 운영되는 모습을 살펴보며, 개발자가 이런 점을 조금 더 고려했다면 커뮤니티를 더 잘 형성했을 것이라는 아쉬움이 들었던 상황을 정리한 것이다. 따라서 기술적인 부분과는 거리가 멀다. 그러나 오픈소스SW에서 기술만큼 중요한 것이 커뮤니케이션이다. 온화한 커뮤니케이션은 더 강력한 커뮤니티를 형성한다. 강력한 커뮤니티는 다시 기술력 향상의 밑거름이 되어, 오픈소스SW가 성장하는 선순환의 고리를 만든다.

이뿐만 아니라 [오픈소스SW 공개 가이드 - 기업 편: 공개만 하면 끝인가요? 그 이후에 해야 할 일](#공개만-하면-끝인가요-그-이후에-해야-할-일) 에서 나열한 일에도 관심을 가질 것을 추천한다. 오픈소스SW를 가장 잘 설명할 수 있는 사람은 결국 개발한 사람이기 때문이다. 다만 이 모든 일을 메인테이너 혼자 지기에는 부담이 크다. 그렇기 때문에 커뮤니티를 잘 형성해야 한다. 커뮤니티가 메인테이너를 대신해 오픈소스SW 프로젝트를 바깥에 더 널리 알리는 역할을 하게 된다.

