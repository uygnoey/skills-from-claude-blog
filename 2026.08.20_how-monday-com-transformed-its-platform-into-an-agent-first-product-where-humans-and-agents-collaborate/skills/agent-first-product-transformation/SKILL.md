---
name: agent-first-product-transformation
description: Move a product or an internal platform from bolted-on AI features to an agent-first design where people and agents work on the same items. Use when AI features shipped, adoption looked fine for a month, and usage has flattened into occasional summarization; when deciding whether to embed agents into an existing workflow or rebuild the workflow around them; when agents live in a chat surface parallel to the real work and context must be pasted in by hand; when pilots stall before production because governance, permissions, and reliability were never designed in; or when you need concrete per-function agent jobs instead of one general assistant.
---

# Going agent-first

Distilled from monday.com's account of rebuilding a work management platform —
used by more than 250,000 companies — into a product where humans and agents
collaborate on the same work items. The rebuilt experience launched in May 2026
and reached 5 million agent interactions in two months.

The organizing distinction: **adopting AI features is not the same as becoming
an AI company.** Everything below follows from taking that seriously.

## Instructions

### 1. Diagnose whether you are making "AI dust"

The prior attempt is the useful part of this story. monday ran an "AI month" in
May 2025 and embedded AI features into existing workflows — summarize this text,
categorize this information. Adoption was real. The pattern did not stick.

VP of Product Orly Stern Izhaki's name for it: **"AI dust"** — sprinkling
automations onto workflows that are otherwise unchanged.

Symptoms to check for in your own product:

- Usage spikes at launch and settles into a narrow band of one or two verbs.
- The AI is optional at every step, so the workflow still works identically
  without it — which means nothing about the work has changed.
- Value is described in terms of time saved on a sub-step, never in terms of a
  job somebody no longer has to do.

If those hold, more features will not fix it. The workflow is the thing that
has to change.

### 2. Decide how agents get into the product

There are several ways in, and they are not alternatives — monday ships four in
parallel, because different customers arrive from different directions.
Full descriptions and fit criteria:
[references/deployment-models.md](./references/deployment-models.md).

In brief: prompt-built agents native to the platform; joining externally built
managed agents to the platform; pre-built specialized agents from a store; and
a coding integration where teams connect from dashboards, assign tasks, and
execute in their own environments.

Pick a primary path for the first release, but design the surface so the others
can attach later. Retrofitting a bring-your-own-agent path onto a closed design
is expensive.

### 3. Give every agent a named job

The failure mode on the other side of "AI dust" is one general-purpose
assistant that nobody can describe. monday instead defines agent jobs per
function — IT intake and triage, knowledge gap detection, incident handling; HR
resume screening, interview scheduling, hiring coordination, feedback
management; marketing competitive intelligence and battlecards; an executive
office with operator, org health, and strategy consultant roles.

The map: [references/agent-job-map.md](./references/agent-job-map.md).

For each agent, write down before building: what triggers it, what it may do
without a human, what it must hand back, and what a good output looks like.
Five of these roles are written out as subagent definitions in the `agents/`
folder of this post.

### 4. Design agents as teammates, not as a chat surface

Each monday agent has a name, an avatar, and a place inside the workflow. Teams
assign work through triggers and mentions, in the board where they already
operate, rather than in a parallel chat interface.

This is a product decision with a technical consequence: an agent that lives
where the work lives inherits the context of that work — the item, its history,
its owners, its status — instead of requiring a person to paste it in.

Practical checks:

- Can a person assign work to the agent without leaving the object they are
  working on?
- Does the agent's output land back on that object, where the next person will
  look for it?
- Can you tell, from the object, which steps were done by an agent?

### 5. Build the production line on one object

The point of the previous step is that a multi-agent workflow becomes legible
when it runs on a single item. In the campaign example, brief → structured
brief → landing page variants → brand review → human approval all happen on one
board item, with different agents and people picking it up in turn.

Worked through, with the Cooke Seafood deployment as a second case:
[examples/campaign-production-line.md](./examples/campaign-production-line.md).

### 6. Invest in trust infrastructure before scaling

monday's third lesson is that governance, permissions, transparency, and
reliability determined whether agents got past pilots. Not model quality —
those four.

Treat them as launch requirements, not hardening work:

- **Governance** — who authorizes an agent to act on which objects.
- **Permissions** — the agent's access is bounded by the assigning human's.
- **Transparency** — what the agent did is visible on the object afterwards.
- **Reliability** — behavior that is predictable enough to build a process on.

### 7. Fund the backend the agents depend on

Agents performed significantly better when grounded in live project data, team
history, and structured workflows. monday invested in **monday DB** to carry
agent volume and complexity at enterprise scale.

The general form: agent capability is bounded by what your data layer can serve,
at what latency, at what concurrency. A capability roadmap with no
infrastructure line item is a plan to plateau.

### 8. Extend the identity you already have

monday's framing was that it had always been the place where people team up, and
agents joined as team members. Rebuilding did not mean introducing a new
paradigm the customer had to learn from scratch.

Ask what your product already means to its users, and make agents an extension
of that sentence rather than a competing one.

The five lessons in full, each with what it implies for a plan:
[references/transformation-lessons.md](./references/transformation-lessons.md).

## Examples

### A product stuck in AI dust

A support platform ships an "AI summary" button on every ticket. Usage is 40% in
month one, 12% by month three. Under this skill, the diagnosis is that
summarization is a sub-step, not a job: nobody's work has been removed. The
agent-first version defines an intake and triage job — classify the ticket,
resolve what it can, escalate the rest — that arrives with the ticket rather
than waiting to be clicked, and lands its classification and its reasoning on
the ticket itself.

### Choosing a deployment path

A team already runs an internally built agent on its own infrastructure and does
not want to rebuild it as a prompt inside a vendor platform. That is the
bring-your-own-agent case: the agent joins the platform and participates in the
workflow, rather than being re-implemented. A team with no agent engineering
capacity and a well-understood function — legal review, say — takes the
pre-built store agent instead.

### Deciding an agent is not ready

A drafting agent produces good output but its permissions are inherited from a
service account rather than the assigning user, so it can read boards its
requester cannot. Under step 6 this blocks launch regardless of output quality —
permissions are a launch requirement, and this is exactly the class of gap that
keeps pilots from becoming production.

## Source
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) (published 2026-08-20).
