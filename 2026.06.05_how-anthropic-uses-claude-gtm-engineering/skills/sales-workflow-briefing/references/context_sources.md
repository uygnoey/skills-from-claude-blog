# Context sources checklist

This post describes pulling context at generation time from multiple tools and shared sources.

## Typical sources
- Email threads (e.g., Gmail drafts + thread history)
- Calendar events (agenda, attendees)
- CRM records (account status, open opportunities)
- Call recordings and notes (e.g., sales calls)
- Shared docs (e.g., team Drive folder)
- Public documentation (queried via web search)

## Implementation notes
- Prefer the source of truth (CRM, docs) over memory.
- Keep a shared folder or shared document set for reusable context.
- If a source is unavailable, explicitly note it and proceed with what you have.
