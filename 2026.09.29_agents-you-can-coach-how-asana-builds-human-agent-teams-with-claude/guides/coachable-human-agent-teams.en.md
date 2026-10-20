**English** · [한국어](./coachable-human-agent-teams.ko.md) · [Español](./coachable-human-agent-teams.es.md) · [日本語](./coachable-human-agent-teams.ja.md)

# Coachable human-agent teams: lessons from Asana

The third post in Claude's series on human-agent teams (after multiplayer AI at Anthropic and Slack as
agent context). Arnab Bose, Asana's Chief Product Officer, explains how Asana runs AI agents as
teammates inside its Work Graph® model — the web of tasks, projects, goals, and conversations with
defined owners, contributors, and dependencies.

## Design choice: agents live in the same work model
Instead of adding new context structures for AI, Asana's agents operate within the existing model.
They have defined roles, are assigned tasks, read and write messages, and appear in activity feeds
next to people — with additional safeguards around what agents can access and share. Claude is the
default AI tool for Asana employees, connected to Google Drive, Slack, and Asana.

## Four practices

| Practice | What it means | Put it into practice |
|---|---|---|
| Structure work before agents act | People turn unstructured input (ideas, Slack, meeting recordings, reports, docs) into projects and tasks with Claude; agents then act with persistent memory, their own credentials, and shared context | Start with your own ideas → debate with Claude → log actionable items to the work graph |
| Role, tools, and access per agent | Agents are built around roles (content writer, insights analyst, project manager, work intake specialist, campaign analyst, campaign coordinator) with pre-built skills and integrations; each has a profile page; effective access is bounded by the triggering person's permissions | Define the role first → scope access → name users and admins separately |
| Separate working with an agent from training it | Shared memory lets the agent reuse past instructions across users; anyone gives task feedback, but only admins/editors commit, undo, or delete permanent memory | Decide who trains vs. who uses → match editors to expertise → build memory as you work |
| Keep agent work visible | The agent posts its research plan and steps on the task; anyone with access can comment and steer | Bring agents where the team reviews work → make agent work visibly agent work → let reviewers coach |

Why visibility matters, in Arnab's words: with a one-on-one agent, the other reviewers "don't know
what the prompt was and what the back-and-forth was." On a shared task, the request, pushback, and
output are in one place, and reviewers can revise the instructions that produced the output.

## Three agent jobs at Asana
1. **Product Q&A from Slack** — questions become tasks; the agent answers from approved guidance with
   source links, files product gaps into the product intake project, and creates enablement tasks
   when questions repeat.
2. **At-Risk Renewal digest** — a daily digest of every at-risk renewal task in three buckets
   (positive momentum, negative momentum, recommended follow-ups), global then regional, pushed each
   morning to customer and revenue leaders who can ask follow-ups and coach it.
3. **Engineering cycles with Command** — agents fill an unplanned board from feedback; people decide
   what enters the cycle; Command gives optimistic/balanced/conservative completion estimates;
   tickets go to people or coding agents; data is reachable through Asana's MCP server.

## Takeaway
One shared context for humans and agents, a distinct identity for every agent so its contributions
and access can be audited, and a durable record of what agents learn so team knowledge compounds.

Reusable steps and templates: the `design-coachable-agent-teammates` skill in this folder.

Source: https://claude.com/resources/articles/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
