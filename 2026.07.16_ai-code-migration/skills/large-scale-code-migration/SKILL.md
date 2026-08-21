---
name: large-scale-code-migration
description: Plan and execute a large-scale code migration — porting a codebase to a new language, framework, or architecture — using parallel agent loops, a written rulebook, a dependency map, adversarial review, and a mechanical verification harness. Use when a migration is too large to do by hand, when a port or rewrite keeps stalling, when deciding how to parallelize translation work across agents, or when a migration is producing plausible-looking code that drifts from the original's behavior. Covers the six-step process (rulebook and gap inventory, stress test, translate, compile, run, match behavior), how to design resumable work queues, when to fix the rulebook instead of the file, and how to build a judge that answers for both codebases.
---

# Large-scale code migration

A method for porting a codebase at a scale where reading every diff is not an option. The
organizing idea: **you do not fix the code, you fix the loop that produced the code.**

Human effort concentrates in the first two steps. Steps 3–6 are queues that burn themselves
down, and your job during them is to watch for patterns rather than to work individual
failures.

## Instructions

### Before anything: build the judge

Do not start translating without a verification mechanism that can be run against both the
original and the port and that answers the same way for both. Categorize the existing tests
into portable and non-portable, rewrite the portable ones into two-sided assertions, then
validate the judge by running it against known-good code (must pass) and deliberately broken
code (must fail). If there is no test suite, have Claude build a parity harness of real
end-to-end scenarios first.

Full procedure: [references/verification-harness.md](references/verification-harness.md).

### Step 1 — Rulebook, dependency map, gap inventory

In that order.

1. **Decide the architecture first.** A structure-preserving port and a redesign produce
   very different rulebooks — lookup tables in the first case, a design document in the
   second. Everything downstream depends on this choice.
2. **Write the rulebook**: type mappings, idiom mappings, error handling, memory and
   concurrency conventions, dependency substitutions, and the rule that an unsure agent
   flags rather than guesses. Start from [templates/rulebook.md](templates/rulebook.md).
3. **Build the dependency map.** This is the parallelization schedule: a file is ready when
   its dependencies are done. Read it from a manifest where one exists; otherwise have Claude
   discover it and record it as machine-readable data. Start from
   [templates/dependency-map.md](templates/dependency-map.md).
4. **Write the gap inventory** — the places the rulebook's defaults will not cover and that
   need refactoring rather than translation. It comes last because a gap is only definable
   against a stated default. Start from [templates/gap-inventory.md](templates/gap-inventory.md).

### Step 2 — Stress-test the rules

Run a mini-migration on a small, representative sample. Use three roles: a translator working
only from the rulebook, a reviewer in a separate context evaluating the output the way a
senior engineer would, and a rule extractor reading the diffs to propose rules the rulebook
is missing.

Then **throw the translated files away.** The output of this step is a better rulebook, not
progress. Keeping the files creates pressure to keep their decisions.

Repeat Steps 1–2 until a sample run yields few new rules. That convergence is the signal to
scale.

### Step 3 — Translate everything

Fan out across the dependency map.

- Keep the queue **mechanical and resumable**: done means the output file exists on disk.
  Queue state lives on disk, never only in an agent's context.
- Run **many implementers on a smaller model**; they are rulebook-constrained and
  high-volume.
- An unsure implementer emits `// TODO(port): <reason>` and moves on. Never guess, never
  invent target APIs, never change behavior to make something compile.
- Put **two adversarial reviewers on a larger model** over each unit of work, in separate
  contexts; escalate disagreement to a third agent.
- When a reviewer catches the same mistake repeatedly, **add a sentence to the rulebook and
  regenerate the batch.** Do not patch file by file.

### Steps 4–6 — Compile, run, match behavior

Same loop shape; only the source of work items changes.

| Step | Queue is fed by | Referee |
| --- | --- | --- |
| 4 — Compile | Build errors | The compiler |
| 5 — Run | Crashes from smoke tests | The smoke test |
| 6 — Match behavior | Differences vs the original | The judge / parity harness |

- **Step 4:** fold into Step 3 if the build is fast; otherwise serialize the build behind an
  orchestrator script and fan fixer agents out over the batched error list. Agents should not
  each invoke the build.
- **Step 5:** categorize crash root causes with adversarial subagents so one systemic cause
  is not filed as ten unrelated bugs.
- **Step 6:** let scripts be the referee — a compiler, a diff, a test suite. An agent judging
  whether two behaviors are "basically the same" puts the judgment you removed back into the
  loop.

Loop mechanics, model selection, and orchestrator patterns:
[references/loop-design.md](references/loop-design.md).
Step-by-step detail: [references/six-step-process.md](references/six-step-process.md).

### Standing rules

- **Fix the process, not the output.** A per-file patch leaves the generator still producing
  the error.
- **Do not use the largest model for everything.** Token spend concentrates in the loops;
  put small models on implementation and large ones on review and delegation.
- **Front-load the human effort.** Steps 1 and 2 are where your time belongs.
- **Watch patterns, not incidents.** Individual failures are the fixer agents' job.
- **Adapt the plan.** Every migration differs; plan yours with Claude before committing.

## Examples

### Deciding what shape the rulebook takes

> "We're moving our Python service to Go. Where do I start?"

Ask the architectural question before writing anything: is this the same service in a new
language, or a redesign? If it is structure-preserving, the rulebook is lookup tables and
the migration is mostly mechanical. If the goal is also to restructure, the rulebook is a
design document and the gap inventory will be long. Answering this wrong makes every later
step ambiguous.

### A reviewer keeps flagging the same thing

> "The reviewer has caught the same nullable-handling mistake in 40 files."

Do not fix 40 files. Add the rule to the rulebook — one sentence stating how the source's
nullable type maps and what to do at the boundary — log it in the rulebook changelog, then
regenerate the affected batch. This is why cheap batch regeneration is a design requirement:
you will do it every time a rule changes.

### An agent is unsure about a construct

> A translator hits a macro with no target equivalent.

It writes `// TODO(port): source macro expands at build time; no target equivalent chosen`
and moves on. The marker becomes a work item for a later step and, if the same marker appears
across many files, a gap-inventory entry with a single decision rather than dozens of
improvised ones.

### Scoping the effort

Two migrations reported in the source post — Bun from Zig to Rust (about a million lines in
under two weeks, 100% of the existing suite green before merge, 19 regressions after) and a
Python-to-TypeScript port (165,000 lines over a weekend, twelve parallel Sonnet subagents,
seven parity scenarios). Details and cost figures:
[examples/case-studies.md](examples/case-studies.md).

Use them for calibration, not as a promise. Zero regressions is not the target; findable and
cheap regressions are.
