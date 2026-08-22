# Controls for managing spend

## Model defaults and entitlements

Admins set **which model new conversations start with**, across:

- chat
- Cowork
- Claude Code

so routine work doesn't necessarily default to the most expensive option.

Admins also control **which models are available to specific roles or across the entire
organization**. Entitlements are the role-scoped half; the default is the org- or surface-scoped
half. They are set independently.

## Spend-threshold alerts

| Who | Thresholds | What they can do |
|---|---|---|
| Admins | **75%** and **90%** of an org-level spend limit | Raise the cap before anyone gets blocked mid-task |
| Users | **75%** and **95%**, in-app | Request a limit increase directly from their admin, without leaving the product |

The admin's second alert (90%) fires before the user's second alert (95%), which is what makes the
cap increase a decision rather than an interruption.

## Pre-existing controls this builds on

The post is explicit that these additions sit on top of controls already available:

- spend caps at every level
- access and model routing
- a usage analytics dashboard with exports, and an Analytics API
- effort controls

## Source

["Giving admins more visibility and control over Claude spend"](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)
— Anthropic, July 2, 2026.
