# Default permission mode — decision record

Copy this file, fill it in, and keep it with the settings it describes.

## 1. Scope

- **Organization / team / individual:**
- **Plan or surface:** (Pro / Max / Team / Enterprise / API / AWS / Bedrock / Google Cloud Agent Platform / Microsoft Foundry)
- **Date of decision:**
- **Owner:**

## 2. Decision

- **Default permission mode being set:**
- **Set how:** (left to the product default / `defaultMode` in managed settings / `disableAutoMode` / individual choice)
- **Applies to:** (everyone / named teams / named repositories)
- **Users who will see a one-time switch prompt:**

## 3. Rationale

- Why this default rather than the alternatives:
- Evidence cited (see `references/safety-evidence.md`):
- What the previous default was costing us (prompt fatigue, bypass usage, broad allow-rules, stalled long-running work):

## 4. Permission rule audit

| Rule | Type | Status under auto mode | Keep / change |
| --- | --- | --- | --- |
| e.g. `Bash(python:*)` | interpreter allow-rule | set aside while in auto mode | |
| | deny | still enforced | |
| | allow (narrow) | still fires before the classifier | |

- **Interpreter-level allow-rules that will be inactive:**
- **Deny rules retained as hard guardrails:**
- **Additional hard-deny categories configured beyond the built-in data-exfiltration denies:**

## 5. Exceptions — when to step out of auto mode

List the workflows that must not run under auto mode, and the mode to use instead.

| Workflow | Why | Mode to use |
| --- | --- | --- |
| Production infrastructure changes | High-stakes, hard to reverse | |
| Actions that communicate with other people on a user's behalf | Policy, not safety | |
| | | |

## 6. Rollout plan

- **Announcement to users (date, channel):**
- **Pilot group and duration, if any:**
- **What we will measure:** (classifier denial rate, PR throughput, escalations, incidents)
- **Rollback: what would make us change the default back, and who decides:**

## 7. Limits acknowledged

- Auto mode relies on classification systems and does not eliminate risk.
- Published miss rates come from synthetic, adversarial attack sets and are not real-world
  miss rates.
- High-stakes production changes still warrant human review.

**Signed off by:**
