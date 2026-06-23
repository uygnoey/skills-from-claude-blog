**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post explains the “agent identity” access model in Claude Tag: how workspace-admin provisioned tool identities let Claude operate in shared channels without borrowing any individual user’s accounts.

## When is it useful?
Use these ideas when you are enabling AI agents in team-wide spaces (shared channels, projects, workspaces) and need a permissions model that is auditable, revocable, and scoped so an agent’s access does not accidentally expand beyond what was explicitly granted.

## Key points
- Multiplayer agent experiences need workspace-owned tool identities, not personal accounts.
- Permissions should be scoped to the channel (or equivalent shared space), and revocable centrally.
- Roll out access gradually: start with a baseline profile in a few channels, review the audit trail, then extend deliberately.
- Keep hard boundaries so shared spaces never become a side door into private documents; memory and access should respect those boundaries.
- Prefer a credential pattern where credentials are stored independently, mapped to the channel identity, and injected only at request time.
- Block outbound network traffic to unapproved hosts, and audit every routine, memory write, and network call.

## Bundled resources
- Skill: “Agent identity access model playbook” (guidance distilled from this post)

## Source
- https://claude.com/blog/agent-identity-access-model
