# Customer patterns from the source

| Company | Tool | Pattern |
|---|---|---|
| Foxglove (agents that help robotics teams debug robots) | PostHog | Analyze agent interactions alongside product usage data to see how agents perform, where they fall short, and what to improve |
| Ramp | Langfuse | "Reflect", an agentic system that scores Langfuse traces, finds recurring failures, and proposes fixes; on some agents token usage fell 10–20% and sessions got 30% faster. Native export feeds instrumentation into that loop with no extra steps |
| Sterling Labs (agents analyzing live markets 24/7) | Langfuse | Every trace streamed in with no custom instrumentation, so the team focuses on the work, not the wiring |
| Accounting agents (company: see source) | Grafana Cloud | Each model call sits in the same trace as the reconciliation or journal-entry workflow; prompt version, tool calls, latency, and token spend on one timeline for auditors |

## Takeaways
- Put agent traces where the rest of your telemetry already lives.
- An improvement loop can only improve what it observes — export first, then score and fix.
- For regulated work, keep model calls inside the business workflow's trace for auditability.
