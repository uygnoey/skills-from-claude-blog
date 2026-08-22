---
name: usage-and-spend-governance
description: Set up visibility and cost control for an enterprise AI deployment using admin analytics, model defaults and entitlements, spend-threshold alerts, and programmatic access through the Analytics API and Admin API. Use when an org's usage and cost patterns stop looking like a chat tool's and start looking like agentic work, when finance or IT needs usage and cost data alongside the rest of cloud spend, when routine work is defaulting to the most expensive model, when users are hitting spend limits mid-task, or when someone asks what value the deployment is actually returning per team or per seat.
---

# Governing usage and spend for an enterprise deployment

As an assistant takes on increasingly difficult and complex agentic work across an organization,
usage and cost patterns look different from a standard chat tool's. Governing that requires two
halves that are easy to confuse:

- **Visibility** — knowing how it is being used, by whom, producing what, at what cost.
- **Control** — the levers that change usage before a bill or a hard stop does.

Instrument first, then set controls. Controls set without the breakdown behind them either throttle
the wrong teams or leave the expensive path as the default.

## Instructions

### 1. Break usage and cost down along the org chart you already have

Start in the admin analytics dashboard, which shows usage and cost **by group and by user**, with
output — artifacts created, files edited, skills and connectors used — displayed directly next to
its cost.

Filter by the **SCIM groups** your IT team already manages, so the breakdown follows the existing
org chart rather than a second structure invented for analytics. If SCIM groups are not in place,
that is the prerequisite to fix first: every downstream control in this skill is set per group.

The surfaces available, and what each one shows, are in
[references/analytics-surfaces.md](references/analytics-surfaces.md).

### 2. Separate the usage question from the value question

For a developer deployment, the two are reported separately, and they answer different things:

- **Usage** — active developers, session counts, top commands across the org. Updated daily.
- **Value** — an estimate of productivity lift, cost per commit, and annual value.

The value figures are estimates built on visible formulas with **adjustable inputs**. Before quoting
one to a finance stakeholder, open the formula and set the inputs to your organization's real
numbers. A value estimate carried at default inputs is not a finding.

### 3. Ask the analytics in plain language, then export what you find

Analytics chat answers plain-language questions and returns charts that can be exported and shared
with stakeholders. Use it for the questions a fixed dashboard does not have a tile for — comparative
questions across teams and time, and value-per-seat questions.

Worked question patterns are in
[examples/analytics-questions.md](examples/analytics-questions.md).

### 4. Pull the data into the systems finance and IT already run

Usage and cost data is available programmatically through the **Analytics API**, so it can sit
alongside the rest of your cloud and AI spend in tools like **Datadog Cloud Cost Management** and
**CloudZero**.

Results can be filtered by **date range, team, product, or model**. Skills report their own usage
and cost, and there are endpoints for **plugin adoption** and **artifact creation**.

Skill-level cost is worth wiring up specifically: repeated runs of the same skill across the org are
a stronger signal of realized value than raw token counts.

### 5. Extend visibility to individual users

Admins can extend usage visibility to individual users — cost, product and model breakdowns, and
progress against spend limits — so no one hits a surprise cutoff. Users can also see their own usage
trends over time, including which products, models, and skills they rely on most, and how that
activity adds up in spend.

Turning this on is a control as much as a reporting feature: a user who can see their own trend
adjusts before an alert fires.

### 6. Set the default model, and scope entitlements by role

Model defaults and entitlements let you set which model new conversations start with across chat,
Cowork, and Claude Code, so routine work doesn't necessarily default to the most expensive option.
You also control which models are available to specific roles or across the entire organization.

Set the default from the breakdown in step 1, not from a guess about what teams need. Details are in
[references/spend-controls.md](references/spend-controls.md).

### 7. Configure spend-threshold alerts at both levels

- **Admins** are notified at **75%** and **90%** of an org-level spend limit — time to raise the cap
  before anyone is blocked mid-task.
- **Users** get in-app notifications at **75%** and **95%**, and can request a limit increase
  directly from their admin without leaving the product.

The point of the admin alert firing earlier than the user's hard edge is that the cap gets raised as
a decision rather than as an interruption.

### 8. Script the controls once there are too many groups to click through

For organizations managing limits across many groups, the **Admin API** moves cost-control workflows
into scripts so controls scale with the org. The three named workflows — reviewing increase
requests, identifying members close to their spend limit, and flagging rapidly changing usage — are
described in [references/admin-api-workflows.md](references/admin-api-workflows.md).

### 9. Run the rollout as a checklist

Use [templates/rollout-checklist.md](templates/rollout-checklist.md) to work through the sequence:
explore usage and cost breakdowns in the admin console, set model defaults and spend limits by
group, configure spend-threshold alerts, and connect the Analytics API to existing reporting.

## Examples

- **Cost visibility as a habit, not a monthly ritual.** Granular spend data plus alerts give teams
  regular nudges to reassess how they're using the product, instead of a surprise at the end of the
  billing cycle. Configure the 75%/90% admin alerts and the per-user visibility together — that
  combination is what makes it continuous.

- **Making an ROI case to a CIO.** Cost by team next to business impact by team is the shape of the
  argument. One CIO in the post ties the deployment, connected to enterprise MCP servers, to a 4%
  revenue lift — and the reason the number lands is that cost is being read *beside* impact, per
  team, rather than as a single org-wide line.

- **Reading skills instead of tokens.** "Token usage alone doesn't tell you much. What I actually
  want to see is which skills get run again and again across the org — that's the real signal of
  value." Skills report their own usage and cost through the Analytics API, so this is a query, not
  an inference.

- **Stopping routine work from defaulting to the most expensive option.** Set model defaults for new
  conversations across chat, Cowork, and Claude Code, and scope entitlements so the most expensive
  models are available to the roles that need them rather than org-wide.

- **A user about to be cut off mid-task.** They see their own progress against the limit, get an
  in-app notification at 75%, and can request an increase without leaving the product; the admin has
  already been notified at 75% of the org limit and can approve before the 95% user threshold.

- **Fifty groups, three admins.** Clicking through per-group limits does not scale. The Admin API
  turns increase-request review, proximity-to-limit detection, and rapid-usage-change flagging into
  scheduled scripts.

## Source

["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)
— Anthropic, July 2, 2026.
