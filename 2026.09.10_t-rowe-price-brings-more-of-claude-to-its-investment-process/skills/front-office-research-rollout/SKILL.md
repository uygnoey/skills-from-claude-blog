---
name: front-office-research-rollout
description: Plan and run a front-office AI rollout for a research-driven investment firm, following the pattern T. Rowe Price described in September 2026 - Claude and Claude Cowork for research synthesis and knowledge-intensive multi-step processes, Claude Code for building investment tools, business-owned applications under responsible-use standards, and human judgment kept accountable for decisions. Use when an asset manager or similar research organization wants to start AI adoption with portfolio managers and analysts, classify candidate use cases, or set up ownership and governance for them.
---

## Purpose
The source describes T. Rowe Price expanding Claude across its investment organization. The firm is an
active manager: decisions rest on its own fundamental research, and Claude is meant to give analysts and
portfolio managers more capacity for that work, not to make the call. This skill turns that pattern into a
repeatable rollout checklist. Details beyond what the post states are left to the firm (see the original).

## When to use
- Deciding where Claude fits in an investment research workflow.
- Sorting candidate use cases into research, multi-step process, or tool-building work.
- Setting up who owns each AI application and which standards govern it.

## Instructions

1. **Start with the decision makers.** Scope the first wave around portfolio managers and analysts (the
   post notes this is unlike most enterprise deployments, which begin in the back office).
2. **Classify each candidate use case** into one of the three areas from the post:
   - *Research* - ask Cowork to synthesize complex information so people spend more time on analysis and debate.
   - *Multi-step process* - knowledge-intensive tasks run in Cowork where consistency and oversight matter.
   - *Tool building* - developers use Claude Code to build and improve tools for investment and operating teams.
   Record each one in [templates/use-case-register.md](templates/use-case-register.md).
3. **Keep judgment with people.** For every use case, name the human who reviews Claude's output and owns the
   resulting view or decision. Claude extends the research process; it does not replace it.
4. **Assign ownership and governance** using the model in
   [references/governance-model.md](references/governance-model.md): the business owns each application,
   a central AI hub evaluates and scales, embedded AI leaders sit in the business lines, and responsible-use
   standards apply.
5. **Pair the rollout with enablement**: training, talent development, and responsible-use guidance so people
   use AI confidently.
6. **Review and scale.** Have the central hub evaluate results and decide which applications to scale.

## Examples

**Research synthesis**
> An analyst asks Cowork to synthesize a large set of filings and notes on a company into a briefing, then
> spends the saved time testing the thesis with the portfolio manager. The analyst owns the conclusion.

**Register entry**
> Use case: consistent multi-step review in Cowork. Area: multi-step process. Business owner: the investment
> team. Human reviewer: named analyst. Governing standard: firm responsible-use policy. Status: pilot.

**Tool building**
> A developer uses Claude Code to improve an internal tool the investment team relies on; the owning team
> signs off before it is scaled.
