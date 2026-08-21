# The model family, and how to place a workload

Four primary models, matched to different kinds of work.

| Model | Fits |
|---|---|
| **Fable** | The hardest problems |
| **Opus** | Long-horizon work and coding |
| **Sonnet** | Everyday work and analysis |
| **Haiku** | High-volume and routine tasks |

## Placing a workload

The question is not "how big is this job" but "what kind of thinking does it require."

- **Does the task require judgment and reasoning?** Weighing options, resolving ambiguity,
  deciding what matters. Move up the family.
- **Is it high-volume straightforward processing?** Extraction, classification, formatting,
  routing. Move down the family.

Volume alone does not settle it. A million routine documents belong on Haiku. A hundred
genuinely hard decisions belong on Fable. Sorting by volume rather than by kind of work is how
workloads end up on the wrong model.

## Two failure modes

**Too small for the work.** Assigning a less capable model to complex reasoning often
*increases* final costs. The cost does not show up as a higher per-token rate — it shows up as
tokens consumed on retries and as human time spent on correction. The line item gets cheaper
while the outcome gets more expensive.

**Too large for the work.** Deploying a frontier model for basic document processing wastes
capabilities the task does not require. This failure is more visible on the invoice and less
damaging to quality, which is why it survives longer than it should.

## Two cross-cutting adjustments

Beyond picking a model, two controls tune how much you pay per unit of work:

- **Effort controls** — adjust how much the model *thinks* when solving a problem. This makes
  the model-choice decision less binary: a capable model at low effort is a different cost
  point from the same model at high effort. Set it per call, matched to what the call decides.
- **The advisor tool** — lets smaller models consult frontier models only when they encounter a
  difficult problem. Instead of choosing one model for the whole workload, most of the work
  runs cheap and the hard moments escalate.

Together these mean the model choice is rarely all-or-nothing. See
[api-cost-controls.md](api-cost-controls.md) for how they are applied on the API side.
