**English** · [한국어](./managed-agents-private-execution-overview.ko.md) · [Español](./managed-agents-private-execution-overview.es.md) · [日本語](./managed-agents-private-execution-overview.ja.md)

# Private execution options for Claude Managed Agents (overview)

## What is this?
A short, decision-oriented guide to two Claude Platform capabilities mentioned in the Code w/ Claude London 2026 recap: self-hosted sandboxes and MCP tunnels.

## Decision tree
1) Do you need to control **where agent code executes** (data and files must remain inside your boundary)?
- Yes → Self-hosted sandboxes.

2) Do you need Claude to reach **private MCP servers** without exposing inbound endpoints?
- Yes → MCP tunnels.

3) Do you need both?
- Yes → Use both together.

## Implementation checklist (high level)
- Identify the data boundary (repos, files, secrets, logs).
- List internal tools to expose (MCP servers), and their required auth.
- Define network egress policy and audit logging requirements.
- Assign owners: runtime/infra, security, and Console administrators.

## Further reading
- Reference: `../skills/managed-agents-private-execution/references/managed-agents-private-execution.md`
- Event recap source: https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
