---
name: unified-app-task-handoff
description: Plan and hand over work in the unified Claude app, where (from September 16, 2026) Claude Cowork and chat merged into one Claude. Covers framing a bigger task inside an ordinary conversation so Claude can keep working after the laptop closes, producing Claude Docs, Claude Slides, and Claude Design outputs from the same conversation (each at one shareable link; edit directly, comment for Claude, present, or download as PowerPoint or PDF), choosing the check-in mode (ask before acting by default, or keep working and check in only when needed), scheduling recurring work such as a Monday report, and what carries over for Cowork users. Includes rollout facts (Pro and Max first; Team and Free later; Enterprise admins get at least 30 days notice; Docs, Slides, Design in conversations are beta on paid plans and admin-controlled for Enterprise). Use when someone asks where a task should go in Claude, how to hand over a report or deck, or what changed after the Cowork and chat merge.
---

## Purpose
After the merge there is no separate place to choose for bigger work: Claude figures out what a task
needs from any conversation, using the context, skills, and connectors already set up. This skill helps
a user hand over a task well and explains what changed. It uses only what the announcement states; for
the full capability list, point to the Help Center.

## When to use
- "Should I do this in chat or Cowork?" (answer: just ask Claude in a conversation)
- Handing over a report, document, or deck to be finished while away.
- Setting up recurring work (e.g. every Monday).
- A Cowork user asking whether their chats, projects, artifacts, connectors, and skills moved.
- An admin asking about rollout and controls.

## Instructions

1. **Start in a normal conversation.** Quick questions and bigger hand-offs go to the same place. No
   setting needs to be turned on.
2. **Frame the hand-off in one message**: the data question, the house style ("the way we always do"),
   what to flag, and the outputs (e.g. "a doc plus five slides for the leadership meeting"). Claude
   asks if something is unclear.
3. **Pick outputs from the same conversation** so they stay consistent:
   - *Claude Docs* - you and Claude write the document together.
   - *Claude Slides* - Claude drafts the slides; edit directly, present from Claude, or download as
     PowerPoint or PDF.
   - *Claude Design* - visual work now available inside conversations (standalone Design keeps working).
   Each lives at one shareable link that opens on a phone; select an element to move it, or tell
   Claude what to change, or leave a comment for Claude.
4. **Choose the check-in mode.** Default: Claude asks before taking an action. Optionally let it keep
   working and check in only when something needs a closer look. The user keeps the final say.
5. **Follow up from anywhere.** Progress can be checked from a phone; work can continue after the laptop
   is closed.
6. **Make it recurring** by scheduling it (e.g. every Monday) so Claude starts without being asked.
7. **Answer rollout questions** with these facts only:
   - Rolling out to Pro and Max first, on web, desktop, and mobile, over the coming weeks, for existing
     and new users. Team and Free follow soon.
   - Enterprise admins hear at least 30 days before changes for their organization, and choose when to
     turn on Docs, Slides, and Design.
   - Docs, Slides, and Design are in beta on paid plans.
   - Cowork users find everything where they left it.

## Examples

**Example 1 - where does it go?**
Input: "I have a big messy competitive analysis. Do I open Cowork?"
Output: No separate place is needed. Ask in a conversation, describe the outputs (doc, slides), and pick
the check-in mode.

**Example 2 - weekly report with slides**
See [examples/weekly-report-walkthrough.md](examples/weekly-report-walkthrough.md) for the post's
end-to-end scenario turned into a reusable hand-off prompt.

**Example 3 - admin question**
Input: "Will this change our Enterprise org overnight?"
Output: No. Enterprise admins are notified at least 30 days before anything changes, and they choose
when to enable Docs, Slides, and Design.

## Source
- https://claude.com/resources/articles/cowork-is-now-claude
