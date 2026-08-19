**English** · [한국어](./life-sciences-deployment.ko.md) · [Español](./life-sciences-deployment.es.md) · [日本語](./life-sciences-deployment.ja.md)

# Deploying an AI research workbench in life sciences

A practical deployment guide, distilled from the Claude Science product guide.

## The problem this addresses

Deloitte's 2026 Life Sciences Outlook, a survey of 280 biopharma and medtech leaders, found that 78% expect AI to play a central role in driving major change this year — yet only 14% report full implementation of AI tools into daily workflows, with another 40% still working toward it. Anthropic's own internal research, drawn from interviews with researchers across chemistry, physics, biology, and computational fields, found that 91% of scientists want more AI in their research, while 79% named trust and reliability as their number-one barrier to adoption.

The gap is structural. A biologist's day spans literature, experiment design, data wrangling, analysis, figures, and writing, but the tools span PubMed, Jupyter, R, a cluster terminal, scientific data renderers, and spreadsheets. The labs pulling ahead are not the ones with the most compute or the biggest bioinformatics teams — they are the ones that have collapsed the distance between a scientist's question and a defensible result.

## Step 1 — Choose the surface before you choose the rollout

Claude Science is the surface built for scientists. The other surfaces cover the document, software, and enterprise work that surrounds discovery. Most organizations deploy more than one, and the reliable dividing line is the *output*:

| Output | Surface |
|---|---|
| An analysis, a figure, a result | **Claude Science** — local app on macOS/Linux, dispatching to SSH, SLURM, or cloud compute |
| A quick answer or a draft | **Claude Chat** — browser, desktop, mobile |
| A document spanning folders and apps | **Claude Cowork** — desktop app across local files and connected systems |
| In-place drafting and redlining in Office | **Claude for Microsoft 365** — add-ins plus the M365 connector |
| Software that ships to other teams | **Claude Code** — terminal and IDE |
| A system integration (ELN, LIMS, CTMS, safety, RWE) | **Claude Platform** — API, including via Bedrock, Vertex AI, Foundry |
| A hosted, long-running agent | **Claude Managed Agents** — scoped permissions, full execution tracing |

Run this conversation with the functional leads before the first install, so medical writing, regulatory, and scientific computing know what they are getting and when.

## Step 2 — Understand where it runs

Claude Science is a standalone application for macOS and Linux that runs a **local daemon with its UI in the browser** — the same model as a Jupyter notebook, except the agent is driving. It installs wherever the data lives: a laptop, a lab Linux box, an HPC login node, or a cloud VM in your tenancy. Data, compute environments, and agents stay on that machine; scientists connect from a laptop browser over an SSH tunnel when the daemon runs remotely.

When a job needs bigger hardware, the agent dispatches it from the same session to the lab's own GPU box, an SSH host, a SLURM cluster (SLURM is auto-detected and batch directives are written automatically), or a serverless GPU account the user supplies.

Agents can be pointed at any local folder — FASTQ files, AnnData objects, Seurat objects — and connect natively to S3, GCS, GitHub, and institutional literature access. Conda and pip environments are managed per specialist; sessions, kernels, and artifacts persist across reboots.

## Step 3 — Know what makes the analysis defensible

Five design choices are what let the output survive review:

1. **Persistent kernels.** A dataset is loaded into a Python or R kernel once, then explored rather than re-loaded. Agents also see their own plots — every figure is fed back into the agent's context, so it runs QC on its own output.
2. **Four-layer provenance on every artifact.** A human-readable description of what was done, the exact reproducible code, the conversation and reasoning that led there, and a snapshot of every package and version used.
3. **A background reviewer.** A separate reviewer agent reads each session's transcript while the primary agent works and flags any claim it cannot trace to evidence, inline at the suspect sentence. It runs every session by default.
4. **Plans before actions, visible permissions.** Each task is drafted as a step-by-step plan awaiting approval; the plan stays visible as an editable checklist. New website, folder, or code execution each raise an approval card — once, for this project, or always — reviewable and revocable from one screen. Underneath sits an OS-level sandbox with deny-by-default network egress and a human-approval broker gating thirteen action kinds.
5. **Built-in biosecurity safeguards.** Biosecurity rules ship unconditionally in every agent's system prompt, a per-turn bio trajectory classifier runs in the binary and cannot be disabled, and the product completed external red-teaming and Anthropic Safeguards review before public release.

## Step 4 — Lay the foundation

Because the product runs locally, the foundation phase is about getting it next to the right data and compute rather than standing up cloud tenancy.

- **Decide the daemon host pattern** and confirm scientists can reach that host from their browser.
- **Have Research IT review** the OS-level sandbox, the deny-by-default network egress allowlist, and the human-approval broker that gates code execution, file access, and remote compute.
- **Do the account setup**: the same SSO and SCIM work as any other surface, plus one extra step — an admin must enable Claude Science before any user can download or sign in. On Team, under admin settings → capabilities. On Enterprise, create a role including the Claude Science permission, assign it to the pilot group, *then* enable the capability, so access is scoped from day one.
- **Scope governance in parallel.** For groups working with NIH-controlled data, patient-level data, or sponsor IP that cannot leave the lab's machines, the local-daemon model is what makes deployment possible where a SaaS product would not be — but quality, IT security, and data privacy should review the install footprint, the network allowlist, and the compute-dispatch targets before the first scientist points it at a controlled-data folder.
- **Pick pilot teams** with a motivated lead already pushing on AI, whose work is analysis-heavy and standard-shape. Computational biology and bioinformatics groups are the natural starting point; wet-lab scientists and PIs follow quickly once they see a colleague run an analysis they could not have run themselves.

> **Pro-tip:** the first session matters. A scientist who opens the tool, points it at a folder of FASTQ files, approves the plan, and gets a clustered UMAP with the code and environment captured underneath will come back. A scientist who opens it without data in reach will close it. Make sure the install lands next to real data.

## Step 5 — Run the pilot against defined criteria

At this stage champions are running real analyses on real lab data, measured against criteria defined up front:

- **Cycle time** — how long the pilot analysis took before, and how long it takes now, on the same dataset class.
- **Keep rate** — how often a scientist or PI trusts the result without re-running it by hand.
- **Cold-reproduce rate** — hand a week-one artifact's provenance bundle to a different scientist in week four and confirm they can re-run it cold.

**The strongest qualitative signal is champions saving their own skills.** A bioinformatician wraps the lab's internal normalization pipeline so every future session inherits it; a group lead wraps the lab's LIMS API. Those skills become the lab's catalog and can be shared across the organization.

Adjacent surfaces typically come online during this phase: medical writing and regulatory groups ask for Cowork and the Microsoft 365 add-ins; scientific computing asks for Claude Code for the production pipelines downstream. Run those as parallel tracks rather than gating them on the science pilot.

> **Pro-tip:** schedule weekly check-ins with pilot teams. Edge cases surface fast — a database schema the connector does not handle, a cluster scheduler quirk, a renderer that does not cover a niche file format — and the catalog is designed to be extended in response.

## Step 6 — Scale, with governance settled first

Skills and specialists that worked during the pilot roll out to additional groups, and Research IT moves from per-lab installs to a managed deployment pattern: a standard daemon host per group, a vetted network allowlist, a curated skill catalog seeded from the pilot, and a defined set of compute-dispatch targets.

Skills compound across groups because so much computational biology shares structure: a single-cell skill built in oncology is most of the way to one built in immunology. New hires start on day one with the lab's encoded pipelines rather than building them from scratch.

Decide before scale, not after:

- who owns each skill in the catalog,
- how a skill is QC'd before it is shared beyond its author's group,
- how provenance bundles are retained for analyses feeding regulatory or publication outputs,
- how the network allowlist is reviewed when a group requests a new external database.

> **Pro-tip:** for analyses that will feed a regulatory submission or a publication, treat the four-layer provenance bundle as a controlled record. The description, code, conversation, and environment snapshot together are what a reviewer, an auditor, or a journal will want to see — agree where those bundles are stored and for how long.

## Phase summary

| Phase | Actions | What you'll see |
|---|---|---|
| **Foundation** | IT and data-governance review of local install, sandbox, and network allowlist. Decide daemon host pattern. Identify 2–3 champion groups in computational biology or bioinformatics. Confirm SSO/SCIM and plan tier. | Champions reporting back use cases. First "this would have taken me three weeks" moments. |
| **Pilot** | Champions run real analyses on real lab data. Weekly check-ins. Measure cycle time, keep rate, and cold-reproduce rate. Stand up Cowork and M365 for adjacent document functions in parallel. | Measurable time savings. Champions saving custom skills and specialists. Wet-lab scientists and PIs joining behind the computational leads. |
| **Scale** | Managed daemon host pattern. Curated org skill catalog. Vetted network allowlist and compute-dispatch targets. Agreed provenance-retention policy for regulated and publication-bound analyses. Onboard the next wave of groups. | Skills shared across therapeutic areas. New hires ramping on encoded pipelines. Declining "can someone help me run this" requests to the bioinformatics core. |

## What the field looks like

- **Novo Nordisk** built NovoScribe, a generative AI platform powered by Claude that automates the creation of clinical study reports, device verification protocols, and patient materials. Clinical documentation that previously took more than ten weeks now reaches a reviewable first draft in roughly ten minutes. "Claude has helped us cut writing times on CSRs by 90% so we can get documentation directly into human hands for review and approval." — Waheed Jowiya, Digitalization Strategy Director, Novo Nordisk
- **The Garvan Institute of Medical Research** has adopted Claude across research, operations, and administration, with more than twenty software engineers and data scientists using agentic development tools for drug discovery research, rare disease diagnosis through multi-agent systems that interpret genetic variants, and data analysis across genomics projects. "Claude Code has completely transformed the way that I work as a scientist and as a leader." — Daniel MacArthur, Professor, Garvan Institute
- **Sanofi** has deployed Claude enterprise-wide inside its internal Concierge application, now used by the majority of employees daily across the value chain.

## Known limits to state up front

The guide is explicit about the boundaries, and stating them early is what keeps a pilot from stalling on an unanswered compliance question:

- Research use only; **not designed for clinical or diagnostic decision-making**.
- **Not a validated system** for GxP. Deploy in research, analysis, and draft-support roles with a qualified reviewer approving every output before it enters a validated record, a submission, or a publication.
- **Not HIPAA-ready at launch**; readiness is on the post-launch roadmap.
- NIH controlled-access datasets typically require the analysis environment to meet NIST SP 800-171 controls; the product has not yet been assessed against that standard.
- **Windows is not supported**; the endpoint install is a signed user-space daemon plus a browser UI, with no kernel components.
- **Not available through Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.**
- **Zero Data Retention does not apply** — the product is stateful, since sessions, artifacts, and provenance bundles require storage to function. ZDR is available on the Claude Platform and Claude Code for approved customers.
- Usage is **token-intensive**; heavy individual users may need Max-tier limits. There is no separate license and no free tier — it draws down the user's existing plan.
- Public databases and third-party resources carry their own licenses; commercial use is the organization's responsibility to verify.
- Roadmap items are subject to change and do not represent a commitment.

## Source

- https://claude.com/blog/the-claude-science-product-guide
