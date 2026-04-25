**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?

This post announces updated Claude Platform web search and web fetch tools that can automatically run code to dynamically filter retrieved content before it is placed into the model’s context window.

## When is it useful?

Use this when your agent’s web search workflow pulls in lots of irrelevant HTML or long pages, and you want better accuracy and lower token usage—especially for technical documentation lookups or citation verification.

## Key points

- Web search can be token-intensive because agents often fetch full HTML from multiple sites and then reason over large amounts of irrelevant content.
- With dynamic filtering, the web search and web fetch tools can write and execute code to post-process results, keeping only relevant content before loading it into context.
- On BrowseComp, accuracy improved from 33.3% → 46.6% (Sonnet 4.6) and 45.3% → 61.6% (Opus 4.6).
- On DeepsearchQA, F1 improved from 52.6% → 59.4% (Sonnet 4.6) and 69.8% → 77.3% (Opus 4.6).
- Across both benchmarks, dynamic filtering improved performance by an average of 11% while using 24% fewer input tokens.
- Dynamic filtering is enabled by default when using the new tool versions with Sonnet 4.6 and Opus 4.6 on the Claude API.

## Bundled resources

- Skill: a reusable workflow for using web_search + web_fetch effectively and validating results/citations.
- Example API request JSON taken from the post.

## Source

- https://claude.com/blog/improved-web-search-with-dynamic-filtering
