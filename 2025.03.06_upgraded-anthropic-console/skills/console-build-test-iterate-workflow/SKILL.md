---
name: console-build-test-iterate-workflow
description: Use the upgraded Anthropic Console as a single workspace to build, evaluate, and iterate Claude prompts before shipping. Walks through Workbench authoring, the prompt generator, side-by-side evaluation, prompt improvement, "Get Code" export, shareable prompts for team collaboration, and the extended thinking budget for Claude 3.7 Sonnet — based strictly on the March 6, 2025 launch post.
---

# Console build / test / iterate workflow

Anthropic's March 6, 2025 launch describes a redesigned Console designed to streamline the loop from a rough idea to a production-ready API call. This skill turns the post's product description into a repeatable workflow.

## Instructions

### 1. Decide whether to start from a blank slate or from an existing prompt

The post describes two entry points:

- **Blank slate** — open the Workbench and structure your prompt manually, adding examples and tool integrations as the post recommends.
- **Generated draft** — describe what you want to achieve and let the prompt generator produce a draft that already uses techniques like chain-of-thought.

If you have an existing prompt (including one written for another AI model), the post recommends a third path: feed it to the prompt improvement tool, which refines it using Anthropic's prompt-engineering techniques.

The full list of tools the post calls out is in [references/console-tools-from-post.md](./references/console-tools-from-post.md).

### 2. Build prompts in the Workbench

Per the post, the Workbench is where you:

- Structure prompts effectively.
- Incorporate examples.
- Integrate external tools.
- Test API calls in an interactive environment.

Treat the Workbench as the surface where the prompt actually lives — not a notepad. The "Get Code" button at the end exports a production-ready API call from this same surface.

### 3. Evaluate before shipping

The post describes the evaluation tooling in three steps:

1. Generate test cases automatically.
2. Run the test suite against your prompt.
3. Compare outputs side by side and grade response quality.

Use this as the gate between "draft I like" and "prompt I am willing to deploy." Side-by-side comparison is the post's recommended way to make data-driven decisions about which prompt to deploy.

### 4. Improve, do not rewrite

When evaluation shows weaknesses, prefer the prompt improvement tool over rewriting from scratch. The post explicitly positions this tool as ideal for:

- Adapting prompts originally written for other AI models.
- Optimizing hand-written prompts.

This keeps you inside the same Console workflow rather than fragmenting iteration across editors.

### 5. Use shareable prompts to break out of doc copy-paste

Before this redesign, the post says teams "resorted to copying and pasting prompts between documents or chat applications, leading to version control issues and knowledge silos." Shareable prompts replace that with a centralized library inside Console.

Use shareable prompts when:

- Developers, domain experts, product managers, and QA need the same prompt under review.
- You want best practices and standards to propagate across the org.
- You need consistent prompt quality across multiple Claude-powered applications.

Concrete role-specific scenarios are in [examples/team-collaboration-scenarios.md](./examples/team-collaboration-scenarios.md).

### 6. Optimize for extended thinking on Claude 3.7 Sonnet

The post describes Claude 3.7 Sonnet as Anthropic's "latest and most intelligent model" capable of producing near-instant responses or extended, step-by-step thinking visible to the user.

Workflow guidance from the post:

- When you know the prompt will be used with extended thinking on, signal that in Console so it generates the best response possible.
- Set a max number of thinking tokens to control the thinking budget — do not leave it implicit if cost or latency matters.

### 7. Ship via "Get Code"

After evaluation passes, click "Get Code" to export the production-ready API call directly. Treat this as the natural endpoint of the loop — do not hand-translate the prompt back into your codebase, since that risks reintroducing the version-control issues the post calls out.

## Examples

### Example A: Drafting a new prompt for a customer-support classifier

1. In Console, open the prompt generator and describe: "Classify support tickets into billing, bug, feature_request, account, other."
2. Move the generated draft into the Workbench. Add a few labeled example tickets the way the Workbench supports.
3. Open the evaluation tool. Auto-generate test cases. Run side-by-side and grade results.
4. If quality is uneven, run the prompt improvement tool on the prompt and re-evaluate.
5. Share the prompt with QA and the support PM via shareable prompts before clicking "Get Code".

### Example B: Migrating a prompt written for another model

1. Paste the existing prompt into the Workbench.
2. Run the prompt improvement tool to rewrite it using Anthropic's prompt-engineering techniques.
3. Generate test cases and run side-by-side against the improved version.
4. Iterate inside Console rather than swapping back to a doc.
5. Export with "Get Code" once evaluation passes.

### Example C: Adopting Claude 3.7 Sonnet's extended thinking

1. In Console, signal that this prompt will be used with extended thinking on.
2. Let Console regenerate or improve the prompt for that mode.
3. Set a max thinking-token budget so latency and cost stay predictable.
4. Evaluate with side-by-side comparison against the non-extended-thinking version to confirm the budget is justified for your task.

## Source

Get to production faster with the upgraded Anthropic Console — Anthropic, March 6, 2025: <https://claude.com/blog/upgraded-anthropic-console>
