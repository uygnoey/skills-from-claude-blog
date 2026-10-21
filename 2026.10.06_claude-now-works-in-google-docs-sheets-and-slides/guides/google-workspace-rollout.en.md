**English** · [한국어](./google-workspace-rollout.ko.md) · [Español](./google-workspace-rollout.es.md) · [日本語](./google-workspace-rollout.ja.md)

# Rolling out Claude for Google Workspace

There are two ways to use Claude with Google Docs, Sheets, and Slides. This guide covers how to set
up each one for an individual user and for an organization.

## Two surfaces

| | Add-on (sidebar) | Connectors (from chat) |
|---|---|---|
| Starts from | An open Google file | A Claude conversation |
| Best for | Editing the file in front of you, working on a selection | New files, work spanning several files |
| Status | Public beta, all paid Claude plans | Beta |
| File access | Follows your Google sharing permissions | Follows your Google sharing permissions |

The add-on uses the same models, connectors, and skills as regular Claude.

## Individual setup
1. Install Claude from the Google Workspace Marketplace.
2. Open a Doc, Sheet, or Slides deck and choose Extensions > Claude > Open Claude.
3. Choose an edit mode: **Ask before edits** (default; each change is an approval card) or
   **Accept all edits** (changes apply without stopping).
4. To work from chat, turn on the Google Docs, Sheets, and Slides connectors, then paste a file link
   or ask for a new file.

## Organization rollout
1. **Deploy the add-on** from the Google Admin console to the whole domain or to selected groups.
2. **Enable connectors**: on Team and Enterprise plans, an owner or primary owner must enable the
   Google connectors before users can use them.
3. **Confirm enterprise controls**: the Compliance API, customer-managed encryption keys, and
   OpenTelemetry audit export also apply to the add-on.
4. **Set a default edit-mode policy** for your teams (e.g. keep "Ask before edits" for shared files).
   This is a suggested practice, not a requirement from the post.
5. **Share reusable formats as skills** so teams get consistent outputs (e.g. a review deck format).

## Things to keep in mind
- Both surfaces are in beta.
- The post does not mention version history or undo; see the Help Center setup guide.

## Source
- https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides
