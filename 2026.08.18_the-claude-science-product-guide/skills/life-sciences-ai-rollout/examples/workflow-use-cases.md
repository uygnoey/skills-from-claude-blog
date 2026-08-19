# Function and workflow use cases

The workbench is built to handle a scientist's most analysis-heavy work and repetitive workstreams: pipeline assembly, database wrangling, and figure iteration, so the scientist's time goes to design decisions and results interpretation. Below is what that looks like across the research lifecycle, with the adjacent surfaces noted where the work crosses into document and submission territory.

## Discover and plan

Early-stage work is reading, reconciling, and designing — across literature, public databases, and the lab's prior results.

- Literature review and synthesis across primary sources, with citation verification by the background reviewer.
- Target and indication assessment from PubMed, ChEMBL, ClinicalTrials.gov, Open Targets, and internal program files.
- Experiment and protocol design, construct design, and assembly strategy for ordering.
- Competitive trial scans cross-referenced with preclinical model availability.
- Hypothesis generation against pathway and ontology references.

## Analyze

Analysis is where most of the toil lives. End-to-end pipelines run with kernels that persist, agents that QC their own outputs, and branching for alternative approaches.

- Single-cell RNA-seq clustering, marker identification, and treatment-response analysis.
- Genomics from FASTQ through alignment, QC, and variant calling.
- CRISPR screen design and analysis.
- Proteomics quantitation and interpretation, protein structure prediction, and homolog search.
- Cheminformatics: ADMET prediction, similarity search, structural alert flagging.
- Phylogenetic and evolutionary analysis.
- Parameter sweeps and ML modeling dispatched to SLURM or remote GPU.

## Polish and publish

Results become defensible outputs: figures with provenance, methods sections that match the code, manuscripts edited in place.

- Surgical figure iteration in plain language, with every version saved.
- Methods-section drafting from the artifact's provenance bundle.
- Manuscript drafting and editing with live LaTeX and Markdown rendering.
- Progress reports and PI briefings synthesized from session history and lab notes.

## Adjacent document and regulatory work

Once results leave the lab, the surrounding surfaces (the desktop cross-app surface and the Microsoft 365 add-ins) pick up the document load — with qualified human review before anything enters a regulated record.

- Protocol and synopsis drafting against the sponsor shell; CSR section drafting from TLFs.
- CTD module authoring and gap analysis against current guidance.
- SAE narrative drafting and QC; medical information response drafting.
- SOP drafting, deviation write-ups, and inspection-readiness summaries.

## Worked example — the first pilot session

The shape of a first session that converts a skeptic:

1. Point the agent at a folder of FASTQ files or an AnnData object already sitting on the lab's machine.
2. Ask for QC and clustering. The agent drafts a step-by-step plan; the scientist reviews it, scopes it down, and approves.
3. The agent loads the dataset into a persistent kernel, runs QC, and produces a UMAP — then reads its own figure, spots an outlier cluster, and filters it before continuing.
4. The scientist asks, in plain language, for a colorblind-safe palette and a log-scale axis. The agent edits the exact code that produced the figure rather than regenerating something similar.
5. The scientist subsets to immune cells and redoes the marker analysis in the same session, with the kernel state intact.
6. The artifact carries its four-layer provenance bundle: description, reproducible code, the conversation, and an environment snapshot — which is what a different scientist needs to re-run it cold four weeks later.

## Source

- https://claude.com/blog/the-claude-science-product-guide
