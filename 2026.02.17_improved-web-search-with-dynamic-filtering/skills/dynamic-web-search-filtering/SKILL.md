---
name: dynamic-web-search-filtering
description: Use web_search + web_fetch efficiently by filtering retrieved pages before analysis, focusing only on relevant excerpts and verifying key claims with citations.
---

## Instructions

Use this skill when you need to answer a question that requires searching the web and retrieving pages, but long HTML pages or irrelevant sections would otherwise waste tokens and degrade answer quality.

### Workflow

1. **Plan the search**
   - Restate the user’s question as a small set of concrete sub-questions.
   - Decide what would count as sufficient evidence (exact values, quotes, definitions, etc.).

2. **Search broadly, then narrow**
   - Use `web_search` to collect several candidate sources.
   - Prefer primary sources (official docs, vendor pages, standards bodies) when possible.

3. **Fetch only what you need**
   - Use `web_fetch` on the most promising results.
   - If the fetched page is long, identify the sections likely to contain the answer.

4. **Dynamically filter before reasoning**
   - If the tool supports it, allow the tool to run code to post-process the retrieved content before it is loaded into context.
   - Otherwise, manually extract: headings + the smallest set of paragraphs/tables required to answer.
   - Discard navigation, unrelated sections, repeated footers, and boilerplate.

5. **Answer with verifiable support**
   - Provide the final answer using short quotes or precise figures.
   - Include citations to the fetched URLs.
   - If sources disagree, present both and explain the discrepancy.

### Notes on cost and evaluation

- Web search is token-intensive; filtering reduces irrelevant context.
- Token costs can vary depending on how much code is written to filter context; evaluate against representative queries.

## Examples

### Example 1: API request enabling the newest web tools

See [templates/api-request.json](./templates/api-request.json).

### Example 2: Research task that needs careful filtering

User prompt:

> “Find the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.”

Approach:

- Search for authoritative sources (major exchanges, financial data providers).
- Fetch the pages.
- Filter to the exact price and P/E fields.
- Calculate the comparison and cite the sources.

## References

- Post: https://claude.com/blog/improved-web-search-with-dynamic-filtering
- Benchmarks mentioned: BrowseComp and DeepsearchQA (see post for details)
