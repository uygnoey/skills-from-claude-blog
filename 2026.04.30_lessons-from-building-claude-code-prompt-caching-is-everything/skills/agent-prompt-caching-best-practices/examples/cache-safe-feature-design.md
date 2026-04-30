# Cache-safe feature design

These are the concrete design patterns the April 30, 2026 post by Thariq Shihipar walks through. They are kept here so the SKILL can reference them without expanding inline.

## Pattern 1 — State transitions modeled as tools (Plan Mode)

The naive design (which the post warns against): when the user enters Plan Mode, swap the toolset to only read-only tools. This invalidates the cache for the entire conversation because tools are part of the cached prefix.

The Claude Code design:

- Keep *all* tools in the request at all times.
- Add `EnterPlanMode` and `ExitPlanMode` as tools themselves.
- When the user toggles Plan Mode on, inject a system message explaining the new mode and rules: "explore the codebase, don't edit files, and call ExitPlanMode when the plan is complete."
- Tool definitions never change.

Bonus property the post calls out: because `EnterPlanMode` is a tool the model can call itself, it can autonomously enter plan mode when it detects a hard problem, with no cache break.

Apply this pattern any time you have a feature that "feels like" it should hide tools. Model the mode itself as a tool call instead.

## Pattern 2 — Defer tool loading instead of removing tools

The setup: Claude Code can have dozens of MCP tools loaded. Including every full schema on every request is expensive. Removing tools mid-conversation would break the cache.

The Claude Code design:

- Send lightweight stubs for each tool — just the tool name, with `defer_loading: true`.
- The model can "discover" each tool via the tool search tool when needed.
- The full tool schema loads only when the model selects that tool.
- The same stubs appear in the same order on every request, so the cached prefix stays stable.

The post also notes that the tool search tool is available through the API to simplify this for your own applications.

Apply this pattern any time the temptation is to "only include the tools the model needs right now." That instinct breaks caching; defer instead.

## Pattern 3 — Compaction as cache-safe forking

The naive design (which the post warns against): when context is full, run a separate API call with a "summarize this" system prompt and no tools. The new request shares no prefix with the parent, so none of the cache applies and you pay the full uncached input rate for the entire conversation. The longer the conversation, the worse this gets.

The Claude Code design:

- Use the *exact same* system prompt, user context, system context, and tool definitions as the parent conversation.
- Prepend the parent's conversation messages.
- Append the compaction prompt as a new user message at the end.
- Reserve a "compaction buffer" inside the context window so there is room for the compaction prompt and the summary output tokens.

From the API's perspective, this looks like a continuation of the parent's last request, so the cached prefix is reused. Only the compaction prompt itself is new tokens.

The post notes that you do not need to re-implement this yourself: compaction is built directly into the API, with these patterns applied for you.

## Pattern 4 — `<system-reminder>` for dynamic info

When something inside the prefix would otherwise become out of date — current time, a file the user just edited — do not edit the system prompt. The post's pattern in Claude Code:

- Add a `<system-reminder>` tag in the next user message or tool result with the updated information for the model.
- The static system prompt stays untouched.

Apply this every time you are tempted to "just update the system prompt" with a small dynamic value.

## Pattern 5 — Cross-model hand-off via subagents

When you really do need a cheaper model for a sub-task, do not switch models mid-session in the same conversation. Per the post:

- Deploy a subagent that prompts the parent model (e.g., Opus) to prepare a hand-off message to the cheaper model.
- Run the cheaper model only inside that subagent.
- Claude Code does this with the Explore agents, which use Haiku.

This keeps the parent conversation's prefix cached on its own model and isolates the cheaper-model call to its own context.

## Source

Lessons from building Claude Code: Prompt caching is everything — Anthropic (Thariq Shihipar), April 30, 2026: <https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything>
