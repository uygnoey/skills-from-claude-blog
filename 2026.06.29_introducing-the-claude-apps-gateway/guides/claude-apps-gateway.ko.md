[English](./claude-apps-gateway.en.md) · **한국어** · [Español](./claude-apps-gateway.es.md) · [日本語](./claude-apps-gateway.ja.md)

# Claude apps gateway: 배포 및 롤아웃 개요

## 이 가이드가 뭔가요
이 가이드는 원문 글에서 설명한 게이트웨이의 배포/롤아웃 모델을 요약합니다. SSO, 정책 강제, 텔레메트리, 라우팅 기능과 클라이언트 설정 방법을 중심으로 정리했습니다.

## 언제 유용한가요
Amazon Bedrock 또는 Google Cloud에서 Claude Code를 조직 단위로 배포할 때, 중앙 로그인과 정책 강제, 사용자별 사용량 귀속이 필요하다면 빠른 참조로 활용할 수 있습니다.

## 아키텍처(원문 기준)
- **Gateway**: Linux에서 실행되는 단일 무상태 컨테이너, **PostgreSQL** 백엔드.
- **Identity**: 게이트웨이는 IdP(예: Google Workspace, Microsoft Entra ID, Okta)에 대해 **OIDC relying party**로 동작하며, 짧은 수명의 세션을 발급합니다.
- **Policy**: managed settings(정책)은 서버에서 한 번 정의되며, 클라이언트는 로그인 시 이를 수신하고 게이트웨이는 모든 요청에서 강제합니다.
- **Telemetry**: 클라이언트는 요청마다 사용량 메트릭을 찍고, 게이트웨이는 이를 **OTLP**로 설정된 수집기(collector)로 전달합니다.
- **Routing**: 게이트웨이가 상위(업스트림) 자격증명을 보관하며, **Claude API**, **Amazon Bedrock**, **Google Cloud**로 라우팅하고 선택적으로 페일오버를 지원합니다.

## 롤아웃 단계(원문 기준)
1. **게이트웨이 배포**
   - Claude Code CLI 바이너리를 다운로드합니다.
   - `gateway.yaml`에서 OIDC issuer 및 업스트림 자격증명을 지정합니다.
   - IdP에 OIDC 애플리케이션 1개를 등록합니다.
2. **클라이언트에서 게이트웨이 로그인 강제**
   - 개발자 머신에 `managed-settings.json`을 배포합니다.
   - `forceLoginMethod`, `forceLoginGatewayUrl`을 설정해 첫 실행부터 게이트웨이에 연결되도록 합니다.
3. **중앙에서 운영/조정**
   - 허용 모델과 기본 설정을 중앙에서 관리합니다.
   - 수집기로 전달된 텔레메트리로 사용자별 귀속을 수행합니다.
   - 조직/그룹/사용자 단위로 일/주/월 지출 한도를 적용합니다.

## 출처
- https://claude.com/blog/introducing-the-claude-apps-gateway
