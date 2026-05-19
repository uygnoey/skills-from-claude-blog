**English** · [한국어](./managed-agents-network-perimeter.ko.md) · [Español](./managed-agents-network-perimeter.es.md) · [日本語](./managed-agents-network-perimeter.ja.md)

# Keep agent execution and connectivity inside your perimeter

## What this guide covers
- How self-hosted sandboxes change the execution boundary for Claude Managed Agents.
- How MCP tunnels enable private connectivity to MCP servers without public exposure.

## Practical guidance

### Execution boundary
- Put repositories, files, dependencies, and compute-heavy tool runs inside your sandbox.
- Keep the managed agent loop in the control plane.

### Connectivity
- Prefer MCP tunnels for private MCP servers so you avoid inbound firewall rules and public endpoints.
- Ensure traffic is encrypted end to end.

## Source
- https://claude.com/blog/claude-managed-agents-updates
