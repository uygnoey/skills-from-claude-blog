# What ends up in the context, and how long it stays

The second variable behind a session's cost is volume: how much the session sends on each
turn. The key fact is that nothing is sent once. Everything read or run is re-sent on
every turn for the rest of the session — cheaply, because it is cached, but it is still
there and still occupying context.

## What is already loaded before you type

Run `/context` in a fresh session to see it. Typically:

- **Tool definitions**, including every connected MCP server's tools.
- **The system prompt.**
- **`CLAUDE.md`.**
- **Startup items** loaded by your configuration.

This is the standing load. It is paid on every turn of the session, so it is worth
auditing once rather than never.

Two ways to shrink it:

- **Keep `CLAUDE.md` specific.** Workflow instructions belong in skills, which load only
  when they are actually used. A `CLAUDE.md` that documents every workflow is a file you
  pay for continuously in exchange for the small fraction relevant to today's task.
- **Disable MCP servers you are not using** with `/mcp`. Their tool definitions leave the
  standing load with them.

## What gets added while you work

### File reads

The specificity of the request determines how much gets pulled in.

| Request | What happens |
|---|---|
| "The tests are failing" | Grep across the repo, then a spread of reads |
| "Fix the failing test in `utils.test.ts`" | One Read call |
| "Fix the failing test in `@utils.test.ts`" | No Read call — the file is attached before the message is sent |

`@`-mention is the cheapest form because it skips the tool call entirely. The file itself
occupies the same context space either way, so the saving is the round trip, not the
content. Mention a file once per conversation; mentioning it again attaches a second copy.

### Command output

Command output is appended to the conversation just like a file read, and stays for the
rest of the session. A test runner in its default verbose mode can deposit hundreds of
lines that get re-sent on every subsequent turn.

Output over roughly 30,000 characters is written to a file, with a preview left inline —
`BASH_MAX_OUTPUT_LENGTH` controls that threshold. That protects you from the extreme case
but not from the steady accumulation of moderately noisy commands.

The fix is quiet flags, recorded once in `CLAUDE.md` so they are used consistently. Or
run the noisy job in a subagent, where the output never reaches your conversation.

## How long it stays

Everything above persists for the life of the session. Turn 40 re-sends the thirty-nine
turns before it. This produces the single most important structural fact about cost: one
long session is more expensive than the same work split across several short ones.

The three controls, and when each is right:

| Control | Use when | Cost |
|---|---|---|
| `/clear` | Starting an unrelated task | Free — the next turn starts clean |
| `/compact` | A chunk of work is done but you need what it established | Always costs; cheaper while the cache is warm |
| `/rewind` | Backing out of a wrong path | Free — trims the end, cache intact |

Practical notes:

- `/rename` before `/clear` if you might want to come back to the session.
- With `/compact`, say what to keep. If the answer is consistent across sessions, put a
  compact-instructions section in `CLAUDE.md` instead of retyping it.
- On a 1M-context model, `/autocompact 200k` restores the auto-compact safety net
  (requires Claude Code v2.1.221+).
- Compact **before** a keyboard break, not after. Summarizing while the conversation is
  still cached avoids paying a full re-prefill first.

## Background turns

`/loop` fires as a full turn inside the session that started it, carrying that session's
entire conversation each time. If more than an hour separates firings, each one also
misses the cache. Start loops in a fresh session in another terminal so they do not drag
your working conversation along.

## Subagents

A subagent gets its own context: system prompt, tools, `CLAUDE.md` — but **not** your
conversation. It takes its own turns, and only its final answer returns to the main
session. Everything it read and everything it ran is discarded.

The trade-off in both directions:

- **Cost:** it may re-read material your main session already holds, and it pays for its
  own turns.
- **Benefit:** none of the volume it generated lands in your conversation.

That makes subagents clearly worthwhile for jobs that produce a lot of output you do not
need to keep — trawling logs and traces is the archetype. The main session receives only
the report the subagent chose to write.

For a noisy job you delegate repeatedly, define the subagent pinned to a smaller model. A
subagent without a model set runs on the main session's model.

## Priority order

Where to look first, roughly by impact:

1. **Session length** — how much conversation is being re-sent each turn.
2. **Command output size** — how much noise is accumulating in it.
3. **Files read** — how precisely you are pointing at what you need.
4. **Model and effort** — chosen deliberately at the start, and not switched mid-session.

## Source

- https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions (August 14, 2026)
