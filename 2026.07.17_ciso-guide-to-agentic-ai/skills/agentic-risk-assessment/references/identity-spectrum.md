# The agentic identity spectrum

Everything you deploy sits at one of two ends of an identity access model spectrum.

## End A — the system service account

A self-contained, single-purpose, least-privilege identity that does exactly one thing for the
business, **with no human identity attached**.

Examples named in the source article:

- an incident response agent
- a ticket triage agent
- an autonomous code reviewer
- a shared-workspace agent that human teams collaborate with by tagging it into a channel

Accountability is unambiguous because the agent *is* the identity: it holds its own account,
its own least-privilege grants, and its own audit trail.

## End B — the human credential

When an employee uses a chat interface or a personal agent harness on their laptop, **the
person at the keyboard is accountable for the outcome**, the same way they are accountable for
anything else done with their credentials.

## The ambiguous middle

The middle of the spectrum — where an agent carries a person's delegated identity into systems
that person is not watching — is where accountability gets ambiguous.

**Ambiguous accountability is how incidents become unexplainable.** When a deployment lands in
the middle, the work of the review is to push it toward one end or the other: either give it
its own service identity with its own least-privilege grants, or keep a human on the loop for
every write.

## Why the insider-risk framing

An agent that drifts out of alignment with your intent is **indistinguishable from an insider
attack**. The security industry spent 2019–2022 formalizing insider risk as a discipline
distinct from perimeter defense, recognizing that the most dangerous attack vector in a system
is often one that compromises someone who already has legitimate access.

The operational difference with agents is response time. The Ponemon Institute's 2026 *Cost of
Insider Risks* report found organizations took an average of **67 days** to contain an insider
incident — even after years of investment in dedicated insider risk programs. At agent
execution speeds, 67 days is the wrong unit of measurement entirely.

Agents that hold their own accounts and run multi-day workstreams already operate inside
organizations today, and they need to be governed the way you govern people: **identity, least
privilege, monitoring, and an insider-risk program that can respond in minutes.**

## Source

["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai)
