# Template — Cost-per-outcome review

A worksheet for one workload. Fill it in before changing a model setting, not after the invoice
arrives.

## 1. The outcome

- **What does this workload produce?** (Not "it calls the API 40,000 times a day" — what comes
  out the other end that someone uses.)
- **Who consumes it, and what do they do differently because it exists?**

## 2. The counterfactual

> What would this work have cost without AI, considering resources, time, or whether the project
> would have been attempted at all?

- **Resources:** how many people, at what level, for how long?
- **Time:** what was the turnaround before, and what is it now?
- **Would it have happened at all?** If the honest answer is no, say so. Work that would never
  have been attempted has no baseline — the comparison is against zero output, not against a
  cheaper process.

## 3. The kind of work

> Is the model handling tasks requiring judgment and reasoning, or processing high-volume
> straightforward work?

- **Judgment and reasoning:** weighing options, resolving ambiguity, deciding what matters.
- **High-volume straightforward:** extraction, classification, formatting, routing.
- **Mixed?** Then it is a pipeline, and the steps should not all be on the same setting. List
  the steps and mark each one.

| Step | Judgment or volume? | Model | Effort |
|---|---|---|---|
| | | | |

## 4. The current placement

- **Model in use today:**
- **Does it match the kind of work above?**
- If the model is *smaller* than the work: are you seeing retries, low-quality outputs, or human
  correction time? Those are the real cost, and they do not appear on the token bill.
- If the model is *larger* than the work: what capability is being paid for and not used?

## 5. The levers not yet applied

- [ ] Could non-urgent portions run in **batch** at half price?
- [ ] Is there a large stable prefix that could be **cached**?
- [ ] Are mechanical steps running at higher **effort** than they need?
- [ ] Could most steps run on a smaller model with a **frontier model consulted only at the
      decision points**?

## 6. Decision

- **Change:**
- **Expected effect on cost-per-outcome (not cost-per-token):**
- **What you will watch to confirm it:** (see the usage analytics and Analytics Chat questions in
  `examples/usage-questions.md`)
