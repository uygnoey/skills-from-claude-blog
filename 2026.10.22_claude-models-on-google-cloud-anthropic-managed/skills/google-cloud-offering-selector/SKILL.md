---
name: google-cloud-offering-selector
description: Decide between the two ways to run Claude on Google Cloud - Claude Models on Google Cloud (Anthropic managed), generally available since October 22, 2026, and Claude Models on Google Cloud (Google managed) - and plan onboarding for the chosen path. Anthropic managed gives full Claude Platform feature parity with day-zero betas (Managed Agents, code execution, computer use, agent skills, advisor strategy, Files API, citations, web search/fetch, MCP connector, prompt caching, batch processing, Fast Mode on Opus 5.5, Claude Console) behind Google Cloud IAM, one Google Cloud invoice, and commitment drawdown, with Anthropic as data processor and US/Global endpoints. Google managed fits when Google must be the data processor, strict regional data residency applies, or native integrations like Model Armor or Agent Engine are needed. Use when a Google Cloud customer asks which Claude offering to adopt, wants Claude features unavailable on their current path, or is migrating billing and access into Google Cloud.
---

## Purpose
Google Cloud customers can reach Claude through two offerings. This skill turns the October 22, 2026
announcement into a decision procedure and an onboarding checklist, so a team picks the path that fits
its data-processing, residency, and feature requirements before it builds.

## When to use
- A team on Google Cloud wants Claude and must choose Anthropic managed or Google managed.
- A team needs Claude Platform features (betas included) the day they ship, but wants Google Cloud IAM,
  billing, and commitment retirement.
- A team already on Claude via Google Cloud asks whether to move or stay.

## Instructions

1. **Gather requirements.** Fill in [templates/offering-decision.md](templates/offering-decision.md):
   who must be the data processor, regional residency rules, needed Google Cloud integrations, and the
   Claude Platform features the workload depends on.
2. **Apply the decision rule.**
   - Choose **Google managed** if any hold: Google Cloud must be the data processor; strict regional
     data residency is required; native Google Cloud integrations such as Model Armor or Agent Engine
     are required.
   - Otherwise choose **Anthropic managed** when the team wants day-zero access to all beta and GA
     Claude Platform features with full feature parity, accessed through Google Cloud. Anthropic
     operates the service and is the data processor.
3. **Check endpoint fit.** Anthropic managed is currently available with **US and Global endpoints**
   only. If the workload needs another region, it does not fit today.
4. **Map features.** Compare the workload's needs with
   [references/feature-matrix.md](references/feature-matrix.md) (agents, knowledge/integration,
   cost/performance, Fast Mode, Console, models).
5. **Handle commercial terms first.** If the organization has an existing discount, contact the
   Anthropic or Google Cloud account executive **before** starting on Anthropic managed. Discounts
   cannot be applied retroactively to usage.
6. **Onboard.** Open the Google Cloud Marketplace listing "Claude Models on Google Cloud (Anthropic
   managed)" and follow the official documentation. Reuse existing Google Cloud IAM credentials and
   permissions; usage is billed on a single Google Cloud invoice and draws down the existing Google
   Cloud commitment.
7. **Use the Console.** Anthropic managed customers also get the Claude Console to write prompts,
   configure agents and run them on hosted environments, monitor usage and costs, and manage access
   and security per workspace.
8. **Record the decision** with the reason (processor, residency, integrations, features) so it can be
   revisited when requirements change.

## Examples

**Example 1 - agent builder needing new features fast.**
Input: "We build enterprise assistants, need new Claude capabilities on day one, and want our existing
IAM and Google Cloud commitment to apply."
Output: Anthropic managed. No processor/residency constraint; day-zero features; IAM reuse; usage
counts toward the commitment. Check that US or Global endpoints suffice; contact the account executive
first if a discount exists.

**Example 2 - cost-sensitive production harness.**
Input: "Our harness depends on prompt caching to stay cost-effective, and we want billing and access
through Google Cloud."
Output: Anthropic managed keeps prompt caching (and batch processing) on the same Claude API while
billing and access run through Google Cloud.

**Example 3 - regulated workload with residency.**
Input: "Legal requires Google as data processor and data must stay in one region; we also use Model
Armor."
Output: Google managed. Each of the three conditions alone points there.

## Bundled resources
- [references/feature-matrix.md](references/feature-matrix.md) - what the Anthropic managed offering
  includes and how the two offerings differ.
- [templates/offering-decision.md](templates/offering-decision.md) - requirement checklist and decision
  record.

## Source
- https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed
- Docs: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed
