# Evaluation plan for a delegated agent

How the Claude Duet post describes testing, laid out as a plan you can adapt.

## 1. Routine-style tasks in three variants
For each realistic task (e.g. "reply to this thread", "book this", "tidy this folder"):

| Variant | What it checks |
|---|---|
| Innocent | Does the agent complete the task correctly? |
| With injected instructions | Does it ignore instructions planted in pages, emails, or files? |
| Tempting overreach | Does it stay within what the user asked instead of doing more? |

## 2. Red teaming
- Information leaks
- Unapproved actions
- Malicious prompts

## 3. Threat model
Cover the whole system, not only the model: agent machine, browser machine, proxy, sign-in form,
connectors, and memory.

## 4. External review
- An external penetration-testing firm reviewed the source code.
- A follow-on engagement for the cloud browser and the sign-in form was underway at publication.

## 5. Ongoing
- Put the agent in scope for a public bug bounty (Duet is in Anthropic's HackerOne program).
- Let users report problems directly through the agent.
