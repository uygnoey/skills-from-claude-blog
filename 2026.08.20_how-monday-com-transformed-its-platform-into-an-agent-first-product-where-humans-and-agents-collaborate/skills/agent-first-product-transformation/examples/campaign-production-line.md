# Worked examples

Two deployments described in the source: a marketing campaign production line
run end to end on a single board item, and Cooke Seafood operating its business
from the platform.

---

## A campaign production line on one item

The point of the example is not the marketing workflow. It is that a
multi-agent, multi-human process becomes legible when it runs on **one object**
that everyone — people and agents — picks up in turn.

### The sequence

1. **A marketer and a content lead shape the brief.**
   Humans first. The judgment about what campaign is worth running is not
   delegated.

2. **A Strategist Agent structures the brief.**
   It turns the shaped brief into objectives, messaging pillars, channels, and
   metrics. Note that this is a *structuring* job, not an authoring job — the
   intent came from the humans in step 1, and the agent gives it a shape the
   rest of the line can consume.

3. **A Landing Page Builder generates variants.**
   This is a Claude Managed Agent — the bring-your-own-agent path — producing
   page variants with copy adapted per variant. It can do this because step 2
   produced structured inputs rather than prose.

4. **A Brand Reviewer checks against guidelines.**
   It compares the output to brand guidelines and flags issues. A separate agent
   from the builder, deliberately: the reviewer's job is to disagree with the
   builder's output.

5. **A marketing manager approves or refines.**
   A human decision before publishing. The line ends where accountability sits.

### What makes it work

- **One item carries the state.** Each participant finds the current state where
  they expect it, and leaves their contribution in the same place. Nobody pastes
  context between tools.
- **Structure at step 2 enables automation at step 3.** The builder is only
  possible because something upstream converted intent into fields.
- **Producer and reviewer are different agents.** Asking one agent to generate
  and then approve its own output collapses the check.
- **Humans bracket the line.** People at the start, where intent is set, and at
  the end, where accountability lands. Agents do the production work in between.

### Adapting it

The generalizable shape is: *human intent → agent structuring → agent production
→ agent review → human approval*. It transfers to any pipeline where the
expensive middle is mechanical but the ends require judgment — proposal
production, incident write-ups, report generation, onboarding packets.

---

## Cooke Seafood: operating from the platform

Cooke, described as the world's largest family-owned seafood company, deployed
Claude and monday together across three areas:

- **Project delivery and resource management** across roughly 200 active and
  proposed projects.
- **Contract management** across 130 contracts.
- **Automated reporting** that surfaces risks into RAID logs (risks, assumptions,
  issues, dependencies).

Director of Strategy Patti Stevens describes the change as moving from a
platform they had to update to one they operate from.

### Why that sentence is the point

The distinction between *updating* a system and *operating from* it is the same
distinction the whole post turns on. A system you update is one where the real
work happens elsewhere and the tool is a record of it — which is exactly the
condition in which AI features become "AI dust," because they are decorating the
record rather than doing the work.

The three deployments above have a common property: each is a place where the
record and the work were already the same object. Project delivery, contract
status, and risk registers are all things whose *state* is the deliverable. That
is where agents pay off first, and it is a reasonable heuristic for choosing
where to start.

### Scale as a constraint

200 projects and 130 contracts is not a large number of documents; it is a large
number of *continuously changing* documents. This is the concrete form of the
source's fourth lesson — agents grounded in live project data need a backend
that can serve that data at agent read volumes, which is why monday invested in
monday DB.

## Source
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) (published 2026-08-20).
