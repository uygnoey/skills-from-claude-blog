**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Outtake, founded in 2023 by Alex Dhillon (previously on Palantir's moonshot team), built an autonomous cyber investigator called the **Recon Agent** — first prototyped in Claude Code, then moved to the Claude Agent SDK for production. It detects, investigates, and dismantles digital threats across whole attack networks, and scanned more than 20M potential cyberattacks in 2025.

Dhillon frames the problem from the attacker's side: "If you put on the bad actor's hat, it's actually a great time to be running attacks. The average attack is not only executed faster because of AI, but it also captures deeper access due to AI." Attacks run in three stages — weaponize public data, build impersonations as lures, exploit internal systems — and traditional tools address each stage separately. The Recon Agent instead maps the whole adversarial network: from a single cloned login page it gathers and classifies evidence, follows leads to connected infrastructure such as a fake Telegram account presenting itself as "Customer Support," and produces an investigation report with actor profiles and an attack timeline. It reads, writes, and runs code, and interacts with malicious login pages directly to trace where stolen credentials go. Median session runtime is 16 minutes; sessions routinely run an hour, and the longest observed was two.

Most of the post is engineering lessons from Jack Hayford, engineering lead: a four-stage development process, and four hard-won learnings about long-running agents — on tools, on why prompts stop working, on evals as a speed instrument, and on defending an agent you are deliberately sending into adversarial environments.

## When is it useful?
- When building an agent whose sessions run for tens of minutes to hours, where context compaction and drift are real rather than theoretical.
- When deciding whether to stay in Claude Code or graduate to the Claude Agent SDK, and what you gain by moving.
- When an agent keeps ignoring an instruction in its system prompt no matter how the instruction is worded.
- When deciding which tools an agent needs, and whether a purpose-built tool beats a filesystem and bash.
- When you cannot tell whether a change to the agent helped, because reviewing 30-minute transcripts by hand does not scale.
- When an agent must operate in an environment that is actively hostile, including pages built to prompt-inject it.

## Key points
- **Become the expert before you build.** The team ran real investigations themselves and pulled domain expertise from customers and design partners. Hayford: "The most important thing about building long running agents is that you really have to understand *what does good look like? What is the agent supposed to be doing?*"
- **Prototype in Claude Code, graduate deliberately.** Traditional agent frameworks did not have enough coding capability: "Every investigation is different, and deeply technical. The agent needed coding muscle and capability, and Claude Code was a strong initial harness." Production needed lower-level primitives — "We really liked the patterns that Claude Code had introduced, but we needed additional access to the lower level primitives" — so the team moved to the Agent SDK for tighter control over memory, context, and the file system without rebuilding the agent loop.
- **Constrain orchestration, not judgment.** Tightly specify what always happens (X, then Y, then Z) and leave improvisation space where the work requires judgment.
- **A filesystem and bash go remarkably far.** A filesystem gives memory that survives context compaction; bash lets the agent route around obstacles. "We've observed plenty of cases where an agent had a tool that was failing due to a network hiccup or whatever, and it would just find the right workaround and continue."
- **Prompts are suggestions.** "When you're building these long-running agents that get complicated over time, prompts are suggestions. Every single word in that prompt will probably be ignored eventually." Behavioral requirements move out of the prompt and into hardcoded guardrails at the orchestration layer, which also preserves context for high-judgment work.
- **Evals are for speed, not just reliability.** Manually reading 30-minute transcripts does not scale. Evals turn reflection into structured graded checks: "Building some version of evals from the very beginning will make you build that agent faster regardless of how official or 'perfect' they are."
- **A second agent closes the tool gap.** When the Recon Agent finishes an investigation and reports it could have done better with a tool it did not have, a separate coding agent reads those suggestions, writes the new tool, and builds a test scenario to try it out — humans only evaluate the final result.
- **Assume the agent can be hijacked, then contain the damage.** "Security is a big note for us for building the Recon Agent. We gave it a file system and bash and we're sending it to adversarial environments." Outtake scores trust at the exact point the agent reaches out to the internet, with a checkpoint asking: "Is this page an impersonation? Is it malware? Is it trying to prompt-inject the agent right now?"

## Bundled resources
- `skills/long-running-agent-development/` — the four-stage build process and the four learnings as a working method, with references on the harness decision and on containment, a template for the "what does good look like?" definition that gates every iteration, and an example walking the Recon Agent's investigation loop.
- `agents/recon-investigator.md` — the long-running investigation agent: gather and classify evidence, follow leads to connected infrastructure, map the adversarial network as a graph, report actor profiles and an attack timeline.
- `agents/tool-gap-builder.md` — the separate coding agent that reads an investigation's tool suggestions, writes the missing tool, and builds a test scenario for it.
- `guides/building-long-running-agents.{en,ko,es,ja}.md` — the full walkthrough in four languages.

## Source
[How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude) — Michael Segner, July 22, 2026
