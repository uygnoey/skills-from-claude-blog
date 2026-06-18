---
name: instruction-placement-framework
description: Decide where to place Claude Code instructions (CLAUDE.md, rules, skills, subagents, hooks, output styles, or appended system prompt) based on load timing, compaction behavior, context cost, and authority.
---

## Instructions

Use this skill when you are configuring Claude Code and want a consistent way to choose *where* an instruction should live.

1. Classify the instruction:
   - Project facts that should always be in context → CLAUDE.md (root)
   - Team or folder-specific conventions → CLAUDE.md (subdirectory) or path-scoped rules
   - Specific constraints that must hold reliably → rules (prefer path-scoped)
   - A repeatable procedure (runbook/checklist) → skill
   - A side task that should run in isolation and return only a summary → subagent
   - Deterministic automation or enforcement on lifecycle events → hook
   - A major, persistent change in role or tone → output style
   - One-off additive instructions for a single invocation → append-system-prompt

2. Check tradeoffs:
   - If always-on instructions are growing, reduce context cost by using path scoping or skills.
   - If you need deterministic enforcement, prefer hooks/permissions over prompts.
   - If you don’t want intermediate results cluttering the main thread, use subagents.

## Examples

- If you wrote a 30-line deployment procedure in CLAUDE.md, move it into a skill.
- If a rule only applies to `src/api/**`, add `paths:` frontmatter so it loads only when relevant.
- If you need to block a dangerous tool call reliably, use a PreToolUse hook and exit code 2.

See: references/methods-table.md
See: examples/rules-paths-frontmatter.md
