# Situation report format

Posted by the orchestration agent into the incident channel, and updated as evidence changes. The first one should land within minutes of the incident opening, even when the root cause is not yet known — a report that says "here is what I have ruled out so far" is still useful.

Every claim names its evidence. A report a human cannot check is a report a human has to redo.

---

```markdown
**SITREP — <incident id> — <update #n> — <timestamp>**

**Status:** investigating | mitigated | resolved
**Impact:** <what is broken, for whom, since when>

**Current hypothesis** *(confidence: high | medium | low)*
<one or two sentences>

**Evidence**
- <claim> — <query, dashboard, log line, or diff that supports it>
- <claim> — <source>

**Ruled out**
- <hypothesis> — <what ruled it out>

**Open questions**
- <question> — <who or what could answer it>

**Recommended next action**
<action, and whether it needs human approval>

**Prior related incidents**
- <date> — <title> — <what was different or the same>
```

---

## Notes on writing these

- Lead with impact, not with mechanism. The first line is for someone who just joined the channel.
- Distinguish observed from inferred. The "Evidence" section holds only what was observed.
- "Ruled out" is not filler. It is the section that stops three people re-checking the same dashboard.
- Update the report; do not silently rewrite the first one. The sequence of hypotheses is itself post-mortem material.

## Handoff and status reports

Two other report types are worth separating from the incident sitrep:

- **Handoff report** — daily and weekly, for humans, so the next person in the rotation can pick up where the last left off.
- **Public status report** — newsroom-style, compiled from incident channels, build metrics, merge queue stats, and deploy lag, posted to a channel anyone in the company can read. Expect to iterate the format several times; readability here is team-specific taste, not plumbing.

## Source

- https://claude.com/blog/ai-ci-cd-on-call
