---
name: inbound-buying-agent-design
description: Design, build, and iterate an inbound "buying agent" that takes a prospect from "I want this for my company" to a purchase, a hand-off to a sales rep, or a quick answer - modeled on how Anthropic's sales team rebuilt inbound with Claude Managed Agents (beta) in September 2026. Covers where to deploy the agent (contact-sales and pricing pages, in-product, email), the three conversation outcomes, keeping the experience opt-in, a goal-first and short system prompt, a small tool set plus knowledge base, versioned prompt iteration with a staging agent and subject-matter experts in the loop, recommending the right (not the biggest) plan, and treating every agent-to-rep escalation as feedback. Use when a sales or go-to-market team cannot keep up with inbound demand, wants an always-on self-serve buying path, or is writing and tuning the prompt for such an agent.
---

## Purpose
Inbound demand can outgrow a form-to-BDR-to-AE process: buyers wait days for simple answers that are
already in the docs. This skill turns Anthropic's buying-agent case study into a repeatable design and
iteration procedure. In the source, the agent holds thousands of conversations a day; escalated leads
convert to opportunities more than twice as often as old form leads and close about five days faster.

## When to use
- Inbound requests far exceed what the BDR team can answer, and most questions are simple
  (price, seat minimums, compliance terms such as HIPAA contract requirements).
- You want buyers answered at any hour and in any language, and able to buy without a rep if they prefer.
- You are drafting or tuning the system prompt, tools, or knowledge base of a sales-facing agent.

## Instructions

1. **Define the job like a rep's job.** The agent should do what a good rep does: understand what the
   customer is trying to solve, what their current usage looks like, and how best to help them.
2. **Deploy where buyers already ask.** Contact-sales page, pricing page, inside the product, and email.
   Keep it **opt-in**: at the start the buyer chooses an agent or a sales rep.
3. **Design the conversation flow.** The buyer describes needs, the agent asks a few follow-ups, answers
   pricing, security, and data questions, then recommends a plan and seat count. Every conversation
   ends in one of three outcomes - see [references/conversation-outcomes.md](references/conversation-outcomes.md).
4. **Keep the architecture small.** A prompt, a handful of tools, and Claude, on a managed runtime
   (Claude Managed Agents handles hosting, sessions, and tool orchestration). Spend your effort on the
   three selling-specific parts: the prompt, the tools, and the knowledge base.
5. **Write a goal-first, short prompt.** State the goal instead of a rules flowchart, and supply the
   knowledge Claude needs (what seat-based pricing covers, when billing cycles run). Start from
   [templates/goal-first-system-prompt.md](templates/goal-first-system-prompt.md).
6. **Optimize for the right plan, not the biggest.** Pointing a small team to a smaller plan is a
   feature: correctly placed buyers stay longer and have a better experience.
7. **Put SMEs in the loop.** Engineering owns the code; sales and content leads review and edit the
   system prompt directly (in the Console in the source). Changes go to a **staging agent** first.
8. **Version every change.** Each prompt change is a version (the source reached v7 about a week into
   internal testing and kept shipping weekly after launch). Roll new sessions back to a prior version
   when needed.
9. **Treat escalations as feedback.** Require the agent to state *why* it hands off. Log reasons with
   [templates/escalation-feedback-log.md](templates/escalation-feedback-log.md), cluster them, and fix
   the self-serve gaps they reveal (the source roughly halved the share needing a human).
10. **Measure.** Track conversations/day, outcome mix, lead-to-opportunity rate vs. the old form,
    time to close, and rep effort per deal. See [references/lessons-and-results.md](references/lessons-and-results.md).

## Examples

**Example 1 - prompt rewrite.**
Input: a 3-page prompt that lists every qualification rule as a flowchart.
Output: a short prompt opening with "Your goal is to understand customer requirements, qualify
prospects, and recommend the best plan," followed by pricing/billing knowledge and the three outcomes;
the rule list is dropped.

**Example 2 - small team asks about Enterprise.**
Input: "We're 8 people, should we get Enterprise?"
Output: the agent asks about needs, and if a smaller plan fits, recommends it with a seat count and a
checkout link instead of upselling.

**Example 3 - escalation review.**
Input: a week of hand-offs where most reasons are "customer needs X that self-serve can't do yet."
Output: a ranked list of self-serve gaps fed into the product/experience backlog; re-measure the
hand-off share next cycle.

## Bundled resources
- [references/conversation-outcomes.md](references/conversation-outcomes.md) - the three endings and hand-off payload.
- [references/lessons-and-results.md](references/lessons-and-results.md) - lessons, platform reasons, reported results.
- [templates/goal-first-system-prompt.md](templates/goal-first-system-prompt.md) - starting prompt skeleton.
- [templates/escalation-feedback-log.md](templates/escalation-feedback-log.md) - hand-off reason log.

## Source
- https://claude.com/resources/articles/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents
