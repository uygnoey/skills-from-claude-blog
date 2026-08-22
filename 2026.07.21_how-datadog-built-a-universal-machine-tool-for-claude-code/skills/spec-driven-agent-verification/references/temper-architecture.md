# Temper's architecture

Temper is described in the article as a "universal machine tool" for Claude Code:
the thing agents build *with*, rather than another thing agents build.

## The three contracts

Every capability in Temper requires three contracts. A capability is not a
capability until all three exist.

### Behavior

- **states** — the named states the capability can be in
- **transitions** — the moves between states
- **preconditions** — the guard on each transition
- **safety properties** — the invariants that must hold across all of them

This is the part that replaces control code. Rather than expressing lifecycle in
route handlers and background jobs, the agent writes down states, moves, guards,
and invariants, and the kernel proves things about them.

### Data contract

- **entity types**
- **properties**
- **actions**

Held in **machine-parseable form**. Machine-parseable is load-bearing: it is what
lets an agent read the contract, reason about it, and propose a modification
without parsing prose or inferring intent from implementation.

### Authorization

- **default-deny** — nothing is permitted until granted
- **scope-based approval** — permissions are scopes, not code paths
- **pending decisions** — a requested scope that has not yet been granted is a
  first-class state, not a failure
- **hot-loading** — an approved change takes effect without a redeploy

Default-deny plus pending decisions is what makes an agent asking for more
permission a normal, reviewable event instead of an incident.

## The three roles in the Helix dark factory

Helix is a Kafka-comparable streaming system that Claude Code built most of in
days. Temper serves its dark factory in three roles at once:

1. **Agent control plane** — sessions, roles, work queues, and lifecycle for the
   managed agents doing the work.
2. **Tool-builder layer** — lets agents bridge SDLC tooling: Git, CI, deployment.
   This is the role that addresses the bottleneck that appeared after Helix, where
   "agents could build large parts of the system…but then humans still have to
   coordinate to ship the work to production through tools and mechanisms built
   for humans."
3. **Helix control API** — the lifecycle surface around the data plane. The same
   contract machinery that governs the factory also governs the product.

The third role is what makes it a machine tool rather than a build system: the
control plane for the agents and the control plane for the thing being built are
the same explicit, verified surface.

## Why not just build a CRUD app

Claude Code builds CRUD apps well. The problem is not capability, it is where the
control logic ends up. As Sesh Nalla, VP of engineering at Datadog, puts it:

> "In normal CRUD apps, the control logic is spread across routes, database
> constraints, service code, background jobs, and documentation…the operational
> mode, which generally takes the form of a state machine, is implicit in the
> codebase."

And on what changes:

> "Temper makes that state machine explicit. The agent produces a precise
> description, not arbitrary code…Agents can change it dynamically, with safety,
> and hot-reload it without going through CI."

Three consequences follow from making the state machine data:

- An agent can **read** the whole control logic without reading the whole codebase.
- An agent can **modify** it as a bounded diff instead of an edit across five files.
- A change can **hot-reload under policy** instead of taking a CI cycle.

## Source

[How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code) — Michael Segner, July 21, 2026
