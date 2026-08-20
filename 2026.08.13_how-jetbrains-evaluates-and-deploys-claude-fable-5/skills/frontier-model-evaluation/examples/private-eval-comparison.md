# Worked example: a private-repo eval round

This walks the method through with the one public data point available — JetBrains'
evaluation of Claude Fable 5 against Opus 4.8 on their own repositories, including their
monorepo. Numbers marked *(reported)* come from the source post; the rest of the walkthrough
shows how to reason from numbers of that shape.

## The setup

- Eval tasks drawn from **private repositories**, not public benchmark suites.
- Explicit goal: check that a model's real-world behaviour matches its public benchmark
  scores, because some models are tuned to score well publicly and fall down on actual
  tasks.
- Standing infrastructure: **three leaderboards** — best quality, best cost-per-task,
  fastest — rather than one ranking.

## What the round produced

| Metric | Claude Fable 5 | Opus 4.8 |
|---|---|---|
| Python pass rate *(reported)* | 44.3% | 28.2% |
| Head-to-head, Python *(reported)* | solved 18 the other missed | solved 2 the other missed |
| Steps to solution *(reported)* | ~22% fewer | baseline |
| Code that ran but was wrong *(reported)* | notably lower | baseline |

A qualitative observation sat alongside the numbers: on a Java task, the weaker model
repeatedly tried to pull in an external resource it did not need, while the stronger model
prioritised correctly and skipped it. That is the kind of thing a pass rate never shows,
and it is why steps-to-solution is worth logging.

## How to read this

**The 16-point pass-rate gap is the headline, not the decision.** Read it together with
the head-to-head split: 18 wins against 2 losses is a lopsided trade, which is a much
stronger adoption signal than the same average produced by a uniform small lift. The 2
lost tasks are still worth inspecting — if they cluster into a recognisable category, that
category keeps routing to the incumbent.

**The runs-but-wrong improvement matters more than the pass rate for autonomous work.**
Failing loudly is cheap. Producing a plausible wrong answer consumes reviewer attention
and can ship. For long-running agentic runs where nobody is watching each step, weight
this dimension above raw pass rate.

**Fewer steps changes the cost arithmetic.** Fable 5 carries a higher per-token price and
a lower per-task price on complex long-running work. That inversion is the entire reason
to keep cost-per-task on its own leaderboard: a per-token comparison would have pointed
the wrong way.

## The routing that followed

| Workload | Model | Why |
|---|---|---|
| Routine, high-confidence work | Opus | Described as the workhorse — you can be very sure it will do the work |
| Reasoning-bound problems | Fable 5 | Used when you need good reasoning and something closer to a partner |
| Intricate component implementation | Fable 5 | A tech lead nearly one-shotted a rich text editor component after several earlier attempts had failed |
| Long-running agentic experiments | Fable 5 | Agents given a spec in text and images implement IDE-like applications; agents also generate specs from an existing app and rewrite it into another runtime, framework, or language in a near black-box setup |
| Security testing of own products | Fable 5 | White-box vulnerability hunting, on the assumption external actors will use comparable models |

Note that adoption was **not** a blanket switch. Both models stayed in service with
different jobs, which is what separate leaderboards are for.

## The posture set around the model

- Safety was treated as a **harness** problem rather than a model problem: the provider is
  expected to have done the red-teaming, and the deploying company guarantees safety
  through systematic deployment — the safety net around the model.
- **Data retention:** the stated preference was zero retention, with limited retention
  accepted only for investigating the most serious flagged cases, on the grounds that
  otherwise nobody can tell when a classifier fired incorrectly — described as a fair
  tradeoff for access to frontier capability.
- A real tension was named rather than papered over: aggressive content classifiers make
  a company's own defensive security testing harder.

## Scale context

The company running this evaluation serves 12.5 million active users and 88 of the
Fortune Global 100, which is why the security-testing and retention questions carry the
weight they do.

## Source

- https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5 (August 13, 2026)
