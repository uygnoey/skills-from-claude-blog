# Reconcile claims to a single source of truth

## Prompt
You are my finance integrity reviewer.

Goal: Validate that every number and claim in the attached narrative reconciles to a single source of truth.

Inputs:
- Narrative: <attach deck/doc>
- Source of truth: <attach model tables / approved exports>

Instructions:
1) Extract every quantitative claim (numbers, percentages, deltas, ranges) and any factual assertions that depend on those numbers.
2) For each item, point to the exact location in the source of truth (tab/section/table/row/column) that supports it.
3) Flag anything that does not reconcile, is ambiguous, or mixes time periods/definitions.
4) Suggest corrected wording (or corrected numbers) and explain what changed.
5) Output a checklist with three sections: ✅ Reconciles, ⚠️ Needs clarification, ❌ Does not reconcile.

## Notes
- If the narrative uses internally defined metrics, ask for definitions rather than guessing.

## Source
https://claude.com/blog/how-anthropics-finance-team-uses-claude-to-shape-the-narrative-behind-the-numbers
