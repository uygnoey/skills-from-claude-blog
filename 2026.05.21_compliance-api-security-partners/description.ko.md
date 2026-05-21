[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude가 더 많은 보안·컴플라이언스 도구와 연결됩니다

## 이 글이 뭔가요

2026년 5월 21일 Anthropic이 발표한 **Claude Compliance API** 기반의 보안·컴플라이언스 통합 28종 공개 글입니다. IT·보안팀이 자사 스택의 다른 애플리케이션을 다루듯 Claude Enterprise와 Claude Platform 전반에 동일한 거버넌스를 적용할 수 있게 해줍니다. 본문은 API가 노출하는 데이터, 카테고리별 통합 범위, 28개 런치 파트너, 그리고 고객·파트너의 다음 단계를 정리합니다.

## 언제 유용한가요

- IT·보안팀이 기존 DLP·SASE·SIEM·아이덴티티·eDiscovery·AI-SPM·AI 옵저버빌리티 스택에 Claude를 어떻게 꽂을지 검토할 때.
- 자체 통합을 구축할지, 현재 사용하는 보안·컴플라이언스 벤더의 Claude 커버리지를 확장할지 결정할 때.
- 보안·컴플라이언스 플랫폼 벤더가 통합 네트워크에 합류할지 판단할 때.
- CISO·CRO 사인오프를 위한 Claude Enterprise/Platform 거버넌스 스토리를 정리할 때.

## 핵심 포인트

- 28개 통합 모두의 기반은 Claude Compliance API.
- API가 엔터프라이즈 보안·컴플라이언스 팀에 프로그래매틱하게 노출하는 **두 가지 데이터 타입**:
  - **Claude Enterprise의 대화 콘텐츠** — 채팅, 업로드된 파일, 프로젝트. 다른 워크플레이스 앱에 이미 적용 중인 보안·모니터링·DLP 정책을 Claude에도 그대로 적용 가능.
  - **Claude Enterprise와 Claude Platform 전반의 활동 이벤트** — 사용자 로그인, 관리자 액션, 구성 변경. 사용 현황을 통합 뷰로 확보.
- 28종 런치 통합의 **커버리지 카테고리**: DLP, SASE, 데이터 보안, SIEM·보안 운영, 아이덴티티, eDiscovery, AI security posture management, AI 옵저버빌리티·텔레메트리 인프라.
- **28개 런치 파트너**: Cloudflare, Cribl, CrowdStrike, Cyera, Datadog, Forcepoint, Fortinet, Geordie AI, IBM Guardium, Microsoft Purview, Mimecast, Netskope, Okta, Palo Alto Networks, Proofpoint, Relativity, ReliaQuest, Rubrik, SailPoint, Smarsh, Snyk, Sumo Logic, Tenable, Theta Lake, Trellix, Varonis, Wiz(현재 Google Cloud 소속), Zscaler.
- **고객 온보딩** — Claude 인스턴스를 파트너 플랫폼에 connect/configure 하면, 이미 사용 중인 대시보드·알람 워크플로우로 데이터가 흐름.
- **파트너 온보딩** — Compliance API 통합을 만든 보안·컴플라이언스·IT 플랫폼은 네트워크 합류 신청 가능.

## 번들 리소스

- `skills/governance-via-compliance-api/SKILL.md` — 기존 스택에 맞는 Compliance API 통합을 고르고 Claude 거버넌스를 설계하기 위한 플레이북.
- `skills/governance-via-compliance-api/references/launch-partners-by-category.md` — 본문 카테고리별로 정리한 파트너 원문 카탈로그.
- `skills/governance-via-compliance-api/examples/dlp-and-siem-wiring.md` — Claude Enterprise·Platform 전반에 DLP·SIEM 커버리지를 엮은 작동 예시.

## 출처

- [Claude now works with more security and compliance tools](https://claude.com/blog/compliance-api-security-partners) (Anthropic 블로그, 2026년 5월 21일)
