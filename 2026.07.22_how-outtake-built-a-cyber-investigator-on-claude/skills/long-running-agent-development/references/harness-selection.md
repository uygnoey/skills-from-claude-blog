# Choosing and changing the harness

Outtake moved through three harnesses. Each move was triggered by a specific
missing capability, not by a roadmap.

## Traditional agent frameworks → Claude Code

**What was missing:** coding capability at the depth the work required.

> "Every investigation is different, and deeply technical. The agent needed
> coding muscle and capability, and Claude Code was a strong initial harness."
> — Jack Hayford, engineering lead

The Recon Agent reads, writes, and runs code as part of doing its job — it
interacts with malicious login pages directly to trace where stolen credentials
go. That is not an agent that occasionally calls a tool; the coding capability is
the work. A framework that treats code execution as one tool among many is
mismatched to that workload.

**Use Claude Code as the prototype harness when:**

- The task is technical enough that the agent needs to write and run code to
  handle cases you did not enumerate in advance.
- You are still validating assumptions and want to change the shape of the agent
  quickly.
- The patterns you need — filesystem, bash, an agent loop that already works —
  exist and you do not want to build them.

## Claude Code → Claude Agent SDK

**What was missing:** access to lower-level primitives.

> "We really liked the patterns that Claude Code had introduced, but we needed
> additional access to the lower level primitives."

Moving to the Agent SDK gave the team tighter control over **memory, context, and
the file system** — without rebuilding the agent loop. That last clause is the
point of the move. The patterns carry over; what you gain is control underneath
them.

**Graduate when you need:**

| Need | Why the prototype harness is not enough |
| --- | --- |
| Control over what stays in context across a long session | Compaction behavior is not yours to shape |
| Control over memory | You need to decide what persists and in what form |
| Control over the file system surface | The agent operates in adversarial environments and the boundary matters |
| Production deployment characteristics | Sessions run 16 minutes at the median and up to two hours |

**Do not graduate because:** the agent needs a different tool, a different prompt,
or better instructions. Those are cheaper to change where you are.

## The rule that spans both moves

> Don't rebuild the agent loop yourself.

Both harnesses give you a working loop. The reason to move between them is
control over the primitives underneath it, never the loop itself. If you find
yourself reimplementing turn handling, tool dispatch, or context management from
scratch, the harness choice was probably wrong rather than the loop.

## The session profile this is sized for

| Measure | Value |
| --- | --- |
| Median session runtime | 16 minutes |
| Routine upper range | ~1 hour |
| Longest observed | 2 hours |

At this profile, context compaction happens mid-task, instructions given at the
start are far behind, and any behavior that depends on the agent remembering a
prompt line will eventually fail. That is what makes harness-level control worth
the migration.

## Source

[How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude) — Michael Segner, July 22, 2026
