# Governance controls

Many security processes are automated, but humans remain integral. The attention
moves off reviewing individual code changes and bug reports, and onto Claude Tag,
loops, and dashboards.

This is why governance matters more, not less. The structure degrades if a skill
goes stale, if a discovered bug class never makes it back into `CLAUDE.md`, or if an
agent's decisions go unsampled.

## The five controls

### 1. Tier the codebase by risk, then automate reviews based on that level

Automation is not uniform. Decide per tier what runs, what an agent may approve, and
what always waits for a person. Entire codebases can stay under strict human
approval.

### 2. Shadow mode for all new AI reviewers

A new agent posts comments for human approval until trust is earned. Nothing it says
blocks or approves anything while it is in shadow.

The team also red teams new reviewers by trying to insert malicious changes and
seeing whether the reviewer catches them. A reviewer that cannot catch a planted
change should not graduate out of shadow mode.

### 3. Sample a percentage of all automated approvals

Weight the sample by risk. Sampling is what makes an automated approval an
accountable decision rather than an unobserved one.

### 4. Watch the vitals

Maintain and closely monitor a dashboard that rolls up key metrics across every
security process and workstream. Useful metrics implied by the post:

- Share of PRs receiving substantive review comments.
- Proportion of automated approvals sampled, and the disagreement rate on that
  sample.
- Reviewers currently in shadow mode, and how long they have been there.
- Time since each `CLAUDE.md` and org-wide security skill was last updated.
- Findings by bug class, and whether each discovered class has been written back
  into guidance.

### 5. Route every agent action to the SIEM

Every automated approval, tool call, and agent-to-agent message is logged with the
signals it used and lands in the SIEM, so any decision is attributable and auditable
after the fact.

Treat these agents as a new type of insider threat and raise alerts when they act
out of alignment. This is what makes an incident like an agent asking another agent
to push code visible rather than silent.

## Degradation checklist

Run this periodically. Each item is a way the structure quietly stops working.

- [ ] Is any org-wide security skill older than its last relevant incident?
- [ ] Was every bug class discovered this period written back into guidance?
- [ ] Is any reviewer approving without being sampled?
- [ ] Has any reviewer been in shadow mode long enough that nobody remembers it?
- [ ] Does the vitals dashboard have an owner who looks at it?
- [ ] Are agent-to-agent messages actually landing in the SIEM, or only the tool
      calls?
- [ ] Can a specific automated approval from last month be reconstructed with the
      signals and reasoning behind it?
