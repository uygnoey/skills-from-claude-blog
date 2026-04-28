# Team collaboration scenarios for shareable prompts

The launch post calls out four collaborator roles by name: developers, domain experts, product managers, and QA specialists. These scenarios show how shareable prompts in Console fit each role, derived directly from the post's framing.

## Scenario 1 — Developer hands off a draft to domain experts

A developer drafts a Claude prompt for a regulated workflow. Without shareable prompts, the post says, the developer would resort to "copying and pasting prompts between documents or chat applications, leading to version control issues and knowledge silos."

With shareable prompts:

- The developer publishes the draft to the org's prompt library inside Console.
- Domain experts open it directly in Console, propose wording adjustments, and reuse the same Workbench environment for testing.
- Iteration history stays in Console rather than fragmenting across docs.

## Scenario 2 — Product manager standardizes a prompt across multiple Claude apps

A PM oversees several Claude-powered features that should "feel" consistent. The post highlights that shareable prompts make it "easier to establish best practices and ensure consistent quality across all your Claude-powered applications."

With shareable prompts:

- The PM curates a small library of approved base prompts (tone, refusal rules, formatting).
- Each product team starts from the approved base instead of authoring its own variant.
- Updates to the base ripple through the org, so consistency is maintained without manual sync.

## Scenario 3 — QA specialist owns the evaluation gate

The post pairs QA specialists with developers and domain experts as collaborators on prompts. The Console's evaluation tool gives QA a natural surface: "automatic test case generation and side-by-side output comparison" plus the ability to "run test suites, grade response quality, and make data-driven decisions about which prompts to deploy."

With shareable prompts and the evaluation tool:

- QA opens the shared prompt directly in Console.
- They generate test cases, run the suite, and grade outputs in the same environment where the prompt was authored.
- Sign-off lives next to the prompt, not in a separate ticket.

## Scenario 4 — Cross-functional team adopts extended thinking together

The post emphasizes that Claude 3.7 Sonnet's extended thinking can be optimized inside Console, including setting a max thinking-token budget. Shareable prompts let the cross-functional team agree on that budget together:

- The developer drafts the prompt with extended thinking on.
- The PM reviews the cost / latency implications of the chosen thinking-token budget.
- QA runs side-by-side comparisons of extended-thinking-on vs off to confirm the budget is justified.
- The agreed prompt + budget combination becomes the shared, standardized version in the library.

## Source

Get to production faster with the upgraded Anthropic Console — Anthropic, March 6, 2025: <https://claude.com/blog/upgraded-anthropic-console>
