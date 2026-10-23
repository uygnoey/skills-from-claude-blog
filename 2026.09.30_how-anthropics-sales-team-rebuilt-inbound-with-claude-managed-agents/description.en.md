**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A case study (September 30, 2026) by Carl Johnson, a sales development leader at Anthropic, on how a
buying agent built on Claude Managed Agents (beta) now answers most inbound customers and takes them from
"I want Claude for my company" to a purchase, and how that changed the sales team's work.

## When is it useful?
- When inbound demand outgrows a form → BDR → AE process and buyers wait days for simple answers.
- When designing a self-serve, always-on buying experience that still hands complex deals to reps.
- When writing and iterating the prompt for a customer-facing sales agent.

## Key points
- Old process: tens of thousands of inbound requests a month; reps answered questions the docs already covered.
- The agent lives on the Contact Sales and Pricing pages, in the product, and in emails; it is opt-in.
- Each conversation ends in a purchase, a hand-off to a rep with full context, or a quick answer.
- Architecture: a prompt, a handful of tools, and Claude on Managed Agents (hosting, sessions, tool orchestration).
- Why Managed Agents: one engineer shipped in a few weeks; sales/content leads edited the prompt in the
  Console with a staging agent; every change is a version (v7 after about a week of internal testing).
- Lessons: give Claude a goal, not rules; less is more; keep SMEs in the loop; recommend the right plan
  (e.g. Team over Enterprise); treat each escalation reason as feedback (hand-offs fell by about half).
- Results: thousands of conversations a day; escalated leads convert to opportunities more than 2x as often
  and close about five days faster; one rep went from ~10 to ~6 emails per deal and 2.5x closed-won output.

## Bundled resources
- Skill: `inbound-buying-agent-design` (`references/conversation-outcomes.md`,
  `references/lessons-and-results.md`, `templates/goal-first-system-prompt.md`,
  `templates/escalation-feedback-log.md`).

## Source
- https://claude.com/resources/articles/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents
