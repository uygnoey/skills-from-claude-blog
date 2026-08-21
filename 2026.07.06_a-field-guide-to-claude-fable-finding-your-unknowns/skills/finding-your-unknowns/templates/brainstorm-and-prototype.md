# Template — Brainstorms and prototypes

Use before committing to an approach, especially when you cannot yet tell a good result
from a bad one. The prototype's job is to make your own success criteria visible to you.

## Brainstorm prompt

```
Before we implement <the thing>, brainstorm <3-4> genuinely different approaches. For each
one: what it optimizes for, what it gives up, and what would have to be true about our
codebase or constraints for it to be the right call.

Do not pick a favorite yet. I want to see the space.
```

## Prototype prompt

```
Build quick, throwaway prototypes of approaches <A> and <B>. Keep them minimal — enough
that I can look at the result and react to it, not enough to be production code.

Then tell me: what did building them reveal that we could not have known from the
descriptions alone?
```

## Notes

- If you cannot articulate the criteria you would judge the result by, that is the signal
  to prototype rather than to plan harder. Reacting to two concrete artifacts recovers
  criteria that introspection does not.
- Prototypes are cheap discovery, not wasted implementation. The output that matters is the
  list of things you now know you care about.
- Keep the prototype and feed it into `templates/pitch-and-explainer.md` later — it is the
  most persuasive part of a pitch, because it shows the alternative that was rejected.
