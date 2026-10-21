[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude Platform에서 Claude Managed Agents, Messages API, Claude SDK의 OpenTelemetry(OTel) 트레이스를
내보낼 수 있게 되었다는 발표입니다. 어떤 OTel 도구에서든 에이전트의 각 단계를 따라갈 수 있습니다.

## 언제 유용한가요
- Claude Platform으로 만든 에이전트를 단계별로 들여다보고 싶을 때.
- 느리거나 실패한 에이전트 단계를 나머지 스택과 함께 디버깅할 때.
- 프로덕션 트레이스를 eval로 바꾸거나 팀별 토큰 사용량을 추적할 때.

## 핵심 포인트
- 모든 에이전트 턴, 모델 호출, 도구 사용(MCP 서버 호출 포함)이 지연 시간·토큰·ID가 담긴 표준 OTel
  트레이스로 도착합니다.
- 트레이스는 OpenTelemetry GenAI 시맨틱 컨벤션을 따르므로 Claude와 다른 제공사의 데이터를 같은 도구와
  대시보드에서 볼 수 있습니다. Claude Code·Cowork 트레이스와도 같은 곳에 모을 수 있습니다.
- 신뢰는 근거와 함께 커집니다: 에이전트의 트레이스를 검토하고, 신뢰할 만하다고 확인되면 권한을 넓힙니다.
- 언급된 도구: Grafana Cloud, Honeycomb, Sentry, Splunk(디버깅) / Arize AI, Braintrust, Datadog, Langfuse,
  LangSmith, New Relic, PostHog(eval·품질) / Databricks Unity Gateway(조직 사용량). OTLP 호환 도구라면 모두 가능.
- 퍼블릭 베타. Managed Agents와 Messages API는 Claude Console에서 destination을 추가해야 하고, SDK는
  자동으로 내보냅니다.
- Foxglove, Ramp(Reflect로 일부 에이전트의 토큰 사용량 10–20% 절감, 세션 30% 단축), Sterling Labs,
  회계 에이전트 팀의 고객 인용.

## 번들 리소스
- Skill: `agent-otel-tracing` — 내보내기 설정, 목적지 선택, 점진적 권한 확대, 개선 루프
  (`references/observability-tools.md`, `examples/customer-patterns.md`).

## 출처
- https://claude.com/resources/articles/agent-observability-on-the-claude-platform
