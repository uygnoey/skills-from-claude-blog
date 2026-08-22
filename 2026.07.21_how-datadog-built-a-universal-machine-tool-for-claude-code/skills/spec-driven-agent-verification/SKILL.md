---
name: spec-driven-agent-verification
description: Shift an agentic codebase from "agents emit code" to "agents emit verifiable specifications." Use when agents generate code faster than the team can review it and verification has become the real bottleneck, when control logic is scattered across routes, database constraints, service code, background jobs, and docs so no one can state the system's state machine, when agents need to change operational behavior safely without a full CI cycle, or when designing an autonomous build-and-operate loop and deciding what humans must still coordinate. Based on Datadog's Temper, a "universal machine tool" that verifies agent-emitted specs through four independent layers before anything runs.
---

# Spec-driven agent verification

Agent-driven development moves the bottleneck. Generation stops being scarce and
verification becomes the constraint — the gap between what was generated and what
was proven is where failure modes accumulate.

The move this skill encodes: **stop having agents emit control code, and have them
emit specifications that a deterministic kernel outside the model can verify.**
Compilation and proof leave the LLM. The artifact that gets verified is the
artifact that runs.

Background on where this came from is in
[examples/road-to-temper.md](examples/road-to-temper.md).

## Instructions

### 1. Name the bottleneck before optimizing anything

Assume it is verification. Agents already produce code faster than any team can
review, so more generation throughput buys nothing. Ask directly:

- How much generated code is waiting on human review right now?
- Of the last N incidents, how many came from code that was generated but never
  proven — as opposed to code that was never generated fast enough?

If review queue depth is growing, invest in proof, not in throughput.

### 2. Decide what the agent emits

Split the codebase in two:

| Kind of code | What the agent emits | How it is checked |
| --- | --- | --- |
| Control logic (lifecycle, state, permissions, work routing) | A **specification** | Deterministic kernel, four verification layers |
| Arbitrary application code | Code that **carries its proof** | The accompanying proof/tests, verified outside the model |

Keep compilation and proof outside the LLM. The model proposes; the kernel
decides.

### 3. Express every capability as three contracts

A capability is not accepted until all three are present. Full field-by-field
detail is in [references/temper-architecture.md](references/temper-architecture.md);
start from [templates/capability-contract.md](templates/capability-contract.md).

1. **Behavior** — states, transitions, preconditions, safety properties.
2. **Data contract** — entity types, properties, and actions in machine-parseable
   form.
3. **Authorization** — default-deny, scope-based approval, with pending decisions
   and hot-loading so policy can change without a redeploy.

### 4. Run the four verification layers

They are independent on purpose: each catches a class the others miss. Details,
including what each layer proves and what it cannot, are in
[references/verification-layers.md](references/verification-layers.md).

1. **Symbolic reasoning** — proves each guard is satisfiable and each invariant is
   inductive.
2. **Exhaustive state exploration** — visits every reachable state.
3. **Deterministic simulation** — runs production code paths with seeded fault
   injection.
4. **Randomized property testing** — executes roughly 1,000 pseudorandom action
   sequences.

Do not let a spec reach the running system until all four have passed. Because
the layers are deterministic, a failure is reproducible from its seed.

### 5. Pull the state machine out of the codebase and make it data

In a conventional CRUD service the operational mode — almost always a state
machine — stays implicit, spread across routes, database constraints, service
methods, background jobs, and documentation. That is why agents cannot safely
change it.

Make it a transition table an agent can read, modify, and hot-reload under
policy. Scaffold: [templates/transition-table.json](templates/transition-table.json).
Check the shape of a candidate table with:

```
scripts/check_contract.py path/to/transition-table.json
```

The checker verifies only that the three contracts and their named fields are
present and internally consistent. It is a gate before the kernel, not a
substitute for it.

### 6. Keep every artifact human-comprehensible

If a person cannot hold a generated artifact in their head, the verification
story has failed even when every layer passes — nobody can say whether the spec
describes the system that was wanted. Split capabilities until each one fits.

### 7. Close the loop into a dark factory

Once specs are verified deterministically, the same surface can run the whole
build-and-operate loop: an agent control plane (sessions, roles, work queues,
lifecycle), a tool-builder layer bridging SDLC tooling (Git, CI, deployment), and
a control API around the data plane. See
[references/temper-architecture.md](references/temper-architecture.md) for how
these three roles fit together, and note where humans still coordinate.

## Examples

### Example 1 — the review queue is the constraint

> Our team merges maybe 30 PRs a week and Claude Code opens 80. Should we add
> another reviewer agent?

Diagnose the bottleneck first (step 1). Another reviewer raises review throughput
but leaves the same gap between generated and proven. Ask which of those 80 PRs
touch control logic — lifecycle, permissions, work routing. Move that subset to
specs (step 2), give each capability its three contracts (step 3), and let the
kernel verify them (step 4). The remaining PRs are ordinary application code and
should carry their proof.

### Example 2 — nobody can state the state machine

> A user can be `invited`, `active`, or `suspended`, but the rules live in three
> route handlers, a database `CHECK` constraint, and a nightly job.

This is the CRUD failure mode from step 5. Extract the states, the transitions,
the precondition on each transition, and the safety properties that must hold
across all of them into a transition table
([templates/transition-table.json](templates/transition-table.json)). Run
`scripts/check_contract.py` on it, then hand it to the kernel. Once it verifies,
an agent can propose a new transition and hot-reload it under policy instead of
editing three files and waiting for CI.

### Example 3 — an agent wants a new permission

> The deployment agent needs to be able to roll back, not just deploy.

Authorization is a contract, not a code change (step 3). Default-deny means the
rollback scope does not exist until it is granted. The agent proposes the scope;
the grant becomes a pending decision; approval hot-loads it. Nothing about the
running binary changes, and the change is visible as a contract diff rather than
buried in a service method.

## Source

[How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code) — Michael Segner, July 21, 2026
