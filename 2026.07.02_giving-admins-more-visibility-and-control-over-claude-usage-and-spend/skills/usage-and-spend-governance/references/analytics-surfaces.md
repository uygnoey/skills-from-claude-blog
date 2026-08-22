# Analytics surfaces for admins

Four surfaces, each answering a different question.

## 1. Admin analytics dashboard

Shows **usage and cost by group and by user**, with output displayed directly next to its cost:

- artifacts created
- files edited
- skills and connectors used

Admins can filter by the **SCIM groups their IT team already manages**, so the breakdown follows the
existing org chart rather than a parallel structure.

## 2. Claude Code insights — two tabs in the admin console

**Usage tab** — updated daily:

- active developers
- session counts
- top commands across the org

**Value tab** — summarizes usage and cost data to help admins understand value at a glance:

- estimated productivity lift
- cost per commit
- annual value

**Every formula is visible in the tab, and the inputs are adjustable.** Treat the defaults as a
starting point and set them to the organization's real numbers before quoting the output.

## 3. Analytics chat

Answers a broad set of questions and produces richer artifacts that can be explored further. Admins
ask in plain language and get back charts that can be **exported and shared with stakeholders**.

Examples given in the post:

- "Which teams doubled their Claude usage this month?"
- "Where are we getting the most value per seat?"

## 4. Analytics API

Programmatic access to usage and cost data, so finance and IT can bring it into the tools they
already run — named examples: **Datadog Cloud Cost Management** and **CloudZero** — and see it
alongside the rest of their cloud and AI spend.

- Results can be filtered by **date range, team, product, or model**.
- **Skills report their own usage and cost.**
- New endpoints track **plugin adoption** and **artifact creation**.

## 5. User-level visibility

Admins can extend usage visibility to individual users:

- cost
- product and model breakdowns
- progress against spend limits

so no one hits a surprise cutoff. Users can also see their own usage trends over time — which
products, models, and skills they rely on most, and how that activity adds up in spend.

## Context

These additions build on controls already provided: spend caps at every level, access and model
routing, a usage analytics dashboard with exports and an Analytics API, and effort controls. Richer
analytics and more granular cost controls are the newest additions to a control surface that has
been built up over months.

## Source

["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)
— Anthropic, July 2, 2026.
