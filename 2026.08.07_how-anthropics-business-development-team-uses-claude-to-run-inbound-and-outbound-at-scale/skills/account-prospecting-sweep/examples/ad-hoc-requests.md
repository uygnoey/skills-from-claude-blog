# Ad-hoc requests that never became skills

The post has a section on one-off work: "Often, requests come to the BDR team in
an ad-hoc manner and Claude makes it possible for us to partner with our AEs in
a more strategic way." Three examples are given, and in each case the answer is
a prompt, not a new skill.

## 1. Usage trends for a top account

> "If an AE is curious about usage trends for a top account, we are a prompt
> away from providing a legible and descriptive dashboard that highlights the
> relevant trends."

**Input:** the account, the data warehouse.
**Output:** a dashboard-style report that highlights the relevant trends —
legible and descriptive, meaning the AE can act on it without a follow-up
meeting.
**Why no skill:** the request arrives shaped differently every time.

## 2. Undiscovered usage sweep

> "One of my favorite workflows is running an undiscovered usage prompt. It
> considers an AE's full book and finds usage signals on the account level where
> we do not yet have a sales opportunity."

**Input:** the AE's full book, product usage data, CRM opportunity records.
**Output:** every account already using the product with no matching
opportunity.
**Why it matters:** the post calls this "a great signal for us to begin reaching
out and working together with a customer to optimize their usage and experience"
— the gap between usage and pipeline is the lead.

**Shape of the prompt:**

> Consider every account in _[AE]_'s book. Find accounts with usage signals for
> _[product]_ where no sales opportunity exists. For each, show the usage signal,
> the account owner, and why the gap looks real.

## 3. Event invite list

> "One of my AEs recently flagged that we have an upcoming Claude Code for Data
> Engineering webinar and asked if I could find accounts in his book that would
> be interested in attending. I don't have a skill for that, but for this type of
> request a prompt was enough."

**What Claude did:** checked usage data and CRM history across the book, scored
each account against the ICP, and flagged the best fits with contacts worth
inviting.

**Shape of the prompt:**

> We have a _[topic]_ webinar on _[date]_. Across _[AE]_'s book, check usage data
> and CRM history, score each account against our ICP, and return the best fits
> with the contacts worth inviting and why.

## When to promote one into a skill

The post's own rule for the shared plugin applies here too: a workflow earns a
skill once reps use it consistently in their daily work. Until then, a prompt is
cheaper — and the ad-hoc version teaches you what the skill would need to
contain.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)
