# Template — Implementation notes

The territory reveals unknowns while the work is happening. Capture them at the moment they
appear, not at review time.

## Prompt

```
Keep an implementation-notes.md file as you work. If you hit an edge case that forces you to
deviate from the plan, write down:
- what you hit
- what the plan said to do
- what you did instead
- why
- what I should double-check as a result

Keep it terse. It is a working file, not documentation. Update it as you go, not at the end.
```

## Suggested file shape

```markdown
# Implementation notes — <task>

## Deviations

### <short title of the edge case>
- **Hit:** <what the code/API/data actually did>
- **Plan said:** <the planned approach>
- **Did instead:** <the actual approach>
- **Why:** <the constraint that forced it>
- **Check:** <what a reviewer should verify>

## Open questions
- <things that were assumed and should be confirmed>
```

## Notes

- This file is temporary. Its value is in the handoff, not in being kept forever — it feeds
  `templates/pitch-and-explainer.md` and `templates/quiz.md`, and then it can be deleted.
- "Why" is the field that matters. A reviewer looking at retry logic that does not match the
  plan needs the reason (an upstream API returns 200 with an error body), not the diff.
- Open questions are where unknown unknowns get parked before they become bugs.
