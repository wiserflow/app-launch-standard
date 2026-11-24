# UX polish (UX)

Detailed interaction rules → ux-patterns.md (UXP)

| ID | L | Requirement |
| --- | --- | --- |
| UX-01 | 1 | Tested on real phones (iOS + Android) and a 1280×720 laptop screen. Proof: dated device matrix or device-cloud report (e.g. BrowserStack) over the core flows listed in the PRD |
| UX-02 | 1 | Every action has loading, error (human message + next step) and success feedback. Proof: pass over the actions of the core flows listed in the PRD |
| UX-03 | 1 | Locale formatting: currency, dates, time zone, local document/phone masks (masks n/a if the app collects no such fields). Proof: check each date, currency and input field of the core flows |
| UX-04 | 1 | Per-page `<title>`, correct favicon, no framework defaults left anywhere (unique titles also → A11Y-12) |
| UX-05 | 1 | Accessibility baseline → see `accessibility.md` (A11Y-01..06); not counted separately, status follows those items |
| UX-06 | 2 | Installable PWA (icons, splash, offline fallback page) |
| UX-07 | 2 | Keyboard shortcuts + command palette (`⌘K`) |
| UX-08 | 3 | i18n → see `i18n.md` |

---
