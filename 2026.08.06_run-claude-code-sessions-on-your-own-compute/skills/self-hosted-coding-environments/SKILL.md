---
name: self-hosted-coding-environments
description: Decide whether to run agentic coding sessions on self-hosted infrastructure instead of the vendor-hosted default, then size and operate that environment. Use when network isolation, pre-installed internal toolchains, or keeping source and build artifacts on controlled infrastructure are hard requirements; when choosing between fixed and on-demand runner capacity; when clarifying the data boundary (what stays local vs. what is sent for inference); or when assigning ongoing ownership of runner images and orchestration to a platform, DevEx, or developer-productivity team.
---

# Self-hosted agent coding environments

Self-hosted environments run agent coding sessions on infrastructure the
organization provisions, inside its own network, rather than on vendor-hosted
systems. Sessions started from any supported surface — web, mobile, desktop, or
a scheduled routine — route into the same environment.

This skill covers the decision, the architecture, and the ownership commitment.
It does **not** reproduce the setup commands; those live in the official
documentation linked at the bottom.

## Instructions

### 1. Test whether self-hosting is actually required

Default to the hosted offering. It has no infrastructure to run or maintain,
and for most organizations that operational simplicity is the right trade.

Move to self-hosting only when at least one of these is a hard requirement:

- **Network access** — sessions must reach internal services, databases, or
  package registries that are not exposed to the public internet.
- **Customizability** — every session must start with company compilers, SDKs,
  and internal CLIs already installed and ready to build.
- **Compliance** — source code and build artifacts must remain on
  infrastructure the organization controls.

If none of these applies, self-hosting adds an operational burden without
buying anything. Work through
[references/decision-criteria.md](references/decision-criteria.md) before
committing.

### 2. Check eligibility before designing anything

Three gates, all from the announcement:

- Available in **public beta** to organizations on Team and Enterprise plans.
- **Off by default** — it must be enabled deliberately.
- **Not available** to organizations using ZDR.

A design effort that skips these gates can be wasted entirely.

### 3. State the data boundary out loud

Self-hosting is not the same as "nothing leaves the network." Be precise with
security reviewers, because the distinction is what the review will turn on:

- **Stays on infrastructure you provision:** repository checkouts, build
  artifacts, secrets, and any file a session creates or modifies.
- **Sent to the vendor for inference:** the conversation itself — prompts,
  responses, and tool results, which can include code the model reads. The
  session transcript is stored so a session can be resumed from any surface.

Presenting self-hosting as full data residency will fail review later. Say what
it does and does not move.

### 4. Choose a runner mode

Execution happens on **runners**: long-lived processes that pick up sessions and
start one agent process per session.

- **Fixed** — a set number of runners stay up; sessions are distributed across
  them. Simplest to reason about; capacity is a standing cost.
- **On-demand** — an orchestrator watches for queued sessions, starts runners as
  sessions arrive, and stops them when work finishes, so capacity tracks demand.
  Adds the orchestrator as a component you must run and maintain.

Pick fixed unless demand is spiky enough that idle capacity is the dominant
cost. On-demand buys elasticity and charges an operational component for it.

See [references/architecture.md](references/architecture.md) for how runners,
sessions, and isolation fit together.

### 5. Rely on per-session isolation, not per-runner isolation

A single runner can serve more than one session. Isolation comes from each
session getting its own checkout, which is what keeps work separated between
developers and between accounts. Do not design a "one runner per developer"
scheme expecting it to be the isolation boundary — it isn't the mechanism, and
it wastes capacity.

### 6. Do not confuse this with Remote Control

They solve different problems and get mixed up constantly:

| | Self-hosted environments | Remote Control |
|---|---|---|
| Where the session runs | Shared infrastructure a platform team operates | The developer's own machine |
| Who can use it | Any user in the organization | The user who ran the CLI |
| Lifetime | Independent of any one laptop | Ends when that machine stops running the session |
| Purpose | Run sessions on controlled infrastructure | Continue a local session from a phone or browser |

### 7. Assign an owner before you enable it

The announcement is direct about staffing: plan on a platform, developer
experience, or developer productivity team owning setup **and ongoing
operation**. Concretely that means:

- Building and maintaining the runner image.
- Updating runners.
- Running the orchestrator, if you chose on-demand mode.

If no team will hold this, the answer to step 1 is the hosted offering. Use
[templates/rollout-checklist.md](templates/rollout-checklist.md) to make the
ownership explicit before enabling the feature.

## Examples

### Example 1 — the requirement is real, and fixed mode fits

A platform team's build system depends on an internal artifact registry that is
not reachable from the public internet, and their SDK setup takes several
minutes per machine.

Both the network-access and customizability criteria apply, so self-hosting is
justified. Engineer count is stable and sessions run through the working day, so
idle capacity is not the dominant cost: **fixed mode**. The runner image is
built with the internal SDKs and CLIs preinstalled so sessions start ready to
build. The DevEx team takes ownership of the image and its updates. The security
review is given the data boundary from step 3 in writing — checkouts and
artifacts local, conversation and transcript sent for inference.

### Example 2 — the requirement is not real

A team wants self-hosting because "our code shouldn't leave our network."
Working through step 3 shows this expectation is not met: tool results, which
can include code the model reads, are still sent for inference. Their services
are all reachable over the public internet and their toolchain is standard, so
neither of the other two criteria applies either.

The correct outcome is to stay on the hosted offering and route the underlying
concern to the actual data-handling terms, rather than to spend a platform team
on infrastructure that would not have addressed it.

### Example 3 — spiky demand, on-demand mode

Sessions cluster around a nightly routine and are near zero otherwise.
**On-demand mode**: the orchestrator starts runners as queued sessions arrive
and stops them when the batch finishes. The team accepts the orchestrator as a
component they now operate, and puts it on the rollout checklist alongside the
runner image.

## Source

- https://claude.com/blog/run-claude-code-sessions-on-your-own-compute (August 6, 2026)
- Setup and implementation details: https://code.claude.com/docs/en/self-hosted-environments
