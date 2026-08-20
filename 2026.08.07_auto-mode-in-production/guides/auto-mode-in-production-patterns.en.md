**English** · [한국어](./auto-mode-in-production-patterns.ko.md) · [Español](./auto-mode-in-production-patterns.es.md) · [日本語](./auto-mode-in-production-patterns.ja.md)

# Running auto mode in production: patterns from Nuro, Gusto, and Garner Health

Source: https://claude.com/blog/auto-mode-in-production (August 7, 2026)

## The tradeoff auto mode addresses

Auto mode is now the default setting in Claude Code. Instead of asking you to approve every
command an agent wants to run, a classifier evaluates each action and blocks the ones that
look potentially harmful.

The design resolves a common agentic coding tradeoff:

- **Reviewing every command** keeps a human in the loop — but once sessions stretch to hours
  or multiply in parallel, that oversight becomes the bottleneck.
- **Skipping permission checks entirely** is faster — and it is also how prompt injection,
  scope drift, and the occasional deleted production resource get through.

In internal evaluations, the classifier caught more dangerous actions than developers did when
clicking through permission prompts by hand, and its performance held up under third-party
red-teaming. Because sessions pause less often, Claude works **9x longer between
interruptions** than under the previous default, across all Claude Code usage.

## Nuro — powering longer-running autonomous agents

Nuro, the physical AI company developing universal Level 4 autonomous driving technology,
adopted Claude Code in late 2025; by March it was the most popular agentic coding tool at the
company.

**The problem before auto mode.** Staff software engineer Kai Zhou had prototyped an internal
stand-in: a hook that sent each pending action to a small model, auto-approved the routine 90
percent of the time, and routed anything sensitive to Slack for a human to review. It answered
a real tension — engineers hated babysitting approval prompts, but from a company security and
legal standpoint, skipping permissions outright was too dangerous to sanction. When auto mode
shipped, Kai shelved the side project.

**How it runs today.**

- Auto mode for everything he writes: "I use auto mode for 100 percent of my coding work. Most
  of the time, I open three or four sessions running auto mode in parallel and just check in
  when I need to."
- **The exception is work that touches other teams.** When Claude Code reviews a pull request
  on his behalf, Kai switches back to interactive mode and reviews each one before it goes out.
- **It does not run unconstrained.** Nuro leans heavily on skills, and engineers deny the most
  dangerous commands — recursive deletes, for instance — outright in their settings. The
  classifier makes its judgment calls inside those guardrails.

**The bigger unlock: work that keeps running after engineers are done for the day.** Kai's
team uses auto mode to power long-running research agents that hill-climb the evaluation
metrics behind its autonomous-driving stack — tasks with a clear, measurable signal an agent
can iterate against on its own. Overnight, an agent can study false negatives flagged by the
evaluation suite, draft a proposal, run experiments, and keep iterating on the results. The
approach extends to any task with a clear evaluation method, because the metric itself tells
the agent whether it is improving or regressing; another Nuro team uses it to shrink the memory
footprint of a specific binary.

> "The other day, I kicked off an agent at 10 p.m. and it kept running until 5 a.m. — and it
> gave me three PRs in the morning. I think it's pretty impressive. Only auto mode enables this
> kind of workload."

## Gusto — shipping PRs faster and safer

At Gusto, a leading SMB technology company, the move to auto mode started as a proactive
security upgrade.

**Martin Emde, AI Dev Tools team.** He had watched permission fatigue slow the team down. Auto
mode gave them the same velocity without sacrificing control or security, and since adoption
took hold across engineering, the overall permissions burden has noticeably declined.

- 2,425 Claude Code sessions since December, with auto mode as his daily driver.
- Cross-repo work that used to stall on folder-access approvals now runs uninterrupted.
- Unattended jobs — compiling daily notes from GitHub, Slack, and Jira — run on their own.
- Roughly **10% of session transcripts since mid-May 2026 included an auto mode denial**,
  evidence the classifier is doing real work without dragging on legitimate tasks.

> "Auto mode gave us a safer balance between speed and control. We were able to remove the
> repeated prompts and increase productivity without compromising safety. We can see that auto
> mode blocks at the right time, which gives us the confidence to move quickly."

**Chad Kunsman, AIT Cloud Engineering.** He reached the same conclusion from the other
direction. His work — endpoint investigations, log audits, connector management, doc ingestion
across a stack of MCP servers — runs in short, twenty-minute bursts rather than overnight
marathons. He was not looking for longer runs; he wanted the hands-off pace of bypass
permissions without the exposure of a bad prompt, or a prompt injection, slipping through.

> "Given the protection against prompt injection, and the way it checks that what you're doing
> actually lines up with what you asked for, it's the better choice than bypass permissions and
> far faster than permission prompts."

On the rare occasions the classifier does step in, he says it is on the mark: "When it stopped
me, it made sense and explained why. It was drifting from what I'd originally asked, and it
checked in. It wasn't off base at all."

**Where he steps out.** When a session has its teeth into production infrastructure —
Terraform, AWS, direct POST calls against live APIs — he switches to accept edits and verifies
each tool call by hand. "You have to weigh the amount of time you're saving against what it
could reasonably make a mistake on, and how catastrophic that would be. Ultimately, you're
still responsible for what happens."

That judgment operates inside a broader defense-in-depth setup: Gusto routes its MCP traffic
through a governed proxy layer with tool guards and prompt inspection, so agents work with
tightly scoped permissions before auto mode ever weighs in.

## Garner Health — accelerating the software development lifecycle

Garner Health, the healthcare technology company, rolled out Claude Code in February to all
550 employees across every function. The tool is wired into core systems including Salesforce,
Zendesk, and Snowflake, and employees are encouraged to spend about two hours a week
automating the most repeatable parts of their job.

**Before auto mode,** that scale came with overhead. Platform engineering manager Evan
Magnussen describes permission management as a tedious cycle of hand-curating approved command
lists and watching piped commands get rejected.

**Today,** Evan and most of his colleagues use auto mode in every session, from researching the
codebase to managing external integrations through MCP.

> "We've built out a standardized software development lifecycle for the entire engineering
> organization that is really only possible because of auto mode. Employees view it as a weight
> off their shoulders. They don't have to monitor their agents for hours on end anymore."

**That lifecycle runs as a plugin of standardized skills.** An agent picks up a task, explores
the context it has access to, commits context files to the repository, runs what Evan calls
"antagonistic research" to pressure-test its own assumptions, and then moves on to
implementation — pausing for a human only when it needs context it cannot find on its own. The
research-heavy stages, Evan notes, were not possible before auto mode.

**Tuning.** Out of the box, the classifier has needed little tuning. Evan's one adjustment
mirrors Kai's at Nuro: he configured auto mode not to approve actions that communicate with
other people, like sending Slack messages or emails. "I personally don't like Claude to just
act on my behalf when I'm communicating with another person." Teams working on core
intellectual property — the most skeptical of skipping permissions before auto mode — learned
to tune the classifier's injected prompts to be more or less permissive for their work.

**Advice for other enterprises.** Lean in and build the right controls so you can empower
engineers while ensuring safe deployment. "If we were to say, everyone go build your own
workflows, and we have no telemetry, that would be very dangerous. Because we have the
telemetry, because we've built out workflows that are relatively standard, we have much more
confidence."

## The patterns worth copying

1. **Set hard guardrails in settings first.** The classifier makes judgment calls inside
   limits you define; it does not replace them.
2. **Constrain the tools before the classifier sees them.** A governed MCP proxy with tool
   guards and prompt inspection means agents already hold tightly scoped permissions.
3. **Make one narrow tuning adjustment by default:** do not auto-approve actions that
   communicate with other people. Two of the three teams landed on this independently.
4. **Decide in advance which sessions step out** — work that leaves your boundary, and
   production infrastructure.
5. **Match task shape to unattended running.** A clear, measurable evaluation signal is what
   lets an agent iterate overnight. The deliverable is finished PRs for review, not merged
   changes.
6. **Standardize the workflow, then instrument it.** Telemetry is the precondition that makes
   a company-wide rollout defensible, not a follow-up task.
7. **Watch the denial rate.** Around 10% of sessions including a denial reads as the classifier
   doing real work without obstructing legitimate tasks.
