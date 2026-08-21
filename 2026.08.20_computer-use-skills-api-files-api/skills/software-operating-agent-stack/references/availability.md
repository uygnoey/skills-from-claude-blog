# Availability and migration

As stated in the general-availability announcement of 2026-08-20.

## Claude Platform

The computer use tool, the browser use tool, the Skills API, and the Files API
are now available on the Claude Platform.

## Cloud availability

| Surface | Status as announced |
| --- | --- |
| Claude Platform | Computer use, browser use tool, Skills API, Files API available |
| Microsoft Foundry | Skills API and Files API available |
| Google Cloud Vertex AI | Updated computer use and browser use tools **coming soon** |

## Regulated workloads

Computer use is now eligible for HIPAA-regulated workloads under Anthropic's BAA.

## Migrating from beta

**Existing beta integrations keep working while you migrate.** There is no
forced cutover stated in the announcement.

A reasonable migration order, given what GA changes:

1. **Files API first.** The additions are additive — automatic expiration, 5x
   higher rate limits, 1 TB per organization. Little to change in calling code;
   review whether automatic expiration matches your retention expectations.
2. **Skills API next.** The API for uploading and versioning skills is simpler at
   GA. Moving here also moves your procedures out of prompt strings and into
   versioned artifacts, which is worth doing before you scale the number of
   agents.
3. **Computer use last, and measure.** The multi-action turns change latency and
   cost characteristics, so re-run your evals rather than assuming parity. The
   reported experience is that gains came with no prompt changes, but that is one
   team's result, not a guarantee for yours.
4. **Swap web tasks to the browser use tool.** For anything already running
   against a web application under pixel-level computer use, the structural
   targeting is the reliability upgrade.

## Documentation

The announcement points to the platform documentation for computer use, the
browser use tool, the Skills API, and the Files API as the place to get started.
Those docs, not this file, are authoritative for parameters, limits, and pricing.

## Source

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api) (published 2026-08-20).
