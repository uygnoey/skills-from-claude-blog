**English** · [한국어](./agent-first-platform-rollout.ko.md) · [Español](./agent-first-platform-rollout.es.md) · [日本語](./agent-first-platform-rollout.ja.md)

# From AI features to agent-first: sequencing the rollout

Derived from monday.com's August 20, 2026 account of rebuilding its work
management platform — used by more than 250,000 companies — into a product where
humans and agents collaborate on the same items. The rebuilt experience launched
in May 2026 and reached 5 million agent interactions within two months.

## Start with the failed version

The most useful part of the story is the attempt that did not work. In May 2025,
during an internal "AI month," monday embedded AI features into existing
workflows — summarizing text, categorizing information. Adoption happened. The
pattern did not stick.

The name the team gave it, from VP of Product Orly Stern Izhaki, is **"AI
dust"**: automations sprinkled onto workflows that were otherwise unchanged. The
conclusion drawn was that adopting AI features is not the same as becoming an AI
company.

This is worth dwelling on because the failure mode is not visible in the launch
metrics. Features that summarize and categorize genuinely help. They just do not
change how the work is done, so usage settles into a narrow band and stops
compounding. Chief Product and Technology Officer Daniel Lereya describes the
subsequent pivot to an agent-first product as one of the company's most
significant decisions — which is a fair description of a choice to rebuild
rather than to add.

**Diagnostic:** if your product still works identically with the AI turned off,
you have added dust. Nothing about the work has moved.

## Phase 1 — Decide what "agent-first" means for your product

Before any build, answer the question the fifth lesson points at: what does your
product already mean to its users? monday's answer was that it had always been
the place where people team up, and agents joined as team members. The
transformation extended an existing identity rather than replacing it.

Getting this wrong is expensive in a specific way: if agents require users to
learn a new mental model *and* trust a new class of actor simultaneously, you
have doubled the adoption cost. The usual way it happens by accident is a
separate chat surface with its own concepts, sitting beside the product.

## Phase 2 — Reframe the team before rebuilding

monday's first lesson is that mental models were harder to move than the
technology: shifting teams from "improve the existing product" to "responsibly
rebuild for a different future" took longer than the engineering.

Two implications for a plan:

- **Schedule the reframing.** A timeline with engineering estimates and no time
  allocated to changing what the team thinks it is building will slip on the
  unscheduled part.
- **Expect resistance from your strongest people.** Expertise in the current
  product is exactly what the reframe asks them to set down.

## Phase 3 — Restructure ownership for a period of simultaneous change

The second lesson comes with a precondition worth reading carefully: direction,
UX, technology, pricing, trust models, and quality definitions were all moving at
once. Under those conditions, small teams with clear ownership and fast decision
rights stayed aligned better than hierarchical structures.

The general rule is not "hierarchy is bad." It is that hierarchy struggles when
every input to a decision is still in motion, because each decision has to
travel up and back down while its premises change underneath it. Structure for
the number of simultaneously unstable variables.

## Phase 4 — Define agent jobs, function by function

The failure mode on the far side of AI dust is a single general-purpose
assistant nobody can describe. monday defined named jobs instead:

- **IT** — an Intake & Triage Agent (classify, auto-resolve, escalate), a
  Knowledge Agent (detect gaps, draft articles), an Incident Agent (detect
  incidents, open war rooms).
- **HR** — resume screening, interview scheduling, hiring coordination, feedback
  management.
- **Marketing** — competitive intelligence, battlecards.
- **Executive office** — an Operator Agent, an Org Health Agent, a Strategy
  Consultant Agent.

Reading across them, four properties recur, and they make a usable test. Before
building an agent, you should be able to state: its **trigger** (the moment it
activates, not the button that invokes it), its **bounded verb** (a job
description, not a domain), its **handback** (what it produces for a person or
another agent to pick up), and its **identity** (a name and an avatar, so it is
addressable in the workflow). If you cannot name the trigger or the handback,
what you have is a feature.

## Phase 5 — Put agents where the work already is

Each monday agent has a name, an avatar, and a place inside the workflow. Work
is assigned through triggers and mentions on the board where employees already
operate, rather than through a parallel chat interface.

This is a product decision with a technical consequence. An agent that lives
where the work lives inherits that work's context — the item, its history, its
owners, its status — instead of requiring a person to paste it in. Three checks:

- Can a person assign work without leaving the object they are working on?
- Does the output land back on that object, where the next person will look?
- Can you tell from the object which steps an agent performed?

## Phase 6 — Run a production line on one object

The campaign example makes the shape concrete. On a single board item: a
marketer and content lead shape the brief; a Strategist Agent structures it into
objectives, messaging pillars, channels, and metrics; a Landing Page Builder — a
Claude Managed Agent — generates variants with adapted copy; a Brand Reviewer
checks against guidelines and flags issues; a marketing manager approves or
refines before publishing.

The generalizable pattern: **human intent → agent structuring → agent production
→ agent review → human approval.** Three things make it hold together. One
object carries the state, so nobody pastes context between tools. The
structuring step is what makes the production step possible at all. And the
producer and the reviewer are different agents, because an agent approving its
own output is not a review.

## Phase 7 — Ship trust infrastructure with the first release

monday's third lesson is blunt: governance, permissions, transparency, and
reliability determined whether agents moved beyond pilots into production. Not
model quality.

Treat all four as acceptance criteria rather than hardening work, because a
pilot that skips them demos well and then fails to convert — and the failure
gets misread as a capability problem.

- **Governance** — who authorizes an agent to act on which objects.
- **Permissions** — the agent's access bounded by the assigning human's, not by
  its own service identity.
- **Transparency** — what the agent did, visible on the object afterwards.
- **Reliability** — behavior predictable enough to build a process on.

## Phase 8 — Fund the data layer

The fourth lesson: agents performed significantly better grounded in live
project data, team history, and structured workflows, and monday invested in
**monday DB** to support agent volume and complexity at enterprise scale.

Agent quality is bounded by what the data layer can serve — how fresh, how
structured, at what latency and concurrency. Agents read far more, and far more
often, than human users do. A capability roadmap with no infrastructure line
item is a plan to plateau at whatever your current query patterns support.

## What the end state looks like

Cooke, described as the world's largest family-owned seafood company, runs
project delivery and resource management across roughly 200 active and proposed
projects, contract management across 130 contracts, and automated reporting that
surfaces risks into RAID logs. Director of Strategy Patti Stevens frames the
change as going from a platform they had to update to one they operate from.

That distinction is the whole thing in one sentence. A system you *update* is
one where the real work happens somewhere else and the tool holds a record of
it — which is precisely the condition under which AI features become dust,
because they decorate the record instead of doing the work. All three of Cooke's
deployments share a property worth using as a heuristic for where to start:
project delivery, contract status, and risk registers are each cases where the
record and the work are already the same object.

## Source
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) (published 2026-08-20).
