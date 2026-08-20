**English** · [한국어](./slack-analytics-rollout.ko.md) · [Español](./slack-analytics-rollout.es.md) · [日本語](./slack-analytics-rollout.ja.md)

# Rolling out self-service data analytics in Slack

## Why deployment is a separate problem from accuracy
Earlier work covered how to get an analytics agent to roughly 95% accuracy: semantic layers, skill files, and evaluation suites. This guide covers what comes after — putting that agent into Slack so anyone in the company can ask it ad hoc questions. The decisions that matter here are different ones: freshness, permissions, and observability.

## 1. Refresh skills as often as you refresh data models
The central architectural decision is to treat skill files as **served content, refreshed continuously**, rather than something shipped once and forgotten.

Data models change constantly. Columns are renamed, metrics are corrected, tables are deprecated. A skill file written against last quarter's model is a source of confidently wrong answers. The runtime re-reads skill files on every conversation from a mounted repository, so the agent always resolves against current definitions.

Practical consequence: skill-file updates belong in the same review process that governs the data model itself, so a metric correction and its skill-file update land together.

## 2. Give the agent skills beyond data access
Knowing which table to query is the floor. The agent also needs the analytical conventions your analysts already follow:

- **Forecasting** — trend fitting, seasonality assumptions
- **Cohort and retention analysis** — standard definitions, retention curves
- **Funnel analysis** — canonical stage definitions
- **Charting** — visualization conventions
- **Analytical writing** — structure, hedging, confidence levels

These document existing practice rather than inventing methodology. Writing them down is what keeps the agent's output consistent with the analysts' output.

## 3. Connect to business context, not just the warehouse
Wire the agent into internal knowledge indexes — catalogs of documents, discussions, and events — alongside the warehouse.

When a metric moves, the agent can then search for what else happened at the same time: an incident report, a feature flag change, a competitor announcement. That is the difference between "sign-ups dropped 12%" and an answer that explains the week.

## 4. Permission the service account deliberately
Treat the agent's channel access as **a shared read replica of your governed warehouse**. Five protections:

1. **Scope the account to governed data only.** Keep ungoverned staging and scratch schemas out of reach.
2. **Classify PII at the column level and deny the agent clearance.** Column-level, so a table stays usable for aggregates while identifying columns stay out.
3. **Document connection paths in skill files.** Makes the agent's real reach reviewable by someone outside the data team.
4. **Treat channel membership as an access grant.** Everyone in a channel with the agent gets indirect read access to whatever it can read.
5. **Label every query.** Audit trail and cost attribution, both.

## 5. Instrument every answer
Log a structured event for every question. At minimum capture:

- Which skill files were loaded, and at which version
- User reactions (👍/👎) and any typed correction
- Data quality warnings on the tables accessed

**Adoption is the most actionable metric.** A dip signals one of two things: skill drift — definitions have moved and answers have started to feel wrong — or an uncovered data need, where people are asking about something the agent cannot reach.

## What the surface enables beyond one-off questions

**Threads as collaborative spaces.** Several team members add context while the agent does the analysis. The thread becomes a reviewable historical record of the problem and how it was solved.

**Configured loops for repetitive work.**
- Weekly proactive readouts before standups
- Test and experiment monitoring
- Pipeline and dashboard observability
- Triage of incoming data questions

**Proactive assistance.** Configured appropriately, the agent can answer 75%+ of channel questions without being explicitly mentioned.

## Implementation sequence
1. Establish permissions first
2. Configure distribution and verify freshness
3. Enable telemetry from day one
4. Wire in knowledge indexes when data paths stabilize
5. Create analytics skills informed by actual user questions

## Source
- https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
