# Accessibility (A11Y)

Target: WCAG 2.2 AA. Many jurisdictions mandate it (EU European Accessibility Act, US ADA/Section 508, Brazil LBI) — confirm with counsel.

| ID | L | Requirement |
| --- | --- | --- |
| A11Y-01 | 1 | axe (Playwright) shows 0 critical/serious violations on signup, login, core flow and checkout; runs in CI |
| A11Y-02 | 1 | Every flow completable by keyboard: visible focus, no trap, logical order |
| A11Y-03 | 1 | Every input has a programmatic label; errors are text tied to the field (not color only) |
| A11Y-04 | 1 | Contrast ≥ 4.5:1 text, ≥ 3:1 UI and large text |
| A11Y-05 | 1 | Images and icon buttons have alt/accessible name; `lang` set; unique page titles |
| A11Y-06 | 1 | Works at 200% zoom and 320 px width; `prefers-reduced-motion` respected |
| A11Y-07 | 2 | WCAG 2.2 additions: target size ≥ 24 px, focus not obscured, no drag-only actions, accessible auth (paste and password managers allowed) |
| A11Y-08 | 2 | Manual screen-reader pass (NVDA or VoiceOver) on the core flow; dynamic updates via live regions |
| A11Y-09 | 2 | Accessibility statement + contact channel published |
| A11Y-10 | 3 | External audit or VPAT/ACR; a11y acceptance criteria in the definition of done |

References: [A11Y Project checklist](https://www.a11yproject.com/checklist/) · [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/) · [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) · [Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing).
