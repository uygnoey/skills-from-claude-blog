**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post announces the Web Search tool for the Anthropic Messages API, which lets Claude run web searches and return answers with citations.

## When is it useful?
Use it when your application needs up-to-date, verifiable information beyond the model’s training cutoff (e.g., market/regulatory updates, latest docs, current events).

## Key points
- Enable the web search tool on a Messages API request.
- Claude decides when web search is helpful, generates targeted queries, and may run multiple searches (controlled by max_uses).
- Responses include citations to the retrieved sources.
- Admins can manage usage with domain allow/block lists at the org level.
- The post also notes a Web Fetch capability for fetching and analyzing a specific URL (update section).

## Bundled resources
Skill: api-web-search-with-citations. Guide: web-search-and-fetch.

## Source
https://claude.com/blog/web-search-api
