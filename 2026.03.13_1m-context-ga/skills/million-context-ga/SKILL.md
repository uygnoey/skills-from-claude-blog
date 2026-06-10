---
name: million-context-ga
description: Guidance for using Claude models with a generally available 1M-token context window (Opus 4.6 and Sonnet 4.6), including practical considerations for very large inputs.
---

## Instructions
Use this skill when you want to:
- Decide whether 1M context materially changes your workflow for a task.
- Plan how to structure a single request that includes extremely large inputs (text and media).

Follow these guidelines:
1. Confirm the target model and availability
   - The 1M context window is generally available for Claude Opus 4.6 and Claude Sonnet 4.6.
   - Requests over 200K tokens no longer require a beta header (if a beta header is present, it is ignored).

2. Use the full window to reduce loss from summarization/compaction
   - Prefer including primary source material directly (large diffs, full traces, long documents) when fidelity matters.
   - If you previously relied on lossy summarization or clearing context due to window limits, re-evaluate whether you can keep more of the original material.

3. Plan for large media bundles
   - Up to 600 images or PDF pages can be included per request.
   - When sharing many pages/images, provide a short “reading map” that tells Claude what to prioritize (sections, page ranges, or questions).

4. Keep operational expectations explicit
   - State the deliverable format (e.g., “risk register table”, “issue list with file:line anchors”, “executive summary + appendix”).
   - State what counts as evidence (citations to page numbers, quoted snippets, or document section headings).

## Examples
### Example 1: Analyze a large contract pack
User: I’m uploading 400 pages of contracts. Identify (1) termination clauses, (2) renewal terms, and (3) any unusual liability carve-outs. Cite page numbers.

Assistant: I will scan for termination, renewal, and liability sections; extract verbatim clause snippets; and return a table with document name, page, clause title, and risk notes.

### Example 2: Debug across a huge diff
User: Here’s a large diff across multiple services. Find any changes that could break backward compatibility and list the affected endpoints.

Assistant: I will review API surface changes, identify breaking changes, map them to endpoints/clients, and return a prioritized list with file paths and rationale.

## Source
- https://claude.com/blog/1m-context-ga
