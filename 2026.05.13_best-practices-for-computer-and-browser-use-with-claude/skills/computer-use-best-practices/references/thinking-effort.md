# Thinking effort recommendations (computer use)

Source: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude

## Claude Opus 4.7
- Default for most computer use: `high`
- High-throughput / cost-sensitive: `low`
- Complex, one-shot tasks: `max` (the post notes this is not recommended for computer use generally)

## Claude 4.6 family
- Default for most computer use: `medium`
- High-throughput / cost-sensitive: `low`
- Simple, well-defined workflows where latency is priority: thinking disabled
- Complex, one-shot tasks: `high`

## Notes
- More thinking typically increases output tokens, latency, and cost.
- The post states Opus 4.7 on `high` uses roughly half the output tokens of `max`, and 4.6 on `medium` uses roughly half the output tokens of `high`.
