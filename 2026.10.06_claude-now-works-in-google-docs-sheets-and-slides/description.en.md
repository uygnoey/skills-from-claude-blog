**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement that Claude for Google Workspace is in public beta on all paid Claude plans. It
opens a Claude sidebar next to an open Google Doc, Sheet, or Slides deck that can read the file, see
the selection, and edit it directly. New Google Docs, Sheets, and Slides connectors (beta) also let
Claude create and edit Google files from a Claude chat.

## When is it useful?
- When you want Claude to edit, analyze, or build content inside a Google file you already have open.
- When you want to start in Claude and produce a new doc, sheet, or deck, or work across several files.
- When an admin is planning a domain-wide or group rollout.

## Key points
- Docs: small in-place edits; larger rewrites come back as suggestion cards to apply or dismiss.
- Sheets: formulas, pivot tables, native charts, new tabs, and cleaning or joining data by running
  Python on a range and writing results back.
- Slides: builds slides from the deck's layouts and themes, then checks for overlapping or off-slide
  elements and hard-to-read text.
- Edit modes: "Ask before edits" (default, each change is an approval card) or "Accept all edits".
- The sidebar uses the same models, connectors, and skills as regular Claude; enterprise controls
  (Compliance API, customer-managed encryption keys, OpenTelemetry audit export) also apply.
- File access follows existing Google sharing permissions.
- Setup: install from Google Workspace Marketplace, then Extensions > Claude > Open Claude. Admins
  can deploy to a domain or groups from the Google Admin console; on Team and Enterprise plans an
  owner or primary owner must enable the connectors first.

## Bundled resources
- Skill: `google-workspace-editing` — choosing the add-on vs connectors, edit modes, and task
  patterns per app, with task examples in `examples/task-prompts.md`.
- Guide: `google-workspace-rollout` (en/ko/es/ja) — individual setup and organization rollout.

## Source
- https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides
