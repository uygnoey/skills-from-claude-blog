**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# A Guide to Cost Visibility and Control in Claude

## What is this post?

A guide for IT administrators and developers on how to see and control what an organization
spends on Claude. Its central argument is that **cost-per-outcome**, not token consumption,
is the right primary metric of value — and that most cost problems are model-matching
problems in disguise.

The guide covers three surfaces: how to think about cost in the first place, the admin
controls available in Claude Enterprise (access gating, model controls, hard spend caps),
the tools for observing usage (usage analytics, the Analytics API, Analytics Chat), and the
levers available to developers building on the API (prompt caching, batch processing, the
effort parameter, and the advisor strategy).

## When is it useful?

- Rolling Claude Code or Claude Cowork out to an organization and deciding who gets access
  first.
- Setting a budget and needing spend to actually stop at it.
- Reconciling Claude spend against invoices, or feeding usage data into a BI or finance system.
- Deciding which model a workload should run on, and whether a cheaper model is actually
  cheaper.
- Reducing the cost of a production API workload without giving up quality where it matters.

## Key points

- **Measure cost-per-outcome, not tokens.** Two questions to ask about any project: what
  would this work have cost without AI (in resources, in time, or in whether it would have
  been attempted at all), and is the model doing judgment-and-reasoning work or high-volume
  straightforward work?
- **Mismatched models cost more, in both directions.** Putting a less capable model on
  complex reasoning often raises final cost through retries and human correction. Putting a
  frontier model on basic document processing pays for capability the task never uses.
- **Four models, four kinds of work.** Fable for the hardest problems, Opus for long-horizon
  work and coding, Sonnet for everyday work and analysis, Haiku for high-volume and routine
  tasks.
- **Enterprise controls, in order:** *access gating* (which groups and custom roles can use
  which products, so rollout can be phased by department), then *model controls*
  (entitlements for which models a team can reach, and defaults for what new conversations
  start on), then *hard spend caps* (ceilings at org, user, or group level; each member of a
  group receives the specified limit; caps take effect immediately).
- **Observation tools.** Usage analytics break spend down by person, team, and model, with
  exports aligned to invoices. The Analytics API pushes the same data into existing BI,
  finance, and dashboard systems. Analytics Chat answers usage questions in natural
  language — "Who are our top spenders this month?", "Which team's usage grew fastest this
  quarter?" — without generating a full report.
- **API-side levers.** Prompt caching stores reusable content across requests and can bring
  cache hits to roughly 10% of the normal input rate. Batch processing runs non-urgent jobs
  at half price and stacks with caching. The effort parameter tunes reasoning intensity per
  call. The advisor strategy runs most work on a smaller model and consults a frontier model
  only at critical decision points.
- **Admins can also** automate spend-limit increase requests, identify users approaching
  their limits, and track rapidly changing usage patterns.

## Bundled resources

- `skills/cost-aware-model-selection/SKILL.md` — the decision procedure as an Agent Skill.
- `skills/cost-aware-model-selection/references/model-family.md` — which model fits which work.
- `skills/cost-aware-model-selection/references/enterprise-controls.md` — the three admin
  controls and the order to apply them.
- `skills/cost-aware-model-selection/references/api-cost-controls.md` — caching, batching,
  effort, and the advisor strategy.
- `skills/cost-aware-model-selection/templates/cost-per-outcome-review.md` — a worksheet for
  evaluating a workload.
- `skills/cost-aware-model-selection/examples/usage-questions.md` — analytics questions and
  what they are for.
- `guides/cost-visibility-and-control.en.md` — the full guide in four languages.

## Source

- [A Guide to Cost Visibility and Control in Claude](https://claude.com/blog/a-guide-to-cost-visibility-and-control-in-claude) — published 2026-08-04
