# Template — Pitches and explainers

People who were not in the loop cannot review a diff. They can review the story of why the
change looks like this.

## Prompt

```
Package the prototype, the spec, and the implementation notes into a single doc I can drop
in Slack.

Audience: <who — e.g. "the two other engineers on this service plus my manager, who is
non-technical">.

It should answer, in this order:
1. What problem this solves and who felt it
2. What we considered and rejected, and why (use the prototypes)
3. What we built
4. Where it deviates from the original plan and what forced that (use the implementation
   notes)
5. What I need from the reader — approval, review, or just awareness

Keep it short enough to read in one sitting.
```

## Notes

- Naming the audience changes the doc more than any other instruction. "Two engineers plus a
  non-technical manager" produces something different from "the platform team."
- Section 2 is what buys agreement. Showing the rejected prototype is more convincing than
  arguing for the chosen one.
- Section 4 is where the implementation notes earn their keep. Deviations look like sloppiness
  when unexplained and like diligence when explained.
- End with an explicit ask. A doc that does not say what it wants gets read and forgotten.
