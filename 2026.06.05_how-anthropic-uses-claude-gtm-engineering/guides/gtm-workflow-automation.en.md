**English** · [한국어](./gtm-workflow-automation.ko.md) · [Español](./gtm-workflow-automation.es.md) · [日本語](./gtm-workflow-automation.ja.md)

# GTM workflow automation with Claude Code

## What this guide covers
This guide distills the post's approach into a repeatable method for building Claude Code workflows for GTM teams: start with one narrow workflow, pull live context, iterate on prompts for voice, and then package the result for broad adoption.

## Method
1. **Pick one painful workflow** (e.g., customer email replies).
2. **Define the context sources** you will use at run time (email, calendar, CRM, docs).
3. **Draft a system prompt** and iterate until the output matches your team's voice.
4. **Add tone variants** for different relationship contexts.
5. **Expand to adjacent workflows** (pre-call brief, daily recap) once the first workflow is stable.
6. **Bundle for adoption** (skills + connectors/integrations) so others can install and use it quickly.

## Recommended artifacts
- Skill: [../skills/sales-workflow-briefing/SKILL.md](../skills/sales-workflow-briefing/SKILL.md)
- Templates: [../skills/sales-workflow-briefing/templates/](../skills/sales-workflow-briefing/templates/)

## Source
- https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering
