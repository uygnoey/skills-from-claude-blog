---
name: supervised-risk-analyst
description: Build an analyst agent that works alongside human experts in a high-stakes domain — surfacing insights and forming opinions on exposure, while logging its reasoning, testing actions in sandboxes, and requiring expert approval before decisions count. Use when designing an AI teammate for risk, compliance, or another regulated analytical function; when outputs must be auditable back to their reasoning; when analysis depends on proprietary data plus judgment the firm will not delegate; or when the job is to explain how numbers changed since yesterday rather than answer one-off questions.
---

# Building a supervised analyst agent

Derived from the announcement that Anthropic and Millennium — one of the world's
largest alternative investment management firms — are co-developing a *digital
risk analyst*: an AI teammate that works alongside and under the supervision of
the firm's risk managers, surfacing new risk insights and forming opinions on
risk exposure across asset classes.

The organizing claim from the post: AI can raise the bar for what people
achieve while human judgment stays at the center of decision making. Everything
below follows from that split.

## Instructions

### 1. Scope the agent as a teammate, not an oracle

The analyst in the post is explicitly designed to work *alongside and under the
supervision of* risk managers. It expedites and enriches the analysis of risk
positions; it does not own the call.

- Name the human role the agent reports into. In the post that role is the risk
  manager, and its findings are validated and enriched by those managers.
- Write down the workflows the agent is meant to tackle. Millennium's analyst
  targets critical risk workflows, not the whole risk function.
- Write down what stays with the human: the decision, and the judgment behind
  it.

Use [templates/analyst-charter.md](templates/analyst-charter.md) to capture
this before any tooling is built.

### 2. Combine proprietary data with frontier reasoning

The analyst is powered by the firm's proprietary data plus the model's frontier
intelligence. Neither half works alone: the model has never seen the firm's
positions, and the positions do not interpret themselves.

- Inventory the proprietary sources the analyst must reach, and the access path
  for each.
- Curate the firm's own guidance — how the function measures exposure, what
  counts as material — as context the agent reads before reasoning.
- Treat industry background the model already has as a starting point that the
  firm's data corrects, not as an answer.

### 3. Give the analyst memory, so it can explain change

The post highlights that the analyst retains and recalls information over time,
and applies new reasoning capabilities to help explain daily risk changes. That
is a different job from answering a question in isolation.

- Persist what the analyst concluded, and on what evidence, each cycle.
- On the next cycle, have it compare today's position against what it recorded,
  and explain the delta rather than restating the level.
- Carry forward what it learned from the last question into the next one.

Worked through in
[examples/daily-risk-change-review.md](examples/daily-risk-change-review.md).

### 4. Make human validation a step in the workflow

Findings are validated and enriched by human risk managers. "Enriched" matters:
the review is not just a pass/fail gate, it is where domain knowledge is added.

- Ship findings in a form a reviewing expert can correct in place — claim,
  evidence, and the reasoning that connects them.
- Capture the expert's additions back into the record, so the enrichment is not
  lost when the next cycle starts.
- Require approval before a decision is acted on, not after.

### 5. Build the three auditability controls in from the start

The post states the analyst provides secure, auditable analysis by doing three
things. Treat them as requirements, not enhancements:

1. **Logs its reasoning** — the chain from data to conclusion is recorded.
2. **Tests its actions in sandboxed environments** — actions are exercised
   somewhere they cannot affect production positions.
3. **Requires human experts to evaluate and approve its decisions** — approval
   is a gate, and the approver is an expert in the domain.

Spelled out as requirements in
[references/auditability-controls.md](references/auditability-controls.md).

### 6. Co-develop inside a lab, with the domain experts in the room

Millennium's risk experts are building the analyst with Anthropic's research and
applied AI teams working alongside them in Millennium's AI lab. The lab also
pressure-tests the latest models against ambitious use cases.

- Put the people who own the domain and the people who own the model in the
  same working group, rather than passing requirements between them.
- Use the lab to test frontier models against the hard cases before those cases
  reach production.
- Expect the target to move: what the lab proves possible this quarter defines
  next quarter's scope.

## Examples

**Standing up an analyst for a new exposure type.** Fill in the charter: the
agent surfaces insights on the exposure and forms an opinion; the risk manager
validates, enriches, and decides. Connect the proprietary position data and the
firm's measurement guidance. Turn on the reasoning log from day one. Run every
action against a sandbox copy of the environment until the reviewing experts
sign off on a full cycle.

**Explaining a daily move.** The analyst recalls yesterday's recorded position
and reasoning, compares it against today's data, and produces a candidate
explanation of the change with the evidence attached. The risk manager reads
the reasoning, corrects the parts that miss firm-specific context, and the
correction is written back for the next cycle. See
[examples/daily-risk-change-review.md](examples/daily-risk-change-review.md).

**Deciding whether an action is allowed yet.** A proposed action that has only
ever run in the sandbox, or that no domain expert has approved, does not
execute. The gate is structural — it is the same gate for a routine
recalculation and for a novel one.

**Pressure-testing a new model in the lab.** Take the most ambitious use case
the function has, run it against the newest model in the lab environment
alongside the domain experts, and let the result — not the roadmap — decide
what moves into the supervised workflow.

## Source

- https://claude.com/blog/millennium-and-anthropic-are-building-a-digital-risk-analyst-with-claude (August 6, 2026)
