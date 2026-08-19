**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A product announcement: self-hosted environments for Claude Code entered public beta. Instead of running agent sessions on Anthropic-hosted infrastructure, an organization can run them on machines it provisions itself — inside its own network, next to its own internal services, toolchains, and security controls. Sessions started from web, mobile, desktop, or a routine all route into the same environment.

The post is explicit that this is not the default recommendation. For most enterprises Anthropic still recommends the hosted offering for operational simplicity; self-hosting is for teams whose network, tooling, or compliance requirements make agent execution on their own infrastructure a hard requirement, and it comes with a staffing commitment.

## When is it useful?
- When agent sessions need to reach internal services, databases, or package registries that are not exposed to the public internet.
- When every session should start with company compilers, SDKs, and internal CLIs already installed.
- When source code and build artifacts must stay on infrastructure the organization controls.
- When deciding between the hosted offering and self-hosting, and you need the trade-off — including what does *not* stay on your infrastructure — stated plainly before committing a platform team to it.

## Key points
- **Public beta, Team and Enterprise plans only.** Self-hosted environments are off by default, and are not available to organizations using ZDR.
- **What stays local, and what does not.** Repository checkouts, build artifacts, secrets, and any file a session creates or modifies stay on infrastructure you provision. The conversation itself — prompts, responses, and tool results, which can include code Claude reads — is still sent to Anthropic for inference, and the session transcript is stored so a session can be resumed from any surface.
- **Runners are the execution unit.** You deploy long-lived runner processes; each picks up sessions and starts a Claude Code process per session.
- **Two runner modes.** *Fixed*: a set number of runners stay up and sessions are distributed across them. *On-demand*: an orchestrator watches the queue, starts runners as sessions arrive, and stops them when work finishes so capacity tracks demand.
- **Isolation is per session, not per runner.** One runner can serve several sessions, but each session gets its own checkout, so work stays separated between developers and accounts.
- **One environment, every surface.** Set it up once and sessions from every supported surface route to it.
- **Not the same thing as Remote Control.** Remote Control continues a session running on a developer's own machine from a phone or browser; it ends when that machine stops and is tied to the user who ran `claude`. Self-hosted environments run on shared infrastructure a platform team operates and are usable by any user.
- **Someone has to own it.** Plan for a platform, developer experience, or developer productivity team to own setup and ongoing operation — building and maintaining the runner image, updating runners, and running the orchestrator if you choose on-demand mode.

## Bundled resources
- `skills/self-hosted-coding-environments/SKILL.md` — how to decide on, size, and operate a self-hosted environment.
- `skills/self-hosted-coding-environments/references/decision-criteria.md` — hosted vs. self-hosted, and the eligibility gates.
- `skills/self-hosted-coding-environments/references/architecture.md` — runners, the two modes, session isolation, and the data boundary.
- `skills/self-hosted-coding-environments/templates/rollout-checklist.md` — an ownership and rollout checklist derived from the post.
- `guides/self-hosted-session-environments.{en,ko,es,ja}.md` — the same material as a four-language guide.

## Source
- https://claude.com/blog/run-claude-code-sessions-on-your-own-compute (August 6, 2026)
- Implementation details: https://code.claude.com/docs/en/self-hosted-environments
