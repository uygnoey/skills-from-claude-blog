**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Anthropic introduces richer admin analytics, model-level entitlements, and spend alerts for Claude Enterprise. The premise is that as Claude takes on increasingly difficult and complex agentic work across an organization, usage and cost patterns stop looking like a standard chat tool's — so admins need both the visibility to understand how Claude is being used and the levers to manage what it costs.

The visibility half: an analytics dashboard broken down by group and by user, filterable by the SCIM groups IT already manages, showing output (artifacts created, files edited, skills and connectors used) directly next to its cost; two new Claude Code tabs splitting usage from value, with every value formula visible and its inputs adjustable; analytics chat for plain-language questions that returns exportable charts; and an Analytics API that pulls the same data into Datadog Cloud Cost Management, CloudZero, and other tools finance and IT already run.

The control half: model defaults and entitlements so routine work doesn't start on the most expensive model, spend-threshold alerts at 75%/90% for admins and 75%/95% for users, and an Admin API that turns cost-control workflows into scripts once there are too many groups to manage by hand. All of it builds on controls already shipped — spend caps at every level, access and model routing, the usage dashboard with exports, and effort controls.

## When is it useful?
- When an organization's usage and cost patterns start looking like agentic work rather than chat.
- When finance or IT needs Claude usage and cost sitting next to the rest of cloud and AI spend.
- When routine work is defaulting to the most expensive model available.
- When users are hitting spend limits mid-task and nobody saw it coming.
- When someone asks what value the deployment returns per team or per seat and the answer has to hold up.
- When per-group limits have outgrown what admins can review by clicking.

## Key points
- **Usage and cost by group and by user**, with output — artifacts created, files edited, skills and connectors used — displayed directly next to its cost, filterable by existing SCIM groups.
- **Claude Code splits usage from value.** Usage: active developers, session counts, top commands, updated daily. Value: productivity lift, cost per commit, annual value — with every formula visible and its inputs adjustable.
- **Analytics chat takes plain-language questions** ("Which teams doubled their Claude usage this month?", "Where are we getting the most value per seat?") and returns charts that can be exported and shared.
- **The Analytics API filters by date range, team, product, or model**, skills report their own usage and cost, and new endpoints track plugin adoption and artifact creation. Named integrations: Datadog Cloud Cost Management and CloudZero.
- **Users can see their own usage** — trends over time, which products, models, and skills they lean on, and how it adds up in spend — so no one hits a surprise cutoff.
- **Model defaults and entitlements** set which model new conversations start with across chat, Cowork, and Claude Code, and which models specific roles can reach at all.
- **Spend-threshold alerts fire at 75% and 90% for admins** and **75% and 95% in-app for users**, who can request an increase from their admin without leaving Claude.
- **The Admin API scripts three named workflows:** increase-request reviews, identifying members close to their spend limit, and flagging rapidly changing usage.
- **Three stakeholder framings from the post:** cost visibility as a recurring nudge rather than a month-end surprise; cost read next to business impact by team to make an ROI case (one CIO ties Claude, connected to enterprise MCP servers, to a 4% revenue lift); and repeated skill runs across the org as the real signal of value, over raw token counts.

## Bundled resources
- `skills/usage-and-spend-governance/SKILL.md` — instrument first, then control: break usage down by group, separate usage from value, extend visibility to users, set defaults and entitlements, configure both alert tiers, script the rest.
- `skills/usage-and-spend-governance/references/analytics-surfaces.md` — the five surfaces (dashboard, Claude Code tabs, analytics chat, Analytics API, user-level visibility) and what each shows.
- `skills/usage-and-spend-governance/references/spend-controls.md` — model defaults, entitlements, both alert tiers side by side, and the pre-existing controls this builds on.
- `skills/usage-and-spend-governance/references/admin-api-workflows.md` — the three named Admin API workflows and an explicit note on where the post stops short of publishing endpoint shapes.
- `skills/usage-and-spend-governance/examples/analytics-questions.md` — the two questions from the post plus question shapes mapped onto the filter dimensions the API exposes.
- `skills/usage-and-spend-governance/templates/rollout-checklist.md` — a sequenced checklist from SCIM prerequisite through visibility, controls, integration, and scale.
- `guides/admin-analytics-and-cost-controls.{en,ko,es,ja}.md` — the full guide in four languages.

## Source
["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend) — Anthropic, published July 2, 2026.
