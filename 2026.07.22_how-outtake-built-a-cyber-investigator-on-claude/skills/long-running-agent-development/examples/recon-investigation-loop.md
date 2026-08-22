# The Recon Agent's investigation loop

A worked read of how Outtake's Recon Agent actually runs, as a concrete instance
of the patterns in the skill.

## The attack it is investigating

Attacks proceed in three stages:

1. **Weaponize public data** — harvest information about an organization and its
   personnel.
2. **Build impersonations as lures** — fake login pages and other bait.
3. **Exploit internal systems** — reach the valuable assets.

Traditional tools address each stage separately. That is the gap: the stages
belong to one adversarial network, and treating them individually means never
seeing the network.

## What the agent does instead

Starting from a **single cloned login page**, the Recon Agent:

1. **Gathers and classifies evidence** from the impersonation event.
2. **Follows those leads to connected infrastructure** — for example a fake
   Telegram account presenting itself as "Customer Support."
3. **Maps the adversarial network in a graph.**
4. **Produces an investigation report** with actor profiles and an attack
   timeline.

It reads, writes, and runs code, and it **interacts with the malicious login
pages directly** to trace where the credentials go.

## Where each pattern shows up

| Pattern | Where it appears in this loop |
| --- | --- |
| Constrain orchestration, not judgment | The stages above always happen in order; *which* lead to follow next is left to the agent |
| Filesystem as memory | The evidence and the graph persist as files, so they survive compaction across a session that may run two hours |
| Bash for resilience | A tool failing on a network hiccup does not end the investigation; the agent finds a workaround and continues |
| Guardrails over prompts | Anything that must happen for every investigation is enforced by the orchestration layer, not asked for in the prompt |
| Checkpoint at the network boundary | Before the agent touches a page, it is scored: impersonation? malware? actively trying to prompt-inject? |
| Second agent closes the tool gap | The report can end with "I could have done this better with a tool I didn't have," and a separate coding agent acts on it |

## Session shape

| Measure | Value |
| --- | --- |
| Median runtime | 16 minutes |
| Routine | up to an hour and beyond |
| Longest observed | 2 hours |

Two hours is long enough that instructions given at the start are far behind the
current context. This is the concrete reason "prompts are suggestions" is an
architectural claim rather than a complaint about prompt engineering.

## The improvement loop around it

When the investigation ends, the agent reports where it fell short — including
tools it wished it had. A separate coding agent reads those suggestions, writes
the new tool, and builds a test scenario to try it out. Humans evaluate only the
final result.

> "When you build these long, complex agents, it's very important that the
> feedback loop be automated." — Jack Hayford

Scale context for why the automation matters: Outtake scanned more than 20M
potential cyberattacks in 2025.

## Source

[How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude) — Michael Segner, July 22, 2026
