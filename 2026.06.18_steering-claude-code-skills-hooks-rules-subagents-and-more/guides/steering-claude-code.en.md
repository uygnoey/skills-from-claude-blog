**English** · [한국어](./steering-claude-code.ko.md) · [Español](./steering-claude-code.es.md) · [日本語](./steering-claude-code.ja.md)

# Decision framework for steering Claude Code

## Summary

Claude Code provides several places to put instructions, each with different tradeoffs (load timing, compaction behavior, context cost, and authority).

## The seven methods

The post covers: CLAUDE.md files, rules, skills, subagents, hooks, output styles, and appending the system prompt.

## Practical placement guidance

- Keep root CLAUDE.md concise (<200 lines) and treat it like code (owner + review).
- Use subdirectory CLAUDE.md files for conventions limited to a folder.
- Use rules for constraints; prefer path-scoped rules so they load only when relevant.
- Use skills for procedures (deploy workflows, release checklists, review processes).
- Use subagents for isolated side tasks that should return only a summary.
- Use hooks for deterministic automation and enforcement on lifecycle events.
- Use output styles only for significant role changes; check built-in styles first.
- Use append-system-prompt for one-off additive instructions (tone/format).

## Source

- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
