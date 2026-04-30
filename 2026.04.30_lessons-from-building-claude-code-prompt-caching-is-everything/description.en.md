**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Lessons from building Claude Code: Prompt caching is everything

## What is this post?

Anthropic's April 30, 2026 post by Thariq Shihipar (member of technical staff on the Claude Code team) shares the prompt-caching lessons the Claude Code team built into the harness. It explains how prefix matching works, the order Claude Code uses for static and dynamic content, why ad-hoc updates to the system prompt break caching, why mid-session model and tool changes are dangerous, how Plan Mode and tool search avoid invalidating the cache, and how compaction is implemented as cache-safe forking. The post finishes with five reusable patterns for any agent builder.

## When useful

- You are building or operating a long-running agent and your goal is to keep the prompt cache hit rate high.
- You are debugging a regression where cache hits dropped after a code change (timestamps, tool order, parameter tweaks, etc.).
- You are designing a feature like Plan Mode that "feels" like it should swap out the toolset, and you need a cache-safe alternative.
- You are implementing compaction or summarization and want it to share the parent's cached prefix instead of paying full uncached input rates.
- You are looking for an SLO/alerting model around cache hit rate.

## Key points

- Prompt caching is a prefix match — anything that changes inside the prefix invalidates everything after it.
- Claude Code's harness layout: static system prompt + tools (globally cached) → CLAUDE.md (cached within a project) → session context (cached within a session) → conversation messages.
- Common ways cache ordering breaks: timestamps in the static system prompt, non-deterministic tool ordering, changing tool parameters.
- For dynamic info (current time, file changes), use messages — Claude Code adds a `<system-reminder>` tag in the next user message or tool result instead of editing the system prompt.
- Don't change models mid-session. Switching from Opus to Haiku at 100k tokens forces a fresh cache build for Haiku and is more expensive than letting Opus answer. If you must switch, use a subagent that prepares a hand-off message — Claude Code does this for Explore agents on Haiku.
- Never add or remove tools mid-session. Plan Mode keeps every tool in place and uses EnterPlanMode / ExitPlanMode as tools themselves. Tool search uses `defer_loading: true` stubs instead of removing tools.
- Compaction is implemented as cache-safe forking: identical system prompt, user/system context, and tools as the parent, with the compaction prompt appended as a new user message. A "compaction buffer" is reserved in the context window for the summary. Compaction is now built into the API.
- The team monitors cache hit rate like uptime and declares SEVs when it drops too low.

## Bundled resources

- Skill: `skills/agent-prompt-caching-best-practices/SKILL.md` — the actionable rules and design patterns for keeping the prefix stable, encoded as a checklist.
- Reference: `skills/agent-prompt-caching-best-practices/references/lessons-from-claude-code.md` — verbatim lessons from the post (lay out for caching, use messages for updates, model and tool stability, cache-safe forking, the five summary patterns).
- Examples: `skills/agent-prompt-caching-best-practices/examples/cache-safe-feature-design.md` — concrete examples adapted from the post (Plan Mode as tools, defer_loading for tool search, compaction as cache-safe forking).

## Source

Lessons from building Claude Code: Prompt caching is everything — Anthropic (Thariq Shihipar), April 30, 2026: <https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything>
