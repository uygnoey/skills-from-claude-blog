---
name: auto-mode-production-practices
description: Operating patterns for running Claude Code's auto mode as a daily production default, drawn from how Nuro, Gusto, and Garner Health use it. Use when deciding whether a team should default to auto mode, when designing the guardrails around it (deny rules, MCP proxying, classifier tuning, telemetry), when choosing which work to leave unattended overnight, or when deciding which sessions should step out of auto mode and into manual review.
---

# Running auto mode in production

Auto mode replaces per-command approval prompts with a classifier that evaluates each action
and blocks the potentially harmful ones. Reviewing every command keeps a human in the loop
but becomes the bottleneck once sessions run for hours or in parallel; skipping permission
checks entirely is how prompt injection, scope drift, and deleted production resources get
through. Across all Claude Code usage, Claude now works **9x longer between interruptions**
than under the previous default.

This skill covers how to operate it, not how to justify it. For what each team configured,
read [references/team-practices.md](references/team-practices.md); for which work survives
unattended, read [references/unattended-task-patterns.md](references/unattended-task-patterns.md).

## Instructions

### 1. Put guardrails around auto mode before turning it on

Every team in the source post runs auto mode inside a boundary they set themselves. The
classifier makes judgment calls *within* those limits — it does not replace them.

- **Deny the commands that must never run**, regardless of context. Nuro's engineers deny the
  most dangerous commands, such as recursive deletes, outright in their settings.
- **Constrain the tools before the classifier sees them.** Gusto routes MCP traffic through a
  governed proxy layer with tool guards and prompt inspection, so agents already operate with
  tightly scoped permissions.
- **Standardize the workflows rather than letting each person invent one.** Garner Health runs
  its lifecycle as a plugin of standardized skills.
- **Instrument it.** Garner's stated precondition for confidence is telemetry: without it,
  telling everyone to build their own workflows would be dangerous.

### 2. Decide the tuning, and keep it narrow

Out of the box the classifier needs little tuning. The adjustment both Nuro and Garner Health
made independently is worth copying by default:

- **Do not let auto mode approve actions that communicate with other people** — sending Slack
  messages, sending email. This is a policy choice about acting on someone's behalf, not a
  safety judgment.

Teams working on core intellectual property at Garner Health tuned the classifier's injected
prompts to be more or less permissive for their specific work. Treat per-team permissiveness
as the escape valve, not a blanket loosening.

### 3. Name the sessions that step out of auto mode

Have each engineer decide this in advance rather than mid-task. The published examples:

| Situation | Mode used instead | Reason |
| --- | --- | --- |
| Claude Code reviews a pull request on your behalf | interactive mode | The output goes to other teams |
| Production infrastructure — Terraform, AWS, direct POST calls against live APIs | accept edits, verifying each tool call by hand | High blast radius |

The framing to apply: weigh the time saved against what the agent could reasonably get wrong
and how catastrophic that would be. You remain responsible for what happens.

### 4. Match the task shape to unattended running

Long unattended runs work when the task carries its own success signal. See
`references/unattended-task-patterns.md`. The short version: a clear, measurable evaluation
metric lets the agent tell on its own whether it is improving or regressing, so it can keep
iterating without a human. Tasks whose quality can only be judged by a person are the wrong
shape for overnight work regardless of permission mode.

Auto mode also serves short sessions. Twenty-minute bursts — endpoint investigations, log
audits, connector management, doc ingestion across MCP servers — benefit from the
prompt-injection protection and intent checking rather than from longer runs.

### 5. Measure whether the classifier is earning its place

Gusto's own analysis found roughly 10% of session transcripts since mid-May 2026 included an
auto mode denial — evidence the classifier does real work without dragging on legitimate
tasks. Track the same number. A denial rate near zero suggests the guardrails are doing all
the work; a rate high enough to interrupt routine tasks suggests the deny rules or the
task scoping need attention.

When the classifier does step in, expect it to explain why. Reported experience: blocks
landed on genuine drift from the original request, and the explanation made sense.

### 6. Write the policy down

Fill in [templates/team-auto-mode-policy.md](templates/team-auto-mode-policy.md) so the
guardrails, exceptions, tuning, and telemetry are a team artifact rather than individual
habit.

## Examples

### Example 1 — an engineer asks whether to run auto mode for everything

Ask what the work touches. If it stays inside their own repositories and the dangerous
commands are already denied in settings, auto mode for 100% of coding work is the pattern
Nuro reports, often with three or four parallel sessions checked in on periodically. Carve
out the work that leaves their boundary — a PR review done on their behalf goes back to
interactive mode.

### Example 2 — a platform team wants to enable auto mode org-wide

Sequence it as Garner Health did: standardize the workflows first (a plugin of shared
skills), wire up telemetry, then make auto mode the default. Add the one tuning adjustment —
no auto-approval of actions that message other people — and let individual teams tune
permissiveness for their own IP-sensitive work. Without telemetry, hold the rollout.

### Example 3 — someone is about to use bypass permissions for speed

Name the tradeoff concretely. Bypass permissions removes the prompt-injection screening and
the intent check, which is the specific reason a Gusto cloud engineer chose auto mode over it
for short, hands-off sessions. If the friction is permission fatigue rather than a need for
zero checks, auto mode addresses the fatigue without removing the checks.

### Example 4 — designing an overnight agent

Pick a task with a measurable signal the agent can iterate against: hill-climbing an
evaluation metric, shrinking a binary's memory footprint, or anything where a suite tells the
agent whether it improved. Set the deny rules, start it in auto mode, and expect finished PRs
for human review in the morning rather than merged changes.

## Source

- https://claude.com/blog/auto-mode-in-production
