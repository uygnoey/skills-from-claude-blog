---
name: pipeline-hygiene-proposals
description: Keep a CRM current by reading the team's own guidance on opportunity stages, checking it against what is actually happening in email and call recordings, and proposing each update with the evidence behind it for a rep to approve. Use when pipeline data drifts because updating stages is manual; when a stage change should be justified by evidence rather than memory; when an agent must propose rather than write to the system of record; or when rejected proposals should teach the skill instead of being silently discarded.
---

# Proposing CRM updates with evidence

Derived from the pipeline scanner described by John Albert, a business
development rep at Anthropic: "We also have a skill that keeps Salesforce
current by reading our internal guidance on opportunity stages and checking it
against what's actually happening in Gmail and Gong."

The point is not automated data entry. It is that the evidence for a stage change
usually already exists — in the mailbox and the call recording — and nobody has
time to reconcile it by hand.

## Instructions

### 1. Make the stage guidance readable

The skill reads the team's internal guidance on opportunity stages. That
guidance has to exist as text the skill can read, with each stage stated in
terms that can be checked against evidence.

For each stage, write down:
- what must be true for an opportunity to be in it,
- what observable event marks entry,
- what disqualifies it.

Structure in
[templates/stage-guidance.md](templates/stage-guidance.md).

### 2. Read what is actually happening

Check the guidance against the record of the relationship: email (Gmail in the
post) and call recordings (Gong). The post's example is direct — "If we've met
with a customer and moved on to pricing questions, the opportunity should
probably progress a stage."

The evidence is the conversation, not the rep's recollection of it.

### 3. Propose, never write

Claude proposes each update **with the evidence behind it** and waits for
approval. The system of record is changed by a person.

Each proposal carries:
- the opportunity,
- current stage → proposed stage,
- the guidance rule that applies,
- the evidence, quoted and sourced,
- what would make the proposal wrong.

Format in
[templates/update-proposal.md](templates/update-proposal.md).

### 4. Record why a proposal was rejected

"When I edit or reject a proposal, it records the reason why so it doesn't
repeat the mistake." This is the loop that makes the skill worth keeping: a
rejection without a reason is a proposal you will see again next week.

- Capture the reason at the moment of rejection, in the rep's own words.
- Feed it back into the skill, the way the post describes feedback being written
  into skills generally.
- Watch for repeat rejections of the same kind — that usually means the stage
  guidance itself is ambiguous.

Failure patterns and how the loop closes them:
[references/feedback-loop.md](references/feedback-loop.md).

### 5. Keep the scan scheduled and bounded

Run it on a schedule so hygiene does not depend on anyone remembering. Bound
each run to opportunities where something actually changed — new mail, a new
call — so reps get few, high-signal proposals rather than a queue.

## Examples

**A stage that should have moved.** The team met with a customer last week and
the thread since then is about pricing. The guidance says pricing discussion
marks the next stage. The proposal shows the current stage, the proposed stage,
the guidance line, and the two messages that establish the pricing conversation.
The rep approves.

**A stage that should not move.** A pricing question came up in passing, but the
economic buyer has not engaged. The rep rejects and writes the reason: a single
question is not a pricing conversation. The skill records it and stops proposing
on that pattern.

**A stale opportunity.** No mail, no calls, no activity for weeks. The evidence
supports a proposal too — the direction is just backwards.

**An ambiguous rule.** The same rejection reason shows up across three reps. The
fix is not more feedback into the skill; it is rewriting that line of the stage
guidance so it can be checked.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)
