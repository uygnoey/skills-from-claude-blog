# Estimating and reducing token cost

Every modernization differs. Main cost drivers:

- How much of the codebase has to be **read** versus **changed**.
- How involved the certificate is — in a regulated environment, verification (not writing the
  change) is usually the larger share.
- How much new test writing and test repair the certificate demands.
- How much reconciliation work comes from other teams merging around you during the run.

## Estimate from the pilot

When completing the modernization on a small part of the codebase, measure token usage and
extrapolate to the rest of the run. Treat anything the pilot could not see (e.g., reconciliation on
a live codebase) as an unknown. The result is a **cost floor** for the full modernization.

## Optimize using pilot measurements

- Find the parts of the workflow that consumed the most tokens and make them more efficient.
- Move compute-heavy verification signals behind cheaper gates so they only run after easier checks
  pass.
- Use cost/capability-balanced models such as Sonnet for mechanical, high-volume work the
  certificate fully checks; keep more intelligent models for hard transformations and adversarial
  correctness reviews.
- Escalating to a more expensive model when a cheaper one fails the certificate is an option, but
  analyze retry rates while piloting — several cheap attempts can cost more than one expensive one.
- Give Claude access to the workflow and the pilot data; it can do much of this analysis with you.

Published costs of prior large-scale modernizations (by Anthropic and others) can serve as a rough
baseline — see the original article.
