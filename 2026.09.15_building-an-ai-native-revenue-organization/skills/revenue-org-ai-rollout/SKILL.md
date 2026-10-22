---
name: revenue-org-ai-rollout
description: Plan and run an organization-wide Claude rollout for a sales or revenue team, following Anthropic's revenue-leader guide. Covers the AI maturity ladder (individual gains → team and department workflows → plugins or managed agents pointed at KPIs/OKRs), pre-pilot decisions (RevOps as owner, connected systems, IT and security review, one activity plus one revenue metric with a baseline, spend limits by org/group/user, pilot cohort of two or three teams), the Sales plugin's commands and skills, the three-phase rollout (setup, pilot, scale in waves) with a champion ratio of one per 25-50 users, ROI readouts in three groups (efficiency, expansion, new capabilities) using pilot-vs-non-pilot comparison, and the three pitfalls that stall rollouts. Use when a revenue leader, RevOps owner, or sales manager is preparing, running, or measuring a Claude program.
---

## Purpose
Turn the "Building an AI-native revenue organization" guide into a working plan. The guide argues
that returns grow with the access and trust the organization extends to Claude, and that whole-team
adoption compounds beyond individual time savings. Details live in companion files:
- [references/maturity-and-rollout.md](references/maturity-and-rollout.md) — maturity ladder,
  setup decisions, phases, ROI, pitfalls, FAQ answers, cited customer results.
- [references/sales-plugin-catalog.md](references/sales-plugin-catalog.md) — Sales plugin commands
  and skills, connectors, other Claude surfaces.
- [templates/rollout-plan.md](templates/rollout-plan.md) — fill-in plan and checklists.

## When to use
- A revenue leader owns the department's AI program and needs a rollout plan.
- A pilot is running and someone must decide whether to scale.
- Leadership wants an ROI readout or a budget case for next year.
- Spend is rising and the team must decide between coaching and capping.

## Instructions

1. **Place the org on the maturity ladder.** Ask what Claude can read and write today, how much of
   the work it is trusted to finish, and whether top performers' methods are written down as shared
   skills. Name the next level and what it needs (connections, trust, governance: who can publish
   skills, what data each workflow can reach, who owns results).

2. **Make the setup decisions before any pilot date.**
   - Owner: RevOps is a strong default (owns CRM and pipeline/forecast reporting).
   - Connect systems (CRM, call recording, email, Slack) so reps stop uploading files by hand.
   - Name an IT owner (provisioning, SSO, admin consents) and agree provisioning dates first.
   - Start the security review early: data boundaries, connector permission model, auditability,
     telemetry export.
   - Pick **one activity metric** and **one revenue metric**, set a baseline, commit to readout dates.
   - Set spend limits by org, group, and user; restrict costlier capabilities by role; track usage
     from day one; give champions more headroom.
   - Pick two or three teams with motivated leads; provision plugins at the admin level.

3. **Set up the team's toolkit.** Provision the starter pack (see the catalog). Preload the Sales
   plugin settings file (name, quota, positioning, competitors) before first login so every rep has
   a working command on day one. Connectors inherit each rep's existing permissions.

4. **Run the three phases.**
   - **Setup:** IT handles workspace and SSO while RevOps configures connectors and plugins. Choose
     champions with sales managers: two or three per department, or one per 25-50 users, with
     dedicated hours.
   - **Pilot:** each pilot team runs two or three use cases. Champions demo on live accounts, staff
     office hours, and write the first skills. Track how many champion-built skills pilot teams use
     regularly — the best early signal for scaling.
   - **Scale:** move pilot skills into the shared bundle; provision in waves (e.g., 25 → 150 →
     everyone); bring Claude output into standing meetings (e.g., `/forecast` in the weekly call).

5. **Measure ROI the way the guide recommends.** Compare pilot vs non-pilot teams in the same
   quarter on pipeline per rep, cycle length, and win rate, rather than before/after. Sort returns
   into efficiency, expansion, and new capabilities. Scale when output persists past the novelty,
   quality checks hold, and pilot teams outperform on the chosen outcome metric. After a full
   quarter, set daily spend per rep next to results, and lead budget talks with expansion and new
   capabilities — not hours saved.

6. **Read spend in context.** High spend plus high output (often a champion) is the design working.
   High spend with little output → coach first; lower the cap only if coaching does not help.

7. **Pre-empt the three pitfalls** (details in the reference): pilot with no end date, seats scaled
   without champions, spend ignored until the invoice.

8. **Use the template** in [templates/rollout-plan.md](templates/rollout-plan.md) to produce the
   written plan. Do not invent numbers or customer claims beyond the reference.

## Examples
- User: "Our 25-seat pilot has run for three quarters and everyone likes it."
  → Pilot without an end date. Put a scale-decision date on the sponsoring executive's calendar,
  name the decider, and agree what a "yes" requires.
- User: "We're going from 25 to 150 seats next month with our three champions."
  → Hold one champion per 25-50 users; ask incoming managers to name champions now so current
  champions can train them.
- User: "The CFO asked what we got for the spend."
  → Report pilot-vs-non-pilot pipeline per rep, cycle length, win rate; frame as efficiency,
  expansion, new capabilities; avoid a case built only on hours saved.
- User: "One rep is top of the spend table."
  → Check what they produced (briefs, opportunity updates, proposals). If low output, have a
  champion coach them on commands, skills, and connectors before cutting the cap.
