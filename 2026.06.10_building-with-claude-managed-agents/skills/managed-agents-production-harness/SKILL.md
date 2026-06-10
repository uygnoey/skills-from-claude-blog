---
name: managed-agents-production-harness
description: A checklist and guidance for taking a tool-using Claude agent from prototype to production by separating the harness (agent runner) from the execution sandbox, with emphasis on sessions, credentials, and observability.
---

# Managed Agents production harness checklist

This skill distills production-oriented requirements described in the Claude blog post “The evolution of agentic surfaces: building with Claude Managed Agents”.

## Instructions

Use this checklist when designing or reviewing a production agent system.

1. Define the agent surface
   - Clarify the task, tools, and guardrails.
   - Decide whether you need a managed harness or will maintain your own.

2. Separate harness and sandbox
   - Treat the harness (model calls, orchestration) and the execution sandbox (tool/code runtime) as separate components.
   - Prefer an architecture where credentials do not live in the sandbox.

3. Make sessions first-class
   - Persist an append-only log of: every model call, tool call, and result.
   - Ensure a run can be reconstructed from the session log for debugging.

4. Credentials and secret handling
   - Keep tool tokens out of the sandbox.
   - Retrieve/decrypt secrets only on demand via a dedicated component.
   - Track which end user the agent acted on behalf of without passing tokens on every call.
   - See: [references/vaults-and-credentials.md](./references/vaults-and-credentials.md)

5. Reduce latency and wasted work
   - Avoid spinning up an execution environment for sessions that never use tools.
   - Allow model reasoning to start in parallel with environment startup.

6. Observability
   - Provide a timeline view and transcript-level debugging of each session.
   - Export/emit telemetry (e.g., via OpenTelemetry) if you run the harness yourself.

7. Persistence, pause/resume, and checkpointing
   - Preserve session history between interactions unless explicitly deleted.
   - Support pausing and resuming sessions cleanly.
   - Checkpoint idle sandboxes so work resumes reliably.

8. Network and deployment options
   - Decide whether sandboxes run in a managed cloud environment or inside your own infrastructure (e.g., VPC).
   - If sandboxes are self-hosted, ensure filesystem and network egress stay within your boundary.
   - If connecting to internal tools, consider controlled tunnels.

9. Long-term improvement hooks
   - If you maintain memory stores, schedule a review process that looks across sessions to curate durable memories.

## Examples

### Example: Production readiness review
Use the following prompts in a design review:

- “Where do credentials live, and can the sandbox access them directly?”
- “Do we persist a complete append-only session log (model calls, tool calls, results)?”
- “Can we reconstruct any run from the session log for debugging?”
- “What happens when the agent is idle — do we checkpoint state?”
- “Which sessions never use tools, and are we paying container startup cost anyway?”

### Example: Mapping responsibilities
- Harness responsibilities: model calls, tool selection, orchestration, session logging.
- Sandbox responsibilities: executing tool/code steps with restricted access and controlled networking.

## Bundled resources

- Reference note on credential separation: [references/vaults-and-credentials.md](./references/vaults-and-credentials.md)
- Reference note on sessions and event logs: [references/sessions-and-events.md](./references/sessions-and-events.md)
- Checklist template you can copy into a PRD: [templates/production-harness-checklist.md](./templates/production-harness-checklist.md)

## Source

- https://claude.com/blog/building-with-claude-managed-agents
