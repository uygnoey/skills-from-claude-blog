---
name: discovery-call-scorecard
description: Score a discovery call against the team's playbook and return a scorecard — top three things done well, top three areas to improve, an explicit pass or fail against the criteria, and the single highest-leverage thing to practice next. Use when call coaching does not scale past the calls a manager can personally listen to; when feedback needs to be specific to what was said rather than generic; or when a team wants a consistent, playbook-anchored standard applied to every discovery conversation.
---

# Coaching discovery calls against a playbook

Derived from the call coach described by John Albert, a business development rep
at Anthropic: "We use a skill that evaluates Gong transcripts against our
discovery call playbook and builds a scorecard for each call, with specific
feedback based on the conversation."

The scorecard has a fixed shape, and the shape is the useful part: it forces
prioritization instead of a list of everything that could have gone better.

## Instructions

### 1. Write the discovery playbook down

The skill evaluates transcripts *against the team's discovery call playbook*. If
the playbook lives in people's heads, there is nothing to evaluate against and
the feedback becomes generic advice.

The playbook needs, per area of the call, criteria concrete enough that a
transcript either meets them or does not.

Structure in [templates/discovery-playbook.md](templates/discovery-playbook.md).

### 2. Evaluate the transcript, not the impression

Feed the call transcript and score it against the playbook. Feedback must be
"specific feedback based on the conversation" — tied to what was said, quotable
back to the rep.

### 3. Produce the four-part scorecard

The post specifies exactly what the feedback includes:

1. **Top three things done well.**
2. **Top three areas to improve.**
3. **An explicit pass or fail score on the criteria.**
4. **A single highest-leverage thing to practice next.**

Keep all four, and keep the counts. Three and three is a forcing function; the
single practice item is what makes the scorecard actionable rather than
comprehensive.

Format in [templates/scorecard.md](templates/scorecard.md).

### 4. Make pass/fail explicit

The post calls out an *explicit* pass or fail against the criteria. A scorecard
that only offers commentary lets everyone read their own call as a pass. State
the verdict, and state which criterion decided it.

Guidance on setting the bar:
[references/scoring-criteria.md](references/scoring-criteria.md).

### 5. Feed corrections back

As with the team's other skills: when the scoring is wrong, record why, so the
skill does not repeat it. A coach that mis-scores twice in the same way stops
being read.

## Examples

**A call that passes with a clear next practice item.** Three specific strengths
quoted from the transcript, three specific gaps, a pass, and one thing to
practice — for instance, a habit of moving to the next question before the
customer finished the answer.

**A call that fails on one criterion.** The rest of the conversation was strong,
and the scorecard says so in the "done well" section, but the criterion that
decided the fail is named explicitly rather than buried in the improvement list.

**Feedback that stays specific.** "Ask better qualifying questions" is not
usable. "When they mentioned the migration deadline, the follow-up moved to
product rather than to what happens if the deadline slips" is.

**Coaching at book scale.** Every discovery call gets the same standard applied,
rather than only the calls a manager had time to listen to.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)
