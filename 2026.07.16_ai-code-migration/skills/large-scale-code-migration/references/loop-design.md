# Designing the loops

The post's central claim is that you do not fix the code — you fix the process that produced
the code. Everything below follows from taking that seriously.

## What every loop needs

A migration loop is a work queue plus a set of roles. Steps 3, 4, 5 and 6 are all the same
shape; only the source of work items changes.

| Step | Work items come from |
| --- | --- |
| 3 — Translate | Files in the dependency map |
| 4 — Compile | Build errors |
| 5 — Run | Crashes from smoke tests |
| 6 — Match behavior | Differences between the port and the original |

The queues write themselves. A `// TODO(port)` marker left by a translator, a compiler
error, a failed assertion — each becomes the next item for an agent to pick up. You are not
maintaining a to-do list by hand.

## Make "done" mechanical and resumable

Long migrations get interrupted: rate limits, machine restarts, a bad batch you decide to
throw away. A queue survives interruption only if the completion test requires no judgment.
The post's formulation is that done should mean the output file exists on disk.

Consequences worth designing for:

- Queue state lives on disk, not in an agent's context.
- Re-running the runner after a crash resumes rather than restarts.
- Regenerating a batch is a cheap, ordinary operation — because you will do it every time
  the rulebook changes.

## Do not guess — flag

An implementer that is not confident should not produce a plausible-looking translation. It
should emit:

```
// TODO(port): <reason this could not be translated confidently>
```

and move on. This converts an invisible correctness risk into a visible queue item. The
reason string matters: it is what lets a later pass cluster the markers into categories
rather than working them one at a time.

## Adversarial review

Single-reviewer setups converge on the implementer's framing. The post's arrangement:

- Two reviewers evaluate each unit of work, **in separate contexts** so they cannot
  anchor on each other.
- Disagreement escalates to a third agent that adjudicates.

The post notes this allows longer-running tasks and is often worth the token consumption. It
is a deliberate trade: you spend tokens to avoid the failure mode where a systemic error is
reviewed as acceptable a thousand times in a row.

## Fix the rule, not the file

When a reviewer catches the same mistake across multiple files, resist the per-file patch.
Add one sentence to the rulebook and regenerate the affected batch. A per-file fix leaves the
generator still producing the error; a rulebook fix stops it at the source and repairs
everything the error already touched.

This is why cheap batch regeneration is a design requirement rather than a nice-to-have.

## Model selection

Token spend concentrates in the loops, so decide deliberately where each model runs rather
than defaulting to the largest one everywhere:

- **Implementers** — high volume, narrow task, rulebook-constrained. Smaller model.
- **Reviewers, adjudicators, delegators** — judgment-heavy, lower volume. Larger model.

The post reports Sonnet used for parallel implementer subagents, with the larger models
reserved for delegation and verification.

## Orchestrator scripts

Some operations are expensive and do not parallelize well — a whole-workspace compile, for
instance. Put those behind an orchestrator script that serializes the expensive operation and
then fans agents out over the resulting error list. Agents should not each be invoking the
build.

## Where your attention belongs

Individual failures are the loop's job; fixer agents burn those down. Your attention belongs
on the patterns — which categories of failure keep recurring, and what rulebook change makes
a whole category disappear.
