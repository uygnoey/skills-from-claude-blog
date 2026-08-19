# The starter kit

One week of up-front work is what let a fleet grow from fifteen agents to fifty in a month. The kit is two templates stored in dedicated git repositories, plus one standard folder structure.

## Two templates

| Template | Starts when | Typical shape |
|---|---|---|
| **Event-driven** | Something happens — a new job arrives, a document comes back from an external system, a pull request opens | Runs in real time, reacts to one event class, posts a recommendation or takes a bounded action |
| **Scheduled** | A timer fires — hourly, daily, or weekly | Sweeps a queue, compiles a report, proposes a change |

Recurring agents can run their deployments through the CI system that already handles repo access, secrets, and billing, rather than a separate scheduler.

## The standard agent folder

Each agent lives in its own folder with the same structure, whichever template it started from:

```
agents/
  <agent-name>/
    agent-config.json     # config: trigger, model, tools, credentials, memory, workspace
    system-prompt.md      # the prompt, in Markdown
    deploy.sh             # deployment script run by the pipeline on merge
    operations.md         # operational documentation: owner, dependencies, runbook
```

Copy the templates in this skill's `templates/` folder to start one:

- `templates/agent-config.json`
- `templates/system-prompt.md`
- `templates/deploy.sh`
- `templates/operations.md`

## The property that makes it work

**Merging a change into the main branch deploys the agent automatically.**

That is what turns the pull request from a formality into the control surface. Line-by-line comments, approval workflows, and immutable audit trails come free with version control, and they compose naturally with both AI and human review.

## The builder's path

A builder never has to write software:

1. Clone the repository.
2. Copy a starter template into a new folder.
3. Tell a coding agent what the agent should do.
4. Get back everything the agent needs: config, prompt, credential store, and memory.
5. Open a pull request. Someone approves it. It deploys.

## What goes in the repo, and why

An agent's prompt, tool list, schedule, credentials reference, and memory settings are all text. Putting them in a repository alongside the company's software gives every agent:

- **version history** — what changed, when, and by whom
- **code review** — a second pair of eyes before anything reaches production
- **rollback** — every push creates a new version with optimistic locking
- **an audit trail** — immutable, and the same one auditors already accept for software

Nothing about an agent changes except through a pull request someone approved.

## The hurdle to plan for

The hard part is not the AI. It is getting business users comfortable with cloning a repo and working in git and pull requests. Expect to explain what a pull request is — literally. It works, and fast, but it is a real hurdle, and it is worth choosing tooling that lowers it.

## Source

- https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
