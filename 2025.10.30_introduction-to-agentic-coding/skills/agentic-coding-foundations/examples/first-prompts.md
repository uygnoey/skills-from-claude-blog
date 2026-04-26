# First prompts and the Rakuten case study

Material reproduced from [Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (2025-10-30). Use this when running an onboarding session.

## Three onboarding prompts (verbatim)

Run each from inside `claude` in a real project directory.

```
Explain the structure of this codebase and how the main components interact
```

> Claude Code reads your files and provides an architectural overview, helping you or new team members understand project organization.

```
Review the authentication module for potential security issues
```

> Claude Code examines the relevant code, identifies concerns like exposed credentials or insufficient validation, and suggests specific improvements.

```
Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching
```

> Claude Code analyzes your entire codebase, identifies specific ORM patterns causing N+1 problems, and implements a fix.

## Rakuten case study (summary)

The post's headline real-world example.

- **Codebase**: vLLM, an open-source library spanning 12.5 million lines of code in Python, C++, and CUDA.
- **Task**: implement a specific activation-vector extraction method.
- **Outcome**: Claude Code completed the implementation in a single seven-hour autonomous session.
- **Quality**: 99.9% numerical accuracy compared to the reference method.

### Quotes from the post

> "I didn't write any code during those seven hours, I just provided occasional guidance"
>
> — Kenta Naruse, Machine Learning Engineer at Rakuten

> "You can have five tasks running in parallel by delegating four to Claude Code while focusing on the remaining one."
>
> — Yusuke Kaji, General Manager of AI for Business at Rakuten

### Rakuten transformation metrics

- 79% faster feature delivery (24 days → 5 days).
- 7-hour autonomous implementations with minimal human intervention.
- 99.9% accuracy on complex algorithmic refactoring.
- 5x parallel task execution capacity for engineering teams.

## Quick-win categories to expand into

- Test automation for uncovered code paths.
- Documentation generation for legacy systems.
- Routine refactoring of technical debt.
- Feature implementation for well-understood requirements.

## Source

All quotes and metrics above are reproduced from [Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (2025-10-30).
