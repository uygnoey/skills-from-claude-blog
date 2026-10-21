# Observability tools named in the source

Claude traces work with any OpenTelemetry tool that accepts a standard OTLP endpoint. The source
groups named tools by goal:

| Goal | Tools named | What it gives you |
|---|---|---|
| Debug agents next to the rest of your stack | Grafana Cloud, Honeycomb, Sentry, Splunk | Agent traces beside logs and metrics; see which service a slow or failed step came from |
| Improve agents with production data | Arize AI, Braintrust, Datadog, Langfuse, LangSmith by LangChain, New Relic, PostHog | Turn real traces into evals, catch quality issues, measure whether a change helped |
| Track usage across the organization | Databricks Unity Gateway | Token usage by team; flag unusual activity for platform and security teams |

## Setup summary
| Source of traces | How to enable |
|---|---|
| Claude Managed Agents | Add a destination in the Claude Console |
| Messages API | Add a destination in the Claude Console |
| Claude SDKs | Exported automatically |

Status at publication (2026-10-14): public beta. Configuration specifics: see the official docs.
