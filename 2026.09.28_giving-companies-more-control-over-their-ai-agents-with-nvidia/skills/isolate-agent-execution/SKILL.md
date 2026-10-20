---
name: isolate-agent-execution
description: Design a secure execution setup for AI agents by splitting the "brain" (harness, session state, credentials) from the "hands" (a sandbox used only for execution), running tool calls in a self-hosted sandbox inside your own perimeter, and governing that sandbox with a default-deny policy runtime such as NVIDIA OpenShell that is tightened from its decision log toward least access. Use when building or reviewing agents that clone repos, read websites, parse tool output, or install packages, especially on Claude Managed Agents or in regulated environments.
---

## Purpose
Agents routinely pull untrusted content into their execution environment — cloned repos, web pages,
tool output, installed packages. Any of it can carry text a model might follow as instructions
(prompt injection) or code that runs. This skill applies the architecture the post describes: keep
what matters out of the sandbox, keep the sandbox inside your perimeter, and constrain what the
sandbox can reach with rules enforced outside the agent.

## When to use
- Designing a new agent that executes code or touches untrusted inputs.
- Reviewing an existing agent where credentials or session state live next to executed code.
- Moving a Claude Managed Agents workload into an enterprise or regulated environment.
- Deciding how narrow an agent's file, network, and data access should be.

## Instructions

1. **Split the brain from the hands.** List where the harness, session state, and credentials live.
   Move them to durable infrastructure *outside* the sandbox. The sandbox should be just a tool the
   agent uses for execution. The post calls this the easy first step.

2. **Choose where execution runs.** With Claude Managed Agents self-hosted sandboxes, the agent loop
   (orchestration, context management, error recovery) stays on Anthropic's infrastructure while
   each session's tool calls run in an environment you control — your own infrastructure or a
   managed sandbox provider. Confirm that code execution, sensitive files, packages, services, and
   data stay within your perimeter under your own security and runtime controls.

3. **Pick the isolation boundary that fits your risk.** Examples from the post: a sandbox that can
   mount external file stores and install packages on the fly (Clay's Sculptor), or isolated microVMs
   that keep code and data inside the company perimeter for regulated customers (Rogo).

4. **Put a default-deny policy runtime in the sandbox.** NVIDIA OpenShell can serve as the sandbox
   runtime: it blocks everything unless a rule allows it, checks each tool the agent tries to use,
   applies rules to files, network connections, and data, enforces them outside the agent, and logs
   every allow/block decision.

5. **Start narrow, then tighten from the log.** Begin with narrow permissions, review the decision
   log, and use Claude to help refine the rules toward the least access the task needs.

6. **Prove what the agent can reach.** Use OpenShell's policy prover, which uses mathematical proof to
   confirm what the agent can reach under the rules you wrote. Re-run it whenever rules change.

7. **Record the design** with the checklist in
   [references/architecture-checklist.md](./references/architecture-checklist.md).

## Examples

**Coding agent that clones customer repos**
- Brain: harness, session state, and Git credentials stay outside the sandbox.
- Hands: a self-hosted sandbox runs builds and tests; OpenShell allows the package registry and the
  repo host only, denies everything else, and logs decisions.
- After a week of logs, rules are narrowed with Claude's help and checked with the policy prover.

**Regulated-industry analysis agent**
- Each session's code runs in an isolated microVM inside the company's perimeter, so code and data
  never leave it — the pattern the post attributes to Rogo.

## Notes
- Claude Managed Agents was in public beta at publication; NVIDIA OpenShell is open source under
  Apache 2.0. See the Managed Agents docs and cookbooks for sandbox-provider setup (original post).
- Source: https://claude.com/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia
