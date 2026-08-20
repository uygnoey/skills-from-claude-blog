---
name: inbound-reply-drafting
description: Run a sales inbox as an hourly drafting loop — a thin system prompt, a curated knowledge base of common questions and best answers, and a per-rep voice profile — so every thread needing a reply gets a draft the rep reads, edits, and sends. Use when inbound volume is consuming hours a day on repeated questions; when replies must stay factually anchored to approved product answers; when drafts should sound like the person sending them; or when adding lighter monitors for no-shows, prospects going dark, and new leads that need a first touch.
---

# Drafting inbound replies from a knowledge base

Derived from a first-person account by John Albert, a business development rep
at Anthropic, who used to spend around five hours a day answering the sales
inbox by hand — often the same questions — on top of his own book of business.

The order matters: the knowledge base comes first, the workflows are built on
top of it, and a person stays on every send.

## Instructions

### 1. Build the knowledge base first

Collect the questions the team receives most often in the sales inbox, along
with the team's best answers, into a single external-facing document. This is
the source of product facts for everything downstream.

- **Do not write it by hand.** Point Claude at the relevant product docs and
  team channels and have it build the first version.
- **Keep it fresh with a check, not a chore.** Have Claude continuously verify
  the document and flag information that might be stale, which a person then
  validates.
- Treat it as external-facing: what lands in it is what customers will read.

Structure to copy in
[templates/sales-knowledge-base.md](templates/sales-knowledge-base.md).

### 2. Give each rep a voice profile

Drafts should arrive sounding like the sender. Each rep creates a profile of
their own writing style using a voice skill that reads through documents,
messages, and emails they have written.

Structure in [templates/voice-profile.md](templates/voice-profile.md).

### 3. Assemble the inbox skill from three thin parts

The heaviest workflow in the post is also the simplest in structure. It is made
of:

1. a thin system prompt,
2. the knowledge base as context — the source for product facts,
3. the rep's voice profile.

It runs **every hour**: it scans the rep's inbox, finds every thread the rep
needs to answer, and drafts a reply for the rep to read, edit, and send.

Note what is *not* in the skill: product knowledge baked into the prompt, or
authority to send. Both are deliberate — facts live in the knowledge base so
they can be corrected in one place, and sending stays with the human.

Anatomy in
[references/inbox-skill-anatomy.md](references/inbox-skill-anatomy.md).

### 4. Add the lighter monitors around it

Two smaller skills in the post cover the administrative load around the inbox:

- **No-show and gone-dark watcher.** Watches Gmail and Google Calendar and
  notifies the rep when a meeting is a no-show or a prospect goes dark, so the
  follow-up is quick.
- **New-lead first touch.** Uses the CRM connector to scan for all new leads and
  draft a personalized first touch. It runs on a schedule throughout the day so
  leads are not left waiting.

Both are described in
[examples/lighter-monitors.md](examples/lighter-monitors.md).

### 5. Keep a person on every send

Claude can generate drafts; the rep still reads, edits, and sends them.
Personalized customer emails are prepared as drafts that the rep reviews and
customizes before sending. This is the boundary that makes the rest safe to
automate.

### 6. Write feedback back into the skill

When a draft gets corrected, have Claude record the reason in the skill so the
same mistake is not repeated. The knowledge base absorbs fact corrections; the
skill absorbs behavior corrections.

## Examples

**A repeated product question.** The hourly run finds a thread asking something
the team answers weekly. The draft pulls the approved answer from the knowledge
base, phrased in the rep's voice. The rep skims, trims a paragraph, and sends.

**A question the knowledge base does not cover.** The draft should say what is
known and stop, rather than inventing an answer. The rep writes the real reply —
and that question, with its answer, becomes the next knowledge base entry.

**A stale fact.** Claude flags an entry that may no longer be current. A person
validates it against the product docs and either confirms or replaces the
answer. Every future draft inherits the fix.

**A no-show.** The watcher notices the meeting did not happen and notifies the
rep the same morning, while the follow-up is still timely.

**A new lead at 3pm.** The scheduled scan picks it up on its next run rather
than the next morning, and leaves a personalized first touch drafted for review.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)
