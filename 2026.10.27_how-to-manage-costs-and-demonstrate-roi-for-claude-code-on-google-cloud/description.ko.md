[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
2026년 10월 27일에 나온 모범 사례 글로, Google Cloud 와 함께한 웨비나를 바탕으로 합니다. 플랫폼 팀이
Google Cloud 에서 Claude Code 비용을 관리하고 그 가치를 증명하는 방법을 통제(control), 추적(track),
증명(prove)이라는 세 가지 독립된 레버로 설명합니다.

## 언제 유용한가요
- Google Cloud 에서 Claude Code 를 도입하면서 가드레일, 예산, 모델 정책이 필요할 때.
- 지출이 늘어나 가치 높은 파워 유저 사용과 낭비를 구분해야 할 때.
- 사용량 대시보드를 만들거나 경영진에게 Claude Code 의 ROI 를 보여 줘야 할 때.

## 핵심 포인트
- 청구액은 작업당 토큰 수 × 모델 가격입니다. 에이전트형 작업은 채팅보다 작업당 토큰을 더 쓰므로
  작업에 맞는 모델을 고르는 것이 큰 레버입니다. 토큰당 가격보다 작업당 비용이 더 중요합니다.
- 도구 상자: Google Cloud 의 프로젝트별 결제, 예산·알림, 지출 상한(Preview), BigQuery 내보내기,
  할당량, 프로비저닝된 처리량, 그리고 IdP 로그인을 붙인 자체 호스팅 Claude apps gateway.
- 통제 - 막지 말고 이끌기: 사용자·IdP 그룹·조직 단위로 일·주·월 지출 상한(공유 풀이 아니라 구성원마다
  상속되는 1인당 기본값), 75%·95% 를 넘으면 CLI 안 경고, 상한에서 429, 그룹별 기본 모델과 허용 목록,
  상한을 바꾸는 admin API. 낭비는 고액 사용자 중간층(일상 작업에 비싼 모델, 잊힌 예약 작업)에 숨어 있습니다.
- 추적: 사용자·팀·모델·스킬·플러그인·에이전트·MCP 서버별 Claude Code OpenTelemetry, 검증된 신원으로
  태그되는 gateway 관리형 텔레메트리, 비용 센터용 `OTEL_RESOURCE_ATTRIBUTES`, Cloud Monitoring 대시보드
  템플릿, 이벤트를 BigQuery 에 넣고 SQL 을 제공하는 OTel 퀵스타트, Cloud Billing 의 BigQuery 내보내기.
- 증명: 도입·사용, 개발자 만족도(도입 전후 설문), 기준선 대비 임팩트(시간·노력·양). 라벨 붙은 병합 PR
  같은 작업 단위를 정의합니다. 텔레메트리의 "생성된 PR" 은 "병합된 PR" 이 아니므로 소스 관리·티켓과
  대조합니다. 프롬프트 로깅은 옵트인입니다.
- 고객 사례: Delivery Hero, Shopify, Fifth Dimension. 기본값(조직 전체 상한, 기본 모델, 허용 목록)으로
  시작해 역할·팀별로 다듬는 연속 루프를 돌립니다.

## 번들 리소스
- 스킬: `coding-agent-spend-roi` (`references/governance-toolbox.md`, `references/telemetry-and-tracking.md`,
  `references/roi-metrics.md`, `references/resources.md`, `examples/customer-outcomes.md`,
  `templates/rollout-defaults.md`, `templates/roi-report.md`, `templates/otel-resource-attributes.env`).
- 가이드: `guides/cost-and-roi-on-google-cloud.{en,ko,es,ja}.md`.

## 출처
- https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
