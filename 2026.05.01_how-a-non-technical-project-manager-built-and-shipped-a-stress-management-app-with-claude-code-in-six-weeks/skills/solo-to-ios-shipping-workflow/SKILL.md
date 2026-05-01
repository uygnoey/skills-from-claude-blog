---
name: solo-to-ios-shipping-workflow
description: Build and ship a real app with Claude Code by iterating from a fast prototype to a production-ready iOS release, coordinating specialist subagents and using Claude for engineering + launch tasks.
---

# Solo to iOS shipping workflow (case-study)

This skill adapts a Claude blog case study into a reusable workflow for shipping a real iOS app using Claude Code as the primary development environment. (The skill name avoids reserved words required by the official naming rules.)

Source: https://claude.com/blog/how-a-non-technical-project-manager-built-and-shipped-a-stress-management-app-with-claude-code-in-six-weeks

## Instructions

### 1) Define the outcome and constraints
- Write a one-sentence goal.
- List platform constraints (e.g., “iOS only”, “no Android test device”, “App Store submission required”).
- Capture success metrics (e.g., retention, funnel conversion, DAU/MAU).

Use the lightweight brief template: [templates/project-brief.md](./templates/project-brief.md)

### 2) Start with a “minimum lovable” prototype
- Ask for a working end-to-end slice quickly.
- Prefer a prototype that can be rewritten, as long as it validates the core loop.

Example seed prompt from the post:
- “Hey Claude, just give me an application that will make me less stressed.”

### 3) Split work into specialist roles (subagents)
The post describes coordinating many specialist subagents. If you have access to subagents, create roles aligned to your architecture and platform needs.

Document the roles you will use (don’t invent new roles beyond what your project needs). Suggested role brief format is in: [templates/subagent-role-brief.md](./templates/subagent-role-brief.md)

### 4) Iterate toward production quality
- Add crash reporting and analytics.
- Use screenshot-driven debugging when UI or device-specific behavior is involved.
- If your prototype stack is mismatched to your constraints, do a focused rewrite (e.g., pivot from a cross-platform prototype to native).

### 5) Launch tasks (non-coding)
Use Claude for:
- App Store submission checklists and copy
- Marketing assets and drafts
- A growth roadmap

### 6) Measure and refine
- Track funnels and retention.
- Use analytics to prioritize iterations.

## Examples

### Example: “Day Zero Questionnaire” for founder/operator context
Use this to quickly understand who is building and how they work.

See: [templates/day-zero-questionnaire.md](./templates/day-zero-questionnaire.md)
