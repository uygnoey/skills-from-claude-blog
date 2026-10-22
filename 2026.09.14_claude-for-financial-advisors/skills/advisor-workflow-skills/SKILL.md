---
name: advisor-workflow-skills
description: Run a financial advisor's daily workflows with Claude the way the Claude for Financial Advisors plugin frames them - pre-meeting prep, post-meeting notes and follow-up, prospect intake, advisor onboarding, portfolio rebalance review, alternative investments brief, estate and tax brief, and compliance and AI policy - drawing on connected custodians, portfolio platforms, CRMs, planning and estate tools, and meeting capture. Claude gathers, summarizes, and drafts; it stages CRM updates and client communications for advisor approval, and leaves investment recommendations, client communications, and compliance determinations to human review. Use when an advisor or RIA wants a meeting brief, a drift explanation, a transcript-to-follow-up pass, an estate/titling check, an alts summary, a prospect handoff, or a marketing-language screen.
---

## Purpose
Anthropic's "Claude for Financial Advisors" release pairs connectors (custodian, portfolio
reporting, CRM, planning, estate, meeting capture) with skills that each map to one moment in an
advisor's day. The goal is to move prep and paperwork forward so the advisor spends more time with
clients, while the advisor stays in control of anything regulated or client-facing.

Companion files:
- [references/skills-catalog.md](references/skills-catalog.md) — the eight skills: inputs, outputs,
  and which systems they draw on.
- [references/connectors.md](references/connectors.md) — the partner connectors and what each one
  brings into Claude.
- [references/oversight-and-setup.md](references/oversight-and-setup.md) — approval rules,
  compliance skill scope, plan recommendation, and install steps.

## When to use
- Before a client review: build one brief from holdings, recent activity, and open items.
- After a meeting: turn the transcript into a client summary, recap email draft, and CRM tasks.
- A portfolio has drifted or holds a concentrated position and needs a first-draft explanation.
- A household holds alternatives that must be shown alongside the rest of the portfolio.
- Estate documents need checking against actual account titling and beneficiaries.
- A prospect has shared information and the first meeting needs a head start.
- A new advisor joins and needs tools connected and a first meeting prepped.
- Client-facing language needs screening before it goes to compliance review.

## Instructions

1. **Identify the moment and pick the matching skill.** Use the catalog in
   [references/skills-catalog.md](references/skills-catalog.md). If the request spans several
   moments (for example prep, then follow-up), run them in order rather than merging outputs.

2. **Pull from connected systems, not memory.** Read the client's data from whichever connectors
   the firm has set up (see [references/connectors.md](references/connectors.md)). If a needed
   source is not connected, say which one is missing and work from what the advisor uploads.

3. **Produce the deliverable the skill defines.**
   - Pre-meeting prep: one brief with holdings, recent account activity, and open items from prior
     meetings, focused on that client's situation.
   - Post-meeting: client summary, recap email draft, and CRM tasks in one pass.
   - Prospect intake: summary, analyst handoff, and a what-to-expect memo.
   - Rebalance review: drift and concentration flags against the target allocation, plus a first
     draft explanation.
   - Alternatives brief: holdings (for example NAV, commitments, unfunded capital, capital
     activity, performance) shown next to the rest of the portfolio.
   - Estate and tax brief: estate plan vs. titling and beneficiaries, prior-year tax look-back,
     mismatches surfaced for review, optional CRM follow-up tasks.
   - Compliance and AI policy: highlight content that may need extra review based on the firm's
     configured criteria (including SEC Marketing Rule screening), help document review workflows
     and AI-governance records.

4. **Stage, never execute, regulated or client-facing actions.** CRM updates, client emails, and
   rebalance sessions are staged for the advisor's approval. Do not present investment
   recommendations or compliance determinations as final; label them for human review.

5. **Match the firm's style.** The skills can be used as-is or adapted to the firm's workflows,
   service model, and house style. Apply any house template the firm provides.

6. **Leave a record.** Note what sources were used and what is awaiting approval so the firm can
   keep records within its existing governance processes.

## Examples

**Pre-meeting prep**
- Input: "Prep me for the Lee household review tomorrow."
- Output: one brief combining custodial positions and recent transactions, open items from the
  last meeting notes in the CRM, and any life events captured by the meeting assistant, with
  questions to raise. Nothing is sent; the brief is for the advisor.

**Post-meeting follow-up**
- Input: a meeting transcript.
- Output: a client summary, a recap email draft marked "awaiting advisor approval", and a list of
  CRM tasks staged for confirmation.

**Rebalance review**
- Input: "Which of my clients are out of tolerance, and explain the drift for the top one."
- Output: list of out-of-tolerance accounts, drift and concentration detail for the selected
  client, and a draft explanation for the advisor to edit. No trades are placed.

**Compliance screen**
- Input: a draft client newsletter paragraph.
- Output: phrases flagged against the firm's configured criteria and the SEC Marketing Rule, with
  a note that the determination rests with the firm's compliance reviewer.

## Source
- https://claude.com/resources/articles/claude-for-financial-advisors (2026-09-14)
