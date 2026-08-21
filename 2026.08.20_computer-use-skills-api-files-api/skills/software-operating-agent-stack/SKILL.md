---
name: software-operating-agent-stack
description: Compose computer use, the browser use tool, the Skills API, and the Files API into agents that operate software, apply your team's expertise, and return finished files. Use when an agent has to work in an application that exposes no API; when choosing between pixel-level computer use and the structure-aware browser use tool for a web task; when packaging team procedure as an uploadable, versioned skill instead of stuffing it into a prompt; or when documents need to persist across requests by ID rather than being re-sent each turn.
---

# The production agent stack on the Claude Platform

Computer use, the Skills API, and the Files API reached general availability on
the Claude Platform on 2026-08-20, and computer use gained a new **browser use
tool** for agents working in web applications. Code execution and web search were
already generally available. Together these are the pieces of an agent that can
operate software it can see, apply your expertise, and hand back finished files.

Per-capability detail is in
[references/capabilities.md](./references/capabilities.md); availability and
migration notes are in
[references/availability.md](./references/availability.md).

## Instructions

### 1. Reach for computer use when there is no API

Computer use lets you build agents that operate software they can see. Given a
screenshot, the agent clicks, types, and scrolls the way someone at the keyboard
would — which is what makes it work in applications that were never built for
automation.

That framing is also the selection rule. If a real API exists, use it: it is
cheaper, faster, and deterministic. Computer use earns its place specifically
where the surface has no programmatic entry point — legacy internal tools,
vendor portals, systems of record that a partner controls.

The GA update changes the economics: the updated computer use tool lets Claude
take several actions per turn instead of one per model call, so tasks finish in
fewer calls and less time.

### 2. On the web, prefer the browser use tool

The browser use tool is new in computer use as of this release, and it is the
better default for anything running in a browser. Alongside the screenshot, the
agent reads the structure of the page and acts on a specific field or button
rather than a position on screen.

Two consequences worth designing around:

- **Reliability.** Targeting a named element survives layout shifts, resolution
  differences, and re-renders that move a button a few pixels. Pixel coordinates
  do not.
- **It keeps the multi-action turns.** The browser use tool uses the same
  several-actions-per-turn model as the updated computer use tool, so you get the
  latency and cost benefit as well as the structural targeting.

Use pixel-level computer use for the desktop surfaces the browser tool cannot
reach, and the browser use tool for web applications.

### 3. Package your procedure as a skill, not as a prompt

A skill is a folder of instructions, scripts, and templates that Claude loads
only when a task calls for it. With the Skills API you upload and version your
own skills, then attach them to any request. They run in Claude's code execution
sandbox, so there is nothing for you to host.

Design implications:

- **Loaded on demand.** Because a skill is pulled in only when the task calls for
  it, the expertise you encode does not have to compete for room in every
  request's prompt.
- **Versioned as an artifact.** Upload and version the skill rather than editing
  a prompt string in application code. That gives the procedure its own change
  history, separate from the code that calls it.
- **Scripts and templates travel with it.** A skill is a folder, so deterministic
  helpers and output templates ship alongside the instructions instead of being
  reconstructed by the model each run.

### 4. Give documents identity with the Files API

The Files API is storage for the documents an agent reads and writes. Upload a
PDF or spreadsheet once, reference it by ID in later requests instead of
re-sending it, and download the files the agent creates.

The GA update adds automatic file expiration, 5x higher rate limits, and 1 TB of
storage per organization.

Reference-by-ID is the part that changes agent design: a multi-turn workflow
stops re-transmitting the same source document on every request, and the agent's
output becomes an artifact you can retrieve rather than text you have to parse
out of a response.

### 5. Compose the loop

The four pieces are meant to be used together, and code execution and web search
fit into the same loop. The canonical shape from the announcement:

1. Read the input document from the Files API.
2. Follow a skill that encodes the team's procedure.
3. Act in the target application — the browser use tool for a web portal,
   computer use for a desktop surface.
4. Save the result back as a file.

When you scope a new agent, walk those four questions in order: what does it
read, whose procedure does it follow, what software does it have to operate, and
what does it hand back?

## Examples

**A claims agent.** The example given in the announcement: it reads the intake
document from the Files API, follows a skill that encodes the team's filing
procedure, completes the submission in an insurer's web portal with the browser
use tool, and saves the confirmation back as a file.

**Agents inside systems with no API.** A research engineer quoted in the
announcement, on agents working inside healthcare and insurance systems that have
no API: on the new computer use tool their longest claims workflow went from 32
minutes to 13, cost per task fell about 30% across every workflow tested, and
completion hit 100% — with no changes to their prompts.

**A skill as the unit of domain expertise.** Box built specialized document
creation into Box Agent with the Skills API: for a bank, a skill captures the
firm's credit methodology and approved memo format, and Box Agent applies it to
the financial statements and deal documents already in Box to produce a
source-grounded credit memo for analyst review. The point made is that customers
get agents for complex workflows without building each one from scratch.

More worked compositions are in
[examples/workflow-shapes.md](./examples/workflow-shapes.md).

## Source

Distilled from [Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api)
(published 2026-08-20).
