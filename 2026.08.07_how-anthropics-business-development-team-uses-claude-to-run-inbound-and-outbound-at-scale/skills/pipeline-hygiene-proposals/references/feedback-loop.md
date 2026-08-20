# The rejection feedback loop

From the post: "When I edit or reject a proposal, it records the reason why so it
doesn't repeat the mistake." And, in the closing advice: "Write feedback back
into the skills. When you dismiss a hook or correct a draft, have Claude record
the reason in the skill so it doesn't make the same mistake again."

This reference is about what that loop needs in order to actually work.

## Why an unexplained rejection is expensive

A rejected proposal with no recorded reason costs three times:

1. the rep's attention now,
2. the same proposal appearing again next run,
3. the rep's trust in the queue, which is what makes them stop reading it.

The third is the one that kills the skill.

## What a useful reason looks like

| Weak | Useful |
| --- | --- |
| "Not yet" | "Pricing came up once in passing; the economic buyer has not engaged" |
| "Wrong" | "That call was with a different business unit" |
| "No" | "The customer asked for pricing to close out the conversation, not to progress" |

The useful column names the *distinguishing feature* — something the skill could
have checked. That is what makes it reusable.

## Where the reason goes

Recorded back into the skill, so the next run applies it. In practice that means
the skill accumulates a set of learned distinctions alongside the stage guidance
it reads.

Keep the two separate:

- **Stage guidance** — the team's standard, owned by the team, edited
  deliberately.
- **Recorded corrections** — accumulated from real rejections, appended as they
  happen.

## The escalation signal

When the same reason is recorded repeatedly, and especially across multiple
reps, the problem is not the skill's judgment. The stage guidance is ambiguous.
Rewrite the rule; then the accumulated corrections for it can be retired.

## Keep it general

The post advises keeping shared skills "general enough to adapt rather than
scoped to one person's routine." Corrections are where a shared skill quietly
becomes one person's: a distinction that is true for one rep's segment can be
wrong for another's. Record what segment or context a correction came from, so a
learned rule can stay scoped to where it holds.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)
