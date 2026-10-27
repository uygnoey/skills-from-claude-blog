**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A best-practices article from October 27, 2026, based on a webinar with Google Cloud. It shows platform
teams how to manage Claude Code spend on Google Cloud and prove its value with three independent levers:
control, track, and prove.

## When is it useful?
- You are rolling out Claude Code on Google Cloud and need guardrails, budgets, and model policy.
- Spend is growing and you need to separate high-value power use from waste.
- You are building usage dashboards or have to show leadership the ROI of Claude Code.

## Key points
- The bill is tokens per task times model price. Agentic work uses more tokens per task than chat, so
  matching the model to the task is a major lever. Cost per task matters more than price per token.
- Toolbox: Google Cloud per-project billing, budgets and alerts, spend caps (Preview), BigQuery exports,
  quotas, and provisioned throughput, plus the self-hosted Claude apps gateway with IdP sign-in.
- Control - guide, don't restrict: gateway spend caps per user, IdP group, or org by day, week, or month
  (inherited per-developer defaults, not a shared pool), in-CLI warnings past 75% and 95%, 429 at the
  cap, per-group model defaults and allowlists, and an admin API for caps. Waste hides in the long
  middle of heavy spenders (expensive models on routine work, forgotten scheduled tasks).
- Track: Claude Code OpenTelemetry by user, team, model, skill, plugin, agent, and MCP server;
  gateway-managed telemetry tagged with verified identity; `OTEL_RESOURCE_ATTRIBUTES` for cost centers;
  a Cloud Monitoring dashboard template; an OTel quickstart that lands events in BigQuery with SQL;
  Cloud Billing exports to BigQuery.
- Prove: adoption and usage, developer satisfaction (pre/post survey), and impact (time, effort,
  volume) against a baseline. Define a unit of work such as a labeled merged PR; telemetry's "PRs
  created" is not "PRs merged", so correlate with source control and tickets. Prompt logging is opt-in.
- Customer examples: Delivery Hero, Shopify, Fifth Dimension. Start with defaults (org-wide cap, default
  model, allowlist) and refine by role and team in a continuous loop.

## Bundled resources
- Skill: `coding-agent-spend-roi` (`references/governance-toolbox.md`, `references/telemetry-and-tracking.md`,
  `references/roi-metrics.md`, `references/resources.md`, `examples/customer-outcomes.md`,
  `templates/rollout-defaults.md`, `templates/roi-report.md`, `templates/otel-resource-attributes.env`).
- Guide: `guides/cost-and-roi-on-google-cloud.{en,ko,es,ja}.md`.

## Source
- https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
