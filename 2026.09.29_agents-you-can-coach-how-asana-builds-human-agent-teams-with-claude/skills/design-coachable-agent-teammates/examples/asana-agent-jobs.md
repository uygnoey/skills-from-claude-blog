# Three jobs Asana handed to agents

Summaries of the examples in the post. Claude powers agentic work at Asana that generates documents
or runs complex tasks.

## 1. Answering product questions from a Slack channel

**Before:** sellers and customer success staff asked about new features in a shared Slack channel;
the same questions repeated and subject-matter experts were @-mentioned each time. A static knowledge
base did not fit because answers are nuanced and change.

**Flow now:**
1. Questions still go to Slack (simplest place for the field).
2. An Asana app turns each question into a task; an agent picks it up.
3. Approved guidance exists → the agent replies with source links.
4. No approved answer and it points to a product gap → the agent creates a task in the product team's
   intake project and adds it to the backlog.
5. The same question keeps coming up → the agent creates a task for the enablement team to update
   training material and documentation.

**Effect:** enablement time goes to higher-priority work; clusters of questions on a topic signal
where extra training is needed.

## 2. Briefing executives on at-risk renewals

**Before:** the Chief Customer Officer produced a weekly briefing from CSM updates; across thousands of
customers this needed a dedicated synthesizer and was reactive.

**Flow now:** the At-Risk Renewal agent reads every at-risk renewal task (updates, status notes,
comments) and generates a structured daily digest — positive momentum, negative momentum, recommended
follow-ups — global first, then by region, pushed each morning to the CCO, CRO, and regional customer
success leaders. Leaders ask follow-ups in the shared space and coach the agent so the report improves
each run. See [../templates/at-risk-renewal-digest.md](../templates/at-risk-renewal-digest.md).

**Why shared rather than personal:** standardization of the report, a shared workspace, and a report
that keeps getting better with every run.

## 3. Planning engineering cycles with Command

**Problem:** automated coding loops (gather feedback → synthesize → coding agents open PRs) bloated
cycles and slipped releases. "Code generation is now no longer the bottleneck" — planning,
decision-making, and refinement are.

**Flow now:**
1. A team space holds 10–12 engineers on one product.
2. Agents populate the team's unplanned board with tickets from customer feedback and the team's
   Slack feedback channel.
3. People decide what moves into the cycle; Command predicts completion with optimistic, balanced, and
   conservative estimates.
4. A ticket is assigned to a person or a coding agent.
5. A manager can ask in chat why a release is off track and which tradeoffs would bring it back.
6. Data is exposed through Asana's MCP server, so leaders can ask Claude what's on track without
   opening Command.
