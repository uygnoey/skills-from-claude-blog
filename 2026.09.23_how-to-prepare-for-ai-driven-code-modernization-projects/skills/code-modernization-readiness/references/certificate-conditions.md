# Certificate conditions

The certificate is the set of conditions or tests every modernization change must meet. Pick the
conditions that give the strongest **cumulative** evidence that a change is correct against the
target. Each must be checkable without a human in the loop.

## Condition catalog

- [ ] The original test suite passes
- [ ] Claude-authored tests written during the modernization all pass
- [ ] Test coverage meets an agreed threshold
- [ ] Performance benchmarks stay within an agreed bound
- [ ] Independent adversarial reviews by Claude, each in a fresh context window, find no blocking issues
- [ ] For user interfaces, Claude-driven computer use finds no regressions
- [ ] Current and target versions produce the same output from the same input (live, recorded, or Claude-generated)
- [ ] Persisted state and wire formats round-trip between current and target versions
- [ ] Changes run in staging for an agreed period with no regressions in error rates, latency, or alerts
- [ ] Static analysis and security scans show no new findings
- [ ] For compiled targets, the build is clean and type checks pass

## Parity strategy by type

| Type | Checked against | Main evidence |
|---|---|---|
| Uplift | The original codebase | The original test suite can be the core of the certificate. |
| Transform | The original codebase | The original tests rarely run on the new stack — production-traffic replay, differential testing between old and new, and a prod-parallel deployment do most of the work. |
| Reimagine | The behavioral spec | Tests written from the spec, independent adversarial Claude reviews against the spec, and differential checks where the new system keeps old behavior. Hardest case: more model judgment, more variable outcomes. Expect to revise the certificate as the spec is clarified. |

## Who writes it

Write the certificate with the developers, user groups, and business leads who will review and
promote changes, while the certificate and workflow are still being designed. Good final check:
would they be comfortable merging on the certificate's evidence alone? If they see their own bar in
it, the promotion policy can be lighter.

## Missing evidence

Older systems often have thin coverage, flaky tests, and little telemetry. Identify these gaps now.
If a strong certificate is hard to support, use Claude to build the missing evidence — stand up a
prod-parallel setup, build a replay harness, or write more tests.
