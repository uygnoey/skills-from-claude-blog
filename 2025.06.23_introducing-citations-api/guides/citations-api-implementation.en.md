**English** · [한국어](./citations-api-implementation.ko.md) · [Español](./citations-api-implementation.es.md) · [日本語](./citations-api-implementation.ja.md)

# Citations API implementation checklist

## Build
- Decide tasks (summarization, Q&A, support) and what must be cited.
- Supply source documents (PDF or text) and choose chunking strategy.
- Design citation display (inline markers, footnotes, jump-to-source).

## Evaluate
- Measure citation recall and precision.
- Track “not found in sources” rate for unsupported questions.

## Source
- https://claude.com/blog/introducing-citations-api
