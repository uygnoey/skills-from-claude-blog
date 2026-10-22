# Maturity, rollout, ROI, and pitfalls — reference

Summarized from Anthropic's guide "Building an AI-native revenue organization" (PDF linked from the
2026-09-15 article). Paraphrased; consult the original for exact wording and diagrams.

## Why whole-team adoption matters
- Rolling out Claude differs from a SaaS rollout: seats and training are only the first step; returns
  grow as the organization extends more access and trust.
- Four-step progression: individual productivity gains → team workflows → department workflows →
  KPI/OKR gains.

## Maturity ladder
- Impact grows with the complexity of work Claude can do; complexity grows with access and trust.
- Movement up the ladder comes from: connecting team systems (e.g., Salesforce in Claude (beta),
  the Sales plugin); reps building fluency (single tasks → several workflows in parallel); workflows
  gaining access and autonomy (pasting call notes → forecast from live CRM data).
- Governance throughout: who can publish skills, what data each workflow can reach, who owns results.
- Mature state: departments rebuild workflows as plugins or managed agents pointed at KPIs/OKRs;
  Claude runs processes end to end with human oversight as needed.

## Setup decisions (before the pilot)
| Decision | Guidance |
|---|---|
| Owner | RevOps — owns CRM and systems, and pipeline/forecast reporting where results are measured |
| Systems | Connect call tools (e.g., Zoom, Granola, Gong) so Claude pulls data instead of reps uploading |
| IT | Workspace provisioning, SSO, admin consents (Salesforce, Microsoft 365); name an IT owner; agree dates before committing to a pilot date |
| Security | Start early; covers data boundaries, connector permission model, auditability, telemetry export |
| Metrics | One activity metric (briefs generated, opportunity updates written) + one revenue metric (pipeline per rep, cycle length); baseline; readout timeline |
| Spend | Limits by org/group/user; gate costlier capabilities by role; usage analytics from day one; champions get more headroom |
| Cohort | Two or three teams with motivated leads, not scattered volunteers; admin-level plugin provisioning |

## Rollout phases
- **Setup** — IT (workspace, SSO) and RevOps (first connectors, admin-provisioned plugins, using
  security decisions) work in parallel. Select champions with sales managers: two or three per
  department, or one per 25-50 users, with dedicated hours.
- **Pilot** — two or three use cases per team. Champions demo on live accounts, staff office hours,
  write the first skills. Early signal: number of champion-created skills pilot teams use regularly.
  Provide a starter pack; preload the Sales plugin settings file; the Salesforce plugin has an
  admin-enabled setup skill that identifies the rep's tools and configures the plugin on first run.
- **Scale** — pilot skills move to the shared team bundle; waves such as 25 → 150 → everyone; Claude
  output enters standing meetings (`/forecast` on the weekly forecast call, QBR decks in Claude in
  PowerPoint).

Field practices cited: Cyera ran a full-day kickoff livestream with 20 department-specific sessions
and twice-weekly office hours, and rolled out company-wide in 17 days with 40 tools connected after
data-mapping exercises. Cox seeded champions and scaled via train-the-trainer.

## Measuring ROI
- Returns appear in order: usage → output → CRM-trackable outcomes → cost.
- Three groups: **efficiency** (same work faster; Workato deal prep 3-4 h → 45 min), **expansion**
  (more accounts covered, more pipeline per rep), **new capabilities** (e.g., long-tail outreach no
  rep had time for).
- Compare pilot vs non-pilot teams in the same quarter (pipeline per rep, cycle length, win rate)
  instead of before/after.
- Scale signals: reps still producing after novelty fades; quality checks holding; pilot teams
  outperforming on the chosen outcome metric, even by a small gap.
- After a full quarter: daily spend per rep next to pipeline per rep, cycle length, win rate. Lead
  budget talks with expansion and new capabilities; "hours saved" caps value at the cost of those hours.
- Spend reading: high spend + high output is intended (champions). High spend + low output → coach
  first; lower the cap only if coaching fails.

## Pitfalls
| Pitfall | Prevention at setup |
|---|---|
| Pilot without an end date | Scale-decision date on the sponsor's calendar, a named decider, agreed criteria for "yes" |
| Seats scaled, champions not | Keep 1 champion per 25-50 users per wave; incoming managers name champions before provisioning |
| Spend ignored until the invoice | Limits by org/group/user before pilot; read usage analytics weekly |

## FAQ answers (condensed)
- Sales plugin connectors include HubSpot, Clay, ZoomInfo, Fireflies, Microsoft 365; Salesforce has a
  dedicated plugin (Salesforce in Claude) with the connection included. Connectors inherit permissions.
- Forecasts come from CRM pipeline data, so numbers trace to records; keep forecast-accuracy tracking
  and rep review before anything customer-facing ships.
- Versus suite-embedded AI: Claude works across the systems a deal touches and produces finished
  work; team methods become shared skills.
- Hours saved are the floor; larger returns are expansion and new capabilities.
- CIO/CISO approval goes through the pre-pilot security review; see "Deploying Claude Across Your
  Organization" and trust.anthropic.com.

## Customer results cited
- Cox Communications: 7x first-year return; lead validation/enrichment cost −86%; accuracy 18% → 97%.
- Cyera: 88% of ~1,500 employees use Claude weekly; BDR outreach skill built from top performers.
- Anthropic: ~80% of its sales org adopted the Sales plugin within months; one leader with a
  4,000-account book saves ~90 min/day and has every account scored overnight; call-prep briefs in
  ~2 min instead of ~30.
