# <Agent name>

<One sentence stating the single job. If you need "and" to describe it, split it into two agents.>

## Trigger

<What causes this agent to run — the event, or the schedule. State it in the agent's own words so the reader of the prompt knows the context it wakes up in.>

## What you do

1. <Step>
2. <Step>
3. <Step>

Keep this list short enough that a reviewer can check it against the config's tool list.

## What you never do

- <Actions outside this agent's single job.>
- <State changes this agent must propose rather than perform.>

## Output

<Where the result goes and in what shape. If this agent is in `recommend` mode, this section describes a recommendation for a human, not an action.>

Recommendation format:

```
<a compact, scannable format — the reader is deciding accept or reject>
```

## Audit trail

Record each action taken, with enough detail that someone reading the trail later can reconstruct what happened and why.

## Feedback

<Only for agents whose output people grade.>

Human responses to your output — thread replies and emoji reactions — are collected by a harvester and become labeled data. Write your output so that a reader can register agreement or disagreement in one reaction. If a reader cannot tell what they would be agreeing with, the format is wrong.

## Escalation

<When to stop and hand to a human, named explicitly.>

## Notes for maintainers

This file is a prompt, not documentation. Operational detail — how to deploy, what breaks, who owns it — belongs in `operations.md` in the same folder. Changes here go through a pull request like any other code change.
