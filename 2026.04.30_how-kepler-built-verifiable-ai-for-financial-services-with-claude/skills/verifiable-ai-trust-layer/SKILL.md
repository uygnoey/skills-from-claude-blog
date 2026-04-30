---
name: verifiable-ai-trust-layer
description: Design an auditable AI system by pairing Claude’s interpretation and reasoning with deterministic retrieval, computation, provenance, and evaluation so every claim can be traced to source.
---

## Purpose
Use this skill to plan an AI workflow for regulated domains where outputs must be verifiable against underlying documents (e.g., financial filings).

## Instructions
1. **Separate responsibilities**
   - Assign Claude to interpretation, ambiguity detection, and planning.
   - Use deterministic components for retrieval, computation, and assembling final outputs so results are provably correct.

2. **Build for provenance and auditability**
   - Ensure each number/claim can be traced to a specific source document and location (page/line item).
   - Maintain audit logs and enforce security/access control at every step.

3. **Engineer the surrounding context**
   - Provide structured domain knowledge: definitions, formulas, and hard boundaries.
   - Maintain an ontology that maps domain concepts to precise definitions (customizable where needed).

4. **Use multi-stage pipelines and match models to stages**
   - Decompose complex workflows into stages (intent decomposition → retrieval → compute → assemble → review).
   - Use higher-reasoning models for ambiguity resolution and plan generation; use faster models for constrained stages.

5. **Invest in evaluation before (and beyond) prompt tuning**
   - Test prompt and model changes against a large set of known-correct cases.
   - Build automated evaluation pipelines that help localize failures (reasoning vs. context vs. execution).

## Examples
### Example: design a verifiable “answer with citations” workflow
User: Build an assistant that answers questions about quarterly results and can be audited.

Assistant:
1. Claude stage: interpret question, list required data points, flag ambiguity (period definitions, restatements).
2. Deterministic stage: retrieve the exact filings and tables, compute metrics, and record provenance for each value.
3. Assembly stage: produce a report where each number links back to the source document location.
4. Evaluation: run the workflow against a regression suite of questions with expected outputs.

## Source
- https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude
