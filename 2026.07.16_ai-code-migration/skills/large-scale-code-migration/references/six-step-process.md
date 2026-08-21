# The six-step migration process

The source post describes a migration as six phases. The first two are where human
judgment concentrates; the last four are queues that burn themselves down.

---

## Step 1 — Rulebook, dependency map, gap inventory

Three artifacts, produced in this order.

### Rulebook

The translation policy: how a construct in the source language or framework becomes a
construct in the target. Its shape depends on the architectural decision you have already
made:

- **Structure-preserving port** (same architecture, new language) — the rulebook is mostly
  lookup tables: type mappings, idiom mappings, error-handling conventions, memory and
  concurrency conventions, naming and file-layout conventions.
- **Redesign** (new architecture) — the rulebook is closer to a design document, because
  there is no one-to-one correspondence to look up.

Decide which of the two you are doing before writing a line of the rulebook. See the rulebook template bundled with this skill.

### Dependency map

Which files depend on which. This is what makes parallel translation possible: files with
no unresolved dependencies can go out to agents simultaneously.

Some ecosystems hand you this from an explicit manifest. For legacy codebases and for
languages such as C/C++ and Python, the post notes that dependencies have to be discovered
and mapped rather than read off a manifest. Have Claude do the discovery pass and record the
result as data your queue runner can consume. See the dependency-map template bundled with this skill.

### Gap inventory

The list of places where the rulebook's defaults do not apply — architectural differences
that need refactoring rather than translation.

Ordering matters here. The post is explicit that the rulebook comes first, because the gap
inventory is *defined by* what the rulebook's defaults will not cover. Writing the gap
inventory first produces a list of anxieties instead of a list of gaps. See
the gap-inventory template bundled with this skill.

---

## Step 2 — Stress-test the rules

A mini-migration over a small, representative set of files. The post calls it a shakedown
cruise: the point is to break the rulebook while the cost of being wrong is still a few
files rather than the whole codebase.

Run three roles against the sample:

1. **Translator** — ports the files using only the rulebook.
2. **Reviewer** — evaluates the output the way a senior engineer would, in a separate
   context from the translator.
3. **Rule extractor** — reads the diffs and proposes new rules for cases the rulebook did
   not anticipate.

Then throw the translated files away. The output of Step 2 is a better rulebook, not
progress on the migration. Keeping the files creates pressure to keep their decisions, which
is exactly the pressure the step exists to remove.

Iterate Steps 1–2 until a sample run produces few new rules. That convergence is the signal
to scale up.

---

## Step 3 — Translate everything

Fan out across the dependency map.

- **Queue** — mechanical and resumable. The post's definition of done for a queue item is
  that the output file exists on disk. A queue that requires judgment to determine whether an
  item is finished cannot be resumed after an interruption, and every long migration is
  interrupted.
- **Implementers** — many parallel agents, each translating files against the rulebook. This
  is the high-volume role, and the post's guidance is to run it on a smaller model.
- **Uncertainty handling** — an agent that is not confident does not guess. It emits a
  `// TODO(port): <reason>` marker and moves on. Those markers become work items for later
  steps.
- **Reviewers** — two adversarial reviewers per unit of work, each in its own context.
  Disagreement between them escalates to a third agent. Reviewers run on a larger model.
- **Rule refinement** — when a reviewer catches the same mistake repeatedly, the fix is not
  per-file. Add a sentence to the rulebook and regenerate the affected batch.

That last point is the whole method in miniature: you do not fix the code, you fix the loop
that produced the code.

---

## Step 4 — Compile

Whether this is its own step or folds into Step 3 depends on how fast your build is. A fast
compiler can run inside the translation loop; a slow one is better serialized behind an
orchestrator script that invokes the build across the workspace and batches the resulting
errors.

The loop: build → collect errors → fan out fixer agents over the error list in parallel →
adversarial review of the fixes → build again.

## Step 5 — Run

Smoke tests. Crashes become the queue. Categorize root causes rather than treating each
crash as a separate incident, and put adversarial subagents on the categorization so a
systemic cause is not filed as ten unrelated bugs.

## Step 6 — Match behavior

Run the port against the original and drive the differences to zero. Scripts are the referee
here — a compiler, a diff, a test suite — not an agent's opinion about whether the behavior
looks equivalent. See [verification-harness.md](verification-harness.md).

If the project has no test suite, have Claude construct the scenarios first. That work is a
prerequisite, not an optional extra: without a referee there is no definition of finished.

---

## Where the human effort goes

Steps 1 and 2 are the expensive ones in human time. Everything after is mostly queues
burning down, and your attention belongs on patterns rather than on individual failures —
individual failures are what the fixer agents are for.
