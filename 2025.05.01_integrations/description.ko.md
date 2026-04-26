[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude가 이제 당신의 세계와 연결됩니다

## 이 글이 뭔가요

원격 MCP 서버를 통해 Claude를 앱·도구에 연결하는 **Integrations** 출시 발표와, **advanced Research** 확장 발표입니다. 둘을 함께 쓰면 Claude가 업무 앱에서 컨텍스트를 가져오고, 웹·Google Workspace를 검색하며, 5~45분 안에 출처가 달린 종합 리포트를 만들 수 있습니다. 2025-05-01 최초 게시, 2025-06-03 업데이트로 Pro 플랜까지 확장되었고 웹 검색은 모든 유료 플랜에서 글로벌로 제공됩니다.

## 언제 유용한가요

- 서드파티 앱을 별도 자동화 대신 Integrations로 Claude에 연결할지 판단할 때
- 수 시간이 걸리는 다출처 조사를 advanced Research로 대체할 계획을 세울 때
- 팀에 Integrations + Research 워크플로우를 도입하면서 어떤 앱부터 연결할지 표준화할 때
- 출시 시점에 어떤 서비스가 지원됐고, 어떤 것이 로드맵에 있었는지 빠르게 확인할 때

## 핵심 포인트

- Integrations는 웹·데스크톱 전반의 **원격 MCP 서버**에 Claude를 연결합니다. 2024년 11월 MCP 출시 당시 Claude Desktop의 로컬 서버에만 한정되던 지원이 확장된 것입니다.
- 출시 라인업 10종: **Atlassian Jira, Atlassian Confluence, Zapier, Cloudflare, Intercom, Asana, Square, Sentry, PayPal, Linear, Plaid**. 로드맵에 **Stripe, GitLab, Box** 언급.
- 개발자는 30분 만에 자체 Integration을 만들 수 있고, Cloudflare가 OAuth·전송·배포를 기본 제공합니다.
- 구체 사례: Zapier로 수천 개 앱과 사전 정의 워크플로우 연결(예: HubSpot 매출 가져오기, 캘린더 기반 미팅 브리프 준비), Atlassian으로 제품 기획·Confluence/Jira 일괄 업데이트, Intercom의 AI 에이전트 **Fin**이 MCP 클라이언트로 동작해 사용자 제보를 받아 Linear 버그 티켓 생성.
- Advanced Research는 요청을 하위 조사로 분해해 수백 개 소스를 탐색하고 **5~45분** 안에 인용 포함 리포트를 반환합니다. 이제 웹·Google Workspace는 물론 **연결된 Integration까지** 검색합니다.
- **가용성**: 출시 시점에 Integrations와 advanced Research는 Max·Team·Enterprise 베타, 웹 검색은 유료 플랜 글로벌. 2025-06-03 업데이트 후 Integrations·Research는 Pro·Max·Team·Enterprise, 웹 검색은 모든 Claude 플랜에서 글로벌.

## 번들 리소스

- [skills/connected-tools-research-playbook/SKILL.md](./skills/connected-tools-research-playbook/SKILL.md): Integrations + Research 사용 패턴
- [references/launch-services.md](./skills/connected-tools-research-playbook/references/launch-services.md): 글에 언급된 도구/서비스 목록
- [examples/example-workflows.md](./skills/connected-tools-research-playbook/examples/example-workflows.md): 글에 등장한 구체 워크플로우 예시
- [guides/getting-started.ko.md](./guides/getting-started.ko.md) (+ en/es/ja): Integrations와 Research 활성화·사용 방법

## 출처

[Claude can now connect to your world](https://claude.com/blog/integrations) (게시일 2025-05-01, 업데이트 2025-06-03) 내용을 바탕으로 정리했습니다.
