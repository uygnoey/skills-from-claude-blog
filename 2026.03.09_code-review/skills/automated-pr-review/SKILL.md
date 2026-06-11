---
name: automated-pr-review
description: Dispatch a multi-pass, high-signal pull request review and deliver a consolidated overview plus actionable inline findings.
---

## Purpose
Provide a consistent, thorough PR review workflow (optimized for depth, not speed) that scales its effort to the size and complexity of the change.

## When to use
- You want deeper review coverage than quick scans.
- You want repeatable review output on every PR.
- You want a single overview comment plus inline notes, while keeping final approval to a human.

## Instructions
1. **Read the PR context**
   - Identify the change intent (what problem it solves).
   - Identify the risk surface: auth, data integrity, migrations, concurrency, security boundaries, config changes.
2. **Scale review depth to change size**
   - Small changes: prioritize correctness, edge cases, and obvious regressions.
   - Large/complex changes: do a deeper pass across architecture, invariants, and adjacent modules.
3. **Review for high-signal issues**
   - Correctness and logic bugs
   - Security and permissions
   - Reliability (timeouts, retries, idempotency)
   - Performance pitfalls
   - Observability (logs/metrics/tracing)
   - Tests and coverage gaps
   - Developer experience (clarity, maintainability)
4. **Write results in two layers**
   - **Overview comment**: a concise summary of main findings and risk areas.
   - **Inline findings**: specific, actionable notes tied to exact locations.
5. **Do not approve the PR**
   - Provide guidance; a human still decides whether to merge.

## Output format
### Overview
- Intent:
- Top risks:
- Findings (highest impact first):
- Suggested follow-ups (tests, docs, rollout):

### Inline findings
For each finding:
- Location:
- Issue:
- Why it matters:
- Suggested fix:

## Examples
See [examples/review-comment-template.md](./examples/review-comment-template.md) for a ready-to-copy PR review comment template.

## Source
- https://claude.com/blog/code-review
