---
name: skill-evals-maintenance-playbook
description: Maintain Agent Skills over time by defining evals, running benchmarks, comparing variants, and tightening skill descriptions to reduce false triggers.
---

## Instructions

Use this skill when you are authoring or maintaining Agent Skills and want a repeatable process to verify quality, detect regressions, and decide what to improve.

### 1) Classify the skill you’re maintaining

Use the post’s two categories to set expectations for what “success” means:

- **Capability uplift**: the skill teaches techniques the base model can’t do reliably.
- **Encoded preference**: the skill sequences steps according to your team’s process.

See [references/skill-types.md](./references/skill-types.md).

### 2) Define evals (tests)

For each eval, capture:

- A **test prompt** (and any files needed)
- A description of **what good looks like**

Run evals to confirm the skill works as intended.

### 3) Use evals to catch regressions

- Re-run evals after model changes or significant edits.
- Treat drops in pass rate (or qualitative degradation) as an early signal of regressions.

### 4) Use evals to detect model progress

If the base model starts passing your evals **without** the skill loaded, the skill may be less necessary (especially for capability uplift skills).

### 5) Run benchmark mode to track tradeoffs

When available, run a standardized benchmark using your eval set, and track:

- Eval pass rate
- Elapsed time
- Token usage

### 6) Speed and consistency: multi-agent evaluation

When supported, run evals in parallel using independent agents so each run has:

- A clean context (no cross-contamination)
- Its own token and timing metrics

### 7) Compare variants with comparator agents

Use blinded comparisons to decide whether changes help:

- Skill vs. no skill
- Skill version A vs. skill version B

### 8) Tune the skill description for reliable triggering

If your eval quality is strong but triggering is unreliable:

- Tighten overly broad descriptions to reduce **false positives**.
- Expand overly narrow descriptions to reduce **false negatives**.

## Examples

- A lightweight eval plan template: [examples/eval-plan-template.md](./examples/eval-plan-template.md)

## References

- Post: https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
