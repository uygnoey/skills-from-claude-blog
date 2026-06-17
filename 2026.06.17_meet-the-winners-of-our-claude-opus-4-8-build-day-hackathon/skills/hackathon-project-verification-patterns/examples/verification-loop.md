# Verification loop with independent reviewers

This example is a generalized version of the pattern described for Tekton in the post.

## Goal

Iteratively verify a generated artifact (e.g., a 3D reconstruction, a structured report, or a dataset transformation) until a fixed test suite passes.

## Steps

1. Generate a first draft artifact.
2. Run multiple independent verifier sub-agents. Each verifier receives only the artifact + the relevant source snippets needed to judge correctness.
3. Collect a verdict per test case (pass/fail + rationale + citation to source snippet).
4. For any failures, revise only the failing components.
5. Repeat verification until all tests pass.

## Notes

- Keep each verifier isolated (fresh context) to reduce anchoring on earlier mistakes.
- Prefer small, targeted revisions over full rewrites to preserve what already passed.

## Source

- https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon
