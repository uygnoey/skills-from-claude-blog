**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post announces two Claude Managed Agents capabilities: running tool execution inside a sandbox you control (self-hosted sandboxes) and securely connecting agents to private Model Context Protocol (MCP) servers via MCP tunnels.

## When is it useful?
Use these features when you need agents to operate on sensitive code, files, or internal systems while keeping execution and network access within your enterprise security boundary.

## Key points
- Self-hosted sandboxes move tool execution into infrastructure you control (or a managed sandbox provider), while the agent loop (orchestration, context management, error recovery) remains on Anthropic infrastructure.
- You can choose a sandbox provider (Cloudflare, Daytona, Modal, Vercel) depending on isolation, scale, networking, and runtime needs.
- MCP tunnels allow agents to reach MCP servers inside a private network without exposing them on the public internet (single outbound connection, no inbound firewall rules, end-to-end encryption).
- Availability: self-hosted sandboxes are in public beta; MCP tunnels are in research preview and require an access request.

## Bundled resources
- Skill: managed-agents-secure-sandboxing (patterns and checklists for choosing and operating self-hosted sandboxes and MCP tunnels)
- Guide: managed-agents-network-perimeter (deployment-oriented guidance on keeping execution and connectivity inside your perimeter)

## Source
- https://claude.com/blog/claude-managed-agents-updates
