---
name: frontier-model-eval-governance
description: Evaluate a new frontier model on real, verifiable domain tasks inside your own agent harness, validate surprising results, route models by evidence, and govern agent deployments with controls around the model (capability never grants authority). Follows the pattern Balyasny Asset Management (BAM) described in September 2026 for Claude Fable 5 and its BAMAgent platform. Use when deciding whether to switch a production model, designing an internal eval suite, setting model routing guidance, or defining the guardrails and human review for long-running agents in a regulated or high-stakes domain.
---

## Purpose
BAM's Chief AI Officer describes how the firm evaluated Claude Fable 5 before turning it on and how it
governs thousands of autonomous agents. The two halves are linked: evals decide *which* model does *which*
work; controls decide *what any model is allowed to do*. This skill turns that into a repeatable procedure.
Numbers and specifics below come from the post; anything beyond it is left to your organization.

## When to use
- A new model is released and you must decide whether to adopt it for production agent work.
- You are building an internal eval suite instead of relying on public benchmarks.
- You need written guidance on which model to use for which task (quality, efficiency, cost).
- You are widening agent access to data and tools and need a control checklist first.

## Instructions

### Part 1 - Evaluate on your own work
1. **Build the task set from real work with verifiable outcomes.** BAM uses thousands of financial tasks
   across equities, macro, and commodities rather than general benchmarks or isolated demos. Tag each task
   by area so results can be broken down.
2. **Run every candidate two ways**: the model alone, and inside your agent harness with the same tools,
   files, and requirements real users have.
3. **Score the agentic dimensions, not just the final answer.** See
   [references/eval-dimensions.md](references/eval-dimensions.md) for the capabilities and failure modes
   the post lists (planning, tool use, evidence, error recovery, intermediate checks, grounded deliverables;
   numerical errors, missed coverage, unsupported conclusions, retrieval problems).
4. **Compare against the current production model on the relevant subset.** BAM reported 89.4% for Fable vs
   86.1% for the prior production model, with the largest gains in complex planning, analysis, and agentic
   execution.
5. **Treat a surprising jump as a possible eval bug first.** When Fable solved economics problems no prior
   model had, BAM re-ran the eval, independently checked the task and scoring logic, and reviewed the result
   with Anthropic before accepting it.
6. **Turn results into routing guidance.** Decide default models per kind of work and publish when to use
   which model based on efficiency and cost (BAM's investment teams default to Fable for systematic and
   coding work). Put the stage where errors compound - planning and analysis - on the strongest model.

### Part 2 - Govern with controls around the model
7. **Frame safety as a product and operating-model question**, not a one-time model pick: what data the
   agent can access, which tools it can use, which actions it may take, which steps need human approval,
   and how problems would be detected.
8. **Apply the control set** in [templates/controls-checklist.md](templates/controls-checklist.md):
   approved data boundaries, least-privilege access, tool-level permissions, logging and traceability, human
   review of material outputs, escalation paths, and adversarial/failure testing before broadening access.
9. **Capability does not confer authority.** A model upgrade never widens permissions by itself; the model
   may use only the data and tools approved for that user and task and cannot grant itself more access.
10. **Keep judgment with people.** Material outputs are reviewed by a human before anyone relies on them;
    responsibility for the decision stays with people. Governance matters more as agents run longer and
    more autonomously.

### Part 3 - Deploy through a governed agent platform
11. Shape each workflow as: plan -> use approved internal systems -> run analysis -> check intermediate
    outputs -> return a reviewable artifact (research package, model, or decision-support pack). BAM built
    the harness, data access, and review controls in-house; the post treats model reasoning and harness as
    both necessary.
12. **Ask whether there is a better way to reach the outcome**, not only how to automate today's process.
    Worked examples with timings are in [examples/workflows.md](examples/workflows.md).

## Examples

**Adoption decision**
> New model released. Run the 2,000-task internal suite standalone and in-harness. Relevant subset: new
> 89.4% vs current 86.1%; gains concentrated in planning. One category jumps from 0 to solved - re-run,
> audit task and scorer, confirm with vendor, then accept. Routing note: new model becomes default for
> planning/analysis steps; cheaper model kept for simple extraction.

**Permission review on upgrade**
> Request: "The new model is better, give the agent write access to the trading database."
> Answer: No. Permissions are tied to the user and task, not to model capability. Keep read-only access;
> route any write action through human approval and log it.

**Agent workflow**
> Deal announced -> agent estimates closing likelihood and timing, extracts key economic/legal terms,
> lists conditions and milestones, flags points needing investor judgment -> analyst reviews before use.
