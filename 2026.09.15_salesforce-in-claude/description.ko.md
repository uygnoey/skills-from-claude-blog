[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Salesforce와 함께 만든 베타 플러그인 Salesforce in Claude를 알리는 글입니다(2026년 9월 15일). 영업
담당자의 계정·영업 기회·파이프라인을 기존 Salesforce 권한 그대로 Claude로 가져오며, 어카운트
이그제큐티브의 일상 업무를 위한 스킬 37개가 들어 있습니다.

## 언제 유용한가요
- 영업 담당자가 Salesforce, 이메일, 통화 녹음, Slack에서 맥락을 모으는 데 시간을 쓸 때.
- 미팅 후 CRM 업데이트가 늦어질 때.
- 관리자가 영업팀에 플러그인을 어떻게 배포할지 계획할 때.

## 핵심 포인트
- Salesforce 커넥터는 CRM 데이터를 읽고 작업하며, Slack 커넥터는 딜 채널 요약과 계정 팀 스레드를
  읽고 씁니다. 처음 쓸 때 설정 스킬이 역할에 맞춘 Claude Artifact를 만듭니다.
- 워크플로: 예약된 아침 브리핑(금요일에는 주간 요약과 매니저 업데이트 초안), 통화 준비, 날짜가 들어간
  상호 클로즈 플랜을 포함한 딜 리뷰, 미팅 후 후속 메일과 영업 기회 업데이트, 공유 가능한 파이프라인·예측
  대시보드.
- Salesforce가 기록 시스템으로 남고, Claude는 담당자 권한이 허용하는 것만 보며 기본적으로 쓰기 전에
  승인을 요청합니다. Team/Enterprise 고객 데이터는 기본적으로 학습에 쓰지 않습니다.
- 모든 유료 플랜에서 베타. Salesforce MCP는 마켓플레이스에서 설치하고, 관리자는 AgentExchange로 접근을
  요청해 조직 전체에 Salesforce를 한 번 연결한 뒤 플러그인을 받을 그룹을 고릅니다.
- GitLab, Siemens, Legora와 Salesforce 영업 담당자 7,000명이 사용 중입니다.

## 번들 리소스
- 스킬: `crm-seller-workflows` (`references/workflows.md`, `references/setup-and-permissions.md`,
  `templates/close-plan.md`, `templates/post-meeting-update.md`).

## 출처
- https://claude.com/resources/articles/salesforce-in-claude
