# Safeguards for agent-written code (as described by Block)

## Hard guarantees (humans only)
- Merges to main.
- Deploys to production.
- Related changes such as feature flags.
- Agent code changes must pass security checks; then **two humans approve** the deploy. This
  dual-approval layer makes it impossible for a model to push these changes on its own.

## Secure by default
- Prefer remote workstations: easier to secure, and they avoid laptop problems such as agents filling
  up disk space.
- Network **allow list** instead of a deny list.

## Checks outside the model loop
- Cheap, efficient checks that run without the model, built into the interfaces people work in —
  sometimes just a regex; increasingly, small classifiers.

## Allowed on purpose (blocking isn't worth it)
- Opening PRs, reviewing code, querying logging systems and analytical databases.

## Model-level safeguards
- Rely on the model's own refusal behavior plus the provider's safety classifiers for the remaining
  risk. Block benchmarks this: asked to "hack around" the dual-approval system, Claude refuses.
  Add a similar test to your own evaluation suite.
