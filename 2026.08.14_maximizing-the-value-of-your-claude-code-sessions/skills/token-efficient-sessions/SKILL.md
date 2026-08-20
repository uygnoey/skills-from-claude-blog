---
name: token-efficient-sessions
description: Get more out of each Claude Code session by controlling what enters the context, how long it stays there, and what breaks the prompt cache. Use when sessions feel expensive, when a long conversation is dragging unrelated files into every turn, when deciding between /clear, /compact, and /rewind, when choosing model and effort, when tool output or MCP definitions are crowding the context, or when working out whether a job belongs in a subagent. Efficiency here means spending tokens on the task you actually asked for, not spending fewer tokens overall.
---

# Token-efficient Claude Code sessions

Agentic coding tools bill per token, so the same task can cost very different amounts
depending on how the session is run. The goal is not frugality — it is making sure the
tokens you spend go toward the thing you actually asked for, rather than re-sending
this morning's unrelated reading on every turn.

Two variables set the bill: **what a token costs**, and **how many tokens the session
sends**. Full mechanics live in
[references/token-pricing.md](references/token-pricing.md) and
[references/context-lifecycle.md](references/context-lifecycle.md).

## Instructions

### Start of session — set it once, then leave it alone

1. Run `/model` and `/effort` in a fresh session and confirm both. They persist from the
   previous session, so the settings you are on may not be the ones you meant. Changing
   either mid-conversation is a cache key change: the whole conversation re-prefills at
   full price.
2. Pick the model by problem, not by habit — a larger model for genuinely hard or
   ambiguous work, a smaller one for routine edits.
3. Run `/context` once to see what is loaded before you have typed anything: tool
   definitions, the system prompt, `CLAUDE.md`, and any startup items. Anything sitting
   there is paid for on every turn of the session.

### Keep the standing load small

- Keep `CLAUDE.md` specific. Move workflow instructions into skills, which load only when
  used, instead of leaving them resident.
- Disable MCP servers you are not using with `/mcp`. Tool definitions are part of the
  standing load.
- Put the two or three commands you run all day into `CLAUDE.md` with their quiet flags,
  written the way you would type them. See
  [templates/claude-md-snippets.md](templates/claude-md-snippets.md).

### Control what gets added mid-session

- **Point at the file.** A vague request ("the tests are failing") triggers a grep and a
  spread of reads. Naming the file cuts that to one read. `@`-mentioning it removes even
  that: the file is attached before the message is sent, with no Read call at all.
  Mention it once per conversation — re-mentioning attaches another copy.
- **Quiet your commands.** Command output is appended to the conversation exactly like a
  file read, and stays for the rest of the session. Add reporter/quiet flags, or run the
  noisy job in a subagent. Very large outputs are written to a file with a preview left
  inline (`BASH_MAX_OUTPUT_LENGTH` controls the threshold).

### Control how long it stays

Everything read or run is re-sent on every subsequent turn. Turn 40 pays for the
thirty-nine turns before it, cached but still occupying context. So one long session
costs more than the same work split into short ones.

- `/clear` when you move to a new task. `/rename` first if you may want the session back.
- `/compact` when a chunk of work is finished but you need what it established. Say what
  to keep; if the answer is always the same, put a compact-instructions section in
  `CLAUDE.md`.
- `/rewind` is the cheap one — it trims from the end and leaves the cache intact.
  `/compact` rewrites the conversation and always costs something.
- Compact **before** a long break rather than after. The cache expires after an hour on a
  subscription (five minutes on an API key), and summarizing while still cached is
  cheaper than paying a full re-prefill first.
- On a 1M-context model, `/autocompact 200k` restores the auto-compact safety net
  (Claude Code v2.1.221+).

### Watch background turns

`/loop` fires as a full turn inside the session that started it, carrying the entire
conversation each time. If more than an hour passes between firings, each one is also a
cache miss. Run loops from a fresh session in another terminal.

### Push noisy jobs into subagents

A subagent gets its own context — system prompt, tools, `CLAUDE.md` — but not your
conversation, and only its final answer comes back. Everything it read or ran is
discarded. That is the right trade whenever a job produces a lot of output you do not
need to keep, log and trace analysis being the clearest case. The cost is that it may
re-read things your main session already has, and it pays for its own turns. For a noisy
job you hand off repeatedly, define a subagent pinned to a smaller model; otherwise it
runs on the main session's model.

### Where to look first

In rough order of impact: **session length**, then **command output size**, then **files
read**, then **model and effort** (and not switching them mid-session). Fixing the first
two usually matters more than tuning the last.

## Examples

**A test is failing and you know which one.**
Instead of "the tests are failing," write `Fix the failing test in @utils.test.ts`. The
file is attached directly — no grep, no Read call, no collateral files pulled in.
Side-by-side versions of this and other patterns are in
[examples/session-patterns.md](examples/session-patterns.md).

**Your test runner prints hundreds of lines per run.**
Add `run a single test file with npx vitest run <file> --reporter=dot` to `CLAUDE.md`. You
save the turn spent working out the invocation and the hundreds of lines that would
otherwise sit in context for the rest of the day.

**Finished a feature, moving to an unrelated bug.**
`/clear`. Continuing in the same session means the bug work pays to re-send the feature
work on every turn. If you might come back, `/rename` first.

**Finished a piece of a task but need what it established.**
`/compact`, and say what to keep — the API shape you settled on, the file you are editing,
the decision you made. Do it before you step away, while the cache is still warm.

**You need to trawl a large log for one error.**
Hand it to a subagent. It reads the whole thing in its own context and returns the
finding; the log never enters your conversation.

**You want to change model or effort halfway through.**
Expect to re-prefill the whole conversation at full price. If the change is worth it, do
it — but a better habit is confirming both at the start of a fresh session.

## Source

- https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions (August 14, 2026)
