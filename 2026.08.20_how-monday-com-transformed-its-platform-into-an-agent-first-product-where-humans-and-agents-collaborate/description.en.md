**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A customer story about monday.com — a work management platform used by more than 250,000 companies — rebuilding itself from a tool people update into an agent-first product where people and agents work on the same items. The rebuilt experience launched in May 2026 and reached 5 million agent interactions within two months.

The post is structured around what did not work first. During an "AI month" in May 2025, monday embedded AI features into existing workflows: summarizing text, categorizing information. Adoption was real but the pattern did not stick. VP of Product Orly Stern Izhaki calls that phase building "AI dust" — sprinkling automations onto workflows that were otherwise unchanged — and the conclusion drawn was that adopting AI features is not the same as becoming an AI company. Chief Product and Technology Officer Daniel Lereya describes the pivot to an agent-first product as one of the company's most significant decisions.

What followed was a rebuild rather than an addition: four ways to bring Claude into the platform, named agents with defined jobs across IT, HR, marketing, and the executive office, and agents treated as teammates who are assigned work through triggers and mentions inside the board rather than through a parallel chat window.

## When is it useful?
- When AI features have shipped, adoption looked fine in the first month, and usage has flattened into occasional summarization.
- When deciding whether to embed agents into existing workflows or to rebuild the workflow around them.
- When agents work in a chat surface parallel to where the work actually lives, and context has to be pasted in by hand.
- When agent pilots keep stalling before production because governance, permissions, and reliability were never designed in.
- When you need to describe concrete agent jobs per function rather than deploying one general assistant.

## Key points
- **"AI dust" is the failure mode.** Sprinkling automations onto existing workflows produces features that help — summarizing, categorizing — without changing how work is done, and usage does not compound.
- **Four deployment paths.** monday Agents built with prompts using Claude as the model; bring-your-own-agent, joining Claude Managed Agents to the platform; pre-built specialized agents from the monday Agents Store, including legal and finance plugins; and Claude coding integration, where teams connect Claude in dashboards, assign tasks, and execute in customer environments.
- **Agents get named jobs, not a general mandate.** IT runs an Intake & Triage Agent, a Knowledge Agent, and an Incident Agent; HR has resume screening, interview scheduling, hiring coordination, and feedback management; marketing has competitive intelligence and battlecards; the executive office has an Operator Agent, an Org Health Agent, and a Strategy Consultant Agent.
- **Teammate design.** Each agent has a name, an avatar, and a place in the workflow. Work is assigned through triggers and mentions where employees already are, rather than in a separate chat interface.
- **The production line runs on one item.** In the campaign example, a brief is shaped by a marketer and content lead, structured by a Strategist Agent into objectives, messaging pillars, channels, and metrics, built into landing page variants by a Claude Managed Agent, checked against brand guidelines by a Brand Reviewer, and approved by a human before publishing.
- **Cooke Seafood, the customer of the customer.** The world's largest family-owned seafood company runs project delivery and resource management across roughly 200 active and proposed projects, contract management across 130 contracts, and automated reporting that surfaces risks into RAID logs. Director of Strategy Patti Stevens frames the shift as going from a platform they had to update to one they operate from.
- **Five lessons.** Mental models were harder to move than the technology; small teams with clear ownership stayed aligned while direction, UX, pricing, trust models, and quality definitions all moved at once; adoption depended on trust infrastructure — governance, permissions, transparency, reliability; agent capability depended on backend investment, including monday DB, to ground agents in live project data at enterprise scale; and the transformation extended an existing identity rather than replacing it.

## Bundled resources
- `skills/agent-first-product-transformation/SKILL.md` — moving a product from AI features to agent-first.
- `skills/agent-first-product-transformation/references/deployment-models.md` — the four ways agents are brought into the platform, and when each fits.
- `skills/agent-first-product-transformation/references/agent-job-map.md` — the named agent jobs by function.
- `skills/agent-first-product-transformation/references/transformation-lessons.md` — the five lessons, with what each one implies for a plan.
- `skills/agent-first-product-transformation/examples/campaign-production-line.md` — the end-to-end marketing example and the Cooke deployment.
- `agents/*.md` — five subagents distilled from the named roles in the post.
- `guides/agent-first-platform-rollout.{en,ko,es,ja}.md` — sequencing a rollout from AI features to agent-first.

## Source
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) — published 2026-08-20.
