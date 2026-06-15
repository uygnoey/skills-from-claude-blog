# Hackathon patterns (examples)

These examples paraphrase patterns described by hackathon winners in the source post.

## Example 1: Split into multiple Claude Code sessions (clean contexts)
- Create distinct sessions for major components (e.g., voice engine, content generation, 3D layer, core app).
- Keep each session focused so context stays relevant.

## Example 2: Multi-agent debugging with one agent per domain
- Assign one agent to schematic ingestion, one to diagnostics, one to UI, etc.
- During debugging, run multiple agents in parallel and benchmark progress at each step.

## Example 3: Eval-first workflow
- Build an auditable evaluation against real cases.
- Use evaluation results to decide what to build next.

Source: https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon
