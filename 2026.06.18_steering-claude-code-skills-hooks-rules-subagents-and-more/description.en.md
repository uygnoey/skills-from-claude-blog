**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Steering Claude Code: skills, hooks, subagents and more

## What is this post?

This post explains the main methods for steering Claude Code behavior and provides a decision framework for choosing where instructions should live.

## When is it useful?

Use it when you are customizing Claude Code and need to balance context cost, persistence across long sessions (compaction), and instruction authority.

## Key points

- Seven methods are covered: CLAUDE.md files, rules, skills, subagents, hooks, output styles, and appending the system prompt.
- Each method differs in when it loads, how it behaves under compaction, and its context cost.
- Guidance: keep root CLAUDE.md concise (<200 lines) and push procedures into skills and constraints into (path-scoped) rules.
- Use subagents for isolated side tasks whose intermediate work should not clutter the main thread.
- Use hooks for deterministic automation and enforcement (e.g., PreToolUse can deny tool calls by exiting with code 2).
- Use output styles only for significant role changes; consider built-in styles before writing custom ones.
- Once you have several methods configured, you can bundle them as a plugin to share a coherent setup.

## Bundled resources

- Comparison table of methods and tradeoffs
- Examples: path-scoped rule frontmatter; subdirectory CLAUDE.md loading behavior
- Lists of hook types and lifecycle events (PreCompact, PreToolUse)

## Source

- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
