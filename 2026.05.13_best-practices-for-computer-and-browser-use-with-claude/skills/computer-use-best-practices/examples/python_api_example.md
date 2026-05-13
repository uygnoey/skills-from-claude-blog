# Python API example (computer use)

Source: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude

This example shows (1) preparing a screenshot for the API, (2) sending text before image,
(3) configuring the `computer_20251124` tool with matching display dimensions, and (4) scaling
the returned coordinates back to native screen coordinates.

```python
import anthropic
from PIL import Image

from scripts.screenshot_pipeline import prepare_screenshot, scale_coordinates

client = anthropic.Anthropic()

# Capture screenshot (your method here)
screenshot = Image.open("screenshot.png")
native_w, native_h = screenshot.size

# Prepare for API
b64, display_w, display_h = prepare_screenshot(
    screenshot,
    native_w,
    native_h,
    mode="fixed_720p",
)

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["computer-use-2025-11-24"],
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Click the Submit button"},
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": b64,
                    },
                },
            ],
        }
    ],
    tools=[
        {
            "type": "computer_20251124",
            "name": "computer",
            "display_width_px": display_w,
            "display_height_px": display_h,
        }
    ],
)

api_x, api_y = extract_click_coords(response)  # your parsing logic
screen_x, screen_y = scale_coordinates(
    api_x,
    api_y,
    display_w,
    display_h,
    native_w,
    native_h,
)
```
