---
name: agentic-coding-operating-rules
description: Apply the five operating rules fast-growing startups use to ship with agentic coding — everyone ships, automate the tedium, trust but verify, build for rebuilding, and prototype-dogfood-productionize. Use when deciding how a small team should organize around Claude Code; when non-engineers want to contribute product changes; when choosing which parts of the SDLC to hand to agents and how to gate them; when a rewrite keeps losing the prioritization fight; or when you want internal agent experiments to graduate into customer-facing product.
---

# The five operating rules for shipping with agentic coding

Distilled from interviews with more than a dozen fast-growing startups —
Artemis Security, Cainex, Clay, ClickHouse, Cognition, Commure, Crosby,
Emergent, Harvey, Heidi, Higgsfield, Omni, Parahelp, Translucent, and Zingage —
about how they operate with Claude Code.

The rules are ordered, and rules 2 and 3 are a pair: you cannot automate a
process you have no reliable way to verify.

1. **Everyone ships** — lower the barrier so the person who understands the
   problem builds the first version.
2. **Automate the tedium** — agents own the mechanical 80%; engineers spend
   their time on cases that need judgment.
3. **Trust, but verify** — automation is only safe where the outcome is
   monitored and checked.
4. **Build for rebuilding** — treat scaffolding as disposable, because model
   capability keeps shifting underneath it.
5. **Prototype, dogfood, productionize** — building *with* AI is how you learn
   to build products *with* AI.

Full statements of each rule, with what it rules in and out, are in
[references/five-rules.md](./references/five-rules.md). The consolidated
technical checklist from the guide is in
[references/checklist.md](./references/checklist.md).

## Instructions

### 1. Open the 0→1 step to everyone, then make it systemic

Agentic coding lowers the barrier to entry, so a non-engineer with domain
expertise can produce a working first version instead of describing it down a
chain of hand-offs. Heidi calls the old path the "broken telephone problem":
idea → PM → designer → engineer, with the essence lost by the time it ships.

There is still a division of labor. Marketers still market and developers still
develop. What opens up is the first step — getting an idea to a working
prototype.

Do three things, or "everyone ships" stays a slogan:

- **Create connections.** Claude cannot understand what it cannot see. Connect
  it to the sources of truth and the tools your team already lives in. Reach for
  MCP whenever people are copying and pasting between a tool and Claude; reach
  for the CLI when a mature command-line tool already exists (`gh`, `kubectl`,
  `bq`, `psql`) and you want the agent working against the same ground truth
  your engineers do — it is often more token-efficient.
- **Give prototypes a road onto the roadmap.** Clay runs quarterly reviews where
  prototypes are considered for the formal roadmap. Omni keeps a dedicated Slack
  channel for Claude-generated prototypes that senior technical staff post into
  as well. Without a forum, contributions stay a matter of individual ambition.
- **Share skills.** Reusable instruction files encode team standards so
  democratized development still produces a cohesive product. Share them through
  a directory or a plugin marketplace so one person's best practice transfers
  instantly. Use `CLAUDE.md` in each subdirectory for conventions that apply
  every time in that subdirectory; use skills for on-demand procedural
  workflows.

Emergent's stance on the shared knowledge base is worth copying: "instead of
trying to be perfect here, it is ok to live with slightly outdated context files
as long as the agent can quickly verify and course correct."

### 2. Hand agents the mechanical 80%, end to end

Two moves, and the startups in the guide made both:

**Integrate agents across the SDLC.** At Emergent a new hire bootstraps their
whole dev setup on day one by pointing Claude at the right markdown file — and
if Claude hits anything broken or out of date during onboarding, it updates that
file. Automated review runs against vetted technical and compliance frameworks
before anything ships (Heidi). Engineers run multiple PRs in flight; one Commure
engineer ran a ~13-ticket initiative with subagents in parallel, each owning a
ticket and its PR.

**Build purpose-built agents that take a recurring task end to end.** At
ClickHouse, agents that fix flaky tests and find missing test coverage are now
the #2 and #3 contributors to the repo, and the team uses Claude Code to build
and iterate on the agents themselves. Four roles named in the guide are written
up as subagent definitions in this bundle's sibling `agents/` folder.

The same pattern extends past code. Self-service data analytics was the most
common non-SDLC process these teams automated — internal analytics agents
(Clay), feedback categorization against usage data (Heidi), summarizing thousands
of legal documents with subagents (Crosby), sweeping claims data for anomalies
(Commure), continuously mining hospital financial data (Translucent).

For fan-out analysis or adversarial review of another agent's work, ask for
dynamic workflows explicitly — with a model like Opus or Fable, say "fan out
multiple subagents" or "use a workflow."

### 3. Verify before you automate

None of these teams have agents merging to main and hoping. Build the checking
apparatus first:

- **Write down what cannot change.** Zingage gave Claude full autonomy early and
  got plausible code that drifted from their architecture in ways that looked
  right but weren't. The fix was 567 lines of invariants — how they frame
  problems, what has to be true no matter what, how to prove something works
  instead of trusting a confident answer. Put that in `CLAUDE.md` at the repo
  root so it travels with every session. A starting scaffold is in
  [templates/root-context-file.md](./templates/root-context-file.md).
- **Use loops where the stop condition is self-contained.** Flaky-test agents
  are the canonical example: the agent verifies its own fix by rerunning the test
  until it passes. Define the criteria in a skill — the more clearly defined, the
  better — and let the agent iterate to the goal.
- **Fix the principle, not the example.** Cainex's correction loop, described in
  full in [examples/self-improvement-loop.md](./examples/self-improvement-loop.md),
  routes expert corrections back into versioned agent instructions rather than
  patching case by case. Their first version overfitted and accumulated patches;
  they changed the approach to force general principles and cap how many
  specifics can enter a change at all.
- **Maintain evals, plural.** Keep a golden set of verified pairs plus random
  samples, run candidate changes across both, and surface regressions before
  anything ships. Multiple eval sets per key use case, updated regularly, are
  what let you prevent drift and evaluate new models. Higgsfield uses this to
  compress model-adoption cycles from days to hours.
- **Add deterministic gates where the work must be identical every time.** Hooks
  are user-defined commands that fire at fixed points in Claude Code's lifecycle
  and execute regardless of what the model decides — block a write that fails a
  lint, require a test pass before commit, strip secrets before anything leaves
  the sandbox. Dynamic workflows give deterministic sequencing with separate
  context windows; `/goal` helps on long tasks where Claude may call the job done
  prematurely, prefer its own findings when reviewing, or drift.

### 4. Treat scaffolding as disposable

Groundbreaking features and critical scaffolding get discarded the moment they
become sunk costs. Clay's framing: build it, build it again, build it again —
by the fourth build you know everything needed and you get it right. Harvey
re-architected the platform for each new wave of model capability; Cognition's
Walden Yan describes accepting that what you build today is likely scrapped in
six months to a year.

Two mechanics make this affordable:

- **Git worktrees.** Run the rebuild in an isolated checkout while the current
  version stays untouched — v2 running next to v1, evals against both, merge only
  when the new one wins. One repository and one object store, several checkouts,
  each on its own branch. This is what makes "build it four times" cheap.
- **Plan mode for non-trivial rewrites.** Start in plan mode (`--plan`, or
  Shift+Tab) so Claude explores the codebase and proposes the approach before
  writing code. It is the cheapest place to catch a rebuild about to drift from
  your architecture.

And finish the job: a rebuild isn't done when the new path ships, it's done when
the old path is gone. Commure turned teardown — which always lost the
prioritization fight because it is tedious and ships no features — into a skill
invocation: "for every feature flag already released to everyone, open a PR
removing it and the associated code," then an engineer reviews what comes back.

### 5. Close the loop from internal agent to shipped product

The repeated pattern: build an internal agent with Claude Code, use it
internally, and depending on the response promote it to a customer-facing
product — often on the Claude API, the SDK, or Claude Managed Agents.

Advancing your own agentic coding practice is what makes this work. It gives you
a grasp of model capabilities and of how harness design evolves at the frontier,
which you then spend on your own agents. Omni took inspiration from the file-vs-
embedding approach and avoided the complexity of a RAG pipeline, and adapted
parallelism concepts from Claude Code's harness into their own UI. Because
Emergent's app builder runs on the same models, they debug locally via Claude
Code to tell whether a reported behavior is model behavior or a harness issue.

## Examples

**A non-engineer ships the first version.** A go-to-market team member at Clay
built an autonomous agent that visits your websites, fills out lead-capture
forms, times the response, rates the experience, and generates a performance
report. It reached the roadmap through Clay's quarterly prototype review, not
through a ticket.

**Teardown as a fan-out.** Instead of scheduling a migration, a Commure engineer
invokes a skill: "for every feature flag already released to everyone, open a PR
removing it and the associated code." Migrations that used to eat a lot of dev
cycles become a plan and a fan out, done in a couple of hours, with the engineer
reviewing the PRs that come back.

**A verification loop in a regulated domain.** Cainex processes a batch with an
agent; auditors review output in an internal app, seeing the model's reasoning
and commenting on both; Claude Code reads the predictions plus every correction
and comment from the database, finds the instruction that produced the mistake,
revises it or writes new guidance, and back-tests the change against a golden set
plus random samples before anything ships. Walked through step by step in
[examples/self-improvement-loop.md](./examples/self-improvement-loop.md).

**More company patterns** — what each of the fifteen featured startups actually
did — are collected in
[examples/company-patterns.md](./examples/company-patterns.md).

## Source

Distilled from [The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups)
by Michael Segner (published 2026-08-20).
