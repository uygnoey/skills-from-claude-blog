# Template — scoping a narrow PR review agent

Multiple narrow reviewers beat one broad one: they do not share biases and
blindspots, one can catch another's mistake or compromise, and effort is not spread
thinly. Fill one of these out per reviewer, and resist widening the scope later —
add another reviewer instead.

```markdown
# Reviewer: [name]

## Single focus
[One vulnerability class or one property. If this sentence needs an "and", split
the agent in two.]

## Explicitly out of scope
[The neighbouring classes another reviewer owns. Say them by name so this agent does
not drift into them.]

## Retrieval context
- Past incidents relating to [focus]
- Org policy: [which documents]
- Codebase areas: [which paths, and their risk tier]

## Proof obligation
Before posting a finding, write out:
1. The entry point for attacker-controllable input.
2. The path from that entry point to the vulnerable code.
3. What an attacker gains.
4. Why existing controls in this path do not prevent it.
A finding without all four is not posted.

## Output
- Post as a PR comment. [Shadow mode: comment only, never block, until trust is
  earned.]
- Log the finding, the signals used, and the reasoning to the SIEM.

## Risk tier behaviour
- Tier [x]: may [comment only / approve].
- Approvals are sampled at [rate] for human re-review.
```

## Notes

- **Shadow mode is the default for a new reviewer.** It posts comments for human
  approval until it has earned trust, and it should be red teamed with deliberately
  malicious changes before it graduates.
- **Separate context windows are part of the control**, not an implementation
  detail. Two reviewers sharing a context share a blindspot.
- **The proof obligation is what moved the numbers.** Requiring agents to prove a
  finding is valid is what raised confidence enough for substantive review comments
  to go from 16% to 54% of PRs.
