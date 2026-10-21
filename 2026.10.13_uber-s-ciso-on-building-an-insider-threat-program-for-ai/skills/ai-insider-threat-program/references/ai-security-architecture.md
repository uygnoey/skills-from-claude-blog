# Uber's AI security architecture (as described in the source)

| Layer | Role | Notes from the source |
|---|---|---|
| LLM gateway | Perimeter; controls how AI is used within Uber | Combined with ADR and safeguards into the overall architecture |
| AI Detection and Response (ADR) | Real-time telemetry and real-time action in deployed agent harnesses | Open-sourced by Uber; detects agents acting outside their bounds |
| Enterprise Frontier Safeguards | Anthropic classifier output on misuse | Customer controls its data and post-trigger actions; expected to feed ADR as a data source |
| Detection environment | Correlates own telemetry + provider classifier output | Run "much like a traditional cybersecurity one" |

## Defender priorities (in Martin's order)
1. Real-time detection and intervention, as close as possible to prompt entry and tool calls.
2. Understanding emerging patterns: trend analysis → discover new behaviors → safeguards back into
   the real-time platform → repeat.

## Why monitoring is justified
- Every company already runs an insider threat program for its people; nobody argues about it.
- Frontier models introduce the same risk: they may be directed to act outside their constraints.
- AI adoption is a business imperative; stakes rise with capability and autonomy.

For product details of ADR and Enterprise Frontier Safeguards, see the links in the source article.
