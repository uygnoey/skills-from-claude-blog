[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Slack 채널에 Claude를 넣는 Claude Tag(베타)가 이제 구성원 개인의 커넥터를 그 사람의 요청에 쓸 수 있게
되었다는 소식입니다. 이전에는 관리자가 채널에 붙인 커넥터만 쓸 수 있어, 접근 권한이 사람이 아닌 채널을 따라갔습니다.

## 언제 유용한가요
- 채널 구성원이 자기 로그인 뒤에 있는 데이터(캘린더, 본인만 여는 문서, 담당 CRM 계정, 스테이징 배포)가 필요할 때
- 관리자가 Claude Tag 채널의 커넥터 접근 거버넌스를 정할 때
- 무인으로 돌릴 일과 사람이 있어야 할 일을 나눌 때

## 핵심 포인트
- claude.ai/customize에서 도구를 연결하면, 요청이 처음 그 커넥터를 필요로 할 때 Claude가 권한을 묻습니다.
  채널의 다른 사람은 내 커넥터를 쓸 수 없습니다.
- 한 요청 안에서 내 커넥터와 채널 공유 커넥터를 함께 씁니다.
- 리뷰 모드는 게시 전에 매 응답을 보여 주고, 자동 모드는 민감한 내용이 감지될 때만 멈추고 바로 게시합니다.
- 개인 커넥터로 한 작업은 해당 도구의 감사 로그에 내 계정으로 남고, 채널 작업은 채널 서비스 계정으로 남습니다.
  언제든 연결을 끊을 수 있습니다.
- 개인 커넥터는 무인으로 돌지 않습니다. 예약 루틴과 Claude가 스스로 시작하는 작업은 공유 커넥터를 씁니다.
- 관리자 옵션: 에이전트 ID 아래 공유 도구 제공, 기존 역할 기반 접근에 기대는 개인 커넥터 전용 채널,
  도구별 결정. Enterprise 관리자는 모든 사람에게 리뷰를 강제할 수 있습니다.
- Team 플랜부터 순차 적용, Enterprise는 이후.

## 번들 리소스
- Skill: `slack-personal-connectors` — 개인 vs 공유 커넥터, 게시 모드, 거버넌스(`examples/channel-scenarios.md`).

## 출처
- https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels
