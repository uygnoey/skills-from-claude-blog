---
name: large-codebase-rollout
description: Best-practice playbook for making Claude Code reliable in large repositories by building a harness (CLAUDE.md layering, hooks, skills, plugins, MCP, LSP) and establishing ownership.
---

## Instructions

Use this skill when you need to introduce or scale Claude Code in a large codebase (monorepo or enterprise repo).

1. **Start with navigability**
   - Prefer starting sessions from the relevant subdirectory instead of the repo root.
   - Keep a lean root `CLAUDE.md` with global conventions.
   - Add subdirectory `CLAUDE.md` files for local conventions.

2. **Treat the harness as first-class**
   - Prioritize extension points in a layered order: `CLAUDE.md` → hooks → skills → plugins → MCP servers.
   - Add LSP integrations to improve symbol-level navigation (especially for C/C++ and multi-language repos).
   - Use subagents to split exploration (mapping) from editing.

3. **Use the right tool for the job**
   - Deterministic checks (format/lint/test) should be done with hooks/scripts, not with prose reminders.
   - Put specialized workflows into skills so they don’t bloat every session.

4. **Maintain configuration as models evolve**
   - Review `CLAUDE.md`, hooks, and skills every 3–6 months.
   - Revisit anything created to compensate for older model limitations.

5. **Define ownership & governance**
   - Assign a DRI (or an agent manager function) for Claude Code configuration, permissions policy, and plugin governance.
   - Establish cross-functional alignment early (engineering + infosec + governance).

## Examples

- You are rolling Claude Code out to a monorepo with many teams: use the checklist in [examples/rollout-checklist.md](./examples/rollout-checklist.md).
- You are hitting navigation errors in a typed multi-language codebase: prioritize LSP integration and document it in your root `CLAUDE.md`.

## Bundled resources

- [examples/rollout-checklist.md](./examples/rollout-checklist.md)
- [references/harness-components.md](./references/harness-components.md)
