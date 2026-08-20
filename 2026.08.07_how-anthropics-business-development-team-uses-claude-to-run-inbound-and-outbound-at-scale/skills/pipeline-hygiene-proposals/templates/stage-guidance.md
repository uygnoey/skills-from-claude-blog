# Opportunity stage guidance

The post describes a skill that keeps the CRM current "by reading our internal
guidance on opportunity stages and checking it against what's actually happening
in Gmail and Gong." This template is a structure for that guidance, written so a
skill can check it against evidence.

The post does not publish the team's actual stage definitions — those are yours.
What it does establish is that the guidance is a document the skill reads, and
that stage movement is judged against observable activity.

---

## How to write a checkable stage

A stage definition an agent can act on names an **observable event**, not an
internal feeling of progress. "Customer is interested" cannot be checked against
a mailbox. "Customer has asked about pricing in writing or on a call" can.

## Stage template

### Stage: _[name]_

**In this stage when:**
- _[condition, stated observably]_

**Entry is marked by:**
- _[the event that moves an opportunity in — e.g. a pricing question raised on a call]_

**Evidence that would establish it:**
- _[email: what kind of message]_
- _[call: what kind of discussion]_
- _[CRM: what field or record]_

**Not this stage if:**
- _[the disqualifying condition — e.g. raised in passing, no follow-up]_

**Common false positive:**
- _[the pattern that looks like entry but is not]_

---

## Worked shape, using the post's own example

The post says: "If we've met with a customer and moved on to pricing questions,
the opportunity should probably progress a stage."

Written as a checkable rule:

> **Entry is marked by:** a meeting has occurred **and** the conversation since
> has moved to pricing.
> **Evidence:** the meeting on the calendar or in the call record, plus pricing
> discussion in email or on a call after it.
> **Not this stage if:** pricing came up before or during the meeting only in
> passing, with no follow-up.

Note the "probably" in the source. That is exactly why the skill proposes and a
person approves.

## Maintenance

When the same proposal keeps getting rejected for the same reason, the guidance
line behind it is ambiguous. Fix the guidance rather than adding another
exception to the skill.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)
