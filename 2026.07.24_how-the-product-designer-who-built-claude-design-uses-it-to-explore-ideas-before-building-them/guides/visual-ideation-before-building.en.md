**English** · [한국어](./visual-ideation-before-building.ko.md) · [Español](./visual-ideation-before-building.es.md) · [日本語](./visual-ideation-before-building.ja.md)

# Visual ideation before building

How Claude Design came about, what it is and isn't for, and the ten practices its
creator uses daily.

## The problem: design became the constraint

In the fall of 2025, Nate Parrott was the only product designer on Claude Code for
VS Code, working with two engineers to reimagine everything Claude Code does for a
friendly interface outside the terminal. The beta shipped at the end of September,
Opus 4.5 arrived in November, and the team started shipping fast and aggressively.

"The engineers were shipping far more than before, while I was still delivering at
the pace I always had. I needed to find a way to catch up."

## The failed first attempt

Claude Code runs in the terminal, where everything is text-based, and the first
attempt treated design that way: copy output into Claude, add screenshots, and ask
"Here's a feature we want to add. Why don't you design it?"

The results weren't good. For about a month, as a side project, the search
continued for a way to improve design output.

## The breakthrough: HTML as a medium

Eventually: Claude is really good with HTML. And HTML is not only the format for
websites — "it's also a rich, interactive visual medium: anything you can make in a
slide deck, a video file, or a PDF, you can make in a web page."

Two moves followed:

1. **A split view.** Prompt for HTML, chat on the left, live output on the right.
2. **Brand in the prompt.** Product design is driven by applying knowledge of the
   product and brand you work on, so the essence of Anthropic's brand — the fonts,
   colors, assets, and principles its products use — was distilled into prompts.
   Output then came out compliant with the brand guide by default.

Designers picked up the internal prototype immediately, for interactive prototypes
in particular. Making a click-through prototype in traditional design tools means
mocking up every state of every screen and wiring them together by hand. Here, you
hand Claude your assets and say: make it work. And every artifact it delivers has a
link you can share the way you'd share a doc.

## From side project to real project

The moment it became clear was an idea pitch session at an Anthropic Labs team
offsite: "every person there threw together slides using it, often in the middle of
the meeting before their turn to present." That session convinced the Labs team to
staff it.

The framing widened. It stopped being a tool for product mockups and became a tool
for producing any kind of visual communication: slide decks, landing pages,
one-pagers you print as a PDF, emails, animations, visuals to share on social
media. Parrott describes it as "one click above product design: you collaborate
with Claude on visuals whose main job is communication and ideation."

Capability tracks vision models. Claude Opus 5 is better than previous Opus models
at reading charts, diagrams, and screenshots, which makes it powerful when paired
with Claude Design for presentation-worthy decks and memos.

## What it is not meant to do

**Logo design.** There is no image model and it isn't built for image generation,
so it's a poor fit for logos — "though that hasn't stopped people from trying." The
better approach is to bring in the logo and assets you already have. The rest of
the product works the same way: Claude creates options and starting points so you
don't have to stare at a blank canvas, and you choose what's good on its own, or as
a combination of multiple versions.

**Production software.** If you're shipping production software, stick with Claude
Code. Claude Code is for coding; Claude Design is for the other parts of design
work: early ideation, collaboration, or getting buy-in on a direction before anyone
commits to building it.

The two round-trip. Sync a prototype you started in Claude Code to Claude Design
for iteration and editing on the canvas, or hand off a prototype you're ready to
build from Claude Design to Claude Code.

And the reason the boundary matters: "As models get better at building production
software, the work that matters most moves earlier in the process: having good
ideas, getting everyone aligned, and collecting feedback while an idea is still
early."

## Daily use

Bread-and-butter design work: wireframing early ideas, or generating 15 versions of
a flow to collect feedback from colleagues. Recent examples:

- **The intro animation.** The animation that plays when you sign up was made in
  the tool itself, but not directly: "I'm not an animator, so I first had Claude
  Design build me a bespoke video editor, then used that editor to make the
  animation."
- **A subway-times app** with adjustable animation controls, for dialing in the
  physics of the motion.
- **Instagram-style color controls** — tweaking an app's color scheme with sliders
  and presets rather than describing colors in words.
- **A redesign of Claude Design itself**, riffed on with two teammates, Helen and
  Andrew, inside the tool. It won't ship as-is; it's how they explore what the
  product could become.

## The ten practices

1. **Do the thinking before you prompt.** Tell Claude what you need up front.
   Parrott spends a lot of time writing prompts before designing — dictated with
   the voice button, typed in the Notes app on the couch, or recorded as a voice
   note on a walk and pasted in later. Figure out what you want while you're away
   from the computer, so Claude can execute your exact vision when you sit down.
2. **Tell Claude what it should look like.** "Left undirected, Claude picks one of
   its favorite aesthetics. You'd probably recognize them." Head that off by
   specifying fonts and colors, providing a moodboard, or brainstorming
   font-and-color pairings until one feels right.
3. **Turn recurring work into a design system.** Upload brand files and assets —
   logos, slide decks, screenshots, typography specs, anything reused — and Claude
   analyzes them into a design system, so each artifact starts from your choices
   rather than a blank slate.
4. **Ask for ten options, then remix.** Most won't be good; one or two will. Then:
   "I like option B and a little of option D. Give me five riffs that smoosh those
   together."
5. **Sketch what you can't describe.** A layout in your head with no words for it:
   draw it on paper and upload a photo.
6. **Point and talk.** Instead of writing a paragraph identifying which element you
   mean, click it and speak. Enable dictation on your device, select "comment", and
   click into the comment box; your words appear as if typed.
7. **Wireframe first when fidelity doesn't matter.** Much faster, and it keeps
   Claude focused on higher-level structure instead of visuals — a great way to try
   many ideas quickly.
8. **Make the last mile manual.** Use direct editing tools — rearrange, delete,
   edit text, resize, change colors — for final touches instead of prompting.
   "Direct edits use no tokens, and small calls like sizing and alignment are
   better eyeballed anyway."
9. **Give Claude your real context.** Connect GitHub and Claude fetches your
   components and existing screens as a starting point; with a few tries it can
   recreate existing designs with pretty high fidelity. Web search and MCP
   connections work too, whenever the design depends on outside information.
10. **Keep working alongside Claude.** You don't have to wait for a finished result
    before prompting new changes or tasks. Queue up multiple messages at once, or
    keep talking while Claude is still working on the previous turn.

## Make it alive

There's a Bret Victor talk called "Stop Drawing Dead Fish". From the blurb:
"Everything we draw should be alive by default."

Parrott's encouragement to designers, in this tool or any other, is to think about
how to make their creations alive. His favorite creations are the ones that don't
fit into existing boxes: docs with interactive simulations, slide decks that talk
to you, diagrams that are also videos, designs that are also their own editors.
Code, specifically HTML, is an amazing medium for creativity, and it's finally
somewhat easy for designers to create with.

Claude Design took its current shape because people at Anthropic kept finding uses
he hadn't planned for. It is now in beta on Claude Pro, Max, Team, and Enterprise
plans, with an invitation to "take it somewhere we haven't thought of yet."

## Source

[How the product designer who built Claude Design uses it to explore ideas before building them](https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them) — Nate Parrott, July 24, 2026. The article expresses his opinions, usage patterns, and advice.
