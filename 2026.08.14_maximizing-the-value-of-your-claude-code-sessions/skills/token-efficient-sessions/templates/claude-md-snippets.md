# `CLAUDE.md` snippets for token-efficient sessions

Two additions to `CLAUDE.md` that pay for themselves immediately. Both work by removing
recurring waste rather than by making anything shorter.

Keep the file **specific**. Anything resident in `CLAUDE.md` is re-sent on every turn of
every session, so workflow instructions that are only occasionally relevant belong in a
skill (loaded on use) rather than here.

---

## 1. Everyday commands, with their quiet flags

Record the two or three commands you run all day, written exactly as you would type them,
quiet flags included. This saves a turn spent working out the invocation, and it keeps
hundreds of lines of default-verbose output from landing in the conversation and being
re-sent for the rest of the session.

```markdown
## Commands

- Run a single test file: `npx vitest run <file> --reporter=dot`
- Run the full suite: `npx vitest run --reporter=dot`
- Typecheck: `npx tsc --noEmit`
- Lint a path: `npx eslint <path> --quiet`
- Build: `npm run build -- --silent`
```

Adapt to your stack. The pattern is: the command you actually want, plus whatever flag
that tool uses to stop narrating. Common ones:

| Tool family | Quieting flag |
|---|---|
| Test runners | `--reporter=dot`, `--quiet`, `-q` |
| Linters | `--quiet` (errors only) |
| Package managers | `--silent`, `--loglevel=error` |
| Build tools | `--silent`, `--log-level error` |
| `git` | `--quiet`, `--no-pager`, `--oneline` |

---

## 2. Compact instructions

If you find yourself telling `/compact` the same thing every time, write it down once.

```markdown
## Compact instructions

When compacting, always keep:
- The file(s) currently being edited and the change in progress.
- Any API shape, schema, or interface we agreed on this session.
- Decisions made and the reasoning behind them — not the exploration that led there.
- Failing test names and their current error messages.

Drop:
- Full file contents already read (re-read on demand instead).
- Command output and stack traces that have been acted on.
- Paths explored and abandoned.
```

---

## 3. Optional: a note on session hygiene

Some teams keep a short reminder in `CLAUDE.md` so the habits survive handoff between
people:

```markdown
## Session hygiene

- New task → `/clear` (`/rename` first if the session may be needed again).
- Piece of work finished but its conclusions still needed → `/compact`, before stepping away.
- Wrong path → `/rewind` (free; leaves the cache intact).
- Noisy one-off investigation (logs, traces) → delegate to a subagent.
```

Keep this short if you include it at all — it is resident text, and its value has to beat
the cost of re-sending it on every turn.

## Source

- https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions (August 14, 2026)
