# Prompt cache checklist

Based on the source article. Prefill (turning a prompt into internal working state) is the expensive part
of input handling; prompt caching stores that state (the KV cache) and bills reads at a fraction of the
normal input price.

## Constraints
- The cache is pinned to a specific model.
- Reads require a byte-exact match across the prompt prefix.
- TTL is limited: 5 minutes by default.
- A cache rewrite costs 1.25x the normal input price (2x for a 1-hour cache).

## Things that break the cache
| Cause | Why | Fix |
|---|---|---|
| Changing effort/thinking mid-conversation | Part of the cached prefix | Keep stable; change only when the cache is already broken (e.g. compaction). Opus 5 and Fable 5.1 allow mid-conversation effort updates without breaking the cache |
| Timestamps, IDs in the prefix | Prefix no longer byte-exact | Move volatile values after the cached content |
| Tool definitions that reorder | Tools render at the top of the prompt | Deterministic ordering; `defer_loading` for rarely used tools |
| Editing the system prompt mid-conversation | Changes the prefix | Apply updates as messages |
| Forked conversations / subagents | Shared only if byte-identical prefix, same model, same effort | Fork with identical prefix and settings |
| Synchronous tools or subagents that outlive the TTL | Cache expires, rewrite is billed | 1-hour TTL on the prefix for long waits |

## Positive practices
- [ ] Monitor hit rates in Claude Console cache diagnostics; use the cache diagnostics API to find where two requests diverged.
- [ ] Order requests: tools, system prompt, then conversation.
- [ ] Move the cache breakpoint as the conversation grows, or use automatic caching on the last cacheable block.
- [ ] Pre-warm at session start: a request with `max_tokens: 0` and an explicit cache breakpoint.
- [ ] Switch model/effort only at points where a miss is already being paid.
