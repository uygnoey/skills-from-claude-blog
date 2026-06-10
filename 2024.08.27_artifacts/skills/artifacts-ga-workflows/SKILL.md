---
name: artifacts-ga-workflows
description: Workflow patterns for using Claude Artifacts (GA) to iteratively build and share code, documents, and visualizations across Free/Pro/Team and mobile.
---

## Instructions
Use this skill when you want to work with Claude in an “artifact-first” way: keep a concrete output (code, doc, visualization) in a dedicated workspace while iterating through conversation.

Apply these patterns:
1. Choose the right artifact type for the job
   - Code for scripts, small apps, or interactive prototypes.
   - Documents for specs, briefs, and structured write-ups.
   - Visualizations for diagrams, charts, dashboards, or SVG.

2. Iterate in tight loops
   - Ask Claude to propose an initial artifact quickly.
   - Review the artifact directly, then request focused edits (specific sections, components, or behaviors).

3. Use publishing and remixing intentionally
   - On Free/Pro, publish artifacts you want to share publicly and remix others’ artifacts for a starting point.
   - Treat remixes as forks: state what you are changing and why.

4. Collaborate via Projects (Team)
   - Share artifacts in Projects when you need team review, shared context, and secure collaboration.

## Examples
### Example 1: Prototype an interactive dashboard
User: Make an interactive dashboard mock for campaign performance. Include CTR, spend, and conversions with a simple filter.

Assistant: I’ll create an artifact with a basic dashboard layout, sample data, and a filter UI; then we can iterate on metrics and styling.

### Example 2: Turn a conversation into a reusable diagram
User: Convert this architecture description into a flowchart diagram we can share.

Assistant: I’ll generate a flowchart visualization artifact and refine the nodes/edges based on your feedback.

## Source
- https://claude.com/blog/artifacts
