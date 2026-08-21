# The four questions

When an agentic use case reaches the review process, its risk is assessed by asking four
questions. The answers together produce a picture of the risk; the **principle of least
agency** — grant the narrowest capability that still completes the task — tells you what to
do with that picture.

---

## 1. What untrusted content does it ingest?

**Untrusted** means anything an attacker could plausibly write or alter:

- outside email
- the open web
- third-party documents
- public repositories

If the answer is "nothing," the agent-specific risk is near zero and you should move quickly.

Why this question comes first: **prompt injection**. An attacker hides instructions inside
content the agent reads, and the agent follows the attacker instead of the user. Any agent
that touches untrusted content could be exposed, depending on how robust the model's defenses
are. As models grow more capable they are getting meaningfully better at resisting injection —
attack success rates keep falling, but they are not zero.

The other dominant internal threat vector is a **data leak enabled by connecting disparate
systems** through personal agents with insufficient oversight.

## 2. What actions can it take, and on whose behalf?

- Read-only is a different concern from read/write.
- Tool calls, code execution, and network egress each widen the aperture.
- Every action happens under some identity, and you need to know whose.

The "on whose behalf" half of the question is what places the deployment on the identity
spectrum (see `references/identity-spectrum.md`).

## 3. What is the blast radius if it is misaligned?

**Scope × severity** is the quick calculation:

- *Scope*: did the bad actor or alignment incident have access to one file or the whole org?
- *Severity*: would it be an anomaly, an annoyance, a data exposure, or a true incident?

Construct the worst outcome you can and write it down. A deployment whose worst constructible
outcome is "a mildly sensitive log line lands in an already-locked-down channel" is a very
different decision from one whose worst outcome is an unrecoverable production change.

## 4. What observability do I have?

- Can you tell agent actions from user actions?
- Does it land in your SIEM?

Observability is what converts "we would find out eventually" into "anything unexpected
surfaces in minutes, not weeks."

---

## Using the answers

The four answers are inputs, not a verdict. The goal of running a use case through them is to
find **the conditions under which you would approve it**.

Default posture: **admin-paced rollout** — enable a small group, watch the telemetry, then
expand access.

## Source

["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai)
