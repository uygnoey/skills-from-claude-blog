**English** · [한국어](./session-cost-optimization.ko.md) · [Español](./session-cost-optimization.es.md) · [日本語](./session-cost-optimization.ja.md)

# Getting more out of each Claude Code session

Agentic coding tools bill per token rather than per seat, which means the same task can
cost very different amounts depending on how the session was run. One session reads the
test file and the implementation and fixes the bug. Another greps the repo first, opens a
dozen files, and then carries all of them — plus everything read earlier that morning —
into every remaining turn.

The framing to hold onto, from the post's author Lydia Hallie: being efficient with tokens
does not mean using fewer of them overall. It means making sure the ones you do use go
toward the thing you actually asked for.

Two variables set the bill: what a token costs, and how many tokens the session sends.

## Part 1 — What a token costs

### Model

Larger models do more work on both input and output tokens and are priced accordingly.
Match the model to the problem — a larger one for genuinely hard or ambiguous work, a
smaller one for routine changes.

### Input versus output

Every turn has two phases. In **prefill**, the model reads what it has been given: the
system prompt, tool definitions, `CLAUDE.md`, the conversation so far, your new message.
Those are input tokens. In **decode**, it writes its response one token at a time — output
tokens, priced at roughly 5× input.

Thinking tokens are output tokens, so the effort level is a direct dial on the expensive
half. Worth doing in a fresh session: run `/model` and `/effort` and confirm both. They
persist from your last session, so what is in force may not be what you intended. If you
want no thinking at all for a session, `MAX_THINKING_TOKENS=0` steps below `/effort low`
(it does not apply to Fable 5).

### Prompt caching

Caching is what makes long conversations affordable. A cache read costs about 0.1× the
input price; a cache write costs up to 2×, paid once per token. Write once, read cheaply
on every turn afterward.

Which makes cache invalidation the expensive event:

| Trigger | Effect |
|---|---|
| `/model` | Different model, different cache — full re-prefill |
| `/effort` | Part of the cache key — full re-prefill |
| Fast mode | Also part of the cache key |
| `/compact` | Replaces the conversation; the system prompt survives |
| Time | Expires after 1 hour on a subscription, 5 minutes on an API key (`ENABLE_PROMPT_CACHING_1H=1` extends the API-key case) |
| Resuming | Usually expired; the system prompt is rebuilt at launch |

The exception worth knowing: `/rewind` costs nothing. It cuts turns off the end and leaves
everything before the cut cached. `/compact` rewrites the conversation and always costs
something — which is why the advice is to compact *before* a break, while things are still
warm, rather than after the cache has expired.

## Part 2 — How many tokens the session sends

Nothing is sent once. Every file read and every command output is re-sent on every turn
for the rest of the session. Cached, so cheap — but present, and occupying context.

### What is loaded before you type

Run `/context` in a fresh session and you will see the standing load: tool definitions
from each connected MCP server, the system prompt, `CLAUDE.md`, startup items. All of it
is paid for on every turn.

Two ways to shrink it. Keep `CLAUDE.md` specific and move workflow instructions into
skills, which load only when used. And disable MCP servers you are not using with `/mcp`.

### What gets added as you work

**Files.** How you ask determines how much comes in. "The tests are failing" produces a
grep and a spread of reads. Naming the file gives you one Read. `@`-mentioning it gives
you none — Claude Code attaches the file before the message is sent. The file takes the
same space either way; the saving is the round trip. Mention it once per conversation, as
re-mentioning attaches another copy.

**Command output.** Appended just like a file, and it stays. A verbose test runner can
deposit hundreds of lines that are then re-sent all day. Output above roughly 30,000
characters is written to a file with a preview inline (`BASH_MAX_OUTPUT_LENGTH` sets the
threshold), which handles the extreme case but not steady accumulation.

The fix is to put the two or three commands you run all day into `CLAUDE.md`, quiet flags
included, written the way you would type them — for example running a single test file
with `--reporter=dot`. You save the turn spent deriving the invocation and the output that
would otherwise sit in context for the rest of the session.

### How long it stays

Turn 40 re-sends the thirty-nine turns before it. So one long session costs more than the
same work split into short ones.

- `/clear` when starting a new task. `/rename` first if you might want it back.
- `/compact` when a piece of work is done but you need what it established. Say what to
  keep; if the answer is always the same, put a compact-instructions section in
  `CLAUDE.md`.
- On a 1M-context model, `/autocompact 200k` restores the auto-compact safety net
  (Claude Code v2.1.221+).

One trap: `/loop` fires as a full turn inside the session that started it, carrying the
whole conversation each time — and if more than an hour separates firings, each one is
also a cache miss. Start loops in a fresh session in another terminal.

### Subagents

A subagent gets its own context — system prompt, tools, `CLAUDE.md` — but not your
conversation. It takes its own turns, and only its answer comes back. Everything else is
discarded.

The trade is real in both directions: it may re-read things your main session already
holds, and it pays for its own turns. It earns its keep when a job produces a lot of
output you do not need, log analysis being the clearest case — you get the report, not the
log. For a noisy job you delegate repeatedly, define the subagent with a smaller model
pinned in its configuration; otherwise it runs on the main session's model.

## Where to look first

Roughly by impact:

1. **Session length** — how much conversation is re-sent each turn.
2. **Command output size** — how much noise accumulates in it.
3. **Files read** — how precisely you point at what you need.
4. **Model and effort** — set deliberately at the start, and not switched mid-session.

The first two usually matter more than the last.

## Bundled artifacts

- The `token-efficient-sessions` skill in this post folder — the same material as an
  actionable skill, with pricing and context-lifecycle references, `CLAUDE.md` snippets,
  and before/after session patterns.

## Source

- https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions (August 14, 2026)
