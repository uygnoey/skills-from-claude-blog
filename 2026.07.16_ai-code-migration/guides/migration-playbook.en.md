**English** · [한국어](./migration-playbook.ko.md) · [Español](./migration-playbook.es.md) · [日本語](./migration-playbook.ja.md)

# Playbook: running a large-scale migration with agents

A migration is large when reading every diff stops being possible. Past that point the work
is no longer writing code — it is designing the loops that write the code, and then watching
what those loops produce in aggregate.

The source post states the principle plainly: you do not fix the code, you fix the process
that produced the code. Everything below is a consequence of that.

## Why this changes the shape of the work

The traditional failure mode of a big rewrite is that it never finishes: a small team ports
by hand, the original keeps moving, and the port is permanently behind. Agent fan-out removes
the throughput limit — the Bun port reported in the post produced roughly a million lines of
Rust in under two weeks — but it replaces it with a different problem. When a thousand files
are translated by agents, a single wrong assumption is not one bug. It is a thousand
instances of one bug, all of which look reasonable in isolation.

So the leverage moves. Careful per-file work buys you almost nothing at this scale. What buys
you everything is a rulebook that is right, a queue that survives interruption, and a referee
that is not an opinion.

## The prerequisite: a referee

Before the first file is translated, you need something that can be run against the original
and against the port and that answers the same way for both. Categorize the existing tests
into those expressible through the public surface and those bound to internals; port the
first group into assertions that run against both sides; discard the second, because what it
asserted on will not exist after the migration.

Then validate the judge itself, in both directions. Run it against the original — it must
pass. Run it against deliberately broken code — it must fail. A judge that has only been
checked in one direction is how a migration ends with a green board and a broken product.

If the project has no usable test suite, build a parity harness of real end-to-end scenarios
instead. The Python-to-TypeScript port in the post used seven, treating any behavior
difference as a bug rather than something to explain. Seven scenarios that genuinely exercise
the system beat hundreds of shallow tests that only prove the port compiles.

## Phase one: decide, then write it down

Three documents, in a fixed order.

The **rulebook** is the translation policy — everything an implementer needs in order to port
a file without asking a human. Its shape is determined by a decision you have to make first:
is this the same architecture in a new language, or a redesign? A structure-preserving port
yields a rulebook that is mostly lookup tables — types, idioms, error handling, concurrency,
dependency substitutions. A redesign yields something closer to a design document, because
there is nothing to look up. Teams that skip this decision write a rulebook that is ambiguous
in exactly the places that matter most.

The **dependency map** is the schedule. A file can be translated when everything it depends
on is done, so the map determines what can run in parallel. Where the ecosystem publishes a
module graph, read it. Where it does not — legacy code, C/C++, Python — have Claude discover
the dependencies and record the result as machine-readable data your queue can consume, not
as prose. Record the cycles explicitly; they will not resolve themselves.

The **gap inventory** comes last, and the ordering is not a style preference. A gap is a place
the rulebook's defaults do not reach, which means it is only definable once the defaults
exist. Written first, it becomes a list of anxieties instead of a list of decisions.

## Phase two: try to break it

Run a mini-migration on a small representative sample — the post calls it a shakedown cruise.
Three roles: a translator working only from the rulebook, a reviewer in a separate context
evaluating the result the way a senior engineer would, and a rule extractor reading the diffs
to propose the rules the rulebook was missing.

Then delete the translated files.

That instruction is the one people resist, and it is the one that matters. The output of this
phase is a better rulebook, not progress. Keeping the files creates pressure to keep the
decisions embedded in them, which is precisely the pressure the phase exists to remove.
Repeat until a sample run produces few new rules; that convergence is your signal to scale.

Phases one and two are where the human time goes. Everything after is queues burning down.

## Phase three onward: four loops with one shape

Translate, compile, run, match behavior. They differ only in what feeds the queue: files from
the dependency map, then build errors, then crashes, then differences against the original.
The to-do lists write themselves — a compiler error is the next work item, a `// TODO(port)`
marker left by a translator is the next work item.

Three design choices carry these loops.

**Done must be mechanical.** The post's formulation is that done means the output file exists
on disk. Long migrations get interrupted — rate limits, restarts, a batch you decide to throw
away — and a queue whose completion test requires judgment cannot resume. Keep queue state on
disk, never only in an agent's context, and make regenerating a batch an ordinary cheap
operation, because you will do it every time a rule changes.

**Uncertainty is flagged, never guessed.** An implementer that is unsure emits
`// TODO(port): <reason>` and moves on. This is the difference between a visible queue item
and an invisible correctness risk. The reason string matters more than it looks: it is what
lets a later pass cluster fifty markers into one decision instead of fifty improvisations.

**Review is adversarial.** Two reviewers per unit of work, in separate contexts so they
cannot anchor on each other, with disagreement escalating to a third agent. The post notes
this is often worth the token consumption, and the reason is structural: a single reviewer
converges on the implementer's framing, and a systemic error reviewed in that frame is
approved a thousand times in a row.

## The move that defines the method

When a reviewer catches the same mistake across many files, do not fix the files. Add one
sentence to the rulebook and regenerate the affected batch.

A per-file patch leaves the generator still producing the error, so you will pay for it again
in the next batch and the batch after that. A rulebook change stops the error at the source
and repairs everything it already touched. This is why cheap batch regeneration was listed as
a design requirement rather than a convenience.

The same logic applies to your attention. Individual failures are what the fixer agents are
for. Your job during the burn-down phases is to notice which categories of failure keep
recurring and what single change makes a whole category disappear.

## Spending deliberately

Token spend concentrates in the loops, so the loops are where model choice actually matters.
Implementers are high-volume and rulebook-constrained, and belong on a smaller model — the
post reports twelve parallel Sonnet subagents on the Python-to-TypeScript port. Reviewers,
adjudicators, and delegators are lower-volume and judgment-heavy, and belong on a larger one.
Using the largest model everywhere spends most of your budget on the role that needs it
least.

The Bun migration's reported figures give a sense of scale: 5.9 billion input tokens and 690
million output tokens, roughly $165,000 at API pricing, for a million-line port that shipped
19% smaller binaries and 2–5% faster real-world performance. That cost is predictable in
advance if you know where your tokens concentrate.

Also serialize what does not parallelize. A whole-workspace compile belongs behind an
orchestrator script that runs the build once and batches the errors for fixers to fan out
over. Agents that each invoke the build spend the parallelism you designed for.

## What success looks like

Bun merged with 100% of its existing test suite passing and 19 regressions afterward, all
fixed. That is the realistic shape of a successful migration at this scale. The question a
migration has to answer is not whether regressions exist but whether they are findable and
cheap — which is another way of saying that the referee you built in the prerequisite step is
the thing that determines whether any of this works.

## Adapting it

The post is explicit that every migration is different and that this is a starting point
rather than a recipe. Plan yours with Claude before committing to it — especially the
architectural decision in phase one, which determines whether your rulebook is a set of
tables or a design document, and therefore determines the shape of everything that follows.

## Source

[How Anthropic Runs Large-Scale Code Migrations with Claude Code](https://claude.com/blog/ai-code-migration) — published 2026-07-16.
