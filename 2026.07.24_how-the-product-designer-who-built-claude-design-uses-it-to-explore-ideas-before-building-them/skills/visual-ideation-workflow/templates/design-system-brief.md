# Design system brief

Turn recurring work into a reusable starting point, so each artifact begins from
your choices rather than a blank slate. This is the same move that made the
original tool brand-compliant: the essence of a brand — fonts, colors, assets, and
principles — distilled into prompts.

## 1. Upload everything you reuse

- [ ] Logos (all lockups and sizes you actually use)
- [ ] Brand files and guidelines
- [ ] Slide decks that represent the house style
- [ ] Screenshots of existing product surfaces
- [ ] Typography specs
- [ ] Icon sets, illustration assets, photography
- [ ] Anything else that shows up in artifact after artifact

## 2. Ask for a design system back

Request an analysis of the uploads that produces, at minimum:

- **Typography** — families, weights, sizes, and what each is for
- **Color** — the palette, with roles (background, surface, text, accent, states)
- **Spacing and layout** — the grid, the rhythm, standard margins
- **Components** — buttons, cards, nav, form fields, as they already exist
- **Principles** — the stated reasons behind the above, in a form that can be
  applied to a new surface not covered by the existing material

## 3. Fill in the prompt block

Keep a short block you paste at the start of any new artifact:

```
Brand: <name>
Fonts: <display> for headings, <text> for body. <weights and sizes>
Colors: <hex list with roles>
Assets: <which uploaded files to draw from>
Principles: <2–5 lines — the aesthetic rules that are not obvious from the assets>
Avoid: <the generic defaults you keep getting>
```

## 4. Attach live context where it exists

A static system is a floor, not a ceiling. Where the design touches an existing
product, connect the repository so components and existing screens are fetched and
used as a starting point — with a few tries this can recreate existing designs at
high fidelity. Add web search or MCP connections when the design depends on
information from outside.

## 5. Re-derive when the brand moves

Regenerate the system when the underlying assets change, rather than patching the
prompt block by hand. The uploads are the source of truth; the block is a cache.

## Source

Adapted from [How the product designer who built Claude Design uses it to explore ideas before building them](https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them) — Nate Parrott, July 24, 2026
