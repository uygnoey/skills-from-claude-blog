---
name: ai-native-sdlc
description: Redesign a software development lifecycle around agentic coding — six stages (Plan, Design, Build, Test, Deploy, Maintain) that each end by committing a version-controlled artifact the next stage reads. Use when agentic coding has made the build phase fast but planning, review, testing, and deployment still run at human speed; when review queues or security sign-off have become the bottleneck; when deciding which SDLC stage to transform first and in what order; when encoding policy as skills, hooks, and managed settings instead of enforcing it in review meetings; or when closing the loop so production signals write the next intent.md without a person in the invocation path. Covers the intent.md / spec.md / plan.md artifact chain, plan mode and auto mode, parallel worktree sessions and subagents, feedback loops and continuous evals, dual-direction PR review, approval-gate hooks, and per-stage leading and lagging indicators.
---

# The AI-native SDLC

Code is no longer the bottleneck. When agents write most of the diff, the constraint moves to
the human-speed steps on either side of build — plan, review, test, deploy — and the controls
designed for human output stop matching reality.

The AI-native SDLC keeps the old control objectives and changes the enforcement. The linear
flow becomes a loop, AI is embedded at each point, and **every stage ends by committing an
artifact the next stage reads.** The chain of commits is the audit trail: who asked for what,
what the agent produced, and who approved it. Humans stay accountable for every decision that
requires judgment.

## Instructions

### The artifact chain

Do not treat the stages as phases with handoffs. Treat them as a loop connected by committed
files, where each commit is the trigger for the next stage.

| Committed artifact | Written in | Triggers |
|---|---|---|
| `intent.md` | Stage 1 Plan | the requirements-and-design pass |
| `spec.md` | Stage 2 Design | plan mode |
| `plan.md` | Stage 3 Build | implementation |
| the diff and its tests | Stage 3–4 | PR review |
| the PR with its review findings | Stage 5 Deploy | the pipeline |
| the incident record | Stage 6 Maintain | the next `intent.md` |

For the early stages `.md` files are the artifact because a product owner and an agent can both
read and act on the same file. From Build onward the artifact is code and its records.

Start by prompting each step by hand. The end state is a loop where each accepted artifact fires
the next gate, and human attention concentrates at the gates — reviewing what the agent flagged
rather than starting each stage from scratch.

### Choosing where to start

Plays are grouped by stage, but stage order is not adoption order. Adopt any play whose
prerequisites are already met; for the rest, adopt what they depend on first.

- **No prerequisites** — capture as `intent.md`, `CLAUDE.md`, skills as institutional knowledge,
  plan mode as default, feedback loops, hooks as approval gates.
- **Depends on `intent.md` plus policy skills** — requirements and design.
- **Depends on `CLAUDE.md`** — parallel sessions and subagents, continuous evals.
- **Depends on review plus gates** — CI/CD integration.
- **Depends on everything above** — closing the loop.

Full per-play detail — what changes, prerequisites, infrastructure, execution steps, governance,
measurement — is in [references/stage-plays.md](references/stage-plays.md).

### Stage 1 — Plan: capture intent once

The originator brainstorms with Claude in their own words until the idea is concrete, then asks
Claude to write the result as `intent.md` using the organization's template (encode the template
as a skill). The originator corrects anything Claude misunderstood and commits the file to a
shared, version-controlled home the product owner watches — an `intent/` folder in the product
repo is the simplest home for a single product.

Contributors without git experience commit through a version-control connector from claude.ai or
Cowork. Scaffold: [templates/intent.md](templates/intent.md).

### Stage 2 — Design: requirements and design collapse into one session

Claude takes the accepted `intent.md` and produces a requirements and design spec, constrained by
the organization's skills for brand, security, compliance, and UX, with areas of concern flagged.
The product owner reviews the spec but does not write it, works the flagged concerns first with
each policy owner, and commits `spec.md` alongside `intent.md`.

Run the pass by hand first, then codify it as an organization-level command, then make acceptance
of `intent.md` the trigger for a non-interactive job that commits `spec.md` as a pull request.
The prompt to start from: [templates/design-pass-prompt.md](templates/design-pass-prompt.md).

### Stage 3 — Build: nothing is implemented without an accepted plan

1. **Plan mode is the default entry point.** Give Claude `intent.md` and `spec.md` and ask for a
   plan naming the files that change, the order of work, and the tests that prove it. Interrogate
   it — what could break, which step is riskiest, what options were rejected. Iterate until an
   engineer who never saw the conversation could implement from the plan alone. Commit it as
   `plan.md`, then let Claude implement. Keep `plan.md` in sync in the same commit when the
   implementation departs from it. Scaffold: [templates/plan.md](templates/plan.md).
2. **`CLAUDE.md` carries institutional knowledge.** Run `/init`, cut the result down to what a new
   joiner needs on day one, check it in at the repo root, keep it under a page. Working rule: when
   Claude makes the same mistake twice, the correction goes into `CLAUDE.md`. Scaffold:
   [templates/claude-md.md](templates/claude-md.md).
3. **Skills encode policy that must be applied consistently.** Write a skill for institutional
   knowledge that must hold across sessions; do not write one for what belongs in `CLAUDE.md` or a
   prompt. Ship it at `.claude/skills/<name>/` or distribute it organization-wide as a plugin, then
   test that it actually triggers. Worked example: [examples/policy-skill.md](examples/policy-skill.md).
4. **Hooks are the deterministic layer behind advisory skills.** Build-phase hooks block edits to
   protected paths, run the formatter and linter after edits, and keep credentials out of the diff.
   Keep them fast and scoped to the changed file; heavier checks belong at the commit or the PR. A
   hook that asks a human for approval belongs in Stage 5, not here.
5. **Auto mode and parallel sessions scale one engineer.** As the guardrails mature, auto-accept
   becomes the default for routine work with a tight spec, a small blast radius, and code the tests
   already cover. Split work into tasks touching different files, give each its own worktree
   (`claude --worktree feature-auth`), start with two or three, and add sessions only while review
   keeps up. Turn recurring jobs into subagents checked into `.claude/agents/`.

### Stage 4 — Test: verification moves inside the session

- **Give Claude a feedback loop.** Wrap checking the work in a single command, list it in the
  `CLAUDE.md` Commands section with an example of healthy output, and state a quantifiable target
  so Claude can check itself. For bug fixes, write the failing test first, commit it, and only then
  ask for the fix without editing the test. For UI work, close the loop with a browser or
  screenshot tool against the approved mock. Make verification part of "done."
  Block: [templates/verification-block.md](templates/verification-block.md).
- **Protect the loop.** An agent fixing code must not be able to weaken the check on that code —
  block edits to test files during a fix task, or reject any test change in review.
- **Continuous evals are the AI-native stage gate.** Collect 20–50 real tasks with their accepted
  outcomes, write each as a prompt plus the checks that define acceptable, and run the suite
  non-interactively in CI on a schedule and on any change to `CLAUDE.md`, skills, or hooks. Gate
  configuration changes on the pass rate. Every production incident becomes a permanent eval,
  written by the team that owned it. Workflow: [examples/agent-evals.yml](examples/agent-evals.yml).

### Stage 5 — Deploy: review both directions, gate the release

- **Claude gives and receives review.** All PRs get an identical set of passes with findings ranked
  by severity, so human attention moves up a level — does the change do what the plan intended, and
  is the risk acceptable. The tech lead writes the policy as `REVIEW.md` at the repo root, split
  into the passes the organization cares about, defining what counts as Important versus a Nit and
  what to skip. Scaffold: [templates/review-md.md](templates/review-md.md).
- **Findings do not approve or block on their own.** Branch protection still requires a code owner.
  Tagging `@claude` on a review comment has Claude address it and push the fix, with the thread
  recording both request and change. Review findings feed back into `CLAUDE.md` on the second
  occurrence of a mistake.
- **Hooks become approval gates.** List the human approvals that must survive — change management
  sign-off, release authorization, edits to protected paths — and express each as a hook that can
  allow, ask, or block. Team hooks live in `.claude/settings.json` in git; non-negotiable hooks live
  in managed settings that engineers cannot switch off. A block must explain itself and name the
  route to approval. Working hook: [examples/production-gate.md](examples/production-gate.md).
- **CI/CD runs Claude non-interactively.** Start with read-only judgment steps (triage a failed
  build, summarize a flaky test, draft the changelog), then add write steps behind the existing
  gates. Sandbox agent jobs with short-lived scoped tokens and no standing production credentials,
  expose deploy/status/rollback through MCP as a per-environment allowlist, and tier autonomy by
  environment: free in development, gated in production. Rehearse rollback regularly in staging —
  Stage 6 calls it.

### Stage 6 — Maintain: close the loop

A deterministic script watches production and invokes Claude when a control band is breached. No
model is involved in detection.

1. Pick one metric with a stable rolling baseline — CI test failure rate, post-deploy 5xx rate, PR
   cycle time.
2. Write the detection script (mean and standard deviation over a rolling window, with Western
   Electric or similar rules so slow drift is caught as well as spikes). Version control and unit
   test it.
3. Define response tiers in version-controlled config: 1σ logs, 2σ invokes Claude read-only to
   diagnose, 3σ lets Claude act — but only by opening a PR into the review gate or triggering a
   pre-approved runbook. Config: [data/bands.yaml](data/bands.yaml).
4. Trigger from a scheduled workflow, a monitoring webhook, or a cron job inside the network. Claude
   runs stateless and non-interactive, so a loop can begin and end without anyone starting it.
5. The agent writes its diagnosis as `intent.md` in the Stage 1 format. From there it goes through
   the pipeline like anything else.
6. The service owner or on-call engineer triages: fix now, schedule, or dismiss. Dismissals tune the
   bands. When a fix ships, add an eval for the incident.

Work also arrives through chat. Claude Tag makes Claude a channel member under its own identity, so
each incident gets a first responder; a small well-bounded fix arrives as a PR through the review
gate and anything larger is written up as `intent.md`. The channel becomes the audit trail.

### Governance

Controls are version-controlled rules, not meetings. The layers, weakest to strongest:

- **Skills** — advisory. They make the policy likely to be applied while the code is written.
- **Hooks** — deterministic. They allow, ask, or block on every matching action.
- **Branch protection** — separation of duties. The agent that wrote the code cannot approve it.
- **Managed settings** — org-wide, not overridable by an engineer, project file, or CLI flag.

A policy that must always hold needs something deterministic behind the skill. The skill makes
violations rare; the hook makes them close to impossible. Detail and the line-by-line worked
managed-settings example: [references/governance-and-controls.md](references/governance-and-controls.md).

When an existing tool already holds the record — Jira, ServiceNow, a requirements tool with
regulatory traceability, Figma — name **one** source of truth per artifact and let everything else
hold a copy or a link. See [references/legacy-integration.md](references/legacy-integration.md).

### Measurement

Every play carries a leading indicator (is the change taking hold) and a lagging one (did it
improve the outcome). The per-stage table, and where each number is read from, is in
[references/measurement.md](references/measurement.md).

## Examples

**Stage 1 — an `intent.md` written by a claims operations lead, not a product manager**

```markdown
# Intent: claims status self-service
Author: J. Ortiz (claims operations). Status: draft.

## Problem
Customers phone the contact center to ask where their claim is.
Handlers spend roughly a third of call time on status-only queries.

## Proposed outcome
Customers see claim status, next step and expected date in the portal.

## Affected users and systems
Claims handlers, portal team, claims-core API.

## Constraints
No new PII in the portal session. Existing authentication only.

## Open questions
Do third-party loss adjusters need access too?
```

**Stage 3 — the `plan.md` that came out of it**

```markdown
# Plan: claims status self-service (from intent.md 2026-06-02)
## Files that change
portal/src/claims/StatusPanel.tsx (new), claims-api/routes/status.py,
claims-api/tests/test_status.py
## Order of work
1. Add the status endpoint behind existing auth.
2. Panel against the endpoint.
3. Wire into the portal nav.
## Risks
The claims-core API rate-limits at 50 rps; the panel must cache.
## Proof
test_status.py covers the four claim states; screenshot matches the
approved mock.
```

**Stage 5 — a pipeline step that spends a model call on judgment, not on scripting**

```yaml
- name: Triage failed build
  if: failure()
  run: >
    claude -p "Read the build log at out/build.log. Identify the most
    likely cause, say whether the failure looks flaky or real, and write a
    three-line summary for the PR thread." >> triage.md
```

**Stage 6 — what a 3σ breach may do**

- CI test failure rate breaches 3σ → the agent quarantines the flaky test or opens a revert PR, and
  the review gate decides.
- Post-deploy 5xx rate breaches 3σ with a deployment in the window → the agent triggers the existing
  rollback pipeline.
- PR cycle time trips a drift rule → the agent writes a report for engineering leadership, which
  shows the harness works for process metrics as well as production ones.

## Source

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) by Louis Claxton
— published 2026-08-21.
