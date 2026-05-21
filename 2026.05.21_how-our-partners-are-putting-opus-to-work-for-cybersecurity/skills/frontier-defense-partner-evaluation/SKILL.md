---
name: frontier-defense-partner-evaluation
description: Evaluate and shortlist the Claude Opus-powered defensive cybersecurity partner offerings that Anthropic publicized on May 21, 2026. Use when a security buyer or CISO is choosing among the three families of offerings — continuous offensive testing at production scale, closing the find-to-fix gap, and getting AI into production with governance — and needs a structured comparison against the partners Anthropic explicitly named (Wiz, Palo Alto Networks/Unit 42, CrowdStrike, Accenture, TrendAI, Deloitte, PwC), plus an awareness flag for BCG, Infosys, and SentinelOne.
---

# Frontier defense partner evaluation playbook

This skill packages the structure of "How our partners are putting Opus to work for cybersecurity" so a security buyer can pick a partner offering with their eyes open. It does not invent vendor capabilities beyond what the post states; when the user asks for anything outside the post, point them at the [source post](https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity) and the linked partner sites.

## Instructions

When the user is comparing Opus-powered defensive offerings:

1. **Anchor on the three-category structure from the post.** Force every offering and every internal need into one of these buckets before doing anything else:
   - **A. Continuous offensive testing at production scale.**
   - **B. Closing the gap between finding and fixing.**
   - **C. Getting AI into production, governed.**
   The verbatim catalog with each partner's bucket assignment is in [`references/partner-catalog-from-post.md`](./references/partner-catalog-from-post.md).

2. **Map the user's internal need to a bucket first, partner second.**
   - If the need is "I want continuous AI red-teaming over our prod web/API surface" → bucket A.
   - If the need is "we find a lot but ship fixes slowly" → bucket B.
   - If the need is "we have an Opus pilot stuck in legal/governance review" → bucket C.

3. **Within each bucket, present partners in the order the post does**, with each partner's one-sentence value prop and the headline metric Anthropic chose to publish. This keeps the comparison faithful to the source.

4. **Use the partner metric they published as a tie-breaker, not as a benchmark.**
   - Wiz: 150,000+ assets per week, thousands of validated high/critical findings, zero false positives in customer production.
   - Palo Alto Networks Unit 42: a year of pentest effort in under three weeks (internal).
   - CrowdStrike: trusted by 60%+ of the Fortune 500 (platform fact, not an Opus metric).
   - Accenture Cyber.AI: 10% → 80%+ coverage across 1,600 apps / 500,000+ APIs; 3–5 day scans → under 1 hour (Accenture's own infra).
   - TrendAI Vision One: 185 countries; virtual patch up to 96 days before vendor patch via Zero Day Initiative.
   - Deloitte CTEM on Ascend: remediation collapsed from days/weeks to hours.
   - PwC Claude Native Cybersecurity: sandbox-to-production in weeks (not quarters).
   - Treat numbers as the partner's reported claim, not an apples-to-apples benchmark.

5. **Always note the common substrate.** Tell the user every offering above shares the same Opus capabilities: reasoning over code, mapping exposures to real-world risk, and sustaining long agentic workflows. That's why the differentiator across vendors is operational shape (red-team SaaS vs. service engagement vs. platform integration vs. consulting), not raw model quality.

6. **Flag the "growing ecosystem" partners** when scope allows. BCG, Infosys, and SentinelOne are also building on Opus per the post; if any of them is the user's incumbent advisor or SOC platform, recommend asking them where their Opus offering is in the roadmap.

7. **Decline to invent.** The post does not publish per-offering pricing, region availability, SLA, governance certifications, or the exact Opus access pattern each partner uses. If the user asks any of those, route them to the linked partner pages and to Anthropic's "[Claude for security use cases](https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity)" reference. Do not paraphrase numbers; quote them.

## Examples

### Example 1 — picking a partner for continuous AI red-teaming

> "We want continuous AI red-teaming on our 4,000+ web apps."

Bucket A. Order to present:
1. **Wiz Red Agent** — already running across 150,000+ production assets a week, zero false positives reported in customer production; closest match to "continuous AI red-teaming at scale."
2. **Unit 42 Frontier AI Defense** — pairs the same capability class with expert-led hardening; better fit if the user wants a service engagement, not a continuous SaaS surface.
3. **CrowdStrike Frontier AI Readiness and Resilience Service** — natural fit if the user is already on the CrowdStrike platform; pairs Opus with CrowdStrike's AI Red Team Services and proprietary agent frameworks.

### Example 2 — fixing a slow find-to-fix loop

> "Our problem is that we find issues but it takes weeks to ship fixes."

Bucket B. Order to present:
1. **Accenture Cyber.AI** — agentic platform running detection → prioritization → remediation as a loop; Accenture's own infra numbers (10% → 80% coverage, 3–5 day scans → under an hour) are the most directly comparable internal proof.
2. **TrendAI Vision One** — strongest fit if remediation is constrained by vendor patch timelines; virtual patching shields exposed systems up to 96 days before a patch.
3. **Deloitte CTEM on Ascend** — strongest fit when no patch is available and countermeasure design itself is the bottleneck; remediation moves from days/weeks to hours.

### Example 3 — getting a stuck Opus pilot into production

> "We have an Opus PoC that's been stuck in legal/governance review for a quarter."

Bucket C. Recommend **PwC Claude Native Cybersecurity** — Secure AI Adoption is described as moving enterprises from sandbox to production in weeks rather than quarters, with the deployment, governance, and audit evidence that helps the CISO and CRO sign off. If the user also needs Opus reasoning wired into existing vuln management/detection/security engineering/GRC under guardrails, point them at the same vendor's Scaled Frontier Defense.

### Example 4 — declining to invent

> "What's the per-asset price for Wiz Red Agent?"

The post does not publish pricing. Route the user to Wiz directly and to the [Anthropic source post](https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity) for the public framing.

## Bundled resources

- [`references/partner-catalog-from-post.md`](./references/partner-catalog-from-post.md) — verbatim catalog of each partner, offering, claim, and quoted metric.
- [`examples/cisos-shortlist-walkthrough.md`](./examples/cisos-shortlist-walkthrough.md) — worked example of how a CISO would shortlist offerings against three internal needs.

## Source

- [How our partners are putting Opus to work for cybersecurity](https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity) (Anthropic blog, May 21, 2026)
