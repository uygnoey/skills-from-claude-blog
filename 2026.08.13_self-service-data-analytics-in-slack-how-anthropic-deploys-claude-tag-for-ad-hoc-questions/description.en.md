**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A field report on how Anthropic deploys Claude Tag inside Slack so that employees can ask ad hoc data questions and get answers grounded in governed data definitions. It picks up where earlier work on accuracy left off — that work covered reaching roughly 95% accuracy through semantic layers, skill files, and evaluation suites — and argues that **getting accurate answers and deploying broadly are different problems**. The post is organized around five deployment learnings: refresh skill files continuously, give the agent analytical skills beyond table access, connect it to business context and not only the warehouse, permission the service account deliberately, and instrument every answer.

The through-line is that the deployment-side properties — freshness, permissions, observability — are what determine whether an accurate agent stays accurate and stays used once it is in front of the whole company.

## When is it useful?
- When an analytics agent already scores well in evaluation and you are deciding how to put it in front of non-analysts.
- When answers were right at launch and have started drifting, and you need to know whether it is skill drift or an uncovered data need.
- When you are scoping a service account's warehouse access and need a defensible model for what channel membership actually grants.
- When you want to know what to log so that adoption and correctness are both measurable from day one.

## Key points
- **Skill files are served content, not shipped artifacts.** The runtime re-reads them on every conversation from a mounted repository, so the agent always uses current definitions. Data models change constantly — columns renamed, metrics corrected, tables deprecated.
- **Analytical skills matter as much as data access.** Forecasting (trend fitting, seasonality assumptions), cohort and retention analysis (standard definitions, retention curves), funnel analysis (canonical stage definitions), charting (visualization conventions), and analytical writing (structure, hedging, confidence levels). These document existing analyst practice; writing them down is what produces consistency.
- **Business context turns numbers into explanations.** Wiring the agent into internal knowledge indexes — documents, discussions, events — lets it search for what happened at the same time as a metric move: incident reports, feature flag changes, competitor announcements. The difference between "sign-ups dropped 12%" and an answer that explains why.
- **Permission the service account deliberately.** Scope it to governed data only; classify PII at the column level and deny the agent clearance; document connection paths in skill files; treat channel membership as an access grant; label every query for audit trails and cost attribution.
- **The framing to hold onto:** treat Claude's channel access as *a shared read replica of your governed warehouse*.
- **Instrument every answer.** Log which skill files were loaded and at which version, user reactions (👍/👎) and corrections, and data quality warnings on accessed tables.
- **Adoption is the most actionable metric.** A dip signals either skill drift or an uncovered data need.
- **Threads become collaborative spaces.** Multiple team members contribute context while Claude handles the analysis, producing a reviewable historical record of the problem and its solution.
- **Configured loops handle repetitive work:** weekly proactive readouts before standups, test and experiment monitoring, pipeline and dashboard observability, and triage of incoming data questions.
- **Proactive answering.** Configured appropriately, Claude can answer 75%+ of channel questions without being explicitly mentioned.
- **Implementation sequence.** Permissions first; then distribution and a freshness check; telemetry from day one; knowledge indexes once data paths stabilize; analytics skills last, informed by the questions users actually asked.

## Bundled resources
- `skills/slack-analytics-agent-deployment/SKILL.md` — the five deployment decisions, as a working procedure.
- `skills/slack-analytics-agent-deployment/references/permissioning-model.md` — the five protections and the shared-read-replica framing, with review questions.
- `skills/slack-analytics-agent-deployment/references/analytical-skills.md` — the five analytical skill areas and how to source them.
- `skills/slack-analytics-agent-deployment/references/rollout-sequence.md` — the implementation ordering and why it is ordered that way.
- `skills/slack-analytics-agent-deployment/templates/telemetry-event.md` — a per-question event field set, derived metrics, and how to read an adoption dip.
- `skills/slack-analytics-agent-deployment/templates/deployment-checklist.md` — a pre-launch checklist across permissions, freshness, telemetry, context, and skills.
- `guides/slack-analytics-rollout.{en,ko,es,ja}.md` — the full rollout guide in four languages.

## Source
- https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
