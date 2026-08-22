# The Claude model family

The Claude model family is Anthropic's lineup of AI models — Fable, Opus, Sonnet, and Haiku — each
balancing intelligence, speed, and cost differently. Choosing well means matching the model to the
job.

Model classes do **not** specialize in one type of work. There is no recommendation of one class for
finance and another for science. Every Claude model is trained to excel in areas like coding,
agentic tasks, and knowledge work. The main difference across classes is **how hard a problem they
can reliably carry, and what that capability costs in price and speed**.

## Mythos / Fable

Mythos is Anthropic's most capable model class, with frontier capabilities across domains. This
class is especially capable at:

- coding
- long-running agent tasks
- solving problems AI has not reliably handled before

**Two packages of the same underlying model:**

| Package | Who it is for |
|---|---|
| **Claude Mythos** | Trusted organizations handling dual-use cybersecurity and biology work. |
| **Claude Fable** | Packaged with additional safeguards that make the model safe for use by the general public. |

Both require limited data retention so they can be used safely.

## Opus

Opus is the powerful model class for **reasoning-intensive enterprise tasks**. Opus models
consistently rank among leading models on key industry benchmarks such as:

- **GDPval-AA** — knowledge work
- **Terminal-Bench 2.1** — agentic coding

### Opus vs. Fable

The choice may not seem clear on the surface: both excel at coding, long-running agents, and
knowledge work. In real-world situations, larger models such as Fable tend to have more **wisdom,
creativity, and writing skills** despite having similar benchmark scores to models such as Opus.

**Rule of thumb:**

- If your evals or internal testing show **Opus struggling** on some tasks → **Fable** is the answer.
- If **Opus already clears the quality bar** → its speed and price profile may make it the better
  choice.

## Sonnet

Sonnet is the versatile model class for everyday tasks. It provides a balance of performance, cost,
and speed for the widest set of general-purpose use cases, **including high-volume sub-agents in
multi-agent orchestration setups**.

## Haiku

Haiku is the lowest cost and fastest model class. Haiku models are designed for **high-frequency
workloads where latency and cost matter**.

## Effort level cuts across all of them

Effort level also impacts the balance of quality, speed, and cost:

- Higher-class models at **higher** efforts offer the best possible performance.
- Higher-class models at **lower** efforts can sometimes be **more efficient than smaller models**.

This is the reason the default advice is to start on the most intelligent generally available model
and dial effort down, rather than starting on a smaller class.

## Source

["Claude models explained: choosing the best model for your use case"](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)
by Michael Segner — published July 24, 2026.
