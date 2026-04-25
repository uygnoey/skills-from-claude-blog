**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?

This post announces updates to “skill-creator” that help authors test, benchmark, and refine Agent Skills so they keep working as models evolve.

## When is it useful?

Use this when you maintain skills over time and need a lightweight way to detect regressions, measure improvements, compare variants, and tighten skill descriptions so they trigger reliably.

## Key points

- The post distinguishes two categories of skills: “capability uplift” skills and “encoded preference” skills.
- Skill-creator now supports writing evals (tests) by defining test prompts (and files if needed) plus describing what good looks like.
- Evals help catch regressions when models change and help detect when the base model has outgrown a capability-uplift skill.
- Benchmark mode runs standardized assessments and tracks eval pass rate, elapsed time, and token usage.
- Multi-agent support runs evals in parallel with clean contexts and independent token/timing metrics.
- Comparator agents can run blinded A/B comparisons (skill vs. no skill, or two skill versions).
- Skill-creator can suggest description edits to reduce false positives and false negatives for triggering.

## Bundled resources

- Skill: a practical playbook for maintaining Agent Skills with evals, benchmarks, and description tuning.
- Reference: definitions of “capability uplift” vs “encoded preference”.

## Source

- https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
