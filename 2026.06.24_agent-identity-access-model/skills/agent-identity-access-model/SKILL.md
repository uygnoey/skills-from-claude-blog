---
name: agent-identity-access-model
description: Configure and roll out workspace-owned “agent identities” for team-wide AI agents with least privilege, strong boundaries, and reliable auditing.
---

## Instructions

### Goal
Set up an access model for agents operating in shared team spaces (channels/projects/workspaces) where tool access is:
- Owned by the workspace (not a single person)
- Scoped to a shared space (e.g., a channel)
- Centrally revocable
- Auditable end-to-end

### Core concepts to implement
1. **Use workspace-owned tool identities**
   - Provision service accounts / app identities for the agent, created by an admin.
   - Do not rely on individual users’ personal accounts for shared-channel automation.

2. **Scope permissions to the shared space**
   - Treat each channel (or equivalent shared space) as the unit of authorization.
   - Ensure removing the identity ends access everywhere the identity was used.

3. **Roll out access gradually**
   - Start with a baseline profile in a small number of channels.
   - Review audit trails to confirm the access is used as intended.
   - Expand access deliberately, one grant at a time.

4. **Maintain hard boundaries**
   - Shared spaces must not become a side door into private documents.
   - Ensure memory and access follow identity boundaries (private stays private).
   - Keep boundaries firm enough that access never travels somewhere it wasn’t granted.

5. **Prefer a safe credential injection pattern**
   - Store credentials independently.
   - Map credentials to the channel’s identity.
   - Inject credentials at the network boundary at request time.

6. **Constrain and audit external activity**
   - Block outbound requests to hosts the admin has not explicitly allowed.
   - Record an audit trail for every routine, memory write, and network call made using agent credentials.
   - Ensure connected systems also receive their own action logs when applicable.

## Examples

### Example: staged rollout checklist
- Choose 2–3 low-risk channels for initial deployment.
- Provision least-privileged tool identities for the baseline tasks.
- Enable access only for those channels.
- Observe the audit trail over real work.
- Tighten boundaries if any access appears broader than intended.
- Expand to additional channels only when the work clearly justifies it.

### Example: boundary tests
- Verify that content learned in a private channel does not appear in other channels.
- Verify that disabling the identity removes access across all integrations that used it.
- Verify outbound network requests are blocked for unapproved hosts.

## Source
- https://claude.com/blog/agent-identity-access-model
