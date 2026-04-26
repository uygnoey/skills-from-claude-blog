# Evolution of AI coding tools

A reference summarizing the three-stage evolution narrated in [Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (2025-10-30). Use it to set context before introducing Claude Code.

## 1. Code prediction and completion

- Examples: IDE autocomplete extensions.
- Strengths: predictable patterns — REST endpoint boilerplate, test scaffolding, common algorithms; fast feedback inside the editor.
- Mechanism: predicts based on the immediate context (function signature, surrounding code, recently imported modules).
- Limits: small context window, typically the current file or a few nearby files. Cannot trace data flow through the application or understand cross-service impact.

## 2. Conversational AI chat interfaces

- Examples: Claude.ai and other browser-based assistants.
- Strengths: analysis and guidance on pasted snippets — slow query optimization, architectural trade-off review, error troubleshooting; iterative refinement.
- Mechanism: dialogue. Ask a general question, get a response, clarify, narrow.
- Limits: orchestrating multi-file change is manual. Refactoring a module imported by 30 files becomes "paste each file in, copy edits back, ensure consistency by hand." Chat assists; humans coordinate.

## 3. Agentic coding

- Examples: Claude Code.
- Strengths: take a high-level goal, read across the entire codebase, run commands, iterate based on environment feedback.
- Mechanism: two-phase workflow — context gathering and planning, then implementation and coordination across multiple files.
- Limits and ergonomics: still requires human oversight via the permission model. The post recommends "start slow, then expand" rather than delegating critical surfaces on day one.

## How to use this reference

When onboarding a teammate, walk through the stages above to anchor expectations:

1. Confirm what they already use (autocomplete? chat?).
2. Show how Claude Code's autonomy and scope differ.
3. Pair the explanation with the [first-prompts](../examples/first-prompts.md) hands-on demo.

## Source

[Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (2025-10-30).
