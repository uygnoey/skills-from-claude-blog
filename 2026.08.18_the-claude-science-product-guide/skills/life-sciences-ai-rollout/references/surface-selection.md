# Which surface for which work

Several Claude surfaces serve life sciences teams. The science workbench is the surface built for scientists; the others cover the document, software, and enterprise work that surrounds scientific discovery. Most organizations deploy more than one.

## The dividing line

Reach for the science workbench when the output is **an analysis, a figure, or a result**. Reach for the coding CLI when the output is **software that ships to other teams**. Everything else follows from where the work happens and who does it.

## Product matrix

| Surface | Best for | Primary users | Where it runs | Example task |
|---|---|---|---|---|
| **Claude Science** | End-to-end research analysis with full provenance — literature, pipelines, figures, writeup | Computational biologists, bioinformaticians, research scientists, PIs | Local app (macOS, Linux); dispatches to SSH, SLURM, or cloud compute | "Run QC and clustering on this scRNA-seq dataset, show me the UMAP, then subset to immune cells and redo the marker analysis." |
| **Claude Chat** | Conversational drafting, day-to-day questions and answers | All staff | Browser, desktop, mobile | "Summarize this document and flag any contradictory findings." |
| **Claude Cowork** | Cross-app study and document work touching files and multiple systems | Medical writing, clinical operations, regulatory, medical affairs | Desktop app | "Review the SAE narratives in this folder against the protocol and flag any that meet expedited reporting criteria." |
| **Claude Code** | Agentic software engineering inside a repository | Scientific computing, biostatistics programming, platform engineering | Terminal, IDE | "Migrate or refactor large codebases." |
| **Claude for Microsoft 365** | In-place drafting, redlining, and review across the Microsoft suite | Medical writing, regulatory, clinical operations | Word, Outlook, Excel, PowerPoint (add-ins); Teams, SharePoint, OneDrive (connector) | "Redline Module 2.5 against the new nonclinical data and produce a change summary for the submission team." |
| **Claude Platform (API)** | Embedding Claude into ELN, LIMS, CTMS, safety, or RWE systems | Scientific computing, R&D IT, clinical systems | Anthropic API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry | "Integrate Claude into our ELN to draft experiment summaries from structured results with source citations." |
| **Claude Managed Agents** | Running custom agents as hosted cloud services | Platform and scientific computing teams | Claude Platform (hosted) | "Deploy our Literature Surveillance agent as a managed service with scoped database access and audit tracing." |

## Notes per surface

**Claude Science** — an application for the digital steps of research: literature review, experiment design, data analysis, figure generation, and writeups. It runs locally next to the lab's data and compute, ships with domain capabilities across genomics, single cell, proteomics, structural biology, cheminformatics, and more, and tracks the provenance of every artifact so results can be reproduced and defended.

**Claude Chat** — the web and desktop chat interface for quick queries and drafting. A medical writer might pressure-test a mechanism-of-action narrative; a discovery scientist might summarize a stack of papers ahead of a program review.

**Claude Cowork** — a desktop application where Claude works across local files and connected systems (for example Benchling, Veeva, Microsoft 365, PubMed) to complete multi-step document projects. Reach for it for study- and submission-level work that spans folders and apps: reviewing every site monitoring report in a study folder, reconciling a TMF section, drafting a CSR section from a folder of TLFs.

**Claude Code** — the command-line interface for software engineering teams, supporting scientific computing, biostatistics programming, and platform groups building and maintaining production pipelines and internal tools under version control.

**Claude for Microsoft 365** — puts Claude inside Word, Outlook, Excel, and PowerPoint via add-ins, and lets Claude search Outlook, Teams, SharePoint, and OneDrive via the M365 connector.

**Claude Platform** — the API for organizations embedding Claude into ELN, LIMS, CTMS, safety, and RWE systems. **Claude Managed Agents** runs any agent built on the Platform as a hosted service with long-running sessions, scoped permissions, and full execution tracing — for example a Literature Surveillance agent monitoring PubMed and ClinicalTrials.gov for competitive readouts across a portfolio.

## Source

- https://claude.com/blog/the-claude-science-product-guide
