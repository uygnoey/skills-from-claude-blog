# What the effort level actually changes

Effort level controls **how much work Claude does on your request overall**. It does include how
long the model thinks, but also:

- how many files it reads;
- how much it verifies; and
- how far it pushes through a multi-step task before checking in with you.

At a higher effort, Claude will take more of those actions — read files, run tests, double-check —
before it comes back to you. At lower effort, it would rather ask you for more context than spend
tokens figuring something out on its own.

## Every kind of output is the same kind of token

When Claude Code is working on a task, the tokens it generates fall into a few categories:

- **Thinking** — the reasoning you see streaming before and between actions.
- **Tool calls** — structured blocks naming a tool like `Read` or `Edit` and its arguments, which
  Claude Code then parses and executes.
- **Text to you** — the plan, progress updates, the summary at the end.

These are all ordinary output tokens from the same loop, **billed at the same rate**. Thinking
tokens are generated exactly like the other output tokens and stay in context for the rest of that
turn: when Claude moves on to writing code, its earlier reasoning is part of the input, just like
a file it has read.

## How the setting reaches the model

The effort level is **sent to the model as part of the request**, right alongside your prompt. The
model was trained to understand how to behave at each effort level, and that learned behavior is
baked into the frozen weights.

So when your request arrives, effort level is one more input the model responds to, the same way
it responds to your prompt text. It sets Claude's behavior for **how thorough and certain it needs
to be before it considers the task done** — considered on every turn, resulting in more tokens
spent to produce higher-confidence answers.

For the same prompt, a high-effort path can generate roughly **7×** more tokens than a low-effort
path to reach a higher-confidence answer.

## Plans are revised, not executed blindly

At higher effort levels Claude often starts by creating a plan, and the level of effort influences
the depth and breadth of that plan. But **the plan is not frozen in place**. As Claude receives
results from its actions, it updates what progress has been made and how certain it is of the
accumulated result.

So when step 1 of a three-hypothesis debugging plan finds the bug, "investigate hypotheses 2 and
3" may no longer be necessary. Claude will typically say this explicitly — *the first check found
it, so the remaining checks aren't needed* — and skip ahead. You see this in Claude Code when task
lists get revised mid-run.

## Higher effort is not padding

Claude is more predisposed to double-checking additional hypotheses or verifying correctness at
higher effort levels, but it generally **won't artificially inflate usage for simple tasks**.
Anthropic's team pays close attention to "overthinking" during model training, because it degrades
effectiveness.

## Source

["Choosing a Claude model and effort level in Claude Code"](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)
