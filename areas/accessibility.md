# Accessibility (A11Y)

Target: WCAG 2.2 AA. Many jurisdictions mandate it (EU European Accessibility Act, US ADA/Section 508, Brazil LBI) — confirm with counsel.

| ID | L | Requirement |
| --- | --- | --- |
| A11Y-01 | 1 | axe (e.g. via Playwright) shows 0 critical/serious violations on signup, login and the core flows listed in the PRD (checkout only if it exists); with no PRD yet, the core flows are those recorded in the audit (STATUS.md evidence) or the app's main journeys (signup, login, the core action). Native apps: equivalent check with the platform accessibility inspector/VoiceOver/TalkBack instead of axe (axe stays e.g. for web). Proof: automated run or a recorded manual pass with screenshots |
| A11Y-11 | 2 | The axe check of A11Y-01 runs in CI on every PR (→ CI-02) |
| A11Y-02 | 1 | Every core flow completable by keyboard: visible focus, no trap, logical order. Proof: automated keyboard test or a manual pass over the core flows listed in the PRD (or, with no PRD yet, those recorded in the audit or the app's main journeys: signup, login, the core action), recorded. Native apps: same check with the platform screen reader/keyboard support |
| A11Y-03 | 1 | Every input has a programmatic label; errors are text tied to the field (not color only). Proof: axe label rules plus a manual check of the signup, login and core-flow forms |
| A11Y-04 | 1 | Contrast ≥ 4.5:1 text, ≥ 3:1 UI and large text. Proof: axe contrast rule or a contrast checker over the landing, auth and core screens and both themes if any |
| A11Y-05 | 1 | Images and icon buttons have alt/accessible name. Proof: axe rules over the screens of A11Y-01 |
| A11Y-12 | 2 | `lang` set on the document; unique, descriptive page titles per route |
| A11Y-06 | 1 | Works at 200% zoom and 320 px width; `prefers-reduced-motion` respected. Proof: manual pass or viewport test over the core flows listed in the PRD |
| A11Y-07 | 2 | WCAG 2.2 additions: target size ≥ 24 px, focus not obscured, no drag-only actions, accessible auth (paste and password managers allowed) |
| A11Y-08 | 2 | Manual screen-reader pass (NVDA or VoiceOver) on the core flow; dynamic updates via live regions |
| A11Y-09 | 2 | Accessibility statement + contact channel published |
| A11Y-10 | 3 | External audit or VPAT/ACR; a11y acceptance criteria in the definition of done |

References: [A11Y Project checklist](https://www.a11yproject.com/checklist/) · [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/) · [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) · [Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing).
