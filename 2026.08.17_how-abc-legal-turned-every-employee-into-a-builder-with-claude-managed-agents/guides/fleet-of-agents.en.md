**English** · [한국어](./fleet-of-agents.ko.md) · [Español](./fleet-of-agents.es.md) · [日本語](./fleet-of-agents.ja.md)

# Deploying a governed fleet of agents

How ABC Legal went from scattered desktop automations to 50+ production agents, built largely by people who are not software developers.

## The starting problem

ABC Legal is a U.S. legal document delivery company with 1,100 employees. When CTO Brandon Fuller rolled out Claude Enterprise, adoption happened on its own: teams across service of process, eFiling, appearance counsel operations, marketing, compliance, and finance started building automations without being asked.

> "Our users really flocked to it. They saw the ease of use of connectors and tools, and suddenly we had people all over the organization automating the tasks that had always eaten up their day."

That is the adoption any CTO hopes for, and it is also where the problem starts. **Early agents lived wherever their builder happened to put them — as scheduled tasks on individual desktops.** Which meant they could not run unattended, there was no single view of what had been built, and nobody knew what it cost or whether it ran last night.

Moving to Claude Managed Agents gave the company one common deployment structure, shared workspaces, a single audit and billing surface, and always-on agents in the cloud instead of on a person's laptop.

As of July 2026:

- **50+ agents** built with Managed Agents in production
- **up to ~50% reduction** in the cost of the human tasks some agents cover, before heavy optimization
- **~310 employees** across every department using Claude for daily work

## Principle 1 — Treat every agent like software

> "An agent is really just structured text, a prompt plus configuration, and anything that is text can live in a repository where the whole company can see it, review it, and improve it."

An agent's prompt, tool list, schedule, credentials, and memory all go into configuration files kept in a git repository alongside the company's software. **Nothing about an agent changes except through a pull request someone approves** — which gives every agent version history, code review, rollback, and an audit trail.

## Principle 2 — Build the starter kit first

Fuller spent a week building a starter kit: two templates, stored in dedicated git repositories.

- **Event-driven agents** — start the moment something happens, like a new job arriving or a document coming back from a court.
- **Scheduled agents** — run on a timer: hourly, daily, or weekly.

Each agent lives in its own folder with a standard structure: **a JSON config file, a system prompt in Markdown, deployment scripts, and operational documentation.** Merging a change into the main branch deploys the agent automatically.

The builder's path is deliberately short: clone the repo, copy a starter template, tell Claude Code what the agent should do, and get back everything the agent needs — config, prompt, credential store, and memory. **A builder never has to write software.**

## Principle 3 — Prove non-developers can ship

Fuller gathered the company's 15-person steering committee — finance, marketing, operations, and development, **none of them software developers** — and had them clone the repository and build agents using Claude Code.

The goal was to prove non-developers could build production agents themselves. If every agent had to route through the dev team, that bottleneck would cap how fast the whole company could move. What made it safe is that they were not writing software: they were filling in configuration and a prompt, and Managed Agents supplied the runtime.

> "I had to explain what a PR was to them. A lot of [the non-software engineers] thought it meant running, like a PR, the fastest you can. Now they're doing pull requests and sending them to each other."

Within a week, all 15 had working agents. Those builders went back to their teams and trained others. **Within a month, roughly 50+ agents were running.** Each has a name, an owner, and a single job.

## What the fleet does

ABC Legal now has an agent at most stages of the legal filing process and the operations around it:

- **AI Code Reviewer** — reviews every pull request across four codebases with multi-model analysis, catching security bugs, performance regressions, and committed credentials. Engineers wait for its review before merging.
- **EvidenceChain™ Delivery Agent** — took over a weekly manual chore: pulls a database report for matching jobs, retrieves each PDF with a browser built into the agent, and delivers it to a customer's FTP server daily. The account manager who set it up had never automated anything, and built it in about an hour by describing it to Claude Code.
- **eFiling Rejection Diagnoser** — fires when a court rejects a filing, reads the job details, checks the court's rules, and posts a diagnosis to Slack in about a minute. That used to consume hours of an employee's day.
- **Job-verification agent** — navigates a court website in a browser, confirms the hearing or case is filed appropriately and occurring on the stated date, then adjusts the job, flagging jurisdictions, courts, and statute-of-limitations timeframes.
- **Attorney Coverage Agent** — works the attorney network to get hearings covered: checking availability, emailing, and reading replies about availability and pricing.
- **AR-remittance agent** — parses a remittance email, builds the NetSuite payment-application file, posts it to Slack for one-click approval, then imports it. A daily agent renders a capitalize-or-expense verdict on each engineering ticket.
- **Google Ads analyst** — posts a weekly recommendation for the channel lead.
- **Charvis** — reviews completed service jobs and agrees with the compliance team about **98% of the time**.
- **Service-Overdue-Nudger** — works the tier-1 layer of operational backlogs and drafts tiered daily outreach for human approval.

## Principle 4 — Harvest, tune, repeat

Agents work under human supervision, posting what they did or recommend to Slack, where people reply in threads and react with emoji. **Hank**, an internal code review agent, posts every review to a shared channel, naming the pull request and the counts that came out of it, so the trail of what the agent decided is public and searchable.

All that reaction data is a training signal going to waste unless something collects it. **Not every agent needs it** — most of the fleet are single-task runners whose output no one grades, and they work alone.

For the agents that do collect graded feedback, ABC Legal uses a **three-role architecture**: separate agents sharing one workspace, environment, and credential vault, running on different schedules.

| Role | Cadence | What it does |
|---|---|---|
| **Initial Agent** | Real time | Does the work as a job comes in or a document comes back, and records an audit trail of each action |
| **Harvester** | Hourly or daily | Gathers human feedback from Slack — thread replies and emoji reactions — turning each into a labeled data point |
| **Tuner** | Weekly | Looks across everything at once and proposes a change to the prompt or config **rather than the model's weights**. It drafts only; a human reviews and merges the pull request |

The pattern turns messages in Slack into versioned, human-approved changes to the agent. Agents improve through the same workflows developers already use.

### "Deliveries-as-code": the four-agent variant

The same loop tunes business configuration, not just prompts. At Docketly, ABC Legal's 50-person sister company, work is organized around deliveries, each with its own ruleset for routing and handling. **All ~145 rulesets are single YAML files in git rather than records in an admin screen**, so tuning a delivery means editing a file and opening a pull request.

Four agents make up the loop: one posts a weekly verdict to Slack, the Harvester turns reactions into labels, the Tuner opens a pull request on the YAML, and a fourth agent pushes the merged config to the production database — executing only what a human has already reviewed and approved.

In practice, an emoji reaction flagging a mis-routed delivery can become a merged change to that delivery's routing rules within the week. **The review is the only manual step in the loop.**

## Choosing the runtime

Fuller evaluated multiple frameworks before settling on Claude Managed Agents. His criteria were specific: versioning, observable sessions, workspace billing, model selection, memory primitives, MCP wiring, and — most critically — **no infrastructure to babysit.**

The division of responsibility maps cleanly:

| Owned by the managed platform | Owned by ABC Legal |
|---|---|
| The execution loop | The prompt |
| Sessions | The tool list |
| Memory | The trigger logic |
| The console | The audit trail |
| The models | The feedback loop on outcomes |

Capabilities that proved especially important at scale:

- **Versioning** — every push creates a new agent version with optimistic locking. Rollback is trivial.
- **Model flexibility** — Claude Sonnet as the default for most agents, Claude Haiku for high-volume and fast tasks, Claude Opus when deeper reasoning justifies the cost. Swapping models is a one-line change.
- **MCP wiring and credential vaults** — agents connect to ABC Legal's own platform (over 100 tools available), Metabase for reporting, Slack for human-in-the-loop interaction, and Atlassian for project management.
- **Scheduled deployments** — recurring agents run on cron schedules through Bitbucket Pipelines, which already handles repo access, secrets, and billing.

## Cost, measured

ABC Legal tracks every dollar of AI spend, broken out by vendor, tool, team, and use case. Spend climbed as the fleet went live through the spring, then **started falling in July while usage kept growing** — the result of the efficiency work below.

The approach to cost is deliberate: push spend toward vertical, operational tools and agents where return is measurable, while keeping horizontal chat and ideation usage broad and its costs in check.

**The metric is an efficiency ratio: the value an agent delivers, measured against what it costs to run.** Every agent reports its own value back to a data warehouse on each run, in hours and dollars. Agents follow a **J-curve** — often starting underwater while they are new and running larger models, then flipping positive as the team writes evals, moves to cheaper and faster models, and trims tokens.

## Trust, earned

Most agents start with a human in the loop: the agent looks at the job or ticket and makes a recommendation for a person to review before anything is acted on. The recommendation is either stored in the job and surfaced in a banner so the person can accept or reject it in the flow of their work, or posted to a Slack channel where people reply in the thread.

Those responses build a labeled dataset of good and bad calls, which feeds the harvester and tuner loop and lets the team write evals and benchmark agents across frontier models. **Once an agent proves it is as good as or better than the humans on that specific task, it shifts into automation mode and acts on its own** — and it stays inside the same measurement framework afterward, to watch for changes in performance.

## Fuller's working principles

- **Think of everything as code.** *"Code is just structured text. LLMs are text engines. The more of your business you can turn into text in a repo, the more leverage agents give you."* This applies to traditional software and equally to prompts, schemas, dispatch rules, notification templates, and business configurations.
- **Start with humans in the loop.** Every agent begins by posting recommendations for human review. Only after demonstrating consistent agreement with human decisions does it earn the right to act independently. *"Every agent earns trust before it acts alone. It doesn't start there."*
- **Use the PR as your control surface.** *"If you want an agent involved in a decision, make the decision look like a pull request."* Line-by-line comments, approval workflows, and immutable audit trails come free with version control, and compose naturally with both AI and human review.
- **Invest in the feedback loop.** The harvester-tuner pattern means agents improve without retraining. Slack replies and emoji reactions become structured signals that feed back into prompt and config changes, all through the same pull request workflow humans already use.
- **Skip the scheduled-tasks detour.** ABC Legal spent real time building scheduled tasks and local routines before moving to Managed Agents, largely because the product had only just launched in beta. Fuller's advice today is to go straight to Managed Agents.
- **Expect the git hurdle, not the AI hurdle.** The hard part was getting business users comfortable with cloning a repo and working in Git and pull requests, more than anything about the AI itself. It worked, and fast, but it was a real hurdle — one Fuller would like to see made easier in the tooling itself.
- **Not every task deserves an agent.** The cost is real, so every team has to think in terms of value over cost. The work is picking tractable problems that genuinely save time or create automation, and being willing to say a given task is not worth an agent.

## What's next

The fleet continues to grow. In-flight projects include a service photo reviewer, a PagerDuty triage agent, a daily KPI digest, and expanded Tuner loops on existing agents. The team is also identifying more "X-as-code" candidates: notification templates, event routing rules, and dispatch logic that can move into repositories where agents can read, reason about, and propose improvements.

> "We want AI to support a business that can run itself, with employees free to steer it." — Brandon Fuller, CTO, ABC Legal

## Source

- https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
