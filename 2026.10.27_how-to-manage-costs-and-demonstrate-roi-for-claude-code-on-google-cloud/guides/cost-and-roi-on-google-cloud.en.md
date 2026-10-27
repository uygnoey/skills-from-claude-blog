**English** · [한국어](./cost-and-roi-on-google-cloud.ko.md) · [Español](./cost-and-roi-on-google-cloud.es.md) · [日本語](./cost-and-roi-on-google-cloud.ja.md)

# Claude Code cost and ROI on Google Cloud: control -> track -> prove

A methodology summary of Anthropic's guidance for platform teams running Claude Code on Google Cloud.

## 1. Why the bill looks the way it does
Claude on Google Cloud is priced on consumption: adoption drives usage, usage is what you pay for, and
it is also where the value shows up. Cost = tokens per task x model price. Agentic tools read files,
run tools, and reason across a whole task, so they use more tokens per task than chat. Matching the
model to the task is the other major control. Visibility comes from the Claude apps gateway and Google
Cloud services.

## 2. The toolbox
| Layer | Capabilities |
|---|---|
| Google Cloud | Per-project billing, budgets and alerts, spend caps (Preview), BigQuery exports, quotas (requests and input/output tokens per minute, per model family and location), provisioned throughput |
| Claude apps gateway | Self-hosted, in the same `claude` binary, runs in your project; IdP sign-in (e.g. Google Workspace) so every request has a verified identity; per-group model allowlists; spend caps per user, IdP group, or org by day, week, or month |

## 3. Lever 1 - Control
Guide instead of restricting. High-cost sessions are often power users doing high-value work; waste
sits in the long middle of heavy spenders (an expensive model on a routine task, a forgotten scheduled
job).
- **Spend limits**: per user, group, or org; group and org caps are inherited per-developer defaults,
  not a shared pool.
- **Threshold alerts**: in-CLI warnings past 75% and 95%; 429 at the cap until reset or raised. Cloud
  Billing alerts are for admins.
- **Model defaults and allowlists**: per IdP group, enforced server-side. Most people keep the default.
- **Gateway admin API**: change caps programmatically, e.g. from tickets.

## 4. Lever 2 - Track
- Claude Code OpenTelemetry: sessions, active time, lines of code, commits, PRs, tokens, cost - by user,
  team, model, and now by skill, plugin, agent, and MCP server. Send via OTLP through a collector or
  the gateway.
- Gateway telemetry: one destination for everyone; exports tagged with verified email and IdP groups.
- `OTEL_RESOURCE_ATTRIBUTES` (e.g. `department=engineering,cost_center=eng-123`) for cost-center views
  in Cloud Monitoring, Grafana, or Splunk.
- Dashboards: active developers, sessions in the last 24 hours, tokens, and blocked requests (pair with
  a cap-increase ticket flow). The "Claude Code Monitoring" template is copyable in Cloud Monitoring.
- OTel quickstart: Cloud Logging/Monitoring plus partitioned BigQuery tables per event type (API
  requests, tool decisions, tool results, assistant responses, hook executions) with SQL for spend per
  developer/model, tool success and latency, hook wait time, and per-turn/session analytics.
- Cloud Billing to BigQuery: filter Claude SKUs by model and token type.

## 5. Lever 3 - Prove
| Dimension | Examples | Source |
|---|---|---|
| Adoption and usage | Activated users, daily/weekly use, retention, power users | OTel |
| Satisfaction | Happiness, perceived time savings, confidence, friction | Pre/post survey + check-ins |
| Impact | Time (PR open -> merge, review turnaround); effort (review iterations, comments, rework per PR); volume (PRs per engineer, deployment frequency, named bodies of work) | Source control + tickets baseline |

**Unit of work**: count merged PRs of a defined class (Claude opens, a person decides), tagged by label,
ticket ID, and Claude involvement. For non-PR work, count one finished thing where it lands.

**Native telemetry**: accept rate, lines modified, commits, PRs created, PRs per user, cost per unit of
output. PRs created are not PRs merged - correlate with GitHub/GitLab and tickets. Prompt logging is
opt-in and shows non-PR value (an SRE debugging an incident, a sales engineer building demo data).

## 6. Reference outcomes
- Delivery Hero: design system overhaul across 100 UI components in minutes instead of about a week.
- Shopify: non-engineers build internal tools in minutes instead of days.
- Fifth Dimension: 300,000+ lines of code a month with a 98% acceptance rate.

## 7. Getting started
Run a continuous loop: start with an org-wide spend cap, a default model, and a model allowlist; refine
by role and team as data arrives; correlate metrics with value and report to stakeholders.

## Source
- https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
