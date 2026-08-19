**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A first-person account from an engineer on Anthropic's Continuous Integration team describing the on-call agent his team built. For several months, Claude Tag has acted as the first responder for CI/CD failures at Anthropic: it authored the opening situation report in every recent incident that had one, typically publishing its first analysis within about 15 minutes.

The post walks through the setup and then through each stage of the incident lifecycle — detection, triage, resolution, and verification/handoff — explaining what the agent does at each point and what stays human.

## When is it useful?
- When an on-call rotation is dominated by alert triage and after-hours interruptions rather than by durable reliability work.
- When you want a first responder that opens every incident with an evidence-grounded hypothesis instead of a blank channel.
- When incident knowledge lives in people's heads and needs to become reviewable, version-controlled instructions.
- When agentic coding has raised merge volume and the CI process needs to scale with it.

## Key points
- **The agent lives where on-call already lives.** Claude Tag holds memory across the on-call Slack channel, watches adjacent channels for context (service alerts, config changes, PR updates), and takes per-turn steering during an incident. Routines are scheduled in natural language in the same channel.
- **Access is granted once, by an administrator**, through a service account wired to the team's tools (for example Datadog or Grafana) via MCP connectors.
- **Standing instructions are markdown files kept as skills in a GitHub repository**, so several teammates can iterate on them and changes are managed like code.
- **Alerting stays deterministic; escalation has both deterministic and agentic paths.** A root instruction file carries the criteria for paging versus deferring, and Claude is used to tune noisy or overly narrow alert rules from the first days of a new service.
- **Triage runs as a dynamic workflow**: an orchestration agent spins up executor subagents that investigate each dependency and source of truth in parallel, then reports back a synthesized situation report. Median first evidence-grounded analysis was about 14 minutes after an incident opened; the fastest named a root cause in about 4.
- **Investigation is guided, not blind.** A per-bug-class investigation skill encodes the steps a human takes — one example runs to 617 lines and was built by troubleshooting turn-by-turn during a real incident.
- **A running lessons log is the memory.** Claude appends what happened, the root cause, the fix, and the gotcha after each incident, and reads it at the start of every new investigation. Recurring patterns get promoted into the investigation skill.
- **Resolution is bounded by permissions.** Progressive rollout behind feature flags is handled by a separate agent running with the engineer's permissions; the on-call agent otherwise proposes PRs, mitigation steps, or cluster actions for a human to approve.
- **Communication is a separate agent.** `ci-weather` compiles incident channels, build metrics, merge queue stats, and deploy lag into a newsroom-style report on a public channel. The team iterated the format several times — readability is team-specific taste, not plumbing.
- **Guardrails held while volume grew.** Engineers ship roughly 8x the code per quarter compared with 2021–2025, and every PR still has a named human owner, requires approval to merge, and passes the same CI gates.

## Bundled resources
- `skills/oncall-first-responder/SKILL.md` — how to stand up and operate an agentic on-call first responder.
- `skills/oncall-first-responder/templates/oncall.md` — the root standing-instruction file (routing, paging criteria, policies).
- `skills/oncall-first-responder/templates/lessons.md` — the running incident-lessons log the agent reads and appends to.
- `skills/oncall-first-responder/templates/investigation-skill.md` — skeleton for a per-bug-class investigation skill.
- `skills/oncall-first-responder/templates/sitrep.md` — situation report format.
- `skills/oncall-first-responder/references/incident-lifecycle.md` — what the agent does at each stage, and what stays human.
- `skills/oncall-first-responder/examples/scheduling-routines.md` — the natural-language routine requests and setup steps described in the post.
- `agents/incident-orchestrator.md`, `agents/incident-executor.md`, `agents/ci-weather.md` — the three named agent roles from the post.
- `guides/agentic-ci-on-call.{en,ko,es,ja}.md` — the full methodology guide in four languages.

## Source
- https://claude.com/blog/ai-ci-cd-on-call
