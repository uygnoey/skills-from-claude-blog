# Task-completion eval plan

## Structure
- [ ] One shared end-to-end set, owned by the central team
- [ ] Small eval set shipped with each skill by its owner team (DRI: ______)
- [ ] At least 10 golden examples to start

## Coverage before every change
- [ ] A task for every chain of agents that runs together in production
- [ ] A task for every rule the agent must not break
- [ ] Each task run more than once (some breaks show up in only one run of two)

## Grading
- [ ] Final message graded against a rubric (answer quality)
- [ ] While an orchestrator exists: routing accuracy (right subagent?)
- [ ] After folding: right skill loaded / right tool called?
- [ ] Move toward task-completion grading over time (matters most when comparing architectures)

## Hard-to-replay environments
- [ ] Record timestamps on important events so they can be replayed later as targeted evals

## Golden examples
| # | User request | Expected outcome | Must-not-break rule | Agent chain exercised |
|---|---|---|---|---|
| 1 | | | | |
