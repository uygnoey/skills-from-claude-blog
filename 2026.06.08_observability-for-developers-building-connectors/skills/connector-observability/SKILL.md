---
name: connector-observability
description: Monitor, debug, and improve a published Claude connector using directory observability signals like adoption, error rates, and latency.
---

# Connector observability

Use this skill to review the directory observability dashboard for a published connector, interpret the signals it provides, and turn them into concrete reliability/performance follow-ups.

## Instructions

1. **Confirm scope and access**
   - Confirm the connector is published in the Claude directory.
   - Confirm you have access (Team or Enterprise with Admin/Owner, or an Enterprise custom role with the Libraries permission).

2. **Review adoption signals**
   - Active users
   - Total tool calls
   - Directory rank over time

3. **Review reliability and performance signals**
   - Health score
   - Error rates
   - Latency overview
   - Per-tool error breakdown (use this to pinpoint which tool is failing)

4. **Break down usage by product surface**
   - Compare tool calls across product surfaces (e.g., Claude, Claude Code, Cowork) to understand where usage is coming from.

5. **Produce an action list**
   - Summarize the biggest issues/opportunities indicated by the dashboard.
   - Propose the next steps (e.g., investigate top failing tools, address latency, validate changes by tracking error rate trends).

## Examples

### Example: quick review checklist
- Adoption: active users, total tool calls, directory rank trend.
- Quality: health score, error rate trend, latency overview.
- Debugging: per-tool error breakdown.
- Distribution: product breakdown (Claude vs Claude Code vs Cowork).

## Source
- https://claude.com/blog/observability-for-developers-building-connectors
