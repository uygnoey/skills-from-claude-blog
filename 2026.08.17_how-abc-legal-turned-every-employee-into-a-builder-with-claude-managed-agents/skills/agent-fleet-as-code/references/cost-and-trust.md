# Cost, trust, and deciding what deserves an agent

Two disciplines keep a fleet defensible: a measured cost model, and a trust ladder every agent has to climb.

## The efficiency ratio

**The metric is an efficiency ratio: the value an agent delivers, measured against what it costs to run.**

Every agent reports its own value back to a data warehouse on each run, in **hours and dollars**. That is the design decision that makes the metric real — value reporting is part of the agent's job, not a quarterly exercise someone does in a spreadsheet.

Track spend broken out by **vendor, tool, team, and use case**.

## The J-curve

Agents follow a J-curve:

1. **Underwater** while they are new and running larger models.
2. **Flipping positive** as the team writes evals, moves to cheaper and faster models, and trims tokens.

Two mistakes follow from not knowing this. Killing an agent at the bottom of its curve throws away the work. Assuming every agent climbs out on its own means nobody does the optimization that makes it climb.

In the source story, spend climbed as the fleet went live through the spring, then started **falling in July while usage kept growing** — the result of exactly that optimization work, alongside a ~50% reduction in the cost of the tasks many agents cover and ~310 employees across every department using Claude.

## The spending posture

Deliberate, and worth copying:

- **Push spend toward vertical, operational tools and agents** where return is measurable.
- **Keep horizontal chat and ideation usage broad**, and its costs in check.

The two halves are different products with different economics. Managing them as one budget hides both.

## Model policy

Swapping models should be a one-line change in config. Given that:

- a **mid-tier model** as the default for most agents,
- a **small, fast model** for high-volume, fast tasks,
- a **large model** only where deeper reasoning justifies the cost.

## The trust ladder

Most agents start with a human in the loop: the agent looks at the job or ticket and makes a recommendation for a person to review before anything is acted on.

**Two placements for the recommendation:**

1. **In the flow of work** — stored on the job and surfaced in a banner, so the person accepts or rejects it where they already are.
2. **In a channel** — posted to a chat channel where people reply in the thread.

**What that buys you:** those responses build a labeled dataset of good and bad calls. The dataset feeds the harvester-and-tuner loop, and it lets the team write evals and benchmark agents across frontier models.

**The promotion criterion:** once an agent proves it is **as good as or better than the humans on that specific task**, it shifts into automation mode and acts on its own.

**What does not change on promotion:** it stays inside the same measurement framework afterward, to watch for any changes in performance.

*"Every agent earns trust before it acts alone. It doesn't start there."*

## Not every task deserves an agent

The cost is real, so every team has to think in terms of value over cost. The work is picking tractable problems that genuinely save time or create automation — **and being willing to say a given task is not worth an agent.**

A workable screen before building:

| Question | Why it matters |
|---|---|
| How much human time does this consume, per month? | The numerator of the ratio. |
| Is the task repetitive and well-bounded? | Judgment nobody has written down is not yet automatable. |
| Who owns the agent after it ships? | An agent without a named owner is one nobody maintains. |
| Is there a grading signal? | Without one, there is no harvester loop and no eval. |
| What does a wrong answer cost? | Sets how long it stays in recommend mode. |

## Source

- https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
