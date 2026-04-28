---
name: api-web-search-with-citations
description: Reusable implementation notes derived from the Claude blog post “Introducing web search on the Anthropic API”.
---

## Instructions

- Read the source post first: https://claude.com/blog/web-search-api
- Do not invent APIs, parameters, or pricing beyond what the post states.
- If the post describes multiple capabilities (e.g., web search vs URL fetch), keep them separate and label them clearly.

### What to produce

- A short implementation checklist.
- A risk/controls checklist if the post mentions admin or policy controls.
- A minimal example request/response outline **only if** the post includes concrete examples (otherwise point back to the source).

## Examples

### Example: Converting the post into an engineering checklist

- Summarize the capability.
- Identify when it should be enabled.
- List operational controls and costs (if present in the source).
- Add a test plan (latency, correctness, citation coverage).

