---
name: legal-artifact-workflows
description: Run legal work in Claude with the ready-to-use legal artifacts announced in October 2026 for Claude for Legal - cite check, jurisdiction survey matrix, matter board, playbook deviation board, regulatory horizon scan, and tabular review, plus partner artifacts (Goodwin, Harvey, Foley & Lardner, PwC) and access-to-justice artifacts. Covers opening an artifact from the legal gallery, tailoring it to a team, wiring in playbooks and research sources through legal connectors instead of manual uploads, sharing it with colleagues, clients, or partners under privacy and ethical-wall settings, and keeping a lawyer's judgment on top of Claude's sourced first pass. Use when a legal team wants a tracker, dashboard, or review table it can reuse and share, or is planning a Claude for Legal rollout.
---

## Purpose
The source announces a legal gallery of interactive artifacts (trackers, dashboards, review tables) in
Claude for Legal. The working pattern is the same for every artifact: the legal professional brings their
own documents and sources, Claude completes the first pass with each answer linked to its source, and a
lawyer applies judgment to the result. This skill turns that pattern into steps. Anything beyond what the
post states (plan availability, exact settings names) is left to the original and the Claude for Legal page.

## When to use
- You need to review a stack of contracts, check citations, survey a rule across jurisdictions, track open
  matters, or watch upcoming regulations, and want a reusable tool instead of a one-off answer.
- You want business colleagues to send legal requests through one place in Claude.
- You need to share legal work product inside the company or with clients and partners without breaking
  privacy rules or ethical walls.
- You work in legal aid or public interest law and want a starting tool for record clearance, eviction,
  immigration, or criminal defense work.

## Instructions

1. **Pick the artifact that matches the job.** Browse the legal gallery in Claude
   (`https://claude.ai/artifacts?templates=legal`) or start from the Claude for Legal page. Match the task to
   an artifact in [references/gallery-artifacts.md](references/gallery-artifacts.md). Partner-built and
   access-to-justice artifacts are listed in
   [references/partner-and-access-to-justice-artifacts.md](references/partner-and-access-to-justice-artifacts.md).
2. **Run the built-in example first.** Every artifact opens with an example. Read it to see how inputs,
   outputs, and source links fit together before adding your own material.
3. **Connect sources instead of uploading.** Use legal connectors to bring in playbooks, contract
   repositories, and research sources so nobody has to upload documents by hand. The post counts more than
   60 legal connectors; see [references/connectors-and-rollout.md](references/connectors-and-rollout.md).
4. **Tailor the artifact to your team.** Ask Claude to adapt it: your standard terms, your approver for
   exceptions, your jurisdictions, your matter fields. Request patterns are in
   [templates/tailoring-requests.md](templates/tailoring-requests.md).
5. **Treat the output as a first pass.** Each answer or output links to its source. Open the links, confirm
   the language, and apply legal judgment before anything leaves the team.
6. **Share with guardrails.** Decide who sees the artifact (colleagues across the business, clients,
   partners) and set sharing so privacy holds and ethical walls between teams stay in place. Walk through
   [templates/sharing-checklist.md](templates/sharing-checklist.md) before sharing.
7. **Plan a wider rollout if needed.** Talk to the sales team or an implementation partner (listed in the
   connectors and rollout reference). Legal professionals who build with Claude can join the Legal
   Ambassadors Program waitlist to learn from peers.

## Examples

**Contract stack review**
> A legal team connects its contract repository and opens Tabular review. It asks for a table of
> severance and non-compete terms across the set. Each cell links to the exact contract language, and a
> lawyer checks the flagged rows.

**Playbook deviations routed to an approver**
> The team tailors the Playbook deviation board with its standard terms from a connected playbook. Each
> clause that differs is flagged and sent to the person who approves exceptions.

**Cite check before filing**
> A lawyer runs Cite check on a brief. It flags quotes that don't match the source, wrong page numbers, and
> sources that don't support the claim. The lawyer fixes them before filing.

**Legal intake for the business**
> Business users send legal questions through Harvey Intake in Claude. Routine ones are answered from
> Legal's own guidance in Harvey; the rest go to a lawyer, whose reply comes back in Claude.

More scenarios, including access-to-justice tools and what partners said, are in
[examples/scenarios.md](examples/scenarios.md).
