---
name: cowork-enterprise-rollout-playbook
description: Plan and run a Claude Cowork enterprise rollout the way Anthropic's own April 29, 2026 deployment guide recommends — pick a first business function, structure a pilot, walk the five-level maturity model, and execute a six-month champion-to-org-wide roadmap, anchored on the post's named internal teams and customer references (Thomson Reuters, Zapier, Jamf).
---

# Cowork enterprise rollout playbook

The April 29, 2026 launch announces a new Anthropic guide for deploying Claude Cowork across an enterprise. This skill turns the structure of that guide — as the post describes it — into an actionable rollout playbook.

## Instructions

### 1. Anchor the rollout in where work already lives

Per the post, Claude Cowork "meets work where it already lives": local files and folders, connected apps like Slack and Google Drive, and the browser. Paired with Claude for Excel and Claude for PowerPoint, it can carry context across spreadsheets and slide decks in a single workflow.

When you describe the rollout to stakeholders:

- Frame Claude Cowork as a desktop agent that touches the same files, apps, and browser tabs that the team uses today.
- Plugins, skills, and commands are the customization surface — they are how Claude is shaped to the team's specific work environment.

### 2. Pick a first use case and structure a pilot evaluation

The post lists "how to choose your first use case and structure a pilot evaluation" as one of the guide's headline contents. Treat the pilot as the first decision, not an afterthought.

Pilot framing the post supports:

- Start with one business function rather than the whole org.
- Define what the pilot will measure before it begins.
- Use the pilot's outcomes to justify expansion at the next maturity level.

The verbatim list of guide contents is in [references/guide-contents-from-post.md](./references/guide-contents-from-post.md).

### 3. Use the five-level maturity model to set expectations

The post calls out "a five-level maturity model for Claude Cowork adoption, from chat Q&A to department-wide plugins."

Practical use of the model:

- Identify which level the function is at today (the post anchors level 1 at chat Q&A).
- Identify the next level you are realistically aiming for.
- Set milestones that move one level at a time rather than jumping from chat Q&A to department-wide plugins in one go.

The post does not enumerate the five levels by name beyond the endpoints, so reference the guide itself for the intermediate levels rather than inventing them.

### 4. Plan a six-month roadmap from champion teams to org-wide deployment

The post says the guide includes "a six-month roadmap for moving from champion teams to organization-wide deployment." Apply this in three movements:

- Months 1–2 — pilot with a champion team in a single function.
- Months 3–4 — expand to neighbouring teams using the pilot's playbook and metrics.
- Months 5–6 — make the deployment org-wide and codify customizations (plugins, skills, commands) as shared assets.

Treat this as the post's framing; the exact monthly cadence and gates inside the guide should be sourced from the guide itself.

### 5. Use the post's reference patterns instead of inventing your own

The post specifically names the reference patterns it relies on:

- Anthropic's own finance, legal, sales, and product teams using Cowork in production.
- Customer stories from Thomson Reuters, Zapier, and Jamf.

When justifying the rollout internally, lean on these as the post's evidence base. Do not invent additional success stories the post does not cite.

The full list with the post's exact wording is in [examples/internal-team-and-customer-references.md](./examples/internal-team-and-customer-references.md).

### 6. Read the guide before committing the plan

The post is the announcement; the depth lives in the guide it links. Before signing off on a rollout plan derived from this skill:

- Open the guide via the post's "Check it out, here" link.
- Replace any of this skill's structural placeholders (the five intermediate maturity levels, the six-month gates) with what the guide actually specifies.

## Examples

### Example A: Legal function rollout

1. Pick a champion legal team for the pilot.
2. Define the first use case (e.g., contract triage) and the metrics for the pilot evaluation.
3. Place the team on the five-level maturity model — likely starting at chat Q&A.
4. Plan a six-month path: champion team → neighbouring legal sub-teams → all of legal.
5. Reference the post's mention that Anthropic's own legal team uses Cowork in production when justifying the plan.

### Example B: Finance function rollout

1. Pick a champion finance team and tie the pilot to a recurring deliverable.
2. Decide which mix of Claude for Excel + Cowork covers the workflow.
3. Use the five-level maturity model to set the next milestone, not a future state several levels away.
4. Plan the six-month champion-to-org-wide path.
5. Reference Anthropic's own finance team plus the named customer stories (Thomson Reuters, Zapier, Jamf) when speaking with stakeholders.

### Example C: Sales function rollout

1. Pick a champion sales team focused on a specific motion (e.g., named-account research).
2. Configure plugins, skills, and commands to wrap the existing CRM and Slack workflow.
3. Use the maturity model to anchor the milestone — for example, moving from chat Q&A on accounts to embedded plugins in the team's daily workflow.
4. Plan the six-month roadmap, using the post's customer stories as the social proof for expansion.

## Source

New guide: Deploying Claude across the enterprise with Claude Cowork — Anthropic, April 29, 2026: <https://claude.com/blog/new-guide-deploying-claude-across-the-enterprise-with-claude-cowork>
