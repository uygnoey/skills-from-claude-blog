# Target single-loop design

Source: "Building agents: When to fold subagents into your main agent loop" (Claude, 2026-10-22).

- One model and one context window run an open-ended tool loop. The harness sets limits: turn and cost
  budgets, write gates.
- Each turn the model emits a batch of tool calls; the harness runs them in parallel and returns raw
  results to the same model, which decides the next step: another batch, a question to the user, or an
  answer.
- The loop stops when the model answers or hits a budget. A goal or verifier check can optionally run
  after the answer.
- The model writes its plan in context on the first turn and revises it as results arrive. The model
  that writes the plan also carries it out, so it can change the plan mid-turn.
- Context is still loaded, but managed by the agent:
  - no code step that rewrites the plan from a catalog of rules;
  - ordering and domain procedure live in **skills**;
  - hard limits (validation, approval gates) and mid-conversation needs (e.g. memory lookup) live in
    **tools**;
  - code still loads anything cheap and almost always relevant (e.g. entity resolution) and handles
    mechanical parts (payload construction, stream parsing, resuming a clarification) inside tools.
- Ownership: one small central team owns the system prompt and end-to-end quality and vets new skills,
  tools, and evals.

This design also suits the end state of an agent that understands a user's high-level goals and acts
on their behalf, because everything the agent has learned stays in one context.
