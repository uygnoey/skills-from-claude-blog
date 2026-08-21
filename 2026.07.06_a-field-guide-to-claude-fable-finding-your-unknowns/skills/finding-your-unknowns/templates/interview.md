# Template — Interview

The highest-yield move for *unknown knowns*: things you know so well you never think to say.

## Prompt

```
Interview me one question at a time about anything ambiguous, prioritize questions where my
answer would change the architecture.
```

## Extended form

```
Before you write any code, interview me. Rules:
- One question at a time. Wait for my answer before the next one.
- Prioritize questions where my answer would change the architecture over questions about
  naming or style.
- If my answer implies something you did not expect, follow it rather than moving to your
  next planned question.
- Stop when the remaining questions would not change what you build, and tell me you are
  stopping.
```

## Notes

- **One question at a time is the whole technique.** A list of twenty questions gets skimmed
  and answered in a paragraph. A single question gets an actual answer, and the answer
  redirects the next question.
- The architecture-priority instruction is what keeps the interview from drifting into
  preference questions. You are trying to prevent rework, not settle formatting.
- Run this after a blind spot pass so the interview covers the gaps you just discovered as
  well as the ones you came in with.
- Interview answers are worth pasting into the plan or a context file — they are exactly the
  *unknown knowns* that were missing from the map.
