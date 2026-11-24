# Brand, logo and positioning (BRD)

| ID | L | Requirement |
| --- | --- | --- |
| BRD-01 | 1 | One-sentence value proposition + ICP (who pays, who uses) in `PRODUCT.md`; reused in hero, welcome email, app store copy |
| BRD-02 | 1 | Domain(s) registered, social handles reserved, company legal name/tax ID ready for footer and invoices |
| BRD-03 | 1 | Logo as SVG in 4 variants: full, mark-only, monochrome, inverted, in `docs/brand/` |
| BRD-04 | 1 | Logo legible at 16 px; clear-space and minimum-size rules written down |
| BRD-05 | 1 | Favicon set generated (`ico`, `svg`, `apple-touch-icon`, manifest icons) via `npx realfavicon generate` or `favicons`; passes favicon checker |
| BRD-06 | 1 | Voice and tone: 3–5 rules with do/don't examples, applied to UI, email, support |
| BRD-07 | 1 | OG image template per public page type (satori), built from brand tokens |
| BRD-08 | 2 | Brand book in `docs/brand/README.md`: logo usage, colors, type, voice, do/don't |
| BRD-09 | 2 | Press kit: logos, screenshots, short/long description |

**Logo procedure (no mature logo tool exists — do this):** agent hand-writes 6–10 SVG concepts (wordmark + simple geometric mark, 1–2 colors, must survive 16 px and monochrome) → renders them with Playwright onto one comparison sheet → user picks → agent produces the 4 variants of BRD-03 → favicon set (BRD-05). Palette from the logo in OKLCH (oklch.com, Radix Colors 12-step scales, `culori` to script scales).
