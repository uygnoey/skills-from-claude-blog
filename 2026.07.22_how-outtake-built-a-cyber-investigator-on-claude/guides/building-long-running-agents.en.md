**English** · [한국어](./building-long-running-agents.ko.md) · [Español](./building-long-running-agents.es.md) · [日本語](./building-long-running-agents.ja.md)

# Building long-running agents

How Outtake built the Recon Agent — an autonomous cyber investigator — and what
held up once sessions started running for hours.

## 1. The problem

Outtake was founded in 2023 by Alex Dhillon, previously on Palantir's moonshot
team. The company unifies the full digital-trust attack chain into a single
defense, and scanned more than 20M potential cyberattacks in 2025.

Dhillon frames the situation from the attacker's side:

> "If you put on the bad actor's hat, it's actually a great time to be running
> attacks. The average attack is not only executed faster because of AI, but it
> also captures deeper access due to AI."

Attacks run in three stages: harvest public data, build impersonations as lures,
exploit internal systems. Traditional tools address each stage separately — and
that is the gap, because the three stages belong to one adversarial network.

## 2. What the Recon Agent does

From a **single cloned login page**, it gathers and classifies evidence, follows
leads to connected infrastructure — for instance a fake Telegram account
presenting itself as "Customer Support" — maps the adversarial network in a
graph, and produces an investigation report with actor profiles and an attack
timeline.

It reads, writes, and runs code, and interacts with malicious login pages
directly to trace where stolen credentials go.

| Measure | Value |
| --- | --- |
| Median session runtime | 16 minutes |
| Routine | up to an hour and beyond |
| Longest observed | 2 hours |

## 3. Four stages of development

### Stage 1 — Become the expert first

The team ran real cyber investigations themselves and extracted domain expertise
from customers and design partners, to define what "good" means.

> "The most important thing about building long running agents is that you really
> have to understand *what does good look like? What is the agent supposed to be
> doing?*" — Jack Hayford, engineering lead

### Stage 2 — Prototype in Claude Code

Traditional agent frameworks were not enough:

> "Every investigation is different, and deeply technical. The agent needed
> coding muscle and capability, and Claude Code was a strong initial harness."

The core design principle set here: **constrain orchestration tightly** — always
perform X, Y, Z — **but allow improvisation in judgment-requiring scenarios.**

### Stage 3 — Graduate to a production-grade harness

> "We really liked the patterns that Claude Code had introduced, but we needed
> additional access to the lower level primitives."

The team migrated to the **Claude Agent SDK** for production, gaining tighter
control over memory, context, and the file system without rebuilding the agent
loop.

### Stage 4 — Build tight iteration loops driven by evals

Automated evaluation suites let the team make sweeping changes safely. A separate
coding agent reads the investigation's suggestions, writes new tools, and builds
test scenarios — humans only evaluate final results.

> "When you build these long, complex agents, it's very important that the
> feedback loop be automated."

## 4. Four learnings about long-running agents

### Tools: a filesystem and bash are sufficient

A filesystem gives memory that survives context compaction. A filesystem plus
bash lets the agent respond creatively to obstacles.

> "Handing those extremely powerful open-ended tools and capabilities to an agent
> is a huge step change. We've observed plenty of cases where an agent had a tool
> that was failing due to a network hiccup or whatever, and it would just find
> the right workaround and continue."

### Prompts are suggestions

System prompts give flexibility but lack staying power in long-running agents.

> "When you're building these long-running agents that get complicated over time,
> prompts are suggestions. Every single word in that prompt will probably be
> ignored eventually."

The response is architectural: move behavioral requirements out of the prompt and
into **hardcoded guardrails at the orchestration layer**, which also preserves
context space for high-judgment tasks.

### Evals are for speed, not just reliability

Manually reviewing 30-minute transcripts does not scale. Evals automate
reflection into structured, graded checks and dramatically accelerate development
cycles.

> "Building some version of evals from the very beginning will make you build
> that agent faster regardless of how official or 'perfect' they are."

### Protecting your agents

Prompt injection is a real threat. Outtake chose Claude partly for its strength
against prompt injection attacks — but the defense is architectural.

> "Security is a big note for us for building the Recon Agent. We gave it a file
> system and bash and we're sending it to adversarial environments."

The strategy: assume the agent might be hijacked, and engineer the surrounding
system to contain the damage. Outtake scores trust at the exact point the agent
reaches out to the internet, implementing a checkpoint that evaluates whatever
the agent is about to touch: "Is this page an impersonation? Is it malware? Is it
trying to prompt-inject the agent right now?"

## 5. Best practices summary

**Do you know what "good" looks like?**
Run the task yourself first. Extract domain expertise from customers and design
partners. Establish a fixed standard for every iteration.

**Is each piece of complexity earned?**
Find the simplest working version. Automate incrementally. Add complexity only
when results justify it.

**Is your harness matched to the workload?**
Validate assumptions in Claude Code. Graduate to the Agent SDK when you need
lower-level control. Don't rebuild the agent loop yourself.

**Where should the agent be constrained?**
Hardcode guardrails at the orchestration layer. Avoid constraints in low-level
judgment calls. Improvisation space produces the best results.

## Source

[How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude) — Michael Segner, July 22, 2026
