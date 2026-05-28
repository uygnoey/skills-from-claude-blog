# Planning Layer Prompt (Collaborative PRD)

## Purpose
Run this prompt *before* any code generation to produce a structured plan the team can review.

## Questions to answer
1. What outcome are you actually trying to create, and how do you measure?
2. What assumptions are still implicit?
3. What workflows or edge cases are easy to forget?
4. How will you know the output matches intent before rollout?

## Output format
Return a “Collaborative PRD” with:
- Problem statement
- Goals / non-goals
- Success metrics
- Assumptions & unknowns
- User workflows
- Edge cases
- Constraints
- Implementation approach (high level)
- Validation plan (how to verify before rollout)
