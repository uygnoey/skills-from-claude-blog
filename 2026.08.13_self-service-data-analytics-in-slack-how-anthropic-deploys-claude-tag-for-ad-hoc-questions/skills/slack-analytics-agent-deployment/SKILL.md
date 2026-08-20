---
name: slack-analytics-agent-deployment
description: Deploy a Slack-based data analytics agent that a whole company can ask ad hoc questions — keep its skill files refreshed like a data model, give it analytical skills beyond table access, wire it into business context, permission its service account deliberately, and instrument every answer so adoption and correctness are measurable.
---

## Instructions
You are helping a data team take an analytics agent that already answers accurately in a test harness and deploy it into Slack, where anyone in the company can ask it questions. Getting accurate answers and deploying broadly are different problems: the first is about semantic layers, skill files, and evaluation suites; the second is about freshness, permissions, and observability.

Work through the five decisions below. If the team is starting from scratch, follow the ordering in [references/rollout-sequence.md](references/rollout-sequence.md) rather than doing them in the order presented here — permissions come first.

### 1) Refresh skills as often as you refresh the data model
Treat skill files as **served content, refreshed continuously**, not as something shipped once and forgotten.

- Data models drift constantly: columns get renamed, metric definitions are corrected, tables are deprecated. A skill file that was right last quarter is a source of confidently wrong answers this quarter.
- Mount the skill repository so the agent runtime re-reads skill files on every conversation. The agent then always resolves against current definitions instead of a snapshot.
- Make the refresh path part of the same review process that governs the data model itself, so a metric correction and its skill-file update land together.

### 2) Give the agent analytical skills, not just data access
Knowing which table to query is the floor. The agent also needs the conventions your analysts already follow, written down. The set to cover is in [references/analytical-skills.md](references/analytical-skills.md):

- Forecasting — trend fitting and how seasonality is assumed.
- Cohort and retention analysis — the standard definitions and retention curves.
- Funnel analysis — the canonical stage definitions.
- Charting — visualization conventions.
- Analytical writing — structure, hedging, and how confidence is expressed.

These are documentation of existing practice, not new methodology. Writing them down is what makes answers consistent between the agent and the analysts.

### 3) Connect to business context, not just the warehouse
Wire the agent into internal knowledge indexes — catalogs of documents, discussions, and events — alongside the warehouse connection.

When a metric moves, the agent can then search for what else happened at the same time: incident reports, feature flag changes, competitor announcements. That is the difference between reporting that sign-ups dropped 12% and explaining what was going on that week.

### 4) Permission the service account deliberately
Model the agent's Slack channel access as **a shared read replica of your governed warehouse**. Anyone in a channel the agent is in can reach whatever the agent can reach. The five protections are detailed in [references/permissioning-model.md](references/permissioning-model.md):

1. Scope the service account to governed data only.
2. Classify PII at the column level and deny the agent clearance to it.
3. Document the connection paths in the skill files.
4. Treat channel membership as an access grant, and review it as one.
5. Label every query so it can be attributed for audit and cost.

### 5) Instrument every answer
Log a structured event for every question so adoption and correctness are both measurable. Use [templates/telemetry-event.md](templates/telemetry-event.md) as the starting field set:

- Which skill files were loaded, and at which version.
- User reactions (👍/👎) and any correction the user typed.
- Data quality warnings on the tables that were touched.

Watch the adoption metric most closely — it is the most actionable of the three. A dip usually means either skill drift (definitions have moved and answers have started to feel wrong) or an uncovered data need (people are asking about something the agent cannot reach).

### Then: use the surface for more than one-off questions
- **Threads as collaborative spaces.** Several people add context while the agent does the analysis; the thread becomes a reviewable record of the problem and how it was resolved.
- **Configured loops for repetitive work.** Weekly proactive readouts before standup, test and experiment monitoring, pipeline and dashboard observability, and triage of incoming data questions.
- **Proactive answering.** Configured appropriately, the agent can answer 75%+ of channel questions without being explicitly mentioned.

## Examples

### Example: answers were right in eval, wrong in Slack a month later
User: Our eval suite passes at 95% but people in Slack keep telling us the numbers are stale.
Assistant:
- This is the freshness failure, not an accuracy failure. Check whether skill files are re-read per conversation from a mounted repo, or baked in at deploy time.
- Find what moved in the data model since the last skill-file update — renamed columns, corrected metrics, deprecated tables — and fix the definitions.
- Then close the loop: put skill-file updates into the same review process as data model changes so this cannot drift again.
- Check the adoption metric over the same window. A dip that starts before the complaints is the earliest signal of skill drift.

### Example: scoping the service account before opening the channel up
User: We want to add the agent to #general so everyone can ask.
Assistant:
- Treat that channel membership as an access grant to everything the service account can read. Decide whether that is acceptable for #general specifically.
- Before it goes in: scope the account to governed data only, classify PII at column level and deny clearance, and label every query for audit and cost attribution.
- Document the connection paths in the skill files so the reach is legible rather than implicit.
- See [references/permissioning-model.md](references/permissioning-model.md); the checklist is in [templates/deployment-checklist.md](templates/deployment-checklist.md).

### Example: the answer is a number with no story
User: It said sign-ups dropped 12% and stopped there. People want to know why.
Assistant:
- The warehouse connection alone gets you the number. Add the internal knowledge indexes — documents, discussions, events.
- With those wired in, the agent can search for what was happening that week: an incident report, a feature flag change, a competitor announcement.
- Also confirm the analytical skills are in place. Without an analytical-writing convention, even a well-sourced answer will not hedge or state confidence the way your analysts do.

### Example: deciding what to build first
User: Where do we even start on this?
Assistant: Follow the sequence in [references/rollout-sequence.md](references/rollout-sequence.md): permissions first, then distribution and a freshness check, then telemetry from day one, then knowledge indexes once the data paths are stable, and only then the analytics skills — informed by the questions people actually asked.
