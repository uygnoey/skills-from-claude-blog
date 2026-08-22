**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A first-person account by Nate Parrott, a product designer at Anthropic, of how the tool he built — Claude Design, now in beta — came to exist and how he uses it daily.

The origin is a throughput mismatch. In fall 2025 Parrott was the only product designer on Claude Code for VS Code, working with two engineers. The beta shipped at the end of September, Opus 4.5 arrived in November, and the team started shipping fast: "The engineers were shipping far more than before, while I was still delivering at the pace I always had. I needed to find a way to catch up."

His first attempt treated design the way the terminal treats everything — as text. He copied output into Claude, added screenshots, and asked it to design a feature. The results weren't good. The breakthrough was noticing that Claude is very good with HTML, and that HTML is not merely a website format: "anything you can make in a slide deck, a video file, or a PDF, you can make in a web page." He prompted Claude to produce HTML, gave it a split view — chat on the left, live output on the right — and then spent a while distilling Anthropic's brand (fonts, colors, assets, principles) into prompts so output came out brand-compliant. Designers picked up the internal prototype immediately for interactive prototypes, because instead of mocking up every state of every screen and wiring them together by hand, you hand Claude your assets and say: make it work.

It became a real project after an Anthropic Labs offsite pitch session where "every person there threw together slides using it, often in the middle of the meeting before their turn to present." The framing widened from product mockups to any kind of visual communication — slide decks, landing pages, one-pagers you print as a PDF, emails, animations, social visuals — which Parrott describes as "one click above product design."

The post also draws boundaries. There is no image model, so it is a poor fit for logo design; bring the logo and assets you already have. For shipping production software, use Claude Code. The two round-trip: sync a prototype from Claude Code into Claude Design for canvas iteration, or hand off from Claude Design to Claude Code to build. The bulk of the piece is ten concrete working practices, then a closing argument, by way of Bret Victor's "Stop Drawing Dead Fish", for making designs that are alive.

## When is it useful?
- When engineering throughput has outrun design throughput and the design step has become the constraint.
- When you need fifteen versions of a flow to collect feedback, and traditional click-through prototyping — mocking every state and wiring it by hand — is too slow.
- When deciding whether a piece of work belongs in a design tool, in Claude Design, or in Claude Code.
- When your generated visuals keep drifting toward a generic aesthetic and you need to direct them.
- When the same brand, deck, or component set shows up in every artifact and you want a reusable starting point instead of a blank canvas.
- When you need buy-in on a direction before anyone commits to building it.

## Key points
- **HTML is the medium, not the output format.** Treating HTML as a rich, interactive visual medium — capable of anything a deck, a video, or a PDF can do — is what made design output good, after text-plus-screenshots failed.
- **Brand goes in the prompt.** Distilling fonts, colors, assets, and principles into prompts is what makes output compliant by default rather than by correction.
- **The value is upstream of building.** "Claude Code is for coding; Claude Design is for the other parts of the design work: early ideation, collaboration, or getting buy-in on a direction before anyone commits to building it." As models get better at production software, the work that matters most moves earlier: having good ideas, getting everyone aligned, collecting feedback while an idea is still early.
- **Round-trip, not either/or.** Prototypes sync from Claude Code into Claude Design for canvas iteration, and hand off from Claude Design to Claude Code when ready to build.
- **Know what it is not.** No image model, so logo design is a poor fit — bring your existing logo and assets instead. The product's general shape is that Claude creates options and starting points so you don't stare at a blank canvas, and you pick what's good on its own or as a combination.
- **Do the thinking before you prompt.** Parrott writes prompts away from the computer — dictation, the Notes app, a voice memo on a walk — so that at the keyboard Claude executes an already-decided vision.
- **Direct the aesthetic or inherit a default.** "Left undirected, Claude picks one of its favorite aesthetics. You'd probably recognize them." Specify fonts and colors, supply a moodboard, or brainstorm font-and-color pairings.
- **Ten options, then remix.** Most won't be good; one or two will. Then: "I like option B and a little of option D. Give me five riffs that smoosh those together."
- **Make the last mile manual.** Rearranging, deleting, editing text, resizing, and recoloring are better done with direct editing tools — "Direct edits use no tokens, and small calls like sizing and alignment are better eyeballed anyway."
- **Give it your real context.** Connect GitHub so Claude fetches your components and existing screens as a starting point; web search and MCP connections work too when a design depends on outside information.
- **Make it alive.** Citing Bret Victor's "Stop Drawing Dead Fish" — "Everything we draw should be alive by default" — Parrott's favorite creations are the ones that don't fit existing boxes: docs with interactive simulations, slide decks that talk to you, diagrams that are also videos, designs that are also their own editors.

## Bundled resources
- `skills/visual-ideation-workflow/` — the ten working practices as an operating procedure, plus a reference on scope boundaries and the round-trip with Claude Code, templates for the pre-prompt brief and the reusable design system, and worked examples of the ten-options remix loop and of designs that build their own tools.
- `guides/visual-ideation-before-building.{en,ko,es,ja}.md` — the full walkthrough in four languages.

## Source
[How the product designer who built Claude Design uses it to explore ideas before building them](https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them) — Nate Parrott, July 24, 2026
