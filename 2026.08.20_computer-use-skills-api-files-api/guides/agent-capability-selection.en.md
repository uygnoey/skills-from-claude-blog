**English** · [한국어](./agent-capability-selection.ko.md) · [Español](./agent-capability-selection.es.md) · [日本語](./agent-capability-selection.ja.md)

# Choosing capabilities for a production agent

Computer use, the Skills API, and the Files API are generally available on the
Claude Platform as of 2026-08-20, and computer use adds a new browser use tool.
This guide is about picking between them.

## The three questions the release answers

An agent that does real work usually needs three things beyond the model:

1. **A way to act on software it does not have an API for.** → computer use, or
   the browser use tool on the web.
2. **A way to carry your team's expertise into the run.** → the Skills API.
3. **A way to hold documents across turns and return finished artifacts.** →
   the Files API.

Code execution and web search, already generally available, sit in the same loop.

## Acting on software

**Computer use** builds agents that operate software they can see. Given a
screenshot, the agent clicks, types, and scrolls the way someone at the keyboard
would — which is exactly what lets it work in applications that were never built
for automation.

**The browser use tool**, new in this release, extends that to the web.
Alongside the screenshot, the agent reads the structure of the page and acts on a
specific field or button rather than a position on screen.

The decision order:

| Situation | Choice |
| --- | --- |
| A real API exists | Use the API — cheaper, faster, deterministic |
| Web application, no API | Browser use tool |
| Desktop or other non-browser surface, no API | Computer use |

Both tools now take several actions per turn instead of one action per model
call, so tasks finish in fewer calls and less time.

**Why structure beats pixels.** Targeting a named element survives layout shifts,
resolution differences, and re-renders that move a control a few pixels. On a web
surface the structural path is the reliability upgrade, and it does not cost you
the multi-action turns.

## Carrying expertise

A **skill** is a folder of instructions, scripts, and templates that Claude loads
only when a task calls for it. The Skills API lets you upload and version your
own skills and attach them to any request; they run in Claude's code execution
sandbox, so there is nothing to host.

Three things follow from that shape:

- **On-demand loading.** Encoded expertise does not have to compete for room in
  every request's prompt.
- **Versioning.** A procedure gets its own change history, separate from the
  application code that calls it. This is the difference between a prompt string
  someone edited last quarter and an artifact with a version.
- **The skill is the customization surface.** Box's account is the clearest
  illustration: one Box Agent, with a skill per firm capturing that firm's credit
  methodology and approved memo format, rather than a bespoke agent built from
  scratch per workflow.

## Holding documents

The **Files API** is storage for the documents an agent reads and writes: upload
a PDF or spreadsheet once, reference it by ID in later requests instead of
re-sending it, and download the files the agent creates. GA adds automatic file
expiration, 5x higher rate limits, and 1 TB of storage per organization.

Reference-by-ID is what changes the design. A multi-turn workflow stops
re-transmitting the same source document every request, and the deliverable
becomes an artifact you retrieve rather than text you parse out of a response.

## The composed loop

The announcement's worked example — a claims agent:

1. Reads the intake document from the Files API.
2. Follows a skill that encodes the team's filing procedure.
3. Completes the submission in an insurer's web portal with the browser use tool.
4. Saves the confirmation back as a file.

Scope your own agent by walking the same four questions in order: what does it
read, whose procedure does it follow, what software must it operate, and what
does it hand back?

## Reported results

- **Healthcare and insurance systems with no API.** On the new computer use tool,
  one team's longest claims workflow went from 32 minutes to 13, cost per task
  fell about 30% across every workflow tested, and completion hit 100% — with no
  changes to their prompts.
- **Box.** A skill captures a bank's credit methodology and approved memo format;
  Box Agent applies it to the financial statements and deal documents already in
  Box and produces a source-grounded credit memo for analyst review.

Note the second one's boundary: the output is *for analyst review*. In domains
where an error is a compliance event, the agent's job ends at a reviewable
artifact.

## Availability

| Surface | Status |
| --- | --- |
| Claude Platform | Computer use, browser use tool, Skills API, Files API |
| Microsoft Foundry | Skills API and Files API |
| Google Cloud Vertex AI | Updated computer use and browser use tools coming soon |

Computer use is now eligible for HIPAA-regulated workloads under Anthropic's BAA.
Existing beta integrations keep working while you migrate. See the platform
documentation for computer use, the browser use tool, the Skills API, and the
Files API to get started.

## Source

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api) (published 2026-08-20).
