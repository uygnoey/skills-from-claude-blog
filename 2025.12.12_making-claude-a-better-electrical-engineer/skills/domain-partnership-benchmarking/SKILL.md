---
name: domain-partnership-benchmarking
description: Create a domain-expert partnership plan to benchmark and improve model performance on specialized agentic tasks.
---

# Making Claude a better electrical engineer (skill)

## Purpose
This skill converts the blog post's ideas into a reusable checklist for either (a) domain-expert partnership benchmarking, or (b) plan-fit assessment, depending on the post.

## Instructions
Use this skill when you need to improve model performance on a specialized, tool-using workflow by partnering with domain experts.

1. Define the target agentic task as an input → output transformation.
2. Build an evaluation harness (testbench) that can grade outputs in domain terms.
3. Prefer requirement-based checks over brittle exact component matches.
4. Collect expert feedback to identify common failure modes and update the benchmark.
5. Run blinded comparisons against baseline models to validate improvements.

When documenting the harness, keep the high-level requirements in the harness and reserve detailed rationale for references.

See: [references/benchmark-notes.md](./references/benchmark-notes.md).

## Examples
- **Goal**: Improve a model that generates reference designs from chip documentation.
  - **Harness requirement**: 'At least 22uF of capacitance between power and ground.'
  - **Evaluation**: Run the testbench and compare outputs across candidate models.

## Source
- https://claude.com/blog/making-claude-a-better-electrical-engineer
