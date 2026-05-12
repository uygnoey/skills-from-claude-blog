# Worked patterns — Outcomes + Multiagent orchestration + Webhooks

This example walks one concrete pattern that combines the three pipeline-shaping capabilities announced at Code w/ Claude SF 2026. It does not extend the source post — it only composes the features the post explicitly names.

## Scenario

A team wants a Claude Managed Agents pipeline that produces a weekly competitive intelligence brief: read raw sources, draft sections in parallel, fact-check, assemble, grade, and notify downstream systems.

## Filesystem contract

All agents share one filesystem. Everything is passed as files, not as prompt context.

```
/inputs/
  sources.txt              # URLs / docs to read (provided by the human or upstream)
  rubric.md                # Outcome rubric (see below)
/work/
  notes/                   # written by researcher subagents
  draft/<section>.md       # written by drafter subagents
  review/<section>.md      # written by reviewer subagents
/out/
  brief.md                 # written by the lead agent
  grade.json               # written by the grader
```

## Roles

- **Lead agent** — orchestrates. Reads `/inputs/`, decides how to split the brief into sections, delegates, and finally writes `/out/brief.md`.
- **Specialist subagents** running in parallel on the shared filesystem, each with its own model, prompt, and tools:
  - `researcher` — for each section in the plan, write `/work/notes/<section>.md`.
  - `drafter` — for each section, read its notes and write `/work/draft/<section>.md`.
  - `reviewer` — for each draft, read it and write `/work/review/<section>.md` with corrections.

## Outcome rubric (`/inputs/rubric.md`)

```
The brief is acceptable iff:

1. Every section in the table of contents has a corresponding draft and review file.
2. Every factual claim has at least one citation from /inputs/sources.txt.
3. Total length is between 1200 and 2000 words.
4. The brief opens with a 5-bullet "What changed this week" summary.
5. No section makes a claim that the matching review file marks as unsupported.
```

This rubric is consumed by the **Outcomes** grader, which runs in its **own context window**, scores the lead agent's `/out/brief.md`, and either accepts or returns it for revision.

## Run loop

1. Lead agent reads `/inputs/`.
2. Lead delegates researcher + drafter + reviewer in parallel by section. Multiagent orchestration runs these on the shared filesystem; each subagent picks its own model and tools.
3. Lead reads `/work/review/*.md` and assembles `/out/brief.md`.
4. Outcomes grader scores `/out/brief.md` against `/inputs/rubric.md` in a fresh context window.
5. If the grader rejects, the agent revises. Iterate until the grader accepts.
6. On acceptance, the webhook fires.

## Webhook payload (consumer side)

The exact webhook schema is not stated in the source post — fetch it from the Claude Console docs. On the consumer side, plan for at least:

- Run ID and timestamp.
- Outcome status (accepted vs. abandoned after N revisions).
- Pointer to the produced artifact(s).

The downstream system reads `/out/brief.md` and `/out/grade.json` and posts to the team's wiki / Slack / mail.

## Where Dreaming fits in (later)

Once the pipeline has run for a few cycles, **Dreaming** can curate memory across past runs — for example, learning that one source domain is unreliable, that a certain rubric clause is regularly the blocker, or that a section author prefers a specific tone. Do not turn Dreaming on before there is real session history to learn from.

## What this example does not invent

- Exact rate-limit numbers (post does not state them).
- Exact webhook payload schema (not in the post).
- Customer-specific architectures from Asana, Cursor, GitHub, Replit, or Vercel — the post lists them but does not quote their architectures.

## Source

- [Code w/ Claude SF 2026: Building on the AI exponential](https://claude.com/blog/code-w-claude-sf-2026-sf)
