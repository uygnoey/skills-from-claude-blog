# Sessions and event logs (reference)

From the source post:

- Managed Agents decouples the harness (“brain”) from the sandbox (“hands”).
- A session is described as an append-only log of every model call, tool call, and result.
- Because events are appended outside the process running the agent, a whole run can be reconstructed later.
- Durable sessions enable debugging timelines and features like Memory and Dreaming.

## Practical implications

- Store the session log in a system separate from the sandbox runtime.
- Ensure event schemas are stable enough to support later replay/inspection.
- Preserve transcripts unless explicitly deleted (to support debugging and learning).

## Source

- https://claude.com/blog/building-with-claude-managed-agents
