---
name: domain-agent-builder
description: Design a natural-language agent builder on top of the Claude Agent SDK, following the approach Cresta used for Conductor, its CX agent builder — the SDK as the general-purpose execution harness, your domain workflows, tools, and context layered on top, a blueprint → implementation → evaluation → optimization flow, explicit decisions about which workflows must be deterministic, a fixed build-task evaluation suite rerun on every model or framework change, and reusable memory artifacts shared as skills. Use when a team with deep domain expertise wants to turn it into a product that builds production-ready agents.
---

## Purpose
Cresta (a customer experience AI company) built Conductor, a natural-language agent builder that
helps teams create production-ready CX agents. Users describe what they want, and Conductor guides
the work through a blueprint, implementation, evaluation, and optimization. Early use across Cresta
and its partners reportedly cut initial deployment time roughly in half. This skill turns that
approach into a repeatable plan for any domain.

## When to use
- You have domain data and expertise (e.g. historical conversations) and want to package it as an
  agent builder.
- You are deciding what to build yourself versus take off the shelf on the Claude Agent SDK.
- You need an evaluation loop that tells you what improved or regressed when a new Claude model
  ships or your framework changes.

## Instructions

1. **Split the stack.** Use the Claude Agent SDK as the general-purpose execution harness: gathering
   context, calling tools, writing and running code. Put your domain workflows, tools, and domain
   context on top. Invest only in what only you can provide (for Cresta: conversation data and CX
   expertise); use off-the-shelf components for the rest.

2. **Check enterprise requirements before committing.** Cresta evaluated the SDK for data privacy,
   tenant architecture, organization-level key distribution, controls, and observability. Record
   your own answers for each.

3. **Model the builder flow.** Guide the user from a natural-language description through four
   stages: blueprint → implementation → evaluation → optimization.

4. **Decide what must be deterministic.** Use historical data (for Cresta, past conversations) to
   find where a human should stay in the loop and where the model can adapt. Harden the workflows
   that can never fail — especially in regulated industries — with explicit rules. Keep the rest
   flexible. Test and revise those rules as business requirements change.

5. **Build a fixed evaluation suite of build tasks.** Cresta's tasks: create an agent, write a test
   case, change an existing agent, perform root cause analysis. Score every run on four dimensions:
   - **Outcome** — was a usable artifact produced?
   - **Execution path** — were appropriate tools and context used?
   - **Quality** — how does the result compare with a curated reference?
   - **Resource use** — time and model usage.
   Use [templates/build-task-scorecard.md](./templates/build-task-scorecard.md).

6. **Rerun on every change.** When a new Claude model launches or your framework changes, rerun the
   same tasks with the same scoring and compare against the previous run to see what improved and
   what regressed.

7. **Dogfood before shipping.** Use the builder internally first (Cresta started with its own
   deployment teams, using Claude Sonnet and Claude Opus). Treat it as a product only when its
   output matches what an expert engineer would build.

8. **Start the knowledge flywheel.** Let builders capture proven patterns, business rules, and
   evaluation approaches as reusable memory artifacts, and share them as skills across the team.

9. **Budget for iteration.** Cresta puts the initial build at about 20% of the effort; testing,
   optimization, and continuous improvement are the other 80%.

## Examples

**Contact-center agent for a regulated industry**
- Deterministic: identity verification and required disclosures are explicit rules with tests.
- Flexible: small talk, rephrasing, and order of non-critical questions.
- Historical conversations show that refund disputes above a threshold need a human in the loop.

**Model upgrade check**
- Rerun the four build tasks on the new model with the same scorecard.
- Result: outcome and quality improve on "change an existing agent", resource use rises on
  "root cause analysis" — investigate before switching the default.

## Notes
- The post does not publish Cresta's rule language, task fixtures, or scoring thresholds; define
  your own. See the original article for context.
