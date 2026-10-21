---
name: google-workspace-editing
description: Work on Google Docs, Sheets, and Slides with Claude, using either the Claude for Google Workspace add-on (a sidebar beside an open file that reads the file, sees the selection, and edits in place) or the Google Docs/Sheets/Slides connectors (create or edit Google files from a Claude chat). Covers choosing the surface, picking an edit permission mode ("Ask before edits" vs "Accept all edits"), and task patterns for Docs (in-place edits, suggestion cards), Sheets (formulas, pivot tables, native charts, tabs, Python-based cleaning and joins), and Slides (layout/theme-based slides plus a layout check). Use when a user wants Claude to draft, edit, analyze, or build content inside Google Workspace files.
---

## Purpose
Claude for Google Workspace (public beta on all paid Claude plans) opens Claude in a sidebar next to
an open Doc, Sheet, or Slides deck. Claude can read the file, see the current selection, and edit it
directly. Separately, the Google Docs, Sheets, and Slides connectors (beta) let Claude create and
edit Google files from a regular Claude conversation. This skill helps pick the right surface and run
common tasks safely.

## When to use
- The user already has a Google file open and wants help on that file → **add-on (sidebar)**.
- The user wants a new file, or work spanning several files, started from chat → **connectors**.
- The work needs data from other tools (e.g. CRM records, Drive notes) → either surface; both use the
  same models, connectors, and skills as regular Claude.

## Instructions

1. **Pick the surface.**
   - Add-on: Extensions > Claude > Open Claude inside the file. Best for edits to the file in front
     of you and for work on a selection.
   - Connectors: in a Claude chat, paste a Google file link or ask for a new doc, sheet, or deck. On
     supported setups the file opens in a pane beside the conversation.
   - Access always follows the user's existing Google sharing permissions.

2. **Pick the edit permission mode (add-on).**
   - **Ask before edits** (default): every change appears as an approval card. Use for shared,
     high-stakes, or unfamiliar files.
   - **Accept all edits**: changes apply without stopping. Use for drafts or bulk mechanical work the
     user has scoped clearly.

3. **Docs.**
   - Small fixes (a sentence, a heading style) are applied in place.
   - Larger rewrites come back as suggestion cards the user can apply or dismiss — keep them scoped
     so each card is easy to review.

4. **Sheets.**
   - Write formulas, build pivot tables and native charts, add tabs.
   - For cleaning or joining data, run Python on a range and write the results back to the sheet.
   - State which ranges/tabs were changed so the user can check them.

5. **Slides.**
   - Build new slides from the deck's own layouts and themes rather than free-form shapes.
   - After building, check for overlapping or off-slide elements and hard-to-read text, and fix them.

6. **Bring in context and reuse it.**
   - Pull in data from other enabled connectors when the task needs it.
   - When a format works (e.g. a review deck), save it as a skill so teammates can reuse it.

7. **Respect admin setup.** On Team and Enterprise plans an owner or primary owner must enable the
   Google connectors before users can use them. Enterprise controls (Compliance API, customer-managed
   encryption keys, OpenTelemetry audit export) also apply to the add-on. If something is unavailable,
   point the user to their admin rather than working around it.

## Examples
See [examples/task-prompts.md](examples/task-prompts.md) for the task examples from the post, grouped
by app and surface.

Short example — Sheets via the add-on, "Ask before edits" mode:
- User: "Build a quarterly budget-vs-actuals workbook with a tab per team and a summary chart, and
  flag overspending."
- Claude: proposes new tabs, formulas, a native chart, and highlighting for over-budget lines; each
  change appears as an approval card.

## Notes
- Both the add-on and the connectors are in beta; behavior may change.
- The post does not describe version history or undo behavior — refer to the Help Center setup guide
  and Google's own version history.
