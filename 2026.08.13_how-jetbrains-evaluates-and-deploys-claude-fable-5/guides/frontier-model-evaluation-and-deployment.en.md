**English** · [한국어](./frontier-model-evaluation-and-deployment.ko.md) · [Español](./frontier-model-evaluation-and-deployment.es.md) · [日本語](./frontier-model-evaluation-and-deployment.ja.md)

# Evaluating and deploying a frontier model

A guide to the decision a tooling company faces on every frontier model release: is this
model better *for us*, which of our workloads should move to it, and what has to be true
around it before it reaches customers. The material comes from an interview with
Vladislav Tankov, CTO of JetBrains Agent Systems, on how JetBrains evaluated and deployed
Claude Fable 5 — a company serving 12.5 million active users and 88 of the Fortune
Global 100.

## The starting position

The interesting shift is not that model quality improved. It is that the internal argument
ended. A company that once had sceptics reached the point where AI being here to stay is
simply assumed, and the open questions moved downstream: which model, for which job, under
what safeguards.

That reframing is what makes the rest of this guide a repeatable process rather than a
one-time adoption decision.

## Evaluate on your own repositories

Public benchmark scores are a hypothesis. Some models are tuned to score well on them and
fall down on actual tasks, so the first job of an evaluation is to check whether the
public number survives contact with your codebase.

The practice that follows:

- **Private eval sets on private repositories**, including the company monorepo. Tasks
  drawn from work the model could not have trained on, carrying your conventions and your
  build system.
- **Verify benchmark claims** against real-world tasks explicitly, and treat a gap between
  the two as information about how the model was tuned.
- **Three leaderboards, not one** — best quality, best cost-per-task, fastest. Different
  workloads pick different winners, and a single ranking destroys exactly the information
  you need to route work.

The cost-per-task leaderboard deserves emphasis. A model can carry higher per-token costs
and still be the cheaper option for complex, long-running work, because it reaches the
answer in fewer steps. A per-token comparison points the wrong way on precisely the
workloads where the stakes are highest.

## What to measure

| Dimension | What it tells you |
|---|---|
| Pass rate, per language | The headline gap, and where it is concentrated |
| Head-to-head win/loss | Whether the gain is a uniform lift or a lopsided trade |
| Ran-but-wrong rate | Exposure to the most expensive failure mode |
| Steps to solution | Cost multiplier, and a proxy for engineering judgment |
| Cost per completed task | The number that actually governs routing |
| Latency | The deciding dimension for interactive in-editor use |

In the JetBrains round, Claude Fable 5 passed 44.3% of Python tasks against 28.2% for
Opus 4.8, solved 18 Python tasks the older model missed while losing 2, and reached
solutions in roughly 22% fewer steps.

Two results deserve more attention than the headline. First, when Fable 5's code ran, it
passed tests far more often — and code that runs but produces a wrong answer is the most
expensive kind of failure to catch, because it consumes reviewer attention and can reach
production. Second, on a Java task the older model repeatedly tried to pull an external
resource it did not need while the newer one skipped it. Tankov reads that as better
engineering habits more generally — the kind of finding a pass rate cannot surface, which
is why steps-to-solution is worth logging separately.

## Route work rather than switching wholesale

Adoption was not a replacement. Both models stayed in service with different jobs.

- **Opus as the workhorse.** Tankov's framing: you can be very sure it will do the work.
  That is the right default for routine, high-volume tasks where confidence matters more
  than reasoning depth.
- **Fable 5 where the path is unknown.** Reserved for when, in his words, you really need
  good reasoning — when you almost need a partner. Concretely: a tech lead nearly
  one-shotted a rich text editor component that had resisted several earlier attempts.
- **Long-running agentic experiments.** Agents receive a specification in text and images
  and implement sophisticated IDE-like applications; agents also generate a specification
  from an existing application and rewrite it into a different runtime, framework, or
  language in a near black-box setup.

Re-open the routing decision on each release rather than freezing it.

## Deployment posture: build the net, not the model

JetBrains does not attempt to make the model itself safer. The stated expectation is that
the red-teaming and alignment work done on the provider's side is enough to believe the
model is safe; the deploying company's job is the **safety net around the model** —
a systematic deployment approach where safety is guaranteed by infrastructure and harness
design rather than by tweaking the model.

Two consequences worth adopting:

**Point the model at your own products.** White-box security testing against your own
software, on the explicit assumption that external threat actors will use models of the
same class against you. For a vendor serving enterprise and regulated customers, finding
those vulnerabilities first is the whole game.

**Take an explicit position on data retention.** The preference stated is zero retention.
The accepted compromise is retention limited to investigating the most serious flagged
cases, on the reasoning that without it there is no way to understand what was asked or
where a classifier may have worked incorrectly — a fair tradeoff for access to frontier
intelligence. The tension is named rather than hidden: aggressive content classifiers make
a company's own defensive security work harder.

## Where this is heading

The roadmap described is less about model capability — that is assumed to keep improving —
and more about the surface around it: a cockpit for software development, a space in which
agents and people collaborate, with real management of the development process. The
expected outcomes are developers shipping more and better code through agents,
non-technical roles taking a larger part in creating software, and organisations getting
governance and clarity on return on investment.

## Bundled artifacts

- The `frontier-model-evaluation` skill in this post folder — the method as a runnable skill.
- Evaluation dimensions, a per-round leaderboard record template, and a worked comparison
  ship alongside it in that skill folder.

## Source

- https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5 (August 13, 2026)
