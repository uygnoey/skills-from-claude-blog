# Sales knowledge base

The post describes "a document where I've collected the questions we most
commonly receive in our sales inbox, along with our best answers to those
questions," which "functions as our sales knowledge base, which Claude reads
before drafting any replies we send."

This template is a structure for that document. The post does not publish its
format — what it does specify is the content (common questions plus best
answers), that Claude builds the first version from existing sources, that the
document is external-facing, and that stale information gets flagged for a
person to validate.

---

## How to create the first version

Point Claude at:

- the team's product documentation,
- the internal channels where these questions get answered,
- past replies that worked.

Ask it to collect the recurring questions and draft the best answer for each.
Then have a person read the whole thing once before it goes into service — it is
external-facing.

## Entry format

### Q: _[the question as customers actually ask it]_

**Answer.**
_[The reply the team stands behind. Written to be sent, not summarized.]_

**Applies to.** _[product / plan / segment, if the answer differs]_

**Do not say.** _[claims that are wrong, unapproved, or out of date]_

**Last validated.** _[YYYY-MM-DD — by whom]_

**Source.** _[the doc or owner this answer is derived from]_

---

## Suggested sections

Group entries so a drafting run can find the right one quickly:

1. **Products and capabilities** — what the product does, what it does not.
2. **Plans, limits, and pricing questions** — what is answerable in writing.
3. **Security, privacy, and compliance** — where the approved language matters
   most.
4. **Getting started** — trials, onboarding, first steps.
5. **Routing** — questions that should not be answered by a draft at all, and
   who they go to instead.

## Staleness

Have Claude re-read the document on a schedule and flag entries whose facts may
have moved — new releases, changed limits, superseded docs. Flagging is the
agent's job; **validating is a person's job.** Record the validation date on the
entry so the next check knows what it is looking at.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)
