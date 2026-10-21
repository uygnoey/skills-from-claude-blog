**English** · [한국어](./dashboards-motion-rollout.ko.md) · [Español](./dashboards-motion-rollout.es.md) · [日本語](./dashboards-motion-rollout.ja.md)

# Rolling out Dashboards, Motion, and the Claude Design migration

A checklist for admins and team leads, based on the October 8, 2026 announcement.

## 1. Availability at a glance
| Feature | Status | Plans | Enterprise default |
|---|---|---|---|
| Claude Dashboards | Beta | Paid plans | Off (Organization settings > Artifacts) |
| Claude Motion | Beta | Team, Enterprise | Off (Organization settings > Artifacts) |
| Claude Docs, Slides, Design | Generally available | All plans, including Free | On by default from October 15 (can be enabled earlier) |

## 2. Before enabling Dashboards
- Decide which data platforms to connect (Amazon Redshift, BigQuery, ClickHouse, Databricks,
  Snowflake) and which other connectors (e.g. Salesforce) dashboards may draw on.
- Position Dashboards for quick, exploratory questions. Agree which BI tool receives a dashboard when
  a question needs deeper analysis (Amplitude, Grafana, Hex, Mixpanel, Omni, Perplexity, PostHog,
  Sigma; Databricks Genie, Looker, monday.com, Tableau listed as coming soon).
- Teach the verification habit: click a number to see its query, ask Claude to explain it, and check
  each chart's last-refresh time.

## 3. Before enabling Motion
- Motion is for explaining your own work: it animates text, charts, shapes, and images with code. It
  does not use a video generation model, so there is no generated footage and no AI-generated people.
- Output: MP4 download, or open in Adobe, Descript, HeyGen, Higgsfield, invideo, Luma AI, or Runway
  (Canva and Captions listed as coming soon).

## 4. Enterprise controls now available for artifacts
- CMEK support for artifacts.
- Admins choose which artifact templates the organization uses.
- Sharing outside the organization, or with anyone with the link, only if the admin allows it.

## 5. Claude Design migration (deadline: December 14)
Claude Design started at claude.ai/design; since September 16 it also works inside every Claude
conversation. The standalone site stays up until December 14.
- [ ] **Migrate design systems.** On the Artifacts page, click "Migrate team design systems". One
  migration brings over every design system in the organization; originals stay unchanged in the
  standalone version until it closes.
- [ ] **Projects.** No action needed yet; they keep working in the standalone version until it closes.
- [ ] **Save chats and comments.** They stay in the standalone version and won't be available after it
  closes.
- [ ] **Public links.** Links to standalone projects stop working when it closes; plan replacements.
- See the migration guide linked from the original post for details.

## Source
- https://claude.com/resources/articles/dashboards-and-motion
