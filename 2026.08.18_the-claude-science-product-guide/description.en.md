**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement of the Claude Science product guide, a practical deployment guide for life sciences organizations. The post summarizes the guide and links to the full PDF.

Claude Science (in beta) is described as an application for every digital step of life science, built to run next to the scientist's data and produce results that can be traced, reproduced, and defended. The guide covers which Claude surface to reach for when, how Claude Science works underneath, the design choices that make its analysis hold up under review, a three-phase adoption roadmap, function and workflow use cases, and a FAQ for CIOs and IT leaders.

## When is it useful?
- When a research organization is deciding which Claude surface fits which kind of scientific work — analysis versus document work versus production pipelines.
- When Research IT needs to review the install footprint, sandbox, network allowlist, and compute-dispatch targets before scientists point a tool at controlled data.
- When planning a staged rollout across computational groups rather than an org-wide switch-on.
- When results need to be reproducible and defensible for a publication, a regulatory submission, or an internal review.

## Key points
- **Surface selection comes first.** Claude Science for analysis, figures, and results; Claude Chat for quick queries and drafting; Claude Cowork and Claude for Microsoft 365 for study- and submission-level document work; Claude Code when the output is software that ships; Claude Platform and Claude Managed Agents for embedded and hosted agents. Most organizations deploy more than one.
- **It runs where the data is.** A local daemon on macOS or Linux — a laptop, a lab Linux box, an HPC login node, or a cloud VM — with the UI in the browser. Heavy jobs dispatch from the same session to an SSH host, a SLURM cluster (batch directives written automatically), or a serverless GPU account.
- **Domain capabilities ship on day one**: configurable capabilities for common scientific workflows, optional connections to more than sixty scientific databases, and roughly 150 curated skills. Because the skills run code rather than retrieve documents, they can be chained inside one analysis, and each is open source so teams can inspect, pin, or extend it.
- **Five design choices make the analysis reviewable**: persistent kernels (agents also see their own plots), four-layer provenance on every artifact (description, code, conversation, environment snapshot), a background reviewer agent that flags claims it cannot trace to evidence, plan-before-action with a visible permission model, and built-in biosecurity safeguards.
- **A three-phase roadmap**: Foundation (IT and data-governance review, daemon host pattern, 2–3 champion groups, SSO/SCIM, admin enablement), Pilot (real analyses on real lab data, weekly check-ins, cycle time / keep-rate / cold-reproduce metrics), Scale (managed daemon host pattern, curated org skill catalog, vetted allowlist, provenance-retention policy).
- **The pilot signal to watch for is champions saving their own skills** — a lab's internal normalization pipeline or LIMS API wrapped once so every future session inherits it.
- **Skills versus connectors**: a connector when the answer lives in the organization's own systems and entitlements matter; a scientific data skill when the answer lives in the public record. Most real questions use both.
- **Known limits are stated plainly** in the guide: research use only and not for clinical or diagnostic decision-making, not a validated system for GxP, not HIPAA-ready at launch, no Windows support, not available through Bedrock / Vertex AI / Foundry, no Zero Data Retention, and NIH controlled-access compliance on the roadmap.

## Bundled resources
- `skills/life-sciences-ai-rollout/SKILL.md` — how to plan and run a staged rollout of an AI research workbench.
- `skills/life-sciences-ai-rollout/references/surface-selection.md` — the product matrix: which surface for which work.
- `skills/life-sciences-ai-rollout/references/product-architecture.md` — local daemon, compute dispatch, and the five design choices.
- `skills/life-sciences-ai-rollout/references/scientific-data-skills.md` — the skill catalog grouped by the question it answers.
- `skills/life-sciences-ai-rollout/references/it-security-faq.md` — the CIO and IT-leader FAQ.
- `skills/life-sciences-ai-rollout/templates/adoption-roadmap.md` — the phase-by-phase rollout plan template.
- `skills/life-sciences-ai-rollout/templates/pilot-scorecard.md` — the pilot measurement sheet.
- `skills/life-sciences-ai-rollout/examples/workflow-use-cases.md` — use cases across discover, analyze, and publish.
- `guides/life-sciences-deployment.{en,ko,es,ja}.md` — the full deployment guide in four languages.

## Source
- https://claude.com/blog/the-claude-science-product-guide
