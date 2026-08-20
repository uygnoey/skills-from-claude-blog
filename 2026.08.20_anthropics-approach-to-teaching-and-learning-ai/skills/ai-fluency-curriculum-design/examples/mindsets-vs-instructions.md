# Mindsets vs. instructions: worked rewrites

The source's second design principle is that durable mindsets beat
feature-specific instructions, because capabilities move faster than course
material. Below are training lines rewritten from the instruction form into the
mindset form, with a note on why the original had a short shelf life.

The two mindsets named in the source are used as anchors:

- **"Today's AI is the worst AI you'll ever use."**
- **"Verify in proportion to the stakes."**

---

## 1. Model choice

**Instruction form**
> For long documents, switch to the model with the larger context window.

**Why it decays**
Context sizes change with every release; the sentence is either obsolete or
misleading within months, and it teaches nothing transferable.

**Mindset form**
> Context is finite and everything you put in it competes for attention. Decide
> what actually needs to be in front of the model, and re-check that judgment as
> capabilities change — today's limits are the tightest you will ever work with.

---

## 2. Checking output

**Instruction form**
> Always verify every fact in AI-generated output before using it.

**Why it decays**
It is unworkable, so learners abandon it, and abandoning a rule wholesale is
worse than never having had one. It also gives no way to reason about a new
situation.

**Mindset form**
> Verify in proportion to the stakes. Ask what happens if this specific claim is
> wrong, who is downstream of it, and whether the error would be visible. A
> throwaway internal summary and a customer-facing number do not deserve the
> same scrutiny.

---

## 3. Task fit

**Instruction form**
> AI is not good at math, so do calculations yourself.

**Why it decays**
It encodes a snapshot of capability as a permanent property, and learners will
keep believing it long after it stops being true.

**Mindset form**
> Where the model is weak today is a moving target. Test it on your own class of
> problem, keep the result as a current observation rather than a rule, and
> re-test when a new model ships.

---

## 4. Prompting

**Instruction form**
> Structure every prompt with role, context, task, and format, in that order.

**Why it decays**
A formula substitutes for the judgment it was meant to encode, and stops being
necessary as models improve at inferring intent.

**Mindset form**
> The model can only work from what it can see. Before adding technique, ask
> what a competent colleague would need to know to do this task, and supply
> that. Then experiment — the shape that works for your work is not necessarily
> the shape in the training deck.

---

## 5. Delegation

**Instruction form**
> Use AI to save time on routine work.

**Why it decays**
Not wrong, but it is agency-free: it never asks whether the delegation is a good
idea, and it invites atrophy of skills the learner cares about.

**Mindset form**
> Decide what to hand over before deciding how. Some work you keep because you
> are accountable for it; some you keep because you want to stay good at it.
> Name which reason applies before you delegate — and say how AI was used when
> you share the result.

---

## How to spot an instruction that should be a mindset

Ask two questions about any line in the material:

1. **Would this still be true after the next model release?** If not, it belongs
   in the continuing ("ever-boarding") track, not in foundational material.
2. **Does it replace a judgment with a rule?** If a learner following it never
   has to decide anything, they will not be able to handle the case you did not
   anticipate.

## Source
[Anthropic's approach to teaching and learning AI](https://claude.com/blog/anthropics-approach-to-teaching-and-learning-ai) (published 2026-08-20). The two anchor mindsets are quoted from that post; the rewrites are worked examples.
