[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude Enterprise에 **인라인 데이터 유출 방지(DLP)** 를 추가하는 보안 기능 **inference hooks**를 소개하는 발표 글입니다. 기능을 켜면 모든 추론 요청이 조직이 관리하는 보안 서버로 서명된 WebSocket 연결을 통해 전달됩니다. 모델이 생성을 시작하기 전에 Claude가 프롬프트와 주변 컨텍스트를 그 서버로 보내 allow/deny 판정을 받고, 판정을 받은 뒤에야 진행합니다. 도구 호출 응답도 모델로 돌아가기 전에 동일하게 검사됩니다.

이전에는 네이티브 인라인 강제가 Claude Code의 클라이언트 측 훅에 한정되어 있었습니다. inference hooks는 채팅, Claude Code, Claude Cowork, 그리고 MCP 커넥터·스킬·플러그인을 통한 도구 호출까지 Claude Enterprise 표면 전반에 하나의 강제 계층을 확장하며, 제품별 개별 연동 작업이 필요 없습니다.

## 언제 유용한가요
- 민감 데이터가 오갈 수 있는 모든 경로가 보안팀이 통제하는 검사 지점을 통과해야 할 때.
- 기존 DLP 프로그램(Netskope, Palo Alto Networks, Proofpoint, Zscaler 또는 자체 구축 서버)을 AI 사용까지 확장하고 싶을 때.
- Claude 제품마다 따로 연동하지 않고 조직 수준 설정 하나로 커버하고 싶을 때.
- 강제 적용 전에 shadow 모드, 예외 대상, 비율 기반 단계 확대가 필요한 롤아웃을 계획할 때.

## 핵심 포인트
- **생성 이전 검사.** 프롬프트와 컨텍스트가 모델 생성 전에 서버로 전달되고, Claude는 판정을 받은 뒤에만 진행합니다.
- **도구 응답도 검사 대상**이며, MCP 커넥터·스킬·플러그인을 통해 호출된 도구도 포함됩니다.
- **공개 스키마를 갖춘 개방형 webhook 기반 프로토콜**이라 기존 DLP 서버를 그대로 재사용할 수 있고, 보안 벤더는 자체 통합을 만들 수 있습니다.
- **조직 수준 스위치 하나**로 Claude Enterprise 표면을 덮습니다. 제품마다 연동을 만들 필요가 없습니다.
- **롤아웃 제어**: shadow 모드(항상 허용), 역할 기반 예외, 비율 기반 롤아웃, 그리고 실패 정책과 타임아웃 설정.
- 글 작성 시점에 **Claude Enterprise 고객 대상 베타**로 제공됩니다.
- 이름이 겹치는 점에 주의하세요. 여기서 말하는 것은 *서버 측 inference hooks*이며, Claude Code의 클라이언트 측 라이프사이클 훅(PreToolUse, PostToolUse 등)과는 다릅니다.

## 번들 리소스
- `skills/inference-dlp-rollout/SKILL.md` — 사용자를 막지 않으면서 인라인 DLP를 켜는 단계별 롤아웃 절차.
- `skills/inference-dlp-rollout/references/enforcement-model.md` — 검사가 일어나는 지점과 각 제어 항목의 역할.
- `skills/inference-dlp-rollout/templates/rollout-plan.md` — 채워 쓰는 롤아웃·결정 로그 템플릿.
- `guides/inline-dlp-for-claude-enterprise.{en,ko,es,ja}.md` — 4개 언어 아키텍처·배포 가이드.

## 출처
- https://claude.com/blog/claude-enterprise-inference-hooks
