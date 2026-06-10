**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# The evolution of agentic surfaces: building with Claude Managed Agents

## What is this post?
This post explains Claude Managed Agents: a set of composable APIs for building and deploying production-grade agents on managed infrastructure.

It contrasts earlier “tokens in, tokens out” API usage with agentic products like Claude Code and the Claude Agent SDK, then introduces Managed Agents as a way to decouple the agent harness ("brain") from the execution sandbox ("hands").

## When is it useful?
- When you want to run agents reliably in production without building and maintaining the full harness and infrastructure yourself.
- When you need secure credential handling, persistent session logs, observability, and scalable orchestration for tool-using agents.
- When you want to separate model reasoning from sandbox execution (including options for self-hosted sandboxes/VPC execution).

## Key points
- A production agent requires more than a prompt: hosting, scaling, session management, filesystem state, execution isolation, credentials, and observability.
- Managed Agents separates the harness from the sandbox; a session is an append-only log of model calls, tool calls, and results.
- Credentials can be kept out of the sandbox via Vaults and on-demand retrieval, reducing exposure to prompt injection.
- Latency can improve because reasoning can start before a container exists, and sessions that never use tools can avoid container startup.
- Durable sessions enable debugging timelines, Memory, and Dreaming (a scheduled process that reviews sessions/memories to curate future memories).

## Bundled resources
- Skill: Production harness checklist and architecture notes derived from the post.
- Reference notes: Vaults, sessions, and managed/sandbox separation concepts.

## Source
- https://claude.com/blog/building-with-claude-managed-agents
