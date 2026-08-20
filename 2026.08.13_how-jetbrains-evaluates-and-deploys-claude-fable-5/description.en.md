**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An interview with Vladislav Tankov, CTO at JetBrains Agent Systems, on how JetBrains evaluates a newly released frontier model, decides which of its workloads should move to it, and sets the safeguards around it before it reaches customers. JetBrains serves 12.5 million active users and 88 of the Fortune Global 100, so the deployment question carries real weight.

The through-line is that public benchmark scores are a hypothesis, not an answer. JetBrains runs large evaluation sets on private repositories — including its own monorepo — checks whether a model's real-world behaviour matches its published scores, and keeps three separate leaderboards (best quality, best cost-per-task, fastest) so that different workloads can pick different winners.

## When is it useful?
- When a new frontier model ships and you need a defensible answer to "should we adopt it," backed by your own code rather than a leaderboard.
- When you are choosing between models per workload instead of picking one default for everything.
- When a per-token price comparison is being used to make a decision that should be made on cost per completed task.
- When deciding what your organization owes on safety versus what you can reasonably expect from the model provider.
- When you need a position on data retention that survives a security review.

## Key points
- **Evaluate on private repositories.** Tasks the model could not have trained on, carrying your conventions and your build system. Tankov's warning is that some models are tuned to score well on public benchmarks but fall down on actual tasks.
- **Three leaderboards, not one** — best quality, best cost-per-task, fastest. Collapsing them into a single ranking destroys the information you need to route work.
- **Cost per task, not cost per token.** Claude Fable 5 carries higher per-token costs but lower per-task costs on complex, long-running work, because it needs fewer steps.
- **The reported numbers.** 44.3% Python pass rate against 28.2% for Opus 4.8 — roughly 16 points. Head-to-head, Fable 5 solved 18 Python tasks Opus 4.8 missed while losing 2. Solutions arrived in about 22% fewer steps.
- **Weight the runs-but-wrong rate.** When Fable 5's code executed it passed tests far more often; code that runs but produces a wrong answer is the most expensive kind of failure to catch.
- **Steps-to-solution is a habits signal.** On a Java task the older model repeatedly tried to pull an external resource it did not need. Tankov reads the difference as better engineering habits more generally.
- **Route, don't replace.** Opus stays the workhorse — you can be very sure it will do the work. Fable 5 is reserved for when you really need good reasoning, when you almost need a partner: an intricate rich text editor component that resisted several earlier attempts, and long-running agentic runs that implement IDE-like applications from a text-and-image spec or rewrite an existing app into another runtime, framework, or language.
- **Safety is a harness problem.** JetBrains is not trying to build the safest model itself; it expects the provider's red teaming to be sufficient and puts its own effort into the safety net around the model — systematic deployment, infrastructure, harness design.
- **Turn the model on your own products.** White-box security testing against JetBrains software, on the assumption that external threat actors will use comparable models against it.
- **Data retention, stated explicitly.** The preference is zero retention; limited retention scoped to investigating the most serious flagged cases is accepted as a fair tradeoff, because otherwise nobody can tell where a classifier worked incorrectly. The tension is named: aggressive classifiers make defensive security work harder.
- **What's next** is described less as model capability and more as a cockpit for software development — a space where agents and people collaborate, with governance and clarity on return on investment.

## Bundled resources
- `skills/frontier-model-evaluation/SKILL.md` — the evaluation-and-routing method, end to end.
- `skills/frontier-model-evaluation/references/evaluation-dimensions.md` — the six dimensions worth scoring separately, and how to compute each.
- `skills/frontier-model-evaluation/templates/leaderboard-record.md` — a per-round record for the three leaderboards, the routing decision, and the deployment posture.
- `skills/frontier-model-evaluation/examples/private-eval-comparison.md` — the JetBrains round walked through as a worked example.
- `guides/frontier-model-evaluation-and-deployment.{en,ko,es,ja}.md` — the same material as a four-language guide.

## Source
- https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5 (August 13, 2026)
