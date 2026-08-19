# The self-improving loop

Agents work under human supervision, posting what they did or what they recommend to a chat channel, where people reply in threads and react with emoji. All of that reaction data is a training signal — and it goes to waste unless something collects it.

**Not every agent needs the signal.** Most of a fleet are single-task runners whose output no one grades, and they work alone. Build the loop only for agents that actually collect graded feedback.

## The three roles

For the agents that do, use three separate agents that **share one workspace, environment, and credential vault but run on different schedules**:

| Role | Cadence | What it does |
|---|---|---|
| **Initial Agent** | Real time, as a job comes in or a document comes back | Does the work. Records an audit trail of each action. |
| **Harvester** | Hourly or daily | Gathers human feedback from the chat channel — thread replies and emoji reactions. Each one becomes a labeled data point. |
| **Tuner** | Weekly | Looks across everything at once and proposes a change to the prompt or config. **It drafts only.** A human reviews and merges the pull request. |

The pattern turns messages in a chat channel into versioned, human-approved changes to the agent. Agents improve through the same workflows developers already use.

Critically: **the tuner changes the prompt or the config, not the model's weights.** No retraining is involved. That is what keeps the improvement path reviewable and reversible.

## Why the roles are separate agents

They run on different schedules, which is the practical reason. But separation also means the initial agent's real-time path stays simple and its permissions stay narrow, while the tuner — which touches the definition of another agent — is reviewed on its own terms.

## Making output harvestable

An agent posts every result to a shared channel, naming the item it acted on and the counts that came out of it, so the trail of what the agent decided is public and searchable.

Format the output so a reader can register agreement or disagreement in a single emoji reaction. If a reader cannot tell what they would be agreeing with, the harvester collects noise.

## The four-agent variant: pushing config back to production

When the thing being tuned is not the agent's own prompt but a business configuration, the loop gains a fourth role.

At the sister company in the source story, work is organized around **deliveries**, each with its own ruleset for routing and handling. All ~145 rulesets are **single YAML files in git rather than records in an admin screen**, so tuning a delivery means editing a file and opening a pull request.

The loop:

1. An agent posts a **weekly verdict** to the channel.
2. The **Harvester** turns reactions into labels based on human feedback.
3. The **Tuner** opens a pull request on the YAML.
4. A **fourth agent pushes the merged config to the production database** — and executes only what a human has already reviewed and approved.

In practice, an emoji reaction flagging a mis-routed delivery can become a merged change to that delivery's routing rules within the week. **The review is the only manual step in the loop.**

## Where this generalizes

The same shape applies to anything currently living as records behind an admin screen — notification templates, event routing rules, dispatch logic, business configuration. Move it into the repo and an agent can read it, reason about it, and propose an improvement.

*"Code is just structured text. LLMs are text engines. The more of your business you can turn into text in a repo, the more leverage agents give you."*

## Source

- https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
