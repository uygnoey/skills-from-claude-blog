# The scientific data skill catalog

The workbench ships with configurable capabilities for common scientific workflows, backed by optional connections to **more than sixty scientific databases** and roughly **150 curated skills**. When a project spans domains, it plans and routes across them automatically. Information about network domains, connectors, and skills is found in Settings.

**Why these are skills and not retrieval.** The pre-built Python skills let Claude write and execute a query against the source of record and return results with provenance. Because they run code rather than retrieve documents, they can be **chained**: pull a gene's variants from one database, cross-reference drug interactions in another, and check expression across cell types in a third, inside a single analysis. Each skill is open source, so computational teams can inspect the query logic, pin versions, or extend a skill with their organization's own filters and output formats.

> Licensing: public databases and other third-party resources are governed by their own licenses and use terms. Organizations are responsible for ensuring their use — including commercial use — complies with those terms and their own entitlements.

## Genes, variants, and annotation

| Skill | Source | Use when |
|---|---|---|
| `gene-database` | NCBI Gene / Datasets | Looking up a gene by symbol or ID — RefSeqs, GO terms, genomic location, associated phenotypes, batch retrieval. |
| `biothings-database` | BioThings.io (MyGene, MyVariant, MyChem, MyDisease) | Resolving identifiers across databases, or pulling aggregated annotation for a gene, variant, compound, or disease in one call. |
| `ena-database` | European Nucleotide Archive | Retrieving raw sequence data — FASTQ reads, assemblies, sample metadata — by accession. |
| `harmonizome-database` | Harmonizome | Asking what a gene is associated with across 170+ functional genomics resources at once. |

## Expression and single-cell

| Skill | Source | Use when |
|---|---|---|
| `cellxgene-census` | CZ CELLxGENE Census | Filtering 125M+ cells by type, tissue, or disease and pulling expression matrices straight into scanpy or PyTorch. |
| `immgen-database` | ImmGen | Checking expression of a gene across mouse immune cell populations. |
| `allen-brain-database` | Allen Brain Atlas | Querying gene expression, connectivity, or spatial transcriptomics across mouse and human brain regions. |

## Oncology

| Skill | Source | Use when |
|---|---|---|
| `cosmic-database` | COSMIC | Searching somatic mutations, the Cancer Gene Census, mutational signatures, or fusion events. Requires institutional authentication. |
| `tcia-database` | The Cancer Imaging Archive | Pulling DICOM imaging series from public cancer imaging collections for radiomics or model training. |

## Pharmacology and safety

| Skill | Source | Use when |
|---|---|---|
| `clinpgx-database` | ClinPGx (PharmGKB) | Checking gene–drug interactions, CPIC dosing guidelines, or allele function for a pharmacogenomic question. |
| `fda-database` | openFDA | Searching adverse event reports, recalls, drug labels, device 510(k)/PMA records, or UNII identifiers. |

## Metabolomics

| Skill | Source | Use when |
|---|---|---|
| `hmdb-database` | Human Metabolome Database | Looking up any of 220K+ human metabolites — properties, biomarker associations, NMR/MS spectra, pathway membership. |
| `metabolomics-workbench-database` | Metabolomics Workbench | Searching 4,200+ public metabolomics studies, RefMet nomenclature, or running m/z lookups. |

## Neuroscience

| Skill | Source | Use when |
|---|---|---|
| `neuromorpho-database` | NeuroMorpho.Org | Retrieving neuron morphology reconstructions and morphometrics by species, brain region, or cell type. |
| `openneuro-database` | OpenNeuro | Finding and pulling BIDS-formatted MRI, fMRI, EEG, MEG, or PET datasets. |

## Multi-database toolkits

For exploratory work that crosses several sources, broader Python toolkits load as skills:

| Skill | Coverage | Use when |
|---|---|---|
| `bioservices` | 40+ services — UniProt, ChEMBL, PubChem, Reactome, QuickGO, KEGG, Ensembl, BioMart, and more | Running pathway analysis or ID mapping across many providers through one unified interface. |
| `gget` | 20+ databases — Ensembl, UniProt, NCBI, ARCHS4, Enrichr, OpenTargets, PDB, AlphaFold, BLAST | Quick one-liner lookups: gene info, enrichment, reference genome download, a fast BLAST. |
| `biopython` (`Bio.Entrez`) | All NCBI Entrez databases — PubMed, Gene, Nucleotide, Protein, SRA, Taxonomy, Assembly, BioProject | Anything behind NCBI E-utilities not covered by a more specific skill. |
| `hmmer` | Pfam, UniProtKB, Reference Proteomes | Profile and sequence searches — phmmer, hmmscan, hmmsearch, jackhmmer — for domain identification and remote homology. |
| `foldseek` | AlphaFold DB, PDB100, ESMAtlas, CATH | Searching by 3D structure rather than sequence, to find structural homologs the sequence would miss. |

## Extending the catalog

The catalog is opinionated but open. A lab can:

- save any working pipeline as a reusable skill,
- build a custom specialist for its own methods from inside any session,
- wrap an internal API once so every future session inherits it.

This is also the signal to watch for during a pilot: when champions start saving their own skills, the catalog becomes the lab's, and it compounds across groups.

## Skill or connector?

- **Connector** — the answer lives in the organization's own systems (ELN, CTMS, regulatory document repository) and entitlements matter.
- **Scientific data skill** — the answer lives in the public record and the value is querying it precisely, reproducibly, and in combination with other sources.

Most real questions use both: internal context through a connector, grounded against public reference data through a skill, returning an analysis the scientist can verify line by line.

## Source

- https://claude.com/blog/the-claude-science-product-guide
