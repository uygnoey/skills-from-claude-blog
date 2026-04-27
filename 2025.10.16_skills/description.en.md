**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post introduces **Agent Skills**: reusable folders of instructions plus optional scripts and resources that Claude can load when relevant to a task.

## When is it useful?
Use this when you want Claude to follow consistent procedures for specialized work (for example: Excel workflows, document creation standards, or brand guidelines) across Claude apps, Claude Code, and the API.

## Key points
- Skills are **composable**, **portable**, **efficient**, and can be **powerful** by bundling executable code.
- Claude automatically detects when a skill is relevant and loads only the minimal required content.
- Skills can be managed via the Claude apps, the Claude Console, and the API (including a `/v1/skills` endpoint).
- Claude Code can install skills via plugins (e.g., from the anthropics/skills marketplace) or via `~/.claude/skills`.

## Bundled resources
- Skill bundle: `skills/agent-skills-overview/` (overview + quick-start checklist and reference links)

## Source
- https://claude.com/blog/skills
