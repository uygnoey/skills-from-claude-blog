[English](./getting-started.en.md) · **한국어** · [Español](./getting-started.es.md) · [日本語](./getting-started.ja.md)

# Integrations와 advanced Research 시작 가이드

[Claude can now connect to your world](https://claude.com/blog/integrations) (2025-05-01, 업데이트 2025-06-03)을 바탕으로 정리한 짧은 가이드입니다. 무엇부터 켤지, 연결 앱 카탈로그를 어떻게 바라볼지, 연결을 활용하는 Research 요청을 어떻게 짤지 다룹니다.

## 1. 플랜 가용성 확인

2025-06-03 업데이트 이후 Integrations와 advanced Research는 Pro·Max·Team·Enterprise에서 사용할 수 있습니다. 웹 검색은 **모든** Claude 플랜에서 글로벌입니다.

게시일 기준으로 보면, Integrations와 Research는 Max·Team·Enterprise 베타였고 웹 검색은 유료 플랜 글로벌이었습니다.

## 2. 처음 연결할 앱 고르기

출시 라인업(Atlassian Jira, Atlassian Confluence, Zapier, Cloudflare, Intercom, Asana, Square, Sentry, PayPal, Linear, Plaid)에서 선택합니다. 미지원 앱이면 Zapier Integration의 사전 정의 워크플로우로 우회할 수 있는지 확인하세요. 글 시점 로드맵에는 Stripe, GitLab, Box가 언급되어 있습니다.

후보별로 다음을 적어 두세요: 어떤 Claude 작업이 이 데이터에 접근해야 하는가, Claude가 어떤 액션을 취해야 하는가, 조직이 허용하는 인증 모델은 무엇인가.

## 3. Integrations 화면에서 연결

각 Integration은 원격 MCP 서버를 사용합니다. 연결되면 Claude가 컨텍스트(프로젝트 이력·태스크 상태·조직 지식)를 읽고 해당 앱 전반에 액션을 취할 수 있습니다.

자체 Integration을 만들려는 빌더는 Cloudflare 호스팅을 활용할 수 있습니다. OAuth·전송·배포가 기본 포함되어 있으며, 글에 따르면 새 Integration을 30분 만에 만들 수 있다고 합니다.

## 4. advanced Research 요청 실행

- **Research** 버튼을 켭니다.
- 요청은 브리프처럼 작성합니다: 질문, 범위, 검색에 포함할 연결 앱을 명시.
- 일반적으로 5~15분, 복잡한 조사는 최대 45분.
- 결과 리포트의 인용 링크를 직접 확인한 뒤 사용합니다.

## 5. 첫 워크플로우 제안

- Zapier 활용: HubSpot 매출 가져오기, 캘린더 기반 미팅 브리프 준비.
- Atlassian 활용: Confluence 스페이스 요약, 킥오프 문서에서 Jira 항목 일괄 생성.
- Intercom + Linear: 반복되는 사용자 피드백 패턴을 찾아낸 뒤, MCP 클라이언트로 동작하는 Fin이 같은 대화 안에서 Linear 버그 티켓 생성.

## 출처

[Claude can now connect to your world](https://claude.com/blog/integrations) (게시 2025-05-01, 업데이트 2025-06-03).
