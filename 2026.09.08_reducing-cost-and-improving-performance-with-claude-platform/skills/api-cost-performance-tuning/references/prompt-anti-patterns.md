# Prompting anti-patterns for frontier models

Instructions accumulate to patch weaknesses of older models. Frontier models follow instructions more
literally, so these waste tokens or degrade results. `/claude-api prompt-audit` scans for them in
application prompts, skills, tool descriptions, CLAUDE.md, and other Claude Code configuration.

| Anti-pattern | Example | Effect on frontier models |
|---|---|---|
| Verification rituals | "double-check your work", "verify twice" | Taken literally: duplicate lookups and tool calls |
| Thoroughness / emphasis boosters | "Be maximally thorough", all-caps mandates | Verbosity, dozens of unneeded searches |
| Mandatory procedures, scratchpad scaffolds | Required step lists, manual scratchpad sections | Stack on native reasoning; can conflict with built-in thinking |
| Stale examples | Long worked reasoning chains | Model imitates unnecessary long reasoning |
| Contradictory rules | Two refund policies that disagree | Followed literally, producing wrong outcomes |
| Dated configuration | Manual thinking budgets | May be rejected by the platform after an upgrade |

## Case study from the source (customer support benchmark, Opus 4.8 -> Opus 5.5)
Six legacy prompts, each with one planted anti-pattern:
- Changing only the model ID cut cost ~18% (lower input and cache-read prices).
- "Verify twice" caused duplicate order lookups; "be maximally thorough" caused dozens of unneeded
  knowledge-base searches.
- The retired thinking setting caused every routing request to be rejected.
- Contradictory refund rules made the model withhold four owed refunds.
- The manual scratchpad conflicted with built-in thinking: on three tickets a tool call was written in
  reasoning but never executed.
- Running prompt-audit cut cost a further ~9% and raised accuracy ~2 percentage points.
