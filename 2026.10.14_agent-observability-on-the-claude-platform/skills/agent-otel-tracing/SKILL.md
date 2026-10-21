---
name: agent-otel-tracing
description: Set up and use OpenTelemetry (OTel) traces from Claude Managed Agents, the Messages API, and Claude SDKs on the Claude Platform (public beta). Each agent turn, model call, tool use, and MCP server call arrives in any OTLP-compatible observability tool as a standard trace with latency, tokens, and IDs, following the OpenTelemetry GenAI semantic conventions. Covers where traces come from (Console destination for Managed Agents and the Messages API; automatic export from SDKs), picking a tool for debugging, eval/quality improvement, or org-wide usage tracking, and using traces to widen an agent's access as it proves reliable. Use when adding observability to Claude-built agents, debugging slow or failed agent steps, turning production traces into evals, or tracking token usage by team.
---

## Purpose
The Claude Platform can send OpenTelemetry traces from Managed Agents, the Messages API, and Claude
SDKs to any OTel tool, so you can follow each step an agent takes. If you already send Claude Code or
Cowork traces to an observability tool, agents built on the Claude Platform can show up in the same
place. Trusting an agent with more access starts with tracing its model calls, tool use, and MCP
server calls: review its traces, then widen its access as it proves reliable.

## When to use
- You run agents on Managed Agents, the Messages API, or a Claude SDK and want per-step visibility.
- A step is slow or failing and you need to see which service it came from.
- You want to turn real production traces into evals and measure whether a change helped.
- Platform or security teams need token usage by team and alerts on unusual activity.

## Instructions

### 1. Turn on export
- **Managed Agents and Messages API**: add a destination in the Claude Console.
- **Claude SDKs**: traces export automatically.
- The feature is in public beta; follow the official docs linked from the source for configuration
  details (endpoint, auth). Any tool that accepts a standard OTLP endpoint works.

### 2. Know what you get
Every agent turn, model call, and tool use (including MCP server calls) arrives as a standard
OpenTelemetry trace with latency, tokens, and IDs. Traces follow the OpenTelemetry GenAI semantic
conventions, so Claude data and data from other providers can share tools and dashboards.

### 3. Pick a destination by goal
See [references/observability-tools.md](references/observability-tools.md):
- **Debug next to the rest of your stack** — agent traces beside logs and metrics.
- **Improve agents with production data** — traces → evals, quality issues, change impact.
- **Track usage across the org** — token usage by team, unusual activity.

### 4. Use traces to grant access gradually
Start an agent with narrow access, review its traces (tool calls, MCP calls, failures), and widen
access only as it proves reliable.

### 5. Close the loop
Feed traces into an improvement loop: score traces, find recurring failures, propose fixes, and
measure the result. Customer patterns are in [examples/customer-patterns.md](examples/customer-patterns.md).

## Examples

**Example — slow step in production**
- Agent traces land in your existing observability backend next to service logs and metrics.
- The slow span is a tool call into an internal service; the trace shows which service and its latency.

**Example — evals from real traffic**
- Export traces to an eval-oriented tool, select failing sessions, turn them into eval cases, then
  compare scores before and after a prompt change.

**Example — audit question**
- An auditor asks what an agent did. Because each model call sits in the same trace as the business
  workflow it ran inside, you answer from one timeline (prompt version, tool calls, latency, tokens).
