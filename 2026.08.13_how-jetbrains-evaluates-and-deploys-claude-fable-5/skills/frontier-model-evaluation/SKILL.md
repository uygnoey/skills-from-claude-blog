---
name: frontier-model-evaluation
description: Evaluate a new frontier model on your own private repositories instead of trusting public benchmarks, then decide which work to route to it. Use when a new model ships and you need to answer "is this better for us, and where do we actually use it" — building a private eval set, scoring quality/cost/speed on separate leaderboards, comparing head-to-head against your current default, measuring steps-to-solution and code that runs but is wrong, and setting a deployment posture around the model (harness-level safety, security testing against your own products, data-retention tradeoffs). Based on how JetBrains evaluated and deployed Claude Fable 5.
---

# Frontier model evaluation and routing

A method for deciding whether a newly released model is better *for your codebase*,
and which of your workloads should be routed to it. The premise is that public
benchmark scores are a starting hypothesis, not an answer — some models are tuned to
score well publicly and fall down on real tasks — so the decision has to be made on
private, representative work.

## Instructions

### 1. Build the eval set out of your own work

- Draw tasks from **private repositories**, including your largest monorepo. The point
  is that these tasks cannot have leaked into training data and they carry your real
  conventions, build system, and mess.
- Keep the set large enough that a few-point difference is signal rather than noise.
- Cover more than one language. Behaviour diverges by ecosystem — a model can lead
  clearly on one language and merely tie on another.
- Automate pass/fail with the repo's own tests, so a run can be repeated on every new
  model release without re-litigating the grading.

### 2. Score on the dimensions that actually cost you money

Do not collapse the result into one number. See
[references/evaluation-dimensions.md](references/evaluation-dimensions.md) for the full
list and how to compute each. The core five:

1. **Pass rate** per language.
2. **Head-to-head deltas** — tasks the new model solves that the incumbent misses, and
   tasks it loses. A net gain hidden behind an overall average is a different decision
   than a uniform lift.
3. **Runs-but-wrong rate** — of the attempts whose code executed, how many produced the
   wrong answer. Code that runs and is wrong is the most expensive failure mode to catch,
   so weight it heavily.
4. **Steps to solution** — how many turns/tool calls the model needed. Fewer steps is
   both a cost saving and evidence of better engineering habits (for example, not
   repeatedly reaching for an external resource it does not need).
5. **Cost per task, not cost per token.** A model with a higher token price can be the
   cheaper choice on long-running work if it takes fewer steps and fails less often.

### 3. Keep three leaderboards, not one

Maintain separate rankings for **best quality**, **best cost-per-task**, and **fastest**,
and re-run them on each release. Different workloads pick different winners, and a single
"best model" ranking destroys the information you need for routing. Record results with
[templates/leaderboard-record.md](templates/leaderboard-record.md).

### 4. Route work by the kind of problem, not by prestige

- Make the **dependable model your workhorse** — the default for routine work where you
  mostly need confidence the job gets done.
- Reserve the **strongest reasoning model** for problems where the path to the solution is
  not known up front and you want something closer to a partner than an executor:
  intricate component work, ambiguous specifications, long-running agentic runs that
  rewrite an app across another runtime, framework, or language.
- Re-check the routing after each eval round rather than freezing it.

### 5. Set the deployment posture around the model, not inside it

- Assume model-level safety is the provider's job (red-teaming and alignment work), and
  spend your effort on the **safety net around the model**: the harness, the permissions
  it runs under, the systematic way it gets deployed.
- Use the model **against your own products** in white-box security testing. If a capable
  model can find vulnerabilities in your software, external threat actors with the same
  class of model will too — better that you find them first. This matters most when you
  serve enterprise and regulated customers.
- Take an explicit position on **data retention**. Zero retention is the preferred default,
  but limited retention scoped to investigating the most serious flagged cases is a
  defensible tradeoff, because without it neither side can tell whether a classifier fired
  incorrectly. Decide deliberately and write the decision down.

### 6. Decide, then re-open the decision on the next release

Write the outcome as: which model is now the default, which workloads are routed
elsewhere, what the deployment posture is, and which numbers would change your mind.
Re-run the same eval set on the next release so the comparison stays apples-to-apples.

## Examples

**A new frontier model ships and leadership asks whether to adopt it.**
Run the existing private eval set unchanged. Report per-language pass rates, the
head-to-head win/loss split against the current default, the runs-but-wrong rate, and
the change in steps-to-solution — then recommend a routing change, not a blanket switch.
A worked version of this using the JetBrains numbers is in
[examples/private-eval-comparison.md](examples/private-eval-comparison.md).

**A team argues the new model is too expensive per token.**
Reframe as cost per completed task. If the model needs materially fewer steps and
produces fewer silently-wrong results, the long-running agentic workloads are likely
cheaper on the expensive model even though each token costs more. Route the routine work
to the cheaper model and let both leaderboards stand.

**A tech lead has failed several times to get a complex component implemented.**
This is the signature of a reasoning-bound rather than throughput-bound problem — an
intricate UI component, an ambiguous spec, a cross-framework rewrite. Route it to the
strongest reasoning model rather than retrying on the workhorse.

**Security review before rolling the model out to customers.**
Point the model at your own products in a white-box setting and treat everything it finds
as a live queue. Note the tension explicitly: the more aggressively a provider's
classifiers block security-adjacent prompts, the harder this defensive work becomes.

## Source

- https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5 (August 13, 2026)
