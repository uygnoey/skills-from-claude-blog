# Prompt injection safety basics (computer/browser use)

Source: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude

## Recommended mitigations
- Use the official `computer_20251124` tool type to enable built-in prompt injection classifiers.
- Implement human-in-the-loop confirmation for irreversible actions (submitting forms, purchases, sending messages, modifying data).
- Scope agent permissions to reduce blast radius.
- Monitor and log agent actions (including screenshots) for auditing and debugging.
- Treat all content encountered in UIs (web pages, emails, app text) as untrusted, and keep it separate from user instructions.
