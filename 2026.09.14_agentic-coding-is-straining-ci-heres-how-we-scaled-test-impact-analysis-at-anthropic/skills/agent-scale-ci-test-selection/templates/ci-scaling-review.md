# CI service scaling review — <service name>

Checklist built from the lessons in the post. Answer each before choosing another patch.

## Load
- [ ] Current CI jobs/day and growth over the last six months:
- [ ] Could the design absorb 25x this load within two quarters?
- [ ] Was v0 sized for 10-20x perceived scale? If not, why (budget)?
- [ ] Effects of agent PR shape accounted for (smaller PRs, overnight/weekend floor, human-driven bursts)?

## State and topology
- [ ] Is state held inside the process? Can it move to an external/in-memory store?
- [ ] Is any critical component a single instance? Can we measure it and canary its changes?
- [ ] Can workers be stateless (append to a journal, roll up separately)?

## Instrumentation (Claude's eyes and ears)
- [ ] Jobs in == jobs out is measured and alerted on.
- [ ] Listener/consumer lag is measured; alert threshold set.
- [ ] An agent session (e.g. long-running) can read these signals and keep history of past fixes.

## Patch history
| Patch | Date | Time it bought |
|---|---|---|
|  |  |  |

- [ ] Is each patch buying less time than the last? If yes, plan the redesign now.
