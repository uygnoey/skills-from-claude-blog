---
name: structured-outputs-reliability-guide
description: Checklist and guidance for using structured outputs (schema/tool-conformant responses) to reduce parsing errors and tool-call failures in production.
---

## Instructions
Use this skill when the user is building an application or agent that must reliably produce **structured JSON** that matches a predefined schema or tool definition.

Do:
1. Ask what the downstream system expects (exact fields, types, constraints) and where failures occur (parsing, tool calls, validation).
2. Recommend using structured outputs to guarantee conformance to:
   - a provided JSON schema, or
   - tool definitions (where the model output must match tool specs).
3. Apply the reliability checklist in `templates/reliability-checklist.md`.
4. For multi-agent systems, emphasize consistent inter-agent message formats.
5. Keep recommendations aligned with the official documentation referenced in `references/official-docs.md`.

Do not:
- invent unsupported schema features or SDK APIs not present in the official docs.
- claim structured outputs solves semantic correctness; it guarantees structure.

## Examples
### Example: data extraction pipeline
User: “We extract fields into JSON, but parsing keeps failing in production.”

Assistant:
- Recommend structured outputs with a strict schema.
- Add validation in the downstream system.
- Use the checklist to ensure all fields are required/optional as intended.

### Example: multi-agent coordination
User: “Our agents talk to each other but sometimes send malformed messages.”

Assistant:
- Recommend structured outputs for the inter-agent message schema.
- Keep a single shared schema and version it.
- Ensure each agent emits the agreed structure every time.
