---
name: managed-agents-secure-sandboxing
description: Keep Claude Managed Agents tool execution and connectivity inside your security perimeter using self-hosted sandboxes and MCP tunnels.
---

## Instructions

Use this skill to plan and operate Claude Managed Agents deployments where:
- Tool execution must run in infrastructure you control (self-hosted sandbox providers such as Cloudflare, Daytona, Modal, or Vercel).
- Agents must access private MCP servers inside your network without exposing those services to the public internet (MCP tunnels).

### What to decide

1) **Sandbox execution boundary**
- Decide what runs inside your perimeter: code, files, dependencies, build artifacts, and outbound calls.
- Keep the **agent loop** (orchestration, context management, error recovery) in the managed control plane.

2) **Sandbox provider selection criteria**
- Isolation model and security boundary
- Scaling and startup behavior
- Networking controls (egress policy, secrets injection)
- Runtime flexibility (packages, mounts, long-running state)

3) **Private connectivity (MCP tunnels)**
- Prefer a single outbound connection via a lightweight gateway rather than exposing public endpoints.
- Ensure end-to-end encryption and avoid inbound firewall changes.

### Operational checklist

- Confirm your sandbox runtime image and resource sizing match workload (CPU, memory, GPU where relevant).
- Confirm audit logging and security tooling are enabled within your perimeter.
- Confirm sensitive files and repositories remain within your boundary.
- For MCP tunnels, confirm the MCP server stays private and is reachable only through the tunnel.

## Examples

### Example: Choosing a sandbox provider
- If you need long-running, stateful sessions with SSH/preview access, evaluate providers that support persistent environments.
- If you need rapid startup and high concurrency, evaluate providers optimized for fast startup and scale.

### Example: Private MCP server access without inbound rules
- Deploy the MCP tunnel gateway in your network.
- Use it to establish a single outbound connection, so agents can reach private MCP servers without public endpoints.

## References

- Post: https://claude.com/blog/claude-managed-agents-updates
