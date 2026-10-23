**English** · [한국어](./agentic-model-evaluation-and-governance.ko.md) · [Español](./agentic-model-evaluation-and-governance.es.md) · [日本語](./agentic-model-evaluation-and-governance.ja.md)

# Evaluating and governing frontier models for agentic work

Methodology from Balyasny Asset Management's account of adopting Claude Fable 5 (September 2026).

## 1. Evaluate before you turn it on
- Use thousands of real tasks with verifiable outcomes from your own domain (BAM: equities, macro, commodities).
- Test the model alone **and** inside your agent harness with the same tools, files, and requirements users have.
- Assess planning, tool selection and use, evidence gathering and analysis, error recovery, intermediate checks,
  and grounded deliverables. Watch for numerical errors, missed coverage, unsupported conclusions, and
  retrieval problems.
- BAM's result: 89.4% for Fable vs 86.1% for the prior production model on the relevant subset.

## 2. Distrust surprising wins until verified
Re-run the eval, check the task and scoring logic independently, and review with the provider before
accepting a result that looks too good.

## 3. Route models by evidence
Break results down by area and use them for model choice and routing. Publish guidance on when to use which
model based on efficiency and cost. Put the strongest model on planning and analysis, where errors propagate.

## 4. Put the controls around the model
| Control | Purpose |
|---|---|
| Approved data boundaries | Agent sees only sanctioned data |
| Least-privilege access | Scoped to the user and task |
| Tool-level permissions | Limits what actions are possible |
| Logging and traceability | Problems can be detected and traced |
| Human review of material outputs | Nobody relies on unreviewed work |
| Escalation paths | Edge cases reach a person |
| Adversarial / failure testing | Done before access widens |

Capability does not confer authority: a better model does not get more access, and cannot grant itself any.
Investment (or business) judgment stays with people.

## 5. Deploy through a governed platform
BAMAgent agents plan, use approved internal systems, run the analysis, check intermediate outputs, and return
a reviewable artifact. The harness (workflow design, data and tool access, retrieval context, permissions,
monitoring, human review) and model reasoning are both needed for production quality.

## 6. Advice for other firms
- Invest early in evals built on real, verifiable tasks; use them for model choice and routing.
- Test in the same environment and with the same tools users will have.
- Treat safety as an operating-model question; controls go around the model.
- Plan a hosted-agent strategy that lets the enterprise enforce policy while maximizing agent value.
- Ask whether there is a better way to reach the outcome, not only how to automate the current process.

Source: https://claude.com/resources/articles/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5
