---
name: life-sciences-ai-rollout
description: Plan and run a staged rollout of an agentic AI research workbench inside a life sciences organization — choosing the right surface for each kind of work, getting the install next to real data and compute, and moving from foundation to pilot to scale with metrics that show it is working. Use when a research org is deciding where AI fits across analysis, document, and pipeline work, when Research IT must review install footprint and governance before controlled data is touched, or when a pilot needs measurable criteria rather than enthusiasm.
---

# Rolling out an AI research workbench in life sciences

A biologist's day spans literature, experiment design, data wrangling, analysis, figures, and writing — but the tools span PubMed, Jupyter, R, a cluster terminal, scientific data renderers, spreadsheets, and more. The labs pulling ahead are not the ones with the most compute or the biggest bioinformatics teams; they are the ones who have collapsed the distance between a scientist's question and a defensible result.

This skill covers how to deploy an AI workbench that runs next to the lab's data and produces results that can be traced, reproduced, and defended.

> Scope note: the source guide describes a research tool, explicitly not intended for clinical or diagnostic decision-making, and not a validated system for regulated records. Everything below assumes a qualified human reviews any output before it enters a validated record, a regulatory submission, or a publication.

## Instructions

### 1. Decide which surface does which work — before you deploy anything

Most organizations deploy more than one surface, and the common rollout failure is treating them as competitors. The dividing line is the *output*:

- The output is an **analysis, a figure, or a result** → the science workbench.
- The output is **software that ships to other teams** → the coding CLI.
- The output is a **document that spans folders and apps** (a study folder, a submission section) → the desktop cross-app surface, or the in-place Office add-ins when the work happens inside Word, Outlook, Excel, and PowerPoint.
- The output is a **quick answer or a draft** → the chat interface.
- The output is a **system integration** (ELN, LIMS, CTMS, safety, RWE) → the API platform, and its hosted-agent service when the integration should run as a long-lived agent.

Work through [references/surface-selection.md](references/surface-selection.md) with the functional leads before the first install, so adjacent groups know what they are getting and when.

### 2. Put the install next to the data

The workbench runs as a local daemon with its UI in the browser — the same model as a notebook, but the agent is driving. Install it where the data lives: a scientist's laptop, a lab Linux box, an HPC login node, or a cloud VM in your own tenancy. Scientists connect from a laptop browser, over an SSH tunnel when the daemon runs remotely.

Decide two things in the foundation phase:

1. **The daemon host pattern.** Per-scientist laptop, per-group Linux box, or per-group cloud VM. This is the decision Research IT will have to support at scale, so make it once.
2. **The compute-dispatch targets.** Which GPU hosts, SSH hosts, SLURM clusters, or serverless GPU accounts a given group's install is permitted to reach. Dispatch is gated by the approval broker, so this is enforceable.

The local-daemon model is what makes deployment possible in environments where uploading data is not an option. It is not a substitute for a data-governance review — see step 5.

Architecture details, including the five design choices that make the analysis reviewable, are in [references/product-architecture.md](references/product-architecture.md).

### 3. Enable it deliberately, scoped to the pilot

Account setup is the same SSO and SCIM work as any other surface, plus one extra step: **an admin must enable the product before anyone in the org can download or sign in.**

- On a Team plan: turn it on under admin settings → capabilities.
- On an Enterprise plan: create or edit a role that includes the product permission, assign that role to the pilot group, *then* enable the capability. Access is scoped to the pilot from day one rather than org-wide.

Do the Enterprise version even if you intend to go broad later. Scoping down after the fact is harder than scoping up.

### 4. Pick pilot teams by the shape of their work, not by seniority

Look for a motivated lead who is already pushing on AI, and work that is analysis-heavy and standard-shape. Computational biology and bioinformatics groups are the natural starting point. Wet-lab scientists and PIs follow quickly once they see a colleague run an analysis they could not have run themselves.

Pick work where the value is obvious in the first session: a single-cell dataset that would otherwise take three weeks, a CRISPR screen analysis, a literature synthesis ahead of a program review.

**The first session decides adoption.** A scientist who points the tool at a folder of real data, approves the plan, and gets back a result with the code and environment captured underneath will come back. A scientist who opens it with no data in reach will close it. Make sure the install lands next to real data.

### 5. Run governance in parallel, not after

For groups working with controlled-access data, patient-level data, or sponsor IP that cannot leave the lab's machines, quality, IT security, and data privacy should review three things **before the first scientist points the tool at a controlled-data folder**:

- the install footprint,
- the network egress allowlist,
- the compute-dispatch targets.

Answer the standing questions from [references/it-security-faq.md](references/it-security-faq.md) in your own terms — including the limits, which are as important to state as the capabilities. Do not let a pilot get ahead of an unanswered compliance question; the answer arriving late is what turns a successful pilot into a stalled one.

### 6. Measure the pilot on three things

Define the criteria up front and measure the same dataset class before and after:

1. **Cycle time** — how long the analysis took before, and how long it takes now.
2. **Keep rate** — how often a scientist or PI trusts the result without re-running it by hand.
3. **Cold-reproduce rate** — take an artifact produced in week one, hand its provenance bundle to a different scientist in week four, and confirm they can re-run it cold.

Use [templates/pilot-scorecard.md](templates/pilot-scorecard.md) to record these per group.

**The qualitative signal that matters most: champions saving their own skills.** A bioinformatician wraps the lab's internal normalization pipeline so every future session inherits it; a group lead wraps the lab's LIMS API. Those skills become the lab's catalog. When this starts happening unprompted, the pilot is working.

Schedule weekly check-ins. Edge cases surface fast — a database schema the connector does not handle, a cluster scheduler quirk, a renderer that does not cover a niche file format — and the catalog is designed to be extended in response.

### 7. Let adjacent surfaces come online as parallel tracks

During the pilot, medical writing and regulatory groups watching it will ask for the document surfaces, and scientific computing will ask for the coding CLI for the production pipelines downstream of the analysis. Run those as parallel tracks. Do not gate them on the science pilot finishing.

### 8. Settle governance before you scale, not after

At scale, Research IT moves from per-lab installs to a managed deployment pattern: a standard daemon host per group, a vetted network allowlist, a curated skill catalog seeded from the pilot, and a defined set of compute-dispatch targets.

Four questions must have owners before the next wave of groups onboards:

- Who owns each skill in the catalog?
- How is a skill QC'd before it is shared beyond its author's group?
- How are provenance bundles retained for analyses that feed regulatory or publication outputs?
- How is the network allowlist reviewed when a group requests a new external database?

For analyses bound for a submission or a publication, treat the four-layer provenance bundle — description, code, conversation, environment snapshot — as a controlled record. Agree where those bundles are stored and for how long.

Skills compound across groups because so much computational biology shares structure: a single-cell skill built in oncology is most of the way to one built in immunology. New hires start on day one with the lab's encoded pipelines rather than rebuilding them.

Track the whole sequence with [templates/adoption-roadmap.md](templates/adoption-roadmap.md).

### 9. Teach the skill-versus-connector distinction early

- **Connector** — when the answer lives in the organization's own systems (ELN, CTMS, a document repository) and entitlements matter. Connectors authenticate as the end user and respect entitlements at the project and folder level, so the agent only sees what the scientist already has access to.
- **Scientific data skill** — when the answer lives in the public record and the value is in querying it precisely, reproducibly, and in combination with other sources.

Most real questions use both: pull internal context through a connector, ground it against public reference data through a skill, and return an analysis the scientist can verify line by line. The available skill families are catalogued in [references/scientific-data-skills.md](references/scientific-data-skills.md).

Public databases and other third-party resources are governed by their own licenses and use terms. Confirm that your intended use — including commercial use — complies with those terms and your own entitlements before a group depends on a source.

## Examples

### Example 1 — scoping the first install

> **Ask:** "We want to start with our immuno-oncology computational group. Where do we install it?"

Work the two foundation decisions in order. The group's scRNA-seq and CRISPR screen data sits on a shared lab Linux box behind the institutional firewall, so the daemon goes on that box rather than on individual laptops — the data does not move, and one host is one governance review instead of eight. Scientists reach the browser UI over an SSH tunnel. Dispatch targets are limited to the institutional SLURM cluster; the serverless GPU path stays off until finance and security have looked at it.

Then run the enablement as the Enterprise pattern: a role carrying the product permission, assigned only to the seven people in the group, before the capability is switched on.

### Example 2 — the pilot review that decides whether to scale

> **Ask:** "The pilot is eight weeks in. How do we tell if it worked?"

Fill in [templates/pilot-scorecard.md](templates/pilot-scorecard.md) for the group and read it against three questions:

- **Cycle time** — the marker-identification analysis that took three weeks now takes two days. Real.
- **Keep rate** — the PI still re-runs every clustering result by hand. Not yet; find out whether the blocker is trust in the method or an unreviewed step in the plan.
- **Cold reproduce** — a week-one UMAP handed to a different scientist in week four re-ran from its provenance bundle without help. Real.

Then check the qualitative signal: two people in the group have saved the lab's normalization pipeline and the LIMS wrapper as skills, without being asked. That is the strongest evidence to scale, and those two skills are the seed of the org catalog.

### Example 3 — a question that crosses public and internal data

> **Ask:** "Which of our internal program targets have a pharmacogenomic liability we should know about?"

This is the skill-plus-connector case from step 9. Internal program files come through a connector that authenticates as the scientist, so only in-scope programs are visible. Public pharmacogenomic evidence comes through a scientific data skill that writes and executes the query against the source of record. The agent chains them inside one analysis and returns a result with provenance on each claim, which the background reviewer then checks for statements it cannot trace to evidence.

See [examples/workflow-use-cases.md](examples/workflow-use-cases.md) for the fuller set of use cases across discover, analyze, and publish.

## Source

- https://claude.com/blog/the-claude-science-product-guide
