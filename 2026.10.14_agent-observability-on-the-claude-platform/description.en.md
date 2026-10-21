**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
The announcement of OpenTelemetry (OTel) traces from Claude Managed Agents, the Messages API, and
Claude SDKs on the Claude Platform, so you can follow each step your agents take in any OTel tool.

## When is it useful?
- When you want per-step visibility into agents built on the Claude Platform.
- When debugging slow or failed agent steps alongside the rest of your stack.
- When turning production traces into evals or tracking token usage by team.

## Key points
- Every agent turn, model call, and tool use (including MCP server calls) arrives as a standard OTel
  trace with latency, tokens, and IDs.
- Traces follow the OpenTelemetry GenAI semantic conventions, so Claude data and other providers'
  data share tools and dashboards. Claude Code and Cowork traces can land in the same place.
- Trust grows with evidence: review an agent's traces, then widen its access as it proves reliable.
- Named tools: Grafana Cloud, Honeycomb, Sentry, Splunk (debugging); Arize AI, Braintrust, Datadog,
  Langfuse, LangSmith, New Relic, PostHog (evals and quality); Databricks Unity Gateway (org usage).
  Any OTLP-compatible tool works.
- Public beta. Managed Agents and the Messages API need a destination in the Claude Console; SDKs
  export automatically.
- Customer quotes from Foxglove, Ramp (Reflect cut token usage 10–20% and made sessions 30% faster on
  some agents), Sterling Labs, and an accounting-agent team.

## Bundled resources
- Skill: `agent-otel-tracing` — enabling export, choosing a destination, gradual access, improvement
  loop (`references/observability-tools.md`, `examples/customer-patterns.md`).

## Source
- https://claude.com/resources/articles/agent-observability-on-the-claude-platform
