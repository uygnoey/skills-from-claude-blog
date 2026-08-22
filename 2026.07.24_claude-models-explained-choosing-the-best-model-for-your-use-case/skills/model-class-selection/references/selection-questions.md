# The four model-selection questions

When choosing a model class for a workload, ask these four questions. They are ordered so that the
first one that binds hard usually decides the class, and the rest refine it.

## 1. How hard is this task?

> If it typically takes a lot of time, involves multiple steps, or is previously unsolved then a
> more capable model class is appropriate.

Signals that push **up** a class:

- The task takes a long time even for a competent human.
- It is genuinely multi-step, with intermediate results feeding later steps.
- It is *previously unsolved* — no reliable existing tool or process handles it today.

Signals that a lower class may suffice: the task is narrow, precisely describable, and repeated
identically many times.

## 2. What are the latency needs?

> If the model is involved in high-frequency customer facing workloads, then Sonnet is often the
> best choice.

Ask whether a human is waiting on the response in real time, and whether the volume is high enough
that per-response latency compounds into a queue. Customer-facing, high-frequency work is the
canonical Sonnet shape.

## 3. What are the access constraints?

> Mythos is only available to organizations under Project Glasswing. Not all organizations make all
> model classes available to all roles.

Check before designing around a class:

- Is Mythos in scope at all (Project Glasswing enrollment)?
- Which classes has your organization enabled, and for which roles?
- Do the data-retention terms fit? Mythos and Fable both require limited data retention.

A model you cannot deploy is not a candidate, however well it scores.

## 4. What are the unit economics?

> Higher volumes of production may be more appropriate for lower classes of models, particularly if
> evaluations show those tasks are completed satisfactorily. Models are priced differently per token
> and will have different price-per-task costs based on their capabilities and effort level.

The key distinction is **price-per-token** vs. **price-per-task**. They can point in opposite
directions: a more capable model costs more per token but often takes fewer turns and less thinking
time, so cost-per-task can come out lower — especially at lower effort levels.

Compute cost-per-task on your own workload, at the effort level you would actually run, rather than
comparing headline token prices.

## After the four questions: the effort dial

Effort level shifts quality, speed, and cost independently of class. Search the grid of
(class × effort), not a single axis:

- Higher class + higher effort → best possible performance.
- Higher class + lower effort → sometimes more efficient than a smaller class.

## Source

["Claude models explained: choosing the best model for your use case"](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)
by Michael Segner — published July 24, 2026.
