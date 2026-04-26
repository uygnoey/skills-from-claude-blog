# API integration failure-mode catalog

Failure modes named or implied in [How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (2025-10-27). Use this list as input to the [risk-discovery-prompt](../templates/risk-discovery-prompt.md). Do not assume an item applies until the vendor's documentation confirms it.

## Authentication

- **Authentication tokens expire during critical workflows**, triggering 401 errors that cascade through downstream services.
- **OAuth tokens expire mid-request during multi-step flows** (e.g. multi-step checkout). Refresh logic must handle in-flight calls without dropping state.
- **Authentication headers expire mid-request** for short-lived credentials.
- **Credential rotation** for API keys must keep monitoring and avoid downtime.
- **JWT validation** required for microservice-to-microservice calls.

## Rate limits

- **Rate limits silently throttle requests**, causing timeout failures downstream.
- **Rate-limit counting varies**: per user, per IP, or per API key, depending on the vendor.
- **All clients retry simultaneously during outages** without jitter, producing a thundering herd.
- **Aggressive retry mechanisms** can themselves create cascade failures.
- **Mitigation**: exponential backoff with jitter for 429 responses; request queuing patterns; circuit breaker implementations.

## Schema and versioning

- **Schema changes in third-party APIs break production integrations without warning.**
- **Multiple API versions in flight** require versioned clients and adapter layers translating between old and new response formats.
- **Schema validation** at the response boundary catches breaking changes early.

## Webhooks vs polling

- **Webhooks**: immediate updates, but require signature validation, idempotency handling, and retry logic for failed deliveries; webhooks may arrive out of order.
- **Polling**: simpler, but increases API call volume and introduces latency.
- **Hybrid strategies** that combine both are valid for some use cases.

## Process / debugging

- Most teams discover the above only after production incidents and retrofit error handling reactively.
- Reproducing the exact conditions that triggered each failure becomes its own debugging challenge.

## Source

[How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (2025-10-27).
