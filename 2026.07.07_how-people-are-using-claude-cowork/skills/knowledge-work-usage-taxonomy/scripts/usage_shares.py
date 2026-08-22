#!/usr/bin/env python3
"""Turn labeled session counts into a share table.

Reads a JSON object of {"category": count} from a file argument or stdin and
prints a sorted share table, the top-two gap, and the combined top-two share.

Shares are shares *of the sample*, never volumes — the printed footer says so,
because the report that quotes this output has to say so too.

Usage:
    ./usage_shares.py counts.json
    echo '{"business process and operations": 334, "content creation": 164}' | ./usage_shares.py
"""
from __future__ import annotations

import json
import sys


def shares(counts: dict[str, float]) -> list[tuple[str, float, float]]:
    total = sum(counts.values())
    if total <= 0:
        raise SystemExit("error: counts must sum to a positive number")
    rows = [(name, n, 100.0 * n / total) for name, n in counts.items()]
    rows.sort(key=lambda r: r[2], reverse=True)
    return rows


def main() -> int:
    raw = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    try:
        counts = json.loads(raw)
    except json.JSONDecodeError as e:
        raise SystemExit(f"error: input is not valid JSON ({e})")
    if not isinstance(counts, dict) or not counts:
        raise SystemExit('error: expected a non-empty JSON object of {"category": count}')
    for name, n in counts.items():
        if not isinstance(n, (int, float)) or n < 0:
            raise SystemExit(f"error: count for {name!r} must be a non-negative number")

    rows = shares(counts)
    width = max(len(name) for name, _, _ in rows)
    total = sum(counts.values())

    print(f"{'Category'.ljust(width)}  {'Sessions':>10}  {'Share':>7}")
    print(f"{'-' * width}  {'-' * 10}  {'-' * 7}")
    for name, n, pct in rows:
        print(f"{name.ljust(width)}  {n:>10,.0f}  {pct:>6.1f}%")
    print(f"{'-' * width}  {'-' * 10}  {'-' * 7}")
    print(f"{'Total (sampled)'.ljust(width)}  {total:>10,.0f}  {100.0:>6.1f}%")

    if len(rows) >= 2:
        (n1, _, p1), (n2, _, p2) = rows[0], rows[1]
        ratio = p1 / p2 if p2 else float("inf")
        print()
        print(f"Top two combined: {p1 + p2:.1f}% ({n1} + {n2})")
        print(f"Top-to-next ratio: {ratio:.2f}x")

    print()
    print("Shares are shares of sampled sessions, not absolute volumes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
