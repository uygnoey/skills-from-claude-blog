---
name: request-artifacts
description: Request and iteratively publish shareable Claude Code artifacts (live, interactive pages) built from full session context.
---

## Instructions

Use this skill to turn an in-progress Claude Code session into a live, shareable artifact (an interactive web page) that updates as you work.

When you invoke this skill, follow these steps:

1. Ask what the artifact is for (PR walkthrough, incident investigation, dashboard, release checklist, architecture explainer) and who will read it.
2. Propose a page outline (sections and key visuals) that can be kept up-to-date as new findings arrive.
3. Build and publish the artifact, then republish as the session progresses so the same link stays current.
4. Ensure the artifact references the session context it was built from (codebase, diffs, connector data, and reasoning from the session) and includes links back to relevant code where possible.
5. Keep sensitive details private; artifacts are shareable only within the organization and cannot be made public.

## Examples

- Incident timeline artifact (live updates)
  - Prompt: “Turn this incident into an artifact — timeline, suspect commits, error spike from our monitoring — and republish as I work through it.”

- PR walkthrough artifact
  - Prompt: “Make an artifact walking through this PR — the diff, the reasoning, and what I tested.”

- License audit artifact
  - Prompt: “Build an artifact listing every third-party dependency and its license, flagging anything copyleft.”

See: examples/role-prompts.md
