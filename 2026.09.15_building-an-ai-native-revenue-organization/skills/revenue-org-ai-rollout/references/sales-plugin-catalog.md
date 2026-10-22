# Anthropic Sales plugin and related surfaces — reference

From the guide "Building an AI-native revenue organization" (2026-09-15).

## Commands
| Command | What it does |
|---|---|
| `/call-summary` | Processes call notes or a transcript, extracts action items, drafts the follow-up, writes an internal summary |
| `/forecast` | Builds weighted projections from pipeline data |
| `/pipeline-review` | Scores deal health and risk |

## Skills
| Skill | What it does |
|---|---|
| `account-research` | Web research on a company or person: intel, key contacts, recent news, hiring signals |
| `call-prep` | Account context, attendee research, suggested agenda, discovery questions |
| `daily-briefing` | Prioritized daily brief: meetings, pipeline alerts, email priorities, suggested actions |
| `draft-outreach` | Research the prospect first, then draft personalized email and LinkedIn messages |
| `competitive-intelligence` | Product comparison, pricing intel, recent releases, differentiation matrix, talk tracks |
| `create-an-asset` | Custom sales assets: landing pages, decks, one-pagers, workflow demos |

## Setup notes
- Initial setup interviews the rep and commits name, quota targets, product positioning, and
  competitor list to a settings file. Preload it for the pilot so commands work on day one.
- Works on web search and pasted context alone, but becomes useful once team tools are connected.
- Connectors respect each rep's existing permissions.
- Salesforce in Claude puts a rep's book of business in Claude and runs workflows end to end
  (renewal prep, QBR decks, pipeline coverage, meeting follow-up).
- Reps can write their own skills (e.g., a renewal-prep routine or forecast format); admins provision
  them in the team bundle; editing the file updates the skill for everyone.

## Other Claude surfaces named
- Claude for Excel — quota and comp models.
- Claude for PowerPoint — proposal and QBR decks.
- Claude Tag (beta) — questions and tasks in Slack.
