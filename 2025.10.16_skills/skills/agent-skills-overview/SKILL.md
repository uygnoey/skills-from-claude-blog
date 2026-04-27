---
name: agent-skills-overview
description: Overview and adoption checklist for Agent Skills (reusable bundles of instructions, scripts, and resources that Claude loads when relevant).
---

## Instructions
Use this skill when the user wants to understand, adopt, or operationalize **Agent Skills** across Claude apps, Claude Code, and the Claude Developer Platform.

Follow these steps:
1. Clarify where the user will run skills: Claude apps, Claude Code, API, or all of the above.
2. Identify the user’s target workflows (e.g., document creation, spreadsheet processing, finance reconciliation, brand/voice enforcement).
3. Propose a minimal skill bundle structure:
   - `SKILL.md` (this file) for the short, always-needed instructions.
   - Move long checklists, templates, and reference links into companion files.
4. Provide an adoption checklist (see `templates/adoption-checklist.md`).
5. Point to platform documentation for authoritative specifications (see `references/official-docs.md`).

Constraints:
- Do not invent product features beyond the linked documentation.
- Prefer actionable next steps and a small starting scope.

## Examples
### Example: turning a repeatable workflow into a skill
User: “We repeatedly create board-ready KPI spreadsheets and slides. Can Claude do this reliably?”

Assistant:
1. Recommend bundling the organization’s KPI definitions, formatting rules, and review checklist into a skill.
2. Suggest adding templates for the spreadsheet layout and slide outline.
3. If deterministic steps are required, recommend a script (e.g., validation of required tabs/fields) as an executable companion.
4. Provide the adoption checklist and next steps to install the skill in the target environment.

### Example: safer use of executable code
User: “Can I add scripts to a skill?”

Assistant:
Explain that skills can include executable code, but recommend:
- limiting scripts to well-defined utilities,
- documenting inputs/outputs,
- and using trusted sources when enabling code execution.
