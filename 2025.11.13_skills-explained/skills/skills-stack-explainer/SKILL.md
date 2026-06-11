---
name: skills-stack-explainer
description: Decide when to use Skills vs prompts, Projects, MCP, and subagents, and combine them into a coherent workflow.
---

## Instructions

### Mental model
Use these building blocks:
- **Skills**: teach repeatable procedures or domain expertise (instructions + optional code/assets), loaded dynamically with progressive disclosure.
- **Prompts**: one-off, conversational instructions inside a chat.
- **Projects**: persistent workspace + knowledge base for an initiative.
- **Subagents**: specialized assistants with their own prompts and tool permissions.
- **MCP**: connectivity to external systems where data lives.

### How to choose
1. If you repeat the same instruction across conversations, convert it into a Skill.
2. If you need persistent background knowledge for a specific initiative, use a Project.
3. If the data lives in another system (drive, repo, CRM), use MCP to connect it.
4. If you want parallelism or strict tool isolation, use subagents.
5. Use prompts to refine the task moment-to-moment.

### Combine them
A common pattern:
1. Put reference materials into a Project.
2. Connect external sources with MCP.
3. Add a Skill that defines the analytical framework.
4. Delegate discrete work to subagents.
5. Iterate via prompts.

## Bundled resources
- Reference table: [references/comparison-table.md](./references/comparison-table.md)
- Skill template example: [templates/gdrive-navigation-skill.md](./templates/gdrive-navigation-skill.md)

## Examples
- Competitive intelligence workflow: [templates/combined-workflow.md](./templates/combined-workflow.md)
