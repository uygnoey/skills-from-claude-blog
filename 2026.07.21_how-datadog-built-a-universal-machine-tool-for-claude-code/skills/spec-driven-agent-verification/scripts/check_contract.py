#!/usr/bin/env python3
"""Check that a capability spec carries all three contracts, before the kernel sees it.

Datadog's Temper requires three contracts per capability: behavior (states,
transitions, preconditions, safety properties), a machine-parseable data contract
(entity types, properties, actions), and authorization (default-deny, scope-based
approval, pending decisions).

This checks shape and internal consistency only. It proves nothing -- proving is
the deterministic kernel's job. Treat it as the gate that stops obviously
incomplete specs from consuming kernel time.

Usage:
    ./check_contract.py path/to/transition-table.json [more.json ...]

Exit status: 0 if every file passes, 1 otherwise.
"""

import json
import sys

REQUIRED_TOP = ("behavior", "data_contract", "authorization")


def check(spec):
    """Return a list of problem strings for one parsed spec."""
    problems = []

    for key in REQUIRED_TOP:
        if key not in spec:
            problems.append(f"missing top-level contract: {key!r}")
    if problems:
        return problems

    behavior = spec["behavior"]
    data = spec["data_contract"]
    authz = spec["authorization"]

    # --- behavior -----------------------------------------------------------
    states = set(behavior.get("states") or [])
    if not states:
        problems.append("behavior.states is empty")

    initial = behavior.get("initial_state")
    if initial is None:
        problems.append("behavior.initial_state is missing")
    elif initial not in states:
        problems.append(f"behavior.initial_state {initial!r} is not in behavior.states")

    transitions = behavior.get("transitions") or []
    if not transitions:
        problems.append("behavior.transitions is empty")

    transition_names = set()
    for i, t in enumerate(transitions):
        where = t.get("name") or f"transitions[{i}]"
        transition_names.add(t.get("name"))
        for field in ("name", "from", "to", "precondition"):
            if not t.get(field):
                problems.append(f"transition {where}: missing {field!r}")
        for field in ("from", "to"):
            value = t.get(field)
            if value and value not in states:
                problems.append(
                    f"transition {where}: {field} {value!r} is not a declared state"
                )

    properties = behavior.get("safety_properties") or []
    if not properties:
        problems.append(
            "behavior.safety_properties is empty -- with no invariants there is "
            "nothing for the symbolic layer to prove inductive"
        )
    for i, p in enumerate(properties):
        where = p.get("name") or f"safety_properties[{i}]"
        if not p.get("statement"):
            problems.append(f"safety property {where}: missing 'statement'")

    # unreachable states (excluding the initial one)
    reachable = {initial} if initial in states else set()
    changed = True
    while changed:
        changed = False
        for t in transitions:
            if t.get("from") in reachable and t.get("to") not in reachable:
                if t.get("to") in states:
                    reachable.add(t["to"])
                    changed = True
    for orphan in sorted(states - reachable):
        problems.append(f"state {orphan!r} is not reachable from the initial state")

    # --- data contract ------------------------------------------------------
    entities = data.get("entity_types") or []
    if not entities:
        problems.append("data_contract.entity_types is empty")
    for i, e in enumerate(entities):
        where = e.get("name") or f"entity_types[{i}]"
        if not e.get("name"):
            problems.append(f"entity {where}: missing 'name'")
        if not (e.get("properties") or []):
            problems.append(f"entity {where}: has no properties")
        for j, prop in enumerate(e.get("properties") or []):
            for field in ("name", "type"):
                if not prop.get(field):
                    problems.append(
                        f"entity {where}, property[{j}]: missing {field!r}"
                    )

    actions = data.get("actions") or []
    if not actions:
        problems.append("data_contract.actions is empty")
    action_names = set()
    for i, a in enumerate(actions):
        where = a.get("name") or f"actions[{i}]"
        action_names.add(a.get("name"))
        driven = a.get("drives")
        if not driven:
            problems.append(f"action {where}: missing 'drives' (no transition to invoke)")
        elif driven not in transition_names:
            problems.append(
                f"action {where}: drives {driven!r}, which is not a declared transition"
            )

    for name in sorted(n for n in transition_names if n and n not in {
        a.get("drives") for a in actions
    }):
        problems.append(
            f"transition {name!r} is driven by no action -- it can never be invoked"
        )

    # --- authorization ------------------------------------------------------
    if authz.get("posture") != "default-deny":
        problems.append(
            f"authorization.posture is {authz.get('posture')!r}; Temper's contract is 'default-deny'"
        )
    if "pending_decisions" not in authz:
        problems.append(
            "authorization.pending_decisions is missing -- an ungranted request is a "
            "first-class state, not a silent failure"
        )
    scopes = authz.get("scopes") or []
    if not scopes:
        problems.append("authorization.scopes is empty; under default-deny nothing can run")
    granted = set()
    for i, s in enumerate(scopes):
        where = s.get("name") or f"scopes[{i}]"
        if not s.get("name"):
            problems.append(f"scope {where}: missing 'name'")
        if not (s.get("granted_to") or []):
            problems.append(f"scope {where}: missing 'granted_to'")
        for action in s.get("grants") or []:
            granted.add(action)
            if action not in action_names:
                problems.append(
                    f"scope {where}: grants {action!r}, which is not a declared action"
                )
    for orphan in sorted(n for n in action_names if n and n not in granted):
        problems.append(
            f"action {orphan!r} is granted by no scope -- under default-deny it is unreachable"
        )

    return problems


def main(argv):
    paths = argv[1:]
    if not paths:
        print(__doc__.strip(), file=sys.stderr)
        return 1

    failed = False
    for path in paths:
        try:
            with open(path, encoding="utf-8") as fh:
                spec = json.load(fh)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"{path}: cannot read as JSON: {exc}")
            failed = True
            continue

        problems = check(spec)
        if problems:
            failed = True
            print(f"{path}: {len(problems)} problem(s)")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"{path}: three contracts present and internally consistent")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
