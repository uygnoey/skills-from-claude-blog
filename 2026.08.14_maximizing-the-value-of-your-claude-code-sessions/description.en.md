**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A practical guide by Lydia Hallie on why two Claude Code sessions doing the same task can cost very different amounts, and what you control. Agentic coding tools bill per token rather than per seat, so the question is not how to use fewer tokens — it is how to keep the ones you spend pointed at the task you actually asked for, instead of re-sending unrelated files and command output on every turn.

It breaks the problem into two variables: what a token costs (model, input versus output, prompt caching) and how many tokens the session sends (what enters the context and how long it stays there), and closes with a rough priority order for where to look first.

## When is it useful?
- When sessions feel expensive and it is not obvious where the spend is going.
- When a long conversation is dragging this morning's unrelated reading into every turn.
- When deciding between `/clear`, `/compact`, and `/rewind`.
- When tool definitions from connected MCP servers, or a sprawling `CLAUDE.md`, are crowding the context before you have typed anything.
- When working out whether a noisy job — log trawling, trace analysis — belongs in a subagent.
- When onboarding a team onto agentic coding and you want the habits set early.

## Key points
- **Output tokens cost roughly 5× input tokens**, and thinking tokens are output tokens — so effort level is a direct dial on the expensive half. `MAX_THINKING_TOKENS=0` steps below `/effort low` for a session (not applicable to Fable 5).
- **Cached reads cost about 0.1× input; a cache write costs up to 2×, once per token.** Preserving the cache dominates most other optimizations.
- **What breaks the cache:** `/model`, `/effort`, and fast mode are all part of the cache key and force a full re-prefill; `/compact` replaces the conversation (the system prompt survives); the cache expires after 1 hour on a subscription and 5 minutes on an API key, with `ENABLE_PROMPT_CACHING_1H=1` extending the latter.
- **`/rewind` is free** — it trims the end and leaves the cache intact. `/compact` always costs something, which is why you should compact *before* a break rather than after the cache has expired.
- **Set `/model` and `/effort` once in a fresh session.** Both persist from the previous session, so what is in force may not be what you meant.
- **Nothing is sent once.** Every file read and command output is re-sent on every subsequent turn — cached and cheap, but occupying context. Turn 40 pays for the thirty-nine before it, which is why one long session costs more than the same work split up.
- **Run `/context` once** to see the standing load: tool definitions, system prompt, `CLAUDE.md`, startup items. Keep `CLAUDE.md` specific, move workflow instructions into skills (loaded only when used), and disable unused MCP servers with `/mcp`.
- **Point at the file.** A vague request triggers a grep and a spread of reads; naming the file gives one Read; `@`-mentioning it gives none, since the file is attached before the message is sent. Mention once per conversation — re-mentioning attaches another copy.
- **Quiet your commands.** Output is appended like a file read and stays for the session. Put the two or three commands you run all day into `CLAUDE.md` with their quiet flags. Output above roughly 30,000 characters is written to a file with a preview inline (`BASH_MAX_OUTPUT_LENGTH`).
- **`/loop` fires as a full turn in the session that started it**, carrying the whole conversation each time — and misses the cache if more than an hour passes between firings. Run loops from a fresh session in another terminal.
- **Subagents get their own context but not your conversation**, and only their answer comes back. Worth it when a job produces a lot of output you do not need; pin a smaller model in the subagent's configuration for noisy jobs you delegate repeatedly.
- **Where to look first**, roughly by impact: session length, then command output size, then files read, then model and effort.
- On a 1M-context model, `/autocompact 200k` restores the auto-compact safety net (Claude Code v2.1.221+).

## Bundled resources
- `skills/token-efficient-sessions/SKILL.md` — the practices as an actionable skill.
- `skills/token-efficient-sessions/references/token-pricing.md` — model, input/output, and the full cache-invalidation table.
- `skills/token-efficient-sessions/references/context-lifecycle.md` — what enters the context, how long it stays, and the `/clear` vs `/compact` vs `/rewind` decision.
- `skills/token-efficient-sessions/templates/claude-md-snippets.md` — everyday-commands and compact-instructions sections to paste into `CLAUDE.md`.
- `skills/token-efficient-sessions/examples/session-patterns.md` — eight before/after pairs.
- `guides/session-cost-optimization.{en,ko,es,ja}.md` — the same material as a four-language guide.

## Source
- https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions (August 14, 2026)
