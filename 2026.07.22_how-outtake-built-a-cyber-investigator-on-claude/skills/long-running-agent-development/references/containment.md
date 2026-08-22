# Containing an agent you send into hostile environments

The Recon Agent is deliberately pointed at infrastructure built by attackers. It
has a filesystem and bash. Outtake's security posture starts from that
combination rather than from a hope that it will not matter.

> "Security is a big note for us for building the Recon Agent. We gave it a file
> system and bash and we're sending it to adversarial environments."
> — Jack Hayford, engineering lead

## The premise: assume hijack, contain damage

Prompt injection is a real threat, not a hypothetical one. Outtake chose Claude
partly for its strength against prompt injection — but the defense does not stop
at model robustness. The design assumption is that **the agent might be hijacked,
and the surrounding system is engineered to contain the damage**.

This is a different question from "will the model resist the injection?" It is:
*if it does not, what can the compromised agent actually do?*

## The checkpoint at the network boundary

Outtake scores the level of trust **at the exact point where the agent reaches
out to the internet**. A checkpoint evaluates whatever the agent is about to
touch, asking:

- **Is this page an impersonation?**
- **Is it malware?**
- **Is it trying to prompt-inject the agent right now?**

Three properties make this work:

1. **It sits at the boundary, not in the prompt.** Consistent with the "prompts
   are suggestions" learning — a rule the agent is asked to follow will eventually
   be ignored; a rule enforced where the request leaves the system will not.
2. **It runs before the agent touches the content.** Evaluating the target after
   ingestion is too late; the injection has already entered context.
3. **It scores rather than blocks binarily.** Trust level, not allow/deny, so the
   investigation can continue with the right amount of caution instead of
   stopping.

## Placing the boundary

The general shape, applicable beyond cyber investigation:

| Question | Where it belongs |
| --- | --- |
| Should the agent behave carefully here? | The prompt (a suggestion, and that is fine) |
| Must the agent never do X? | Hardcoded guardrail at the orchestration layer |
| Is this specific external thing safe to touch? | Checkpoint at the network boundary, before contact |
| If the agent is compromised, what can it still reach? | The permission and environment design, decided in advance |

The last row is the one that gets skipped. It is answered by design, before
deployment — not by inspecting behavior afterwards.

## Why open-ended tools raise the stakes and are still worth it

The filesystem and bash are what make the agent resilient: memory that survives
compaction, and the ability to work around an obstacle rather than stalling. They
are also exactly what makes a hijacked agent dangerous. The resolution is not to
take the tools away — it is to decide, in advance, what a compromised session can
reach, and to check what the agent touches before it touches it.

## Source

[How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude) — Michael Segner, July 22, 2026
