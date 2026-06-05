---
name: sales-workflow-briefing
description: Patterns for building Claude-powered GTM workflows (email drafting, pre-call briefs, end-of-day recaps) that pull fresh context from source systems and can be packaged for team adoption.
---

# sales-workflow-briefing

## Instructions

Use this skill to design and implement practical GTM (go-to-market) workflows in Claude Code that:

1. Start narrow (one painful repetitive task), then expand after you can measure time saved.
2. Pull fresh context at run time from the systems where the truth lives (email threads, calendar, CRM, call recordings, shared docs).
3. Iterate on the system prompt until the drafts match the desired voice (reduce unnecessary length and hedging).
4. Support tone variants for different relationship contexts (customer vs. teammate vs. personal).
5. Bundle the workflow (instructions + templates + references) so others can adopt it quickly.

### Core workflow building blocks

- **Customer context aggregation**: Produce a 360° view of an account by querying multiple systems.
- **Pre-call brief**: Before the first call of the day, generate talking points and risks.
- **Daily recap**: After calls, draft follow-up emails based on meeting notes and docs.
- **Email drafting with voice matching**: Draft replies that match a specific writing style.

### Prompting guidance

- Keep drafts short and direct unless the user explicitly asks for more detail.
- Prefer concrete next steps and questions over generic advice.
- When information is missing, ask for the minimum clarifying input or point to the source system to check.

See: [templates/concise_sales_email.md](./templates/concise_sales_email.md) and [references/context_sources.md](./references/context_sources.md).

## Examples

### Example: generate a pre-call brief

Use the template in [templates/pre_call_brief.md](./templates/pre_call_brief.md).

### Example: draft a follow-up email from notes

Use [templates/follow_up_email_from_notes.md](./templates/follow_up_email_from_notes.md).

### Example: tone variants

Use [templates/tone_variants.md](./templates/tone_variants.md) to select a tone profile.

## Source

- https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering
