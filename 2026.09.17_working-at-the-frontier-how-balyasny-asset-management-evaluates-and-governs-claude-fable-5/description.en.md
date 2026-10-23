**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An interview with Charlie Flanagan, Chief AI Officer at Balyasny Asset Management (BAM), published September
17, 2026. It explains how BAM evaluated Claude Fable 5 before turning it on, how it governs agents with
controls around the model, and what its internal agent platform, BAMAgent, has made possible.

## When is it useful?
- Deciding whether to move production agent work to a new frontier model.
- Building an internal eval suite from real, verifiable tasks instead of public benchmarks.
- Defining permissions, logging, and human review before widening agent access in a high-stakes domain.

## Key points
- 2026 is when BAM moved from AI that searches to AI that completes work, driven by agent harnesses such as
  Claude Code.
- Evals: thousands of financial tasks with verifiable outcomes (equities, macro, commodities), run with the
  model alone and inside BAM's agent harness. Fable scored 89.4% vs 86.1% for the prior production model on
  the relevant subset, with the biggest gains in planning, analysis, and agentic execution.
- A surprising result (economics problems no earlier model had solved) was treated as a possible eval flaw:
  re-run, independently checked, and reviewed with Anthropic before acceptance.
- Safety lives in controls around the model: approved data boundaries, least privilege, tool permissions,
  logging, human review of material outputs, escalation paths. A more capable model gets no extra authority;
  investment judgment stays with people.
- BAMAgent runs thousands of autonomous agents. Merger-arbitrage analysis went from three to five days to
  under a day (about 30 minutes of agent time); a central-bank analysis went from about two days to about
  30 minutes, with review retained. Some teams run more than 300 agents.

## Bundled resources
- Skill: `frontier-model-eval-governance` (`references/eval-dimensions.md`, `templates/controls-checklist.md`, `examples/workflows.md`).
- Guide: `guides/agentic-model-evaluation-and-governance` (4 languages).

## Source
- https://claude.com/resources/articles/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5
