# Asking the analytics

Analytics chat takes plain-language questions and returns charts that can be exported and shared
with stakeholders. The two questions below are the examples given in the post; the rest of this file
maps question shapes onto the filter dimensions the Analytics API actually exposes — **date range,
team, product, model**, plus **skills**, **plugin adoption**, and **artifact creation**.

## The two examples from the post

> "Which teams doubled their Claude usage this month?"

A rate-of-change question, sliced by team over a date range.

> "Where are we getting the most value per seat?"

A value question, which needs cost *and* output — artifacts created, files edited, skills and
connectors used — in the same view, divided by seats.

## Question shapes and the dimensions they need

| Question shape | Dimensions it leans on |
|---|---|
| "How is usage trending?" | date range |
| "Which parts of the org drive the spend?" | team (via SCIM groups), cost |
| "What are we spending it on?" | product, model |
| "What is actually getting produced?" | artifacts created, files edited, skills and connectors used |
| "Which skills are worth keeping?" | skill-level usage and cost |
| "Is the plugin rollout landing?" | plugin adoption endpoints |
| "Who is about to hit a limit?" | progress against spend limits, per user |

## A note on value questions

Value-per-seat and cost-per-commit style answers come from the Claude Code value tab, whose formulas
are visible and whose **inputs are adjustable**. Set the inputs to the organization's real numbers
before exporting a chart for a stakeholder — the default inputs make an illustration, not a finding.

## What the answers are for

Three stakeholder framings appear in the post, and each wants a different cut:

- A product manager wants **regular nudges**, not a month-end surprise — recurring, per-team spend
  data plus alerts.
- A CIO wants **cost next to business impact, by team** — the pairing is what makes an ROI case
  stick.
- A product director wants **which skills get run again and again across the org**, on the grounds
  that token usage alone doesn't tell you much.

## Source

["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)
— Anthropic, July 2, 2026.
