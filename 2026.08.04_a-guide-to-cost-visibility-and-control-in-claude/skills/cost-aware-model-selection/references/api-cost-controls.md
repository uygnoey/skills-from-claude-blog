# Cost controls for building on the API

Four levers available in the Claude Console for developers. They are independent, and several
of them stack.

## Prompt caching

Stores reusable content across requests. On a cache hit, that content bills at approximately
**10% of the normal input rate**.

The lever works best where a large, stable prefix is repeated across many calls: a system
prompt, a taxonomy, a schema, a long set of instructions, a reference document. Structure
requests so the stable part comes first and the varying part comes last.

## Batch processing

Runs non-urgent jobs at **half price**. Suited to work with no interactive deadline — the
canonical example is overnight catalog classification.

**Batch discounts stack with caching.** A batched job over a cached prefix gets both reductions,
which is why moving a recurring bulk job to batch is usually the single largest available
saving.

## The effort parameter

Controls **reasoning intensity per call**.

- **Lower settings** — routing and extraction. Work where the answer is mostly determined by the
  input and there is little to weigh.
- **Higher settings** — final recommendations. Work where the model is genuinely deciding
  something.

The value of this lever is that it makes cost a per-step choice inside a pipeline rather than a
per-workload one. A ten-step pipeline does not need ten steps of peak-rate reasoning; it needs
one or two, and the parameter lets you choose which.

## The advisor strategy

Use a smaller model such as **Sonnet** for most of the work, and consult a frontier model only
at **critical decision points**. You pay premium rates only for the moments that carry high
judgment.

This is the same idea as the effort parameter applied across models rather than within one: the
expensive resource is called in, not left running.

## Combining them

These compose in a natural order for a bulk pipeline:

1. Move the job to **batch** if it has no interactive deadline — half price on everything below.
2. Put the stable instructions and reference material in a **cached prefix** — the repeated
   portion drops to roughly a tenth of input rate, and the batch discount still applies.
3. Run mechanical steps at **low effort**, reserving high effort for the steps that decide
   something.
4. Keep the pipeline on a smaller model and **escalate to a frontier model** only at the
   decision points, following the advisor strategy.

Each layer applies to a different part of the bill, so the savings do not compete with each
other. See [model-family.md](model-family.md) for choosing the base model the pipeline runs on.
