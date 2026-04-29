---
name: managed-agents-pm-workflows
description: Turn product-management jobs-to-be-done into repeatable Claude Managed Agents workflows, moving from discovery to prototype to ongoing automation.
---

## What this skill is

This skill packages a lightweight workflow for product managers who want to:

1. Do open-ended discovery with Claude / Claude Cowork.
2. Convert a clarified “job to be done” into a concrete Managed Agents prototype using Claude Code.
3. Re-run that agent as an operational workflow (async, long-running) as needs repeat.

The guidance and examples are based on the Claude blog post “Product development in the agentic era.”

## When to use

Use this when you want to:

- Pressure-test API or product abstractions by building against them early.
- Replace recurring PM busywork (monitoring, analysis, prep) with a reusable agent run.
- Treat agent prototypes as real internal tools, not one-off demos.

## Instructions

### 1) Choose the right mode for the stage

- **Discovery (murky, early-stage exploration):** use Claude / Claude Cowork for an ongoing conversation.
- **Build (job-to-be-done is clear):** use Claude Code to implement a custom agent on top of Managed Agents.

### 2) “Build with what you ship”

When designing an API or a workflow, don’t rely only on docs and comment threads.
Prototype early against the real primitives you plan to ship so you can discover where an elegant spec fails in practice.

### 3) Start from a job to be done

Write 2–5 sentences that define:

- The user and scenario
- The output artifact you need
- The inputs/sources you can provide
- How you’ll judge success

Save it and reuse it as the seed prompt for future runs.

### 4) Use long-running runs intentionally

Managed Agents sessions can run in the cloud.
Design your workflow so you can:

- Kick off work and come back later.
- Iterate across runs by preserving what the agent learned last time.

## Bundled resources

- Prompt templates: [templates/pm-job-to-be-done.md](./templates/pm-job-to-be-done.md), [templates/managed-agents-onboarding-prompt.md](./templates/managed-agents-onboarding-prompt.md)
- Use-case examples: [examples/pm-use-cases.md](./examples/pm-use-cases.md)
- Notes about the `claude-api skill` mention in the post: [references/claude-api-skill-note.md](./references/claude-api-skill-note.md)

## Examples

See: [examples/pm-use-cases.md](./examples/pm-use-cases.md)
