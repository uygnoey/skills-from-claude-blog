**English** · [한국어](./admin-analytics-and-cost-controls.ko.md) · [Español](./admin-analytics-and-cost-controls.es.md) · [日本語](./admin-analytics-and-cost-controls.ja.md)

# Admin analytics and cost controls for Claude Enterprise

Anthropic introduced richer admin analytics, model-level entitlements, and spend alerts for Claude
Enterprise. The reasoning behind them is stated plainly: **as Claude takes on increasingly difficult
and complex agentic work across the organization, usage and cost patterns look different from a
standard chat tool's.** These controls give admins the visibility to understand how Claude is being
used and the tools to manage costs.

These additions build on controls Anthropic already provides — spend caps at every level, access and
model routing, a usage analytics dashboard with exports and an Analytics API, and effort controls.
Richer analytics and more granular cost controls are the newest additions to a control surface that
has been built up over months.

## Track adoption and cost

### The analytics dashboard

The analytics dashboard for admins now shows **usage and cost by group and by user**, with output —
artifacts created, files edited, skills and connectors used — displayed directly next to its cost.
Admins can filter by the **SCIM groups their IT team already manages**, so the breakdown follows
their existing org chart.

### Claude Code insights

Claude Code gets richer insights through two new tabs in the admin console, focused on value and
usage.

**Usage** shows active developers, session counts, and top commands across the org, and is updated
daily.

**Value** summarizes usage and cost data to help admins understand the value of Claude Code at a
glance, estimating productivity lift, cost per commit, and annual value. Every formula is visible in
the tab, and the inputs are adjustable.

### Analytics chat

Analytics chat can now answer a much broader set of questions and produce richer artifacts to dive
into. Admins ask in plain language — "Which teams doubled their Claude usage this month?" or "Where
are we getting the most value per seat?" — and Claude returns charts that can be exported and shared
with stakeholders.

### The Analytics API

Usage and cost data is available programmatically through the Analytics API, so finance and IT can
bring it into the tools they already run — like **Datadog Cloud Cost Management** and **CloudZero** —
and see it alongside the rest of their cloud and AI spend. Results can be filtered by **date range,
team, product, or model**. **Skills report their own usage and cost**, and new endpoints track
**plugin adoption** and **artifact creation**.

### User-level visibility

Admins can extend usage visibility to individual users — cost, product and model breakdowns, and
progress against spend limits — so no one hits a surprise cutoff. Users can also see their own usage
trends over time, including which products, models, and skills they rely on most, and how that
activity adds up in spend.

## Controls for managing spend

**Model defaults and entitlements** let admins set which Claude model new conversations start with
across chat, Cowork, and Claude Code, so routine work doesn't necessarily default to the most
expensive option. Admins control which models are available to specific roles or across the entire
organization.

**Spend-threshold alerts** notify admins at **75%** and **90%** of an org-level spend limit, giving
them time to raise the cap before anyone gets blocked mid-task. Users receive in-app notifications
at **75%** and **95%** and can request a limit increase directly from their admin without leaving
Claude.

**The Admin API** moves cost-control workflows into scripts for organizations managing limits across
many groups, so controls scale with the org. It can automate increase-request reviews, identify
members close to their spend limit, and flag rapidly changing usage — all at scale.

## What admins say they want from it

> "Cost visibility isn't a once-a-month exercise. Granular spend data and alerts give teams regular
> nudges to reassess how they're using Claude, instead of a surprise at the end of the billing
> cycle."
>
> — Kyra Abbu, Product Manager

> "I'm not going to slow down the people driving our best quarter. He's asking for ROI. We've tied
> Claude, connected to our enterprise MCP servers, to a 4% revenue lift."
>
> — Carter Busse, CIO

> "Token usage alone doesn't tell you much. What I actually want to see is which skills get run
> again and again across the org — that's the real signal of value."
>
> — Ciro Yamada, Product Director

## Getting started

For admins managing Claude across their organization: explore usage and cost breakdowns in the admin
console, set model defaults and spend limits by group, and configure spend-threshold alerts to stay
ahead of overages. Usage data is available in the admin dashboard, and the Analytics API lets
finance and IT pull the same metrics into existing reporting systems.

## Source

["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)
— Anthropic, July 2, 2026.
