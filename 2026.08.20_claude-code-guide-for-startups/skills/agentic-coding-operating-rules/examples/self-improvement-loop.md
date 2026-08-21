# Worked example: a correction loop that fixes the principle, not the example

Cainex combines agents with deterministic checks to read medical records and
generate the codes that direct hospital billing. Uriah Israel, co-founder and
CTO, frames the constraint that governs the whole design:

> "In medical coding, a wrong code isn't a typo. It's a billing and compliance
> event. That one fact governs how we build."

The loop below is domain-specific, but the shape generalizes to any
high-stakes agent whose output experts review.

## The loop

**1. Batch processing.** An agent processes a batch of records.

**2. Expert review with reasoning visible.** Auditors review the output in an
internal app. They do not just see the codes — they see the model's reasoning,
and they comment on both. Everything is versioned and auditable.

**3. Claude Code reads the corrections, not just the outcomes.** It reads the
original predictions along with every correction and comment, straight from the
database. Each correction is tagged by the kind of code involved, so Claude Code
knows whether it is looking at a diagnosis issue, a procedure issue, or another
category, and can go straight to the guidance that governs that specific kind of
coding.

**4. Revise the instruction that produced the mistake.** From there it finds the
part of the agent's instructions that produced the mistake and revises it, or
writes new guidance when the case is genuinely new. Every change is made against
a versioned set of instructions and tested against the records that failed.

> The rule we enforce: fix the principle, not the example.

**5. Back-test before shipping.** A record can have more than one acceptable
coding, so this is not a string match. The check combines semantic matching
against accepted sets with a judge that asks, "Is this a real error or just a
different valid path," and Claude Code adds its own comparisons on top. It runs
the candidate change across a golden set plus random samples and surfaces any
regressions before anything ships.

**6. Hand back a short list.** What comes back is: suggested edits, the records
it couldn't resolve, and the questions it wants answered. Engineers spend their
time on genuinely hard cases rather than the mechanical 80%.

## Generalizable takeaways

- **Route expert guidance into the loop, not into individual fixes.** Subject
  matter experts routinely review and guide the agent's reasoning, and that
  guidance becomes part of a self-improvement loop. They are not there to fix
  example by example.
- **Guard against overfitting explicitly.** "It didn't start this clean. Our
  first version overfitted. It would 'fix' things by encoding the specific case,
  and we were accumulating patches instead of getting smarter. We changed the
  approach to force general principles and to cap how many specifics can enter a
  change at all."
- **Judge, don't string-match.** When more than one output is legitimately
  correct, the back-test needs semantic comparison plus a judge that distinguishes
  a real error from a different valid path.
- **Version everything.** Instructions, corrections, and the records a change was
  tested against.

## Where loops fit generally

Loops are agents that repeat cycles of work until a stop condition is met, and
they are an effective way to use Claude Code for autonomous or long-horizon work.
Use skills to define the criteria the agent needs to meet — the more clearly
defined, the better — and let the agent iterate until it reaches its goal.

Flaky-test agents are the standard first loop precisely because the stop
condition is clear and self-contained: the agent can verify its own fix by
rerunning the test until it passes.

## Source

[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups) (published 2026-08-20).
