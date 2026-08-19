# How the workbench works, and why the analysis holds up

## Where it runs

A standalone application for macOS and Linux that runs a **local daemon with its UI in the browser** — the same model as a Jupyter notebook, but the agent is driving. Install it wherever the data lives: a laptop, a lab Linux box, an HPC login node, or a cloud VM in your own tenancy.

- Data, compute environments, and agents stay on that machine.
- Scientists connect from a laptop browser over an SSH tunnel when the daemon runs remotely; on Linux it can run headless.
- Files remain on the host and are read in place. Content the agent reads as part of an analysis is sent to the API as context, subject to the plan's data-use and retention commitments.
- What is installed on the endpoint is a signed binary running as a user-space daemon plus a browser UI. No kernel-level components. Windows is not currently supported.

## Compute dispatch

When a job needs bigger hardware, the agent dispatches it **from the same session** to:

- the lab's own GPU box,
- an SSH host,
- a SLURM cluster — SLURM is auto-detected and the batch directives are written automatically,
- a serverless GPU account the user supplies.

Dispatch targets are gated by the same approval broker, so Research IT can restrict which hosts a group's install may reach.

## What agents can reach locally

Agents can be pointed at any local folder — FASTQ files, AnnData objects, Seurat objects — and connect natively to S3, GCS, GitHub, and institutional literature access. Conda and pip environments are managed per specialist, and sessions, kernels, and artifacts persist across reboots.

## The five design choices that make the analysis reviewable

### 1. Persistent kernels

Agents load a dataset into a persistent Python or R kernel once; from then on they are exploring it, not re-loading it. Variables, dataframes, and loaded models stay in memory across the whole analysis.

Agents also **see their own plots**: every figure generated is fed back into the agent's context, so it runs QC on its own output — spotting the outlier cluster in its own UMAP and filtering it before moving on.

### 2. Full provenance on every artifact

Figures, tables, reports, and notebooks are first-class objects, not files to dig up afterward. Each ships with **four layers of history**:

1. a human-readable description of what was done,
2. the exact reproducible code that produced it,
3. the conversation itself and the reasoning that led there,
4. a snapshot of every package and version used.

This bundle is what a reviewer, an auditor, or a journal will want to see. For regulated or publication-bound work, treat it as a controlled record.

### 3. A background reviewer

A separate reviewer agent reads each session's transcript while the primary agent works, and flags any claim it cannot trace to evidence. Findings surface inline at the suspect sentence, and the agent fixes them before finishing. The reviewer runs every session by default and can also be triggered manually at any point.

### 4. Plans before actions, permissions you can see

Each task is drafted as a step-by-step plan that waits for approval before executing. The plan stays visible as a checklist and can be edited or scoped down while work runs.

Whenever an agent needs to reach a new website, open a folder, or run code, the same approval card appears — allow it **once**, **for this project**, or **always** — and every decision can be reviewed or revoked from a single permissions screen.

Underneath: an OS-level sandbox with deny-by-default network egress, allowlist proxy, SSRF and DNS-rebind defenses, and seccomp hardening. A human-approval broker gates thirteen action kinds, including code execution, network grants, host file access, deletions, MCP tool calls, remote compute dispatch, and skill persistence.

### 5. Built-in biosecurity safeguards

Biology is a dual-use domain. Biosecurity rules are written unconditionally into every agent's system prompt, a per-turn bio trajectory classifier runs in the binary and cannot be disabled by user or admin, and authentication is OAuth-only with no anonymous or API-key access. The product completed external red-teaming and Anthropic Safeguards review against CBRNE risk before public release. These sit on top of the sandbox and approval broker.

## Working with results

Scientists iterate on outputs in plain language: click a figure to drop an annotation, or just ask — drop the gridlines, make the axis log scale, switch to a colorblind-safe palette, re-run without the outliers. The agent reads the exact code that produced the artifact and **edits surgically rather than regenerating** something that looks roughly right. Every version is saved with its provenance intact, and a session can be forked from any point to explore two approaches in parallel without losing the original thread.

Built-in scientific renderers display protein structures, DNA sequences, multiple sequence alignments, genome tracks, and small molecules natively, alongside spreadsheets, interactive HTML, PDFs, notebooks, and live LaTeX and Markdown for manuscript editing.

## MCP connectors

The product is MCP-native: any MCP server — data warehouses, ELNs, ticketing, internal services — connects, and tools the rest of the organization already uses work here too. Connectors authenticate as the end user and respect entitlements at the project and folder level.

## Source

- https://claude.com/blog/the-claude-science-product-guide
