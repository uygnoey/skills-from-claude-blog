# Rollout checklist — analytics and cost controls

Derived from the "getting started" guidance in the source post, sequenced so each step has the data
the next one needs.

## Prerequisite

- [ ] SCIM groups are managed by IT and reflect the current org chart.
      Every breakdown and every limit below is set per group.

## Visibility

- [ ] Open the admin console and explore **usage and cost breakdowns by group and by user**.
- [ ] Check output next to cost: artifacts created, files edited, skills and connectors used.
- [ ] For developer usage, review the **usage tab** (active developers, session counts, top commands
      — updated daily).
- [ ] Open the **value tab**, read each visible formula, and **adjust the inputs** to the
      organization's real numbers before quoting productivity lift, cost per commit, or annual
      value.
- [ ] Ask analytics chat the questions the dashboard has no tile for; export the charts that answer
      them.
- [ ] Decide whether to **extend usage visibility to individual users** (cost, product and model
      breakdowns, progress against spend limits).

## Controls

- [ ] Set **model defaults** for new conversations across chat, Cowork, and Claude Code, informed by
      the breakdown above — not by a guess.
- [ ] Set **entitlements**: which models are available to which roles, and which org-wide.
- [ ] Set **spend limits by group**.
- [ ] Enable **spend-threshold alerts**: admin at 75% and 90% of the org-level limit; users at 75%
      and 95% in-app, with in-product increase requests.

## Integration

- [ ] Connect the **Analytics API** so finance and IT see usage and cost alongside the rest of cloud
      and AI spend (e.g. Datadog Cloud Cost Management, CloudZero).
- [ ] Confirm the filters your reporting needs: date range, team, product, model.
- [ ] Wire up **skill-level usage and cost**, and the **plugin adoption** and **artifact creation**
      endpoints.

## Scale

- [ ] Once the number of groups outgrows manual review, move to the **Admin API**: automate
      increase-request reviews, identify members close to their spend limit, and flag rapidly
      changing usage.

## Review cadence

- [ ] Set a recurring review so cost visibility is not a once-a-month exercise. The alerts do the
      interrupting; the review does the reassessing.

## Source

["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)
— Anthropic, July 2, 2026.
