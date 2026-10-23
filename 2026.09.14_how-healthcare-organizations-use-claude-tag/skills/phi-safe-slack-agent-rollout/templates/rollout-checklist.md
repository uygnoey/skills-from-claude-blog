# PHI-safe Claude Tag rollout checklist

## Admin controls
- [ ] Claude Tag is off by default for the workspace
- [ ] Approved channel allowlist: `#________`, `#________`
- [ ] DMs disabled; team uses open threads
- [ ] Connectors scoped per channel (list per channel below)
- [ ] Access bundle includes only: codebase / issue tracker / ________
- [ ] Access bundle excludes: EHR, clinical systems, patient communications
- [ ] Confirmed Claude Tag sees only what the invoking member can see; no private channels with PHI invited

## Data path
- [ ] Workstream is PHI-free (incident response / internal tooling / policy-level knowledge)
- [ ] If production data is needed: separate BAA-covered agent queries it and masks PHI before Slack

## Autonomy per channel
| Channel | Connectors | Autonomy (full / review required / answer-only) | Human reviewer |
|---|---|---|---|
| | | | |

## Pilot
- [ ] Read the healthcare best-practices guide
- [ ] Start: one channel, one or two connectors (e.g. alert channel + GitHub)
- [ ] Two-week pilot start date: ____  review date: ____
- [ ] Decision to widen allowlist recorded
