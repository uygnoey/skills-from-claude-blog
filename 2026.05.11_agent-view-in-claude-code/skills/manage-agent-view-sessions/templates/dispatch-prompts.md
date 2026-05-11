# Dispatch prompt templates for agent view

Use these as starting points when dispatching sessions in agent view or from the shell.

## Minimal background session

```bash
claude --bg "<task prompt>"
```

## Background session using a specific custom subagent

```bash
claude --agent <agent-name> --bg "<task prompt>"
```

## Handoff from inside an interactive session

```text
/bg <one more instruction before detaching>
```

## Agent view filters (type in the dispatch input)

- `a:<name>`
- `s:<state>`
- `#<number>` (or paste a PR URL)
