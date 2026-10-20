---
name: code-modernization-readiness
description: Prepare an organization for an agent-driven code modernization of a critical or regulated system — define the target (uplift, transform, or reimagine), write the certificate of automatically checkable conditions every change must meet, agree a tiered promotion policy for human review, stage prerequisites, then build, pilot, and scale a Claude Code dynamic workflow. Use when scoping a legacy rewrite or version upgrade, when review and change management (not code writing) are the bottleneck, or when estimating token cost for a large modernization.
---

## Purpose
Agents can now produce modernization changes far faster than an organization can review and
promote them. The bottleneck moves from writing changes to mobilizing the organization around them.
This skill walks through the six steps of work that must happen before and around the run so that
certified changes reach production at the rate they are produced.

## When to use
- Scoping a legacy modernization (version bump, cross-stack rewrite, or rebuild) of a system with
  change management, auditors, or regulators.
- Stakeholders disagree on whether behavior may change during the modernization.
- The test suite is thin or flaky and there is little telemetry to prove a change is correct.
- Leadership needs a business case or a token-cost estimate before committing.

## Instructions

Work through the steps in order. Steps 1–3 are decided **with** the reviewers and approvers, not
handed to them at the end. Open Step 4 conversations as soon as requirements are known, often while
Steps 1–3 are still underway.

1. **Define the target.**
   - Pick the modernization type — uplift, transform, or reimagine — using
     [references/modernization-types.md](./references/modernization-types.md). Resolve the debate
     up front; if left open it resurfaces later as arguments over whether a given change is "correct."
   - Map the codebase and inventory current behavior. Claude can map dependencies and document
     forgotten workflows; the code modernization plugin's `assess`, `map`, and `extract-rules`
     commands mine business rules with source citations for engineers to review. Fill gaps with
     interviews of business users and developers, and internal documentation.
   - For a reimagine, write a detailed behavioral spec and agree it with user groups.
   - Establish justification and goals, usually at leadership level. Risk reduction (unpatched
     vulnerabilities, unsupported runtimes, a shrinking pool of engineers who understand the system)
     is often the strongest argument — weigh the risk of *not* modernizing.
   - Record the result in [templates/modernization-charter.md](./templates/modernization-charter.md).

2. **Create the certificate** — the set of conditions every change must meet to be considered
   correct against the target.
   - Every condition must be checkable without a human in the loop, so the workflow can iterate a
     change until it passes or flag it for human review.
   - Choose from the condition catalog in
     [references/certificate-conditions.md](./references/certificate-conditions.md); parity
     strategy depends on modernization type.
   - Write it with the people who will review and promote changes. Test: would they be comfortable
     merging on the certificate's evidence alone?
   - Where evidence is missing (thin coverage, flaky tests, no telemetry), use Claude to build it:
     a prod-parallel setup, a replay harness, or more tests.

3. **Set the promotion policy** — a tiered review path, written and agreed in advance, that sets the
   depth of human review per change. Follow the rules in
   [references/promotion-policy.md](./references/promotion-policy.md): tier by blast radius and
   agent confidence, fix recurring flags at the source, design output formats with reviewers, and
   spend SME time on the highest-risk tiers. The directive should come from the top of the
   organization so responsibility for an escaped bug is shared.

4. **Put prerequisites in place** using
   [references/prerequisites-checklist.md](./references/prerequisites-checklist.md): environment,
   codebase and CI/CD, teams and review capacity, security and compliance.

5. **Build and refine the agentic workflow.**
   - Start from the code modernization plugin in Claude Code.
   - Put everything the workflow may need on the file system or behind MCP: target, certificate,
     promotion policy, codebase, documentation, and the data sources and tooling the certificate requires. This
     is the project's central knowledge base.
   - Have Claude build a dynamic workflow that distributes the work across many smaller parallel
     subagent workstreams. Have SMEs review codebase-specific skills and extracted rules before
     anything downstream relies on them.
   - Apply it to small parts of the codebase; SMEs review the changes, the agents' process, and the
     certificate evidence. When issues surface, **modify the workflow, not each change.**

6. **Run the modernization.**
   - Complete one small partition end to end, including review and landing via the promotion
     policy. Fix what doesn't work while it is cheap, repeat until confident, then scale.
   - Transform and reimagine build the target alongside the existing system and cut over once
     complete. An uplift may instead modernize **in place**: split the codebase into partitions
     from the leaves inward, freeze and modernize one partition at a time, and gate CI/CD so new
     commits cannot undo a modernized partition.

7. **Estimate and optimize cost** from the pilot with
   [references/cost-estimation.md](./references/cost-estimation.md).

8. **Codify the playbook.** Outputs beyond the code: the workflow, the written certificate, a
   promotion policy change management already accepted, and an evidence trail per change. Keep them
   as reusable assets for the next upgrade or rewrite.

## Examples

**Example 1 — Runtime losing support (uplift, in place).**
A C++11 service must move to C++20 before its toolchain loses support. Target: runtime version and
package set. Certificate: original test suite passes, clean build and type checks, performance
within agreed bound, no new static-analysis findings. Promotion policy: fast path with lighter human
review, with an explicit agreement to accept more risk per change because of the hard deadline.
Run: partition from the leaves inward, freeze one partition at a time, CI gate prevents regressions.

**Example 2 — COBOL to Java (transform).**
Behavior is trusted; the stack is the problem. The original tests don't run on the new stack, so
the certificate leans on production-traffic replay, differential testing between old and new, and
a prod-parallel deployment. Critical payment paths always get full human review; low-blast-radius,
high-confidence changes take a lighter path.

**Example 3 — Rebuild with new requirements (reimagine).**
Write and agree a behavioral spec first. The certificate uses tests written from the spec,
independent adversarial reviews by Claude in fresh contexts that check each change against the
spec, and differential checks where behavior is meant to stay the same. Expect to revise the
certificate as gaps in the spec show up.

## Source
- https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects
