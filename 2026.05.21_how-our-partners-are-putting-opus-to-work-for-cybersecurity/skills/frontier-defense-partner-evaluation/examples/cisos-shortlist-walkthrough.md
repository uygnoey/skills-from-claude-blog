# Worked example — CISO shortlist walkthrough

A representative CISO at a US-listed enterprise has three internal needs sitting in their queue. This example walks the skill's three-bucket method against those needs using only what is in the source post.

## Need 1 — "We have no continuous red-teaming over our production web/API surface."

Bucket → **A. Continuous offensive testing at production scale.**

Shortlist (in the order the post presents them):

1. **Wiz Red Agent** — the closest match if the CISO wants a continuous SaaS-shaped surface. Reported scale: 150,000+ production assets per week with zero false positives in customer production.
2. **Palo Alto Networks Unit 42 Frontier AI Defense** — if the CISO would rather buy an expert-led engagement plus a hardening roadmap than a continuous platform.
3. **CrowdStrike Frontier AI Readiness and Resilience Service** — if the firm is already standardized on CrowdStrike; pairs Opus with CrowdStrike's AI Red Team Services and proprietary agent frameworks.

Open question to take into vendor conversations: "Walk me through how findings are de-duplicated against my own SAST/DAST and ticketing today." The post does not answer this.

## Need 2 — "Findings pile up; we ship fixes too slowly."

Bucket → **B. Closing the gap between finding and fixing.**

Shortlist:

1. **Accenture Cyber.AI** — closest match if the bottleneck is detection-to-remediation orchestration across many apps and APIs. Cite Accenture's own infra numbers (10% → 80%+ coverage across 1,600 apps and 500,000+ APIs; 3–5 day scans cut to under an hour) as the precedent they are willing to be measured against.
2. **TrendAI Vision One** — strongest fit when remediation is gated by vendor patch availability; virtual patching shields exposed systems up to 96 days before a vendor patch.
3. **Deloitte CTEM on Deloitte Ascend** — strongest fit when there is no patch at all and the bottleneck is designing the countermeasure. Anchor: remediation moves from days/weeks to hours.

Open question for the vendors: "Show me how Opus's code reasoning is wired into our existing ticket flow." Not specified in the post.

## Need 3 — "Our Opus PoC is stuck in legal/governance review."

Bucket → **C. Getting AI into production, governed.**

Shortlist:

1. **PwC Claude Native Cybersecurity — Secure AI Adoption.** Direct quote from the post: moves enterprises from sandbox to production in weeks rather than quarters, with deployment, governance, and audit evidence.
2. After unblocking adoption, transition into the same vendor's **Scaled Frontier Defense** to integrate Opus reasoning into existing vuln management, detection, security engineering, and GRC workflows under guardrails and auditability.

Open question: "What's the audit evidence package that comes out the other side?" The post asserts there is one; it does not enumerate it.

## What this example does not invent

- No pricing.
- No SLAs.
- No certifications (SOC 2, FedRAMP, etc.) are claimed for any partner offering.
- No deployment region availability.
- No customer references beyond what the post quotes.

## Source

- [How our partners are putting Opus to work for cybersecurity](https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity)
