**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A general-availability announcement: computer use, the Skills API, and the Files API are now generally available on the Claude Platform, and computer use adds a new browser use tool for agents that work in web applications. The framing is that together these let you build agents that operate software, apply your team's expertise, and return finished files — with code execution and web search, already generally available, fitting into the same loop.

The post explains what each piece is for. Computer use operates software the agent can see, given a screenshot, which is what lets it work in applications never built for automation. The browser use tool adds page structure so the agent acts on a specific field or button rather than a screen position. A skill is a folder of instructions, scripts, and templates loaded only when a task calls for it, uploaded and versioned through the Skills API and run in Claude's code execution sandbox. The Files API stores the documents an agent reads and writes, referenced by ID across requests.

## When is it useful?
- When an agent has to work inside an application or portal that exposes no API.
- When deciding between pixel-level computer use and the structure-aware browser use tool for a web task.
- When team procedure keeps growing inside a prompt string and needs to become a versioned artifact instead.
- When a multi-turn workflow is re-sending the same source document on every request.
- When the deliverable is a file, not a paragraph of response text.
- When you are migrating an existing beta integration and want to know what changed at GA.

## Key points
- **Multi-action turns.** The updated computer use tool takes several actions per turn instead of one per model call, so tasks finish in fewer calls and less time. The browser use tool uses the same multi-action turns and adds page structure.
- **Computer use is now eligible for HIPAA-regulated workloads** under Anthropic's BAA.
- **Skills API:** a simpler API for uploading and versioning your own skills; they run in Claude's code execution sandbox, so there is nothing to host.
- **Files API:** automatic file expiration, 5x higher rate limits, and 1 TB of storage per organization.
- **The composed loop.** The worked example is a claims agent: read the intake document from the Files API, follow a skill encoding the team's filing procedure, complete the submission in an insurer's web portal with the browser use tool, save the confirmation back as a file.
- **Reported result on the new computer use tool.** For agents working inside healthcare and insurance systems with no API: the longest claims workflow went from 32 minutes to 13, cost per task fell about 30% across every workflow tested, and completion hit 100% — with no prompt changes.
- **A skill as the customization surface.** Box built specialized document creation into Box Agent: a skill captures a bank's credit methodology and approved memo format, and Box Agent applies it to documents already in Box to produce a source-grounded credit memo for analyst review, so banks get agents for complex workflows without building each one from scratch.
- **Availability.** The Skills API and Files API are also on Microsoft Foundry; updated computer use and browser use are coming soon to Google Cloud's Vertex AI. Existing beta integrations keep working while you migrate.

## Bundled resources
- `skills/software-operating-agent-stack/SKILL.md` — composing the four capabilities into one agent, with the selection rules.
- `skills/software-operating-agent-stack/references/capabilities.md` — each capability as announced, including what changed at GA.
- `skills/software-operating-agent-stack/references/availability.md` — cloud availability and a migration order from beta.
- `skills/software-operating-agent-stack/examples/workflow-shapes.md` — the claims agent and the Box composition, mapped stage by stage.
- `guides/agent-capability-selection.{en,ko,es,ja}.md` — choosing between the capabilities for a production agent.

## Source
[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api) — published 2026-08-20.
