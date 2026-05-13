#!/usr/bin/env python3
"""Helpers for pruning old screenshots from a chat history.

Source: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple


def prune_old_screenshots(
    messages: List[Dict[str, Any]],
    keep_n: int = 3,
    interval: int = 25,
) -> List[Dict[str, Any]]:
    """Replace older screenshots with text placeholders in batches.

    Only prunes when the total count exceeds keep_n + interval, so the message prefix stays
    byte-stable for `interval` turns between prunes.

    The function looks for blocks with {"type": "image"}.
    """

    image_positions: List[Tuple[int, int]] = [
        (msg_idx, block_idx)
        for msg_idx, msg in enumerate(messages)
        for block_idx, block in enumerate(msg.get("content", []) or [])
        if isinstance(block, dict) and block.get("type") == "image"
    ]

    if len(image_positions) <= keep_n + interval:
        return messages

    to_prune = image_positions[:-keep_n][-interval:]

    for msg_idx, block_idx in to_prune:
        messages[msg_idx]["content"][block_idx] = {
            "type": "text",
            "text": "[Image omitted]",
        }

    return messages
