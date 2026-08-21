# Template — Blind spot pass

Run this before writing a plan. The point is not to get answers; it is to get a list of
questions you did not have.

## Prompt

```
I'm working on <what you are about to do> but I know <how much you actually know> about
<the relevant area> in this codebase.

Can you do a blind spot pass — what are the unknown unknowns here? What would someone who
has worked in this area for years know that I would not even think to ask about?

My level: <e.g. "I'm senior in this codebase but have never touched auth", or "I've never
worked on video encoding at all">.

Read the relevant code first, then give me the list grouped by how badly getting it wrong
would hurt.
```

## Worked example

```
I'm working on adding a new auth provider but I know nothing about the auth modules in
this codebase. Can you do a blind spot pass — what are the unknown unknowns here, the
things I would not even know to ask about?
```

## Notes

- **State your expertise level explicitly.** Without it the answer is pitched at an average
  reader and is either patronizing or over your head. With it, the list is calibrated.
- Ask it to read the code first. A blind spot pass done from the prompt alone only finds
  generic blind spots; one done from the codebase finds yours.
- Ranking by blast radius matters more than completeness. You will not chase every item —
  you want to know which three would have cost you a week.
- Feed the surviving questions into `templates/interview.md` rather than answering them all
  in one go.
