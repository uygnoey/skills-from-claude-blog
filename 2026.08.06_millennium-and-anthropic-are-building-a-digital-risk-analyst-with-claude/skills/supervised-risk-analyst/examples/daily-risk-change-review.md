# Example: reviewing a daily risk change

The post describes an analyst that "retains and recalls information over time,
applying new reasoning capabilities to help explain daily risk changes," whose
findings "are then validated and enriched by Millennium's human risk managers."
This is that loop written out as a worked example. The mechanics are illustrative
— the post does not publish the analyst's internal workflow — but each step maps
to a property the post does state.

## Cycle N-1: what gets recorded

At the end of a cycle the analyst writes down, per position or exposure it
covers:

- the level it observed,
- the drivers it attributed the level to,
- the reasoning that connected the two,
- anything a risk manager corrected or added during review.

This record is the thing that makes the next cycle an explanation rather than a
restatement.

## Cycle N, step 1: recall before reading

The analyst recalls its own record for the same exposures before it looks at
today's data. It now holds a prior: what it believed yesterday and why, plus
whatever the risk manager enriched it with.

## Cycle N, step 2: form the delta

Against today's proprietary data, the analyst produces, for each material move:

> **Exposure:** _[what moved]_
> **Change:** _[from → to]_
> **Candidate explanation:** _[what it attributes the move to]_
> **Evidence:** _[the inputs behind the attribution]_
> **Reasoning:** _[the chain from evidence to explanation, logged]_
> **Confidence and what would change it:** _[what it would need to see]_

Note the shape: it forms an *opinion* on exposure, which is what the post says
the analyst does, and it attaches the reasoning, which is what makes the opinion
auditable.

## Cycle N, step 3: human validation and enrichment

The risk manager reads the reasoning, not just the conclusion. Three outcomes:

- **Validated** — the explanation holds; it stands as the account of the move.
- **Enriched** — the explanation is right as far as it goes, and the manager adds
  firm-specific context the analyst could not see. The addition is written back.
- **Rejected** — the reasoning is wrong. The correction, and the reason, are
  written back so the next cycle starts from the corrected view.

Human judgment stays at the center: the manager's version is the one that
counts.

## Cycle N, step 4: close the loop

Whatever survives review becomes cycle N's record, and the input to cycle N+1.
Over time the analyst is explaining changes against an account of the book that
its supervisors have already corrected — which is the point of the memory.

## What does not happen here

- No action taken against live positions from this loop; actions are exercised
  in sandboxed environments first.
- No decision counts before a human expert has evaluated and approved it.

## Source

- https://claude.com/blog/millennium-and-anthropic-are-building-a-digital-risk-analyst-with-claude (August 6, 2026)
