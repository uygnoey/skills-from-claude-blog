**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement that Anthropic is working with Millennium, one of the world's largest alternative investment management firms, to co-develop a *digital risk analyst*: an AI teammate that works alongside and under the supervision of the firm's risk managers, surfacing new risk insights and forming opinions on risk exposure across asset classes.

Millennium already uses Claude and Claude Code broadly — from trading desks and engineering to core business functions, including across many of its 340+ investment teams. The digital risk analyst extends that use by helping risk managers expedite and enrich the analysis of risk positions. It is being built by Millennium's risk experts together with Anthropic's research and applied AI teams, working alongside them in Millennium's internal AI lab.

## When is it useful?
- When an analyst-style agent has to operate in a regulated or high-stakes domain where every output must be traceable back to its reasoning.
- When the question is not "can the model answer?" but "what does a human have to approve before an answer counts?"
- When domain analysis depends on proprietary data the model has never seen, and on judgment the firm does not want to delegate.
- When explaining *change over time* — why today's numbers differ from yesterday's — matters more than a one-off answer.
- When deciding how to structure an internal AI lab that pressure-tests frontier models against ambitious use cases.

## Key points
- **The agent is a teammate, not a replacement.** It works alongside and under the supervision of risk managers; human judgment stays at the center of decision making.
- **Proprietary data plus frontier reasoning.** The analyst is powered by Millennium's proprietary data combined with Claude's frontier intelligence, aimed at critical risk workflows.
- **Memory serves continuity.** The analyst retains and recalls information over time, which is what lets it explain daily risk changes rather than answer each question from scratch.
- **Human validation is a step in the workflow.** Findings are validated and enriched by Millennium's human risk managers before they count.
- **Three controls make the analysis auditable:** it logs its reasoning, tests its actions in sandboxed environments, and requires human experts to evaluate and approve its decisions.
- **Co-development happens in a shared lab.** Anthropic's research and applied AI teams work alongside Millennium's risk experts in the firm's AI lab, which also pressure-tests the latest models against ambitious use cases.
- **The stated goal is time.** Risk managers use frontier intelligence to deliver automated recommendations, with the goal of saving valuable time — as quoted in the post.

## Bundled resources
- `skills/supervised-risk-analyst/SKILL.md` — how to build an analyst agent that works under human supervision in a high-stakes domain.
- `skills/supervised-risk-analyst/references/auditability-controls.md` — the three controls (reasoning log, sandboxed actions, human approval) written out as requirements.
- `skills/supervised-risk-analyst/templates/analyst-charter.md` — a charter for scoping what such an agent owns and where a human must sign off.
- `skills/supervised-risk-analyst/examples/daily-risk-change-review.md` — the "explain today's risk change" workflow walked through.

## Source
- https://claude.com/blog/millennium-and-anthropic-are-building-a-digital-risk-analyst-with-claude (August 6, 2026)
