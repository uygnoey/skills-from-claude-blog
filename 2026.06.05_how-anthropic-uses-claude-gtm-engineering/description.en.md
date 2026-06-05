**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# How one seller rebuilt GTM workflows with Claude Code

## What is this post?
A case study of how a non-engineer sales operator used Claude Code to build and iterate internal GTM tools—starting with an email-drafting app inside Gmail, then expanding into automated daily briefs/recaps and a team-wide plugin bundling skills and connectors.

## When is it useful?
- When your team has high-volume, repetitive communication work (customer email replies, meeting follow-ups).
- When you need fast, iterative automation but have limited engineering bandwidth.
- When you want to package internal workflows (skills + integrations) so others can adopt them quickly.

## Key points
- Build one narrow tool around a painful workflow, then expand once it proves value.
- Pull live context from source systems (docs, CRM, calendar, email) at generation time.
- Iterate heavily on the system prompt to match a specific writing style and reduce unwanted traits (length, hedging).
- Use tone variants to adapt drafts for different relationship contexts.
- Productize the result as a plugin so the whole org can install and run the workflows.

## Bundled resources
- Skill: `sales-workflow-briefing` (patterns for GTM briefing + recap + context aggregation)
- Guide: “GTM workflow automation with Claude Code” (how to apply the patterns)
- Output style: “concise-sales-email-draft” (short, confident drafts)

## Source
- https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering
