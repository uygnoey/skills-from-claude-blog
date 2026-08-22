# The four verification layers

Temper's deterministic kernel verifies an agent-emitted specification through four
independent layers before any of it runs. Independence is the point: each layer
catches a class of defect the others structurally cannot.

The article describes the four layers as follows.

## 1. Symbolic reasoning

Proves that **each guard is satisfiable** and that **each invariant is inductive**.

- *Guard satisfiable* — there exists some state in which the transition's
  precondition can actually hold. An unsatisfiable guard is dead logic: a
  transition that can never fire, usually a sign the spec says something other
  than what the author meant.
- *Invariant inductive* — the invariant holds in the initial state, and every
  transition preserves it. Induction is what makes the property hold for all
  executions rather than for the executions someone thought to test.

What it does not cover: this layer reasons about the spec, not about the
production code that implements it.

## 2. Exhaustive state exploration

**Visits every reachable state.**

Where symbolic reasoning argues about states in the abstract, this layer
enumerates them. It answers "can the system ever actually get here?" — deadlocks,
unreachable states, and states nobody modelled show up as concrete traces rather
than as proof failures.

What it does not cover: the real code paths and the timing and fault behavior of
the running system.

## 3. Deterministic simulation

**Runs production code paths with seeded fault injection.**

This is the layer that connects spec to implementation. Real code executes, but
under a deterministic scheduler with injected faults chosen by seed. Determinism
is what makes it useful in an agentic loop: a failure is reproducible from its
seed, so an agent can be handed the exact failing execution rather than a
description of one.

What it does not cover: sequences nobody chose to simulate.

## 4. Randomized property testing

**Executes roughly 1,000 pseudorandom action sequences.**

The breadth layer. Where the previous three are directed, this one goes looking
in the parts of the space nobody aimed at, checking that the declared properties
survive orderings and interleavings no author had in mind.

## Why four and not one

Each layer's blind spot is another layer's subject:

| Layer | Argues about | Blind to |
| --- | --- | --- |
| Symbolic reasoning | The spec, for all executions | The implementation |
| Exhaustive state exploration | Every reachable state | Real code paths, faults |
| Deterministic simulation | Production code under seeded faults | Unexplored sequences |
| Randomized property testing | Unaimed-at sequences | Exhaustive guarantees |

A spec passing all four has been argued about abstractly, enumerated concretely,
executed for real under fault, and stress-ordered. That combination is what
allows the artifact to reach the running system without a human reading it line
by line — the condition for verification to stop being the bottleneck.

## Source

[How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code) — Michael Segner, July 21, 2026
