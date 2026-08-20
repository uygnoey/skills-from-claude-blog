# Implementation sequence

The source gives an explicit ordering for standing up a Slack analytics agent. The ordering matters: permissions before distribution, telemetry before you need it, and analytics skills last so they are shaped by real questions.

## 1. Establish permissions first
Scope the service account, classify PII at column level and deny clearance, and set up query labeling before anyone can ask the agent anything. See [permissioning-model.md](permissioning-model.md).

## 2. Configure distribution and verify freshness
Set up how the agent is distributed into channels, and verify that skill files are being re-read on every conversation from the mounted repository — not baked in at deploy time. Freshness is the property that keeps accuracy from decaying after launch.

## 3. Enable telemetry from day one
Structured events for every question, from the first question. Retrofitting telemetry after adoption has already moved means you cannot see the trend that matters. See [../templates/telemetry-event.md](../templates/telemetry-event.md).

## 4. Wire in knowledge indexes when data paths stabilize
Once the warehouse connections are stable, add the internal knowledge indexes — documents, discussions, events — so the agent can explain metric movements rather than only report them.

## 5. Create analytics skills informed by actual user questions
Write the forecasting, cohort, funnel, charting, and analytical-writing conventions last, using the real question log to decide what to cover and in what depth. See [analytical-skills.md](analytical-skills.md).

## Ongoing
- Refresh skill files on the same cadence and review process as the data model.
- Watch the adoption metric as the leading indicator; a dip means skill drift or an uncovered data need.

## Source
- https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
