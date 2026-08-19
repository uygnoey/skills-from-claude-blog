---
name: inference-dlp-rollout
description: Plan and execute a staged rollout of inline data loss prevention for an enterprise AI deployment, where a policy server returns an allow/deny verdict on every prompt and tool call response before the model sees it. Use when a security or compliance team must inspect AI traffic at a control point they own, when an existing DLP program has to be extended to AI surfaces, or when enforcement must be introduced without blocking users on day one.
---

# Inline DLP rollout for enterprise AI

Inline DLP puts a synchronous checkpoint in front of the model. Every inference request is routed to a policy server the organization controls; the server returns allow or deny, and generation proceeds only after a verdict arrives. Tool call responses are checked the same way before they are returned to the model.

The hard part is not turning it on. It is turning it on without a wave of false denials, and being able to prove afterwards what was inspected and what was blocked.

## Instructions

### 1. Establish the enforcement model before writing any policy

Read [references/enforcement-model.md](references/enforcement-model.md) and confirm, in writing, the answers to these:

- **Which surfaces are in scope?** Chat, coding agents, agentic workspaces, and tool calls made through connectors, skills, and plugins can all be covered by one organization-level configuration. Decide whether you want all of them from the start.
- **What gets inspected?** The prompt plus its surrounding context before generation, and tool call responses before they return to the model.
- **What is the failure policy?** If the policy server is slow or unreachable, does traffic fail open (allow) or fail closed (deny)? Pick one deliberately and record the timeout that triggers it.
- **Who is excluded?** Role-based exclusions exist so that break-glass and administrative roles are not locked out by their own control.

Do not skip this step. A rollout that starts with rules instead of an enforcement model produces rules nobody can explain later.

### 2. Reuse the DLP server you already have

The protocol is webhook-based with a published schema, which means the decision point can be the same server the rest of the security stack already reports to — a commercial DLP or CASB platform, or an in-house policy service. Prefer reuse over a new bespoke service:

- One policy corpus instead of two that drift apart.
- One audit trail for compliance evidence.
- Vendor integrations can be pointed at by configuration rather than rebuilt.

If a new server is genuinely required, hold it to the same latency and availability bar as the rest of the inline path: it is now in the critical path of every request.

### 3. Run shadow mode first, and treat it as a measurement phase

Enable shadow mode — the server evaluates every request and returns allow regardless of verdict — and leave it on long enough to collect a representative week of traffic, including the noisy days.

While in shadow mode, measure:

- **Would-be denial rate**, overall and per surface. A rate that looks fine in aggregate can be intolerable inside one team.
- **Top matching rules.** A handful of rules usually account for most hits; they are also where the false positives are.
- **Added latency** at the tail, not the median. The check is synchronous.
- **Timeout and error rate** from the policy server itself.

Tune the rules until the would-be denial rate is dominated by hits you would actually want to block.

### 4. Ramp enforcement by percentage, with an exit condition per step

Move from shadow mode to enforcement in percentage-based steps rather than one switch. Write the exit condition for each step before starting it, for example: denial rate within the band agreed with the business, no policy-server timeouts above the agreed threshold, and no unresolved escalations from the previous step.

A workable shape, adapted to your own risk tolerance:

| Step | Population | Watch for |
|---|---|---|
| 0 | Everyone, shadow mode | Rule quality, latency, server stability |
| 1 | Security team only, enforcing | Denials that surprise the rule authors |
| 2 | Small percentage of the org | Support tickets, workaround behaviour |
| 3 | Growing percentage | Whether the denial rate holds as usage broadens |
| 4 | Full enforcement | Steady-state noise, exclusion list still justified |

Keep the ability to drop back to shadow mode at any step, and make sure whoever is on call knows how.

### 5. Give users a path when a request is denied

An inline block that leaves no route forward becomes a reason to move work to an unmonitored channel — the exact outcome the control exists to prevent. Before enforcement, publish:

- What a denial looks like from the user's side.
- Who to contact and what evidence to include.
- How an exception is requested, who approves it, and how long it lasts.

### 6. Keep the rollout state reviewable

Record every configuration change — shadow mode on or off, percentage, exclusions, failure policy, timeout — with the date and the reason. Use [templates/rollout-plan.md](templates/rollout-plan.md); the decision log at the bottom is the part that matters six months later.

## Examples

### Example 1: extending an existing DLP program to AI surfaces

A regulated company already routes email and endpoint DLP through one vendor platform.

1. Point the inline AI checkpoint at that same platform rather than standing up a new one.
2. Enable shadow mode organization-wide and collect two weeks of would-be verdicts.
3. Discover that a single source-code-fingerprint rule accounts for most hits, nearly all of them engineers pasting their own repository's code into a coding agent — expected work, not exfiltration.
4. Narrow that rule to the repositories that actually carry the restricted classification.
5. Ramp enforcement 5% then 25% then 100% over three weeks, holding at each step until the exit conditions are met.

### Example 2: choosing a failure policy

The policy server has a maintenance window. The team must decide what happens to AI traffic during it.

- **Fail closed** — no inference proceeds without a verdict. Correct when the data at risk outweighs the productivity loss; requires the maintenance window to be communicated like any other outage.
- **Fail open** — traffic proceeds if the server does not answer within the timeout. Correct when availability dominates; requires that fail-open events are logged, alerted on, and reviewed, because they are gaps in coverage.

Record the choice, the timeout, and the review process in the decision log. Do not leave it at the default because nobody discussed it.

### Example 3: what not to model with this control

A team wants to use the inline checkpoint to enforce coding standards on agent-authored diffs. That is the wrong tool: this checkpoint is a synchronous, security-owned gate on data leaving for the model, and every rule added to it costs latency on every request. Style and quality gates belong in the development lifecycle, not in the inline inference path.

## Notes

- Inspection is synchronous and sits in the critical path. Treat the policy server's latency and availability as a production dependency of every AI surface.
- This is a *server-side* control, distinct from a coding agent's client-side lifecycle hooks. The two can coexist; they enforce at different points and are configured by different people.
- Consult the vendor documentation for the current schema, configuration fields, and availability before implementing. Details not covered here are in the source post and its linked documentation.
