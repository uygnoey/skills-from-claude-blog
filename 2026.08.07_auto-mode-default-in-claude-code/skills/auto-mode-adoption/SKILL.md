---
name: auto-mode-adoption
description: Decide, configure, and roll out a default permission mode in Claude Code now that auto mode is the default on Pro, Max, and Team plans. Use when choosing between auto mode, manual permission prompts, and bypass permissions; when an admin needs to pin or disable an org-wide default; when explaining the safety evidence behind the change; or when working out which permission rules still apply under auto mode and when to step out of it.
---

# Adopting auto mode as the default permission mode

Auto mode replaces per-tool-call approval prompts with a classifier that evaluates every
tool call and blocks actions that are irreversible, destructive, or aimed outside the
user's environment. As of August 14, 2026, new Claude Code sessions on Pro, Max, and Team
plans start in auto mode. On Claude Enterprise, the Claude API, Claude Platform on AWS,
Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry it remains opt-in at
the time of the source post, with a plan to make it the default in the following month.

Read [references/permission-model.md](references/permission-model.md) for how the classifier,
permission rules, fallbacks, and recent hardening fit together, and
[references/safety-evidence.md](references/safety-evidence.md) for the published numbers and
their stated limits.

## Instructions

### 1. Establish what will change for this user or org

- **Pro, Max, Team, no default set** — new sessions start in auto mode; the user gets an
  in-product notice.
- **Pro, Max, Team, a different default already set** — the user may see a one-time prompt
  asking whether to switch.
- **A pinned default (including a Team admin's managed setting)** — nothing changes.
- **Enterprise / API / cloud platforms** — still opt-in; an Enterprise admin can make auto
  mode the default through managed settings today.

Classifier overhead tokens are no longer billed on Pro, Max, and Team plans.

### 2. Choose a default deliberately rather than by inertia

Do not treat "keep manual prompts" as the conservative option by default. The evidence in
`references/safety-evidence.md` shows manual approval performing worse than auto mode on
every measure the post reports, and degrading further as sessions get longer.

Recommend auto mode when:

- Sessions are long-running, parallel, or unattended, so prompt interruptions are the
  bottleneck.
- The alternative in practice is `bypassPermissions`, broad Bash allow-rules, or reflexive
  approval — all of which remove review entirely.

Recommend stepping out of auto mode when:

- The session touches production infrastructure directly, or makes high-stakes,
  hard-to-reverse changes. The source post explicitly still recommends reviewing Claude's
  actions yourself here.
- An action must never be automated for policy reasons even if it is safe (for example,
  messages sent on a person's behalf).

### 3. Audit permission rules before switching

Under auto mode, permission rules still fire before the classifier — **except** allow-rules
broad enough to grant arbitrary code execution, such as `Bash(python:*)` or `Bash(node:*)`.
Those are set aside while in auto mode so commands cannot skip the classifier. Settings
files are not modified, and the rules apply again as soon as the mode changes.

So, before switching:

- List existing allow-rules and mark which are interpreter-level (they will be inactive).
- Keep deny rules for commands that must never run regardless of mode — the classifier
  makes its judgment calls inside those guardrails.
- Record hard-deny categories the organization wants beyond the built-in data-exfiltration
  denies, which are customizable in settings.

### 4. Configure the mode

- Switch interactively: `Shift+Tab` in the CLI, or the mode dropdown in the desktop app.
- Pin an org-wide default: `defaultMode` in managed settings.
- Turn auto mode off entirely: `disableAutoMode` in managed settings.

Consult the auto mode documentation for full configuration syntax; only the setting names
above are given in the source post.

### 5. Plan the rollout and record the decision

Fill in [templates/rollout-decision-record.md](templates/rollout-decision-record.md) so the
choice, its rationale, and its exceptions are written down rather than rediscovered later.
Cover at minimum: the default being set, who it applies to, which rules were audited, which
categories are hard-denied, and which workflows are expected to step out of auto mode.

### 6. State the limits honestly

Auto mode relies on classification systems and does not eliminate risk. The published miss
rates come from adversarial, synthetic attack sets and should not be presented as real-world
miss rates. Say so when you make the recommendation.

## Examples

### Example 1 — an individual on the Max plan asks whether to keep manual prompts

Establish the change (step 1): no default set, so sessions will start in auto mode on
August 14. Ask what the sessions look like. If they are multi-hour or parallel runs, keep
auto mode: manual review measurably decays over long sessions (~17% of dangerous commands
blocked early, ~5% after 50+ prompts) while the classifier's rate stays flat. Advise
switching out with `Shift+Tab` for the specific sessions that touch production
infrastructure.

### Example 2 — a Team admin wants auto mode off for one group

Auto mode can be turned off entirely with `disableAutoMode`, or a different default pinned
with `defaultMode`, in managed settings. Note the tradeoff first: turning it off returns
those users to permission prompts, where the reported approval rate is 97% and the
rejection rate 3%. If the concern is a specific action category rather than the mode, a
hard-deny rule is the narrower fix — the classifier is designed never to approve
data-exfiltration actions, and that rule set is extensible from settings.

### Example 3 — a security reviewer asks for the evidence

Summarize from `references/safety-evidence.md`: the 1,053-tester controlled study (13.6%
human vs 89% auto mode), the flagged-session analysis (6.3% vs 2.4% at production-level
severity), the Apollo Research engagement (miss rate 12% → 7%, verified on a held-out set),
and the Trajectory Labs prompt-injection evaluation (0 of 720 attempts succeeded against
Claude models in auto mode). Then state the caveats the post states: the attacks are
synthetic and adversarial by design, the browser integration tested was a thin third-party
wrapper rather than a first-party extension with its own safeguards, and classification
does not eliminate risk.

### Example 4 — the classifier keeps blocking a legitimate task

Expect Claude to route around a block or ask directly. If it cannot make progress — three
blocks in a row or twenty in a session — Claude Code falls back to manual approvals on its
own. When a task legitimately needs an action in a hard-deny category, the action is to
switch out of auto mode or run the command yourself, not to weaken the deny rule.

## Source

- https://claude.com/blog/auto-mode-default-in-claude-code
