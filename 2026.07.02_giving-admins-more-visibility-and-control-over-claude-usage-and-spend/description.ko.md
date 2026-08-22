[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Anthropic이 Claude Enterprise를 위한 더 풍부한 관리자 애널리틱스, 모델 단위 권한(entitlement), 지출 알림을 도입했다. 전제는 이렇다. Claude가 조직 전반에서 점점 더 어렵고 복잡한 에이전틱 작업을 맡게 되면서 사용량·비용 패턴이 일반 채팅 도구와 달라졌고, 따라서 관리자에게는 Claude가 어떻게 쓰이는지 파악할 가시성과 비용을 조절할 레버가 함께 필요하다는 것이다.

가시성 쪽: 그룹별·사용자별로 분해되고 IT가 이미 관리하는 SCIM 그룹으로 필터링되며 산출물(생성된 아티팩트, 편집된 파일, 사용된 스킬과 커넥터)을 해당 비용 바로 옆에 보여주는 애널리틱스 대시보드, 사용량과 가치를 분리한 Claude Code의 새 탭 두 개(모든 가치 산식이 노출되고 입력값 조정 가능), 평이한 언어 질문에 내보내기 가능한 차트로 답하는 애널리틱스 챗, 그리고 동일한 데이터를 Datadog Cloud Cost Management·CloudZero 등 재무와 IT가 이미 쓰는 도구로 끌어오는 Analytics API.

제어 쪽: 일상 업무가 가장 비싼 모델에서 시작되지 않도록 하는 모델 기본값과 권한, 관리자 75%/90%·사용자 75%/95%의 지출 임계값 알림, 그리고 손으로 관리하기엔 그룹이 너무 많아졌을 때 비용 제어 워크플로를 스크립트로 옮기는 Admin API. 이 모두는 이미 제공되던 제어 — 모든 계층의 지출 상한, 접근 및 모델 라우팅, 내보내기를 갖춘 사용량 대시보드, effort 제어 — 위에 얹힌다.

## 언제 유용한가요
- 조직의 사용량·비용 패턴이 채팅이 아니라 에이전틱 작업의 모습을 띠기 시작할 때.
- 재무나 IT가 Claude 사용량·비용을 나머지 클라우드·AI 지출과 나란히 놓아야 할 때.
- 일상적인 작업이 사용 가능한 가장 비싼 모델로 기본 설정되고 있을 때.
- 사용자가 작업 도중 지출 한도에 걸리는데 아무도 미리 알아채지 못할 때.
- 팀별·시트별로 이 배포가 어떤 가치를 돌려주는지 답해야 하고, 그 답이 검증을 견뎌야 할 때.
- 그룹별 한도가 관리자가 클릭으로 검토할 수 있는 범위를 넘어섰을 때.

## 핵심 포인트
- **그룹별·사용자별 사용량과 비용**을 보여주고, 생성된 아티팩트·편집된 파일·사용된 스킬과 커넥터 같은 산출물을 해당 비용 바로 옆에 배치하며, 기존 SCIM 그룹으로 필터링된다.
- **Claude Code는 사용량과 가치를 분리한다.** 사용량: 활성 개발자, 세션 수, 상위 명령(매일 갱신). 가치: 생산성 향상, 커밋당 비용, 연간 가치 — 모든 산식이 노출되고 입력값을 조정할 수 있다.
- **애널리틱스 챗은 평이한 언어 질문을 받는다** ("이번 달 Claude 사용량이 두 배가 된 팀은?", "시트당 가치가 가장 높은 곳은?"). 답은 내보내서 공유할 수 있는 차트다.
- **Analytics API는 기간·팀·제품·모델로 필터링**되며, 스킬은 자체 사용량과 비용을 보고하고, 새 엔드포인트가 플러그인 도입과 아티팩트 생성을 추적한다. 명시된 연동 대상: Datadog Cloud Cost Management, CloudZero.
- **사용자가 자기 사용량을 볼 수 있다** — 시간에 따른 추세, 가장 많이 의존하는 제품·모델·스킬, 그것이 지출로 쌓이는 정도. 예고 없는 차단을 막기 위해서다.
- **모델 기본값과 권한**은 chat·Cowork·Claude Code 전반에서 새 대화가 어떤 모델로 시작할지, 그리고 어떤 역할이 어떤 모델에 접근할 수 있는지를 정한다.
- **지출 임계값 알림은 관리자에게 75%·90%**, **사용자에게 인앱 75%·95%**에 발생하며, 사용자는 Claude를 벗어나지 않고 관리자에게 상향을 요청할 수 있다.
- **Admin API는 세 가지 워크플로를 스크립트화한다.** 상향 요청 검토, 지출 한도에 근접한 구성원 식별, 급격한 사용량 변화 표시.
- **글에 등장하는 세 가지 이해관계자 관점:** 월말의 놀라움이 아니라 주기적 점검 자극으로서의 비용 가시성, ROI 논증을 위해 팀별로 비용과 비즈니스 임팩트를 나란히 읽기(한 CIO는 엔터프라이즈 MCP 서버에 연결된 Claude를 4% 매출 상승과 연결짓는다), 그리고 토큰 수보다 조직 전반에서 반복 실행되는 스킬이 진짜 가치 신호라는 관점.

## 번들 리소스
- `skills/usage-and-spend-governance/SKILL.md` — 계측 먼저, 제어는 그다음: 그룹별 분해, 사용량과 가치 분리, 사용자 가시성 확장, 기본값·권한 설정, 두 계층 알림 구성, 나머지는 스크립트화.
- `skills/usage-and-spend-governance/references/analytics-surfaces.md` — 다섯 가지 표면(대시보드, Claude Code 탭, 애널리틱스 챗, Analytics API, 사용자 단위 가시성)과 각각이 보여주는 것.
- `skills/usage-and-spend-governance/references/spend-controls.md` — 모델 기본값, 권한, 두 계층 알림 비교, 그리고 이번 기능이 얹힌 기존 제어들.
- `skills/usage-and-spend-governance/references/admin-api-workflows.md` — Admin API의 세 가지 명시된 워크플로와, 원문이 엔드포인트 형태까지는 공개하지 않았다는 명시적 주석.
- `skills/usage-and-spend-governance/examples/analytics-questions.md` — 원문의 두 질문에 더해, API가 노출하는 필터 차원에 매핑한 질문 유형들.
- `skills/usage-and-spend-governance/templates/rollout-checklist.md` — SCIM 전제조건부터 가시성·제어·연동·확장까지 순서대로 정리한 체크리스트.
- `guides/admin-analytics-and-cost-controls.{en,ko,es,ja}.md` — 4개 언어 전체 가이드.

## 출처
["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend) — Anthropic, 2026년 7월 2일 게시.
