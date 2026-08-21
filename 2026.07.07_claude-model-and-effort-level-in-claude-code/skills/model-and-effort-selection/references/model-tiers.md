# Fable vs. Opus vs. Sonnet: the specialist, the expert, and the generalist

One way to think about how the two settings relate:

- **Fable** is a specialist who's seen problems almost no one else has.
- **Opus** is the expert.
- **Sonnet** is a really good generalist.

**The effort level decides how much time any of them spends on your task.**

## Opus at low effort

Like getting five minutes with an expert who has deep experience with problems like yours. They
bring knowledge that isn't anywhere in your codebase: patterns they've seen before, gotchas they
know to check for, the kind of thing you only get from having solved a lot of similar problems.

But five minutes means a quick read of your code, not a careful one.

## Sonnet at high effort

Like giving a really good generalist the whole afternoon. They'll read everything, run things,
double-check their work, and end up understanding your specific code thoroughly.

What they bring less of is that "I've seen exactly this before" recognition.

## Fable, even at low effort

That specialist glancing at the problem everyone else is stuck on and still spotting the thing no
one else would. **That recognition is what you're paying the most for**, so it's worth saving for
the tasks that genuinely need it.

## The takeaway

None of these is universally better.

> The model setting is roughly **how capable**; the effort setting is roughly **how thorough**.
> Most real tasks need some of both.

## Where each model fits

| Work | Pick |
|---|---|
| Subtle bugs, unfamiliar domains, architecture decisions | Larger model |
| Ambiguous requests where the shape of the answer isn't fixed | Larger model — smaller models do better with specific instructions directing execution |
| The smaller model is confidently wrong no matter how much context you give it | Larger model |
| Edits you can describe precisely, mechanical changes, questions about code already in context | Smaller model |
| A routine stretch while you're on the larger model | Drop down — more speed, typically less cost, no quality hit |
| Long, multi-step work nothing else finishes | Fable — in Anthropic's testing it finished jobs Opus and Sonnet can't reach at any effort level |

## A note on newer model generations

Following the launch of Claude Opus 4.8: in Anthropic's testing, using the **default** effort
setting for Opus 4.8 produced better results for about the same number of tokens compared with
using the default effort setting of Opus 4.7 on the same task.

## Source

["Choosing a Claude model and effort level in Claude Code"](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)
