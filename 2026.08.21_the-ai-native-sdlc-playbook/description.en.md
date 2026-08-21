**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Anthropic's Applied AI team lays out how to redesign a software development lifecycle around agentic coding. The premise: code is no longer the bottleneck. When the build phase collapses to hours, the constraint moves to the human-speed steps around it — plan, review and test, deploy — the controls stop matching reality, and governance costs rise because exceptions still route through committees that meet weekly or monthly.

The answer is not to remove the controls but to change how they are enforced. The linear flow becomes a loop with AI embedded at each point, and every stage ends by committing a version-controlled artifact the next stage reads: `intent.md`, `spec.md`, `plan.md`, the diff and its tests, the PR with its review findings, the incident record. The chain of commits is the audit trail. The post walks the six stages — Plan, Design, Build, Test, Deploy, Maintain — as modular plays, each with prerequisites, execution steps, governance considerations, and a leading and lagging indicator.

## When is it useful?
- When agentic coding has made the build phase fast but planning, review, testing, and deployment still run at human speed.
- When the review queue or security sign-off has become the bottleneck, and a regulated organization can accept neither a growing backlog nor under-reviewed code shipping.
- When deciding which SDLC stage to transform first — the post separates stage order from adoption order and names each play's prerequisites.
- When encoding policy as skills, hooks, and managed settings instead of enforcing it in review meetings.
- When an existing system of record (Jira, ServiceNow, a requirements tool) has to coexist with markdown artifacts.
- When closing the loop so a production signal writes the next `intent.md` with no person in the invocation path.

## Key points
- **The committed artifact is the thread.** Each stage ends by writing one to version control and the next begins by reading it. An accepted `intent.md` triggers the design pass, an approved `spec.md` triggers plan mode, a merged PR triggers the pipeline, and a breached control band writes the next `intent.md`.
- **Intent is captured once, in the originator's own words.** The person with the problem brainstorms with Claude and commits `intent.md` — no formal language, no product manager needed to write it up. Contributors without git experience commit through a version-control connector.
- **Requirements and design collapse into one session,** constrained by the organization's skills, with areas of concern flagged. Policy is applied while the spec is written rather than discovered in a review weeks later.
- **Nothing is implemented without an accepted plan.** Plan mode enforces this itself — Claude cannot edit files until the engineer accepts the plan, so changing course is still a matter of editing a document.
- **Skills are advisory; hooks are deterministic.** "The skill makes violations rare and the hook makes them close to impossible." A policy that must always hold needs something deterministic behind the skill.
- **Give Claude a feedback loop, and protect the loop.** For a bug fix, write and commit the failing test first, then ask for the fix without editing the test — a hook blocks test-file edits during a fix task, because an agent fixing code must not be able to weaken the check on that code.
- **Evals are the AI-native stage gate.** 20–50 real tasks with their checks, run non-interactively in CI on a schedule and on any change to `CLAUDE.md`, skills, or hooks — that configuration steers the agent and deserves the regression testing code gets. Every production incident becomes a permanent eval.
- **Review runs both directions.** Claude reviews all PRs against `REVIEW.md` and addresses `@claude` comments on its own. Findings never approve or block on their own; branch protection still requires a code owner, so the agent that wrote the code cannot approve it.
- **The agent acts up to the production gate and not past it.** Autonomy is tiered by environment, deployment is exposed through MCP as a per-environment allowlist, and rollback should be the most rehearsed path in the pipeline.
- **Detection stays deterministic.** A version-controlled script watches one metric with a rolling baseline; 1σ logs, 2σ invokes Claude read-only, 3σ lets it open a PR or trigger a pre-approved runbook. No model is involved in detection.
- **Every play carries two numbers** — a leading indicator that says the change is taking hold and a lagging one that says the outcome improved, both read from git, PR metadata, CI, the incident tracker, or the OpenTelemetry export.

## Bundled resources
- `skills/ai-native-sdlc/SKILL.md` — the six stages as an executable procedure, with the artifact chain and adoption order.
- `skills/ai-native-sdlc/references/stage-plays.md` — every play in full: what changes, prerequisites, infrastructure, execution, governance.
- `skills/ai-native-sdlc/references/governance-and-controls.md` — the four control layers and the managed-settings example explained line by line.
- `skills/ai-native-sdlc/references/measurement.md` — the leading/lagging indicator table and where each number is read from.
- `skills/ai-native-sdlc/references/legacy-integration.md` — naming one source of truth per artifact when Jira or a requirements tool already holds the record.
- `skills/ai-native-sdlc/templates/` — `intent.md`, `plan.md`, `claude-md.md`, `review-md.md`, `design-pass-prompt.md`, `verification-block.md` as fillable scaffolds.
- `skills/ai-native-sdlc/examples/` — the `secure-api-review` policy skill, the CI eval workflow, and the production gate.
- `skills/ai-native-sdlc/data/bands.yaml` — the 1σ/2σ/3σ response tiers.
- `agents/verifier.md`, `code-simplifier.md`, `codebase-researcher.md` — the three subagent roles the post names.
- `hooks/production-gate.json` + `.sh` + `.md` — the release gate, reproduced from the post.
- `hooks/test-file-guard.json` + `.sh` + `.md` — a reference implementation of the test-file block the post specifies.
- `guides/ai-native-sdlc-playbook.{en,ko,es,ja}.md` — the full playbook as a narrative walkthrough.

## Source
[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) by Louis Claxton — published 2026-08-21.
