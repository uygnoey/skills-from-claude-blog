---
name: commitment-funded-partner-procurement
description: Plan and request the purchase of partner software (for example Snowflake capacity, Snowflake's inference API, or a committed Vercel plan) through Claude Marketplace using part of an existing Anthropic commitment, based on how CodeRabbit, Power Digital, and ThoughtSpot did it (September 2026). Covers spotting candidate tools the team already relies on alongside Claude, checking eligibility (limited preview - talk to the account team or submit a request), framing the purchase as already-approved budget rather than a new budget request, and the seller-side view for partners who want to sell through the marketplace. Use when a team with an Anthropic commitment wants to expand a data platform or infrastructure vendor without a new budget cycle, or when a vendor building on Claude asks how marketplace selling helps.
---

## Purpose
Teams building with Claude also depend on data platforms and infrastructure. Claude Marketplace lets a
company with an Anthropic commitment put part of it toward such partners, so one investment covers more
of what teams use and procurement is faster. This skill turns three customer stories into a procedure.

## When to use
- You have an Anthropic commitment and want to expand a partner tool (e.g. Snowflake, Vercel) your
  Claude workloads already depend on.
- A pay-as-you-go plan needs to move to a committed plan and a new budget request would be slow.
- You are a vendor building on Claude and evaluating marketplace selling.

## Instructions

1. **Inventory dependencies.** List the tools your Claude workloads run on (data platform, sandbox and
   workflow infrastructure, inference APIs). Use [templates/procurement-request.md](templates/procurement-request.md).
2. **Match to marketplace partners.** Check whether the vendor is offered on Claude Marketplace
   (the article names Vercel and Snowflake "and more"). Compare with the patterns in
   [references/case-studies.md](references/case-studies.md).
3. **Check eligibility.** Using an Anthropic commitment this way is in **limited preview**. Talk to your
   Anthropic account team or submit a request to see if you are eligible.
4. **Frame it as approved budget.** The value in every case was spending from budget that was already
   approved - no new budget request. State which portion of the commitment you want to apply and why.
5. **Choose the purchase shape.** Examples from the source: expand an existing vendor commitment
   (Power Digital, Snowflake), buy a specific API (ThoughtSpot, Snowflake inference API), or upgrade
   from pay-as-you-go to a committed plan (CodeRabbit, Vercel).
6. **Track outcome.** Record time to contract and what the expansion enabled.
7. **Seller view (optional).** If you build on Claude and want to sell through the marketplace, note the
   seller benefits in [references/case-studies.md](references/case-studies.md); the article itself
   gives no listing steps.

## Examples

**Example 1 - data platform expansion.**
Input: "Our client data lives in Snowflake, Claude runs on it via Cortex AI, and we need more capacity."
Output: Request to expand Snowflake through Claude Marketplace from the Anthropic commitment (as
Power Digital did); confirm eligibility with the account team.

**Example 2 - inference API for a product team.**
Input: "Our analytics product runs Claude against customer data inside Snowflake; the product team
needs Snowflake's inference API now."
Output: Apply the inference API purchase to the existing commitment (ThoughtSpot pattern) so building
can start on budget already set aside.

**Example 3 - infra plan upgrade.**
Input: "Our coding agents run in Vercel Sandbox with Vercel Workflows; we want to leave pay-as-you-go."
Output: Fund the committed Vercel plan from the Anthropic commitment (CodeRabbit closed within a week).

## Bundled resources
- [references/case-studies.md](references/case-studies.md) - the three customers plus seller quotes, summarized.
- [templates/procurement-request.md](templates/procurement-request.md) - internal request / eligibility checklist.

## Source
- https://claude.com/resources/articles/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace
