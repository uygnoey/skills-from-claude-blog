---
name: agentic-analytics-warehouse
description: Use this skill when the user asks for business analytics that requires querying a data warehouse (SQL and/or governed semantic layer), and the work must be reliable under entity ambiguity, freshness/staleness risk, and retrieval gaps.
---

# Agentic analytics for data warehouses

## Instructions

### Mental model: analytics is a context + verification problem
Analytics questions often have a single correct answer tied to a specific, up-to-date entity in a data model, so correctness depends on mapping the question to the right entities, sources, and definitions.

### Guardrails for the three dominant failure modes
1. **Concept–entity ambiguity**: clarify what entity and grain the user means.
2. **Data staleness**: confirm the “as-of” point and freshness lag conventions; avoid assuming “yesterday” is available.
3. **Retrieval failure**: always consult the intended sources of truth (semantic layer, lineage graph, governed docs) before writing raw SQL.

### Semantic-layer-first workflow (required)
Follow the warehouse workflow template in:
- `templates/warehouse_skill_skeleton.md`

Use the domain reference-doc format in:
- `references/reference_doc_skeleton.md`

### Validation and reporting
- Separate **observations** (what data shows) from **interpretations** (what it may imply).
- Never invent columns, tables, or results.
- End every final answer with a provenance footer (see the template).

## Examples

- Use `templates/warehouse_skill_skeleton.md` as a starting point for a production warehouse skill.
- Use `references/reference_doc_skeleton.md` to create governed domain reference docs (grain, key tables, gotchas, query patterns, cross-references).

## Source
- https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
