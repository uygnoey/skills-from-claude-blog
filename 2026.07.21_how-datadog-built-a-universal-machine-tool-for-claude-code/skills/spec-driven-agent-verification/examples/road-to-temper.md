# The road to Temper

Temper did not arrive as a design. Three earlier projects at Datadog each moved
the bottleneck one step, and each move is worth reading as a diagnosis you can
apply to your own system.

## Courier (2024) — a distributed queuing system

The lesson was about where difficulty actually lives. As Sesh Nalla, VP of
engineering at Datadog, put it:

> "The difficulty was not building the parts; it was making the interactions
> between them observable, testable, and verifiable."

Courier emphasized formal modeling. The takeaway that survives into Temper: parts
are cheap, *interactions* are what need proof, and the only interactions you can
prove things about are the ones written down explicitly.

**Diagnostic for your own system:** can you name your system's states and
transitions without opening a file? If not, the interactions are implicit, and
nothing downstream can verify them.

## BitsEvolve (September 2025) — closed-loop evolutionary optimization

Variant generation under feedback. Sesh:

> "This was the first glimpse for me that parts of software could be cultivated
> like living organisms — grown through variation with feedback, and adaptation."

The idea that carries forward: if the feedback loop is closed and automated,
software can be *grown* rather than authored. But growth without proof is just
drift — which is why the verification kernel had to come next.

**Diagnostic:** is there a closed loop between what your agents produce and a
signal that tells them whether it was good? If a human is the only signal, the
loop runs at human speed.

## Helix — Kafka-comparable streaming, built mostly by Claude Code

> "To our disbelief, in a few days we had a fully functional Kafka comparable
> system."

And then the bottleneck moved again — not to generation, and not even to review:

> "The bottleneck moved again where agents could build large parts of the
> system…but then humans still have to coordinate to ship the work to production
> through tools and mechanisms built for humans."

This is the specific observation Temper's tool-builder layer answers. The SDLC
tooling — Git, CI, deployment — was built on the assumption that a human is
driving it. When agents can build the system in days, human-shaped tooling
becomes the slow part.

**Diagnostic:** measure the time from "agent finished" to "running in
production." If that number dwarfs the build time, your constraint is the
coordination surface, not the agents.

## Where it landed

Each step exposed the next constraint:

| Project | Constraint it exposed |
| --- | --- |
| Courier | Interactions between parts are the hard thing to verify |
| BitsEvolve | Software can be grown in a closed loop, if the loop is automated |
| Helix | Agents outrun human-shaped SDLC tooling |
| **Temper** | So: make control logic an explicit, verified, hot-reloadable spec, and give agents the machine tool to operate it |

And what the article suggests is next:

> "If agents can build software autonomously inside factories with this kind of
> discipline, maybe we don't need to stop at dark factories. Software built this
> way starts to feel like an organism we can grow, cultivate, and evolve through
> feedback, selection, and adaptation."

## Source

[How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code) — Michael Segner, July 21, 2026
