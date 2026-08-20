# Anatomy of the inbox skill

From the post: "This skill is made of a thin system prompt, the knowledge base
as context, and a profile of the rep's writing style." It "runs every hour: it
scans a rep's inbox, finds every thread that the rep needs to answer, and drafts
a reply for the rep to read, edit, and send."

That is the whole design. This reference expands on why each part is where it is,
and what belongs in each.

## The three parts

### 1. Thin system prompt

Holds the *job*, not the knowledge:

- what to scan (the rep's inbox),
- how to decide a thread needs a reply,
- that the output is a draft for review, never a send,
- where to get facts (the knowledge base) and how to sound (the voice profile),
- what to do when the knowledge base does not cover the question.

Everything the prompt does not need to know stays out of it. Product facts in
particular: they change, and a prompt is a bad place to change them.

### 2. Knowledge base as context

The single source for product facts. Because it is one document:

- a wrong answer is fixed once and every future draft inherits the fix,
- staleness can be checked mechanically, with a human validating the flags,
- what the team is willing to say in writing is visible in one place.

### 3. Voice profile

Per rep, not per team. The same approved answer leaves two reps' inboxes
sounding like each of them.

## The loop

```
every hour
  → scan the rep's inbox
  → find every thread the rep needs to answer
  → for each: draft a reply
       facts  ← knowledge base
       voice  ← rep's voice profile
  → leave the draft for the rep
rep reads → edits → sends
```

## Boundaries worth keeping

- **No autonomous sends.** The post is explicit: "Claude can generate drafts,
  but we still read, edit, and send them."
- **No facts invented to fill a gap.** A question the knowledge base does not
  cover is a signal to extend the knowledge base, not to improvise.
- **Corrections are written down.** "When you dismiss a hook or correct a draft,
  have Claude record the reason in the skill so it doesn't make the same mistake
  again."

## Generality

The post advises keeping shared skills "general enough to adapt rather than
scoped to one person's routine," because segments, books, and workflows differ
across reps. The three-part structure is what makes this possible: the
per-person parts are data (voice profile, inbox), so the skill itself stays
shareable.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)
