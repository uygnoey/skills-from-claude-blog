#!/usr/bin/env python3
"""Cache-control helper utilities for long-running tool-using agents.

Source: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
"""

from __future__ import annotations

from typing import Any, Dict, List


def set_trailing_cache_control(messages: List[Dict[str, Any]], max_breakpoints: int = 3) -> None:
    """Place up to `max_breakpoints` ephemeral cache_control markers on the most recent tool_result blocks.

    This function clears any existing cache_control markers first.
    """

    for msg in messages:
        for block in msg.get("content", []) or []:
            if isinstance(block, dict):
                block.pop("cache_control", None)

    placed = 0
    for msg in reversed(messages):
        for block in reversed(msg.get("content", []) or []):
            if placed >= max_breakpoints:
                return
            if isinstance(block, dict) and block.get("type") == "tool_result":
                block["cache_control"] = {"type": "ephemeral"}
                placed += 1
