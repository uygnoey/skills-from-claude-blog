**English** · [한국어](./self-hosted-session-environments.ko.md) · [Español](./self-hosted-session-environments.es.md) · [日本語](./self-hosted-session-environments.ja.md)

# Running agent coding sessions on your own compute

A deployment guide derived from the August 6, 2026 announcement of self-hosted
environments for Claude Code (public beta).

## What changes

By default, agent coding sessions execute on vendor-hosted infrastructure. With
a self-hosted environment, they execute on machines your organization
provisions — inside your network, next to your internal services, toolchains,
and security controls. Sessions started from web, mobile, desktop, or a routine
all route into that same environment.

## Decide first: is this required?

The announcement recommends the hosted offering for most enterprises, because
there is no infrastructure to run or maintain. Self-hosting exists for teams
whose network, tooling, or compliance requirements make local execution a hard
requirement — and it comes with a staffing commitment.

Organizations in the preview program adopted it for three reasons:

1. **Network access** — sessions can reach internal services, databases, and
   registries without exposing them to the public internet.
2. **Customizability** — compilers, SDKs, and internal CLIs are pre-installed,
   so every session starts ready to build.
3. **Compliance** — source code and build artifacts stay on infrastructure you
   control.

If none of these is a hard requirement, stay hosted.

## Know the data boundary

This is the point most likely to be misread inside an organization.

| Stays on infrastructure you provision | Sent for inference |
|---|---|
| Repository checkouts | Prompts |
| Build artifacts | Responses |
| Secrets | Tool results, which can include code the model reads |
| Any file a session creates or modifies | |

Session transcripts are stored so a session can be picked up from any surface.

Self-hosting relocates execution and artifacts. It does not keep the
conversation on your network. Present it that way to security review from the
start.

## Architecture

### Runners

You deploy **runners**: long-lived processes that pick up sessions and start an
agent process per session. Runners are the unit you build an image for, deploy,
update, and operate.

### Two capacity modes

- **Fixed** — a set number of runners stay up; sessions are distributed across
  them. Least to operate; idle capacity is a standing cost.
- **On-demand** — an orchestrator watches for queued sessions, starts runners as
  sessions arrive, and stops them when work finishes, so capacity tracks demand.
  You now operate the orchestrator too.

Choose fixed unless demand is spiky enough that idle capacity dominates.

### Isolation

A runner can serve several sessions, but **each session runs in its own
checkout**. That per-session checkout is the isolation boundary between
developers and between accounts — not the runner.

## Not the same as Remote Control

Remote Control lets a developer continue a session running on their own machine
from a phone or browser. That session ends when the machine stops running it,
and it is tied to the user who started it. Self-hosted environments run on
shared infrastructure a platform team operates, and any user can use them.

## Eligibility

- Public beta, for organizations on Team and Enterprise plans.
- Off by default.
- Not available for organizations using ZDR.

## Ownership

Plan on a platform, developer experience, or developer productivity team owning
setup and ongoing operation:

- building and maintaining the runner image,
- updating runners,
- running the orchestrator, if you use on-demand mode.

If no team will own that, the hosted offering is the right answer.

## Source

- https://claude.com/blog/run-claude-code-sessions-on-your-own-compute (August 6, 2026)
- Documentation: https://code.claude.com/docs/en/self-hosted-environments
