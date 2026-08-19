**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A customer story about ABC Legal, a U.S. legal document delivery company with 1,100 employees, told largely through its CTO Brandon Fuller. After Claude Enterprise rolled out, teams started building automations on their own — but those early agents lived as scheduled tasks on individual desktops. Moving to Claude Managed Agents gave the company one deployment structure, shared workspaces, a single audit and billing surface, and always-on agents in the cloud.

As of July 2026 the team tracked 50+ agents in production, up to a ~50% reduction in the cost of the human tasks some agents cover before heavy optimization, and ~310 employees across every department using Claude for daily work.

The post is mostly about the operating model: define every agent as code, teach non-developers to ship through pull requests, and close a feedback loop that turns Slack reactions into merged prompt changes.

## When is it useful?
- When AI adoption is enthusiastic but scattered — automations living on individual laptops with no shared view of what exists, what it costs, or whether it ran.
- When you want non-developers to build production automations without the dev team becoming the bottleneck.
- When agents need version history, code review, rollback, and an audit trail rather than an admin screen.
- When you have human feedback on agent output and no mechanism turning it into improvement.
- When you need a defensible way to decide which tasks deserve an agent at all.

## Key points
- **Every agent is defined as code.** "An agent is really just structured text, a prompt plus configuration, and anything that is text can live in a repository where the whole company can see it, review it, and improve it." Prompt, tool list, schedule, credentials, and memory go into config files in a git repository alongside the company's software. Nothing changes except through an approved pull request.
- **A starter kit, built in a week, is what made it spread.** Two templates in dedicated git repos — one for event-driven agents, one for scheduled agents. Each agent lives in its own folder with a standard structure: a JSON config file, a system prompt in Markdown, deployment scripts, and operational documentation. Merging to main deploys automatically. A builder clones the repo, copies a template, tells Claude Code what the agent should do, and gets back config, prompt, credential store, and memory.
- **Non-developers were the proof.** A 15-person steering committee from finance, marketing, operations, and development — none of them software developers — cloned the repo and built agents with Claude Code. All 15 had working agents within a week; those builders trained their teams, and ~50+ agents were running within a month. Each agent has a name, an owner, and a single job.
- **The hard part was git, not AI.** "I had to explain what a PR was to them." Getting business users comfortable with cloning a repo and working in pull requests was the real hurdle.
- **Agents are supervised through Slack, and the reactions are training signal.** For agents whose output people grade, a three-role architecture shares one workspace, environment, and credential vault but runs on different schedules: the Initial Agent does the work in real time and records an audit trail; the Harvester runs hourly or daily and turns thread replies and emoji reactions into labeled data points; the Tuner runs weekly and proposes a change to the prompt or config — never the model's weights — as a pull request a human reviews and merges. Not every agent needs it: most of the fleet are single-task runners whose output no one grades.
- **"X-as-code" generalizes.** At sister company Docketly, ~145 delivery rulesets are single YAML files in git rather than records in an admin screen, so tuning a delivery means editing a file and opening a PR. Four agents make the loop, including a fourth that pushes merged config to the production database — executing only what a human already approved. An emoji reaction flagging a mis-routed delivery can become a merged routing change within the week.
- **Platform selection criteria were specific**: versioning, observable sessions, workspace billing, model selection, memory primitives, MCP wiring, and no infrastructure to babysit. Anthropic's managed infrastructure owns the execution loop, sessions, memory, console, and models; ABC Legal owns the prompt, tool list, trigger logic, audit trail, and feedback loop.
- **Cost is measured, not assumed.** The metric is an efficiency ratio — value delivered against cost to run — with every agent reporting its own value back to a data warehouse in hours and dollars on each run. Agents follow a J-curve: underwater while new and running larger models, then positive as the team writes evals, moves to cheaper and faster models, and trims tokens. Spend climbed through spring, then fell in July while usage kept growing.
- **Trust is earned, not granted.** Most agents start with a human in the loop, posting a recommendation into the job or a Slack channel. Those responses build a labeled dataset used for evals and cross-model benchmarking. Only once an agent proves as good as or better than humans on that task does it shift into automation mode — and it stays inside the same measurement framework afterward.

## Bundled resources
- `skills/agent-fleet-as-code/SKILL.md` — how to run a fleet of agents as code, with PRs as the control surface.
- `skills/agent-fleet-as-code/templates/agent-config.json` — the standard per-agent JSON config.
- `skills/agent-fleet-as-code/templates/system-prompt.md` — the Markdown system-prompt template.
- `skills/agent-fleet-as-code/templates/operations.md` — the operational documentation each agent folder carries.
- `skills/agent-fleet-as-code/templates/deploy.sh` — the deployment script referenced by the standard folder structure.
- `skills/agent-fleet-as-code/references/starter-kit.md` — the two starter templates and the standard agent folder layout.
- `skills/agent-fleet-as-code/references/self-improving-loop.md` — the harvester and tuner architecture in detail.
- `skills/agent-fleet-as-code/references/cost-and-trust.md` — the efficiency ratio, the J-curve, and the human-in-the-loop trust ladder.
- `skills/agent-fleet-as-code/examples/agent-fleet.md` — the agents ABC Legal actually runs.
- `agents/initial-agent.md`, `agents/feedback-harvester.md`, `agents/config-tuner.md`, `agents/config-deployer.md` — the four named roles from the post.
- `guides/fleet-of-agents.{en,ko,es,ja}.md` — the full deployment guide in four languages.

## Source
- https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
