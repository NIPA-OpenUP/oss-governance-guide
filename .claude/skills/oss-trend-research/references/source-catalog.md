# 축별 1차 출처 카탈로그

조사 시작 시 **자신의 축 절만** 읽는다. 전체를 읽을 이유가 없다.

이 카탈로그는 출발점이며 완결 목록이 아니다. 카탈로그에 없는 1차 출처를 찾았으면 그것을 쓰고, 반복해서 유용했으면 `harness:evolve`로 이 파일에 추가한다. 조직명·URL은 변할 수 있으므로 접근 실패 시 조직명으로 재검색한다.

## 목차

1. [regulation 축](#1-regulation-축)
2. [security 축](#2-security-축)
3. [ai 축](#3-ai-축)
4. [market 축](#4-market-축)
5. [tooling 축](#5-tooling-축)
6. [공통 규칙](#6-공통-규칙)

---

## 1. regulation 축

**EU**
- EUR-Lex (eur-lex.europa.eu) — 규정·지침 원문과 개정 이력. CRA, AI Act, NIS2, PLD의 확정 텍스트는 여기가 유일한 1차 출처다.
- European Commission 디지털 정책 페이지 — 시행 일정과 가이던스 문서.
- ENISA — 기술 이행 가이던스.

**미국**
- Federal Register (federalregister.gov) — 행정명령·규칙 원문.
- CISA — SBOM 관련 실무 문서와 최소 요구 사항 갱신.
- NIST (SSDF SP 800-218 등) — 보안 개발 프레임워크.
- FDA — 의료기기 SBOM 요건.

**국제 표준**
- ISO (iso.org) — ISO/IEC 5230(오픈소스 컴플라이언스), ISO/IEC 18974(보안 보증), ISO/IEC 5962(SPDX). 판번호와 개정 연도를 확인한다.
- OpenChain Project — 표준 원문과 인증(self-certification) 절차, 한국 워킹그룹 자료.
- ECMA/Linux Foundation — SPDX·CycloneDX 표준화 상태.

**국내**
- 국가법령정보센터 (law.go.kr) — 소프트웨어진흥법, 정보통신망법 등 원문·시행일.
- 과학기술정보통신부 / KISA / NIPA 보도자료 — 정책 발표와 사업 공고.
- 공공 조달 관련: 조달청 규격, 행정안전부 지침.

> 국내 정책은 "예정"으로 발표된 뒤 시행이 미뤄지는 경우가 많다. 발표 시점과 시행 시점을 반드시 분리해 기록한다.

## 2. security 축

**프레임워크·표준**
- OpenSSF (openssf.org) — Scorecard, Best Practices Badge, Alpha-Omega, 각종 워킹그룹 산출물.
- SLSA (slsa.dev) — 레벨 정의와 요구사항. 버전에 따라 레벨 정의가 바뀌었으므로 판번호 확인 필수.
- in-toto, Sigstore (sigstore.dev) — 서명·증명 체계.
- CycloneDX VEX / OpenVEX — 취약점 활용성 표현 형식.

**취약점 데이터**
- OSV (osv.dev) — 오픈소스 취약점 DB와 스캐너.
- NVD (nvd.nist.gov) — CVE와 CVSS. NVD의 처리 지연 이슈는 그 자체가 가이드에 쓸 만한 사실이다.
- CISA KEV 카탈로그 — 실제 악용 확인된 취약점.
- FIRST — CVSS 명세, EPSS 점수.
- GitHub Security Advisories / GHSA.

**사고 사례**
- 패키지 레지스트리 공식 블로그 (npm/PyPI/Maven Central) — 악성 패키지 사고 공지.
- 프로젝트 자체 공지 — 사고의 1차 출처는 피해 프로젝트의 공식 발표다.
- 벤더 보고서는 2차 출처로 취급한다.

## 3. ai 축

**오픈소스 AI 정의**
- OSI (opensource.org) — Open Source AI Definition(OSAID) 판번호, 승인 라이선스 목록, 정의를 둘러싼 논쟁 기록.
- Linux Foundation / LF AI & Data — Model Openness Framework, OpenMDW 등 라이선스 프레임워크.

**모델·데이터셋 라이선스 원문**
- 모델 배포처의 라이선스 파일 원문 (Hugging Face 모델 카드의 LICENSE, 벤더 공식 라이선스 페이지). **요약본이 아니라 조항 원문을 읽는다.**
- RAIL (licenses.ai) — 책임 있는 AI 라이선스 계열.
- Creative Commons — 데이터셋 라이선스.

**AI BOM**
- SPDX 3.x 명세의 AI/Dataset 프로필.
- CycloneDX ML-BOM 명세.

**연구**
- arXiv — 프리프린트. **피어리뷰 여부를 반드시 기록**하고 확정 연구로 인용하지 않는다.
- ACM/IEEE 학회 논문 (MSR, ICSE, FSE 등) — 소프트웨어 공학 실증 연구.
- 법률 저널·판례 — 저작권 쟁점은 진행 상태로만 기록한다.

## 4. market 축

**연례 보고서 시리즈** (기존 원고가 인용한 것 우선 갱신)
- Black Duck(구 Synopsys) OSSRA — 오픈소스 보안·라이선스 리스크 연례 보고서. 원고의 핵심 인용원이다.
- Perforce / OpenLogic State of Open Source Report.
- Red Hat State of Enterprise Open Source.
- GitHub Octoverse.
- TODO Group OSPO Survey — 원고의 OSPO 장 핵심 인용원.
- Linux Foundation Research 보고서.
- Sonatype State of the Software Supply Chain.
- Tidelift / OpenSSF 유지관리자 설문.

**국내 통계**
- NIPA / 정보통신산업진흥원 — 국내 오픈소스 시장 조사, OSS 실태조사.
- 오픈업(oss.kr) — 국내 발간 가이드와 사업 자료. 이 가이드 자체의 발행 주체다.
- 한국소프트웨어산업협회, SPRi(소프트웨어정책연구소).

**기업 사례**
- 기업 공식 기술 블로그와 오픈소스 사이트 (예: 각 사의 opensource.* 도메인).
- 기업이 공개한 OSPO 저장소·정책 문서.
- 콘퍼런스 발표 자료 (OSS Summit, OpenChain 워크숍, 국내 오픈소스 콘퍼런스).

> 사례는 **공개 확인 가능한 것만** 쓴다. 내부 프로세스 추정은 사례가 아니다.

## 5. tooling 축

**도구별 1차 확인 경로**
- GitHub/GitLab 저장소 — 최근 릴리스, 커밋 활동, 아카이브 여부, LICENSE 파일.
- 프로젝트 공식 문서 사이트 — 지원 SBOM 포맷, 연동 대상.
- 상용 제품 공식 페이지 — 제품명·회사명 변경 확인 (이 영역은 인수·리브랜딩이 잦다).

**확인 체크리스트 (도구당)**
1. 저장소가 아카이브되었는가
2. 최근 릴리스 시점과 버전
3. 라이선스가 바뀌었는가 (오픈소스 → 소스 공개 라이선스 전환 사례 다수)
4. 제품명·회사명이 바뀌었는가
5. 지원하는 SBOM 포맷과 판번호
6. 원고의 로고 이미지가 현재 브랜드와 일치하는가

**주요 확인 대상** (원고 등재분 + 신규 후보)
- 오픈소스: FOSSLight, SW360, ScanCode Toolkit, ORT(OSS Review Toolkit), Syft, Grype, Trivy, Dependency-Track, OSV-Scanner, ClearlyDefined, Fossology, SPDX 도구군
- 상용: Black Duck, FOSSA, Snyk, Mend(구 WhiteSource), Revenera(구 Flexera/Palamida), Insignary, Checkmarx, Sonatype
- 국내: Olive(LG전자), 기타 국내 상용 도구

> 회사·제품명이 바뀐 도구는 원고에 "구 OOO" 병기가 필요하다. 독자가 자사에서 쓰던 이름과 연결해야 한다.

## 6. 공통 규칙

- **URL은 최종 리다이렉트 주소로 기록한다.** 단축 URL·리다이렉트 URL은 원고에서 먼저 죽는다.
- **PDF 직링크에는 랜딩 페이지 URL을 함께 기록한다.**
- **접근 실패는 조직명으로 재검색한다.** URL 구조는 사이트 개편으로 바뀌지만 조직과 문서는 남아 있다.
- **유료 장벽 뒤의 보고서**는 공개 프레스 릴리스의 수치를 쓰고 원문 미확인을 기록한다.
- **한국어 자료와 영어 자료를 모두 확인한다.** 국내 규제·시장은 한국어 1차 출처만 존재하고, 국제 표준은 영어 원문이 정확하다.
