---
name: foundry-azure-deployment-choice
description: Decide whether to run Claude via Microsoft Foundry hosted on Azure or hosted on Anthropic, based on Azure-native requirements vs. needing full API feature/model availability.
---

## Instructions
Use this skill to turn the post’s product guidance into a repeatable decision check for teams adopting Claude through Microsoft Foundry.

1) **Confirm your baseline requirement**
- If you need Claude to run in your **Azure environment** with Azure authentication, billing, and governance controls, prefer **hosted on Azure**.

2) **Check for feature/model requirements**
- If you need **the full set of API features** or a **model that is not yet available on Azure**, choose **hosted on Anthropic** (previously “Foundry Preview”).

3) **Record operational constraints**
- If you have data residency needs, note that the post mentions the ability to choose where inference is processed, including a **US data zone**.
- If you need consolidated billing, note that the post states you get a **single consolidated invoice**, and eligible Microsoft Enterprise Agreement customers can draw usage down from an **Azure commitment**.

4) **Pick the starting configuration**
- Start with the hosting option that meets your constraints today, and reassess as Microsoft Foundry expands over time.

## Examples
### Example: strict Azure-native requirement
- Requirement: Use existing Azure identity/governance and keep inference in Azure.
- Decision: **hosted on Azure**.

### Example: need a feature/model not yet available on Azure
- Requirement: Use a specific model or API feature not available on Azure-hosted Foundry.
- Decision: **hosted on Anthropic**.

## Source
- https://claude.com/blog/claude-in-microsoft-foundry
