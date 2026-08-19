# Adoption roadmap — <organization / division>

Owner: <name>  ·  Started: <YYYY-MM-DD>  ·  Last reviewed: <YYYY-MM-DD>

Most successful rollouts follow the same sequence: lay the foundation, run a pilot inside one or two computational groups, then scale out across R&D — with the document-facing surfaces coming online alongside as adjacent functions pull for them.

---

## Phase 1 — Foundation

**Goal:** get the tool next to the right data and compute, with governance reviewed in parallel.

| Action | Owner | Status | Notes |
|---|---|---|---|
| IT and data-governance review of local install, sandbox, and network allowlist | | | |
| Decide the daemon host pattern (laptop / lab box / HPC login node / cloud VM) | | | |
| Define permitted compute-dispatch targets per group | | | |
| Confirm SSO / SCIM and plan tier | | | |
| Admin enablement — Team: capabilities setting. Enterprise: role with the product permission, assigned to the pilot group, *then* enable the capability | | | |
| Identify 2–3 champion groups in computational biology or bioinformatics | | | |
| Confirm the first install lands next to real data | | | |

**What you'll see:** champions reporting back use cases; the first "this would have taken me three weeks" moments.

**Pro-tip:** the first session matters. A scientist who points the tool at a folder of real data, approves the plan, and gets a result with the code and environment captured underneath will come back. One who opens it without data in reach will close it.

---

## Phase 2 — Pilot

**Goal:** real analyses on real lab data, measured against criteria defined up front.

| Action | Owner | Status | Notes |
|---|---|---|---|
| Champions run real analyses on real lab data | | | |
| Weekly check-ins with each pilot group | | | |
| Measure cycle time, keep rate, and cold-reproduce rate (see the pilot scorecard) | | | |
| Stand up the document surfaces for adjacent functions **in parallel**, not gated on this pilot | | | |
| Stand up the coding CLI for scientific computing's production pipelines | | | |
| Track which skills champions save on their own | | | |

**What you'll see:** measurable time savings; champions saving custom skills and specialists; wet-lab scientists and PIs joining behind the computational leads.

**Pro-tip:** schedule the weekly check-ins. Edge cases surface fast — a database schema the connector does not handle, a cluster scheduler quirk, a renderer that does not cover a niche file format — and the catalog is designed to be extended in response.

---

## Phase 3 — Scale

**Goal:** move from per-lab installs to a managed deployment pattern, with governance settled before the next wave.

| Action | Owner | Status | Notes |
|---|---|---|---|
| Standard daemon host pattern per group | | | |
| Curated org skill catalog, seeded from the pilot | | | |
| Vetted network allowlist and defined compute-dispatch targets | | | |
| Decide who owns each skill in the catalog | | | |
| Decide how a skill is QC'd before sharing beyond its author's group | | | |
| Agree provenance-bundle retention for regulated and publication-bound analyses | | | |
| Define how the network allowlist is reviewed when a group requests a new external database | | | |
| Onboard the next wave of groups | | | |

**What you'll see:** skills shared across therapeutic areas; new hires ramping on encoded pipelines; declining "can someone help me run this" requests to the bioinformatics core.

**Pro-tip:** for analyses that will feed a regulatory submission or a publication, treat the four-layer provenance bundle — description, code, conversation, environment snapshot — as a controlled record. Agree where those bundles are stored and for how long.

---

## Open questions / blockers

| Question | Raised by | Needed by | Answer |
|---|---|---|---|
| | | | |

## Source

- https://claude.com/blog/the-claude-science-product-guide
