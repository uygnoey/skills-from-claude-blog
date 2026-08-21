# Case studies from the source post

Two migrations reported in the post, with the numbers as published. They are useful mainly
as calibration: for the scale these loops reach, and for what the cost actually looks like.

---

## Bun — Zig to Rust

Led by Jarred Sumner.

| | |
| --- | --- |
| Scale | ~1 million lines produced |
| Elapsed time | Under two weeks |
| Gate before merge | 100% of Bun's existing test suite passing in CI |
| Post-merge regressions | 19, all fixed |
| Token spend | 5.9B input / 690M output |
| Approximate cost | ~$165,000 at API pricing |
| Binary size | 19% smaller on Linux and Windows |
| Performance | 2–5% faster across real workloads |

Points worth taking from it:

- The merge gate was mechanical and pre-existing — the project's own test suite, at 100%.
  The judge was not invented for the migration.
- 19 regressions on a million lines is the realistic shape of success, not zero. The
  question a migration has to answer is whether regressions are findable and cheap, not
  whether they are absent.
- The cost is knowable in advance if you know where your tokens concentrate, which is the
  argument for choosing models per role rather than using the largest one everywhere.

---

## Python to TypeScript — Mike Krieger

| | |
| --- | --- |
| Scale | 165,000 lines of TypeScript |
| Elapsed time | A weekend |
| Fan-out | 12 parallel subagents on Claude Sonnet |
| Judge | Parity harness of seven real-world scenarios |
| Build time | 30 minutes → roughly 2 seconds |
| Follow-up | An autonomous end-to-end test suite left to run overnight for refinement |

Points worth taking from it:

- Seven scenarios were enough, because they were real end-to-end scenarios rather than
  shallow unit tests. Any behavior change against them counted as a bug to fix.
- Twelve implementers on a smaller model, in parallel, is the shape Step 3 is supposed to
  take. The parallelism comes from the dependency map.
- The payoff was not only "same thing, new language" — a 30-minute build becoming a
  two-second one changes how the team works afterward.

---

## Reading these correctly

The post is explicit that each migration is different and that this should be treated as a
starting point rather than a recipe to follow blindly. Plan your specific migration with
Claude before committing to it — particularly the architectural decision in Step 1, which
determines whether your rulebook is a set of lookup tables or a design document.
