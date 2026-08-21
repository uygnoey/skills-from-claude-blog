# Worked compositions

The announcement gives two concrete agents and one general loop. They are
reproduced here with the composition made explicit, so you can map your own
workflow onto the same four questions:

> What does the agent **read**? Whose **procedure** does it follow? What
> **software** must it operate? What does it **hand back**?

## The claims agent

The example the announcement builds the whole stack around.

| Stage | Capability | What happens |
| --- | --- | --- |
| Read | Files API | Reads the intake document, referenced by ID |
| Procedure | Skills API | Follows a skill encoding the team's filing procedure |
| Operate | Browser use tool | Completes the submission in an insurer's web portal |
| Hand back | Files API | Saves the confirmation back as a file |

Code execution and web search, already generally available, fit into the same
loop.

Why each choice:

- **Files API for the intake document** — it is referenced by ID across the whole
  multi-turn run instead of being re-sent on every request.
- **A skill for the filing procedure** — the procedure is loaded only when a
  filing task comes up, is versioned separately from the calling application, and
  carries its own scripts and templates.
- **Browser use tool, not pixel computer use** — the insurer's portal is a web
  application, so the agent acts on named fields and buttons instead of screen
  positions.
- **Files API for the confirmation** — the output is a retrievable artifact, not
  text to be parsed out of a model response.

## Agents in systems with no API

Reported by Davide Locatelli, Research Engineer, for agents that work inside
healthcare and insurance systems with no API:

- Longest claims workflow: **32 minutes → 13 minutes**
- Cost per task: **down about 30%** across every workflow tested
- Completion: **100%**
- Prompt changes required: **none**

The attributed cause is the updated computer use tool taking several actions per
turn instead of one action per model call.

The general lesson: when a workflow is many small UI interactions, per-turn
action batching compounds. Measure your own workflows before and after rather
than assuming the same magnitude.

## A skill as the unit of domain expertise

Box's composition, described by Matthew Midson, Managing Director of Banking:

| Stage | What happens |
| --- | --- |
| Procedure | A skill captures the firm's credit methodology and approved memo format |
| Read | Box Agent applies it to financial statements and deal documents already in Box |
| Hand back | Produces a source-grounded credit memo for analyst review |

The structural point: the bank-specific methodology lives in a skill, so Box did
not have to build a separate bespoke agent per customer workflow. "Banks get
agents for complex workflows without building each one from scratch."

Two things to copy from this shape:

- **The skill is the customization surface.** One agent, many skills, rather than
  many agents.
- **Output is for review, not for autonomy.** The memo is produced *for analyst
  review*. In a domain where being wrong is a compliance event, the agent's job
  ends at a reviewable artifact.

## Mapping your own workflow

Walk the four questions in order, and let the answers select the capability:

1. **Read** — does a document persist across turns? → Files API, referenced by ID.
2. **Procedure** — is there a team procedure that should not live in a prompt
   string? → a skill, uploaded and versioned through the Skills API.
3. **Operate** — is there a real API for the target system? Use it. No API, and
   it's a web application? → browser use tool. No API, not a browser? → computer
   use.
4. **Hand back** — is the deliverable a file? → write it through the Files API and
   download it, rather than reconstructing it from response text.

## Source

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api) (published 2026-08-20).
