# One shared memory, and credentials the fleet never sees

## The shared knowledge base
In the prototype the knowledge base is a shared folder on the laptop; on Managed Agents it is a
memory store. Either way it is one store that every agent in the fleet reads and writes, and it is
where the fleet's context lives instead of in a longer prompt.

What goes into it:
- **The difference between what an agent drafted and what the human actually sent.** Each difference
  is saved as a note on how the human would phrase it.
- **Anything new an agent dug up while researching an answer** — from internal docs and official
  websites.
- **Product and pricing updates**, written in by the coordinator from the morning brief.

Why one store rather than one per agent: a phrasing fixed once in the reply agent's drafts stops the
triage and end-of-day agents from making the same mistake. The correction is made in one place and
reused everywhere.

What this changes about prompting: the knowledge base matters more than the prompt. Claude takes its
context from the store, so the prompt does not have to grow. Getting drafts to sound like the human
took a few hundred cheap rounds of drafting, fixing, and saving — not one long prompt.

Who maintains it: the agents write what they learn into it themselves. Treat hand-maintaining it as
a task to hand over, not a task to keep.

## Credentials in managed vaults
The fleet reaches email and Salesforce records — customer conversations and company records — so
access has to stay under control.

- Credentials live in **managed vaults**, which hold the credentials agents use to log in to outside
  services: OAuth access and refresh tokens, API keys, and personal access tokens.
- **Each agent's deployment uses only the vaults its job needs.** Scope per deployment, not per
  fleet.
- **The agent never sees the credentials.**
- **Access can be revoked in one step.**

## Operational notes from the source fleet
- Instruction changes are saved as versions, so each agent keeps a numbered history of its
  instructions.
- While a change is being tried out, scheduled runs keep using the deployed version — a half-finished
  edit does not end up in tomorrow's run.
- When a run goes wrong, it can be opened in the Console to see each step the agent took.

## Source
[How an Anthropic BDR in Japan runs his day with Claude Managed Agents](https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day)
(published 2026-10-16).
