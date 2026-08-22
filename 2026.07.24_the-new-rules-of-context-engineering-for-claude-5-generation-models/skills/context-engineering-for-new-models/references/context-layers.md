# The four layers of assembled context

Context arrives from several places at once. Each has a job; problems start when one layer takes on
another's.

## System prompt

Tied to the product: what product the agent operates within, and what role it plays there. Claude Code
users mostly never modify it. If you are building a custom agent, this is the layer that deserves
significant effort — it is where the agent's identity and operating context live.

It is *not* where tool usage instructions belong (see shift 4), and not where an accumulating pile of
prohibitions belongs (shift 1).

Anthropic removed over 80% of Claude Code's system prompt for Claude 5 models, with no measurable loss
in coding evaluations.

## CLAUDE.md

Keep it lightweight. It should say what the repository is, and then concentrate on the **gotchas** —
the things that are only discoverable by being told, not by reading the code. Non-obvious patterns,
the build step that has to run first, the directory that looks unused and is not.

When instructions get complex, do not grow the file. Move them into a separate skill and let
progressive disclosure bring them in when they apply.

Memory that you used to pin here with `#` is now saved automatically (shift 5).

## Skills

Lightweight guides for finding information on demand. Two rules from the post:

- **Avoid over-constraining**, except in the areas that critically matter.
- **Encode the opinions and best practices** that are specific to your team or product. Generic advice
  is already in the model; your particular way of doing things is not.

Divide a long skill into multiple files rather than one long body — the same progressive-disclosure
logic that applies to CLAUDE.md applies inside a skill.

## References

Where depth goes. Pull them in with @mentions: specs, mockups, codebases.

Prefer **code** for clarity and fidelity over descriptive text. A description of a behavior is a lossy
encoding of the behavior; the code, the test, or the rubric is not.
