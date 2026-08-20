# Four ways agents get into the platform

monday ships four deployment paths in parallel rather than picking one, because
customers arrive with different amounts of agent engineering capacity and
different constraints on where execution may happen. Each is summarized below
with the fit criteria implied by the source.

---

## 1. Platform-native agents built with prompts

**What it is.** monday Agents: agents configured inside the platform, defined by
prompts, using Claude as the model.

**Fits when**
- The job is well understood and expressible as instructions plus the platform's
  own data.
- The team building it is closer to operations than to engineering.
- You want the agent to be maintainable by whoever owns the workflow.

**Watch for**
- Prompt-defined agents drift when the workflow around them changes. Whoever
  owns the workflow has to own the agent.

---

## 2. Bring your own agent (BYOA)

**What it is.** Claude Managed Agents built outside the platform, joined to it
so they participate in platform workflows.

**Fits when**
- An agent already exists and re-implementing it inside a vendor product would
  throw away real work.
- The agent needs tools, data, or an execution environment the platform does not
  offer.
- Ownership needs to stay with an engineering team.

**Watch for**
- The permission boundary. An externally built agent joining the platform still
  has to be bounded by the assigning human's access, not by its own service
  identity.

---

## 3. Pre-built specialized agents from a store

**What it is.** Ready-made agents from the monday Agents Store, including
domain plugins such as legal and finance.

**Fits when**
- The function is standard enough that someone else's definition is close to
  right.
- There is no capacity to build or maintain an agent for it.
- You want a working example of what a well-scoped agent job looks like before
  writing your own.

**Watch for**
- Domain agents in regulated functions still need the governance and review
  steps of that function. Pre-built means pre-scoped, not pre-approved.

---

## 4. Coding integration

**What it is.** Teams connect Claude in dashboards, assign it tasks, and have it
execute in customer environments.

**Fits when**
- The work product is code or changes to a system, not a document.
- Execution has to happen inside the customer's own environment.
- The assignment should look like the rest of the team's work assignment, not
  like a separate developer tool.

**Watch for**
- Execution in a customer environment raises the stakes of every permission and
  transparency question in the skill's step 6.

---

## Choosing

For a first release, pick a primary path — usually the one matching where your
users' capacity already is — but design the surface so the others can attach
later. Retrofitting a bring-your-own-agent path onto a design that assumed all
agents are prompt-configured internally is expensive, because the assumptions
about identity, permissions, and execution location are baked in early.

## Source
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) (published 2026-08-20). The four paths are from the post; the fit criteria and cautions are drawn out from it.
