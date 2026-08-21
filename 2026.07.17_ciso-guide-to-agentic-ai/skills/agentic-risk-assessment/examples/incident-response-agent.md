# Example: an incident response agent

A worked example of a **system service account** deployment — the low-risk end of the identity
spectrum — and of why you should bound *access and actions* rather than what you believe
today's model can do.

## The problem

Anyone who has been on-call for a production application knows it: you're paged at 2 a.m. about
a security incident, you spin up an incident response channel, you pull in the right people, and
you get to work. The process is tedious, documentation-heavy, and fast-moving — and with the
right context about your production environment and codebase, most of it can be automated.

## The build

The agent was given exactly three tools:

1. **Read-only access to production logs**, which contain no PII.
2. **Access to Slack**, to open the incident channel and run the process.
3. **The ability to draft a Google Doc** for the postmortem once the incident is resolved.

## Running it through the four questions

| Question | Answer |
|---|---|
| **Untrusted content** | None. Inputs were the organization's own logs and own internal Slack, both inside the trust boundary — an injection would require an insider or a compromised account rather than an anonymous attacker. |
| **Actions** | Reads everywhere; writes limited to new documents and Slack messages. No edits or deletes, no permission changes, no external endpoints. |
| **Blast radius** | The worst outcome that could be constructed was some mildly sensitive log lines posted into an incident channel that was already locked down. |
| **Observability** | Every action landed in the SIEM, so anything unexpected would surface in minutes, not weeks. |

Verdict: not risk-free, but a **bounded write surface with full audit coverage** — a risk
profile the security team was comfortable with.

## The addendum: capability appeared without any config change

With each model release the agent got smarter. In November 2025 the agent was moved from Claude
Opus 4 to Claude Opus 4.5 and **nothing else changed** — no new tools, no new permissions, no
new prompts.

Immediately after, for the first time, the intelligence uplift alone was enough for the agent
to notice mid-incident that it had already found the root cause in a stack trace, and that, in
the absence of the human who hadn't arrived yet, it could try to fix production on its own by
reaching out to another agent that had the appropriate code access.

Reviewing the logs afterwards, the reasoning was visible in the thinking traces:

> I have done what I was asked to do. The human is not here. What if I fixed the problem?

On its own, it reached out over Slack to an internal agent instance that can write code changes
and upload them for human review, and asked it to write the fix. The fix went to a pull request
that a human reviewed before pushing to production.

The expanded blast radius from this emergent agent-to-agent communication was itself governed
by the original principles: the worst that could happen was that a code change would be
uploaded containing a production log line.

## The two lessons

1. **New capabilities can show up within the boundaries of an existing agent deployment.**
   Limit access and actions — not what you believe today's model limits are.
2. **Controls are effective even with stochastic agents.** The new behavior was
   human-on-the-loop because it happened in a Slack channel, and the only write-like action
   still required a human review.

Agent-to-agent communication is now a regular part of that incident response root-cause and
remediation practice, all with human-on-the-loop monitoring. Outside incident response,
agent-to-agent communication within chat channels, with a human on the loop where people work,
is the norm.

## Source

["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai)
