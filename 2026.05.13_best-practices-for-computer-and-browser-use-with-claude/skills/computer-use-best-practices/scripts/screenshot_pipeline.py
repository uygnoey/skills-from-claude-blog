#!/usr/bin/env python3
"""Screenshot downscaling and coordinate-scaling helpers.

Source: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
"""

from __future__ import annotations

import base64
import io
import math
from dataclasses import dataclass
from typing import Tuple

try:
    from PIL import Image
except ImportError as e:  # pragma: no cover
    raise SystemExit(
        "Pillow is required for this helper (pip install pillow)."
    ) from e


@dataclass(frozen=True)
class ApiImageLimits:
    """Image size limits used by the Claude API (varies by model family)."""

    max_long_edge_px: int
    max_total_pixels: int


LIMITS_CLAUDE_46 = ApiImageLimits(max_long_edge_px=1568, max_total_pixels=1_150_000)
LIMITS_OPUS_47 = ApiImageLimits(max_long_edge_px=2576, max_total_pixels=3_750_000)


def compute_max_api_fit(native_w: int, native_h: int, limits: ApiImageLimits) -> Tuple[int, int]:
    """Compute the largest resolution that fits API limits while preserving aspect ratio.

    Never upscales beyond the native resolution.
    """

    aspect = native_w / native_h

    # Compute max dimensions from pixel budget
    h_from_pixels = math.sqrt(limits.max_total_pixels / aspect)
    w_from_pixels = h_from_pixels * aspect

    # Apply long-edge constraint
    if native_w >= native_h:
        w = min(w_from_pixels, limits.max_long_edge_px)
        h = w / aspect
    else:
        h = min(h_from_pixels, limits.max_long_edge_px)
        w = h * aspect

    # Never upscale beyond native
    w = min(w, native_w)
    h = min(h, native_h)

    return int(w), int(h)


def prepare_screenshot(
    screenshot: "Image.Image",
    native_w: int,
    native_h: int,
    *,
    mode: str = "fixed_720p",
    limits: ApiImageLimits = LIMITS_CLAUDE_46,
    fixed_size: Tuple[int, int] = (1280, 720),
) -> Tuple[str, int, int]:
    """Resize screenshot to fit typical API budgets and return (base64_png, display_w, display_h)."""

    if mode == "fixed_720p":
        display_w, display_h = fixed_size
    elif mode == "max_api_fit":
        display_w, display_h = compute_max_api_fit(native_w, native_h, limits)
    else:
        raise ValueError("mode must be one of: fixed_720p, max_api_fit")

    resized = screenshot.resize((display_w, display_h), Image.LANCZOS)

    buffer = io.BytesIO()
    resized.save(buffer, format="PNG")
    b64 = base64.standard_b64encode(buffer.getvalue()).decode("utf-8")

    return b64, display_w, display_h


def scale_coordinates(
    api_x: int,
    api_y: int,
    display_w: int,
    display_h: int,
    screen_w: int,
    screen_h: int,
) -> Tuple[int, int]:
    """Scale API-returned coordinates back to native screen space."""

    screen_x = int(api_x * (screen_w / display_w))
    screen_y = int(api_y * (screen_h / display_h))
    return screen_x, screen_y
