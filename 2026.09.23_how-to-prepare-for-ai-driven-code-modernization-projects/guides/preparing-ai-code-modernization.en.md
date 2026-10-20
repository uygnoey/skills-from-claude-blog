**English** · [한국어](./preparing-ai-code-modernization.ko.md) · [Español](./preparing-ai-code-modernization.es.md) · [日本語](./preparing-ai-code-modernization.ja.md)

# Preparing an AI-driven code modernization

A methodology from Anthropic's forward deployed engineers (Notes from the Field) for running large
code modernizations of critical systems in regulated enterprises.

## Why preparation is the real work

Modernizations once scoped as multi-year, all-hands efforts can now finish in months or weeks. But
change management, review, and approval — the processes that make critical systems trustworthy —
were built on the assumption that a human wrote and a human reviewed each diff. Once agents write
the changes, the bottleneck moves from producing changes to mobilizing the organization around them.

## The six steps

| # | Step | Output |
|---|---|---|
| 1 | Define the target | Tech stack and behavior the modernized code must have |
| 2 | Create the certificate | Conditions a change must meet to be considered correct |
| 3 | Set the promotion policy | The path by which certified changes reach production at the rate they are produced |
| 4 | Put prerequisites in place | Environment, CI/CD, review capacity, approvals |
| 5 | Build and refine the agentic workflow | A custom Claude Code dynamic workflow of parallel subagent workstreams |
| 6 | Run the modernization | End-to-end proof on a small partition, then scale |

### 1. Define the target
Choose **uplift** (same-stack version bump), **transform** (cross-stack rewrite with fixed
behavior), or **reimagine** (greenfield rebuild with changed behavior and a written behavioral
spec). Production owners usually favor transform; long-time engineers and business stakeholders
often push for reimagine. Settle it early, or it returns as disputes about whether each change is
"correct." Map the codebase (the code modernization plugin's `assess`, `map`, `extract-rules`
commands help), supplement with interviews and documentation, and anchor the business case —
usually **risk reduction**, not cost reduction.

### 2. Create the certificate
A set of conditions every change must pass, each checkable without a human: original and
Claude-authored tests, coverage thresholds, performance bounds, fresh-context adversarial Claude
reviews, computer-use UI checks, input/output parity, state and wire-format round-trips, staging
soak, static analysis and security scans, clean builds. Uplift leans on the original test suite;
transform on traffic replay, differential testing, and prod-parallel runs; reimagine on the spec.
Write it with the reviewers. If evidence is missing, have Claude build it.

### 3. Set the promotion policy
Tier review depth by blast radius and agent confidence; keep full review for critical paths. Fix
recurring flags at their source. Design review output formats with reviewers. Direct scarce SME time
to the highest-risk tiers. Decide where you sit between speed and review depth, and have leadership
issue the policy in advance so accountability for an escaped bug is shared.

### 4. Put prerequisites in place
Remote host and test capacity; telemetry, prod-parallel or replay data; a grounded dependency map;
CI/CD compatibility checks; code-freeze and communication plans; reviewer time from dependent teams;
an approved model access path, least-privilege access, scrubbed secrets and PII, PR-to-transcript
traceability, and license/vulnerability checks. Start these conversations early — other teams have
their own backlogs.

### 5. Build and refine the workflow
Start with the code modernization plugin. Put the target, certificate, policy, codebase, docs, and
tooling on the file system or behind MCP as the project's knowledge base. Pilot on small pieces with
SME review. When issues surface, fix the workflow, not each change.

### 6. Run it
Land one small partition end to end through the promotion policy, iterate while it's cheap, then
scale. Uplifts can modernize in place: partition from the leaves inward, freeze one partition at a
time, and gate CI/CD so new commits cannot undo finished partitions.

## Cost
Drivers: read-vs-change volume, certificate complexity (verification often dominates in regulated
settings), test writing and repair, and reconciliation with concurrent merges. Measure tokens in the
pilot and extrapolate a cost floor; treat what the pilot couldn't see as unknown. Put expensive
checks behind cheap gates, use models like Sonnet for mechanical work, reserve stronger models for
hard transformations and adversarial review, and watch retry rates when escalating between models.

## Beyond the modernization
Besides the code, you end up with a reusable workflow, a written certificate, an accepted promotion
policy, and an evidence trail. Codify them as a playbook for the next upgrade.

## Source
- https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects
