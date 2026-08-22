**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Datadog engineers use Claude Code for production work across four categories — targeted changes, large refactors, replacing major systems, and building entirely new systems. As that scaled, the constraint moved. Sesh Nalla, VP of engineering at Datadog, describes the shift in what engineering work feels like: "You're no longer writing the code; you're shaping the work. You're deciding what the agent should see. What tools it should have, what success means, how failure should be detected…It's like everyone's promoted three levels up into the management chain, which they didn't sign up for because they're engineers."

The structural answer Datadog built is **Temper**, described as a "universal machine tool" for agents. Instead of agents emitting application code for control logic, they emit **specifications**. A deterministic kernel outside the LLM then verifies each specification through four independent layers — symbolic reasoning, exhaustive state exploration, deterministic simulation with seeded fault injection, and randomized property testing — before anything runs. Every capability is expressed as three contracts: behavior, data, and authorization.

The post traces how Temper became possible through three earlier projects (Courier, BitsEvolve, and Helix), then shows Temper operating a "dark factory" for Helix, a Kafka-comparable streaming system that Claude Code built most of in days. It closes with the Datadog team's best practices.

## When is it useful?
- When agents generate code faster than the team can review it, and review — not generation — has become the thing that limits shipping.
- When deciding what an agent should actually emit: arbitrary code, or a specification that a deterministic kernel can verify.
- When control logic is scattered across routes, database constraints, service code, background jobs, and documentation, and no one can say what the system's state machine is.
- When agents need to change operational behavior safely without a full CI cycle every time.
- When building an autonomous build-and-operate loop and deciding what humans still have to coordinate.
- When judging whether generated artifacts have grown past the size a person can hold in their head.

## Key points
- **Assume verification is the bottleneck, not generation.** Agents already produce code faster than any team can review. The gap between what is generated and what is proven is where failure modes pile up, so investment belongs there rather than in more throughput.
- **Agents emit specs for control logic, not code.** For arbitrary code, the article's framing is proof-carrying. Compilation and proof are placed outside the LLM: the spec goes to a deterministic kernel, so the artifact that gets verified is the artifact that runs.
- **Four independent verification layers.** Symbolic reasoning proves each guard is satisfiable and each invariant is inductive; exhaustive state exploration visits every reachable state; deterministic simulation runs production code with seeded fault injection; randomized property testing runs roughly 1,000 pseudorandom action sequences.
- **Every capability carries three contracts.** Behavior (states, transitions, preconditions, safety properties), a data contract (entity types, properties, actions in machine-parseable form), and authorization (default-deny, scope-based approval with pending decisions and hot-loading).
- **Three projects made Temper possible.** Courier (2024), a distributed queuing system where "the difficulty was not building the parts; it was making the interactions between them observable, testable, and verifiable"; BitsEvolve (September 2025), a closed-loop evolutionary optimizer that was "the first glimpse…that parts of software could be cultivated like living organisms"; and Helix, where a Kafka-comparable system appeared in days and the bottleneck moved again — to humans coordinating a release through tools built for humans.
- **Temper plays three roles in the Helix dark factory.** Agent control plane for managed agents (sessions, roles, work queues, lifecycle), tool-builder layer letting agents bridge SDLC tooling (Git, CI, deployment), and the Helix control API as the lifecycle surface around the data plane.
- **Why not a CRUD app.** Claude Code builds CRUD apps well, but there the operational mode — generally a state machine — stays implicit, spread across routes, constraints, service code, jobs, and docs. Temper makes the state machine explicit and data-driven: "The agent produces a precise description, not arbitrary code…Agents can change it dynamically, with safety, and hot-reload it without going through CI."
- **Keep every artifact human-comprehensible.** If a person cannot hold a generated artifact in their head, you are back where you started.
- **Where it points.** "Software built this way starts to feel like an organism we can grow, cultivate, and evolve through feedback, selection, and adaptation."

## Bundled resources
- `skills/spec-driven-agent-verification/` — the working method: shift investment to verification, have agents emit contracts instead of control code, and put the kernel outside the model. Includes references for the four verification layers and for Temper's architecture, templates for a capability contract and a transition table, an example tracing the road from Courier to the dark factory, and a contract-shape checker script.
- `guides/dark-factory-for-agentic-development.{en,ko,es,ja}.md` — the full walkthrough in four languages.

## Source
[How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code) — Michael Segner, July 21, 2026
