---
name: design-coachable-agent-teammates
description: Set up AI agents as teammates on a shared work platform the way Asana does — structure unstructured work with Claude before agents act, give each agent a defined role, profile, scoped access bounded by the triggering user's permissions, and separate admins/editors who can commit to its shared memory from users whose feedback only applies to the current task, and keep agent work visible on shared tasks so reviewers can coach it. Use when designing human-agent teams, writing an agent's role profile, deciding who trains an agent, or turning a recurring team job into an agent workflow.
---

## Purpose
Asana runs AI agents ("AI teammates") inside the same work model its people use: agents have roles,
get assigned tasks, read and write messages, and show up in activity feeds — with extra safeguards on
what they can access and share. This skill turns the four practices from the post into a repeatable
setup procedure, plus the three agent jobs Asana describes as patterns.

## When to use
- Introducing agents into a team's projects, tasks, or channels.
- Writing the role, instructions, and permissions for a new agent.
- Deciding who may change an agent's behavior or memory.
- Converting a recurring, synthesis-heavy job (Q&A triage, status digests, planning) into agent work.

## Instructions

### 1. Structure the work before agents act on it
1. Bring the unstructured pieces — an idea, a Slack thread, meeting notes, reports, docs — to Claude.
2. Talk it through with Claude as a thinking partner until the next steps are clear.
3. Log the actionable items as projects and tasks on the shared platform, where agents and colleagues
   can pick them up.

### 2. Give every agent a role, tools, and scoped access
1. Define the role before creating the agent: purpose, instructions, and which jobs it owns — as you
   would for a new hire's first quarter. Build agents around roles or types of work (the post lists
   content writer, insights analyst, project manager, work intake specialist, campaign analyst,
   campaign coordinator).
2. Attach the skills and integrations the role needs.
3. Scope access: which projects and documents it can read, which apps it can use, which actions it
   can take — specific sets rather than everything.
4. Bound effective access by the permissions of the person who triggers the agent, so private context
   does not leak to people who lack access.
5. Name users and admins separately: many people can use the agent; a small named group governs it.
6. Record all of this in a profile using [templates/agent-profile.md](./templates/agent-profile.md).

### 3. Separate working with an agent from training it
1. Anyone can give feedback on a task; that feedback applies only to the current task.
2. Only admins/editors can commit feedback to permanent shared memory, or undo/delete from it.
3. Match editors to expertise: the team that owns the standard the agent applies (e.g., brand voice,
   planning conventions) owns or administers the agent.
4. Most people never need to understand skills, behavior, or memory; one or two experts set it up.
5. Build memory as you work: ask the agent to remember decisions worth keeping and delete ones that
   are no longer relevant or true.

### 4. Keep agent work where everyone can see it
1. Assign agents on shared tasks or channels where the team already reviews work.
2. Make agent work visibly agent work.
3. Have the agent post its plan and steps (e.g., research plan) on the task so reviewers can comment,
   revise the instructions, or steer the output in the same place.

## Examples
Three jobs Asana handed to agents — summarized in
[examples/asana-agent-jobs.md](./examples/asana-agent-jobs.md):
- **Product questions from a Slack channel** — each question becomes a task; the agent answers with
  source links, files product gaps to the product team's intake, and flags repeated questions to
  enablement.
- **At-risk renewal digest** — a daily digest in three buckets, global then by region, pushed to
  leaders who can ask follow-ups and coach the agent. Output skeleton:
  [templates/at-risk-renewal-digest.md](./templates/at-risk-renewal-digest.md).
- **Engineering cycle planning with Command** — agents fill an unplanned board from feedback; people
  decide what enters the cycle; tickets go to a person or a coding agent.

## Notes
- The safeguards described (access bounded by the triggering user, admin/editor-only memory commits)
  are Asana's product behavior as stated in the post; replicate them with your platform's equivalents.
- Source: https://claude.com/resources/articles/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
