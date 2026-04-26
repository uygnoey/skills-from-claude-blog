---
name: performance-optimization-playbook
description: Diagnose and optimize code performance by choosing the right Claude workflow (quick function-level analysis vs. project-wide Claude Code changes) and applying a repeatable performance triage loop.
---

## Instructions

You are helping a developer improve code performance.

1. **Clarify the symptom**
   - What is slow (endpoint, job, UI screen, query)?
   - What changed recently (deploy, config, dependency update, data volume)?
   - What is the target (p95 latency, throughput, memory)?

2. **Choose the workflow**
   - Use the **chat workflow** when the problem is contained to a small snippet (roughly tens of lines) and you want fast complexity analysis and a rewrite proposal.
   - Use **Claude Code** when the issue spans multiple files, requires coordinated refactors, or you want changes applied and tests run.

3. **Function-level analysis (chat workflow)**
   - Identify algorithmic complexity (e.g., nested loops, repeated scans).
   - Look for I/O inside loops (database/network calls).
   - Propose an improved approach (hash map lookup, batching, caching, reduced allocations).
   - Provide an optimized version that preserves behavior.

4. **Project-wide optimization (Claude Code workflow)**
   - Start in the most performance-critical directories (e.g., `api/`, `core/`).
   - Ask for a hypothesis about the regression and where to measure.
   - Apply the smallest safe change first.
   - Re-run benchmarks/tests after each change.

5. **Document the result**
   - What bottleneck was found?
   - What change fixed it?
   - What measurement proves improvement?

Bundled references:
- templates/performance-triage-questions.md
- examples/dashboard-function-optimization.md

## Examples

### Example 1: Ask for function-level optimization
Use the prompt in `examples/dashboard-function-optimization.md`.

### Example 2: Ask Claude Code to optimize a performance-critical area
In Claude Code, run a request like:

- Optimize this payment processing function and benchmark results

(If you need a fuller prompt structure, use `templates/performance-triage-questions.md`.)
