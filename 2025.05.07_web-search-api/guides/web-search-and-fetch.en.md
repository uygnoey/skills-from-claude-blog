**English** · [한국어](./web-search-and-fetch.ko.md) · [Español](./web-search-and-fetch.es.md) · [日本語](./web-search-and-fetch.ja.md)

## Overview
This guide summarizes how to think about enabling web search (and the related web fetch capability mentioned as an update) when building with Claude.

## Decision: search vs fetch
- Use **web search** when you need discovery across sources and want citations.
- Use **web fetch** when you already have a URL and want Claude to read and analyze it.

## Operational considerations
- Plan for variable latency due to external requests.
- Validate that citations support key claims.
- If your org uses allow/block lists, test behavior on permitted and denied domains.

## Source
https://claude.com/blog/web-search-api
