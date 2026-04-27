# Prompt structure patterns for caching

These layouts illustrate the prefix/suffix split implied by the launch post. They are conceptual templates, not API code samples — the post itself does not include client code, so do not copy these as if they were verbatim from the source.

## Pattern 1 — Talk-to-book chatbot

Prefix (cache this once):

```
[System]
You are a reading companion for the book below. Answer only from the book text. Cite chapter or section when possible.

[Book]
<full book text, ~100,000 tokens>
```

Dynamic suffix (changes per call):

```
[Recent turns]
<last few user/assistant turns, optional>

[User]
<the new question>
```

Why this matches the post: the 100,000-token chat-with-book row in the benchmark table is the closest analogue, with time-to-first-token dropping from 11.5s to 2.4s and cost dropping 90%.

## Pattern 2 — Many-shot classifier

Prefix (cache this once):

```
[System]
You classify support tickets into one of: billing, bug, feature_request, account, other.

[Examples]
<dozens of labeled ticket → label pairs, ~10,000 tokens>
```

Dynamic suffix (changes per call):

```
[New ticket]
<ticket text>
```

Why this matches the post: the many-shot 10,000-token row in the benchmark table reports a 31% latency drop and 86% cost drop. Detailed instruction sets with "dozens of high-quality examples" are explicitly called out in the use-case list.

## Pattern 3 — Long-context coding assistant

Prefix (cache this once):

```
[System]
You are a coding assistant for this repository. Follow our review rules.

[Codebase summary]
<summarized version of the codebase>

[Review rules]
<persistent style and review guidelines>
```

Dynamic suffix (changes per call):

```
[Conversation so far]
<recent turns, optional>

[User]
<the new request or pasted snippet>
```

Why this matches the post: the 10-turn long-system-prompt row in the benchmark table reports about 75% latency reduction and 53% cost reduction. The post specifically lists "improve autocomplete and codebase Q&A by keeping a summarized version of the codebase in the prompt" as a coding-assistant use case.

## Source

Prompt caching with Claude — Anthropic, August 14, 2025: <https://www.anthropic.com/news/prompt-caching>
