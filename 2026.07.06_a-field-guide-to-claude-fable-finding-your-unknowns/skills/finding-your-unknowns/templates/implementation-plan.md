# Template — Implementation plan with decision points

A plan that only lists steps hides the places where the work could go two ways. Ask for the
forks explicitly.

## Prompt

```
Write an implementation plan for <the thing>. Structure it so that the decision points are
the headline, not the steps.

For each likely decision point:
- what the choice is
- the options
- what each option costs us later
- your recommendation and why
- whether you need my answer before you start, or can proceed and flag it

Then list the steps under the decisions they depend on.
```

## Review checklist

When the plan comes back, review it this way:

- [ ] Read the decision points first. Do you disagree with any recommendation? That is where
      your unknown knowns live.
- [ ] Is anything listed as a step that is actually a decision in disguise?
- [ ] Is any decision point one you cannot answer? Send it back through
      `templates/interview.md` or `templates/blind-spot-pass.md`.
- [ ] Are the decisions that need your answer up front actually blocking, or can work start?

## Notes

- Reviewing steps tells you whether the work will be done. Reviewing decision points tells
  you whether it will be done *right*, which is the only part a plan can still change
  cheaply.
- A plan with no decision points on a non-trivial task means the ambiguity was resolved
  silently. Ask what was assumed.
