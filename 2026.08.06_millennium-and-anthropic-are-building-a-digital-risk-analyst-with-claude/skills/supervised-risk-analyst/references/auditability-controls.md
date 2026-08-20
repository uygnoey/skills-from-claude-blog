# Auditability controls

The post states that Millennium's digital risk analyst "provides secure,
auditable analysis by logging its reasoning, testing its actions in sandboxed
environments, and requiring human experts to evaluate and approve its
decisions." Those three sentences are the whole control set named in the
source. Everything below is that set written out as requirements you can check
a build against — the wording of the obligations is derived from the post, the
implementation details are left open because the post does not specify them.

## 1. Log the reasoning

**Requirement.** Every finding the analyst produces carries the reasoning that
led to it, recorded at the time it was produced.

Check for:

- A record per finding that links the conclusion to the inputs it came from.
- The record surviving the session — it is written down, not just displayed.
- A reviewer being able to answer "why did it say this?" without re-running the
  analysis.

Failure mode this prevents: a conclusion that cannot be defended after the fact,
which in a risk function means a conclusion that cannot be used.

## 2. Test actions in sandboxed environments

**Requirement.** The analyst's actions are exercised in an environment where
they cannot affect real positions or production systems.

Check for:

- A sandbox that mirrors the real environment closely enough that a passing test
  means something.
- Actions running there first, as the default path — not as an optional
  pre-flight someone can skip under time pressure.
- A clear boundary between what the analyst may do in the sandbox and what may
  ever leave it.

Failure mode this prevents: an untested action reaching live positions.

## 3. Require human expert evaluation and approval

**Requirement.** Decisions are evaluated and approved by human experts before
they count.

Check for:

- The approver being a domain expert, not a generic reviewer.
- Approval preceding the decision taking effect.
- The review being able to *enrich* as well as accept or reject — the post
  describes findings being "validated and enriched" by human risk managers, so
  the reviewing step must have somewhere to put the added knowledge.

Failure mode this prevents: automation drifting past the point where human
judgment is still at the center of decision making, which the post names as the
explicit goal of the design.

## How the three fit together

The controls cover three different exposures and none substitutes for another:

| Control | Question it answers | Who relies on it |
| --- | --- | --- |
| Reasoning log | Can we reconstruct why? | Reviewers, auditors, the next cycle |
| Sandboxed actions | Can this action hurt anything yet? | Operators |
| Expert approval | Should this happen at all? | The risk manager who owns the call |

## Source

- https://claude.com/blog/millennium-and-anthropic-are-building-a-digital-risk-analyst-with-claude (August 6, 2026)
