**English** · [한국어](./m365-collaboration.ko.md) · [Español](./m365-collaboration.es.md) · [日本語](./m365-collaboration.ja.md)

# Microsoft 365 cross-app workflows with Claude

## What is this guide?
A short, practical guide to collaborating with Claude across Excel, PowerPoint, Word, and Outlook while maintaining one continuous conversation context.

## Recommended workflows
1. **Email → attachment → analysis → narrative → deck**
   - Start in Outlook to understand the request.
   - Open the attachment in Word/Excel so the request stays in context.
   - Do the analysis in Excel, draft the narrative in Word, and build the deck in PowerPoint.

2. **Keep artifacts open side-by-side**
   - When possible, keep the spreadsheet, memo, and deck open together.
   - When an assumption changes, update the dependent chart and narrative references.

3. **Use Outlook drafts as the “last mile”**
   - Let Claude draft replies and meeting invites.
   - Review drafts before sending.

## Admin considerations (enterprise)
- Deployment can be handled via Microsoft admin tooling and AppSource listings.
- Organizations may configure observability via OpenTelemetry and usage reporting via an Analytics API.

## Source
- https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook
