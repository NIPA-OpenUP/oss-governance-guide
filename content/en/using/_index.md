---
title: "오픈소스 사용하기"
linkTitle: "1. 사용하기"
weight: 20
description: >
   
---

## 배경

### 기업이 바라보는 오픈소스

최근 기업들의 오픈소스에 대한 인식과 활용이 크게 변화하고 있다. Perforce Software의 [2024 State of Open Source Report](https://www.globalbankingandfinance.com/2024-state-of-open-source-report-shows-open-source-software-adoption-growing-despite-security-and-support-challenges/)[^perforce2024]에 따르면, 2023년 기업의 95%가 오픈소스 사용을 유지하거나 증가시켰으며, 33%는 사용이 크게 증가했다고 응답했다.

특히 주목할 만한 점은 비용 절감이 오픈소스 도입의 주요 이유로 부상했다는 것이다. 이는 이전 연도와 달리, 기업들이 '효율성의 해'라 불리는 2023년에 혁신을 희생하지 않으면서도 비용을 절감할 수 있는 방안으로 오픈소스를 선택했음을 시사한다.

[^perforce2024]: 2024 State of Open Source Report : https://www.globalbankingandfinance.com/2024-state-of-open-source-report-shows-open-source-software-adoption-growing-despite-security-and-support-challenges/

또한, 오픈소스 사용이 증가함에 따라 엔터프라이즈 소프트웨어 시장에서 독점 소프트웨어 사용이 지속적으로 감소하고 있다. RedHat의 [2022 오픈소스 Enterprise 현황 보고서](https://www.redhat.com/en/resources/state-of-enterprise-open-source-report-2022)[^redhat2022]에 따르면, 향후 2년 동안 독점 소프트웨어 사용이 현재 45%에서 37%로 8% 줄어들 것으로 전망되며, 같은 기간 동안 엔터프라이즈 오픈소스와 커뮤니티 기반 오픈소스는 각각 5%, 3% 증가할 것으로 예상된다.

[^redhat2022]: 오픈소스 Enterprise 현황 보고서 (2022) : https://www.redhat.com/en/resources/state-of-enterprise-open-source-report-2022

이러한 추세는 오픈소스가 단순히 비용 절감을 위한 도구가 아니라, 기업의 혁신과 경쟁력 강화를 위한 전략적 자산으로 인식되고 있음을 보여준다. IT 리더의 80%는 조직의 새로운 기술을 위한 엔터프라이즈 오픈소스 소프트웨어 사용이 증가할 것이라고 답했으며, 이는 오픈소스가 기업 IT 전략의 핵심 요소로 자리잡고 있음을 나타낸다.

그러나 오픈소스 도입에 따른 과제도 존재한다. 보안 정책 및 규정 준수 유지, 패치 및 릴리스 최신 상태 유지 등이 주요 과제로 지적되고 있다. 응답자의 79%가 보안 정책 및 규정 준수 유지가 어렵다고 답했으며, 70%가 업데이트 및 패치 최신 상태 유지에 어려움을 겪고 있다고 응답했다.

이러한 동향은 기업들이 오픈소스를 통해 기술 혁신을 가속화하고, 개발 생산성을 높이며, 글로벌 기술 생태계와의 연결성을 강화하고 있음을 보여준다. 동시에 오픈소스 관리와 보안에 대한 체계적인 접근의 필요성도 강조되고 있다.




### 국내 기업들의 오픈소스 도입 현황

#### 오픈소스 도입 현황

최근 국내 기업들의 오픈소스 도입은 급속도로 확산되고 있다. Future Market Insights의 [2024년 보고서](https://www.futuremarketinsights.com/reports/open-source-service-market)[^fmi2024]에 따르면, 한국의 오픈소스 서비스 시장은 2024년부터 2034년까지 연평균 성장률(CAGR) 18.3%로 성장할 것으로 예측되며, 이는 글로벌 주요 국가 중 가장 높은 수치이다.

[^fmi2024]: Open Source Service Market Size, Share, Trends & Forecast 2034 : https://www.futuremarketinsights.com/reports/open-source-service-market

이러한 급격한 성장세는 국내 대기업들의 적극적인 오픈소스 도입과 정부의 지원 정책에 기인한다. 삼성, LG, SK 등 주요 기업들이 오픈소스 프로젝트에 투자하고 있으며, 특히 클라우드 네이티브 기술, 인공지능, 빅데이터 분야에서 오픈소스 활용이 두드러지고 있다.

DataReportal의 [Digital 2024: South Korea 보고서](https://datareportal.com/reports/digital-2024-south-korea)[^datareportal2024]에 따르면, 2024년 1월 기준 한국의 인터넷 사용자 수는 5,030만 명으로, 이는 전체 인구의 97.2%에 해당한다. 이러한 높은 인터넷 보급률은 오픈소스 기술의 확산과 활용에 긍정적인 영향을 미치고 있다.

[^datareportal2024]: Digital 2024: South Korea : https://datareportal.com/reports/digital-2024-south-korea

또한, 정부 차원에서도 오픈소스 활성화를 위한 정책을 추진하고 있다. 과학기술정보통신부는 '공개SW 활성화 계획'을 통해 오픈소스 생태계 조성과 전문인력 양성을 지원하고 있으며, 이는 국내 기업들의 오픈소스 도입을 더욱 가속화할 것으로 예상된다.


#### 국내 오픈소스 시장 현황

현재 국내 기업들의 오픈소스 전환 움직임은 주로 기술 지원 서비스를 보유한 상업적 버전에 초점이 맞춰져 있으나, 앞으로는 [커뮤니티 버전의 범위가 훨씬 커질 것으로 전망](https://www.itworld.co.kr/techlibrary/139540)[^itworld-139540]이 된다. 특히, 클라우드 네이티브 기술, 인공지능, 빅데이터 등의 분야에서 오픈소스 활용이 두드러지게 증가하고 있다.

[^itworld-139540]: 커뮤니티 버전의 범위가 훨씬 커질 것으로 전망 : https://www.itworld.co.kr/techlibrary/139540

최근 주목받고 있는 주요 오픈소스 기술들은 다음과 같다:

- [쿠버네티스(Kubernetes)](https://kubernetes.io)[^kubernetes]: 컨테이너 오케스트레이션의 de facto 표준
- [텐서플로우(TensorFlow)](https://www.tensorflow.org)[^tensorflow]: 머신러닝 및 인공지능 개발을 위한 오픈소스 플랫폼
- [아파치 카프카(Apache Kafka)](https://kafka.apache.org)[^kafka]: 대규모 실시간 데이터 스트리밍 처리
- [이스티오(Istio)](https://istio.io)[^istio]: 마이크로서비스 아키텍처를 위한 서비스 메시
- [프로메테우스(Prometheus)](https://prometheus.io)[^prometheus]: 모니터링 및 알림 시스템

[^kubernetes]: 쿠버네티스(Kubernetes) : https://kubernetes.io
[^tensorflow]: 텐서플로우(TensorFlow) : https://www.tensorflow.org
[^kafka]: 아파치 카프카(Apache Kafka) : https://kafka.apache.org
[^istio]: 이스티오(Istio) : https://istio.io
[^prometheus]: 프로메테우스(Prometheus) : https://prometheus.io

국내 오픈소스 시장은 지속적인 성장세를 보이고 있다. NIPA의 [2024년 오픈소스SW 가이드](https://www.oss.kr/oss_guide/show/9a73fa3c-c233-4e8b-8527-7d57ed7218f7)[^nipa2024]에 따르면, 2022년 국내 오픈소스SW 시장규모는 2021년 대비 11.4% 성장한 3,380억 원을 기록했다. 또한, 국내 기업의 오픈소스SW 활용률은 2021년 대비 5.8%p 증가한 67.3%에 달하며, 특히 SW기업의 오픈소스SW 활용률은 94.2%에 이르는 것으로 나타났다.

[^nipa2024]: NIPA, 오픈소스SW 가이드 3종 2024년 개정판 발간 : https://www.oss.kr/oss_guide/show/9a73fa3c-c233-4e8b-8527-7d57ed7218f7

이러한 추세는 국내 오픈소스 생태계가 단순한 사용을 넘어 글로벌 오픈소스 커뮤니티에 적극적으로 참여하고 기여하는 단계로 발전하고 있음을 보여준다. 특히 금융, 제조, 유통 등 전통 산업 분야에서도 오픈소스 기술 도입이 가속화되고 있어, 앞으로 국내 오픈소스 시장의 성장세는 더욱 가파를 것으로 전망된다.


### 오픈소스 도입 이유
해를 거듭할수록 기업들은 점점 더 많은 오픈소스를 도입하고 있다. 기업들이 오픈소스를 도입하게 된 이유로는 비용 절감이 가장 크다. 독점 소프트웨어를 사용하면 라이선스 비용이 계속 발생하며, 벤더에게 종속되는 문제가 있다. 또한 독점 소프트웨어는 오픈소스보다 시장이나 기술의 변화에 빠르게 대응하지 못하는 경우가 많다. 따라서 오픈소스가 소프트웨어의 기능, 품질, 보안 면에서 독점 소프트웨어보다 더 나은 것으로 인식되고 있다. 그 외에도 최신 기술 확보, IT 기술 역량 강화, 경쟁력 강화, 시장 확대 및 인재 확보 등 그 이유가 다양하게 나타난다. 결과적으로는 오픈소스가 총소유 비용(TCO) 감소뿐만 아니라 다른 여러 측면에서도 유리하다. 그렇다면 각각의 오픈소스 도입 이유에 대해 더 자세히 살펴보자. 

#### 비용 절감
일반적으로 오픈소스는 권리자인 저작권자가 라이선스를 통해 이용을 허락한 것이며, [OSI(Open Source Initiative)](https://opensource.org)[^osi]에서 인증한 오픈소스 라이선스들은 모두 상업적 이용을 제한하지 않는다. 라이선스 의무 사항만 준수하면 기업은 비용을 지불하지 않고 자유롭게 오픈소스를 사용할 수 있다. 그리고 오픈소스는 완성된 패키지 형태로 제공되기도 하는데 종종 누구나 자유롭게 사용할 수 있는 커뮤니티 버전과 과금 정책이 포함된 엔터프라이즈 버전이 따로 존재하기도 한다. 엔터프라이즈 버전은 프리미엄 기능이나 보안 패치, 기술 지원 등을 통한 차별화 전략을 사용하기에 기업은 사용 환경에 따라 적절히 선택할 수 있다.

[^osi]: OSI(Open Source Initiative) : https://opensource.org


#### 최신 기술
오픈소스는 전 세계의 누구나 조건 없이 참여할 수 있으며, 급변하는 기술의 변화에 민첩하게 대응하다 보니 최신 기술이 자연스럽게 집약된다. 최근에는 클라우드 환경을 기반으로 하는 오픈소스, AI 관련 오픈소스들이 인기를 얻어 많이 등장하고 있다. 기업들은 최신 오픈소스를 적극적으로 도입하여 사내 개발자들에게 사용을 권장하고 최신 기술력을 확보하는 데 힘쓰고 있다.

#### 안정성

오픈소스는 독점 소프트웨어보다 안정적이라고 평가받는다. 그 이유는 다음과 같다. 

- 이슈를 발견하고 해결해 나가는 주기가 빠르다: 오픈소스는 코드가 공개되어 있으므로 해커가 보안 취약점 및 약점을 찾기가 더 쉽다는 주장도 있지만 실제로는 수많은 기여자에 의해 더 빨리 발견될 가능성이 크다. 커뮤니티가 활성화된 오픈소스일수록 이슈가 발생했을 때 더 빠르게 개선이 이루어진다.
- 패치와 신규 버전 배포가 빠르다: 오픈소스에서 취약점이 보고되면 심각도가 높은 이슈면 빠르면 하루나 이틀 이내에도 수정 사항이 배포된다. 반면에 독점 소프트웨어는 업데이트 주기가 길고 대응이 늦을 수밖에 없다. 독점 소프트웨어는 개발 인력이 제한적이라 소프트웨어의 우선순위를 지정하여 패치가 이뤄지고, 보통 6개월에서 길게는 12개월의 배포 주기를 갖게 된다. 즉 벤더의 스케줄에만 의존하는, 자기 결정권의 부재 상태를 맞을 수 있다.
- 독점 소프트웨어의 상당 부분도 이미 오픈소스를 사용 중이다: 독점 소프트웨어 개발기업가 사용 중인 오픈소스의 보안 이슈를 제대로 추적하고 관리하지 않으면 버그 및 취약점이 포함된 상태로 배포될 가능성이 크다. 또한, 개선되었다 하더라도 실제 배포까지는 오랜 시간이 걸린다.

#### 역량 강화
오픈소스는 수많은 개발자의 손을 거쳐 높은 품질의 소스 코드와 아키텍처를 가지게 된다. 이는 기존 코드에만 익숙한 개발자들에게 시각의 변화를 주거나 새로운 기술을 습득할 기회가 된다. 그뿐만 아니라 보편적 기능은 오픈소스로 대체하고 개발자는 비즈니스 로직 개발에 집중할 수 있는 환경을 만들 수 있기 때문에 오픈소스의 사용은 성공적으로 프로젝트를 완성하기 위한 필수 요건이 되어가고 있다.

#### 생산성의 증가
개발 프레임워크부터 모니터링, 테스트 자동화, 부하 테스트, 빌드, 배포까지 개발 프로젝트를 수행하는 과정 전체에서 오픈소스를 적극적으로 도입하게 되면 부서별로 각자 따로 개발할 필요가 없고, 코드 중복도 최소화할 수 있다. 이렇게 얻어진 효율성은 조금 더 혁신적인 기술에 투자할 여력을 만들어 준다.

#### 시장 확대
국내 소프트웨어 기업의 글로벌 진출은 현실적으로 매우 어렵다. 하지만 소스 코드를 공개하면 사용자를 전 세계에서 확보할 수 있고, 안정성, 보안성, 지속적 발전 가능성이라는 오픈소스라는 긍정적인 기대감이 소프트웨어의 가치를 높일 수 있다. 그 때문에 이전보다 사업을 글로벌로 확장할 기회를 훨씬 더 많이 창출할 수 있다.

#### 인재 확보
독점 소프트웨어를 사용하게 될 경우, 해당 소프트웨어 개발 경력이 있는 인재를 확보하는 데 상당한 어려움이 따른다. 하지만 오픈소스의 경우에는 누구나 접근할 수 있는 코드이기 때문에 더욱 많은 인력 풀을 대상으로 인재를 확보할 기회가 늘어난다. 기존 직원들에게는 오픈소스 교육을 하는 기업이 늘어나고 있으며, 이제는 단순히 오픈소스를 사용하는 것뿐만 아니라 오픈소스에 직접 참여하고 [오픈소스 역량을 가진 오픈소스 전문가 고용을 고려한다는 인사담당자가 늘어 가는 추세](https://training.linuxfoundation.org/resources/2020-open-source-jobs-report)[^training-resource]이다.

[^training-resource]: 2020 Open Source Jobs Report : https://training.linuxfoundation.org/resources/2020-open-source-jobs-report/



### 오픈소스 도입 시 고려사항
Gartner의 [Technology Insight for Software Composition Analysis (2019) 보고서](https://www.gartner.com/en/documents/3971011/technology-insight-for-software-composition-analysis)[^gartner-3971011]에서는 기업은 오픈소스를 도입할 때 고려해야 할 사항으로 크게 4가지를 꼽고 있다. (1) 오픈소스가 장기적으로 생존할 가능성이 큰가? (2) 보안 이슈는 없는가? (3) 벤더 이슈는 없는가? (4) 컴플라이언스 및 지식재산권 확인이다. 이 밖에도 오픈소스가 우리의 제품 또는 서비스에 적합한 기술인지, 오픈소스를 도입했을 때 충분한 기술 지원을 받을 수 있는지 등도 확인해야 한다. 검토 사항 중 일부를 조금 더 자세히 살펴본다. 

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

오픈소스 컴플라이언스란, 오픈소스를 사용하고 개발하는 사람들이 오픈소스의 저작권을 존중하기 위해서 오픈소스의 라이선스 의무를 이행하는 과정이다. 종종 조직에서는 오픈소스 라이선스 컴플라이언스를 성가시다고 여긴다. 물론, 모든 라이선스를 식별하고 각각의 라이선스 의무를 준수한다는 것은 어려운 작업이다. 하지만 오픈소스가 고갈되지 않고 유지될 수 있도록 보장하는 것은 오픈소스를 활용하는 기업이 담당할 책임의 일부이기도 하다. 규정을 준수하기 위한 노력을 통해 기업은 오픈소스를 사용하면서 발생할 수 있는 비용과 위험을 이해하기도 하며, 결과적으로는 오픈소스를 더 잘 이해하고 사용할 수 있게 된다. 

오픈소스 컴플라이언스의 범위를 보면 단순히 기업 내에서의 사용하는 것뿐만 아니라 3rd party 공급자와 소프트웨어 공급 및 수급 계약을 하면서 발생하게 될 오픈소스 라이선스 의무사항을 준수하는 활동도 포함된다. 이런 활동들은 오픈소스 커뮤니티와 존중과 신뢰를 바탕으로 한 관계를 구축하는 기반이 되기도 한다. 궁극적으로는 오픈소스 컴플라이언스는 저작권자의 지식재산권을 보호하는 데에 그 목적이 있다는 것을 기억해야 한다.

{{< imgproc compliancerange Fit "768x768" >}}
<center><i>[오픈소스 컴플라이언스 범위]</i><center>
{{< /imgproc >}}



> 참고로, 지난 2020년 12월, 오픈소스 컴플라이언스에 대한 국제 표준이 ISO에 등록되었다. 
> 
> [ISO/IEC 5230](https://www.iso.org/standard/81039.html)[^iso5230]은 기업이 오픈소스 컴플라이언스를 달성하기 위해 수행해야 할 최소한의 요구사항을 정의하고 있다. NIPA에서 출간한 기업 오픈소스 거버넌스 OpenChain 해설서에서는 이에 대한 자세한 내용 및 준수 방법을 설명한다. 
> 
> 가이드는 다음 페이지에서 다운받을 수 있다. : https://www.oss.kr/oss_guide/show/7050bff0-d06b-43f0-99a6-9975afcd486f

[^iso5230]: ISO/IEC 5230 : https://www.iso.org/standard/81039.html


#### 오픈소스 컴플라이언스 프로세스
기업은 오픈소스 라이선스 의무사항을 준수할 수 있도록 오픈소스의 사용, 기여, 감사 및 배포에 이르는 일련의 과정을 관리/감독해야 한다. 검증 단계까지 전반적인 내용을 체크 리스트를 작성하여, 일관성을 보장하고 검증 단계를 간과하지 않도록 하는 것이 중요하다. 여기서는 일반적인 오픈소스 컴플라이언스 프로세스를 소개하고 단계별 주요 내용을 설명한다.

{{< imgproc compliance-process Fit "768x768" >}}
<center><i>[오픈소스 컴플라이언스 프로세스]</i><center>
{{< /imgproc >}}


##### **1. 오픈소스 라이브러리 식별**
프로젝트에 사용된 오픈소스를 식별하고 목록을 도출하는 단계이다. 모든 오픈소스 컴포넌트가 식별되어야 하며, 오픈소스 원본의 위치와 라이선스 정보 등도 함께 기록되어야 한다. 자동화된 스캐닝 도구를 통해 식별하는 것을 권장한다. 자동화된 스캐닝 도구는 [주요 오픈소스 관리 도구 소개](#주요-오픈소스-관리-도구-소개)에서 자세히 다룬다. 스캔은 배포 시점이나 변동 사항이 있을 때, 개발자의 요청이 있을 때, 혹은 주기적으로 수행할 수 있다.

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
사용 파악 시 미처 확인하지 못한 누락이 발생할 수 있다. 프로젝트 규모가 커질수록, 그 대상이 많아질수록 직접 오픈소스 파악하기는 어려워진다. 또한 개발이 진행되고, 배포까지 최종 단계에 이르기까지 수많은 변경 작업이 일어난다. 이 과정에서 사용된 오픈소스 목록과 실제 코드에 포함된 오픈소스를 완전히 똑같이 맞추기는 어려울 것이다. 현실적으로도 이러한 변경 사항을 추적하는 데 있어 상당히 큰 노력과 시간이 소모되기도 한다.

##### **배포 프로세스 지연**
애플리케이션 개발과 배포에 영향을 줄 수 있다. 오픈소스 목록을 수동으로 관리하게 되면 승인 프로세스도 수동으로 수행되어 매우 느리게 진행될 가능성이 크다. 이미 통합된 오픈소스 중 이슈가 발생하게 되면 해당 오픈소스를 제거하고 대안을 찾도록 개발자에게 요구해야 할 수도 있는데 이렇게 되면 일정에 큰 차질을 빚게 될 것이다.

#### 오픈소스 목록 관리의 자동화
위에서 언급한 것처럼 여러 측면에서 오픈소스 관리는 자동화가 필요하다. 자동화를 위해서는 아래와 같은 오픈소스를 식별하기 위한 적절한 도구를 구축하거나 도입하여 사용해야 한다.
- 코드 레벨에서 사용 중인 오픈소스를 찾아내며 비교를 제공하는 소스 코드 스캐너
- 오픈소스 라이브러리 파일을 찾아내는 파일 스캐너
- 오픈소스를 패키지 단위로 가져오는 패키지 매니저 분석 도구
- 라이선스와 컴플라이언스 항목 및 리소스를 추적하기 위한 컴플라이언스 관리 도구
- 라이선스 결합 방식 분석 도구
- 오픈소스 BOM(Bill of Materials, 사용된 소프트웨어의 ) 관리 도구
- 전반적으로 프로젝트를 관리하고 오픈소스 목록을 관리할 포탈


### SBOM 관리

소프트웨어 공급망 보안의 중요성이 증가함에 따라 SBOM(Software Bill of Materials) 관리가 핵심 요소로 부상하고 있다. SBOM은 소프트웨어 구성 요소, 라이선스, 종속성 등에 대한 정보를 포함하는 문서이다.

#### 글로벌 SBOM 규제 동향

1. 미국

   - 2021년 5월: [행정명령 14028 발표](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity)[^order-14028], 연방 정부 계약자에게 SBOM 제출 의무화
   - 2023년 9월: [FDA, 의료기기 제조업체에 SBOM 제출 요구 발표](https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity)[^fda2023]
   - 2024년 3월: CISA, 주요 인프라 운영자에 대한 [SBOM 요구사항](https://www.cisa.gov/sbom)[^cisa2024] 발표
   - 2024년 5월: CISA, "Secure by Design Pledge" 발표, 주요 기술 기업들의 사이버보안 강화 약속 포함[^cisa-pledge]

2. 유럽연합

   - 2023년 7월: [사이버 복원력 법(Cyber Resilience Act)](https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act)[^eu2023] 초안 승인, SBOM 요구사항 포함
   - 2024년: 최종 법안 채택
   - 2027년: 대부분의 조항 시행 예정, 디지털 요소가 있는 제품을 시장에 출시하는 모든 기업은 최소한의 사이버보안 및 보고 요구사항 [준수 필요](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)[^eu-cra]

3. 일본

   - 2023년 10월: 경제산업성, [SBOM 가이드라인 발표](https://www.meti.go.jp/english/press/2023/0728_001.html)[^japan2023]
   - 2024년 5월: Quad Cybersecurity Partnership의 일환으로 미국, 인도, 호주와 함께 "Secure Software 공동 원칙" 발표, 소프트웨어 보안 강화 및 정부의 소프트웨어 조달 지침 수립[^quad-partnership]


[^order-14028]: Executive Order 14028 of May 12, 2021 : https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity
[^fda2023]: FDA Cybersecurity Guidance for Medical Devices: https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity
[^cisa2024]: CISA SBOM Requirements: https://www.cisa.gov/sbom
[^cisa-pledge]: CISA Secure by Design Pledge: https://www.cisa.gov/secure-by-design
[^eu2023]: EU Cyber Resilience Act: https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act
[^eu-cra]: EU Cyber Resilience Act Implementation: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
[^japan2023]: Japan METI SBOM Guidelines: https://www.meti.go.jp/english/press/2023/0728_001.html
[^quad-partnership]: Quad Cybersecurity Partnership: https://www.whitehouse.gov/briefing-room/statements-releases/2023/05/20/quad-leaders-joint-statement/



#### 국내 SBOM 규제 동향

1. 정부 가이드라인 발표

   - 2024년 5월 13일: 과학기술정보통신부, 국가정보원, 디지털플랫폼정부위원회 공동으로 '[SW 공급망 보안 가이드라인 1.0](https://www.kisa.or.kr/2060204/form?postSeq=15&page=1)' 발표[^2060204]
   - 가이드라인은 SBOM 기반 SW 공급망 보안 관리체계 구축 방안 포함

2. 시범 사업 및 지원 정책

   - 2024년 하반기: 디지털플랫폼정부 주요시스템 구축 시 [SBOM 시범 적용 계획](https://dpg.go.kr/DPG/contents/DPG02020000.do?schM=view&id=20240513105420991857&schBcid=press)[^nia2024]
   - 기업지원허브, 디지털헬스케어 보안리빙랩, 국가사이버안보협력센터에 SBOM 기반 SW 공급망 보안 관리체계 구축 및 기업 지원 서비스 제공

3. 제도화 준비

   - 2024년 하반기: 산·학·연 전문가 참여 [범정부 합동TF 구성](https://www.oss.kr/oss_guide/show/49b93bf6-6c33-48a9-aae8-7494ab8b29ca)[^boannews2024]
   - 'SW 공급망 보안 로드맵' 마련 계획 발표

4. 법적 기반 마련

   - 2024년 1월: '[경제안보 지원을 위한 공급망 안정화 기본법](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=257271#0000)[^korlaw]' 등 3개 공급망 관련 법률 제정, 소프트웨어를 경제안보 품목으로 지정
   - 향후 의료, 국방, 제조 등 특정 산업 분야에 대한 구체적인 정책 수립 예정

이러한 동향은 국내에서 SBOM의 중요성이 인식되고 있으며, 정부 차원에서 가이드라인 제시와 기업 지원을 통해 SBOM 도입을 장려하고 있음을 보여준다. 현재는 의무화 단계까지는 이르지 않았지만, 점진적인 접근을 통해 제도화를 준비하고 있는 상황이다.

[^2060204]: SW 공급망 보안 가이드라인 : https://www.kisa.or.kr/2060204/form?postSeq=15&page=1
[^korlaw]: 경제안보 지원을 위한 공급망 안정화 기본법 : https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=257271#0000
[^boannews2024]: https://www.oss.kr/oss_guide/show/49b93bf6-6c33-48a9-aae8-7494ab8b29ca


#### SBOM 최소 요구 사항

NTIA(National Telecommunications and Information Administration)는 라이선스 및 보안취약점 관리를 위해 SBOM이 갖춰야 할 다음 세 가지의 요구 사항을 제시하였다[^ntia2021].

1. 데이터 필드: SBOM이 포함해야 할 데이터 (다음 단락에서 세부 내용 설명)
2. 자동화 지원: SBOM 생성 자동화
   - SBOM는 인간이 읽을 수 있어야 하고 동시에 기계 판독이 가능하여야 한다.
   - SBOM가 자동으로 생성되는 환경을 지원해야 한다.
3. Practice와 절차: SBOM 생성 및 운영 방법을 정의해야 한다.

#### 데이터 필드

NTIA는 SBOM이 포함해야 하는 7가지 데이터 필드를 [명시하였다](https://www.ntia.gov/files/ntia/publications/sbom_minimum_elements_report.pdf)[^ntia2021].

| Data Field   |      Description      |
|:----------|:-------------|
| 공급자 이름 | 구성요소를 만들고 정의하고 식별하는 주체의 이름 |
| 구성요소 이름 | 최초 공급자에 의해 정의된 소프트웨어 단위의 명칭 |
| 구성요소 버전 | 공급자가 이전에 식별된 소프트웨어 버전으로부터의 변경을 명시하기 위해 사용하는 식별자 |
| 기타 고유 식별자 | 구성요소를 식별하는 데 사용되거나 관련 데이터베이스를 위한 조회 키 역할을 하는 기타 식별자 |
| 종속성 관계 | 업스트림 구성요소 X가 소프트웨어 Y에 포함된다는 관계의 명시 |
| SBOM 데이터 작성자 | 이 구성요소에 대한 SBOM 데이터를 만든 주체의 이름 |
| 타임스탬프 | SBOM 데이터 어셈블리의 날짜 및 시간 기록 |

이러한 데이터 필드를 포함하는 SBOM은 기계가 판독(Machine Readable)할 수 있도록 다음 세 가지 표준화된 형식 중 하나로 [작성되어야 한다](https://www.cisa.gov/sbom)[^cisa2024].

#### SBOM 표준 형식

1. **SPDX (Software Package Data Exchange)**
   - Linux Foundation에서 개발한 오픈 소스 표준
   - ISO/IEC 5962:2021로 국제 표준화
   - 주요 특징: 라이선스 관리에 강점, XML, JSON, YAML, RDF 등 다양한 형식 지원
   - [SPDX 공식 웹사이트](https://spdx.org/)

2. **CycloneDX**
   - OWASP에서 개발한 경량화된 SBOM 표준
   - 주요 특징: 보안 취약점 관리에 초점, XML, JSON, Protocol Buffers 지원
   - [CycloneDX 공식 웹사이트](https://cyclonedx.org/)

3. **SWID Tags (Software Identification Tags)**
   - ISO/IEC 19770-2:2015 표준으로 정의
   - 주요 특징: 소프트웨어 라이프사이클 전반에 걸친 추적 가능, XML 기반
   - [NIST SWID 정보](https://csrc.nist.gov/projects/Software-Identification-SWID)

각 표준은 고유한 특징과 장점을 가지고 있으며, 조직의 필요와 목적에 따라 적절한 형식을 선택할 수 있다. SPDX는 라이선스 관리에, CycloneDX는 보안 취약점 관리에 강점을 보이며, SWID Tags는 소프트웨어 자산 관리에 [특화되어 있다](https://www.techtarget.com/searchsecurity/tip/SBOM-formats-compared-CycloneDX-vs-SPDX-vs-SWID-Tags)[^techtarget2023].

[^ntia2021]: https://www.ntia.gov/files/ntia/publications/sbom_minimum_elements_report.pdf
[^cisa2024]: https://www.cisa.gov/sbom
[^techtarget2023]: https://www.techtarget.com/searchsecurity/tip/SBOM-formats-compared-CycloneDX-vs-SPDX-vs-SWID-Tags


이 중 SPDX 표준에 대해서 좀 더 자세히 살펴보자. 

#### SPDX

여기서는 Linux Foundation의 프로젝트인 SPDX에서 만든 SPDX 표준과 SPDX 문서 작성 방법에 대해 알아보겠다. SPDX 표준은 2021년 9월 ISO 표준([ISO/IEC 5962](https://www.iso.org/standard/81870.html))[^isoiec5962]으로 등록된 대표적인 SBOM 포맷이다. 기업의 SBOM 관리 체계가 모든 포맷의 SBOM을 지원하면 좋겠지만, 하나의 포맷을 선택해야 한다면 국제 표준인 SPDX를 먼저 지원하는 것을 권장한다. 더불어 SPDX는 당초 오픈소스 라이선스 컴플라이언스를 위해 만들어진 포맷이기에 기업의 오픈소스 라이선스 관리에 효율적으로 사용할 수 있다.

[^isoiec5962]: ISO/IEC 5962 : https://www.iso.org/standard/81870.html 

SPDX 표준은 2024년 4월에 3.0 버전이 릴리즈되었다. 하지만, 이 문서에서는 SPDX 3.0에 대해 간단히 소개하고, 주요 내용은 현재 널리 사용되고 있는 SPDX 2.3 기준으로 소개하고자 한다.

SPDX 2.3은 2022년 6월에 릴리즈되었으며 다음과 같은 정보를 포함한다:

{{< imgproc spdx-info Fit "512x512" >}}
<center><i>[SPDX v2.3 format]</i><center>
{{< /imgproc >}}

SPDX는 소프트웨어가 포함하고 있는 패키지, 파일, 스니핏(코드 조각) 등에 대한 각각의 라이선스, 버전, 저작권 등의 정보를 관리할 수 있다. 또한 SPDX는 자동으로 정보를 읽고 쓸 수 있도록 JSON, YAML 등 프로그래밍 언어로 쉽게 조작할 수 있도록 광범위하게 사용되는 데이터 포맷을 채택하였다. SPDX 2.3은 아래의 네 가지 포맷을 지원한다:

- [JSON](https://github.com/spdx/spdx-spec/blob/development/v2.3/examples/SPDXJSONExample-v2.3.spdx.json)[^spdx-json]
- [YAML](https://github.com/spdx/spdx-spec/blob/development/v2.3/examples/SPDXYAMLExample-v2.3.spdx.yaml)[^spdx-yaml]
- [Tag/Value](https://github.com/spdx/spdx-spec/blob/development/v2.3/examples/SPDXTagExample-v2.3.spdx)[^spdx-tagvalue]
- [RDF/xml](https://github.com/spdx/spdx-spec/blob/development/v2.3/examples/SPDXRdfExample-v2.3.spdx.rdf)[^spdx-rdfxml]

[^spdx-json]: JSON SPDX sample : https://github.com/spdx/spdx-spec/blob/development/v2.3/examples/SPDXJSONExample-v2.3.spdx.json
[^spdx-yaml]: YAML SPDX sample : https://github.com/spdx/spdx-spec/blob/development/v2.3/examples/SPDXYAMLExample-v2.3.spdx.yaml
[^spdx-tagvalue]: Tag/Value SPDX sample : https://github.com/spdx/spdx-spec/blob/development/v2.3/examples/SPDXTagExample-v2.3.spdx
[^spdx-rdfxml]: RDF/xml SPDX sample : https://github.com/spdx/spdx-spec/blob/development/v2.3/examples/SPDXRdfExample-v2.3.spdx.rdf

[SPDX 3.0](https://spdx.github.io/spdx-spec/v3.0.1/)은 2024년 4월에 릴리즈되었으며, 이전 버전에 비해 더 유연하고 확장 가능한 구조를 제공한다. 주요 변경 사항으로는 모델 구조의 개선, 새로운 프로필 시스템 도입, 그리고 JSON-LD 기반의 직렬화 등이 있다[^spdx3]. 하지만 SPDX 3.0은 아직 도구 지원과 업계 적용이 제한적이므로, 현재로서는 SPDX 2.3 사용을 권장한다.

[^spdx3]: SPDX 3.0 Specification : https://spdx.github.io/spdx-spec/v3.0.1/

SPDX 규격은 100 페이지가 넘는 적지 않은 분량의 문서이기 때문에 처음 SPDX 표준에 맞추어 문서를 작성하는 것은 쉽지 않다. SPDX 프로젝트는 Excel로 작성된 SBOM을 SPDX 문서로 자동 변환하는 도구를 제공하고 있다. 즉, 사용자는 먼저 SPDX 프로젝트에서 제공하는 [Excel template 파일](https://github.com/spdx/tools/blob/master/Examples/SPDXRdfExample-v2.3.xls)[^spdx-excel]을 다운받아서 각 시트에 필요한 정보를 기입한다.

[^spdx-excel]: SPDX 엑셀 파일 : https://github.com/spdx/tools/blob/master/Examples/SPDXRdfExample-v2.3.xls


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
* [FOSSLight 사용자 문서](https://fosslight.org/fosslight-guide/)[^fosslight-doc]

[^fosslight]: FOSSLight : https://fosslight.org/
[^fosslight-doc]: FOSSLight 사용자 문서 : https://fosslight.org/fosslight-guide/

##### **OLIVE Platform** - https://olive.kakao.com

{{< imgproc logo-olive Fit "384x384" >}}
{{< /imgproc >}}

Kakao는 자사의 수많은 프로젝트의 오픈소스 관리를 위해 사용하던 시스템을 누구나 사용할 수 있도록 [OLIVE Platform](https://olive.kakao.com)[^olive] 을 무료 웹서비스로 오픈했다. **OLIVE Platform**은 프로젝트 실시간 스캔을 통해 사용한 오픈소스 컴포넌트를 조회하고, 오픈소스의 라이선스 의무사항과 이슈를 확인하여 고지 의무를 준수할 수 있도록 지원하는 오픈소스 관리 서비스다. 쉽고, 빠르고 정확한 오픈소스 검증을 목표로 직관적인 기능과 UI로 구성되어 있으며, 소셜 로그인으로 프로젝트를 관리하고, 라이선스 의무사항 확인, 고지문 다운로드를 할 수 있다. 체험하기를 이용하면 로그인 없이 간단하게 Dependency와 라이선스 확인이 가능하다.

또한, 보안상 웹 서비스 사용이 어렵거나, 소스코드 노출이 우려되는 경우 안심하고 사용할 수 있도록 [OLIVE CLI](https://github.com/kakao/olive-cli)를 제공한다. **OLIVE CLI**는 사용자 PC에서 OLIVE Platform 기능을 수행할 수 있으며, 보안이 엄격한 금융권에서도 사용되고 있다.
* [OLIVE 사용자 문서](https://olive.kakao.com/docs/)[^olive-doc]
* [OLIVE CLI 사용자 문서](https://olive.kakao.com/docs/cli/)[^olive-cli-doc]

[^olive]: Kakao, OLIVE Platform : https://olive.kakao.com
[^olive-doc]: OLIVE 사용자 문서 : https://olive.kakao.com/docs/
[^olive-cli-doc]: OLIVE CLI 사용자 문서 : https://olive.kakao.com/docs/cli/

##### **Fossa** - https://fossa.com

{{< imgproc logo-fossa Fit "384x384" >}}
{{< /imgproc >}}

2015년 설립된 실리콘밸리 스타트업에서 제공하는 서비스로, 풍부한 오픈소스 메타데이터 및 정교한 정책 거버넌스를 제공한다. CI/CD 통합 등 DevOps 환경을 지원하며 개발자 친화적 기능들로 구성되어 있다. Twitter, Uber, Zendesk 등과 파트너를 맺고 있으며, JS Foundation, Linux Foundation, NPM 등과 제휴하고 있다. 기본적인 사용은 무료이나 일부 추가 기능들을 유료로 제공하며, 팀 규모가 100명 이상이라면 엔터프라이즈 버전이 적용된다.

##### **FOSSID** - https://fossid.com/

{{< imgproc logo-fossid Fit "384x384" >}}
{{< /imgproc >}}

2016년 스웨덴에서 설립된 FOSSID는 오픈소스 라이선스 및 보안 취약점 관리를 위한 솔루션이다. 소스 코드 내 오픈소스 컴포넌트를 탐지하고, 각 컴포넌트의 라이선스 및 보안 취약점을 식별한다. 방대한 오픈소스 DB 및 자동 데이터 수집 기술, AI를 통한 향상된 탐지 성능 등 특징을 갖고 있다. 특히, 코드 일부에서 보안 취약점을 탐지하는 유일한 오픈소스 스캐너라는 장점이 있다. 

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

2011년 설립되어 라이선스 준수 및 취약점 관리 서비스를 제공하며, 오래된 서비스인 만큼 방대한 데이터베이스를 확보하고 있다. 110억 개 이상의 소스 코드 파일, 200개 이상의 언어지원, 1억 개 이상의 라이브러리를 확보하고 있다. 컨테이너 및 서비리스 등 모든 환경을 지원하며 현재 Microsoft Azure DevOps 서비스로도 제공되고 있다. GitHub의 Ultimate에서 사용할 수 있는 옵션으로 제공되고 있으며 GitHub Package도 지원한다. WhiteSource도 기본적인 사용은 무료이며, 팀 규모가 20명을 넘어가면 유료로 사용 가능하며, 추가 프리미엄 기능을 제공한다.

##### **CodeEye** - https://www.olis.or.kr/codeEye/introduction.do

{{< imgproc logo-codeeye Fit "384x384" >}}
{{< /imgproc >}}

CodeEye는 오픈소스 라이선스 비교·분석·검사를 위해 사람이 해야 할 수작업(Eye Checking)을 원활하게 수행하거나 도움을 주는 시스템으로 오픈소스 사용 시 준수해야 할 라이선스(GNU GPL 등) 내용을 효과적으로 검사하여 보여준다. 한국저작권위원회에서 구축한 오픈소스 DB(지속적 Update)를 기반으로 검사하며, 중소기업기본법 시행령 제3조(중소기업의 범위) 규정에 따른 중소기업 대상으로 무료로 서비스한다. 

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

소스 코드의 저작권 고지는 일반적으로 "copyright" 라는 단어를 포함하여 연도와 저작권자 혹은 회사명을 포함하는 문자열로 이루어진다. 이러한 고지는 저작물에 대한 저작권이 있음을 잠재적인 사용자에게 알려 주게 하며, 저작권 소유자를 식별하는 데 필요하다. 오픈소스에 따라 저작권자뿐만 아니라 특허가 있으면, 특허 소유자, 오픈소스 기여자들을 표시하기도 한다. 연도는 일반적으로 최초 게시된 연도를 의미하며, 저작권 보호 기간을 결정하는 데 사용될 수 있도록 저작권 기간을 의미하기도 한다.    

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
오픈소스 사용 시 고지의무는 라이선스에 따라 고지 방법이 세부적으로 나와 있기도 하다. 대표적인 라이선스인 Apache 2.0의 경우, LICENSE와 NOTICE 파일을 두고, 라이선스 및 저작권 고지 등의 고지사항을 포함할 것을 안내하고 있다.

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


#### 오픈소스 보안의 중요성

오픈소스 소프트웨어는 현대 소프트웨어 개발의 근간이 되었으며, 그 사용량은 지속적으로 증가하고 있다. Sonatype의 [2024 소프트웨어 공급망 현황 보고서](https://www.sonatype.com/state-of-the-software-supply-chain/2024/scale)[^sonatype2024]에 따르면, 2024년 말까지 오픈소스 패키지 다운로드 수가 6.6조 건에 이를 것으로 예상된다. 이는 전년 대비 52%나 증가한 수치이다.

##### 1. 오픈소스 사용 증가 추세

오픈소스 프로젝트의 수와 버전은 매년 급증하고 있다. 2024년 기준으로:

- Java (Maven) 생태계: 6.7만 개의 프로젝트, 1,870만 개의 버전
- JavaScript (npm) 생태계: 480만 개의 프로젝트, 4,880만 개의 버전
- Python (PyPI) 생태계: 63.5만 개의 프로젝트, 660만 개의 버전
- .NET (NuGet Gallery) 생태계: 66.4만 개의 프로젝트, 1,050만 개의 버전

이러한 증가 추세는 오픈소스가 소프트웨어 개발에서 차지하는 비중이 얼마나 큰지를 잘 보여준다. 실제로 현대 소프트웨어 애플리케이션의 90%가 오픈소스 컴포넌트로 구성되어 있다고 한다.

##### 2. 소프트웨어 공급망 보안의 핵심으로서의 오픈소스

오픈소스의 광범위한 사용은 소프트웨어 공급망 보안에 있어 오픈소스가 핵심적인 위치를 차지하게 만들었다. 그러나 이는 동시에 새로운 보안 위협의 원인이 되기도 한다. Sonatype의 보고서에 따르면, 지난 1년간 51만 2,847개의 악성 패키지가 발견되었으며, 이는 전년 대비 156% 증가한 수치이다[^sonatype2024].

이러한 악성 패키지들은 기존의 보안 도구로는 탐지하기 어려운 경우가 많아, 개발자와 자동화된 빌드 환경을 직접적인 위협에 노출시킨다. 특히, 개발자를 직접 타겟으로 하는 새로운 유형의 공급망 공격이 증가하고 있어 더욱 주의가 필요하다.

오픈소스 보안의 중요성은 단순히 기술적인 문제를 넘어 경제적, 법적 영향력까지 확대되고 있다. [세계의 오픈 소스 서비스 시장 보고서(2024년)](https://www.giikorea.co.kr/report/tbrc1429891-open-source-services-global-market-report.html)[^giikorea2024]에 따르면, 오픈소스 서비스 시장은 2028년까지 연평균 24.3%의 성장률로 1,074억 6,000만 달러 규모로 성장할 것으로 예상된다. 이러한 시장의 급격한 성장은 오픈소스 보안의 중요성을 더욱 부각시키고 있다.

따라서, 기업과 개발자들은 오픈소스 사용에 따른 이점을 최대화하면서도, 관련된 보안 위험을 최소화하기 위한 체계적인 접근이 필요하다. 이는 SBOM(Software Bill of Materials) 관리, 지속적인 취약점 모니터링, 그리고 신속한 패치 적용 등을 포함한 종합적인 오픈소스 보안 전략의 수립과 실행을 요구한다.

[^sonatype2024]: Sonatype, 2024 State of the Software Supply Chain Report : https://www.sonatype.com/state-of-the-software-supply-chain/2024/scale
[^giikorea2024]: 세계의 오픈 소스 서비스 시장 보고서(2024년) : https://www.giikorea.co.kr/report/tbrc1429891-open-source-services-global-market-report.html


#### 오픈소스 보안 취약점 현황

오픈소스 소프트웨어의 사용이 급증함에 따라 보안 취약점 관리의 중요성이 더욱 부각되고 있다. 최신 통계와 트렌드를 살펴보고, 주요 취약점 유형 및 공격 벡터를 이해하는 것은 효과적인 보안 전략 수립에 필수적이다.

##### 1. 최신 통계 및 트렌드

Sonatype의 [2024 소프트웨어 공급망 현황 보고서](https://www.sonatype.com/state-of-the-software-supply-chain/2024/scale)[^sonatype2024]에 따르면, 오픈소스 보안 취약점과 관련된 주요 통계 및 트렌드는 다음과 같다:

- 2024년 기준으로 오픈소스 패키지 다운로드 수가 6.6조 건에 이를 것으로 예상되며, 이는 전년 대비 52% 증가한 수치이다.
- 지난 1년간 51만 2,847개의 악성 패키지가 발견되었으며, 이는 전년 대비 156% 증가한 수치이다.
- 오픈소스 프로젝트의 80%가 1년 이상 업데이트되지 않은 종속성을 포함하고 있으며, 이 중 95%는 안전한 대안이 이미 존재한다.
- 분석된 기업 애플리케이션의 3.6%가 업데이트 후에도 여전히 취약한 버전을 사용하고 있다.

이러한 통계는 오픈소스 보안 취약점이 지속적으로 증가하고 있으며, 기업들의 대응이 아직 충분하지 않음을 보여준다.

##### 2. 주요 취약점 유형 및 공격 벡터

OWASP(Open Web Application Security Project)에서 발표한 [오픈소스 소프트웨어 Top 10 리스크](https://owasp.org/www-project-open-source-software-top-10/)[^owasp2024]를 바탕으로 주요 취약점 유형과 공격 벡터를 살펴보면 다음과 같다:

- **알려진 취약점(Known Vulnerabilities)**: CVE, GitHub Security Advisories 등을 통해 공개된 취약점으로, 패치가 제공되지 않거나 적용되지 않은 경우 위험하다. 예: Log4Shell(CVE-2021-44228)
- **정당한 패키지의 손상(Compromise of Legitimate Package)**: 공격자가 기존의 정당한 프로젝트나 배포 인프라를 손상시켜 악성 코드를 주입하는 경우이다. 예: SolarWinds 사이버 공격
- **이름 혼동 공격(Name Confusion Attacks)**: 타이포스쿼팅(typo-squatting), 브랜드재킹(brand-jacking) 등의 방법으로 정당한 패키지와 유사한 이름의 악성 패키지를 배포하는 공격이다.
- **유지보수되지 않는 소프트웨어(Unmaintained Software)**: 더 이상 적극적으로 개발되지 않는 컴포넌트나 버전을 사용하는 경우, 보안 패치가 제공되지 않아 위험할 수 있다.
- **오래된 소프트웨어(Outdated Software)**: 새로운 버전이 존재함에도 불구하고 오래된 버전을 계속 사용하는 경우이다.

이러한 취약점들은 단순히 코드 상의 문제뿐만 아니라, 소프트웨어 공급망 전체에 걸친 보안 위협을 나타낸다. 특히, Sonatype의 보고서에 따르면 악성 패키지의 급증은 전통적인 보안 도구로는 탐지하기 어려운 새로운 유형의 공격이 증가하고 있음을 시사한다[^sonatype2024].

따라서, 기업들은 단순히 알려진 취약점을 패치하는 것을 넘어, 전체 소프트웨어 공급망에 대한 포괄적인 보안 전략을 수립하고 실행해야 한다. 이는 지속적인 모니터링, 신속한 업데이트 적용, 그리고 개발자 교육 등을 포함한 종합적인 접근을 요구한다.

[^sonatype2024]: Sonatype, 2024 State of the Software Supply Chain Report : https://www.sonatype.com/state-of-the-software-supply-chain/2024/scale
[^owasp2024]: OWASP Top 10 Risks for Open Source Software : https://owasp.org/www-project-open-source-software-top-10/

#### 주요 오픈소스 보안 사고 사례 분석

오픈소스 소프트웨어의 보안 취약점은 광범위한 영향을 미칠 수 있으며, 최근 몇 년간 여러 중요한 사례가 발생했다. 이러한 사례들을 분석함으로써 오픈소스 보안의 중요성과 개선 방향을 파악할 수 있다.

##### 1. 최근 5년간의 주요 사례
   
a) XZ Utils 취약점 (2024년)
  
2024년 3월, XZ Utils라는 리눅스 압축 라이브러리에서 심각한 백도어가 발견되었다[^blackkilt2024]. 이 취약점(CVE-2024-3094)은 악의적인 개발자가 2년에 걸쳐 프로젝트에 기여하면서 신뢰를 쌓은 후 삽입한 것으로 밝혀졌다. 이 사례는 오픈소스 프로젝트의 코드 리뷰 과정의 취약성을 드러냈다.

b) Log4Shell 취약점 (2021년)

2021년 12월, Apache Log4j 라이브러리에서 발견된 Log4Shell 취약점(CVE-2021-44228)은 광범위한 영향을 미쳤다[^infosecurity2024]. 이 취약점은 원격 코드 실행을 가능하게 하여 수많은 Java 기반 애플리케이션과 서비스에 영향을 주었다.

c) SolarWinds 공급망 공격 (2020년)

2020년 말, SolarWinds의 Orion 플랫폼이 공급망 공격의 대상이 되었다[^cisa2024]. 공격자들은 SolarWinds의 빌드 프로세스에 침투하여 악성 코드를 삽입했고, 이는 수많은 고객사에 배포되었다.

d) event-stream 패키지 악성코드 삽입 (2018년)

2018년, npm의 인기 있는 JavaScript 패키지인 event-stream에 악성 코드가 삽입되었다[^github2018]. 공격자는 패키지의 관리 권한을 얻은 후, 특정 암호화폐 지갑을 탈취하는 코드를 추가했다.

##### 2. 사고의 영향 및 교훈

a) 광범위한 영향

이러한 사고들은 단일 프로젝트를 넘어 전체 소프트웨어 생태계에 영향을 미쳤다. 예를 들어, Log4Shell 취약점의 경우 수백만 개의 시스템이 영향을 받았으며, 많은 기업과 기관이 긴급 패치를 적용해야 했다.

b) 신뢰와 검증의 중요성

XZ Utils와 event-stream 사례는 오픈소스 커뮤니티에서 신뢰와 검증의 중요성을 보여준다. 단순히 코드가 공개되어 있다는 것만으로는 보안을 보장할 수 없으며, 철저한 코드 리뷰와 지속적인 모니터링이 필요하다.

c) 공급망 보안의 중요성

SolarWinds 사례는 소프트웨어 공급망 전체에 대한 보안 강화의 필요성을 강조한다. 개발 과정부터 배포까지 전 단계에 걸친 보안 조치가 필요하다.

d) 신속한 대응과 패치 관리의 중요성

Log4Shell 사례에서 볼 수 있듯이, 취약점이 발견된 후 신속한 패치 적용이 중요하다. 그러나 많은 조직에서 여전히 취약한 버전을 사용하고 있어, 지속적인 패치 관리의 중요성이 강조된다.

e) 개발자 교육과 보안 인식 제고

이러한 사고들은 개발자들의 보안 인식 제고의 필요성을 보여준다. 오픈소스 컴포넌트를 사용할 때 보안을 고려하는 습관과 지속적인 교육이 필요하다.

이러한 사례들을 통해 오픈소스 소프트웨어의 보안은 단순히 기술적인 문제가 아니라 커뮤니티 전체의 노력과 인식 변화가 필요한 과제임을 알 수 있다. 기업과 개발자들은 이러한 교훈을 바탕으로 더욱 강화된 보안 정책과 실천 방안을 수립해야 할 것이다.

[^blackkilt2024]: https://www.blackkilt.com/blog/2024/04/29/open-source-xz-utils-vulnerability/
[^infosecurity2024]: https://www.infosecurity-magazine.com/news-features/log4j-vulnerability-12-months-on/
[^cisa2024]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a
[^github2018]: https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident


#### 오픈소스 보안 관련 규제 및 정책 동향

오픈소스 보안과 관련된 규제 및 정책은 [SBOM 관리](#sbom-관리)를 넘어서 더 광범위한 영역으로 확대되고 있다. 이미 언급된 SBOM 관련 규제를 제외하고, 주요 국가들의 오픈소스 보안 정책 동향을 살펴보자.

##### 1. 글로벌 규제 동향

a) 미국
   - 2023년 3월: '오픈소스 소프트웨어 보안법(Securing Open Source Software Act of 2023)' 제안[^oss-act]
     * CISA의 역할 강화: 오픈소스 취약점 식별, 안전한 사용 지원, 민간 부문과의 협력 등
   - 2023년 9월: CISA, '오픈소스 소프트웨어 보안 로드맵' 발표[^cisa-roadmap]
     * 오픈소스 프로그램 사무소(OSPO) 운영 가이드 개발 계획
     * 공공 및 민간 영역 대상 모범 사례 교육 지원

b) 유럽연합 (EU)
   - 2024년: 'EU 사이버보안법(Cybersecurity Act)' 개정 예정[^eu-cyber-act]
     * 오픈소스 소프트웨어의 보안 인증 체계 도입
   - 2024년 10월: NIS2 지침 이행 기한[^nis2]
     * 주요 기반시설 운영자의 오픈소스 소프트웨어 보안 관리 강화 요구

c) 일본
   - 2023년 12월: '사이버보안 전략' 개정[^japan-strategy]
     * 오픈소스 소프트웨어 보안 강화를 위한 국제 협력 강조
   - 2024년: '소프트웨어 관리 가이드라인' 발표 예정
     * 오픈소스 소프트웨어 사용 시 보안 관리 방안 제시

##### 2. 국내 규제 및 정책 현황

a) 법적 기반 마련
   - 2024년 1월: '경제안보 지원을 위한 공급망 안정화 기본법' 등 3개 공급망 관련 법률 제정[^korea-law]
     * 소프트웨어를 경제안보 품목으로 지정

b) 보안 강화 정책
   - 2024년 하반기: 범정부 합동TF 구성 예정[^korea-tf]
     * 오픈소스 보안 정책 수립 및 제도화 방안 논의
   - 2025년: '국가 사이버보안 기본계획' 수립 예정
     * 오픈소스 소프트웨어 보안 강화 방안 포함

c) 산업별 대응
   - 2024년~2025년: 의료, 국방, 제조 등 특정 산업 분야에 대한 오픈소스 보안 정책 수립 예정[^korea-industry]

| 국가/지역 | 주요 정책/규제 | 시행/예정 시기 |
|-----------|----------------|-----------------|
| 미국 | 오픈소스 소프트웨어 보안법 | 2023년 3월 (제안) |
| EU | 사이버보안법 개정 | 2024년 (예정) |
| 일본 | 사이버보안 전략 개정 | 2023년 12월 |
| 한국 | 공급망 안정화 기본법 | 2024년 1월 |

이러한 글로벌 동향은 오픈소스 소프트웨어의 보안이 단순히 기술적인 문제를 넘어 국가 안보와 경제 안정성의 핵심 요소로 인식되고 있음을 보여준다. 기업들은 이러한 규제 환경 변화에 대응하여 오픈소스 사용 정책을 재검토하고, 보안 관리 체계를 강화해야 할 것이다.

[^oss-act]: Securing Open Source Software Act of 2023: https://www.congress.gov/bill/118th-congress/senate-bill/2201
[^cisa-roadmap]: CISA Open Source Software Security Roadmap: https://www.cisa.gov/resources-tools/resources/cisa-open-source-software-security-roadmap
[^eu-cyber-act]: EU Cybersecurity Act: https://digital-strategy.ec.europa.eu/en/policies/cybersecurity-act
[^nis2]: NIS2 Directive: https://digital-strategy.ec.europa.eu/en/policies/nis2-directive
[^japan-strategy]: Japan Cybersecurity Strategy: https://www.nisc.go.jp/pdf/policy/kihon-s/cs-senryaku2021-en-booklet.pdf
[^korea-law]: 공급망 안정화 기본법: https://www.law.go.kr/lsInfoP.do?lsiSeq=257271&viewCls=lsRvsDocInfoR#
[^korea-tf]: 범정부 합동TF 구성 계획: https://www.msit.go.kr/bbs/view.do?sCode=user&mId=113&mPid=238&bbsSeqNo=94&nttSeqNo=3184474
[^korea-industry]: 산업별 오픈소스 보안 정책: https://www.oss.kr/oss_guide/show/49b93bf6-6c33-48a9-aae8-7494ab8b29ca



#### 오픈소스 보안 취약점 관리 방안

오픈소스 보안 취약점을 효과적으로 관리하기 위해서는 [SBOM 관리](#sbom-관리) 외에도 다양한 방안이 필요하다. 여기서는 취약점 스캐닝 및 모니터링, 그리고 패치 관리 및 업데이트 전략에 대해 살펴보겠다.

##### 1. 취약점 스캐닝 및 모니터링

취약점 스캐닝과 지속적인 모니터링은 오픈소스 보안 관리의 핵심이다. 이를 통해 사용 중인 오픈소스 컴포넌트의 알려진 취약점을 신속하게 식별하고 대응할 수 있다.

a) 자동화된 취약점 스캐닝 도구 활용
   - SCA(Software Composition Analysis) 도구 사용
     * 예: Snyk, WhiteSource, Black Duck 등
   - CI/CD 파이프라인에 취약점 스캐닝 통합
     * 빌드 및 배포 과정에서 자동으로 취약점 검사 수행

b) 실시간 모니터링 시스템 구축
   - CVE 데이터베이스와 연동된 모니터링 시스템 구축
   - 오픈소스 프로젝트의 보안 공지 구독 및 모니터링

c) 취약점 심각도 평가 및 우선순위 설정
   - [CVSS(Common Vulnerability Scoring System)](https://www.first.org/cvss/) 활용[^cvss]
   - 비즈니스 영향도를 고려한 자체 평가 기준 수립

| 취약점 심각도 | CVSS 점수 | 대응 시간 |
|---------------|-----------|-----------|
| 긴급 | 9.0-10.0 | 24시간 이내 |
| 높음 | 7.0-8.9 | 1주일 이내 |
| 중간 | 4.0-6.9 | 1개월 이내 |
| 낮음 | 0.1-3.9 | 3개월 이내 |

##### 2. 패치 관리 및 업데이트 전략

식별된 취약점에 대한 신속하고 효과적인 패치 적용은 보안 취약점 관리의 핵심이다. 

a) 패치 관리 프로세스 수립
   - 패치 적용 우선순위 설정
   - 패치 테스트 환경 구축 및 영향 평가
   - 롤백 계획 수립

b) 자동화된 업데이트 시스템 구축
   - 패키지 관리자(예: npm, pip) 활용한 자동 업데이트 설정
   - 컨테이너 이미지 자동 업데이트 시스템 구축

c) 의존성 관리 전략
   - 직접 의존성과 간접 의존성 모두 고려
   - 버전 고정(version pinning) vs 유동적 업데이트 전략 수립
   - 의존성 그래프 분석을 통한 취약점 전파 경로 파악

d) 레거시 시스템 관리
   - 더 이상 지원되지 않는 오픈소스 컴포넌트 식별
   - 대체 가능한 최신 오픈소스 솔루션으로의 마이그레이션 계획 수립

e) 패치 적용 후 모니터링
   - 패치 적용 후 시스템 안정성 및 성능 모니터링
   - 새로운 취약점 발생 여부 지속적 확인

f) 비상 대응 계획 수립
   - 제로데이 취약점 발견 시 신속한 대응 프로세스 마련
   - 임시 완화 조치(workaround) 적용 방안 준비

이러한 방안들을 체계적으로 구현하고 지속적으로 개선함으로써, 기업은 오픈소스 보안 취약점으로 인한 위험을 최소화할 수 있다. 특히, 자동화된 도구와 프로세스를 적극 활용하여 대규모 오픈소스 사용 환경에서도 효율적인 취약점 관리가 가능하도록 해야 한다.

또한, 개발자 교육과 보안 인식 제고도 중요하다. 개발 초기 단계부터 보안을 고려하는 "Security by Design" 원칙을 적용하고, 개발자들이 안전한 오픈소스 사용 방법을 숙지하도록 해야 한다.

[^cvss]: Common Vulnerability Scoring System: https://www.first.org/cvss/


#### 오픈소스 보안 취약점 데이터베이스 및 도구

오픈소스 보안 취약점을 효과적으로 관리하기 위해서는 신뢰할 수 있는 취약점 데이터베이스와 적절한 관리 도구가 필요하다. 여기서는 주요 취약점 데이터베이스와 오픈소스 보안 관리 도구 및 플랫폼에 대해 살펴보겠다.

##### 주요 취약점 데이터베이스

1. **NVD (National Vulnerability Database)**
   - 운영: 미국 국립표준기술연구소(NIST)
   - 특징: CVE(Common Vulnerabilities and Exposures)를 기반으로 한 포괄적인 취약점 정보 제공
   - 링크: https://nvd.nist.gov/

2. **CVE (Common Vulnerabilities and Exposures)**
   - 운영: MITRE Corporation
   - 특징: 공개된 사이버 보안 취약점에 대한 표준 식별자 제공
   - 링크: https://cve.mitre.org/

3. **OSV (Open Source Vulnerabilities)**
   - 운영: Google 및 오픈소스 커뮤니티
   - 특징: 오픈소스 프로젝트에 특화된 취약점 데이터베이스
   - 링크: https://osv.dev/

4. **GitHub Advisory Database**
   - 운영: GitHub
   - 특징: GitHub 생태계 내의 보안 취약점 정보 제공
   - 링크: https://github.com/advisories

5. **Mitre의 CVE**
   - 운영: Mitre
   - 특징: 상용 애플리케이션 및 비공개 소스 프로젝트를 비롯하여 다양한 유형의 취약점에 대한 정보 제공. 취약점 정보는 개별 CVE 번호가 부여되어 관리
   - 링크: https://cve.mitre.org
   - 예) CVE-2015-5211 에 대한 CVE 정보

{{< imgproc cve Fit "768x768" >}}
{{< /imgproc >}}

1. **Sonatype OSS Index** 
   - 운영: Sonatype
   - 특징: Maven, npm, Go, Pypi 등 여러 유형의 Package Management 에서 보고된 오픈소스 취약점 정보 데이터베이스 제공
   - 링크: [Sonatype OSS Index](https://ossindex.sonatype.org)
- 예) CVE-2015-5211 에 대한 OSS Index 정보

{{< imgproc sonatype-oss-index Fit "768x768" >}}
{{< /imgproc >}}


##### 오픈소스 보안 관리 도구 및 플랫폼

1. **OWASP Dependency-Check**
   - 기능: 프로젝트의 종속성을 분석하여 알려진 취약점 식별
   - 지원 언어: Java, .NET, JavaScript, Ruby 등
   - 링크: [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)

2. **Trivy**
   - 기능: 컨테이너 이미지, 파일시스템, Git 저장소의 취약점 스캔
   - 특징: 빠른 스캔 속도, 다양한 환경 지원
   - 링크: [Trivy GitHub](https://github.com/aquasecurity/trivy)

3. **Grype**
   - 기능: 컨테이너 이미지 및 파일시스템의 취약점 스캔
   - 특징: 높은 정확도, 빠른 스캔 속도
   - 링크: [Grype GitHub](https://github.com/anchore/grype)


이러한 도구들은 각각 고유한 특징과 장점을 가지고 있으며, 조직의 요구사항과 개발 환경에 따라 적절한 도구를 선택하여 사용해야 한다. 또한, 이러한 도구들을 CI/CD 파이프라인에 통합하여 지속적인 보안 모니터링을 수행하는 것이 중요하다.

오픈소스 보안 취약점 관리는 단순히 도구를 사용하는 것에 그치지 않고, 개발 팀의 보안 인식 제고와 함께 체계적인 프로세스 수립이 필요하다. 정기적인 취약점 스캔, 신속한 패치 적용, 그리고 지속적인 모니터링을 통해 오픈소스 사용에 따른 보안 위험을 최소화할 수 있다.

#### 기업의 오픈소스 보안 전략

기업이 오픈소스를 안전하게 활용하기 위해서는 체계적인 보안 전략이 필요하다. 이는 단순히 취약점을 관리하는 것을 넘어 조직 전체의 오픈소스 사용 문화를 개선하는 것을 포함한다.

##### 오픈소스 정책 수립

1. **OSPO(Open Source Program Office) 설립**
   - 오픈소스 사용과 기여에 대한 전략을 수립하고 실행하는 전담 조직
   - 오픈소스 커뮤니티와의 협업 촉진 및 내부 지원 제공[^itworld2024]

2. **보안 중심의 오픈소스 정책 수립**
   - 오픈소스 사용, 기여, 배포에 대한 명확한 가이드라인 제시
   - 보안 취약점 관리 프로세스 정의
   - 신뢰할 수 있는 오픈소스 저장소 지정 및 관리

3. **시프트 레프트 보안(Shift Left Security) 전략 도입**
   - 개발 초기 단계부터 보안 검사 실행
   - CI/CD 파이프라인에 자동화된 보안 검사 도구 통합

##### 개발자 교육 및 인식 제고

1. **정기적인 오픈소스 보안 교육 실시**
   - 오픈소스 사용의 이점과 위험성에 대한 이해 증진
   - 최신 보안 위협 및 대응 방법 교육

2. **보안 코딩 가이드라인 제공**
   - 안전한 오픈소스 사용 방법 및 모범 사례 공유
   - 언어별, 프레임워크별 보안 코딩 기준 제시

3. **내부 오픈소스 포털 운영**
   - 승인된 오픈소스 목록 및 사용 가이드 제공
   - 보안 취약점 정보 및 패치 적용 방법 공유

##### 보안 취약점 대응 프로세스

1. **지속적인 모니터링 체계 구축**
   - 자동화된 취약점 스캐닝 도구 활용
   - 주요 CVE 데이터베이스 및 보안 공지 실시간 모니터링

2. **신속한 취약점 대응 체계 수립**
   - 취약점 심각도에 따른 대응 우선순위 설정
   - 패치 적용 및 검증 프로세스 자동화

3. **비상 대응 계획 수립**
   - 제로데이 취약점 발견 시 신속한 대응 절차 마련
   - 임시 완화 조치(workaround) 적용 방안 준비

| 전략 영역 | 주요 활동 |
|-----------|----------|
| 정책 수립 | OSPO 설립, 보안 중심 정책 수립, 시프트 레프트 전략 도입 |
| 교육 및 인식 제고 | 정기 교육, 보안 코딩 가이드라인, 내부 포털 운영 |
| 취약점 대응 | 지속적 모니터링, 신속한 대응 체계, 비상 계획 수립 |

이러한 전략을 통해 기업은 오픈소스 사용에 따른 보안 위험을 최소화하면서도 오픈소스의 이점을 최대한 활용할 수 있다. 특히 OSPO의 역할이 중요한데, 이는 개발자를 지원하고 오픈소스 보안 모범 사례의 채택을 촉진하는 핵심 조직이 된다[^itworld2024]. 또한, 체크포인트 소프트웨어의 권고처럼 자동화된 DevOps 사례에 보안을 통합하여 개발 과정에서의 보안 관리를 효율화하는 것도 중요하다[^checkpoint2024].

[^itworld2024]: https://www.itworld.co.kr/news/263110
[^checkpoint2024]: https://www.checkpoint.com/kr/cyber-hub/cloud-security/what-is-open-source-security/


#### 하위 공급망 보안 관리

한국의 소프트웨어 개발 환경, 특히 공공 부문과 대기업이 주도하는 SI(시스템 통합) 프로젝트에서 하위 공급망의 보안 관리는 종종 간과되지만 매우 중요한 부분이다. SBOM이 이 문제를 일부 해결할 수 있지만, 더 포괄적인 접근이 필요하다. 아래 표는 하위 공급망에 있는 회사들과의 협력, 모니터링, 관리를 위한 주요 영역과 구체적인 방안을 제시한다.

| 영역 | 방안 | 설명 |
|------|------|------|
| 협력 | 보안 협의체 운영 | - 주 계약자와 하청업체 간 정기적인 보안 회의 개최<br>- 공통 보안 목표 설정 및 진행 상황 공유 |
| | 공동 보안 대응팀 구성 | - 주 계약자와 하청업체의 보안 전문가로 구성된 통합 대응팀 운영<br>- 보안 사고 발생 시 신속한 공동 대응 체계 마련 |
| 교육 | 통합 보안 교육 프로그램 | - 주 계약자 주도의 하청업체 대상 정기 보안 교육 실시<br>- 최신 보안 위협 및 대응 기술에 대한 워크샵 개최 |
| | 보안 기술 멘토링 | - 주 계약자의 보안 전문가가 하청업체 개발자에게 1:1 멘토링 제공<br>- 실제 프로젝트에 적용 가능한 보안 코딩 기법 전수 |
| 모니터링 | 통합 보안 모니터링 시스템 | - 전체 공급망을 아우르는 중앙 집중식 보안 모니터링 구축<br>- 실시간 위협 탐지 및 알림 체계 운영 |
| | 주기적 보안 감사 | - 정기적인 하청업체 보안 실태 점검 및 감사 실시<br>- 감사 결과에 따른 개선 계획 수립 및 이행 관리 |
| 관리 | 보안 성과 평가 체계 | - 하청업체의 보안 관리 수준을 정량적으로 평가하는 지표 개발<br>- 평가 결과에 따른 인센티브 및 페널티 제도 운영 |
| | 보안 요구사항 명확화 | - 계약 단계에서 구체적인 보안 요구사항 명시<br>- 요구사항 충족 여부에 대한 주기적 검토 및 피드백 |

이러한 접근 방식은 한국정보보호산업협회(KISIA)의 [공급망 보안 가이드라인](https://www.kisa.or.kr/2060204/form?postSeq=15&page=1)[^kisia2024]과 [소프트웨어 개발 보안 가이드](https://www.kisa.or.kr/2060204/form?postSeq=5&lang_type=KO&page=1)[^security2024]를 참고하여 수립되었다. 이를 통해 전체 소프트웨어 공급망의 보안을 강화하고, 하위 공급업체의 보안 역량을 향상시킬 수 있다.

특히, 공공 부문 SI 프로젝트에서는 [정보보호 관리체계(ISMS) 인증](https://isms.kisa.or.kr/main/)[^isms2024]을 활용하여 하청업체의 보안 관리 수준을 객관적으로 평가하고 개선할 수 있다. 이는 전체 프로젝트의 보안 수준을 높이는 데 기여할 것이다.

[^kisia2024]: 한국정보보호산업협회, 공급망 보안 가이드라인: https://www.kisa.or.kr/2060204/form?postSeq=15&page=1
[^security2024]: 과학기술정보통신부, 소프트웨어 개발보안 가이드: https://www.kisa.or.kr/2060204/form?postSeq=5&lang_type=KO&page=1
[^isms2024]: 정보보호 관리체계(ISMS) 인증: https://isms.kisa.or.kr/main/



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
GiHub은 소스 코드 저장소로 널리 사용되고 있는데, 최근 [GitHub Octoverse (2021)](https://octoverse.github.com)[^github-octoverse] 자료를 보면, **Fortune 100대 기업 중 84%가 GitHub Enterprise를 사용**하고 있다고 한다. 그에 맞춰 최근 GitHub에서도 단순히 소스 코드 저장소 기능을 넘어 새로운 기능들을 추가하고 있는데, 특히 보안과 관련된 다양한 기능을 제공하고 있어 주목받고 있다. 이러한 보안 기능들을 활용한 보안 관리 사례를 살펴보고자 한다.

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

여기까지 오픈소스 사용하는 데 있어 기업이 활용할 수 있는 가이드를 알아보았다. 이제 개발자는 어떻게 오픈소스를 사용하고 관리해야 하는지를 알아보자.


## 오픈소스 사용 가이드 - 개발자 편

오픈소스는 생태계는 매년 그 규모가 매우 빠르게 발전하고 있다. 
오픈소스 거버넌스 플랫폼을 운영하는 Sonatype 에서 최근 발표한 [소프트웨어 공급망 현황(2021)](https://www.sonatype.com/resources/state-of-the-software-supply-chain-2021)[^sonatype-report]에 따르면 오픈소스 공급은 상위 4개 오픈 소스 생태계(Java, Javascript, Python, .NET)에서만 3천7백만개 이상의 컴포넌트와 패키지가 포함되어 있다.
또한, 2021년에 전 세계 개발자의 오픈 소스 패키지 다운로드 수가 2조 2천억 개 이상이며, 이는 전년 대비 73% 증가한 수치이다.

[^sonatype-report]: Sonatype, State of the Software Supply Chain (2021) : https://www.sonatype.com/resources/state-of-the-software-supply-chain-2021
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
오픈소스 분야에서 유명한 리처드 스톨만이 1985년에 설립한 재단으로 자유(Free) 소프트웨어의 생산과 보급을 장려하고 있다. 주로 컴퓨터 소프트웨어를 만들어 배포하고 수정하는 보편적인 자유를 추구한다.


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
오픈소스 사용 조건과 같은 비기능적인 부분도 반드시 살펴봐야 한다. 프로젝트에서 사용하는 아키텍처나 운영체제와 호환이 되어야 하고, 프로젝트가 현재 Linux에서 작동하지만, Windows도 다음에 확장될 계획이라면 두 시스템 모두 지원하는 오픈소스여야 한다. 그리고 오픈소스의 성능이 조건에 충족하는지 살펴보고, 성능이 중요하다면 벤치마킹을 수행하여 성능을 반드시 측정해보아야 한다.


##### **라이선스**
오픈소스에 명시된 라이선스를 반드시 확인해야 한다. 상업용 프로젝트에 비상업용 라이선스를 가진 오픈소스를 사용하거나, GPL 라이선스를 가진 오픈소스를 사용하게 되어 의도하지 않게 자신의 코드를 전부 공개해야 하는 상황은 피해야 한다. 이 경우 Apache나 MIT와 같은 상대적으로 관대한 허용적 라이선스를 사용하는 오픈소스를 선택하는 것이 바람직하다.


##### **보안**
[소프트웨어 공급망 현황(2021)](https://www.sonatype.com/resources/state-of-the-software-supply-chain-2021)[^sonatype2021]를 보면 인기 있는 상위 10%의 오픈소스 프로젝트에서 취약점을 포함할 가능성이 평균 29%이다. 오픈소스 검토 보안과 관련된 부분을 반드시 확인하고 사용해야 하며, 취약점이 발견되었을 때 빠르게 조치가 이뤄지고 있는지 등도 검토 대상이 되어야 한다. 오픈소스의 마지막 릴리즈가 오래되었다면, 그만큼 보안 취약점을 가지고 있을 가능성이 높다. GitHub 이슈 또는 오픈소스 설명에 명시된 이슈 트래커등을 통해 보안 문제가 있는지 확인하고, 지난 버전 릴리즈 노트를 살펴보자.

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

여기까지 오픈소스 사용하기에 대한 내용들을 살펴보았다. 기업에서 오픈소스를 도입할 때 고려해야 할 사항들과 오픈소스 컴플라이언스, 그리고 라이선스 의무사항과 각종 오픈소스 관리 도구 및 오픈소스 보안 취약점 등에 대해 다뤘다. 기업은 자칫 잘못된 오픈소스 사용으로 인해 기업 이미지에도 큰 타격을 줄 수도 있음을 기억해야 하며, 오픈소스 사용 시 오픈소스 라이선스 의무사항을 준수하지 않아 발생하는 법적 리스크도 반드시 고려해야 한다. 이를 위해서는 전사 차원에서 오픈소스 정책과 프로세스를 수립하는 등 오픈소스를 올바르게 사용하기 위한 지속적인 노력을 기울여야 할 것이다.      

다음 장에서는 기업의 구성원이 외부 오픈소스 개발에 참여하고 직접 기여할 때 기업이 고려해야 할 사항들을 알아보도록 하겠다.
