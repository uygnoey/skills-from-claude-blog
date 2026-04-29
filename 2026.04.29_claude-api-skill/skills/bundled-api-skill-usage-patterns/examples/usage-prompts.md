# Usage prompts and slash commands (from the post)

These are the four prompts the April 29, 2026 launch post puts forward as ways to ask the bundled `claude-api` skill for help. Each one is paired with what the post says it does.

## 1. "Improve my cache hit rate."

> "The skill applies prompt caching rules many developers miss."

When to use: an existing Claude API agent or app where you suspect cache misses are eating into latency or cost.

## 2. "Add context compaction to my agent."

> "It walks you through the compaction primitives and agent patterns in our docs."

When to use: a long-running agent that is hitting context-length limits or where prompt size is growing turn over turn.

## 3. "Upgrade me to the latest Claude model."

> "Claude reviews your code and walks you through updating model names, prompts, and effort settings for a new model like Opus 4.7. In Claude Code, you can also run this directly with `/claude-api migrate`."

When to use: a model migration. Inside Claude Code, prefer the slash command.

## 4. "Build a deep research agent for my industry."

> "Claude walks you through configuring Claude Managed Agents, so long-running research is a few prompts, not a custom project. In Claude Code, you can also run this directly with `/claude-api managed-agents-onboard`."

When to use: standing up a Claude Managed Agents-based deep research agent. Inside Claude Code, prefer the slash command.

## Slash command reference

| Workflow | Long-form prompt | Slash command (Claude Code) |
| --- | --- | --- |
| Model migration | "Upgrade me to the latest Claude model." | `/claude-api migrate` |
| Deep research agent onboarding | "Build a deep research agent for my industry." | `/claude-api managed-agents-onboard` |

## Source

Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp — Anthropic, April 29, 2026: <https://claude.com/blog/claude-api-skill>
