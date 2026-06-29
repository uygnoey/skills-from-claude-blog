[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude apps gateway를 소개합니다. 이는 조직이 Amazon Bedrock 및 Google Cloud에서 Claude Code를 운영할 때, 인증·정책·비용 통제를 중앙에서 관리할 수 있도록 하는 자체 호스팅 게이트웨이입니다.

## 언제 유용한가요
개발자마다 별도의 클라우드 자격증명을 발급하지 않고도 Claude Code를 대규모로 배포하고 싶을 때 유용합니다. 동시에 모델/기본값 같은 조직 정책을 일관되게 강제하고, 사용자별 비용 귀속과 지출 한도를 적용할 수 있습니다.

## 핵심 포인트
- 게이트웨이는 Linux에서 실행되는 단일 무상태 컨테이너로 배포되며, PostgreSQL 데이터베이스를 백엔드로 사용합니다.
- 상위(업스트림) 제공자 자격증명을 게이트웨이가 보관하고, 개발자는 IdP(OIDC)로 인증합니다.
- Managed settings(정책)은 서버에서 한 번 정의되며, 클라이언트 로그인 시 적용되고 모든 요청에서 강제됩니다.
- 클라이언트는 요청마다 사용량 메트릭을 찍고, 게이트웨이는 이를 OTLP로 조직의 수집기(collector)로 전달합니다.
- Claude API, Amazon Bedrock, Google Cloud로 라우팅할 수 있으며, 선택적으로 제공자 간 페일오버를 지원합니다.
- 일/주/월 지출 한도를 조직·그룹·사용자 단위로 적용할 수 있습니다.

## 번들 리소스
- 글에서 언급된 예시 설정 파일: `gateway.yaml`, `managed-settings.json` (예: `forceLoginMethod`, `forceLoginGatewayUrl`).
- 게이트웨이는 개발자들이 이미 설치하는 동일한 `claude` CLI 바이너리에 포함되어 제공됩니다.

## 출처
- https://claude.com/blog/introducing-the-claude-apps-gateway
