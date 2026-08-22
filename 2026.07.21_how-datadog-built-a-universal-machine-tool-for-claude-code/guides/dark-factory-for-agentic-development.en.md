**English** · [한국어](./dark-factory-for-agentic-development.ko.md) · [Español](./dark-factory-for-agentic-development.es.md) · [日本語](./dark-factory-for-agentic-development.ja.md)

# Building a dark factory for agentic development

How Datadog moved from "agents write code" to "agents write verifiable specs," and
what that requires structurally.

## 1. The flow problem

Engineering flow used to be a direct relationship between intent and code. You
understood the problem, wrote the code, tested it, reviewed it, shipped it,
operated it, repeated. Agents changed the abstraction, and quickly.

Sesh Nalla, VP of engineering at Datadog, on what the job became:

> "You're no longer writing the code; you're shaping the work. You're deciding
> what the agent should see. What tools it should have, what success means, how
> failure should be detected…It's like everyone's promoted three levels up into
> the management chain, which they didn't sign up for because they're engineers."

Datadog engineers use Claude Code across four categories of production work:
targeted changes, large refactors, replacing major systems, and building entirely
new systems. At that scale the promotion is not a metaphor — it is a real change
in what an engineer's day contains, and the tooling underneath it was built for
the previous job.

> "This is the point where I felt we needed something more structural. If agents
> are going to build and operate large parts of our systems, of our databases,
> which are mission critical, they need the equivalent of this machine tool
> concept. Temper is that machine tool for Datadog."

## 2. Three projects that made Temper possible

**Courier (2024)**, a distributed queuing system built with heavy formal
modeling. The lesson: "The difficulty was not building the parts; it was making
the interactions between them observable, testable, and verifiable."

**BitsEvolve (September 2025)**, closed-loop evolutionary optimization through
variant generation with feedback. The lesson: "This was the first glimpse for me
that parts of software could be cultivated like living organisms — grown through
variation with feedback, and adaptation."

**Helix**, a Kafka-comparable streaming system that Claude Code built most of in
days. "To our disbelief, in a few days we had a fully functional Kafka comparable
system." And then the constraint relocated:

> "The bottleneck moved again where agents could build large parts of the
> system…but then humans still have to coordinate to ship the work to production
> through tools and mechanisms built for humans."

That sentence is the specification for what came next. The SDLC tooling assumes a
human driver. When the build takes days, the human-shaped coordination surface
becomes the slow part.

## 3. Temper: agents emit specs, a kernel proves them

The core inversion: agents do not produce application code for control logic.
They produce **specifications**. A deterministic kernel — outside the LLM —
verifies each one before it runs.

Putting compilation and proof outside the model matters for a specific reason:
the artifact that gets verified is the artifact that runs. There is no step where
a proven description is re-implemented by hand into something that might differ.

### The four verification layers

Independent by design, so each covers the others' blind spots:

1. **Symbolic reasoning** proves each guard is satisfiable and each invariant is
   inductive.
2. **Exhaustive state exploration** visits every reachable state.
3. **Deterministic simulation** runs production code with seeded fault injection.
4. **Randomized property testing** runs approximately 1,000 pseudorandom action
   sequences.

Determinism is what makes this usable in an agentic loop. A failure comes back
with a seed, so the agent gets the exact failing execution rather than a
description of one.

### The three contracts

Every capability requires all three:

- **Behavior** — states, transitions, preconditions, safety properties.
- **Data contract** — entity types, properties, and actions in machine-parseable
  form.
- **Authorization** — default-deny, scope-based approval with pending decisions.

Default-deny with pending decisions is what turns "the agent wants more
permission" from an incident into a reviewable diff.

## 4. The dark factory for Helix

Temper plays three roles at once for the Helix dark factory:

1. **Agent control plane** — sessions, roles, work queues, and lifecycle for the
   managed agents.
2. **Tool-builder layer** — lets agents bridge SDLC tooling: Git, CI, deployment.
   This is the direct answer to the post-Helix bottleneck.
3. **Helix control API** — the lifecycle surface around the data plane.

The third role is what makes it a machine tool rather than a build pipeline: the
control plane for the agents and the control plane for the product they are
building are the same explicit, verified surface.

## 5. Why not just build a CRUD app?

Claude Code builds CRUD apps well. That is not the objection. The objection is
where the control logic ends up:

> "In normal CRUD apps, the control logic is spread across routes, database
> constraints, service code, background jobs, and documentation…the operational
> mode, which generally takes the form of a state machine, is implicit in the
> codebase."

Implicit control logic cannot be verified, and cannot be safely changed by an
agent, because there is no single artifact to change. Temper's answer:

> "Temper makes that state machine explicit. The agent produces a precise
> description, not arbitrary code…Agents can change it dynamically, with safety,
> and hot-reload it without going through CI."

Three things follow from making the state machine data rather than code:

- An agent can read all the control logic without reading the whole codebase.
- A change is a bounded diff, not an edit across five files.
- It can hot-reload under policy instead of consuming a CI cycle.

## 6. Where this is going

> "If agents can build software autonomously inside factories with this kind of
> discipline, maybe we don't need to stop at dark factories. Software built this
> way starts to feel like an organism we can grow, cultivate, and evolve through
> feedback, selection, and adaptation."

## 7. Best practices from the Datadog team

**Is your real bottleneck generation or verification?**
Assume verification. Agents already produce code faster than any team can review;
the gap between what's generated and what's proven is where the failure modes
pile up. Invest there, not in more throughput.

**What should the agent actually emit?**
Specs for control logic (not code), and proof carrying for arbitrary code. Put
compilation and proof outside the LLM — hand the spec to a deterministic kernel
so the artifact that gets verified is the artifact that runs.

**Is your control logic explicit, or scattered across the codebase?**
Pull the state machine out of routes, service methods, and background jobs and
make it data: a transition table an agent can read, modify, and hot-reload under
policy.

**Can a human hold each artifact in their head to comprehend?**
If not, you're back where you started. Keep every generated piece small enough to
reason about.

## Source

[How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code) — Michael Segner, July 21, 2026
