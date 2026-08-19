# Incident lifecycle with an agentic first responder

What changes at each stage when an agent is the first responder, and what deliberately stays human. Drawn from the source post's account of a CI/CD on-call rotation.

## The four ingredients

Before the stages, the setup. An on-call agent needs:

| Ingredient | What it means in practice |
|---|---|
| **Memory** | It remembers what has been done — across the channel, and across incidents via a lessons log |
| **Connections and access** | A service account with the tools an on-call engineer uses, wired through MCP connectors |
| **Schedules** | Routines it runs on a cadence, requested in natural language in the channel |
| **Instructions** | Standing instructions as markdown skills, committed to a repository |

Access is granted once, by an administrator, for the channel. The agent also watches other channels it is a member of, picking up service alerts, configuration changes, and PR updates as context it will need later.

## Stage 1 — Detection

Two failure modes existed before the agent, and each gets a different answer.

**Imperfect thresholds.** Humans rarely set the right rules on a new service, especially without enough traffic history to analyse patterns. The agent analyses the data and incoming alerts over a new service's first days, then suggests additional rules and tunes ones that are too broad or too narrow.

**Alert fatigue.** Vetting every alert is tedious and humans degrade at it; the agent does not degrade the same way. It monitors every relevant alert channel and applies the criteria in the root instruction file to decide whether something can wait until morning or needs to page. A criterion is concrete — a threshold, a duration, and an exception for known deploy windows — with the non-paging branch writing to the lessons log instead.

Two further entry points stay open: a team member reporting an issue directly in the on-call channel, and an incident opened through an internal process that provisions a dedicated channel the agent then picks up.

**The shape to keep:** the alerting process stays deterministic. On-call escalation has both a deterministic and an agentic path.

## Stage 2 — Triage

This is where the time is saved — not in filtering noise, but in the investigation.

The agent kicks off a dynamic workflow: an **orchestration agent** spins up **executor subagents** that investigate each dependency and source of truth in parallel — dashboards, log store, paging system, source control, cluster, related incident channels, all reached through MCP connectors. Chasing several leads at once is what reduces mean time to resolution.

Executors report findings back to the orchestrator, which synthesizes them into one coherent situation report rather than a pile of raw output.

The measured result in the source account: a median of about 14 minutes from incident open to the first evidence-grounded analysis, with the fastest cases naming a root cause about 4 minutes in, in the first report.

Two things keep the agents from searching blind:

- **A per-bug-class investigation skill**, with detailed reference files. One example runs to 617 lines and encodes every step the engineer takes for that class. It was built by troubleshooting a real incident turn-by-turn with the agent and then having it write the file from that experience.
- **The lessons log**, read at the start of every investigation, so the first hypothesis starts from what has happened recently.

**What stays human:** intuition and experience still matter, and the agent does not always get it right first time. The team troubleshoots in multi-player mode — anyone can steer the investigation or add a hypothesis in real time, alongside the agent.

## Stage 3 — Resolution

Where the boundary falls varies by team. The pattern in the source account:

- **Progressive rollout behind feature flags** is handled by a *separate* agent, created in a coding agent, running with a named engineer's permissions. Its first stage manages canary traffic, monitors for issues, and ramps a flag up or down.
- **Cluster actions** — draining or cordoning off sections — are surfaced as recommendations for a human.
- **Scale-up instructions** for demand surges are produced as exact steps, rare but valuable when they arrive complete.
- **Fixes as PRs**, most frequently: the on-call reviews, merges, and deploys.

The dividing line is permission scope, not capability. Anything that writes runs under a named human's authority.

## Stage 4 — Verification, communication, handoff

**Verification** uses the same connectors and tools as the investigation. A fix is done when the signal returns to baseline, not when the change merges.

**Post-mortem** goes into the lessons log automatically, as part of the standing instructions, along with the handoff situation report.

**Public communication** is a separate agent — `ci-weather` in the source account — compiling incident channels, build metrics, merge queue stats, and deploy lag into a newsroom-style report on a public channel. Engineers read that channel instead of pinging the on-call to ask whether they should hold their merges.

One honest caveat from the author: the report format needed several iterations. An agent can one-shot a skill that generates a status report, but what makes it *readable* is team-specific taste — human communication, not plumbing.

**Handoff reports** for humans run on a schedule, daily and weekly, so one team member can pick up where another left off.

## The self-improvement loop

1. An incident is resolved.
2. The agent appends what happened, the root cause, the fix, and the gotcha to the lessons log.
3. Every subsequent investigation starts by reading that log.
4. When a pattern recurs often enough, it is promoted into the investigation skill itself.

Entries about *how the team investigates* count as much as entries about specific bugs — for instance, a correction that data should be queried before a theory is formed, because configuration tells you what could go wrong while metrics tell you what did.

## What does not change

Volume grew — engineers in the source account ship roughly 8x the code per quarter compared with 2021–2025 — and the quality bar was held by keeping the guardrails:

- Every PR has a named human owner.
- Every change requires approval to merge.
- Every change goes through the same CI gates.

The argument the post makes is that the only way to keep up with agentic coding is agentic CI, and the way to do that safely is to leave those three constraints alone.

## Source

- https://claude.com/blog/ai-ci-cd-on-call
