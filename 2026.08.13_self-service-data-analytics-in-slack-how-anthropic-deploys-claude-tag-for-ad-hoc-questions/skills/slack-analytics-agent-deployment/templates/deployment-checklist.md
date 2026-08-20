# Deployment checklist

Fill this in before an analytics agent goes into a channel where people who are not on the data team can ask it questions.

## Permissions (do first)
- [ ] Service account scoped to governed data only
- [ ] PII classified at the **column** level
- [ ] Agent clearance to PII columns denied — and the denial tested, not just configured
- [ ] Connection paths documented in the skill files
- [ ] Channel membership reviewed as an access grant, for each channel the agent will join
- [ ] Every query labeled; labels confirmed to be landing in the audit destination

## Distribution and freshness
- [ ] Skill repository mounted to the agent runtime
- [ ] Skill files verified to be re-read **on every conversation**, not baked in at deploy
- [ ] Skill-file updates folded into the same review process as data model changes
- [ ] Channels for initial rollout chosen and named

## Telemetry (from day one)
- [ ] Structured event logged per question
- [ ] `skill_files_loaded` and `skill_file_versions` captured
- [ ] Reactions (👍/👎) and typed corrections captured
- [ ] Data quality warnings on accessed tables captured
- [ ] Adoption dashboard live before the first question

## Business context (once data paths are stable)
- [ ] Internal knowledge indexes wired in — documents, discussions, events
- [ ] Verified that a metric-movement question returns contemporaneous context, not just the delta

## Analytics skills (last, informed by real questions)
- [ ] Forecasting — trend fitting, seasonality assumptions
- [ ] Cohort and retention — standard definitions, retention curves
- [ ] Funnel — canonical stage definitions
- [ ] Charting — visualization conventions
- [ ] Analytical writing — structure, hedging, confidence levels

## Ongoing operation
- [ ] Weekly proactive readouts configured (if wanted) ahead of standups
- [ ] Test and experiment monitoring configured
- [ ] Pipeline and dashboard observability configured
- [ ] Triage of incoming data questions configured
- [ ] Proactive-answering behavior tuned for the channel

## Source
- https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
