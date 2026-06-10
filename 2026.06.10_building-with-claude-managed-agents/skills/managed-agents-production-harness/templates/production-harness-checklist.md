# Production harness checklist (template)

Copy/paste this into a PRD or design doc and fill it in.

## Scope

- Agent task:
- Tools:
- Guardrails:
- Target deployment:
  - [ ] Managed harness
  - [ ] Self-managed harness
  - Sandbox location:
    - [ ] Provider-managed
    - [ ] Self-hosted (VPC)

## Core requirements

### Sessions

- [ ] Append-only log stored outside the sandbox
- [ ] Includes model calls, tool calls, and results
- [ ] Run is reconstructible from logs
- [ ] Pause/resume supported

### Credentials

- [ ] No credentials stored in sandbox
- [ ] On-demand retrieval/decryption path exists
- [ ] Access is auditable

### Observability

- [ ] Timeline view / transcript-level debugging
- [ ] Telemetry export (if self-managed harness)

### Reliability and latency

- [ ] Sandbox is not started for sessions that never use tools
- [ ] Reasoning can start in parallel with sandbox startup
- [ ] Idle sandbox can be checkpointed

## Source

- https://claude.com/blog/building-with-claude-managed-agents
