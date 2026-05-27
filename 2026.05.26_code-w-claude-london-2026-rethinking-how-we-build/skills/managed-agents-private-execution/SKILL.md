---
name: managed-agents-private-execution
description: Use this skill to decide whether to run Claude Managed Agents with self-hosted sandboxes and/or MCP tunnels, and to collect the minimum deployment details and security considerations for each option.
---

## Instructions

You are helping an engineering team plan private execution for Claude Managed Agents.

1) Clarify goals and constraints
- What must stay inside the network boundary (code execution, tool access, or both)?
- What compliance, audit, or data residency constraints apply?
- What internal systems must be reachable (databases, ticketing, knowledge bases), and are they publicly routable?

2) Choose the right capability (or both)
- Recommend **self-hosted sandboxes** when the primary need is to control *where agent code executes* and keep files/repositories inside the organization’s perimeter.
- Recommend **MCP tunnels** when the primary need is to let agents reach *private MCP servers* without exposing inbound endpoints.
- If both execution locality and private tool access are required, recommend using **both** together.

3) Collect required implementation details
- For self-hosted sandboxes: execution environment, network policies, audit logging expectations, and whether compute will run on your own infrastructure or a supported managed provider.
- For MCP tunnels: which MCP servers will be routed, and which org/workspace admins will manage tunnels and certificates in the Console.

4) Produce an actionable plan
Provide:
- A short recommendation (self-hosted sandbox, MCP tunnels, or both)
- A deployment checklist
- A risk checklist (secrets handling, network restrictions, certificate management, audit logs)

For authoritative product details and limitations, cite the bundled reference.

## Examples

### Example: execution must stay inside the perimeter
User: Our agents need to run code against a monorepo that cannot leave our network, and must follow our audit logging and egress policies.
Assistant (using this skill): Recommend self-hosted sandboxes, gather required runtime/infra details, and produce a deployment + risk checklist. Reference: `references/managed-agents-private-execution.md`.

### Example: tool access must stay private
User: We have internal MCP servers for ticketing and knowledge base search; we can’t expose them publicly.
Assistant (using this skill): Recommend MCP tunnels, gather which servers/routes are needed, who will manage tunnels in Console, and produce a deployment + risk checklist. Reference: `references/managed-agents-private-execution.md`.

### Example: both execution and tools must stay private
User: We need agents to execute inside our infra and also call internal MCP servers.
Assistant (using this skill): Recommend combining self-hosted sandboxes + MCP tunnels, and produce a phased rollout plan with controls. Reference: `references/managed-agents-private-execution.md`.
