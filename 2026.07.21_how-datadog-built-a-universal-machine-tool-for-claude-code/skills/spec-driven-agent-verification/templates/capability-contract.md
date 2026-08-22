# Capability contract template

Fill all three contracts. A capability with two of them is not ready for the
kernel. Field names come directly from the article's description of Temper's
contracts; the surrounding prose is scaffolding for the person or agent filling
it in.

---

## Capability: `<name>`

One sentence on what this capability governs. If you cannot say it in one
sentence, it is probably two capabilities.

---

### 1. Behavior contract

**States**

| State | Meaning | Initial? |
| --- | --- | --- |
| `<state>` | | yes / no |

**Transitions**

| From | Action | To | Precondition (guard) |
| --- | --- | --- | --- |
| `<state>` | `<action>` | `<state>` | `<condition that must hold>` |

Every transition needs a precondition. "Always" is a precondition, but write it
down — the symbolic layer proves each guard is *satisfiable*, and a guard nobody
wrote is a guard nobody checked.

**Safety properties (invariants)**

| Property | Statement | Must hold |
| --- | --- | --- |
| `<name>` | `<what is never true>` | in every reachable state |

State these as things that are never true, not as things that usually happen.
The symbolic layer proves each is inductive: true initially, and preserved by
every transition.

---

### 2. Data contract

Machine-parseable. Prose here defeats the purpose — an agent has to be able to
read this and propose a change without inferring intent.

**Entity types**

| Entity | Description |
| --- | --- |
| `<Entity>` | |

**Properties**

| Entity | Property | Type | Required |
| --- | --- | --- | --- |
| `<Entity>` | `<property>` | `<type>` | yes / no |

**Actions**

| Action | Input | Effect |
| --- | --- | --- |
| `<action>` | `<entity/properties>` | `<which transition it drives>` |

Each action here should correspond to an action in the behavior contract's
transition table. Actions with no transition are dead; transitions with no action
cannot be invoked.

---

### 3. Authorization contract

**Posture:** default-deny. Anything not listed below is denied.

**Scopes**

| Scope | Grants | Granted to |
| --- | --- | --- |
| `<scope>` | `<which actions>` | `<role / agent / session>` |

**Pending decisions**

| Requested scope | Requested by | Rationale | Status |
| --- | --- | --- | --- |
| `<scope>` | | | pending / approved / denied |

A requested-but-ungranted scope is a normal state, not an error. Record it here
rather than letting it fail silently at call time.

**Hot-loading:** state whether an approval here takes effect without a redeploy,
and what the propagation boundary is.

---

### Pre-kernel checklist

- [ ] Every transition has a precondition
- [ ] Every safety property is stated as an invariant, not a scenario
- [ ] Every data-contract action maps to a transition
- [ ] Every scope names the actions it grants
- [ ] A person can hold this whole capability in their head — if not, split it

## Source

[How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code) — Michael Segner, July 21, 2026
