# Telemetry and tracking (Track lever)

## What Claude Code exports
Once enabled, Claude Code (on developer machines or cloud workstations) exports OpenTelemetry covering:
- sessions and active time;
- lines of code, commits, pull requests;
- tokens and estimated cost;
- broken down by user, team, and model - and, in recent releases, by **skill, plugin, agent, and MCP
  server**, so you can see which internal skills and plugins get adopted.

Send it over OTLP to tools you already run (for example Google Cloud Monitoring) through an
OpenTelemetry collector, or relay it through the Claude apps gateway for centralized config.

## Gateway-managed telemetry
- No per-machine configuration: set a telemetry destination on the gateway and it enables telemetry for
  signed-in developers.
- Every export is tagged with the developer's verified email and IdP groups from sign-in, rather than
  values configured on the client.

## Cost-center attribution
Set `OTEL_RESOURCE_ATTRIBUTES` (for example `department=engineering,cost_center=eng-123`). Claude Code
adds these tags to every metric and event so you can filter and aggregate by them in Cloud Monitoring,
Grafana, Splunk, or similar. See [../templates/otel-resource-attributes.env](../templates/otel-resource-attributes.env).

## Dashboards
- A typical adoption view: active developers, sessions in the last 24 hours, total tokens consumed, and
  **blocked requests** when developers hit gateway-enforced caps. Pair the blocked-request metric with
  a ticket workflow that lets developers request a cap increase.
- Ready-made: the **Claude Code Monitoring** template for Cloud Monitoring (copyable from the Cloud
  Monitoring console) shows adoption, coding activity, token usage, and estimated spend by user and model.

## Custom telemetry pipeline (OTel quickstart)
The Claude Code OTel quickstart for Google Cloud:
- exports OpenTelemetry to Google Cloud Observability (Cloud Logging and Cloud Monitoring);
- routes logs into partitioned BigQuery tables, one per event type: API requests, tool decisions,
  tool results, assistant responses, and completed hook executions;
- ships SQL for spend per developer/model, tool success and latency, hook wait time, and per-turn and
  per-session analytics.

## Billing data
Cloud Billing exports to BigQuery let you filter to Claude SKUs by model and token type, so Claude spend
sits alongside the rest of your cloud and AI spend.

## Prompt logging (opt-in)
User prompts are **not** logged automatically because they may contain sensitive content. Opting in
helps you understand what people are trying to build, including work that never becomes a PR.

Links: [resources.md](resources.md).
