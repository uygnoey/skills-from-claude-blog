---
name: hackathon-builder-patterns
description: Reusable planning and iteration patterns drawn from multiple winning projects in Claude’s “Built with Opus 4.7” hackathon.
---

## Instructions
Use this skill as a checklist of proven build patterns highlighted by hackathon winners.

1) Plan before you build
- Write a short spec and a step-by-step plan before implementing.
- Separate responsibilities (e.g., design, ingestion, core logic) so you can iterate cleanly.

2) Parallelize intentionally
- Split work across multiple Claude Code sessions when components have distinct contexts.
- When debugging, try multiple agents in parallel with one agent per domain.

3) Treat Claude as a thought partner
- Brainstorm options and ask for alternatives (including challenging initial assumptions).
- Ask Claude to audit what you already built before starting the next feature.

4) Evaluate early
- Build an evaluation process early, and prioritize it ahead of adding features.
- Consider injecting domain-specific reference data (e.g., a JSON knowledge file) into each run where relevant.

## Examples
See [examples/hackathon-patterns.md](./examples/hackathon-patterns.md).

## Notes
Source: https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon
