# Agent deployment controls checklist

Workflow: ____________   Owner: ____________   Model(s): ____________   Date: ________

## Scoping questions
- [ ] What data can the agent access? (list approved sources)
- [ ] Which tools can it use?
- [ ] Which actions is it permitted to take?
- [ ] Which steps require human approval?
- [ ] How would we detect a problem?

## Controls around the model
- [ ] Approved data boundaries defined
- [ ] Least-privilege access for this user + task
- [ ] Tool-level permissions set
- [ ] Logging and traceability enabled
- [ ] Human review of material outputs before anyone relies on them (reviewer: ________)
- [ ] Escalation path for edge cases (contact: ________)
- [ ] Adversarial and failure scenarios tested before access is broadened

## Principles (confirm)
- [ ] Model upgrade does NOT change permissions (capability does not confer authority)
- [ ] Agent cannot grant itself additional access
- [ ] Decision responsibility stays with a named person
