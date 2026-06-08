---
name: foundation-models-handoff
description: Use Apple Foundation Models for fast on-device tasks, then hand off to Claude for multi-step reasoning, code generation, web search, or code execution—while keeping a single, continuous user experience.
---

# Foundation Models → Claude handoff

## Instructions
You help an Apple-platform developer design a two-stage workflow that uses Apple’s Foundation Models framework for simple, on-device work and escalates to Claude for more complex requests.

### 1) Decide what stays on-device vs. what is handed off
Use on-device Foundation Models when the task is primarily:
- summarization
- extraction

Hand off to Claude when the request calls for:
- multi-step reasoning
- code generation
- web search for current information
- executing code for data analysis

### 2) Use typed outputs as the boundary between stages
When the on-device stage returns typed Swift values (e.g., via guided generation / `@Generable`), treat those values as the structured input to the Claude request.

### 3) Preserve “one experience” in the UI
Plan for Claude output to be streamed back into the same view that initiated the request.

### 4) Document the intent clearly
When you propose the handoff design, include:
- What the on-device stage does
- What triggers escalation to Claude
- What structured inputs are passed to Claude
- How the UI presents the two stages as one flow

## Examples
### Example: Journaling app prompt → long-term pattern discovery
- On-device: generate a daily journaling prompt.
- Hand off to Claude: find threads across months of entries.

### Example: Study app definition → deep follow-up
- On-device: define a term at the student’s level.
- Hand off to Claude: handle a follow-up like “why does this matter for everything else we’ve covered?”

## References
- Post: https://claude.com/blog/claude-for-foundation-models
