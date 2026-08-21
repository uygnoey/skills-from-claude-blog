# REVIEW.md scaffold

The tech lead writes the review policy as `REVIEW.md` at the repo root, divided into the passes
the organization cares about. Every PR then gets an identical set of passes with findings ranked
by severity, and human attention moves up a level: does the change do what the plan intended, and
is the risk acceptable?

```markdown
# Review instructions

## Passes
Run three passes and tag each finding with its pass:
- Bugs: logic errors, broken edge cases, subtle regressions
- Security: injection risks, authentication gaps, PII in logs
- Compliance: the change matches spec.md, plan.md and our design principles

## What Important means here
Reserve Important for findings that would break behavior, leak data
or breach a policy. Style and naming are nits.

## Cap the nits
Report at most five nits per review; summarize the rest as a count.

## Do not report
Generated files under src/gen/ and anything CI already enforces.
```

**How it is operated**

- **Findings do not approve or block on their own.** Branch protection still requires approval
  from a code owner. A platform engineer who wants to gate merges on findings reads the severity
  counts the check run publishes as a machine-readable tally.
- **The fix loop.** When a reviewer or the author tags `@claude` on a review comment, Claude
  addresses the comment and pushes the fix; the PR thread records both the request and the change.
  For PRs Claude opened, teams wrap the loop in a custom command that sweeps unresolved comments
  and failing checks, addresses them, and pushes fixes until the PR is green and waiting only on
  code owner approval.
- **Findings feed back into `CLAUDE.md`.** When a review flags the same mistake a second time, the
  correction goes into `CLAUDE.md` as part of that review — and because review reads `CLAUDE.md`,
  the mistake is caught from the next PR onwards. Review also flags when a change has made
  `CLAUDE.md` outdated.
- **Monthly tuning.** The tech lead rates findings so the reviewer improves, caps nit volume here,
  and excludes generated paths and anything CI already enforces.

**Separation of duties holds.** The agent that wrote the code has no way to approve it. Findings,
fixes, ratings, and approvals are logged in the PR history, so the PR is the audit record.
