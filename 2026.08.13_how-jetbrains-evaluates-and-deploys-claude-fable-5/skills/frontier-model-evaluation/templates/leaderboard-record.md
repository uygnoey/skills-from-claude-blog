# Model evaluation round — record template

Copy this file per evaluation round (one round = one new model release run against the
standing private eval set). Fill in every field; leave `n/a` rather than deleting a row,
so rounds stay comparable over time.

---

## Round metadata

| Field | Value |
|---|---|
| Round date | `YYYY-MM-DD` |
| Model under test | |
| Incumbent default | |
| Eval set version | |
| Repositories used | |
| Languages covered | |
| Task count | |
| Harness / agent scaffold version | |

## Pass rate, per language

| Language | Model under test | Incumbent | Delta (pp) |
|---|---|---|---|
| Python | | | |
| Java | | | |
| Kotlin | | | |
| TypeScript | | | |
| _(add rows)_ | | | |

## Head-to-head split

| Language | Won (new solves, incumbent misses) | Lost (incumbent solves, new misses) | Net |
|---|---|---|---|
| | | | |

Task IDs lost — list them, these are the candidates to keep routing to the incumbent:

- 

## Failure decomposition

| Outcome bucket | Model under test | Incumbent |
|---|---|---|
| Failed to run | | |
| Ran and was wrong | | |
| Ran and was right | | |

## Efficiency

| Metric | Model under test | Incumbent | Delta |
|---|---|---|---|
| Median steps to solution | | | |
| Median wall-clock to solution | | | |
| Cost per completed task — routine work | | | |
| Cost per completed task — long-running agentic work | | | |

## Public-benchmark cross-check

| Public benchmark | Reported score | Our private-set behaviour | Consistent? |
|---|---|---|---|
| | | | |

> A large gap between a strong public score and weak private-set behaviour is itself a
> finding. Record it.

---

## The three leaderboards after this round

| Leaderboard | 1st | 2nd | 3rd | Changed this round? |
|---|---|---|---|---|
| Best quality | | | | |
| Best cost-per-task | | | | |
| Fastest | | | | |

## Routing decision

| Workload class | Model routed to | Rationale | Changed this round? |
|---|---|---|---|
| Routine edits / high-volume work | | | |
| Ambiguous or reasoning-heavy problems | | | |
| Long-running agentic runs | | | |
| Interactive in-editor completion | | | |
| Security testing against our own products | | | |

## Deployment posture

- **Safety approach:** what is enforced by the harness/permissions rather than by the model —
- **Security testing:** what we ran the model against, and open findings —
- **Data retention position:** chosen setting and the reasoning —
- **What would change our mind:** the numbers or incidents that would trigger a re-decision —

## Sign-off

| Role | Name | Date |
|---|---|---|
| Eval owner | | |
| Deployment owner | | |
