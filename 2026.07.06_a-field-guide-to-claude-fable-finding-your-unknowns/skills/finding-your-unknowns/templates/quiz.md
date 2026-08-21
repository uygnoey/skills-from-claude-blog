# Template — Quizzes

The cheapest way to find out you do not understand your own change is to be asked about it
before someone else is.

## Prompt

```
Give me a HTML report on the changes for me to read and understand with context — not just
the diff, but what each part does and why it is there.

Then quiz me on it: <5-8> questions, hardest last, covering the parts where getting it wrong
would matter. Do not give me the answers until I have tried.
```

## Follow-up

```
Here are my answers: <...>

Grade them. For each one I got wrong or vague, point me at the specific code or note that
would have answered it, and tell me whether the gap is in the code being unclear or in my
understanding.
```

## Notes

- The report and the quiz do different jobs. The report gives you context to read the change;
  the quiz tells you whether the context landed.
- Ask that the answers be withheld. A quiz you read the answers to is a summary, not a check.
- The grading follow-up is the useful half: a question you got wrong because the *code* is
  unclear is a refactor or a comment, not a personal knowledge gap.
- Run this before review, not after. Discovering the gap yourself is free; discovering it in
  review is not.
