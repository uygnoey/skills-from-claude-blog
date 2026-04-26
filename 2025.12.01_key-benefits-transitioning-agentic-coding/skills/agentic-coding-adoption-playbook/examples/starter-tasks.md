# Starter tasks and concrete examples

Reproduced from [What are the key benefits of transitioning to agentic coding for software development?](https://claude.com/blog/key-benefits-transitioning-agentic-coding) (2025-12-01). Use this when running a Claude Code first session.

## The pagination example (verbatim framing)

> When you describe a requirement like "add pagination to the user listing API," an agent doesn't just suggest code snippets. It finds the relevant endpoint, analyzes the current implementation, adds pagination logic following your project's patterns, updates related tests, and ensures the changes integrate properly with your existing database queries.

Use this as the canonical "what an agent actually does" demonstration.

## Recommended starter tasks (verbatim)

> Start with smaller tasks to build confidence: ask Claude Code to add error handling to an API endpoint, refactor a complex component, or write tests for uncovered code. As you experience its capabilities firsthand, you'll naturally expand to more complex operations like cross-cutting refactors and architectural improvements.

Translate that to three concrete prompts:

```
Add error handling to the /checkout endpoint, following the existing error patterns in this codebase
```

```
Refactor the OrderSummary component to remove duplicated state management and align with our Zustand conventions
```

```
Write tests for the cart-merging utility — currently uncovered — and aim for parity with the test style used elsewhere in this module
```

## Mapping benefits to starter tasks

| Benefit | Starter task to demonstrate |
| --- | --- |
| Timeline acceleration | "Add pagination to the user listing API" — show the cross-file edit |
| Onboarding compression | "Explain the structure of this codebase and how the main components interact" |
| Autonomous problem solving | "Diagnose this production error report and propose a fix with test coverage" |
| Scaling capacity | Run several agents in parallel on independent areas; review the diffs |
| Systematic code quality | "Review the authentication module for potential security issues" |
| Democratized access | A frontend engineer asks Claude Code to optimize a slow query (or vice versa) |

## Adoption path the post recommends

1. Install Claude Code in your terminal or IDE.
2. Navigate to your project directory.
3. Run `claude`.
4. Approve every file change before it is written.
5. Start small. Expand to cross-cutting refactors and architectural improvements as confidence grows.

## Source

All quoted material is from [What are the key benefits of transitioning to agentic coding for software development?](https://claude.com/blog/key-benefits-transitioning-agentic-coding) (2025-12-01).
