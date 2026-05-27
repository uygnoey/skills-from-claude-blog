# Managed Agents private execution: self-hosted sandboxes and MCP tunnels

This reference summarizes the concrete product details mentioned in the Code w/ Claude London 2026 recap and links to the canonical docs.

## Self-hosted sandboxes (public beta)

What it is:
- Claude Managed Agents can run in a sandbox you control.
- Agent orchestration (the agent loop for context management and error recovery) remains on Anthropic infrastructure.

Why teams use it:
- Operate on data that should not leave your network boundary.
- Reach internal services that are not publicly routable.
- Run under your organization’s compliance, audit, and network controls.

Operational notes:
- You control compute sizing and the runtime image.
- You can apply your standard network policies, audit logging, and security tooling.
- Compute execution can use your own infrastructure or a managed provider.

Canonical docs:
- Self-hosted sandboxes: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes

## MCP tunnels (research preview)

What it is:
- MCP tunnels connect Claude to MCP servers inside your private network.
- A lightweight gateway you deploy makes a single outbound connection; you do not need inbound firewall rules or public endpoints.

Operational notes:
- Traffic is encrypted end to end.
- Tunnels are managed from the Claude Console by organization admins.

Canonical docs:
- MCP tunnels overview: https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview
- Manage tunnels in the Console: https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console

## Related announcement
- New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels: https://claude.com/blog/claude-managed-agents-updates
