---
name: cost-aware-model-selection
description: Decide which model a workload should run on, and which cost controls to apply, using cost-per-outcome rather than token count as the metric. Use when rolling a product out to an organization, setting or enforcing a spend budget, reconciling spend against invoices, choosing between a frontier and a smaller model for a workload, or reducing the cost of a production API workload without losing quality where it matters. Covers the model family, enterprise admin controls (access gating, model controls, hard spend caps), usage observation tools, and API-side levers (prompt caching, batch processing, the effort parameter, and the advisor strategy).
---

# Cost-Aware Model Selection and Control

Token consumption is a poor primary metric of value. The metric that matters is
**cost-per-outcome**: what the work produced, against what it cost to produce it.

Most cost problems turn out to be model-matching problems. A model that is too small for the
reasoning it is being asked to do burns tokens on retries and then burns human time on
correction — the cheap model produces the expensive outcome. A frontier model doing basic
document processing pays for capability the task never uses.

## Instructions

### Step 1 — Frame the workload in cost-per-outcome terms

Ask two questions about any project before touching a model setting:

1. **What would this work have cost without AI?** Count resources and time — and count
   whether the project would have been attempted at all. Work that would never have been
   started has no baseline to be expensive relative to.
2. **What kind of work is the model doing?** Judgment and reasoning, or high-volume
   straightforward processing? These have different right answers and the difference is not
   about volume.

Use [templates/cost-per-outcome-review.md](templates/cost-per-outcome-review.md) to work
through this on a specific workload.

### Step 2 — Match the model to the work

Pick from the family by the kind of work, not by price:

- **Fable** — the hardest problems
- **Opus** — long-horizon work and coding
- **Sonnet** — everyday work and analysis
- **Haiku** — high-volume and routine tasks

Then apply the two cross-cutting adjustments: **effort controls**, which adjust how much the
model thinks when solving a problem, and the **advisor** approach, which lets a smaller model
consult a frontier model only when it hits something difficult.

See [references/model-family.md](references/model-family.md) for how to place a workload and
the failure modes of getting it wrong in each direction.

### Step 3 — If you are an administrator, apply controls in order

Apply these in sequence. Each one narrows the surface the next one has to cover.

1. **Access gating** — decide which groups and custom roles can access which products, so
   rollout is phased by department instead of switched on organization-wide.
2. **Model controls** — set *entitlements* (which models a team can reach) and *defaults*
   (which model new conversations start on). Restrict the most capable models to teams doing
   complex work; default everyone else to Sonnet.
3. **Hard spend caps** — set ceilings at the organization, individual user, or group level.
   A cap on a group gives each member the specified limit. Caps take effect immediately.

See [references/enterprise-controls.md](references/enterprise-controls.md) for the details,
including automating spend-limit increase requests, identifying users approaching their
limits, and tracking rapidly changing usage.

### Step 4 — Observe before you tighten further

Do not guess at where the spend is. Three tools answer different questions:

- **Usage analytics** — spend broken down by person, team, and model. Exports align with
  invoices, so this is what you reconcile billing against.
- **Analytics API** — the same data pushed into existing business systems: BI tools, finance
  systems, internal dashboards.
- **Analytics Chat** — natural-language questions about usage, when you want an answer rather
  than a report.

See [examples/usage-questions.md](examples/usage-questions.md) for the questions worth asking
and which tool answers each.

### Step 5 — If you are building on the API, apply the four levers

- **Prompt caching** — store reusable content across requests. Cache hits cost roughly 10% of
  the normal input rate.
- **Batch processing** — run non-urgent jobs at half price. Batch discounts stack with caching.
- **The effort parameter** — control reasoning intensity per call. Low for routing and
  extraction; high for the final recommendation. The point is to choose *when* you pay peak
  rates.
- **The advisor strategy** — run most work on Sonnet and consult a frontier model only at
  critical decision points, so you pay premium rates only for high-judgment moments.

See [references/api-cost-controls.md](references/api-cost-controls.md) for how these combine.

## Examples

### A cheaper model that costs more

A document-classification pipeline is moved to the smallest available model to cut spend. Token
cost per call drops. But the classifications now need a second pass and a human spot-check, and
the failures cluster on exactly the ambiguous documents that mattered. Cost-per-outcome went up
even though cost-per-token went down. This is the failure mode the guide names directly:
assigning less capable models to complex reasoning often increases final costs through retries
and human correction.

### A rollout that does not blow the budget

An organization enabling Claude Code starts with access gating — engineering only, not the whole
company. Model controls give engineering entitlement to the capable models and default everyone
else to Sonnet. Hard spend caps go on at the group level, so each engineer gets the specified
limit rather than the team racing for a shared pool. Only then does the admin turn on usage
analytics and watch for a week before widening access.

### An API workload tuned four ways

An overnight catalog classification job runs in batch at half price. The shared taxonomy and
instructions live in a cached prefix, so the repeated portion of each request bills at roughly
10% of the normal input rate — and the batch discount stacks on top. Per-item extraction runs at
low effort. Only the final merge-and-recommend step runs at high effort, and only that step
consults the frontier model, following the advisor strategy.

### Asking where the money went

Rather than exporting a full report, an administrator asks Analytics Chat "Who are our top
spenders this month?" and "Which team's usage grew fastest this quarter?" — then uses the
Analytics API to pipe the underlying numbers into the finance dashboard where they will be
reconciled against the invoice.

## Source

- [A Guide to Cost Visibility and Control in Claude](https://claude.com/blog/a-guide-to-cost-visibility-and-control-in-claude), 2026-08-04
