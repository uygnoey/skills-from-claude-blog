---
name: web-search-use-case-playbook
description: Apply Claude's web search feature (announced March 20, 2025, made globally available May 27, 2025) effectively. Helps users decide when web search is the right tool, enable it correctly with Claude 3.7 Sonnet, get cited responses, and reuse the four use cases the post calls out — sales, finance, research, and shopping.
---

# Claude web search use case playbook

This skill turns the March 20, 2025 launch post into a playbook for getting useful, cited answers out of Claude's web search feature.

## Instructions

### 1. Decide whether the question actually needs the web

Web search adds value when the answer depends on information that is recent, public, and citable. The post frames the feature this way:

> "Claude can now search the web to deliver up-to-date, cited information in conversational responses across all plans."

Use web search when:

- The answer hinges on recent events, prices, filings, or releases.
- You want a citation alongside the answer for fact-checking.
- The question is closer to one of the four post-named use cases (sales, finance, research, shopping) than to a generic knowledge question.

Do not assume web search helps for purely reasoning, coding, or stylistic tasks; the post does not claim wins there.

### 2. Enable web search before starting the conversation

The post's setup instructions are explicit:

> "To get started, toggle on web search in your profile settings and start a conversation with Claude 3.7 Sonnet. When applicable, Claude will search the web to inform its response."

Workflow:

- Open profile settings and toggle web search on.
- Start the conversation with Claude 3.7 Sonnet.
- Phrase the request so it cues recency or sourcing (see step 4).

### 3. Confirm rollout coverage for your audience

The post documents two stages of rollout:

- Initial: feature preview for paid Claude users in the United States; support for free-plan users and additional countries is coming soon.
- May 27, 2025 update: web search is available globally on all Claude plans.

If you are advising a colleague or building docs, cite the most recent state. The May 27, 2025 update supersedes the initial paid-US-only rollout.

### 4. Phrase requests so Claude reaches for the web

The post says Claude searches "when applicable" — so user phrasing matters. Patterns that align with the post's framing:

- Mention recency explicitly ("as of this week", "current", "latest").
- Ask for sources or citations ("with citations", "include sources").
- Pose the question as a research / comparison task that fits one of the four post-named use cases.

Concrete examples for each role are in [examples/prompt-patterns-by-role.md](./examples/prompt-patterns-by-role.md).

### 5. Verify the citations

The post emphasizes citations as the trust mechanism:

> "When Claude incorporates information from the web into its responses, it provides direct citations so you can easily fact check sources."

Treat the cited links as the primary deliverable, not a decorative footer. If a citation looks shaky, rerun the question with a more specific prompt before quoting Claude downstream.

### 6. Map the request to one of the four post-named use cases

The post explicitly lists four "popular ways to use Claude with web search." Treat them as your default starting templates:

- Sales — analyze industry trends to learn key initiatives and pain points; transform account planning and improve win rates.
- Financial analysts — assess current market data, earnings reports, and industry trends; inform financial-model assumptions.
- Researchers — build stronger grant proposals and literature reviews by searching primary sources, spotting trends, and identifying gaps.
- Shoppers — compare product features, prices, and reviews across multiple sources for purchase decisions.

The verbatim wording of these four use cases is in [references/use-cases-from-post.md](./references/use-cases-from-post.md).

## Examples

### Example A: Pre-call account research (Sales)

Prompt pattern: "Search the web for the latest initiatives, hires, and pain points at <Account>. Cite primary sources from the past 90 days."

This matches the sales use case the post names: "analyzing industry trends to learn key initiatives and pain points" to "transform account planning and drive higher win rates."

### Example B: Quarterly assumptions update (Finance)

Prompt pattern: "Search the web for <Company>'s most recent earnings report and the current consensus on <metric>. Provide citations to the filings and analyst notes."

This matches the financial-analyst use case: assessing "current market data, earnings reports, and industry trends to make better investment decisions and inform financial model assumptions."

### Example C: Literature review starter (Research)

Prompt pattern: "Search the web for the most-cited recent papers on <topic> and summarize emerging trends and gaps. Provide direct citations to the primary sources."

This matches the researcher use case: building "stronger grant proposals and literature reviews by searching across primary sources on the web, spotting emerging trends and identifying gaps in the current literature."

### Example D: Comparison shopping (Shopping)

Prompt pattern: "Search the web to compare features, current prices, and recent reviews of <Product A> vs <Product B>. Provide citations to retailer pages and trusted reviews."

This matches the shopper use case: comparing "product features, prices, and reviews across multiple sources to make more informed purchase decisions."

## Source

Claude can now search the web — Anthropic, March 20, 2025 (updated May 27, 2025): <https://claude.com/blog/web-search>
