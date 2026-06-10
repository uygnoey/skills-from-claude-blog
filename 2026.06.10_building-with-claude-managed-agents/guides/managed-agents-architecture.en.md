**English** · [한국어](./managed-agents-architecture.ko.md) · [Español](./managed-agents-architecture.es.md) · [日本語](./managed-agents-architecture.ja.md)

# Managed Agents architecture overview

## What is this guide?
A concise architecture overview based on the post “The evolution of agentic surfaces: building with Claude Managed Agents”.

## Core idea
Managed Agents separates:
- The harness ("brain"): orchestration and model calls.
- The sandbox ("hands"): the execution environment for tools/code.

A session provides an append-only event log connecting the two.

## Why the separation matters
- Security: credentials can stay out of the sandbox.
- Performance: reasoning can begin before a container exists; sessions that never use tools can avoid container startup.
- Operability: durable sessions enable debugging timelines, pause/resume, and higher-level features (Memory, Dreaming).

## Concepts mentioned in the post
- Agents, environments, sessions as composable resources.
- Vaults for credentials.
- Optional self-hosted sandboxes (e.g., inside a VPC).
- MCP tunnels for connecting to private-network MCP servers.

## Source
- https://claude.com/blog/building-with-claude-managed-agents
