---
name: visual-ideation-workflow
description: Explore, iterate on, and share visual ideas early — product prototypes, slide decks, landing pages, one-pagers, animations — by treating HTML as an interactive visual medium and directing the aesthetic explicitly. Use when engineering throughput has outrun design, when you need many versions of a flow fast for feedback, when generated visuals keep drifting to a generic look, or when deciding whether work belongs in early ideation or in production code.
---

# Visual ideation workflow

The working method Nate Parrott used to build and then use Claude Design: get
visual ideas out fast, in a medium that is interactive by default, before anyone
commits to building them.

The problem it solves is a throughput mismatch. When engineers ship faster and
design does not, the design step becomes the constraint. And as models get better
at building production software, the work that matters most moves earlier in the
process: having good ideas, getting everyone aligned, and collecting feedback while
an idea is still early.

## Instructions

### 1. Treat HTML as a visual medium, not a website format

The first attempt that failed was treating design as text: copying terminal output
into a chat, adding screenshots, and asking for a design. What worked was
recognizing that HTML is "a rich, interactive visual medium: anything you can make
in a slide deck, a video file, or a PDF, you can make in a web page."

Ask for HTML artifacts and view them live beside the conversation. The scope of
what you can ask for widens accordingly: slide decks, landing pages, one-pagers you
print as a PDF, emails, animations, visuals to share on social media.

### 2. Do the thinking before you prompt

The most efficient way to get output matching your vision is to tell it what you
need up front. Write prompts away from the computer — dictation, a notes app on the
couch, a voice memo on a walk that you paste in later. Figure out what you want
while you are away from the keyboard, so the model executes your exact vision when
you sit down.

Use [templates/pre-prompt-brief.md](templates/pre-prompt-brief.md) to capture a
vision before opening the tool.

### 3. Say what it should look like

Left undirected, the model picks one of its favorite aesthetics — recognizable ones.
Head that off by specifying fonts and colors, providing a moodboard of images for
inspiration, or asking for font-and-color pairings and going back and forth until
one feels right.

### 4. Turn recurring work into a design system

Upload brand files and assets — logos, slide decks, screenshots, typography specs,
anything reused — and have them analyzed into a design system. Every artifact after
that starts from your choices rather than a blank slate. This is also what makes
output brand-compliant by default: distilling fonts, colors, assets, and principles
into prompts is exactly how Claude Design was made to respect a brand guide.

[templates/design-system-brief.md](templates/design-system-brief.md) lists what to
upload and what to ask for back.

### 5. Ask for ten options, then remix

Most won't be good, and that's fine; one or two will. Then name the parts that
worked and ask for hybrids: "I like option B and a little of option D. Give me five
riffs that smoosh those together."

The full loop, including how to keep option identity stable across rounds, is in
[examples/ten-options-remix.md](examples/ten-options-remix.md).

### 6. Wireframe first when fidelity doesn't matter

Asking for wireframes is much faster and keeps attention on high-level structure
instead of visuals — a good way to try many different ideas quickly. Save fidelity
for the direction you have already chosen.

### 7. Sketch or point when words fail

If a layout is in your head and you have no words for it, draw it on paper and
upload a photo. To refer to a specific element, don't write a paragraph identifying
it — click on it and speak, with device dictation enabled, into the comment box.

### 8. Give it your real context

Connect GitHub so your components and existing screens are fetched and used as a
starting point; with a few tries this can recreate existing designs with high
fidelity. Web search and MCP connections work too, whenever the design depends on
outside information.

### 9. Make the last mile manual

Use direct editing tools — rearrange, delete, edit text, resize, change colors —
for final touches instead of prompting for them. "Direct edits use no tokens, and
small calls like sizing and alignment are better eyeballed anyway."

### 10. Keep working alongside the model

Don't wait for a finished result before prompting new changes. Queue multiple
messages at once, or keep talking while the previous turn is still being worked on.

### 11. Know the boundaries

There is no image model here, so logo design is a poor fit — bring the logo and
assets you already have. For shipping production software, use Claude Code. The two
round-trip in both directions. See
[references/scope-and-round-trip.md](references/scope-and-round-trip.md).

### 12. Make it alive

From Bret Victor's "Stop Drawing Dead Fish": "Everything we draw should be alive by
default." The most interesting outputs are the ones that don't fit existing boxes —
docs with interactive simulations, slide decks that talk to you, diagrams that are
also videos, designs that are also their own editors. When a static artifact would
do, ask what an interactive one would show instead.
[examples/tools-that-build-tools.md](examples/tools-that-build-tools.md) works
through the case where the artifact you need is a tool for making the artifact.

## Examples

### Catching up with engineering

A lone designer on a team of fast-shipping engineers stops mocking every state of
every screen by hand. Instead they hand over their assets and say "make it work",
producing a click-through prototype with a shareable link — the same way you'd
share a doc — and generate fifteen versions of a flow to collect colleague feedback
in the time one high-fidelity mock used to take.

### Slides in the middle of the meeting

At an idea pitch session, participants assemble their slides during the meeting,
before their turn to present. The artifact is disposable; the point is that the
idea gets seen at all. This is the usage pattern that turned an internal side
project into a staffed one.

### Building the tool that builds the artifact

The intro animation for Claude Design was made in the tool itself, but indirectly:
"I'm not an animator, so I first had Claude Design build me a bespoke video editor,
then used that editor to make the animation." When you lack the craft skill for a
medium, ask for the instrument rather than the performance.

### Controls instead of adjectives

Rather than describing colors in words, ask for Instagram-style sliders and presets
that let you tweak an app's color scheme directly. Same for motion: a subway-times
app with adjustable animation controls lets you dial in the physics rather than
argue about "snappier".

### Deciding where work belongs

A team wants to explore a redesign of a product's editor. That is early ideation, so
it happens on the canvas — three people riffing on a new design they explicitly
won't ship as-is, because the point is to explore what the product could become.
When a direction is chosen and production code starts, the prototype hands off to
Claude Code.

## Source

[How the product designer who built Claude Design uses it to explore ideas before building them](https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them) — Nate Parrott, July 24, 2026
