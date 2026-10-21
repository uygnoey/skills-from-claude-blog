---
name: orchestrated-code-migrations
description: Run large code migrations (hundreds to thousands of pull requests across repos) with a tiered model setup in which a frontier orchestrator model does the upfront design — data models, API specs, algorithms — and directs up to dozens of smaller, cheaper worker models that make the file edits and run tests, while a human engineer steers and humans keep merges, deploys, and feature flags. Also covers picking a model and effort level per task from a benchmarked model × effort grid, recurring codebase cleanup passes, and safeguards that run outside the model loop. Based on how Block uses Claude Fable 5 with Opus and Sonnet workers. Use when planning or operating a multi-PR migration, choosing models for agent work, or setting guardrails for agent-written code.
---

## Purpose
Block uses Claude Fable 5 to orchestrate company-wide migrations that can mean hundreds or thousands
of pull requests across multiple repos and millions of lines of code. A human engineer steers; the
frontier model does the higher-level design and directs smaller, more cost-effective models (Opus or
Sonnet) to do the individual tasks. Early results: frontier tokens go to complex upfront planning, a
higher share of tokens goes to worker models, without a drop in quality. In a single migration Block
might merge a thousand PRs orchestrated this way.

## When to use
- A migration too large for one session or one PR at a time.
- Choosing which model and effort level to use for a recurring kind of agent task.
- Setting up daily or weekly agent passes that look for tech debt to clean up and consolidate.
- Deciding which agent actions to allow freely and which to gate behind humans.

## Instructions

### 1. Split roles by tier
- **Human engineer** — steers the migration and makes the hard design decisions.
- **Orchestrator (frontier model)** — designs the data models, API specs, and algorithms; breaks the
  migration into tasks; dispatches and reviews worker output (companion subagent:
  `migration-orchestrator`).
- **Workers (smaller models)** — make the actual file edits and run the tests, up to dozens in
  parallel (companion subagent: `migration-worker`).
Do not use the frontier model for everything: "Using Fable to fix a typo in a README is a very bad use
of resources."

### 2. Run the work where people can see it
Block runs the whole setup in Buzz, its open-source workspace where humans and agents share channels
and threads, for visibility into progress. Use any shared workspace that keeps many concurrent agents
observable; single-conversation interfaces don't keep up with dozens of agents.

### 3. Pick model × effort per task from a benchmark
Treat each model at each effort level as a separate option — a grid, not a slider. A frontier model on
low effort may beat another model on xhigh. Benchmark every model at every effort level for each use
case and publish a clear default ("use this model on high for this kind of task"). Fill in
[templates/model-effort-grid.md](templates/model-effort-grid.md). Automate the choice where possible
(Block is building an auto-selector), and let experts explore beyond the default.

### 4. Keep humans on irreversible steps
Merges to main, deploys to production, and related changes such as feature flags stay with people.
Agent changes must pass security checks, then two humans approve the deploy. See
[references/safeguards.md](references/safeguards.md).

### 5. Add recurring maintenance passes
With more PRs shipping, tech debt accumulates faster. Schedule daily or weekly agent passes over the
whole codebase asking what needs cleaning up and consolidating.

### 6. Capture what people learn at the system level
Individuals build local skills and context; move that knowledge into a shared system so every agent
run starts with the best context available.

## Examples

**Example — migration kickoff**
- Engineer: defines the target state and constraints of the migration.
- Orchestrator: writes the new data model and API spec, splits the work into per-repo/per-module
  tasks, and dispatches them to worker agents.
- Workers: each edits files for one task, runs the tests, and opens a PR.
- Humans: review and merge; deploys go through security checks plus dual approval.

**Example — model choice**
- Task: README typo fix → smallest adequate model from the grid, not the frontier model.
- Task: designing the migration's data model → frontier model at the effort level the grid recommends.
