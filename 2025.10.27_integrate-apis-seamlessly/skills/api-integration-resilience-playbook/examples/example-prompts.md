# Example prompts (verbatim from the post)

The original post lists concrete prompts at each stage of the workflow. Reproduced here exactly as published so you can copy/paste them.

## Claude.ai — debugging questions

- "Here's a Stripe webhook signature error. What validation steps am I missing?"
- "Why might OAuth tokens expire during multi-step checkout flows?"
- "Compare webhook vs polling for real-time inventory updates"

## Claude.ai — failure-mode discovery

- "What could break with this payment API during high traffic? Include rate limiting and timeout scenarios."

## Claude.ai — specification triage

> Use the web search feature or paste API documentation into Claude. Ask for "integration risks ranked by likelihood."

Example refined output the post highlights: instead of "implement error handling," your team gets "add exponential backoff for 429 responses with jitter to prevent thundering herd."

## Claude Code — install and launch

```
npm install -g @anthropic-ai/claude-code
```

```
claude
```

## Claude Code — auth implementation prompts

- "Build OAuth2 flow for Google Calendar with automatic token refresh"
- "Create rotating API key system for Twilio with monitoring"
- "Implement JWT validation for microservices"

## Claude Code — validation prompts

- "Create tests that reproduce this rate limit scenario"
- "Generate contract tests for schema validation"
- "Run tests for authentication refresh during long operations"

## Claude Code — ship command

```
> Commit these API changes and open a PR
```

## Source

All prompts above are quoted verbatim from [How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (2025-10-27).
