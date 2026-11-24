# Design system and prototyping (DES)

Design is where agents drift most: each screen invents its own spacing, colors and components. The fix is **one source of truth** (`DESIGN.md` + `@theme` tokens + one component registry), a **prototype approved before feature code**, and **automated gates** that do not rely on the agent remembering.

## Workflow for a new app (each step produces an artifact)

| # | Step | Tool | Artifact |
| --- | --- | --- | --- |
| 1 | Product brief: audience, job, tone, 3 reference products | `/impeccable init` | `PRODUCT.md` |
| 2 | Visual direction: 2–3 options (palette, type, density); user picks | `frontend-design` skill or ui-ux-pro-max `--design-system` | Comparison sheet (HTML + screenshot) |
| 3 | Logo (see BRD procedure) | Agent + Playwright render | `docs/brand/logo-*.svg` |
| 4 | Tokens: OKLCH semantic colors light/dark, type scale, spacing, radius, shadow, motion | `npx @google/design.md lint DESIGN.md` | `DESIGN.md` (lint clean) |
| 5 | Implement tokens in Tailwind v4 `@theme` with defaults reset; `shadcn init` with the theme | shadcn skill | `app.css`, `components.json` |
| 6 | Gates: Tailwind lint + edit-time design hook | `eslint-plugin-better-tailwindcss`, impeccable hook | Lint config, CI job |
| 7 | Component inventory: add from shadcn/own registry, every variant and state as a story | shadcn MCP, Storybook | Stories |
| 8 | Screen inventory + flows, lo-fi | `/impeccable shape`, Excalidraw skill | `docs/design/screens.md` + `docs/design/wireframes/*.excalidraw` |
| 9 | Clickable prototype with mock data, **only** existing components | Storybook page stories or `/prototype` route | Prototype URL + screenshots |
| 10 | User approval per screen; a new pattern goes back to step 7 first | Playwright screenshots | Approved screenshots = visual baselines |
| 11 | Build real screens from the approved prototype | Storybook MCP, shadcn MCP | Feature code |
| 12 | Review loop per screen: screenshot vs approved, fix | `/impeccable critique`/`audit`, `web-design-guidelines`, Playwright | Findings closed |
| 13 | Regression + a11y in CI | `toHaveScreenshot`, `@axe-core/playwright`, `impeccable detect` | CI gate |
| 14 | Emails + marketing site + OG from the same tokens (hex export for email) | React Email, Astro with shared CSS/registry, satori | Templates, site, OG |
| 15 | Extract and publish for the next app | `/impeccable extract`, `shadcn build` | Private shadcn registry (theme + components + blocks) |

**CLAUDE.md rule block (paste into every app):** "UI work: read `DESIGN.md` first. Only semantic tokens. Only components from `@/components/ui` or our registry. No arbitrary Tailwind values. New pattern → add it to the design system and stories first, then use it."

## Checklist

| ID | L | Requirement |
| --- | --- | --- |
| DES-01 | 1 | `DESIGN.md` exists (google-labs-code/design.md format) and `npx @google/design.md lint` reports 0 errors |
| DES-02 | 1 | All colors are semantic tokens in `@theme`; default Tailwind palette reset (`--color-*: initial`) so `bg-blue-500` does not exist |
| DES-03 | 1 | Light and dark themes defined; every text/background pair passes WCAG AA |
| DES-04 | 1 | One type scale, max 2 font families, fonts self-hosted |
| DES-05 | 1 | Spacing, radius, shadow scales defined; no arbitrary values in code (lint passes in CI) |
| DES-06 | 1 | Every UI primitive comes from shadcn or the own registry; no duplicate implementations of the same component |
| DES-07 | 1 | One form-field pattern (label, help, error), one icon set at consistent sizes, one page shell (header, nav, paddings) |
| DES-08 | 1 | Every screen prototyped and approved **before** feature code |
| DES-09 | 1 | Every screen has loading, empty and error states; checked at 375, 768, 1280 px |
| DES-10 | 1 | `CLAUDE.md` points to `DESIGN.md` with the rule block above |
| DES-11 | 2 | Each component has stories for all variants and states (hover, focus, disabled, loading, error) |
| DES-12 | 2 | Visual regression baseline per key screen, light and dark (`toHaveScreenshot`) |
| DES-13 | 2 | axe: 0 serious/critical violations on key screens |
| DES-14 | 2 | Design lint (`impeccable detect` or equivalent) passes in CI |
| DES-15 | 2 | Email hex palette generated from the same token source; site, emails and app compared side by side |
| DES-16 | 3 | Private shadcn registry shared across apps; DTCG tokens via Style Dictionary/Terrazzo only if non-web targets need them |

References: [design-system-checklist](https://github.com/ardakaracizmeli/design-system-checklist) · [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) · [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (DESIGN.md examples) · Atomic Design (Brad Frost) · Refactoring UI · Laws of UX.

Avoid as primary tools: v0, Figma Make, 21st.dev Magic — they emit their own styles and break the single token source. Figma/Penpot MCP only when a human designer joins.
