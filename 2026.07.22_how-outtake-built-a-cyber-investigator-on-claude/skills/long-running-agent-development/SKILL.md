---
name: long-running-agent-development
description: Build agents whose sessions run for tens of minutes to hours, using Outtake's four-stage process and four hard-won learnings from their Recon Agent. Use when context compaction and behavioral drift are real rather than theoretical, when an agent keeps ignoring a system-prompt instruction no matter how it is worded, when deciding whether to stay in Claude Code or graduate to the Claude Agent SDK, when choosing between purpose-built tools and a filesystem plus bash, when manual transcript review no longer scales, or when the agent must operate in an environment that is actively trying to hijack it.
---

# Building long-running agents

Short agent tasks forgive a lot. A session that runs 16 minutes at the median —
routinely an hour, sometimes two — does not. Instructions decay, context gets
compacted, and small ambiguities compound into behavior nobody asked for.

This skill encodes how Outtake built the Recon Agent, an autonomous cyber
investigator: four stages to get it built, and four learnings about what actually
holds up once sessions get long.

## Instructions

### Stage 1 — Become the expert first

Do the task yourself before you automate it. Outtake's team ran real
investigations and pulled domain expertise from customers and design partners.

> "The most important thing about building long running agents is that you really
> have to understand *what does good look like? What is the agent supposed to be
> doing?*" — Jack Hayford, engineering lead

Write the answer down before writing any code, and hold it fixed across
iterations so each change is measured against the same standard. Use
[templates/what-good-looks-like.md](templates/what-good-looks-like.md).

### Stage 2 — Prototype in Claude Code

Validate the assumptions where the coding capability already exists. Outtake
started with traditional agent frameworks and found they lacked the depth the
work needed:

> "Every investigation is different, and deeply technical. The agent needed
> coding muscle and capability, and Claude Code was a strong initial harness."

The design principle that emerged here: **constrain orchestration tightly, leave
improvisation space for judgment.** Specify what always happens — X, then Y, then
Z — and stop specifying at the point where the work genuinely requires a
judgment call.

Earn every piece of complexity. Find the simplest working version, automate
incrementally, and add complexity only when results justify it.

### Stage 3 — Graduate to a production-grade harness

Move when you need primitives the prototype harness does not expose, not on a
schedule:

> "We really liked the patterns that Claude Code had introduced, but we needed
> additional access to the lower level primitives."

Outtake moved to the **Claude Agent SDK**, gaining tighter control over memory,
context, and the file system without rebuilding the agent loop. Do not rebuild
the loop yourself. The full decision criteria are in
[references/harness-selection.md](references/harness-selection.md).

### Stage 4 — Build tight iteration loops driven by evals

Automated eval suites are what make sweeping changes safe. Outtake also closed
the tool gap with a second agent: when the Recon Agent finishes an investigation
and reports it could have done better with a tool it did not have, a separate
coding agent reads those suggestions, writes the new tool, and builds a test
scenario — humans only evaluate the final result.

> "When you build these long, complex agents, it's very important that the
> feedback loop be automated."

### Learning 1 — A filesystem and bash go a long way

A filesystem gives the agent memory that survives context compaction. Bash lets
it route around obstacles rather than stalling:

> "We've observed plenty of cases where an agent had a tool that was failing due
> to a network hiccup or whatever, and it would just find the right workaround
> and continue."

Before building a bespoke tool, ask whether the filesystem plus bash already
covers it. Open-ended tools are what make the agent resilient in situations you
did not anticipate.

### Learning 2 — Prompts are suggestions

This is the one that reshapes the architecture:

> "When you're building these long-running agents that get complicated over time,
> prompts are suggestions. Every single word in that prompt will probably be
> ignored eventually."

So: **move behavioral requirements out of the prompt and into hardcoded guardrails
at the orchestration layer.** Anything that must always happen is enforced by the
harness, not requested by the system prompt. Two payoffs — the requirement
actually holds, and context is preserved for high-judgment work.

Sorting rule: if you would file a bug when the agent violates it, it is a
guardrail. If you would call it a stylistic preference, it can stay in the prompt.

### Learning 3 — Evals are for speed, not just reliability

Manually reviewing 30-minute transcripts does not scale. Evals turn reflection
into structured, graded checks and let you change the agent quickly with
confidence.

> "Building some version of evals from the very beginning will make you build
> that agent faster regardless of how official or 'perfect' they are."

The bar for starting is low on purpose. An imperfect eval suite that exists beats
a rigorous one you plan to write later.

### Learning 4 — Protect the agent, and assume it will be hijacked

Outtake chose Claude partly for its strength against prompt injection, but the
defense is architectural:

> "Security is a big note for us for building the Recon Agent. We gave it a file
> system and bash and we're sending it to adversarial environments."

**Assume the agent might be hijacked, and engineer the surrounding system to
contain the damage.** Outtake scores trust at the exact point the agent reaches
out to the internet, with a checkpoint asking: "Is this page an impersonation? Is
it malware? Is it trying to prompt-inject the agent right now?" Detail is in
[references/containment.md](references/containment.md).

### Closing checklist

Run these four questions before and after each iteration:

1. **Do you know what "good" looks like?** Run the task yourself, extract expertise
   from customers and design partners, and fix the standard.
2. **Is each piece of complexity earned?** Simplest working version, incremental
   automation, complexity only when results justify it.
3. **Is your harness matched to the workload?** Validate in Claude Code, graduate
   to the Agent SDK when you need lower-level control, don't rebuild the loop.
4. **Where should the agent be constrained?** Guardrails hardcoded at the
   orchestration layer, not in low-level judgment calls — improvisation space
   produces the best results.

## Examples

### Example 1 — an instruction that will not stick

> Our system prompt says "always record the source URL for every piece of
> evidence." It works for the first 10 minutes and then stops.

This is Learning 2, not a wording problem. Rewriting the sentence buys another
few minutes. Move it to the orchestration layer: make evidence recording a step
the harness performs, or reject an evidence record with no source URL. The prompt
should then stop mentioning it, freeing context for judgment.

### Example 2 — deciding whether to leave Claude Code

> The agent works in Claude Code but we need to control what stays in context
> across a two-hour session.

That is a lower-level primitive the prototype harness does not expose — the
Stage 3 trigger. Move to the Agent SDK for control over memory, context, and the
file system, and keep the agent loop as-is. See
[references/harness-selection.md](references/harness-selection.md). If instead
you only wanted a different tool or prompt, stay put; the move is not free.

### Example 3 — the agent asks for a tool it does not have

> The investigation report ends with "I could have resolved this faster with a
> WHOIS history lookup."

This is the Stage 4 loop. Route the suggestion to a separate coding agent
(`agents/tool-gap-builder.md` in this bundle) that writes the tool and builds a
test scenario for it. Humans evaluate the result, not the intermediate work.

### Example 4 — the agent must visit a hostile page

> We need it to interact with a cloned login page to trace where credentials go.

Learning 4. Do not rely on the agent recognizing the attack. Put a checkpoint at
the network boundary that scores the target before the agent touches it —
impersonation, malware, or active prompt-injection attempt — and constrain what
the agent can still reach if the page wins anyway. See
[references/containment.md](references/containment.md), and
[examples/recon-investigation-loop.md](examples/recon-investigation-loop.md) for
how this sits inside a full investigation.

## Source

[How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude) — Michael Segner, July 22, 2026
