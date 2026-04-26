---
name: citations-grounded-answers
description: Build and evaluate “grounded answers” experiences using Anthropic API Citations so users can trace each claim back to source passages.
---

## Instructions
Use this skill to design an application workflow that answers questions or summarizes documents with verifiable citations.

1) Define the job and citation expectations
- What tasks: summarization, complex Q&A, customer support?
- What needs a citation: every bullet, every paragraph, or only factual claims?

2) Prepare sources
- Collect PDFs and/or plain text relevant to the user request.
- Decide whether to rely on the platform’s sentence chunking or provide your own pre-chunked text.

3) Prompt for grounded outputs
- Ask for concise answers and require citations alongside claims.
- Instruct the model to avoid unsupported claims and to say “not found in sources” when needed.

4) UX: make citations legible
- Choose how to display citations (inline markers, footnotes, expandable source snippets).
- Let users jump to the cited passage.

5) Evaluate and iterate
- Sample real user queries.
- Check recall (are key claims cited) and precision (are citations relevant).
- Track failure modes: missing citations, irrelevant citations, over-quoting.

## Examples
See examples in:
- examples/grounded-qa.md

## Source
- https://claude.com/blog/introducing-citations-api
