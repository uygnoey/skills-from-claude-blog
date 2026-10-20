**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
The third post in Claude's series on human-agent teams. Asana's Chief Product Officer, Arnab Bose,
explains how Asana runs AI agents ("AI teammates") inside its Work Graph® model: agents with scoped
roles, shared memory that only designated people can commit to, and work posted where everyone can
see and coach it — plus three jobs Asana has handed to agents powered by Claude.

## When is it useful?
- When introducing agents into a team's projects, tasks, or channels.
- When writing an agent's role, instructions, permissions, and governance.
- When deciding who may train an agent versus who just works with it.
- When turning recurring synthesis work (Q&A triage, status digests, cycle planning) into agent work.

## Key points
- Structure work first: bring unstructured inputs to Claude, talk them through, and log actionable
  items as projects and tasks that agents and colleagues can pick up.
- Each agent gets a role, pre-built skills, integrations, and a profile page (purpose, users, admins,
  instructions, skills, integrations, permissions). Access is scoped to specific projects, documents,
  and apps, and bounded by the permissions of the person who triggers the agent.
- Anyone can give task-level feedback; only admins and editors can commit to, undo, or delete the
  agent's permanent shared memory. The team that owns the standard (e.g., brand voice) owns the agent.
- Agents post their plan and steps on shared tasks, so reviewers see the request and back-and-forth
  and can revise the instructions as well as the output.
- Jobs: product Q&A from Slack (answer, file product gaps, flag repeated questions to enablement);
  a daily At-Risk Renewal digest in three buckets, global then by region; engineering cycle planning
  in Command, with data exposed through Asana's MCP server.

## Bundled resources
- Skill: `design-coachable-agent-teammates` — setup procedure with an agent profile template, an
  at-risk renewal digest template, and examples of the three Asana agent jobs.
- Guide: `coachable-human-agent-teams` (en/ko/es/ja) — the four practices and three jobs in one view.

## Source
- https://claude.com/resources/articles/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
