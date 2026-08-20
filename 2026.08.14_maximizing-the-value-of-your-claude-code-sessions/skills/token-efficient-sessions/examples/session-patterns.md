# Session patterns, side by side

Each pair shows the same work done two ways. The difference is never how much Claude has
to think — it is how much unrelated material gets dragged into every subsequent turn.

---

## Pattern 1 — Point at the file

**Wasteful**

```
> the tests are failing
```

Claude greps the repo, finds candidate files, reads a dozen of them. Every one of those
files stays in the conversation and is re-sent on every turn for the rest of the session.

**Better**

```
> Fix the failing test in utils.test.ts
```

One Read call. One file in context.

**Best**

```
> Fix the failing test in @utils.test.ts
```

No Read call at all — the file is attached before the message is sent. The file occupies
the same context space either way; what you save is the round trip.

> Mention a file once per conversation. Mentioning it again attaches a second copy.

---

## Pattern 2 — Quiet the commands you run all day

**Wasteful**

```
> run the tests
```

The default reporter prints a line per test plus a summary block. Several hundred lines
land in the conversation and get re-sent from then on. Repeat that eight times across a
session and a meaningful share of the context is test-runner narration.

**Better** — one line in `CLAUDE.md`:

```markdown
- Run a single test file: `npx vitest run <file> --reporter=dot`
```

Now the invocation is known without a turn spent deriving it, and each run deposits a
handful of characters instead of a screen.

---

## Pattern 3 — One long session versus several short ones

**Wasteful**

A single session running from morning to evening: a feature, then an unrelated bug, then a
dependency bump, then a README fix. By the fortieth turn every message re-sends
thirty-nine turns of unrelated history.

**Better**

```
> /rename feature-auth-redirect
> /clear
```

`/clear` between tasks. `/rename` first when the session may be worth returning to. The
bug work no longer pays for the feature work.

---

## Pattern 4 — Compact versus clear versus rewind

| Situation | Do this | Why |
|---|---|---|
| Moving to an unrelated task | `/clear` | Nothing from before is needed |
| A chunk of work is done but its conclusions matter | `/compact` | Keeps the decisions, drops the exploration |
| Went down a wrong path | `/rewind` | Free — trims the end, leaves the cache intact |
| About to step away for an hour | `/compact` **now** | Summarizing while cached beats re-prefilling later |

When compacting, say what to keep:

```
> /compact keep the schema we settled on, the file I'm editing, and the failing test names
```

If that instruction is the same every time, move it into `CLAUDE.md` as a compact-instructions
section instead of retyping it.

---

## Pattern 5 — Send the noisy job elsewhere

**Wasteful**

```
> read deploy.log and find why the rollout failed
```

The whole log enters the conversation and is re-sent on every turn afterward, long after
the answer has been found.

**Better**

Delegate it to a subagent. It reads the log in its own context, takes its own turns, and
returns only its conclusion. Everything else is discarded when it finishes.

For a job you hand off repeatedly, define the subagent with a smaller model pinned in its
configuration — a subagent with no model set runs on the main session's model.

---

## Pattern 6 — Loops belong in their own session

**Wasteful**

Starting `/loop` inside your working session. Each firing is a full turn carrying the
entire conversation, and any gap longer than an hour also misses the cache.

**Better**

Open another terminal, start a fresh session, and run the loop there.

---

## Pattern 7 — Settle model and effort at the start

**Wasteful**

Switching `/model` or `/effort` at turn 30. Both are part of the cache key, so the whole
conversation re-prefills at full price.

**Better**

```
> /model
> /effort
```

Run both in a fresh session and confirm what you are on — they persist from the previous
session, so the settings in force may not be the ones you meant. Then leave them alone.

---

## Pattern 8 — Audit the standing load once

```
> /context
```

In a fresh session, before typing anything else, this shows what is already loaded: tool
definitions from every connected MCP server, the system prompt, `CLAUDE.md`, and startup
items. All of it is paid for on every turn.

Two follow-ups worth doing once:

- Move occasional workflow instructions out of `CLAUDE.md` and into skills, which load
  only when used.
- Turn off MCP servers you are not using with `/mcp`.

## Source

- https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions (August 14, 2026)
