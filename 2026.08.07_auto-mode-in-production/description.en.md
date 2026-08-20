**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Three customer stories about running Claude Code's **auto mode** as the daily default in production: **Nuro**, **Gusto**, and **Garner Health**. Auto mode replaces per-command approval prompts with a classifier that evaluates each action and blocks the potentially harmful ones. The post frames it as a resolution of the speed-versus-safety tradeoff in agentic coding: reviewing every command keeps a human in the loop but becomes the bottleneck once sessions run for hours or in parallel, while skipping permission checks entirely is how prompt injection, scope drift, and deleted production resources get through.

Across all Claude Code usage, Claude works **9x longer between interruptions** than under the previous default.

## When is it useful?
- When deciding whether to make auto mode a team or company default and needing concrete operating patterns rather than a feature description.
- When designing the guardrails that surround auto mode — deny rules, classifier tuning, MCP proxying, telemetry.
- When you want to know where practitioners deliberately step *out* of auto mode.
- When building long-running or overnight agents and looking for the task shapes that actually work unattended.

## Key points
- **Auto mode runs inside guardrails, not instead of them.** Nuro's engineers deny the most dangerous commands, like recursive deletes, outright in their settings, and the classifier makes its judgment calls within those limits. Gusto routes MCP traffic through a governed proxy layer with tool guards and prompt inspection, so agents already work with tightly scoped permissions before auto mode weighs in.
- **The unlock is unattended duration, not per-step speed.** Nuro runs overnight research agents that hill-climb the evaluation metrics behind its autonomous-driving stack — one engineer kicked off an agent at 10 p.m. and had three PRs by morning. The pattern generalizes to any task with a clear evaluation signal the agent can iterate against; another Nuro team used it to shrink a binary's memory footprint.
- **Short sessions benefit too.** A Gusto cloud engineer runs twenty-minute bursts — endpoint investigations, log audits, connector management, doc ingestion across MCP servers — and chose auto mode over bypass permissions for the prompt-injection protection and the intent check, not for longer runs.
- **The classifier is doing real work.** In Gusto's own analysis, roughly 10% of session transcripts since mid-May 2026 included an auto mode denial. One engineer has run 2,425 sessions since December with auto mode as the daily driver.
- **Practitioners still step out deliberately.** Kai at Nuro switches back to interactive mode when Claude Code reviews a pull request on his behalf. Chad at Gusto switches to accept edits for Terraform, AWS, and direct POST calls against live APIs — "you're still responsible for what happens."
- **Tuning is minimal but pointed.** Garner Health's one adjustment mirrors Nuro's: configure auto mode not to approve actions that communicate with other people, such as sending Slack messages or emails.
- **Auto mode can be the precondition for a standardized SDLC.** Garner Health rolled Claude Code out to all 550 employees, wired into Salesforce, Zendesk, and Snowflake, and runs its lifecycle as a plugin of standardized skills: explore context, commit context files to the repository, run "antagonistic research" to pressure-test assumptions, then implement — pausing for a human only when it needs context it cannot find. The research-heavy stages were not possible before auto mode.
- **Telemetry is the enabling control.** Garner's advice for enterprises: build the workflows and telemetry first. "If we were to say, everyone go build your own workflows, and we have no telemetry, that would be very dangerous."

## Bundled resources
- `skills/auto-mode-production-practices/SKILL.md` — operating patterns for running auto mode as a daily default.
- `skills/auto-mode-production-practices/references/team-practices.md` — what Nuro, Gusto, and Garner Health each configured and why.
- `skills/auto-mode-production-practices/references/unattended-task-patterns.md` — which task shapes work overnight, and which do not.
- `skills/auto-mode-production-practices/templates/team-auto-mode-policy.md` — a fill-in team policy covering guardrails, exceptions, and telemetry.
- `guides/auto-mode-in-production-patterns.{en,ko,es,ja}.md` — the three case studies and their common patterns, in four languages.

## Source
- https://claude.com/blog/auto-mode-in-production
