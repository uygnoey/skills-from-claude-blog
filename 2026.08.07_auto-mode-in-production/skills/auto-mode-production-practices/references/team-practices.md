# What Nuro, Gusto, and Garner Health configured

Source: https://claude.com/blog/auto-mode-in-production

## Nuro — long-running autonomous agents

Nuro is a physical AI company developing universal Level 4 autonomous driving technology. It
adopted Claude Code in late 2025, and by March it was the most popular agentic coding tool at
the company.

**Before auto mode shipped.** Staff software engineer Kai Zhou prototyped an internal
stand-in: a hook that sent each pending action to a small model, auto-approved the routine
90 percent of the time, and routed anything sensitive to Slack for human review. The
prototype answered a real tension — engineers hated babysitting approval prompts, but from a
company security and legal standpoint, skipping permissions outright was too dangerous to
sanction. When auto mode shipped, Kai shelved the side project.

**Today.**

- Kai runs auto mode for everything he writes: "I use auto mode for 100 percent of my coding
  work. Most of the time, I open three or four sessions running auto mode in parallel and just
  check in when I need to."
- **The exception is work that touches other teams.** When Claude Code reviews a pull request
  on his behalf, Kai switches back to interactive mode and reviews each one before it goes
  out.
- **Guardrails.** Nuro leans heavily on skills, and engineers deny the most dangerous
  commands — recursive deletes, for example — outright in their settings. The classifier makes
  its judgment calls inside those guardrails.

**The bigger unlock: work that keeps running after engineers go home.** Kai's team uses auto
mode to power long-running research agents that hill-climb the evaluation metrics behind the
autonomous-driving stack. Overnight, an agent can study false negatives flagged by the
evaluation suite, draft a proposal, run experiments, and keep iterating on the results.

> "The other day, I kicked off an agent at 10 p.m. and it kept running until 5 a.m. — and it
> gave me three PRs in the morning. I think it's pretty impressive. Only auto mode enables
> this kind of workload." — Kai Zhou, Staff Software Engineer

Another Nuro team applies the same approach to shrinking the memory footprint of a specific
binary. The generalization: any task with a clear evaluation method works, because the metric
itself tells the agent whether it is improving or regressing.

## Gusto — shipping PRs faster and safer

Gusto is an SMB technology company. The move to auto mode started as a proactive security
upgrade.

**Martin Emde (AI Dev Tools team).** He had watched permission fatigue slow the team down.
Auto mode gave them the same velocity without sacrificing control or security, and as
adoption spread across engineering the overall permissions burden noticeably declined.

- 2,425 Claude Code sessions since December, with auto mode as the daily driver.
- Cross-repo work that used to stall on folder-access approvals now runs uninterrupted.
- Unattended jobs — compiling daily notes from GitHub, Slack, and Jira — run on their own.
- **Measurement:** in his team's own analysis, roughly 10% of session transcripts since
  mid-May 2026 included an auto mode denial — evidence the classifier is doing real work
  without dragging on legitimate tasks.

> "Auto mode gave us a safer balance between speed and control. We were able to remove the
> repeated prompts and increase productivity without compromising safety. We can see that auto
> mode blocks at the right time, which gives us the confidence to move quickly." — Martin Emde

**Chad Kunsman (AIT Cloud Engineering).** He arrived at the same conclusion from the opposite
direction. His work — endpoint investigations, log audits, connector management, doc ingestion
across a stack of MCP servers — runs in short, twenty-minute bursts rather than overnight
marathons. He was not looking for longer runs; he wanted the hands-off pace of bypass
permissions without the exposure of a bad prompt, or a prompt injection, slipping through.

> "Given the protection against prompt injection, and the way it checks that what you're doing
> actually lines up with what you asked for, it's the better choice than bypass permissions
> and far faster than permission prompts." — Chad Kunsman

On the rare occasions the classifier steps in, he reports it is on the mark: the block made
sense and was explained, the session had been drifting from the original request, and the
intervention was not off base.

**Where he steps out.** When a session has its teeth into production infrastructure —
Terraform, AWS, direct POST calls against live APIs — he switches to accept edits and verifies
each tool call by hand. "You have to weigh the amount of time you're saving against what it
could reasonably make a mistake on, and how catastrophic that would be. Ultimately, you're
still responsible for what happens."

**Defense in depth around it.** Gusto routes its MCP traffic through a governed proxy layer
with tool guards and prompt inspection, so agents work with tightly scoped permissions before
auto mode ever weighs in.

## Garner Health — a standardized SDLC

Garner Health is a healthcare technology company. It rolled out Claude Code in February to all
550 employees across every function. The tool is wired into core systems including Salesforce,
Zendesk, and Snowflake, and employees are encouraged to spend about two hours a week
automating the most repeatable parts of their job.

**Before auto mode,** that scale came with overhead. Platform engineering manager Evan
Magnussen describes permission management as a tedious cycle of hand-curating approved command
lists and watching piped commands get rejected.

**Today,** Evan and most of his colleagues use auto mode in every session, from researching
the codebase to managing external integrations through MCP.

> "We've built out a standardized software development lifecycle for the entire engineering
> organization that is really only possible because of auto mode. Employees view it as a weight
> off their shoulders. They don't have to monitor their agents for hours on end anymore."
> — Evan Magnussen

**The lifecycle runs as a plugin of standardized skills:**

1. An agent picks up a task.
2. It explores the context it has access to.
3. It commits context files to the repository.
4. It runs what Evan calls **"antagonistic research"** to pressure-test its own assumptions.
5. It moves on to implementation — pausing for a human only when it needs context it cannot
   find on its own.

The research-heavy stages were not possible before auto mode.

**Tuning.** Out of the box the classifier has needed little tuning. Evan's one adjustment
mirrors Kai's at Nuro: he configured auto mode not to approve actions that communicate with
other people, like sending Slack messages or emails. "I personally don't like Claude to just
act on my behalf when I'm communicating with another person." Teams working on core
intellectual property — the most skeptical of skipping permissions before auto mode — learned
to tune the classifier's injected prompts to be more or less permissive for their work.

**Advice for other enterprises.** Lean in and build the right controls so that you can empower
engineers while ensuring safe deployment. "If we were to say, everyone go build your own
workflows, and we have no telemetry, that would be very dangerous. Because we have the
telemetry, because we've built out workflows that are relatively standard, we have much more
confidence."

## Common patterns across the three

| Pattern | Nuro | Gusto | Garner Health |
| --- | --- | --- | --- |
| Hard deny rules set in settings | recursive deletes and similar | — | — |
| Governed layer in front of tools | — | MCP proxy with tool guards + prompt inspection | MCP integrations under standard workflows |
| Classifier tuning | — | — | no auto-approval of messages to people; per-team permissiveness |
| No auto-approval of communication with people | yes (same adjustment) | — | yes |
| Steps out of auto mode | PR reviews on his behalf | production infra: Terraform, AWS, live API POSTs | pauses for humans when context is missing |
| Measurement | — | ~10% of sessions include a denial | telemetry as the precondition for the rollout |
| Standardized workflows | heavy use of skills | — | plugin of standardized skills |
