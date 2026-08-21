# Cost controls for Claude Enterprise

Three controls, applied in this recommended sequence. The order matters: each layer shrinks the
population the next layer has to govern.

## 1. Access gating

Determines **which groups and custom roles can access which products** — for example Claude Code
and Claude Cowork.

The point of doing this first is that it enables a **phased rollout by department** rather than
switching a product on organization-wide. You are not trying to restrict people permanently; you
are trying to learn what a department's usage actually looks like before the next department
joins.

## 2. Model controls

These function at **two levels**:

- **Entitlements** — specify which models a team can access at all.
- **Defaults** — set the starting model for new conversations.

The two together let you restrict the most capable models to teams handling complex work, while
defaulting everyone else to Sonnet. Defaults matter more than they look: most usage follows the
default, so setting a sensible default moves more spend than any entitlement restriction.

## 3. Hard spend caps

Usage ceilings placed at three levels:

- **Organizational** — a ceiling for the whole org.
- **Individual user** — a ceiling for one person.
- **Group** — note the semantics: **each member of the group receives the specified limit**. A
  group cap is not a shared pool that the fastest spender drains.

**Caps take effect immediately.** This is what makes them different from a budget alert — the
spend actually stops.

## Ongoing administration

Beyond the three controls, administrators can:

- **Automate spend limit increase requests** — so a person hitting a cap does not have to go
  find an admin, and the admin is not the bottleneck for legitimate work.
- **Identify users approaching limits** — intervene before the cap interrupts someone
  mid-project.
- **Track rapidly changing usage patterns** — a sharp change is worth a look regardless of
  whether it breaches a cap, in either direction.

## Sequencing note

Applying caps first, before gating and model controls, is the common mistake. It produces a
ceiling nobody understands and interruptions that look arbitrary. Gate access, set sensible
model defaults, watch what happens, and only then set caps at levels informed by what you
observed. The companion file `examples/usage-questions.md` lists what to look at during that
observation window.
