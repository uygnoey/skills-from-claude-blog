---
name: agent-fleet-as-code
description: Run a fleet of production agents as code in a git repository — every agent a config file plus a prompt, every change a reviewed pull request, every improvement harvested from human feedback rather than retraining. Use when AI automations are scattered across individual laptops with no shared view of what exists or what it costs, when non-developers need to ship production agents without the dev team becoming the bottleneck, when agents need version history and an audit trail instead of an admin screen, or when you need a defensible way to decide which tasks deserve an agent at all.
---

# Running an agent fleet as code

The premise: *"An agent is really just structured text, a prompt plus configuration, and anything that is text can live in a repository where the whole company can see it, review it, and improve it."*

Everything below follows from that. An agent's prompt, tool list, schedule, credentials, and memory go into configuration files kept in a git repository alongside the company's software. Nothing about an agent changes except through a pull request someone approves — which gives every agent version history, code review, rollback, and an audit trail for free.

This is an operating model, not a framework. It is what turns scattered desktop automations into a fleet you can see, price, and improve.

## Instructions

### 1. Get the agents off individual machines first

The usual starting state after a successful chat rollout is genuine enthusiasm and no infrastructure: people automate their own work, and those early agents live wherever their builder happened to put them — typically as scheduled tasks on personal desktops.

That state has three specific costs: agents cannot run unattended, there is no single view of what has been built, and nobody knows what it costs or whether it ran last night. Move to a hosted runtime with one common deployment structure, shared workspaces, a single audit and billing surface, and always-on execution.

**Skip the scheduled-tasks detour if you are starting now.** Teams that built local routines first spent real time on work that a managed runtime replaced.

### 2. Build the starter kit before you invite anyone

One week of work up front is what makes the rest spread. Create two templates, each in its own git repository:

- **Event-driven agents** — start the moment something happens: a new job arrives, a document comes back from an external system.
- **Scheduled agents** — run on a timer: hourly, daily, weekly.

Each agent gets its own folder with a standard structure — see [references/starter-kit.md](references/starter-kit.md) for the full layout, and these templates to copy:

- [templates/agent-config.json](templates/agent-config.json) — the per-agent config
- [templates/system-prompt.md](templates/system-prompt.md) — the system prompt
- [templates/operations.md](templates/operations.md) — the operational documentation
- [templates/deploy.sh](templates/deploy.sh) — the deployment script

**Merging to the main branch deploys the agent.** That single property is what makes the pull request the control surface rather than a formality.

The builder's path must be: clone the repo → copy a starter template → describe what the agent should do to a coding agent → get back config, prompt, credential store, and memory. **A builder never has to write software.**

### 3. Prove non-developers can ship, then let them teach

Do not roll the kit out org-wide. Gather a cross-functional steering committee — finance, marketing, operations, and development — deliberately weighted toward people who are not software developers. Have them clone the repository and build real agents.

If every agent has to route through the dev team, that bottleneck caps how fast the whole company can move. What makes it safe is that they are not writing software: they are filling in configuration and a prompt, and the runtime supplies the rest.

Then let those builders go back to their teams and train others. That is the mechanism that takes a fleet from fifteen agents to fifty in a month.

**Expect the git hurdle, not the AI hurdle.** Getting business users comfortable with cloning a repo and working in pull requests is the real obstacle. Plan to explain what a PR is. Budget time for it and pick tooling that lowers it.

### 4. Give every agent a name, an owner, and a single job

One agent, one job. A named owner. This is what keeps a fifty-agent fleet legible and is the precondition for measuring anything per agent.

See [examples/agent-fleet.md](examples/agent-fleet.md) for what a real fleet looks like across operations, engineering, finance, and marketing.

### 5. Start every agent with a human in the loop

Most agents begin by making a recommendation for a person to review before anything is acted on. Two placements work:

- **In the flow of work** — the recommendation is stored on the job and surfaced in a banner so the person accepts or rejects it where they already are.
- **In a channel** — posted to a chat channel where people reply in the thread.

Those responses build a labeled dataset of good and bad calls. That dataset is what lets you write evals and benchmark the agent across frontier models.

Only once an agent proves it is as good as or better than humans on that specific task does it shift into automation mode and act on its own — **and it stays inside the same measurement framework afterward**, to catch performance drift.

*"Every agent earns trust before it acts alone. It doesn't start there."*

### 6. Close the feedback loop with a harvester and a tuner

Human reactions to agent output are training signal going to waste unless something collects them. For the agents that do get graded, use three roles that share one workspace, environment, and credential vault but run on different schedules:

1. **Initial Agent** — does the work, usually in real time, and records an audit trail of each action.
2. **Harvester** — runs hourly or daily, gathers thread replies and emoji reactions, turns each into a labeled data point.
3. **Tuner** — runs weekly, looks across everything at once, and proposes a change **to the prompt or config, not to the model's weights**. It drafts only; a human reviews and merges the pull request.

**Not every agent needs this.** Most of a fleet are single-task runners whose output no one grades. Adding a harvester where there is no grading signal is pure cost.

The full architecture, including the four-agent variant that pushes merged config back to a production system, is in [references/self-improving-loop.md](references/self-improving-loop.md).

### 7. Use the pull request as the control surface

*"If you want an agent involved in a decision, make the decision look like a pull request."*

Line-by-line comments, approval workflows, and immutable audit trails come free with version control, and they compose naturally with both AI and human review. This is why the tuner proposes a diff rather than writing to a database, and why any agent that changes production state should execute only what a human has already merged.

### 8. Look for more "X-as-code" candidates

The pattern generalizes past agents. Anything currently living as records behind an admin screen is a candidate to become files in a repository: routing rulesets, notification templates, event routing rules, dispatch logic, business configuration, schemas.

*"Code is just structured text. LLMs are text engines. The more of your business you can turn into text in a repo, the more leverage agents give you."*

The test is whether an agent could usefully read it, reason about it, and propose an improvement. If yes, move it into the repo.

### 9. Measure an efficiency ratio, and expect a J-curve

Have every agent report its own value back to a data warehouse on each run, in hours and dollars. The metric is the **efficiency ratio**: value delivered against cost to run.

Agents follow a J-curve — often underwater while they are new and running larger models, then flipping positive as the team writes evals, moves to cheaper and faster models, and trims tokens. Do not kill an agent at the bottom of its curve; do not assume one climbs out on its own either.

Track spend broken out by vendor, tool, team, and use case. Push spend toward vertical, operational agents where return is measurable, while keeping horizontal chat and ideation usage broad and its costs in check.

**Not every task deserves an agent.** The cost is real. The work is picking tractable problems that genuinely save time, and being willing to say a given task is not worth one. See [references/cost-and-trust.md](references/cost-and-trust.md).

### 10. Choose the runtime on specific criteria

The criteria that mattered when this fleet's platform was selected:

- versioning — every push creates a new agent version with optimistic locking, so rollback is trivial
- observable sessions
- workspace billing
- model selection — swapping models should be a one-line change
- memory primitives
- MCP wiring and credential vaults
- **no infrastructure to babysit**

Then draw the responsibility line explicitly. The managed platform owns the execution loop, sessions, memory, the console, and the models. You own the prompt, the tool list, the trigger logic, the audit trail, and the feedback loop on outcomes.

Model policy worth copying: a mid-tier model as the default for most agents, a small fast model for high-volume tasks, and a large model only where deeper reasoning justifies the cost.

## Examples

### Example 1 — a first agent built by someone who has never automated anything

An account manager pulls specific records from an internal site for one customer every week by hand.

The agent that replaced it pulls a database report for matching jobs, retrieves each PDF with a browser built into the runtime, and delivers the files to the customer's FTP server daily. The account manager had never automated anything and built it in about an hour by describing it to a coding agent inside a copied starter template.

This is the shape to aim for in the first month: a repetitive, well-bounded chore, owned by the person who does it today, built without writing software.

### Example 2 — the loop that turns an emoji into a merged config change

At the sister company, delivery routing lives as ~145 YAML rulesets in git rather than as records in an admin screen. Four agents make the loop:

1. one posts a weekly verdict to a channel,
2. the **Harvester** turns reactions into labels,
3. the **Tuner** opens a pull request on the YAML,
4. a fourth agent pushes the merged config to the production database — executing only what a human already approved.

In practice, an emoji reaction flagging a mis-routed delivery can become a merged change to that delivery's routing rules within the week. **The review is the only manual step in the loop.**

### Example 3 — deciding an agent is not worth building

A team proposes an agent for a task that runs twice a month, takes twenty minutes, and requires judgment nobody has written down.

Run it through the efficiency ratio before building: forty minutes a month of value, against the cost of a new agent, its evals, and someone owning it. Say no. The discipline of declining is what keeps the fleet's aggregate ratio positive, and it is the same discipline that lets you spend confidently on the agents that clear the bar.

## Source

- https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
