**English** · [한국어](./ai-education-program.ko.md) · [Español](./ai-education-program.es.md) · [日本語](./ai-education-program.ja.md)

# Running an AI education program: onboarding plus ever-boarding

Derived from Anthropic's August 20, 2026 post on its approach to teaching and
learning AI, published alongside the launch of Claude Academy.

## The premise

The post states a belief that shapes everything else in it: AI instruction
should increase agency and empower learners to expand their capabilities. That
is a claim about what education is *for*, and it rules out the most common
default — a tour of what the product can do.

It also implies a timing problem. Capabilities move faster than course material.
A program built as a single training event is stale on delivery. So the shape
Anthropic describes internally is two tracks, not one.

## Two tracks

### Onboarding: the durable layer

Every new employee is taught a fluency framework — internally, the 4D AI Fluency
Framework. This is the layer that has to stay true across model releases, so it
carries framings rather than procedures:

- Today's AI is the worst AI you'll ever use.
- Verify in proportion to the stakes.

Neither sentence depends on a version number. Both give a learner something to
do in a situation the course never anticipated.

### Ever-boarding: the perishable layer

After onboarding, continuing programs cover current AI capabilities, current
limitations, and best practices for working with agents. This is deliberately
the part you expect to rewrite. Anything version-specific belongs here — not
because it is unimportant, but because putting it in the foundational layer is
what makes foundations go stale.

**The allocation rule:** if a statement will be wrong after the next model
release, it goes in ever-boarding. If it would still be worth saying in two
years, it goes in onboarding.

## What the content has to cover

The post gives five design principles. Three shape the substance:

**Agency first.** Organize material around real problems learners have, and make
them reflect on which tasks should remain human-owned versus delegated. The
delegation decision is the lesson; the mechanics are a footnote.

**Mindsets over behaviors.** Prefer framings that survive change. When you catch
yourself writing a numbered click-path, ask what judgment the learner would need
if the interface were different, and teach that instead.

**Safe use, holistically.** Beyond the interaction itself, three areas:

- *Task selection* — what is appropriate to hand over at all.
- *Skill preservation* — continuing to practice skills that matter to you, so
  delegation does not quietly hollow them out.
- *Disclosure* — explicitly stating how AI was used in producing a document,
  analysis, or piece of media before sharing it with others.

Most enablement programs cover none of the three. They are the difference
between teaching operation and teaching use.

## How the content is delivered

**Active learning.** Courses carry practice exercises, reflection prompts, and
room to experiment. The stated goal of experimentation is that learners discover
approaches personalized to their own work — which means the program must not
present a single correct workflow. If everyone finishes with the same process,
the experimentation was decorative.

**AI as the amplifier.** The end state is not tool proficiency. Once someone has
fluency, they can use AI as a learning partner in any domain. A program that
stops at proficiency has stopped one step before the payoff.

## The platform

Claude Academy, at [academy.claude.com](https://academy.claude.com), is the
public form of this: courses recommended by interest, completion tracking and
badges, and a Claude Academy Skill that recommends courses or learning paths
based on how you work.

For an internal program, the equivalent question is whether your enablement can
meet a person where their work already is, rather than requiring them to go
looking for the relevant module.

## Building your own

1. **Split the curriculum in two** by the allocation rule above. Most existing
   material will land in ever-boarding, and that is the diagnosis, not a
   failure.
2. **Retitle every onboarding unit** after a problem rather than a feature. Any
   unit whose title survives this step unchanged was already about the work.
3. **Add the three safe-use areas** as first-class units, sequenced with task
   selection *before* interaction technique — teaching prompting first implies
   the delegation decision is already made.
4. **Require the three active-learning elements** in every unit, on the
   learner's own material.
5. **Set a rewrite cadence for the perishable track only.** The durable track
   should not need one; if it does, it has version-specific content in it.
6. **End by pointing outward** — the last unit should hand the learner a way to
   use their new fluency to learn something unrelated.

## Source
[Anthropic's approach to teaching and learning AI](https://claude.com/blog/anthropics-approach-to-teaching-and-learning-ai) (published 2026-08-20). The post links to Claude Academy for the 4D AI Fluency Framework itself rather than defining the four D's inline.
