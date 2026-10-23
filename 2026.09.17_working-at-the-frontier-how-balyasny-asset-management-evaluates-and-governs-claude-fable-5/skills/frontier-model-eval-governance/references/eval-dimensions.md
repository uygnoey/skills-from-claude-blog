# Evaluation dimensions (from the BAM post)

## Task set
- Thousands of real domain tasks with **verifiable outcomes** (BAM: equities, macro, commodities).
- Not general benchmarks, not isolated demos.
- Tag each task by area so results can be broken down and used for routing.

## Test conditions
| Condition | Purpose |
|---|---|
| Model alone | Raw capability |
| Inside the agent harness (same tools, files, requirements as users) | Real-world behavior |

## Capabilities assessed
- Planning
- Tool selection and use
- Finding and analyzing evidence
- Recovering from errors
- Checking intermediate results
- Producing grounded deliverables

## Failure modes checked
- Numerical errors
- Missed coverage
- Unsupported conclusions
- Retrieval problems

## Validating a surprising result
1. Assume it may be an evaluation flaw.
2. Re-run the evaluation.
3. Independently check the task and the scoring logic.
4. Review with the model provider.
5. Only then accept the improvement.

## Reported result
- Relevant subset: Claude Fable 5 89.4% vs prior production model 86.1%.
- Largest gains: complex planning, analysis, agentic execution.
- Per-category task counts and a detailed scoring breakdown are not published (see original).
