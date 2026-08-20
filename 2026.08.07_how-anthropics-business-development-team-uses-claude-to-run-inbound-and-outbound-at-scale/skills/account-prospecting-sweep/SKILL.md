---
name: account-prospecting-sweep
description: Run an overnight prospecting sweep across a rep's whole book so each morning starts with a brief, a score, and an outbound play per account. Use when outbound coverage is capped by manual research across a hundred-plus accounts; when account state lives scattered across CRM, sales tools, call recordings, and a data warehouse; when research must be validated against curated outbound guidance and ICP criteria; when a memory file is needed to stop duplicate outreach; or when handling one-off book-wide analysis requests like undiscovered usage sweeps and event invite lists.
---

# Prospecting a whole book overnight

Derived from a first-person account by John Albert, a business development rep
at Anthropic, who works "upwards of a hundred accounts at any given time" and
covers them through a skill that runs as a scheduled task overnight.

The output is not a list of accounts. It is, per account, a brief, a score, and
an outbound play — waiting when the rep opens their workspace in the morning.

## Instructions

### 1. Define what "the current state of an account" means

The sweep observes the current state of each account. In the post that means
questions like:

- Who are we in touch with?
- How do they use the product today?
- What signals are relevant right now?

Write these down before wiring anything up. They determine which sources you
need and what the brief has to contain.

### 2. Connect the sources that answer those questions

The post names the connections behind the sweep: the CRM, sales tools such as
Apollo and Common Room, call recordings from Gong, and the team's data
warehouse. Claude connects to these, performs deep research, and validates the
result.

Mapping of source to question in
[references/context-sources.md](references/context-sources.md).

### 3. Validate research against curated guidance

Deep research alone produces plausible accounts of a business. The post adds a
validation step: findings are checked against **outbound guidance and ICP
criteria that the team has curated**.

- Curate the guidance as a document the skill reads, the way the inbound side
  reads a knowledge base.
- Score the account against the ICP criteria explicitly, so the score is
  reproducible rather than a vibe.
- Let the guidance decide the play, not the research alone.

This is what the post means by adding context "to help Claude work more like a
BDR" at the company — the team's own standards are part of the input.

### 4. Produce a brief, a score, and a play per account

The morning artifact has three parts. Keep them separate:

- **Brief** — the current state, with the evidence behind it.
- **Score** — the account against ICP criteria.
- **Play** — the specific outbound move this state and score imply.

Format in [templates/account-brief.md](templates/account-brief.md).

### 5. Keep a memory file and a ledger

The skill keeps a small memory file and ledger, which prevents repetitive or
duplicative work. Without it, an overnight sweep re-discovers the same signals
and re-proposes outreach that already went out.

- Memory: what the sweep concluded about an account, and when.
- Ledger: what was actually acted on, so the next run does not repeat it.

### 6. Feed rep feedback back into the skill

The workflow "becomes increasingly useful over time as each BDR can provide
feedback on Claude's results, which then feeds back into the skill." Treat a
rejected play or a corrected brief as input, not just as a fix for today.

### 7. Do not build a skill for every ad-hoc request

The post is explicit that one-off requests are often just a prompt: a spend
analysis dashboard for a top account, a sweep for accounts already using the
product with no matching opportunity, a scored list of webinar invitees from an
AE's book. Reach for a skill when the request repeats.

Worked examples in
[examples/ad-hoc-requests.md](examples/ad-hoc-requests.md).

## Examples

**The morning open.** The rep opens their workspace to a brief, a score, and an
outbound play for each account in the book. The research they would have spent
hours compiling is already done; the judgment about which plays to run is not.

**Undiscovered usage.** A prompt considers an AE's full book and finds
account-level usage signals where no sales opportunity exists yet — often a good
signal to start a conversation about optimizing that usage.

**Event outreach without a skill.** An AE flags an upcoming webinar and asks
which accounts in his book would be interested. Claude checks usage data and CRM
history across the book, scores each account against the ICP, and flags the best
fits with contacts worth inviting. No skill was built for this.

**Avoiding a duplicate touch.** The sweep surfaces a signal it already surfaced
last week and the ledger shows outreach went out on it. It does not propose the
same play twice.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)
