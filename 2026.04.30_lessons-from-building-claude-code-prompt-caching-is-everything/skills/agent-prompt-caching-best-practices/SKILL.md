---
name: agent-prompt-caching-best-practices
description: Keep prompt cache hit rate high in long-running agents by following the patterns Claude Code's team uses — lay out static-then-dynamic, push updates into messages instead of editing the system prompt, never change models or tools mid-session, model state transitions as tools (Plan Mode), defer tool loading instead of removing tools, and implement compaction as cache-safe forking. Treat cache breaks as incidents.
---

# Agent prompt caching best practices

The April 30, 2026 post from Thariq Shihipar (Claude Code team) shares the prompt-caching playbook the Claude Code harness is built around. This skill turns it into a checklist and design-pattern catalogue you can apply to any Claude-based agent.

## Instructions

### 1. Lay out the prompt static-first, dynamic-last

Per the post, prompt caching works by prefix matching, "everything from the start of the request up to each cache_control breakpoint." Anything that changes inside the prefix invalidates everything after it.

Claude Code's harness ordering:

1. Static system prompt + tools — globally cached.
2. CLAUDE.md — cached within a project.
3. Session context — cached within a session.
4. Conversation messages.

Apply this layout to your own agent. Maximize how many sessions share a prefix.

The verbatim ordering and the ways the team has previously broken it are in [references/lessons-from-claude-code.md](./references/lessons-from-claude-code.md).

### 2. Avoid the four ordering traps the post calls out

The post explicitly names ways it has broken the ordering:

- Putting an in-depth timestamp in the static system prompt.
- Shuffling tool order definitions non-deterministically.
- Updating parameters of tools (e.g., what agents the Agent tool can call).
- (Implied) any other "static" content that turns out to vary per request.

Audit your prefix for each of these before shipping a change.

### 3. Push dynamic updates into messages, not the system prompt

When the value of something inside the prefix changes — current time, a file the user just edited — do not edit the system prompt. Per the post:

> "Consider if you can pass in this information via messages in the agent's next turn instead. In Claude Code, we add a `<system-reminder>` tag in the next user message or tool result with the updated information for the model, which helps preserve the cache."

Adopt the same pattern in your agent: use a tagged message rather than rebuilding the prefix.

### 4. Don't change models mid-session — use a subagent for hand-offs

Per the post:

> "Prompt caches are unique to models and this can make the math of prompt caching quite unintuitive."
>
> "If you're 100k tokens into a conversation with Opus and want to ask a question that is fairly easy to answer, it would actually be more expensive to switch to Haiku than to have Opus answer, because we would need to rebuild the prompt cache for Haiku."

If you must use a cheaper model, deploy a subagent that prepares a hand-off message — the post notes Claude Code does this with Explore agents on Haiku.

### 5. Never add or remove tools mid-session

Tools are part of the cached prefix. Adding or removing one invalidates the cache for the entire conversation. Apply two patterns:

- **Model state transitions as tools.** Plan Mode keeps every tool in place and exposes EnterPlanMode and ExitPlanMode as tools themselves. The tool definitions never change — toggling Plan Mode only adds a system message describing the new mode. Bonus: the model can call EnterPlanMode itself when it detects a hard problem, with no cache break.
- **Defer tool loading instead of removing tools.** Tool search sends lightweight stubs (just the tool name, with `defer_loading: true`) that the model can discover when needed. Full tool schemas load only when the model selects them. Same stubs, same order, every request.

Concrete versions of both patterns are in [examples/cache-safe-feature-design.md](./examples/cache-safe-feature-design.md).

### 6. Implement compaction as cache-safe forking

The naive way — a separate API call with a different system prompt and no tools — pays the full uncached input rate for the entire conversation, which gets worse the more you need compaction.

Per the post, the cache-safe approach is:

- Use the **exact same** system prompt, user context, system context, and tool definitions as the parent conversation.
- Prepend the parent's conversation messages.
- Append the compaction prompt as a new user message at the end.

Reserve a "compaction buffer" in the context window so you have room for the compaction prompt and the summary tokens. The post notes that compaction is now built into the API, so you can use it directly without re-deriving these patterns yourself.

### 7. Monitor cache hit rate like uptime

The post is explicit about the operational discipline:

> "We run alerts on our prompt cache hit rate and declare SEVs if they're too low."

Apply the same discipline:

- Define a target cache hit rate.
- Alert on drops.
- Treat sustained drops as incidents — find the prefix change that caused them.

### 8. Apply the five-summary checklist to every agent change

The post closes with five reusable patterns. Run through them on every change to the prefix or agent harness:

1. Prompt caching is a prefix match — any change anywhere in the prefix invalidates everything after.
2. Use messages instead of system prompt changes.
3. Don't change tools or models mid-conversation. Use tools to model state transitions; defer tool loading instead of removing tools.
4. Monitor your cache hit rate like you monitor uptime.
5. Fork operations need to share the parent's prefix.

The verbatim list is in [references/lessons-from-claude-code.md](./references/lessons-from-claude-code.md).

## Examples

### Example A: Adding a "current time" feature without breaking the cache

Wrong: edit the static system prompt to include the current timestamp on every request. This breaks the cache on every call.

Right: keep the static system prompt timestamp-free. When the agent needs the current time, inject a `<system-reminder>` tag with the time in the next user message or tool result. The prefix stays stable; only the message content varies.

### Example B: A "read-only mode" feature for an agent

Wrong: when the user enables read-only mode, swap the toolset to only read tools. Cache invalidated.

Right: keep all tools in place. Add EnterReadOnlyMode and ExitReadOnlyMode as tools themselves. Toggling read-only mode injects a system message describing the rules; the tool definitions stay frozen. Same pattern as Plan Mode in the post.

### Example C: Loading dozens of MCP tools

Wrong: include all schemas in every request. Expensive. Wrong-er: remove tools mid-conversation. Cache invalidated.

Right: send lightweight stubs with `defer_loading: true` for each tool. Full schemas load only when the model selects them. Same stubs, same order, every request — prefix stays stable.

### Example D: Compacting a long-running session

Wrong: separate API call with "summarize this" system prompt and no tools. Pays full uncached input rate for the whole conversation.

Right: cache-safe forking — same system prompt, same user/system context, same tool definitions as the parent. Append the compaction prompt as a new user message. Reserve a compaction buffer so the summary fits.

## Source

Lessons from building Claude Code: Prompt caching is everything — Anthropic (Thariq Shihipar), April 30, 2026: <https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything>
