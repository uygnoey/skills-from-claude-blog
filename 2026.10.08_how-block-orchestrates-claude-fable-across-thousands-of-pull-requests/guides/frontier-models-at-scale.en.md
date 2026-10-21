**English** · [한국어](./frontier-models-at-scale.ko.md) · [Español](./frontier-models-at-scale.es.md) · [日本語](./frontier-models-at-scale.ja.md)

# Operating frontier models efficiently and safely at scale

Lessons from Block's AI Capabilities team on giving a whole engineering organization frontier models
without losing control of cost or risk.

## 1. Access and efficiency
- Give anyone in a technical role full access to the most capable models, so teams keep working at
  the edge of what is possible.
- Make efficiency the default: build tooling (Block's auto-selector) that suggests the right model for
  a task, and use multi-agent systems that mix larger and smaller models.
- Reserve the frontier model for big problems (migration design, large-scale orchestration); let
  smaller models fill in code-change details.

## 2. Benchmark a grid, not a slider
- A model at xhigh effort can behave like a different model than the same model at medium.
- For every use case, benchmark every model at every effort level.
- Publish plain recommendations ("use this model on high as the default for this kind of task"),
  automate them in tools, and let experts explore beyond them.

## 3. Tools for many agents
- Single-conversation interfaces don't keep up with dozens of agents working at once. Block uses Buzz,
  an open-source workspace where multiple people and many agents work in shared channels and threads.

## 4. Safeguards in layers
| Layer | What Block does |
|---|---|
| Human guarantees | Merges to main, production deploys, and feature-flag changes stay with people; agent changes pass security checks, then two humans approve the deploy |
| Secure by default | Remote workstations; network allow list instead of a deny list |
| Outside the model loop | Cheap checks built into work interfaces — regexes, increasingly small classifiers |
| Deliberately allowed | Opening PRs, code review, querying logs and analytical databases |
| Model safeguards | Model refusal behavior plus Anthropic's safety classifiers; Block benchmarks that Claude refuses to "hack around" dual approval |

## 5. Keep up with maintenance
More PRs mean faster tech-debt growth. Run agents that make daily or weekly passes over the codebase
to find what to clean up and consolidate.

## 6. Make knowledge organizational
People accumulate local skills and context (e.g. skills that let a non-front-end engineer work in a
web front end). Document what people learn and put it in a shared system so every agent run has the
best available context.

## Source
- https://claude.com/resources/articles/how-block-orchestrates-claude-fable-across-thousands-of-pull-requests
