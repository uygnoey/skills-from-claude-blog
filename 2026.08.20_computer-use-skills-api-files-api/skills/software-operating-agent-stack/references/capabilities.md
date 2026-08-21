# The four capabilities, as announced

Everything on this page is drawn from the general-availability announcement of
2026-08-20. Where the announcement did not state a detail, it is not stated here
— consult the platform documentation for the full parameter surface.

## Computer use

**What it does.** Lets you build agents that operate software they can see. Given
a screenshot, the agent clicks, types, and scrolls the way someone at the
keyboard would. That is what lets it work in applications that were never built
for automation.

**What changed at GA.**

- Claude can take **several actions per turn** instead of one per model call, so
  tasks finish in fewer calls and less time.
- Computer use is now **eligible for HIPAA-regulated workloads** under
  Anthropic's BAA.

**Reported effect.** From Davide Locatelli, Research Engineer, on agents working
inside healthcare and insurance systems that have no API: on the new computer use
tool, "our longest claims workflow went from 32 minutes to 13, cost per task fell
about 30% across every workflow we tested, and completion hit 100%, with no
changes to our prompts."

## Browser use tool

**What it is.** New in computer use as of this release, for agents that work in
web applications.

**How it differs from pixel-level computer use.** Alongside the screenshot, the
agent reads the **structure of the page** and acts on a specific field or button
rather than a position on screen. It uses the same multi-action turns as the
updated computer use tool, and adds page structure so agents target web elements
more reliably than with pixels alone.

**Selection rule.** Web application → browser use tool. Desktop or other
non-browser surface → computer use.

## Skills API

**What a skill is.** A folder of instructions, scripts, and templates that Claude
loads **only when a task calls for it**.

**What the API gives you.** Upload and version your own skills, then attach them
to any request. They run in Claude's code execution sandbox, so there is nothing
for you to host.

**What changed at GA.** A simpler API for uploading and versioning your own
skills.

**Reported use.** From Matthew Midson, Managing Director of Banking, on Box:
"The Skills API gave us a straightforward way to build specialized document
creation into Box Agent. For a bank, a skill captures the firm's credit
methodology and approved memo format; Box Agent applies it to the financial
statements and deal documents already in Box and produces a source-grounded
credit memo for analyst review. Banks get agents for complex workflows without
building each one from scratch."

## Files API

**What it is.** Storage for the documents an agent reads and writes. Upload a PDF
or spreadsheet once, reference it by ID in later requests instead of re-sending
it, and download the files the agent creates.

**What changed at GA.**

- Automatic file expiration.
- 5x higher rate limits.
- 1 TB of storage per organization.

## Already generally available

Code execution and web search were already generally available, and fit into the
same loop as the four capabilities above.

## Source

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api) (published 2026-08-20).
