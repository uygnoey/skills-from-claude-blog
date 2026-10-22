# Manual review checkpoint audit

Audit each human review step periodically in production. If the catch rate is low and the cost is high,
the checkpoint can be automated, sampled, or removed.

| Checkpoint | Output type | Current tier | What does it actually catch? | How often does a reviewer change the output? | Cost per review | Justification | Action (keep / sample / automate / remove) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Authority to remove or automate checkpoints: ____________

## Incident response (answer before go-live)
- Who gets notified? ____________
- What is the remediation path? ____________
- Who has authority to pause the system? ____________
- Who communicates to affected parties? ____________

## Continuous monitoring
| Signal | Source of degradation (model update / prompt drift / stale data / process change) | Threshold | Alert | Escalation |
|---|---|---|---|---|
| | | | | |

## Error modes before scaling
| Error mode | Share of failures at current volume | Cost per occurrence at full volume | Safe to automate? |
|---|---|---|---|
| | | | |
