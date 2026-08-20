---
name: ai-fluency-curriculum-design
description: Design AI training that increases learner agency and survives model releases. Use when writing internal AI enablement, an onboarding module, or a course and the draft keeps turning into a feature tour; when a program teaches tool operation but not which work should be delegated; when "safe use" has been reduced to prompt hygiene and omits task selection, skill preservation, and disclosure; or when you need an onboarding plus continuing-education structure rather than a one-time session.
---

# Designing AI-fluency training

Derived from Anthropic's account of how it approaches teaching and learning AI,
published alongside the launch of Claude Academy.

The organizing claim: **AI instruction should increase agency and empower
learners to expand their capabilities.** Everything below is a consequence of
taking that seriously instead of teaching the interface.

## Instructions

### 1. Start from the learner's problem, not the product surface

A feature tour answers "what can this do?" Agency-first material answers "what
were you trying to get done?"

- Open each unit with a real task the learner already owns. The AI capability
  is introduced as a way through that task, not as the subject.
- Make delegation an explicit decision the learner practices, not a default.
  Ask directly: which parts of this task should stay yours, and why?
- Judge a unit by whether the learner can now do something they could not do
  before — not by how many features were covered.

Anti-pattern: a module named after a product surface. If the title is a feature
name, the unit is probably a tour.

### 2. Teach mindsets that outlive the model

Feature-level instruction decays with every release. Framings do not.

Two carried by the source:

- **"Today's AI is the worst AI you'll ever use."** Treat a current limitation
  as a snapshot, and re-test assumptions rather than encoding them as rules.
- **"Verify in proportion to the stakes."** Not "always check everything" and
  not "trust it" — a calibration the learner performs per task.

When you catch yourself writing a numbered click-path, ask what judgment the
learner would need if the interface changed. Teach that instead. See
[examples/mindsets-vs-instructions.md](./examples/mindsets-vs-instructions.md)
for rewrites.

### 3. Cover safe use holistically

Safe use is not confined to the interaction itself. The curriculum has to reach
three areas that prompt-craft training normally skips:

- **Task selection** — deciding what is appropriate to hand over at all.
- **Skill preservation** — continuing to practice skills that matter to you, so
  they do not atrophy through delegation.
- **Disclosure** — explicitly stating how AI was used in producing a document,
  analysis, or piece of media *before* sharing it with others.

Details and how to teach each: [references/holistic-safe-use.md](./references/holistic-safe-use.md).

### 4. Make the learning active

Reading about AI use does not produce AI use. Every unit should carry:

- a **practice exercise** on the learner's own material, not a toy prompt;
- a **reflection prompt** that forces a judgment call rather than a recall;
- **room to experiment**, so the learner arrives at an approach fitted to their
  work instead of copying the instructor's.

Use [templates/course-outline.md](./templates/course-outline.md) as the
scaffold — it will not let you write a unit without all three.

### 5. Aim at fluency, then let it amplify

The final goal is not tool proficiency but the point at which the learner can
use AI to learn anything else. Once fluency is established, teach people to
treat AI as a learning partner in whatever domain they need next — that is
where the curriculum's leverage actually comes from.

### 6. Structure the program as onboarding plus continuing education

One-time training goes stale by definition. Anthropic's own shape:

- **Onboarding** — a fluency framework taught to every new employee (internally,
  the 4D AI Fluency Framework).
- **"Ever-boarding"** — ongoing programs that keep covering current
  capabilities, current limitations, and best practices for working with agents.

The continuing track is where model-specific content belongs, precisely because
it is the part you expect to rewrite.

The five design principles in full, each with what it rules in and out:
[references/design-principles.md](./references/design-principles.md).

## Examples

### Rewriting a stale module

A team has a module titled "Using the file-upload feature." Every screenshot is
one release out of date and the module is skipped in practice.

Rewritten under this skill: the unit becomes "Getting an answer out of a
document you did not write." It opens with a contract or report the learner
actually has to review. The upload step appears in one line. The substance is
the judgment: what parts of this review must you do yourself to be accountable
for the output, and how hard should you verify each claim given what it is
attached to? The exercise uses the learner's own document; the reflection prompt
asks them to name one thing they will keep doing manually and say why.

### A safe-use unit that is not about prompting

Instead of "how to write a good prompt," the unit asks the learner to take three
tasks from their week and sort them: delegate fully, delegate with review, keep.
They then justify one item in the "keep" column purely on skill-preservation
grounds — a skill they want to stay sharp at — and draft the one-line disclosure
they would attach to the delegated output before sending it on.

### Choosing where content lives

A new model ships with a longer context window. That fact goes in the
ever-boarding track, not in onboarding: onboarding teaches that context is
finite and that you decide what deserves to be in it, which stays true
regardless of the number.

## Source
[Anthropic's approach to teaching and learning AI](https://claude.com/blog/anthropics-approach-to-teaching-and-learning-ai) (published 2026-08-20). Claude Academy is at [academy.claude.com](https://academy.claude.com).
