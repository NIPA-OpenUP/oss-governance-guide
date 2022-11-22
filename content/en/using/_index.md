---
title: "오픈소스 사용하기"
linkTitle: "1. 사용하기"
weight: 20
description: >
   
---

## 배경

### 기업이 바라보는 오픈소스
2022년 RedHat은 전 세계 IT 리더 1296명을 대상으로 한 인터뷰 결과를 발표했다. 이 [오픈소스 Enterprise 현황 보고서 (2022)](https://www.redhat.com/en/resources/state-of-enterprise-open-source-report-2022)[^redhat2022]에 따르면 오픈소스 사용이 증가함에 따라 엔터프라이즈 소프트웨어 시장에서 점차 독점 소프트웨어 사용이 감소하고 있다는 것을 확인할 수 있다. 앞으로 독점 소프트웨어 사용이 향후 2년 동안 현재 45%에서 37%로 8%나 줄어들 것으로 전망하고 있으며, 같은 기간 동안 엔터프라이즈 오픈소스와 커뮤니티 기반 오픈 소스는 각각 5%, 3% 증가할 것으로 예상한다. 또한 IT 리더의 80%는 조직의 새로운 기술을 위한 엔터프라이즈 오픈 소스 소프트웨어 사용이 증가할 것이라고 답했다.

[^redhat2022]: 오픈소스 Enterprise 현황 보고서 (2022) : https://www.redhat.com/en/resources/state-of-enterprise-open-source-report-2022

Gartner는 [오픈소스 소프트웨어 하이프 사이클 보고서 (2016)](https://www.gartner.com/en/documents/3371817/hype-cycle-for-open-source-software-2016)[^gartner2016]에서 ‘주류 IT 조직의 95%는 사실을 인지하고 있는지를 떠나서 적지 않은 오픈소스 소프트웨어 자산을 활용하고 있다’라고 보고하기도 했다.

[^gartner2016]: 오픈소스 소프트웨어 하이프 사이클 보고서 (2016) : https://www.gartner.com/en/documents/3371817/hype-cycle-for-open-source-software-2016

### 국내 기업들의 오픈소스 도입 현황
#### 오픈소스 도입 현황
오픈소스 도입 현황을 조사한 한국 IDG의 [오픈소스, 기업 IT에 안착하다 (2020)](https://www.itworld.co.kr/techlibrary/144662)[^itworld144662]보고서에 따르면 국내 기업들의 오픈소스 도입 또한 이미 확산되었음을 확인할 수 있다. 운영체제와 데이터베이스에 오픈소스를 사용하고 있다는 응답이 40%이며, 오픈소스 도입을 고려하고 있다는 답변도 20%나 나왔다. 전체 응답자의 95%가 오픈소스를 IT 기업 환경에 적용하거나 적용하려고 시도하고 있다는 것을 알 수 있다.

[^itworld144662]: 오픈소스, 기업 IT에 안착하다 (2020) : https://www.itworld.co.kr/techlibrary/144662

[2021년 국내 기업의 공개SW 활용률은 61.5%](https://www.nipa.kr/main/selectBbsNttView.do?key=113&bbsNo=9&nttNo=8859)인 것으로 나타났다. 세부적으로는 전사적 활용 비율이 전년 10.7%에서 26.4%로 크게 증가했으며, 부분적 활용 비율은 35.1% 이다.

{{< imgproc opensource-company Fit "768x768" >}}
<center><i>[국내 기업 오픈소스 도입 및 활용]</i><center>
{{< /imgproc >}}


#### 국내 오픈소스 시장 현황
현재 국내 기업들의 오픈소스 전환 움직임은 주로 기술 지원 서비스를 보유한 상업적 버전에 초점이 맞춰져 있으나, 앞으로는 [커뮤니티 버전의 범위가 훨씬 커질 것으로 전망](https://www.itworld.co.kr/techlibrary/139540)[^itworld-139540]이 된다. 다음에서 나열하는 커뮤니티 버전 오픈소스가 대표적이며, 이들은 기업이 클라우드, 마이크로서비스, 인공지능, 빅데이터 등 비즈니스 전략을 수립하는 데 있어서 매우 중요한 역할을 하고 있다.

[^itworld-139540]: 커뮤니티 버전의 범위가 훨씬 커질 것으로 전망 : https://www.itworld.co.kr/techlibrary/139540


- [도커(Docker)](https://www.docker.com)[^docker]
- [쿠버네티스(Kubernetes)](https://kubernetes.io)[^kubernetes]
- [아파치 톰캣(Apache Tomcat)](http://tomcat.apache.org)[^tomcat]
- [아파치 HTTP 서버(Apache HTTP Server)](https://httpd.apache.org)[^http]
- [마리아DB(Maria DB)](https://mariadb.org)[^mariadb]
- [몽고DB(Mongo DB)](https://www.mongodb.com)[^mongodb]
- [젠킨스(Jenkins)](https://www.jenkins.io)[^jenkins]
- [아파치 스파크(Apache Spark)](http://spark.apache.org)[^spark]

[^docker]: 도커(Docker : https://www.docker.com
[^kubernetes]: 쿠버네티스(Kubernetes) : https://kubernetes.io
[^tomcat]: 아파치 톰캣(Apache Tomcat) : http://tomcat.apache.org
[^http]: 아파치 HTTP 서버(Apache HTTP Server) : https://httpd.apache.org
[^mariadb]: 마리아DB(Maria DB) : https://mariadb.org
[^mongodb]: 몽고DB(Mongo DB) : https://www.mongodb.com
[^jenkins]: 젠킨스(Jenkins) : https://www.jenkins.io
[^spark]: 아파치 스파크(Apache Spark) : http://spark.apache.org

국내 오픈소스 시장은 [2021년 OSS 시장규모는 2020년 대비 6.6% 성장한 3,032억 원이고, OSS 시장가치는 2020년 대비 6.1% 성장한 약 7조 원](https://www.nipa.kr/main/selectBbsNttView.do?key=113&bbsNo=9&nttNo=8859)[^kdb-633]으로 성장하고 있다.

[^kdb-633]: Nipa, 2021 오픈소스SW(OSS) 실태조사 보고서 https://www.nipa.kr/main/selectBbsNttView.do?key=113&bbsNo=9&nttNo=8859


### 오픈소스 도입 이유
해를 거듭할수록 기업들은 점점 더 많은 오픈소스를 도입하고 있다. 기업들이 오픈소스를 도입하게 된 이유로는 비용 절감이 가장 크다. 독점 소프트웨어를 사용하면 라이선스 비용이 계속 발생하며, 벤더에 종속되는 문제가 있다. 또한 독점 소프트웨어는 오픈소스보다 시장이나 기술의 변화에 빠르게 대응하지 못하는 경우가 많다. 따라서 오픈소스가 소프트웨어의 기능, 품질, 보안 면에서 독점 소프트웨어보다 더 나은 것으로 인식되고 있다. 그 외에도 최신 기술 확보, IT 기술 역량 강화, 경쟁력 강화, 시장 확대 및 인재 확보 등 그 이유가 다양하게 나타난다. 결과적으로는 오픈소스가 총 소유 비용(TCO) 감소뿐만 아니라 다른 여러 측면에서도 유리하다. 그렇다면 각각의 오픈소스 도입 이유에 대해 더 자세히 살펴보자. 

#### 비용 절감
일반적으로 오픈소스는 권리자인 저작권자가 라이선스를 통해 이용을 허락한 것이며, [OSI(Open Source Initiative)](https://opensource.org)[^osi]에서 인증한 오픈소스 라이선스들은 모두 상업적 이용을 제한하지 않는다. 라이선스 의무 사항만 준수하면 기업은 비용을 지불하지 않고 자유롭게 오픈소스를 사용할 수 있다. 그리고 오픈소스는 완성된 패키지 형태로 제공되기도 하는데 종종 누구나 자유롭게 사용 가능한 커뮤니티 버전과 과금 정책이 포함된 엔터프라이즈 버전이 따로 존재하기도 한다. 엔터프라이즈 버전은 프리미엄 기능이나 보안 패치, 기술 지원 등을 통한 차별화 전략을 사용하기에 기업은 사용 환경에 따라 적절히 선택할 수 있다.

[^osi]: OSI(Open Source Initiative) : https://opensource.org


#### 최신 기술
오픈소스는 전 세계의 누구나 조건 없이 참여 가능하며, 급변하는 기술의 변화에 민첩하게 대응하다 보니 최신 기술이 자연스럽게 집약된다. 최근에는 클라우드 환경을 기반으로 하는 오픈소스, AI 관련 오픈소스들이 인기를 얻어 많이 등장하고 있다. 기업들은 최신 오픈소스를 적극적으로 도입하여 사내 개발자들에게 사용을 권장하고 최신 기술력을 확보하는 데 힘쓰고 있다.

#### 안정성

오픈소스는 독점 소프트웨어보다 안정적이라고 평가받는다. 그 이유는 다음과 같다. 

- 이슈를 발견하고 해결해 나가는 주기가 빠르다: 오픈소스는 코드가 공개되어 있으므로 해커가 보안 취약점 및 약점을 찾기가 더 쉽다는 주장도 있지만 실제로는 수많은 기여자에 의해 더 빨리 발견될 가능성이 크다. 커뮤니티가 활성화된 오픈소스일수록 이슈가 발생했을 때 더 빠르게 개선이 이루어진다.
- 패치와 신규 버전 배포가 빠르다: 오픈소스에서 취약점이 보고되면 심각도가 높은 이슈면 빠르면 하루나 이틀 이내에도 수정 사항이 배포된다. 반면에 독점 소프트웨어는 업데이트 주기가 길고 대응이 늦을 수밖에 없다. 독점 소프트웨어는 개발 인력이 제한적이라 소프트웨어의 우선순위를 지정하여 패치가 이뤄지고, 보통 6개월에서 길게는 12개월의 배포 주기를 갖게 된다. 즉 벤더의 스케줄에만 의존하는, 자기 결정권의 부재 상태를 맞을 수 있다.
- 독점 소프트웨어의 상당 부분도 이미 오픈소스를 사용 중이다: 독점 소프트웨어 개발기업가 사용 중인 오픈소스의 보안 이슈를 제대로 추적하고 관리하지 않으면 버그 및 취약점이 포함된 상태로 배포될 가능성이 크다. 또한, 개선되었다 하더라도 실제 배포까지는 오랜 시간이 걸린다.

#### 역량 강화
오픈소스는 수많은 개발자의 손을 거쳐 높은 품질의 소스 코드와 아키텍처를 가지게 된다. 이는 기존 코드에만 익숙한 개발자들에게 시각의 변화를 주거나 새로운 기술을 습득할 수 있는 기회가 된다. 그뿐만 아니라 보편적 기능은 오픈소스로 대체하고 개발자는 비즈니스 로직 개발에 집중할 수 있는 환경을 만들 수 있기 때문에 오픈소스의 사용은 성공적으로 프로젝트를 완성하기 위한 필수 요건이 되어가고 있다.

#### 생산성의 증가
개발 프레임워크부터 모니터링, 테스트 자동화, 부하 테스트, 빌드, 배포까지 개발 프로젝트를 수행하는 과정 전체에서 오픈소스를 적극적으로 도입하게 되면 부서별로 각자 따로 개발할 필요가 없고, 코드 중복도 최소화할 수 있다. 이렇게 얻어진 효율성은 조금 더 혁신적인 기술에 투자할 여력을 만들어 준다.

#### 시장 확대
국내 소프트웨어 기업의 글로벌 진출은 현실적으로 매우 어렵다. 하지만 소스 코드를 공개하면 사용자를 전 세계에서 확보할 수 있고, 안정성, 보안성, 지속적 발전 가능성이라는 오픈소스라는 긍정적인 기대감이 소프트웨어의 가치를 높일 수 있다. 그 때문에 이전보다 사업을 글로벌로 확장할 기회를 훨씬 더 많이 창출할 수 있다.

#### 인재 확보
독점 소프트웨어를 사용하게 될 경우, 해당 소프트웨어 개발 경력이 있는 인재를 확보하는데 상당한 어려움이 따른다. 하지만 오픈소스의 경우에는 누구나 접근 가능한 코드이기 때문에 더욱 많은 인력 풀을 대상으로 인재를 확보할 기회가 늘어난다. 기존 직원들에게는 오픈소스 교육을 하는 기업이 늘어나고 있으며, 이제는 단순히 오픈소스를 사용하는 것뿐만 아니라 오픈소스에 직접 참여하고 [오픈소스 역량을 가진 오픈소스 전문가 고용을 고려한다는 인사담당자가 늘어 가는 추세](https://training.linuxfoundation.org/resources/2020-open-source-jobs-report)[^training-resource]이다.

[^training-resource]: 2020 Open Source Jobs Report : https://training.linuxfoundation.org/resources/2020-open-source-jobs-report/


### 오픈소스 도입 시 고려사항
Gartner의 [Technology Insight for Software Composition Analysis (2019) 보고서](https://www.gartner.com/en/documents/3971011/technology-insight-for-software-composition-analysis)[^gartner-3971011]에서는 기업은 오픈소스를 도입할 때 고려해야 할 사항으로 크게 4가지를 꼽고 있다. (1) 오픈소스가 장기적으로 생존할 가능성이 큰가? (2) 보안 이슈는 없는가? (3) 벤더 이슈는 없는가? (4) 컴플라이언스 및 지식재산권 확인 이다. 이 밖에도 오픈소스가 우리의 제품 또는 서비스에 적합한 기술인지, 오픈소스를 도입했을 때 충분한 기술 지원을 받을 수 있는지 등도 확인해야 한다. 검토 사항 중 일부를 조금 더 자세히 살펴본다. 

[^gartner-3971011]: Technology Insight for Software Composition Analysis (2019) 보고서 : https://www.gartner.com/en/documents/3971011/technology-insight-for-software-composition-analysis



#### 보안
오픈소스 도입 시 오픈소스가 과연 안전한지 검토해야 한다. 오픈소스는 코드가 공개되어 있으므로 공격자가 공개된 코드를 통해 결함을 발견하고 악의적인 공격을 할 수 있다. 보통 취약점이 발견되면 심각한 정도에 따라 우선순위가 정해져서 심각한 취약점은 신속하게 보안 패치가 이뤄지는 편이다. 따라서 사용하고자 하는 오픈소스 버전에 보고된 취약점이 있는지 확인해보는 것이 필요하며, 보안 취약점이 얼마나 자주 보고되고, 신속하게 대응을 잘하고 있는지 등도 살펴보고 오픈소스를 도입하는 것이 안전하다. 오픈소스 도입 이후에도 지속해서 오픈소스 취약점 현황을 모니터링하고 패치가 이루어져야 하며, 보안 취약점 현황을 알려주는 도구들이 시중에 상당수 존재하므로 도입 여부를 검토해보는 것을 추천한다. 자세한 내용은 뒤에 나올 [`오픈소스 관리 도구 소개`](#오픈소스-관리-도구-소개)를 참고할 수 있다.

#### 오픈소스 기술 지원
내부 인력만으로도 오픈소스의 도입과 지속적인 관리가 가능한지 검토해야 한다. 이를 위해서 내부 기술력이 뒷받침되어야 한다. 그렇지 아니한 경우에는 기술지원 서비스가 제공되는 엔터프라이즈 오픈소스를 도입할 수 있다. 엔터프라이즈 오픈소스를 도입할 경우에는 어느 수준까지 기술 지원을 받을 수 있는지도 확인이 필요하다.

#### 오픈소스 커뮤니티
오픈소스는 특정 단체가 관리하기도 하고, 개인 혹은 기업이 관리하기도 한다. 따라서 오픈소스를 운영하는 방식도 다양하므로 사전에 꼼꼼히 체크해야 향후 발생할 수 있는 리스크를 최소화할 수 있다. 얼마나 많은 사용자를 보유하고 있는지, 업데이트는 자주 이뤄지는지, 이슈가 발생했을 때 대응은 신속하게 이뤄지고 있는지 등 따져봐야 한다. 자세한 내용은 [`오픈소스 선택 가이드`](#오픈소스-선택-가이드) 편에서 다뤄질 예정이다.

#### 컴플라이언스, 지식재산권

오픈소스에도 독점 소프트웨어와 마찬가지로 저작권 등 지식재산권이 있다. 오픈소스 저작권자는 라이선스를 통해 오픈소스를 사용하는데 지켜야 할 의무 사항을 명시한다. 자유로운 복제 및 배포 및 수정의 허용은 모든 오픈소스에 동일하게 적용된다. GPL과 같은 라이선스는 오픈소스를 사용하게 되면 소프트웨어를 배포할 때 추가되거나 수정된 소스 코드를 모두 공개하도록 요구하기도 한다. 오픈소스 라이선스를 미리 파악하고 의무 사항을 준수해야 한다. 자세한 내용은 [`오픈소스를 사용하고 관리하기`](#오픈소스를-사용하고-관리하기) 편에서 다뤄질 예정이다.

#### 호환성
오픈소스가 기업에 적합한지 따져보려면 먼저 현재 기업 내 IT 시스템에 대한 충분한 파악이 선행되어야 한다. 현재 시스템의 아키텍처와 현황 등을 문서화하고 오픈소스를 도입했을 때 이슈가 될 부분은 없는지 확인이 되어야 한다. 또한 케이스에 따라 장기적으로 계획을 세워 점진적으로 도입해야 할 수도 있다.


---

이제는 기업이 선택적으로 오픈소스 사용 여부를 결정하는 것이 아니라 소프트웨어 개발의 필수 요소가 되었다. 따라서 이후에서는 기업에서 오픈소스를 어떻게 올바르게 선택하고 사용하는지에 대한 가이드를 제시하고자 한다.



## 오픈소스 사용 가이드 - 기업 편

오픈소스에 의존하는 정도가 증가함에 따라 기업은 어떻게 하면 올바르게 오픈소스를 사용할 수 있는지 지속해서 고민하고 정책을 수립해야 하며 이를 실무에 반영해야 한다. 오픈소스에 적용되는 라이선스의 종류는 매우 다양하며 조건에 따라 지켜야 할 의무사항도 라이선스마다 다르다. 따라서 기업은 사용하고 있는 오픈소스를 추적 관리하고, 오픈소스 라이선스 의무 사항을 준수할 책임이 있다. 이번 장에서는 기업이 오픈소스를 사용할 때 필요한 관리와 그 과정 전반에 대해 알아본다.


### 오픈소스를 사용하고 관리하기
오픈소스 라이선스를 관리하는 것은 독점 소프트웨어의 라이선스를 관리하는 것만큼 중요하다. 실제로 오픈소스 라이선스를 위반한 기업을 상대로 많은 소송이 제기되고 있다. 2017년 미국 연방 법원에서 있었던 [GPL이 법적 계약이라고 판결한 사례](https://www.linux.com/topic/open-source/artifex-v-hancom-open-source-now-enforceable-contract)[^hancom]가 그 한 예이다. 이처럼 기업 입장에서는 오픈소스 라이선스를 제대로 관리하지 않는다면 분명 큰 리스크로 다가올 것이다.

[^hancom]: Linux.com, Artifex v. Hancom: Open Source is Now an Enforceable Contract : https://www.linux.com/topic/open-source/artifex-v-hancom-open-source-now-enforceable-contract


### 오픈소스 컴플라이언스
#### 오픈소스 컴플라이언스의 정의

{{% alert color="success" %}}

<i>“Open source compliance is the process by which users, integrators and developers of open source software observe copyright notices and satisfy license obligations for their open source software components”  
— The Linux Foundation</i>

{{% /alert %}}

오픈소스 컴플라이언스란, 오픈소스를 사용하고 개발하는 사람들이 오픈소스의 저작권을 존중하기 위해서 오픈소스의 라이선스 의무를 이행하는 과정이다. 종종 조직에서는 오픈소스 라이선스 컴플라이언스를 성가시다고 여긴다. 물론, 모든 라이선스를 식별하고 각각의 라이선스 의무를 준수한다는 것은 어려운 작업이다. 하지만 오픈소스가 고갈되지 않고 유지될 수 있도록 보장하는 것은 오픈소스를 활용하는 기업이 맡은 책임의 일부이기도 하다. 규정을 준수하기 위한 노력을 통해 기업은 오픈소스를 사용하면서 발생할 수 있는 비용과 위험을 이해하기도 하며, 결과적으로는 오픈소스를 더 잘 이해하고 사용할 수 있게 된다. 

오픈소스 컴플라이언스의 범위를 보면 단순히 기업 내에서의 사용하는 것뿐만 아니라 3rd party 공급자와 소프트웨어 공급 및 수급 계약을 하면서 발생하게 될 오픈소스 라이선스 의무사항을 준수하는 활동도 포함된다. 이런 활동들은 오픈소스 커뮤니티와 존중과 신뢰를 바탕으로 한 관계를 구축하는 기반이 되기도 한다. 궁극적으로는 오픈소스 컴플라이언스는 저작권자의 지식재산권을 보호하는 데에 그 목적이 있다는 것을 기억해야 한다.

{{< imgproc compliancerange Fit "768x768" >}}
<center><i>[오픈소스 컴플라이언스 범위]</i><center>
{{< /imgproc >}}



> 참고로, 지난 2020년 12월, 오픈소스 컴플라이언스에 대한 국제 표준이 ISO에 등록되었다. 
> 
> [ISO/IEC 5230](https://www.iso.org/standard/81039.html)[^iso5230]은 기업이 오픈소스 컴플라이언스를 달성하기 위해 수행해야 할 최소한의 요구사항을 정의하고 있다. NIPA에서 출간한 기업 공개소프트웨어 거버넌스 OpenChain 해설서에서는 이에 대한 자세한 내용 및 준수 방법을 설명한다. 
> 
> 가이드는 다음 페이지에서 다운받을 수 있다. : https://www.oss.kr/oss_guide/show/7050bff0-d06b-43f0-99a6-9975afcd486f

[^iso5230]: ISO/IEC 5230 : https://www.iso.org/standard/81039.html


#### 오픈소스 컴플라이언스 프로세스
기업은 오픈소스 라이선스 의무사항을 준수할 수 있도록 오픈소스의 사용, 기여, 감사 및 배포에 이르는 일련의 과정을 관리/감독해야 한다. 검증 단계까지 전반적인 내용을 체크 리스트를 작성하여, 일관성을 보장하고 검증 단계를 간과하지 않도록 하는 것이 중요하다. 여기서는 일반적인 오픈소스 컴플라이언스 프로세스를 소개하고 단계별 주요 내용을 설명한다.

{{< imgproc compliance-process Fit "768x768" >}}
<center><i>[오픈소스 컴플라이언스 프로세스]</i><center>
{{< /imgproc >}}


##### **1. 오픈소스 라이브러리 식별**
프로젝트에 사용된 오픈소스를 식별하고 목록을 도출하는 단계이다. 모든 오픈소스 컴포넌트가 식별되어야 하며, 오픈소스 원본의 위치와 라이선스 정보 등도 함께 기록이 되어야 한다. 자동화된 스캐닝 도구를 통해 식별하는 것을 권장한다. 자동화된 스캐닝 도구는 [주요 오픈소스 관리 도구 소개](#주요-오픈소스-관리-도구-소개)에서 자세히 다룬다. 스캔은 배포 시점이나 변동 사항이 있을 때, 개발자의 요청이 있을 때, 혹은 주기적으로 수행할 수 있다.

##### **2. 소스 코드 감사**
코드 레벨의 스캔을 수행하여 아직 식별되지 않은 오픈소스를 추가로 더 찾아내는 단계이다. 코드 스캐닝 도구는 오픈소스의 코드를 기반으로 개발 언어가 바뀌었거나 함수명, 변수명이 변경되었더라도 식별이 되어야 하며, 기존 코드와 비교를 통해 수동으로 확인하는 과정을 거친다.

##### **3. 이슈 확인 및 해결**
도출된 오픈소스 목록에서 이슈가 있는지 파악하고 해결하는 단계이다. 이슈가 발견되었을 경우에는 해당 오픈소스를 다른 것으로 대체하거나 제거하는 작업이 필요하기 때문에 개발 부서와의 긴밀한 협의가 필요하다. 코드를 수정한 이후에는 다시 스캔 과정으로 돌아가 이슈가 해결되었는지 정확히 확인해야 한다.

#####  **4. 아키텍처 리뷰**
프로젝트 전반의 아키텍처 리뷰를 진행한다. 오픈소스마다 결합 방식에 따라 준수해야 할 의무사항이 다르기 때문이다. 오픈소스 코드뿐만 아니라 독점 코드, 상용 코드 확인을 한다. 또한, 코드들의 의존성 및 결합 방식을 검토한다.

#####  **5. 승인**
이전 단계들이 모두 완료되었는지 확인하며, 검토 결과를 토대로 오픈소스 책임자는 이 단계에서 오픈소스의 사용을 승인하거나 거절한다. 승인된 오픈소스와 관련 정보들은 취합 후 등록하여 중앙에서 관리한다.

#####  **6. 고지**
오픈소스를 포함한 프로그램을 배포하는, 즉 오픈소스를 재배포하는 형태에서는 기본적으로 저작권과 라이선스 정보를 포함한 내용을 고지할 의무가 발생한다. 고지문은 일반적으로 NOTICE라는 이름의 파일로 작성한다. 이에 포함할 내용은 사용된 오픈소스의 명칭, 오픈소스에 접근할 수 있는 URL, 라이선스 원문, 저작권 표기 등이 있다. GPL과 같이 소스 코드 공개의 의무가 발생하는 경우에는 소스 코드를 받는 방법도 함께 기재한다.

##### **7. 검증**
배포한 패키지를 확인하여 고지문이 정상적으로 제공되었는지 최종적으로 확인한다.

### 라이선스 의무사항
#### 오픈소스 배포
오픈소스 라이선스의 의무 사항은 배포하는 시점에 발생한다. 여기서 배포란 소스 코드 또는 바이너리의 복사본을 다른 사람에게 제공하는 행위를 의미한다. 앱스토어 배포, 판매, 3rd party 제공, 코드 공개 등이 배포에 해당한다. 개인적으로 사용하거나 외부에 제공하지 않고 사내 도구로만 사용하는 경우는 배포에 해당하지 않는다.

#### 오픈소스 라이선스 공통 의무사항
오픈소스 라이선스는 오픈소스 저작자의 권리를 존중하기 위해 공통으로 네 가지의 의무 사항을 기본으로 둔다. 오픈소스 사용자는 저작권을 고지해야 하고, 라이선스 사본을 포함해야 한다. 오픈소스 사용 시 보증은 제공되지 않으며, 오픈소스 사용으로 인해 발생한 손해에 대해서도 책임을 지지 않는다.  

{{< imgproc common-right Fit "768x768" >}}
<center><i>[오픈소스 라이선스 공통 의무사항]</i><center>
{{< /imgproc >}}


### 오픈소스 라이선스 컴플라이언스 실행
#### 사용 중인 오픈소스를 추적해야 하는 이유
기업이 효과적으로 오픈소스를 활용하기 위해서는 제품별, 버전별 사용한 오픈소스 현황을 추적하여 관리해야 한다. 그 이유와 목적은 다음과 같다.

##### **오픈소스 목록 관리**
오픈소스를 효율적으로 관리하고 조직의 정책을 준수하기 위해서는 오픈소스 목록을 관리해야 한다.


##### **라이선스 확인**
사용 중인 오픈소스의 라이선스 파악을 통해 라이선스의 의무 사항을 확인하고 준수하여야 한다. 모든 오픈소스 라이선스가 호환되는 것이 아니다. 라이선스의 의무사항 및 조건들은 충돌할 수 있다. 조직 내 모든 오픈소스 라이선스 규정 준수 요구사항을 충족하는지 확인하는 유일한 방법은 오픈소스 라이선스를 식별하고 추적하는 것이다.


##### **취약점 파악**
오픈소스는 악의적인 공격자에게 타깃이 된다. 특히 엔터프라이즈 오픈소스는 더 많은 공격의 대상이 된다. 이때 오픈소스 목록을 확보하지 않는다면, 소프트웨어 내에 사용 중인 오픈소스가 알려진 취약점이 있는지 알지 못하게 되어 알려진 취약점을 수정할 수 없게 된다.


##### **패치 및 버전 업데이트**
오픈소스는 기능 개선 및 버그 수정을 위하여 지속해서 업데이트가 이뤄진다. 오픈소스 목록을 관리하여 중요 패치 또는 버전 업데이트를 놓치지 말아야 한다.

#### 오픈소스 목록 수동 관리
오픈소스 목록을 관리하는 방법으로는 수동 방식과 자동 방식이 있다. 수동 방식은 개발자 또는 오픈소스 관리자가 모든 오픈소스 사용 현황을 직접 파악하는 방법이다. 수동으로 관리하는 경우 몇 가지 문제가 발생한다.
##### **오픈소스 파악의 어려움**
소스 코드 수준에서 사용된 오픈소스까지 일일이 파악하는 것은 매우 힘든 작업이다. 오픈소스 코드를 그대로 가져다 쓰거나 혹은 오픈소스를 수정하여 사용하게 되면, 일부 제한된 라이선스에서는 오픈소스를 사용하는 모든 프로젝트의 소스 코드를 공개해야 할 수도 있다. 또한 오픈소스 목록에서 누락이 된다면 추후 개선되는 패치나 버그 수정도 불가능하게 되며 오픈소스에 취약점이 발견되어도 파악이 힘들어진다.

##### **사용된 오픈소스 목록 누락**
사용 파악 시 미처 확인하지 못한 누락이 발생할 수 있다. 프로젝트 규모가 커질수록, 그 대상이 많아질수록 직접 오픈소스 파악하기는 어려워진다. 또한 개발이 진행되고, 배포까지 최종 단계에 이르기까지 수많은 변경 작업이 일어난다. 이 과정에서 사용된 오픈소스 목록과 실제 코드에 포함된 오픈소스를 완전히 똑같이 맞추기는 어려울 것이다. 현실적으로도 이러한 변경 사항을 추적하는 데 있어 상당히 많은 노력과 시간이 소모되기도 한다.

##### **배포 프로세스 지연**
어플리케이션 개발과 배포에 영향을 줄 수 있다. 오픈소스 목록을 수동으로 관리하게 되면 승인 프로세스도 수동으로 수행되어 매우 느리게 진행될 가능성이 크다. 이미 통합된 오픈소스 중 이슈가 발생하게 되면 해당 오픈소스를 제거하고 대안을 찾도록 개발자에게 요구해야 할 수도 있는데 이렇게 되면 일정에 큰 차질을 빚게 될 것이다.

#### 오픈소스 목록 관리의 자동화
위에서 언급한 것처럼 여러 측면에서 오픈소스 관리는 자동화가 필요하다. 자동화를 위해서는 아래와 같은 오픈소스를 식별하기 위한 적절한 도구를 구축하거나 도입하여 사용해야 한다.
- 코드 레벨에서 사용 중인 오픈소스를 찾아내며 비교를 제공하는 소스 코드 스캐너
- 오픈소스 라이브러리 파일을 찾아내는 파일 스캐너
- 오픈소스를 패키지 단위로 가져오는 패키지 매니저 분석 도구
- 라이선스와 컴플라이언스 항목 및 리소스를 추적하기 위한 컴플라이언스 관리 도구
- 라이선스 결합 방식 분석 도구
- 오픈소스 BOM(Bill of Materials, 사용된 소프트웨어의 ) 관리 도구
- 전반적으로 프로젝트를 관리하고 오픈소스 목록을 관리할 포탈


### 오픈소스 목록 관리와 SBOM

오픈소스 목록 관리의 중요성은 2021년 5월 미 행정명령 ([Executive Order 14028 of May 12, 2021](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity)[^order-14028])에서도 알 수 있다. 미 정부는 국가 사이버 보안 강화의 일환으로 SBOM(Software Bill of Materials) 제출을 의무화 하였다. SBOM은 위에서 설명한 오픈소스 목록과 유사한 개념이며, NITA(미 전기통신 및 정보청)[^nita]는 이 행정 명령에 따라 [SBOM의 최소 요구 사항](https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf)[^minimum_element]을 정의하였다. 미 연방 정부가 가진 지배적 지위를 고려하면 이러한 요구 사항은 SBOM의 표준이 될 가능성이 크다고 볼 수 있다. 

[^order-14028]: Executive Order 14028 of May 12, 2021 : https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity
[^nita]: National Telecommunications and Information Administration
[^minimum_element]: Department of Commerce, The Minimum Elements for an SBOM, 2021, https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf

#### SBOM 최소 요구 사항

NITA는 라이선스 및 보안취약점 관리를 위해 SBOM이 갖춰야 할 다음 세가지의 요구 사항을 제시하였다. 
1. 데이터 필드 : SBOM이 포함해야 할 데이터 (다음 단락에서 세부 내용 설명)
2. 자동화 지원 : SBOM 생성 자동화
  - SBOM는 인간이 읽을 수 있어야 하고 동시에 기계 판독이 가능하여야 한다. 
  - SBOM가 자동으로 생성되는 환경을 지원해야 한다. 
3. Practice와 절차 : SBOM 생성 및 운영 방법을 정의해야 한다.

#### 데이터 필드

NITA는 SBOM이 포함해야 하는 7가지 데이터 필드를 명시하였다. 

| Data Field   |      Description      |
|:----------|:-------------|
| 공급자 이름 |  구성요소를 만들고 정의하고 식별하는 주체의 이름 |
| 구성요소 이름 | 최초 공급자에 의해 정의된 소프트웨어 단위의 명칭 |
| 구성요소 버전 | 공급자가 이전에 식별된 소프트웨어 버전으로부터의 변경을 명시하기 위해 사용하는 식별자 |
| 기타 고유 식별자 | 구성요소를 식별하는 데 사용되거나 관련 데이터베이스를 위한 조회 키 역할을 하는 기타 식별자 |
| 종속성 관계 | 업스트림 구성요소 X가 소프트웨어 Y에 포함된다는 관계의 명시 |
| SBOM 데이터 작성자 | 이 구성요소에 대한 SBOM 데이터를 만든 주체의 이름 |
| 타임스탬프 | SBOM 데이터 어셈블리의 날짜 및 시간 기록 |

그리고 이러한 데이터 필드를 포함하는 SBOM은 기계가 판독(Machine Readable)하도록 다음 세가지 표준화된 형식 중 하나로 작성되어야 한다. 
* [SPDX](https://spdx.org/)
* [CycloneDX](https://cyclonedx.org/)
* [SWID Tags](https://nvd.nist.gov/products/swid)

이 중 SPDX 표준에 대해서 좀 더 자세히 살펴보자. 

#### SPDX

여기서는 Linux Foundation의 프로젝트인 SPDX에서 만든 SPDX 표준과 SPDX 문서 작성 방법에 대해 알아보겠다. SPDX 표준은 2021년 9월 ISO 표준([ISO/IEC 5962](https://www.iso.org/standard/81870.html))[^isoiec5962]으로 등록된 대표적인 SBOM 포맷이다. 기업의 SBOM 관리 체계가 모든 포맷의 SBOM을 지원하면 좋겠지만, 하나의 포맷을 선택해야 한다면 국제 표준인 SPDX를 먼저 지원하는 것을 권장한다. 더불어 SPDX는 당초 오픈소스 라이선스 컴플라이언스를 위해 만들어진 포맷이기에 기업의 오픈소스 라이선스 관리에 효율적으로 사용할 수 있다. 

[^isoiec5962]: ISO/IEC 5962 : https://www.iso.org/standard/81870.html 

SPDX 표준은 2022년 9월 현재 v2.3까지 나왔으며 다음과 같은 정보를 포함한다. 

{{< imgproc spdx-info Fit "512x512" >}}
<center><i>[SPDX v2.3 format]</i><center>
{{< /imgproc >}}


SPDX는 소프트웨어가 포함하고 있는 패키지, 파일, 스니핏(코드 조각) 등에 대한 각각의 라이선스, 버전, 저작권 등의 정보를 관리할 수 있다. 또한 SPDX는 자동으로 정보를 읽고 쓸 수 있도록 JSON, YAML 등 프로그래밍 언어로 쉽게 조작할 수 있도록 광범위하게 사용되는 데이터 포맷을 채택하였다. 현재 아래의 네가지 포맷을 지원한다. 

- [JSON](https://github.com/spdx/spdx-spec/blob/development/v2.2.2/examples/SPDXJSONExample-v2.2.spdx.json)[^spdx-json]
- [YAML](https://github.com/spdx/spdx-spec/blob/development/v2.2.2/examples/SPDXYAMLExample-2.2.spdx.yaml)[^spdx-yaml]
- [Tag/Value](https://github.com/spdx/spdx-spec/blob/development/v2.2.2/examples/SPDXTagExample-v2.2.spdx)[^spdx-tagvalue]
- [RDF/xml](https://github.com/spdx/spdx-spec/blob/development/v2.2.2/examples/SPDXRdfExample-v2.2.spdx.rdf.xml)[^spdx-rdfxml]

[^spdx-json]: JSON SPDX sample : https://github.com/spdx/spdx-spec/blob/development/v2.2.2/examples/SPDXJSONExample-v2.2.spdx.json
[^spdx-yaml]: YAML SPDX sample : https://github.com/spdx/spdx-spec/blob/development/v2.2.2/examples/SPDXYAMLExample-2.2.spdx.yaml
[^spdx-tagvalue]: Tag/Value SPDX sample : https://github.com/spdx/spdx-spec/blob/development/v2.2.2/examples/SPDXTagExample-v2.2.spdx
[^spdx-rdfxml]: RDF/xml SPDX sample : https://github.com/spdx/spdx-spec/blob/development/v2.2.2/examples/SPDXRdfExample-v2.2.spdx.rdf.xml

그런데, SPDX 규격은 100 페이지가 넘는 적지 않은 분량의 문서이기 때문에 처음 SPDX 표준에 맞추어 문서를 작성하는건 쉽지 않다. SPDX 프로젝트는 Excel로 작성된 SBOM을 SPDX 문서로 자동 변환하는 도구를 제공하고 있다. 즉, 사용자는 먼저 SPDX 프로젝트에서 제공하는 [Excel template 파일](https://github.com/spdx/tools/blob/master/Examples/SPDXRdfExample-v2.1.xls)[^spdx-excel]을 다운받아서 각 시트에 필요한 정보를 기입한다. 

[^spdx-excel]: SPDX 엑셀 파일 : https://github.com/spdx/tools/blob/master/Examples/SPDXRdfExample-v2.1.xls

{{< imgproc spdx-excel Fit "1024x768" >}}
<center><i>[SPDX가 제공하는 Excel 파일 캡쳐]</i><center>
{{< /imgproc >}}

그리고, 이 Excel 파일을 SPDX에서 제공하는 도구를 사용하면 SPDX가 지원하는 데이터 포맷인 JSON, YAML 등의 데이터 포맷으로 변환할 수 있다. 간단하게는 [SPDX Online Tool 웹사이트](https://tools.spdx.org/app/convert/)[^spdx-online]에서 원하는 형태의 데이터 포맷으로 쉽게 변환할 수 있다.

{{< imgproc spdx-web Fit "1024x768" >}}
<center><i>[SPDX Online Tool - Convert to other SPDX format]</i><center>
{{< /imgproc >}}

[^spdx-online]: SPDX Online Tool : https://tools.spdx.org/app/convert/ 

위에서 설명한 SBOM 최소 요구사항에 의하면 SBOM은 자동으로 생성되는 환경이어야 한다. 지금까지 설명한 SPDX 문서를 만드는 방법은 사람이 Excel 파일을 작성하고, 이를 온라인에서 SPDX 형태로 컨버팅을 수동으로 수행하는 방식이기 때문에 이런 절차를 자동화하는 노력이 필요하다. SPDX는 다양한 [Tool](https://spdx.dev/spdx-tools/)[^spdx-tools]을 제공하여 프로그래밍적으로 SPDX 문서를 생성할 수 있는 방법을 제공한다. 기업은 소프트웨어 빌드 프로세스에서 자동으로 SBOM을 생성하고, SPDX 형태의 SBOM 문서를 생성할 수 있는 환경을 갖추어야 한다.

[^spdx-tools]: SPDX Community Tools : https://spdx.dev/spdx-tools/

### 오픈소스 관리 도구 소개
앞서 언급한 것처럼 오픈소스 사용에 따른 의무사항 준수와 위험 요소 확인을 위해서는 SDLC(Software System Development Life Cycle) 전체에서 지속적인 스캔 및 모니터링이 필요하다. 이에 **SCA(Software Composition Analysis)** 라는 오픈소스 관리 도구들이 생겨났다. SCA는 보안 및 라이선스 규정 준수를 발견하고 관리하기 위한 자동화된 프로세스를 제공한다.

#### 오픈소스 관리 도구를 선택하는 기준
Gartner의 [Technology Insight for Software Composition Analysis](https://www.gartner.com/en/documents/3971011/technology-insight-for-software-composition-analysis)[^gartner-3971011]보고서에서 SCA 도구 선택 기준이 제시되는데 아래와 같다.
- [x] 충분한 취약점 데이터베이스가 마련되었는가?
- [x] IDE 및 Repository 연동, 코드 커밋 전 오픈소스 평가 기능 등 개발자 지원이 잘 되어 있는가?
- [x] 모든 라이선스를 추적하고 보고하는 기능이 있는가?
- [x] 라이선스 정책을 자동을 설정할 수 있는가?
- [x] 취약점을 빠르게 감지하고 우선순위를 결정하는가?
- [x] 라이선스, 저작권, 버전 관리 등 관련 정보를 포함한 보고서 발급 기능이 있는가?

[^gartner-3971011]: Gartner, Technology Insight for Software Composition Analysis (2019) : https://www.gartner.com/en/documents/3971011/technology-insight-for-software-composition-analysis

#### 주요 오픈소스 관리 도구 소개

##### **FOSSology** - https://www.fossology.org

{{< imgproc fossology Fit "384x384" >}}
{{< /imgproc >}}

소스 코드 스캐닝 도구로 소스 파일 상단의 문구를 스캔하여 라이선스를 자동으로 확인한다. FOSSology의 자세한 설치 및 사용 방법은 다음 사이트를 참고할 수 있다.  
https://openchain-project.github.io/OpenChain-KWG/guide/appendix/3-tools/fossology

##### **SW360** - https://www.eclipse.org/sw360

{{< imgproc SW360 Fit "384x384" >}}
{{< /imgproc >}}

소프트웨어에 포함된 구성요소를 관리하기 위한 도구이다. 오픈소스를 포함하는 제품을 개발하고 배포하는 기업이라면 각 제품과 릴리스 버전마다 사용한 오픈소스의 버전, 라이선스 등의 정보를 수집하고 추적해야 한다. 이를 통해 기업은 올바른 오픈소스 컴플라이언스 활동을 수행할 수 있다. SW360은 오픈소스 정보를 추적하기 위한 도구이다. SW360의 자세한 설치 및 사용 방법은 다음 사이트를 참고할 수 있다.  
https://openchain-project.github.io/OpenChain-KWG/guide/appendix/3-tools/sw360

##### **SPDX** - https://spdx.dev

{{< imgproc SPDX Fit "384x384" >}}
{{< /imgproc >}}

SPDX(Software Package Data  소프트웨어 정보 교환 방식을 표준화하고 이를 용이하게 하기 위한 도구를 제공한다.

##### **FOSSLight** - https://fosslight.org/

{{< imgproc logo-fosslight Fit "384x384" >}}
{{< /imgproc >}}

LG전자는 [FOSSLight 오픈소스 Project](https://fosslight.org/)[^fosslight]로 FOSSLight Hub와 FOSSLight Scanner를 공개했다. **FOSSLight Hub**는 오픈소스, 라이선스, 그리고 보안취약점까지 관리해줌으로써 오픈 소스 소프트웨어 사용 시 Compliance를 준수하고 보안취약점으로부터 안전하게 사용할 수 있도록 해준다. 또한 프로젝트 별 BOM 관리, 라이선스의 의무사항 및 보안취약점 조회 기능을 제공하여 OSC(Open Source Compliance) Process를 수행할 수 있도록 도와준다. **FOSSLight Scanner**는 Dependency, 소스 코드, 바이너리로부터 오픈소스 정보를 스캔하는 도구이다.  

[^fosslight]: FOSSLight : https://fosslight.org/

##### **Olive (Kakao)** - https://olive.kakao.com

{{< imgproc logo-olive Fit "384x384" >}}
{{< /imgproc >}}

Kakao는 자사의 수많은 프로젝트의 오픈소스 관리를 위해 사용하던 시스템을 누구나 사용할 수 있도록 [Olive Platform](https://olive.kakao.com)[^olive] Beta를 무료로 오픈했다. Olive는 Github 프로젝트를 분석하여 사용한 오픈소스 데이터를 관리하고, 라이선스 및 의무사항을 확인하여 Report를 제공한다. 쉽고, 빠르고 정확한 오픈소스 검증을 목표로 직관적인 기능과 UI로 구성되어 있으며, 간단히 Dependency와 라이선스 확인이 가능한 심플 체크 기능 등 사용자 편의에 초점을 맞추고 있다.

[^olive]: Kakao, Olive Platform : https://olive.kakao.com

##### **Fossa** - https://fossa.com

{{< imgproc logo-fossa Fit "384x384" >}}
{{< /imgproc >}}

2015년 설립된 실리콘밸리 스타트업에서 제공하는 서비스로, 풍부한 오픈소스 메타데이터 및 정교한 정책 거버넌스를 제공한다. CI/CD 통합 등 DevOps 환경을 지원하며 개발자 친화적 기능들로 구성되어 있다. Twitter, Uber, Zendesk 등과 파트너를 맺고 있으며, JS Foundation, Linux Foundation, NPM 등과 제휴하고 있다. 기본적인 사용은 무료이나 일부 추가 기능들을 유료로 제공하며, 팀 규모가 100명 이상이라면 엔터프라이즈 버전이 적용된다.

##### **FOSSID** - https://fossid.com/

{{< imgproc logo-fossid Fit "384x384" >}}
{{< /imgproc >}}

2016년 스웨덴에서 설립된 FOSSID는 오픈소스 라이선스 및 보안 취약점 관리를 위한 솔루션이다. 소스 코드 내 오픈소스 콤포넌트를 탐지하고, 각 콤포넌트의 라이선스 및 보안 취약점을 식별한다. 방대한 오픈소스 DB 및 자동 데이터 수집 기술, AI를 통한 향상된 탐지 성능 등 특징을 갖고 있다. 특히, 코드 일부에서 보안 취약점을 탐지하는 유일한 오픈소스 스캐너라는 장점이 있다. 

##### **Black Duck** - https://www.blackducksoftware.com/

{{< imgproc logo-blackduck Fit "384x384" >}}
{{< /imgproc >}}

Black Duck은 오픈소스를 사용하는 동안 발생하는 라이선스와 취약점, 소스 코드 품질 관리를 위한 포괄적인 솔루션이다. 전반적인 소프트웨어의 공급망과 애플리케이션 라이프사이클 전반에 거쳐 오픈소스의 라이선스와 보안을 관리한다. 정확도를 높이고 오탐을 줄이기 위해 오픈 소스 검색에 다각적 접근 방식을 취하여 신뢰성 있는 BOM을 생성한다. 


##### **Snyk** - https://snyk.io

{{< imgproc logo-snyk Fit "384x384" >}}
{{< /imgproc >}}

오픈소스 라이선스 취약점 관리를 위한 서비스를 제공하다가 2020년부터 라이선스 준수 관리 기능이 추가되었다. Dependency Tree 뷰어, 이슈 우선순위 선별 시스템, 런타임 모니터링 등 기능을 제공하며, 전담 보안 연구팀이 리뷰를 진행한다. 현재 Docker 공식 독점 보안 파트너로 IBM Cloud, RedHat, OpenShift, Kubernetes 등과 제휴를 맺고 있다. 무료로 사용할 수 있지만 팀 규모와 프리미엄 기능에 따라 유료 Plan이 세부적으로 마련되어 있다.

##### **WhiteSource** - https://www.whitesourcesoftware.com

{{< imgproc logo-whitesource Fit "384x384" >}}
{{< /imgproc >}}

2011년 설립되어 라이선스 준수 및 취약점 관리 서비스를 제공하며, 오래된 서비스인 만큼 방대한 데이터베이스를 확보하고 있다. 110억 개 이상의 소스 코드 파일, 200개 이상의 언어지원, 1억 개 이상의 라이브러리를 확보하고 있다. 컨테이너 및 서비리스 등 모든 환경을 지원하며 현재 Microsoft Azure DevOps 서비스로도 제공되고 있다. GitHub의 Ultimate에서 사용 가능한 옵션으로 제공되고 있으며 GitHub Package도 지원한다. WhiteSource도 기본적인 사용은 무료이며, 팀 규모가 20명을 넘어가면 유료로 사용 가능하며, 추가 프리미엄 기능을 제공한다.

##### **CodeEye** - https://www.olis.or.kr/codeEye/introduction.do

{{< imgproc logo-codeeye Fit "384x384" >}}
{{< /imgproc >}}

CodeEye는 오픈소스 라이선스 비교·분석·검사를 위해 사람이 해야 할 수작업(Eye Checking)을 원활하게 수행하거나 도움을 주는 시스템으로 오픈소스 사용 시 준수 해야 할 라이선스(GNU GPL 등) 내용을 효과적으로 검사하여 보여준다. 한국저작권위원회에서 구축한 오픈소스 DB(지속적 Update)를 기반으로 검사하며, 중소기업기본법 시행령 제3조(중소기업의 범위) 규정에 따른 중소기업 대상으로 무료로 서비스한다. 

##### **Clarity** - http://insignary.com/

{{< imgproc logo-insignary Fit "384x384" >}}
{{< /imgproc >}}

Clarity는 바이너리 코드 분석을 통한 오픈소스 관리 솔루션으로, 바이너리 코드를 스캐닝하여 소프트웨어 내에 존재하는 오픈소스 컴포넌트를 식별하고 해당 오픈소스의 라이선스 및 보안 취약점 정보를 제공한다. 기업은 클래리티의 바이너리 코드 점검을 통해 라이선스 위반에 대한 법적 이슈와 오픈소스 보안 취약점을 사전에 방지하여
외부에서 공급되는 소프트웨어를 안전하게 활용할 수 있다.

##### **LABRADOR** - https://www.iotcube.com/

{{< imgproc logo-labrador Fit "384x384" >}}
{{< /imgproc >}}

LABRADOR는 R&D 및 공급망에서 오픈소스 취약점 및 라이선스 이슈를 분석하고 수정하기 위해 제작되었다. 단순 취약점의 나열에 그치지 않고 한발 더 나아가 수정을 위한 다양한 방안을 제시한다. 이를 통해 기업은 취약한 구성 요소를 식별하고 수정할 뿐 아니라 추후 문제의 여지가 있는 라이선스에 대한 사전 조치가 가능하다. 함수 단위 소스 취약점 분석으로 더 빠르고 정확한 진단이 가능합니다.

##### **ClearlyDefined** - https://clearlydefined.io

{{< imgproc ClearyDefined Fit "384x384" >}}
{{< /imgproc >}}

ClearlyDefined는 오픈소스 데이터베이스를 제공하여 사용자가 오픈소스의 출처, 라이선스 등의 정보를 확인할 수 있게 한다. 또한 정보의 오류가 있다면 사용자가 자발적으로 데이터를 개선할 수 있게 하여 커뮤니티 기반의 신뢰성 있는 오픈소스 데이터베이스 구축을 가능하게 한다.


### 오픈소스 고지 의무사항
오픈소스 라이선스는 공통으로 저작권 고지와 라이선스 사본 첨부 의무를 갖는다. 따라서 오픈소스를 사용하였다면, 해당 오픈소스의 저작권과 라이선스 사본을 고지하여 의무사항을 준수해야 한다. 여기서는 고지문과 관련된 내용을 살펴보도록 한다.

#### 고지 항목

##### 저작권 고지

소스 코드의 저작권 고지는 일반적으로 "copyright" 라는 단어를 포함하여 연도와 저작권자 혹은 회사명을 포함하는 문장열로 이루어진다. 이러한 고지는 저작물에 대한 저작권이 있음을 잠재적인 사용자에게 알려 주게 하며, 저작권 소유자를 식별하는데 필요하다. 오픈소스에 따라 저작권자뿐만 아니라 특허가 있으면, 특허 소유자, 오픈소스 기여자들을 표시하기도 한다. 연도는 일반적으로 최초 게시된 연도를 의미하며, 저작권 보호 기간을 결정하는데 사용될 수 있도록 저작권 기간을 의미하기도 한다.    

```
Copyright (C) year1, year2, year3 저작권 보유자
```

##### 라이선스 고지 (사본 첨부)

많은 오픈소스 라이선스는 사용한 오픈소스의 라이선스를 명시하고 라이선스 사본을 첨부하여, 오픈소스 사용자들이 오픈소스에 관한 권리를 잘 이해할 수 있도록 제공하도록 요구하고 있다.


{{% alert title="Apache License (예)" color="success" %}}

1. You must give any other recipients of the Work or Derivative Works a copy of this License.  

   저작물이나 파생 저작물을 양도받는 모든 사람에게 본 라이선스의 사본을 제공해야 한다.

{{% /alert %}}



##### 수정 내용 고지

Apache 2.0, MPL, GPL 2.0, GPL 3.0 등의 라이선스는 소스 코드 수정 시 수정내용을 고지할 것을 요구한다. 수정한 사람, 수정 일자 등 수정에 관한 내용도 포함하도록 함으로써 원본과 구별이 되어야 한다.  

{{% alert title="Apache License (예)" color="success" %}}

2. You must cause any modified files to carry prominent notices stating that You changed the files.  

   수정된 파일에 대해서는 수정을 했다는 사실을 설명하는 명확한 안내문구를 첨부해야 한다.

{{% /alert %}}


#### 고지 방법
오픈소스 사용시 고지의무는 라이선스에 따라 고지 방법이 세부적으로 나와 있기도 하다. 대표적인 라이선스인 Apache 2.0의 경우, LICENSE와 NOTICE 파일을 두고, 라이선스 및 저작권 고지 등의 고지사항을 포함할 것을 안내하고 있다.

##### Apache Royale 프로젝트[^royale]의 예

[^royale]: Apache Royale 프로젝트https://infra.apache.org/licensing-howto.html

~~~
Apache Royale  
Copyright 2020 The Apache Software Foundation  

This product includes software developed at  
The Apache Software Foundation (http://www.apache.org/).  

The Initial Developer of some parts of the framework, which are copied from, derived from, or  
inspired by Adobe Flex (via Apache Flex), is Adobe Systems Incorporated (http://www.adobe.com/).  
Copyright 2003 - 2012 Adobe Systems Incorporated. All Rights Reserved.  

The Initial Developer of the examples/mxroyale/tourdeflexmodules,  
is Adobe Systems Incorporated (http://www.adobe.com/).  
Copyright 2009 - 2013 Adobe Systems Incorporated. All Rights Reserved.  
 
The ping sound effect (ping.mp3) in  
examples/mxroyale/tourdeflexmodules/src/mx/effects/assets  
was created by CameronMusic. (http://www.freesound.org/people/cameronmusic/sounds/138420/)  
~~~


##### Apache Hive 프로젝트[^hive]의 예    

[^hive]: Apache Hive 프로젝트 : https://github.com/apache/hive

###### 1. NOTICE
~~~
Apache Hive  
Copyright 2008-2018 The Apache Software Foundation  
  
This product includes software developed by The Apache Software  
Foundation (http://www.apache.org/).  
  
This project includes software licensed under the JSON license.  
~~~

###### 2. LICENSE : Pointer 방식으로 고지  
~~~
For the SQLLine package:  

Copyright (c) 2002, 2003, 2004, 2005 Marc Prud'hommeaux  
From: http://sqlline.sourceforge.net/#license  
"SQLLine is distributed under the BSD License, meaning that you are free to redistribute, modify, or sell the software with almost no restrictions."  

Statement from Marc Prud'hommeaux regarding inconsistent licenses in some SQLLine source files:  

SQLLine was once GPL, but it was changed to be BSD a few years back.  
Any references to the GPL are vestigial. Hopefully the license  
declaration at http://sqlline.sourceforge.net/#license is sufficiently  
authoritative in this regard.  
~~~

###### 3. /binary-package-licenses/ : 바이너리 파일에 포함된 오픈소스 라이선스와 저작권 고지


##### 카카오톡[^kakaotalk]의 예

[^kakaotalk]: 카카오톡 : https://www.kakaocorp.com/service/KakaoTalk

{{< imgproc kakaoNotice Fit "768x768" >}}
<center><i>Kakao Notice</i></center>
{{< /imgproc >}}


##### LG전자[^lge]의 예

[^lge]: LG전자 : https://opensource.lge.com

{{< imgproc lgNotice Fit "768x768" >}}
<center><i>LG전자 Notice</i></center>
{{< /imgproc >}}

### 오픈소스의 보안 취약점
#### 오픈소스의 보안 취약점 현황
Sonatype의 [소프트웨어 공급망 현황(2021)](https://www.sonatype.com/resources/state-of-the-software-supply-chain-2021)[^sonatype2021]에 따르면 소프트웨어 공급망 공격도 작년보다 650%나 증가하였으며, 인기있는 상위 10%의 오픈소스 프로젝트에서 취약점을 포함할 가능성이 평균 29%이다. 가장 일반적인 공격 유형은 Typosquatting 이며, 이는 오픈소스를 검색할 때 단순한 오타를 유도하는 공격 방식으로 개발자가 "lodash"의 이름을 가진 오픈소스를 사용하려고 할 때 "lodahs"와 같은 유사한 이름의 악성 컴포넌트를 미리 등록해두어 설치하게 만드는 방식이다. 또 다른 방식으로는 프로젝트 관리자로부터 자격 증명을 가로채 악성 코드를 심는 방식 등 다양한 수단을 통해 이뤄지고 있다.

[^sonatype2021]: Sonatype, State of the Software Supply Chain Report (2021) : https://www.sonatype.com/resources/state-of-the-software-supply-chain-2021

특히 소프트웨어 공급망을 통해 공격이 증가하는 이유는 하나의 오픈소스가 다른 많은 오픈소스를 포함하는 종속 관계로 구성되어 있다 보니 실제 프로젝트에서 사용되는 오픈소스는 엄청난 수의 의존성을 가진 오픈소스를 사용하게 되어 전체를 파악하기가 힘든 점이 있다. 그리고 오픈소스 정신은 **신뢰하는 공유**에 기반을 두고 있다 보니 이것은 공격자가 쉽게 접근할 수 있게 하는 토대가 되기도 한다.

#### 오픈소스의 보안 취약점 사례
최근 오픈소스를 통한 취약점 사례를 살펴보면, 2020년 5월 "Octpus Scanner" 26개의 오픈소스 패키지에 악성 코드가 삽입되어 멀웨어를 전파하고 백도어를 심었다. 4월에는 RubyGems 에서도 "typosquatting" 및 "crypto" 마이닝 멀웨어 등이 발견되어 현재는 제거된 상태이다. 그리고 npm 패키지를 통한 공격도 있었는데 2월에 1337qq-js npm 패키지는 설치 스크립트와 UNIX 시스템만을 대상으로 하드 코딩된 암호나 API 액세스 토큰 등 민감한 정보를 빼낸 사례도 있었다.

#### 오픈소스의 보안 취약점 조치
그렇다면 이러한 취약점이 발견되었을 때 오픈소스는 얼마나 빠르게 대처할까?

보고서를 보면 보통은 1일 ~ 1주 이내가 35%로 제일 많았으나 여기서 주목해야 할 점은 1주 이상 소요되거나 아예 고쳐지지 않는 케이스가 무려 51%나 된다는 것이다. 오픈소스 커뮤니티의 신속한 대응도 중요하지만, 해당 오픈소스 사용처에서도 바로 적용해야 하는 이슈도 존재한다. 또한, 공격자는 문제가 되는 오픈소스 버전이 배포된 후 3일 이내에 오픈소스 취약점을 악용한 것으로 제일 많이 나타나므로 더 빠른 조치가 필요한 상황이다.

#### 취약점 데이터베이스
보통 오픈소스의 취약점 내용과 이루어진 버전 정보들은 수집되어 [CVE](https://cve.mitre.org)[^cve]와 같은 오픈소스 취약점 데이터베이스에 저장이 된다. 다양한 유형의 취약점 정보가 포함되는데 주요 데이터베이스는 아래와 같다.

[^cve]: CVE : https://cve.mitre.org

##### Mitre의 CVE(Common Vulnerabilities and Exposures - https://cve.mitre.org
상용 애플리케이션 및 비공개 소스 프로젝트를 비롯하여 다양한 유형의 취약점에 대한 정보를 제공한다. 취약점 정보는 개별 CVE 번호가 부여되어 관리된다.
- 예) CVE-2015-5211 에 대한 CVE 정보

{{< imgproc cve Fit "768x768" >}}
{{< /imgproc >}}

##### Sonatype OSS Index - https://ossindex.sonatype.org
Maven, npm, Go, Pypi 등 여러 유형의 Package Management 에서 보고된 오픈소스 취약점 정보 데이터베이스를 제공한다.
- 예) CVE-2015-5211 에 대한 OSS Index 정보

{{< imgproc sonatype-oss-index Fit "768x768" >}}
{{< /imgproc >}}


### DevSecOps
2012년 Gartner는 "DevOpsSec: Creating the Agile Triangle"[^devopsset] 이란 보고서를 통해 DevOps 이니셔티브에 보안 기반을 구축할 필요가 있다는 사실을 강조하기 위해 DevSecOps라는 개념을 소개했다. DevSecOps는 소프트웨어 개발<sub>Development</sub>과 운영<sub>Operation</sub>, 보안<sub>Security</sub>의 합성어로 애플리케이션 개발자와, 운영, 보안 실무자 간의 소통과 협업, 통합을 강조하는 개발문화를 의미한다.

[^devopsset]: DevOpsSec: Creating the Agile Triangle : https://www.gartner.com/en/documents/1896617/devopssec-creating-the-agile-triangle

{{< imgproc devsecops Fit "768x768" >}}
<center><i>DevSecOps (이미지 출처 https://www.redhat.com/ko/topics/devops/what-is-devsecops)</i></center>
{{< /imgproc >}}



SDLC<sub>Software System Development Life Cycle)</sub> 전체에 걸쳐 가능한 빨리, 그리고 자주 보안이 통합되도록 해야 한다. 오늘날 일반적인 애플리케이션에는 오픈소스 코드가 60~80% 포함된다는 점을 고려할 때 DevSecOps에서 중요한 것은 오픈소스 취약점에 대한 고려일 것이다. DevSecOps 전체에서 오픈소스 취약점을 추적하고 사용자에게 알려주는 것은 매우 중요하다.

컨테이너 및 마이크로서비스와 같은 혁신적인 기술로 업데이트하면서도 분리된 팀들 간에 긴밀하게 협업하도록 하기는 쉽지 않은 일이다. IBM에서 제시한 [모범 사례 (2020)](https://developer.ibm.com/recipes/tutorials/open-source-security-trends-for-2020)[^bestpractive2020]를 통해 DevSecOps 관점에서 본 오픈소스 취약점 관리에 대해 좀 더 알아보자.

[^bestpractive2020]: IBM, Open Source Security Trends (2020) : https://developer.ibm.com/recipes/tutorials/open-source-security-trends-for-2020

#### IBM DevSecOps 모범 사례
##### **자산 추적**
먼저 보호가 필요한 자산에 대해 알아야 한다. 오픈소스를 식별하고 추적을 통해 어떤 자산이 중요한지 파악하는 데 도움이 된다.


##### **위협 평가 수행**
이 단계에서는 예상되는 위협 유형을 평가한다. 가능한 공격 방법과 구현할 수 있는 보안 조치의 실행 가능성을 평가한다.


##### **보안 체크리스트**
명확한 실천 체계를 수립하여 일상 업무에서 쉽게 규정을 지킬 수 있게 한다. 이렇게 하면 패치를 쉽게 적용할 수 있어서 보안 격차를 줄일 수 있다.


##### **가능한 자동화**
오픈소스 가시성을 높일 수 있는 애플리케이션 보안 테스트 및 오픈소스 보안 솔루션이 있다. [SonarQube](https://www.sonarqube.org)[^sonarqube] 같은 모니터링 도구를 사용하면 오픈소스 구성요소를 추적하여 버그와 결함을 실시간으로 탐지할 수 있다.

[^sonarqube]: SonarQube : https://www.sonarqube.org

##### **보안 우선 문화 구축**
유관 부서 전반에 걸쳐 보안을 적용하고 개발프로세스의 모든 단계에 보안 사항을 관리하는 데 집중해야 한다. DevOps 전반에 Security를 결합한 DevSecOps 모델을 채택하면 보안 우선의 문화를 구축하는 데 도움이 된다.


##### **컨테이너 보안 모범 사례 적용**
컨테이너화는 자체적인 운영체제를 고려할 때 보안상의 이점이 있다.


##### **모든 것을 암호화**
모든 데이터에 암호화를 적용한다.


#### GitHub 기능을 활용한 보안 관리 사례
GiHub은 소스 코드 저장소로 널리 사용되고 있는데, 최근 [GitHub Octoverse (2021)](https://octoverse.github.com)[^github-octoverse] 자료를 보면, **Fortune 100대 기업 중 84%가 GitHub Enterprise를 사용**하고 있다고 한다. 그에 맞춰 최근 GitHub에서도 단순히 소스 코드 저장소 기능을 넘어 새로운 기능들을 추가하고 있는데, 특히 보안과 관련된 다양한 기능을 제공하고 있어 주목을 받고 있다. 이러한 보안 기능들을 활용한 보안 관리 사례를 살펴보고자 한다.

[^github-octoverse]: GitHub Octoverse (2021) : https://octoverse.github.com

##### **Dependency Graph**
프로젝트에서 사용 중인 외부 라이브러리 정보를 보여주는 기능이다. 사용 중인 라이브러리와 라이브러리 버전 정보들을 조회할 수 있다. Ruby, Javascript, Python 등 다양한 언어와 패키지 매니저를 지원한다. Dependency Graph 는 사용 중인 것뿐만 아니라 자신의 프로젝트를 참조하고 있는 다른 프로젝트도 확인할 수 있다.

{{< imgproc dependency-graph Fit "768x768" >}}
{{< /imgproc >}}

##### **dependabot**
프로젝트에서 사용 중인 오픈소스 중 오래된 버전이 있다면 PR(Pull Request)를 추가해 준다. 개발자는 변경된 릴리즈 정보를 검토하여 새로운 버전 을 머지(Merge) 할 수 있게 한다.

{{< imgproc dependabot Fit "768x768" >}}
{{< /imgproc >}}


##### **코드 스캐닝**
코드 스캐닝은 GitHub 네이티브 환경으로 제공된다. 코드 스캔이 활성화되면 모든 'git push'에서 새로운 잠재적 보안 취약점이 스캔 되고 결과는 풀 요청에 직접 표시된다. 코드 스캐닝은 세계에서 가장 진보된 시맨틱 분석 엔진인 CodeQL을 사용하는데, 이는 실제 취약점을 발견하는 최고의 기록을 가지고 있다. 오픈소스 코드 스캔은 무료로 제공되고 있다.

{{< imgproc code-scanning Fit "768x768" >}}
{{< /imgproc >}}


##### **Secret 스캐닝**
GitHub Private Repository와 Enterprise 버전에 추가된 기능으로 코드 내 Secret 코드를 스캔하는 기능이다. 소스 코드에 포함되어 노출되면 민감한 코드 정보들을 찾아내어 실수로 커밋 된 자격 증명의 부정 사용을 방지한다. 일치하는 Secret 포맷이 발견되면 지정된 HTTP 주소로 payload가 전달된다.

{{< imgproc secret-scanning Fit "768x768" >}}
{{< /imgproc >}}


---

여기까지 오픈소스 사용하는 데 있어 기업이 활용할 수 있는 가이드를 알아보았다. 이제 개발자는 어떻게 오픈소스를 사용하고 관리해야 하는지에 대해 알아보자.


## 오픈소스 사용 가이드 - 개발자 편

오픈소스는 생태계는 매년 그 규모가 매우 빠르게 발전하고 있다. 
오픈소스 거버넌스 플랫폼을 운영하는 Sonatype 에서 최근 발표한 [소프트웨어 공급망 현황(2021)](https://www.sonatype.com/resources/state-of-the-software-supply-chain-2021)[^sonatype-report]에 따르면 오픈소스 공급은 상위 4개 오픈 소스 생태계(Java, Javascript, Python, .NET)에서만 3천7백만개 이상의 컴포넌트와 패키지가 포함되어 있다.
또한, 2021년에 전 세계 개발자의 오픈 소스 패키지 다운로드 수가 2조 2천억 개 이상이며, 이는 전년 대비 73% 증가한 수치이다.
****
이처럼 수많은 오픈소스가 생겨나면서 오픈소스를 선택하는 폭도 그만큼 넓어졌다. 이번 장에서는 오픈소스를 올바르게 선택하는 방법에 관한 내용을 알아보고자 한다.

### 오픈소스 생태계의 이해
오픈소스 선택에 관한 내용에 앞서 오픈소스 생태계를 이해할 필요가 있다. 오픈소스 생태계의 구성은 크게 생산자, 공급자와 소비자로 나뉘는데 생산자는 오픈소스 커뮤니티 및 재단, 그리고 오픈소스 기여자 등으로 구성된다. 공급자로는 소프트웨어 인프라 공급자, 교육 및 컨설팅 기업, 기술지원 기업 등이 있다. 소비자로는 일반 사용자와 오픈소스를 활용하는 조직이 해당한다.

#### 오픈소스 생태계 구성

{{< imgproc opensouece-ecosystem Fit "768x768" >}}
<center>[오픈소스 생태계]</center>
{{< /imgproc >}}

##### **생산자**
- **오픈소스 커뮤니티** : 오픈소스 생태계에서 허브 역할
- **오픈소스 재단** : 오픈소스 커뮤니티와 상용 오픈소스 밴더 사이에서 공동 작업을 지원
- **오픈소스 기여자** : 오픈소스를 개발하고 다양한 오픈소스 이슈를 처리하는 개발자

##### **공급자**
- **소프트웨어 인프라 공급자** : 오픈소스 공급망 제공
- **교육 및 컨설팅 기업** : 오픈소스 프로젝트를 중심으로 비즈니스 생태계 조성
- **기술 지원 기업** : 오픈소스 커뮤니티와 협력 관계를 유지하며 오픈소스를 지원하기 위한 기술 인력을 운영

##### **소비자**
- **일반 사용자** : 오픈소스를 사용하고, 커뮤니티를 통해 오픈소스의 개선에 참여
- **오픈소스 유료 사용자** : 유료 서비스를 통해 차별화된 지원을 받는 사용자 또는 조직


#### 오픈소스 커뮤니티
오픈소스 커뮤니티의 구성은 양파 구조에 비유를 많이 하게 되는데, 프로젝트 리더(또는 창시자)와 핵심 기여자, 기여자, 신입 기여자, 사용자로 구성된다. 이 중 프로젝트 리더는 오픈소스 프로젝트 전반적인 사항에 대해 최종 의사 결정을 내린다. 핵심 기여자는 프로젝트에서 경험이 제일 많은 실력자이며, 커뮤니티 구성원들을 지도하거나 멘토링을 하게 된다. 그 외 자세한 내용은 오픈소스 기여하기 편에서 다루기로 한다.

#### 오픈소스 재단
오픈소스 생태계에는 다양한 오픈소스 재단이 존재한다. 오픈소스 이니셔티브(OSI, Open Source Initiative)의 앨리슨 랜달 회장은 "기업들이 신뢰할 수 있는 비영리 독립 단체를 통해 오픈소스 프로젝트를 공동 추진할 수 있다고 생각함에 따라 재단 설립이 증가하고 있다. 이는 아주 중요한 의미를 지닌다. 경쟁 관계에 있는 기업들이 협력할 경우 통상 많은 장애물은 만나게 된다. 중립적이면서도 경쟁적이지 않은 재단을 매개체로 삼는 방법이 아주 유용할 수 있다"라고 설명했다.

몇 가지 주요 오픈소스 재단은 아래와 같다.
##### **OSI (Open Source Initiative)** - http://opensource.org/
이 조직은 1998년 Netscape에서 영감을 받아 시작되었으며, 오픈소스 소프트웨어 사용을 장려하기 위해 만들어진 단체이다. 현재는 OSI 라이선스 검토와 승인 등 OSD(Open Source Definition)을 관리하고 있다.


##### **Free Software Foundation** - https://www.fsf.org
오픈소스 분야에서 유명한 리차드 스톨만이 1985년에 설립한 재단으로 자유(Free) 소프트웨어의 생산과 보급을 장려하고 있다. 주로 컴퓨터 소프트웨어를 만들어 배포하고 수정하는 보편적인 자유를 추구한다.


##### **Linux Foundation** - https://linuxfoundation.org
리눅스의 성장을 지원하고 상업적 지원을 진행하고 있는 기술 컨소시엄이다. 최근에는 오픈소스 이벤트, 교육 및 인증, 오픈소스 프로젝트 지원 프로그램 등으로 영역을 확장하고 있다.


##### **Apache Software Foundation** - http://apache.org
1993년 Apache HTTP 개발자들에서 시작한 이 그룹은 전 세계 분산 개발자 커뮤니티로 발전하여, 다양한 오픈소스 프로젝트를 진행하고 있다. 그들이 개발하고 있는 소프트웨어는 아파치 라이선스로 배포된다. 재단의 목적 중 하나는 아파치 프로젝트에서 일하는 지원자들에 대한 법적 보호와 허가 없이 다른 조직에서 아파치 브랜드의 사용을 막는 데에 있다. 그리고 아파치 프로젝트와 관련된 기술과 아파치 개발자들이 함께 모이는 데에 초점을 맞춘 ApacheCon 콘퍼런스를 해마다 열고 있다.


##### **Cloud Foundry Foundation** - https://www.cloudfoundry.org/foundation/
클라우드 파운드리 재단은 클라우드 파운드리 오픈소스 프로젝트의 전 세계적인 인식 및 채택을 이끌고 기여자 공동체를 성장시키고, 프로젝트 성공을 위해 모든 파트너 기업들을 통해 전략 및 조치의 일관성을 구축하기 위해 존재한다. EMC, HP, IBM, 인텔, SAP가 공동 참여하고 있다.


### 오픈소스 라이선스
오픈소스는 저작권법에 따른 보호를 받는다. 오픈소스는 일반적으로 소스가 공개되어서 접근할 수 있으며 누구나 자유롭게 사용, 수정, 배포할 수 있다. 오픈소스는 라이선스는 해당 오픈소스를 사용하기 위해 사용자가 지켜야 할 의무 사항을 명시하고 있다. 이러한 의무 사항을 제대로 준수하지 않고 사용하면 저작권법 위반이 된다.

오픈소스 라이선스 중 GPL 라이선스의 경우에는 오픈소스를 사용하는 조건으로 수정하거나 추가된 모든 소스 코드를 공개해야 하는 의무 사항을 가지고 있다. 만약 상용 소프트웨어에서 코드 공개를 하지 않고 GPL 라이선스의 오픈소스를 사용하면 저작권법 위반으로 형사처벌을 받을 수도 있다.


#### 오픈소스 라이선스 구분
오픈소스 라이선스는 크게 permissive 라이선스와 copyleft 라이선스로 나눌 수 있다.

{{< imgproc license Fit "768x768" >}}
<center>[오픈소스 라이선스 구분]</center>
{{< /imgproc >}}


두 가지 라이선스의 특징을 요약하면 다음과 같다.

##### **permissive 라이선스**
- 고지 의무를 지키면 자유롭게 사용 가능
- 대표적인 라이선스: MIT, BSD, Apache 등

##### **copyleft 라이선스**
- 고지 의무 + 코드 공개 의무
- 사용한 오픈소스의 라이선스와 동일한 조건으로 배포 의무
- 대표적인 라이선스: GPL, LGPL, AGPL, MPL 등

오픈소스 라이선스에 대한 세부 사항은 NIPA에서 출간한 "오픈소스 라이선스 가이드" (링크)를 참고할 수 있다.


### 오픈소스 선택 가이드
수많은 오픈소스로 인해 요구 사항에 가장 적합한 오픈소스를 선택하기가 어려울 수 있다. 여기서 오픈소스 선택을 위한 기준을 몇 가지 제시해보고자 한다.

#### 오픈소스 선택 기준
##### **기능성**
자신의 프로젝트에서 필요한 기능을 충분히 충족할 수 있고 사용하기에 적합한지 따져봐야 한다. 예를 들어 메시지 큐 기능을 위한 오픈소스를 선택하는 데 있어서 기본 메세징 기능이 적합한지 확인하고, 업계에서 널리 사용되는 프로토콜과 호환이 되는지 확인해야 한다. 필요한 기능 이상으로 지나치게 과도한 기능을 제공하진 않는지도 중요하다. 예를 들어 단순히 문서  파일 포맷 변환이 필요한데 이미지, 영상 포맷까지 다양하게 제공하는 오픈소스라면 현재 필요하지 않은 기능 때문에 더 많은 용량이나 리소스를 차지할 수도 있다.
오픈소스가 프로젝트에서 요구하는 기능에 완벽하게 충족시키지 못한다면 필요한 추가 기능을 직접 수정하여 사용하는 것도 고려될 수 있다. 그러나 이 수정하게 되는 경우 오픈소스 기여와 변경에 따른 라이선스와 같은 다양한 내용을 살펴보고 진행해야 한다.


##### **오픈소스 사용 조건 및 성능**
오픈소스 사용 조건과 같은 비기능적인 부분도 반드시 살펴봐야 한다. 프로젝트에서 사용하는 아키텍처나 운영체제와 호환이 되어야 하고, 프로젝트가 현재 Linux 에서 작동하지만, Windows도 다음에 확장될 계획이라면 두 시스템 모두 지원하는 오픈소스여야 한다. 그리고 오픈소스의 성능이 조건에 충족하는지 살펴보고, 성능이 중요하다면 벤치마킹을 수행하여 성능을 반드시 측정해보아야 한다.


##### **라이선스**
오픈소스에 명시된 라이선스를 반드시 확인해야 한다. 상업용 프로젝트에 비상업용 라이선스를 가진 오픈소스를 사용하거나, GPL 라이선스를 가진 오픈소스를 사용하게 되어 의도하지 않게 자신의 코드를 전부 공개해야 하는 상황은 피해야 한다. 이 경우 Apache나 MIT와 같은 상대적으로 관대한 허용적 라이선스를 사용하는 오픈소스를 선택하는 것이 바람직하다.


##### **보안**
[소프트웨어 공급망 현황(2021)](https://www.sonatype.com/resources/state-of-the-software-supply-chain-2021)[^sonatype2021]를 보면 인기있는 상위 10%의 오픈소스 프로젝트에서 취약점을 포함할 가능성이 평균 29%이다. 오픈소스 검토 보안과 관련된 부분을 반드시 확인하고 사용해야 하며, 취약점이 발견되었을 때 빠르게 조치가 이뤄지고 있는지 등도 검토 대상이 되어야 한다. 오픈소스의 마지막 릴리즈가 오래되었다면, 그만큼 보안 취약점을 가지고 있을 가능성이 높다. GitHub 이슈 또는 오픈소스 설명에 명시된 이슈 트래커등을 통해 보안 문제가 있는지 확인하고, 지난 버전 릴리즈 노트를 살펴보자.

##### **인기도**
오픈소스가 GitHub 에서 관리 중이라면, Star 개수나 Watch, Fork 횟수 등으로 얼마나 많은 사용자가 오픈소스를 활용할 수 있는지 가늠해볼 수 있다. 그뿐만 아니라 오픈된 이슈 개수나 PR 수, 마지막 커밋 일시 등을 통해 얼마나 활발하게 오픈소스 개발이 이뤄지고 있고 계속 발전할 가능성이 얼마나 되는지 파악할 수 있다. 그 밖에도 해당 오픈소스와 관련된 StackOverflow 질문 수, 오픈소스 다운로드 수, Google 쿼리 결과 수 등과 같은 간단한 측정을 통해서 인기도를 확인해 볼 수 있다. 이러한 여러 지표를 측정하여 오픈소스 커뮤니티의 건강성을 측정하는 [CHAOSS](https://chaoss.community/metrics)[^chaoss] 와 같은 도구도 있다.
- Star 수
- 참조 횟수
- 오픈된 이슈 수
- 오픈된 PR 수
- 마지막 커밋일시
- 릴리즈 주기

[^chaoss]: CHAOSS : https://chaoss.community/metrics

##### **소스 코드**
오픈소스의 소스 코드와 코드의 품질도 중요하다. 프로젝트에서 사용 중이거나 익숙한 프로그래밍 언어로 작성된 오픈소스를 사용하는 것이 유리하다. 이는 오픈소스를 직접 수정하지 않더라도 이슈가 발생했을 때 디버깅을 하거나 원인을 파악하는 데 도움이 된다. 낮은 코드 품질의 오픈소스는 잠재적으로 버그, 보안 취약점, 성능 저하와 유지 관리 이슈를 갖고 있습니다. 코드 품질을 파악하는 방법으로는 세부적인 로직을 모르더라도 단위 테스트 코드가 포함되어 있는지, 메서드 또는 함수가 읽기 쉽게 명명되어 사용 중인지, 코딩 컨벤션은 올바르게 지켜지고 있는지 등을 참고하여 판단할 수 있다.


##### **문서화**
오픈소스 코드 품질과 더불어 문서화가 잘 되어 있는지 살펴보는 것도 중요하다. 설치 방법, 튜토리얼, 참조 설명서 등 문서화가 잘되어 있는 오픈소스는 그만큼 성숙한 오픈소스라고 볼 수 있다. 문서화가 잘되어 있으면 직접 오픈소스 코드를 보지 않더라도 세부적인 사용 방법도 손쉽게 파악할 수 있고 빠르고 다양하게 적용할 수 있어서 오픈소스 활용도도 그만큼 올라가게 된다.


#### 오픈소스 선택 체크리스트
- [x] 많이 쓰이고 있는 오픈소스인가?
- [x] 팀에서 오픈소스를 배우는데 어렵지는 않은가? (레퍼런스가 충분한가?)
- [x] 유지보수가 잘 되고 있는가?
- [x] 유사 오픈소스와의 차이점은 무엇인가? (얼마나 효율적인가?)
- [x] 쓰지 않는다면 어떤 문제가 생기는가?
- [x] 라이선스에는 문제가 없는가?
- [x] 커뮤니티는 활성화되어 있는가?

---

여기까지 오픈소스 사용하기에 대한 내용들을 살펴보았다. 기업에서 오픈소스를 도입할때 고려해야 할 사항들과 오픈소스 컴플라이언스, 그리고 라이선스 의무사항과 각종 오픈소스 관리도구 및 오픈소스 보안 취약점 등에 대해 다뤘다. 기업은 자칫 잘못된 오픈소스 사용으로 인해 기업 이미지에도 큰 타격을 줄 수도 있음을 기억해야 하며, 오픈소스 사용시 오픈소스 라이선스 의무사항을 준수하지 않아 발생하는 법적 리스크도 반드시 고려해야 한다. 이를 위해서는 전사 차원에서 오픈소스 정책과 프로세스를 수립하는 등 오픈소스를 올바르게 사용하기 위한 지속적인 노력을 기울여야 할 것이다.      

다음 장에서는 기업의 구성원이 외부 오픈소스 개발에 참여하고 직접 기여할 때 기업이 고려해야 할 사항들을 알아보도록 하겠다.
