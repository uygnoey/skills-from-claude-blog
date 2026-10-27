---
name: coding-agent-spend-roi
description: Plan, review, or report on Claude Code spend and return on investment for an organization running Claude on Google Cloud, using the control -> track -> prove framework. Control sets guardrails that guide rather than restrict (Claude apps gateway spend caps per user, IdP group, or org by day, week, or month; 75%/95% in-CLI warnings and 429 at the cap; per-group model defaults and allowlists; the admin API), plus Google Cloud billing, budget alerts, spend caps, and quotas. Track uses Claude Code OpenTelemetry metrics and events (by user, team, model, skill, plugin, agent, MCP server), OTEL_RESOURCE_ATTRIBUTES cost-center tags, Cloud Monitoring dashboards, and Cloud Billing exports to BigQuery. Prove maps usage to adoption, satisfaction, and impact metrics (time, effort, volume) around a defined unit of work such as a labeled, merged PR. Use when rolling out Claude Code on Google Cloud, setting budgets or model policy, building usage dashboards, or preparing an ROI case for stakeholders.
---

## Purpose
Claude on Google Cloud is billed on consumption, so the bill is a readout of how much developers use
Claude Code. Spend is the product of tokens per task (which grows with task complexity and conversation
length, and is higher for agentic multistep work than for chat) and the per-token price of the model
that handles it. This skill applies the post's three independent levers so a platform team can keep
spend in check, see where it goes before the bill arrives, and show the value it buys.

## When to use
- A platform or FinOps team is rolling out Claude Code on Google Cloud and needs default guardrails.
- Spend is rising and you need to tell high-value power-user sessions apart from waste.
- You are wiring Claude Code telemetry into Cloud Monitoring, BigQuery, or another observability stack.
- Leadership asks what the organization gets back for its Claude Code spend.

## Instructions

1. **Frame the bill.** Explain cost as tokens consumed per task x model price. The two big levers are
   task scope/length and matching the model to the task. The most important metric is **cost per task**,
   not price per token.
2. **Pick the toolbox pieces** from [references/governance-toolbox.md](references/governance-toolbox.md).
   Google Cloud gives per-project billing, budgets and alerts, spend caps (Preview), BigQuery billing
   exports, quotas, and provisioned throughput. The Claude apps gateway (self-hosted, shipped in the
   same `claude` binary, running in your Google Cloud project) adds IdP sign-in, per-group model
   allowlists, and spend caps.
3. **Lever 1 - Control: guide, don't restrict.** High-cost sessions are often your most valuable power
   users. Waste usually sits in the long middle of heavy spenders: a top-tier model used for a routine
   task a smaller model handles, or a forgotten scheduled task that keeps running. Set up:
   - gateway **spend limits** per user, IdP group, or organization, by day, week, or month (group and
     org caps are per-developer defaults each member inherits, not a shared pool);
   - **threshold alerts**: developers are warned in the CLI past 75% and 95%; at the cap the gateway
     returns 429 until the period resets or an admin raises it (Cloud Billing alerts are for admins);
   - **model defaults and allowlists** per IdP group, enforced server-side on every request - a
     default works well because most people keep it and switch only for a reason;
   - the **gateway admin API** to change caps programmatically, for example from a ticketing workflow.
   Start from [templates/rollout-defaults.md](templates/rollout-defaults.md).
4. **Lever 2 - Track: see spend before the bill.** Follow
   [references/telemetry-and-tracking.md](references/telemetry-and-tracking.md):
   - enable Claude Code OpenTelemetry (or set one telemetry destination on the gateway, which turns
     telemetry on for signed-in developers and tags exports with verified email and IdP groups);
   - tag cost centers with `OTEL_RESOURCE_ATTRIBUTES` - see
     [templates/otel-resource-attributes.env](templates/otel-resource-attributes.env);
   - use the Cloud Monitoring "Claude Code Monitoring" dashboard template or the OTel quickstart that
     lands events in partitioned BigQuery tables with ready SQL;
   - export Cloud Billing to BigQuery and filter Claude SKUs by model and token type;
   - pair the "blocked by spend cap" metric with a ticket flow for cap increases.
5. **Lever 3 - Prove: map usage to ROI.** Use the three dimensions in
   [references/roi-metrics.md](references/roi-metrics.md):
   - *adoption and usage* (activated users, daily/weekly use, retention, power users) from OTel;
   - *satisfaction* (happiness, perceived time savings, confidence, friction) from a short survey
     before and after rollout plus ongoing check-ins;
   - *impact* against a baseline from source control and tickets: time (PR open -> merge, review
     turnaround), effort (review iterations, comments, rework per PR), volume (PRs per engineer,
     deployment frequency, named bodies of work shipped with freed capacity).
6. **Define the unit of work.** Count merged PRs of a defined class (Claude opens it, a person decides
   whether it ships), found via labels such as hotfix or feature release, ticket IDs, and a
   Claude-involved flag. For non-PR work (a service cutover, an incident closed at its root cause),
   count one finished thing where it lands.
7. **Correlate, don't over-trust one signal.** Claude Code's PR metric counts PRs it *created*, not
   PRs that *merged*. Join telemetry with GitHub/GitLab and the ticket tracker. Prompt logging helps
   show non-PR value but is opt-in because prompts may be sensitive.
8. **Report and iterate.** Fill [templates/roi-report.md](templates/roi-report.md). Treat governance
   as a loop: start with sensible defaults, then refine by role and team as usage data arrives.
   Customer reference points are in [examples/customer-outcomes.md](examples/customer-outcomes.md);
   official links are in [references/resources.md](references/resources.md).

## Examples

**Example 1 - first rollout**
Input: "We're giving Claude Code on Google Cloud to 300 engineers next month. What guardrails?"
Output: A dedicated Google Cloud project with budget alerts; the Claude apps gateway with IdP sign-in;
an org-wide monthly per-developer cap; a default model plus a per-group allowlist; developers warned at
75%/95%; a ticket flow that raises caps through the admin API; telemetry turned on at the gateway with
`department` and `cost_center` attributes. Review caps and model policy by team after the first month.

**Example 2 - a spend spike**
Input: "Five developers account for a large share of spend. Should we cap them?"
Output: Not by default - high-cost sessions are often high value. Check telemetry by model, skill, and
plugin: look for routine work on the most expensive model, or scheduled tasks nobody needs. Fix those
with model defaults and by stopping stale jobs; keep the power users productive.

**Example 3 - ROI question from leadership**
Input: "Is Claude Code worth it?"
Output: Adoption (active users, retention, power users) from OTel; satisfaction from the pre/post
survey; impact as PR cycle time, review iterations, and PRs per engineer for one defined class of
merged PRs versus the pre-rollout baseline, plus named backlog items shipped with freed capacity and
non-PR wins such as faster incident troubleshooting.

## Source
- https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
