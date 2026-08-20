# The five lessons, and what each implies for a plan

monday closes its account with five lessons from the transformation. Each is
restated below with the planning consequence it carries — the thing you would do
differently if you believed it before starting rather than after.

---

## 1. Mental models are harder to move than the technology

**The lesson.** Shifting teams from "improve the existing product" to
"responsibly rebuild for a different future" took longer than the technical
work.

**Planning consequence.** Budget the reframing explicitly, and do it before the
build rather than alongside it. A schedule that allocates time to engineering
and none to changing what the team thinks it is building will slip on the part
it did not schedule. Expect the strongest resistance from the people who are
best at the current product, because their expertise is what the reframe is
asking them to set aside.

---

## 2. Small teams with clear ownership accelerate change

**The lesson.** When direction, UX, technology, pricing, trust models, and
quality definitions all moved at once, small teams with clear ownership and fast
decision rights stayed aligned better than hierarchical structures.

**Planning consequence.** Notice the precondition: *six things moving
simultaneously*. Hierarchy is not the problem in general — it is the problem
when every dependency is in motion, because each decision has to travel up and
back down while its inputs are still changing. Structure for the number of
simultaneously unstable variables, not for the size of the project.

---

## 3. Adoption requires trust infrastructure

**The lesson.** Governance, permissions, transparency, and reliability
determined whether agents moved beyond pilots into production.

**Planning consequence.** These are launch requirements, not hardening work.
A pilot that skips them will demo well and then fail to convert, and the failure
will be misread as a capability problem. Write the four as acceptance criteria
for the first release:

- Who authorizes an agent to act on which objects.
- Whether the agent's access is bounded by the assigning human's.
- Whether what the agent did is visible on the object afterwards.
- Whether behavior is predictable enough to build a process on.

---

## 4. Capability needs backend infrastructure

**The lesson.** Agents performed significantly better when grounded in live
project data, team history, and structured workflows. monday invested in
monday DB to support agent volume and complexity at enterprise scale.

**Planning consequence.** Agent quality is bounded by what the data layer can
serve — how fresh, how structured, at what latency and concurrency. A roadmap
with agent capabilities and no infrastructure line item is a plan to plateau at
whatever your current query patterns support. Model the load: agents read far
more, far more often, than human users do.

---

## 5. Build on existing strengths

**The lesson.** monday extended its identity as the place where people team up
to include agents as team members, rather than introducing an entirely new
paradigm.

**Planning consequence.** Write the one sentence your product already means to
its users, then check that the agent story is a continuation of that sentence
rather than a competing one. If your agents require users to learn a new mental
model *and* trust a new class of actor at the same time, you have doubled the
adoption cost for no gain. This is also the cheapest of the five to get right,
and the easiest to get wrong by accident — a separate chat surface with its own
concepts is the usual way it happens.

---

## Reading them together

Lessons 1 and 5 are about meaning; 2 is about structure; 3 and 4 are about
foundations. The sequence they suggest for a plan is: settle what the product
means with agents in it (5), reframe the team around building that (1),
restructure ownership for a period when everything moves at once (2), then make
trust and data layer work first-class deliverables rather than follow-ups
(3, 4).

## Source
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) (published 2026-08-20). The lessons are from the post; the planning consequences are drawn out from them.
