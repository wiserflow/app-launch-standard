# UX and UI patterns (UXP)

Goal: a rulebook an agent follows screen by screen and a reviewer checks with a screenshot — how screens are laid out, behave and talk, with numbers instead of adjectives. It is NOT the token/component source (`design.md`, DES), the WCAG baseline (`accessibility.md`, A11Y), first-run activation (`onboarding.md`, ONB), speed budgets (`performance.md`, PERF) or the shell — sidebar, user menu, org switcher, global search, breadcrumbs (`app-shell.md`, SHL).

How to use: **building** → apply the section's decision table, then its checklist. **Reviewing** → run the [Screen review protocol](#screen-review-protocol-2-minutes-per-screen). Numbers are defaults: an app may override one in `DESIGN.md`, and then that number rules every screen. A deviation not written there is a bug. A valid override is a number or token in `DESIGN.md` (the design-system doc), applied app-wide; a distinctive design world is fine when written there. **Proof for screen-by-screen rules:** the Screen review protocol screenshots over the core screens listed in the PRD (computed styles or a screenshot count for numeric limits); an "every screen" rule is ok when every sampled screen passes. Team-only rows are marked "(team accounts only)" and are n/a for one-person-per-account apps (kickoff question: one person per account or team accounts).

## Layout and spacing (UXP-L)

| ID | L | Requirement |
| --- | --- | --- |
| UXP-L1 | 1 | Spacing only from a 4 px-based scale (4, 8, 12, 16, 24, 32, 48, 64 → DES-05); space between groups ≥ 2× the space inside a group, so grouping is visible without drawing boxes |
| UXP-L2 | 1 | Content sits on a shared left edge; centered layout only for auth screens, empty states and dialogs with ≤ 2 lines of text |
| UXP-L3 | 1 | Width caps: running text 45–75 characters per line (~65ch); forms 480–640 px; app content ≤ 1440 px (not stretched at 1920); only tables, boards and canvases go full width |
| UXP-L4 | 1 | Same page header anatomy everywhere: h1 title top-left, at most 1 primary action top-right, optional one-line description under the title, then content (shell → DES-07) |
| UXP-L5 | 1 | Max 3 radius values (e.g. 6 px controls, 8–12 px cards and dialogs, full for pills/avatars), nested radius = outer − padding; max 3 elevation levels (flat, raised, overlay); a surface is separated by border OR shadow OR background, one per component; no card inside card |
| UXP-L6 | 1 | Color budget: neutrals ≥ 80% of the screen (estimated on the screenshot); the accent color only on the primary action, links and selected state; red/amber/green/blue only for status and always with icon or text (→ A11Y-03) |
| UXP-L7 | 2 | Page padding 16 px below 640, 24 px at 640–1023, 32 px from 1024; control height 36–40 px desktop and 44–48 px touch; all controls on one row share one height |

## Typography and hierarchy (UXP-T)

| ID | L | Requirement |
| --- | --- | --- |
| UXP-T1 | 1 | Per screen: ≤ 4 font sizes, ≤ 2 weights (400 + 500/600), ≤ 3 text colors (primary, secondary, muted), all from the scale (→ DES-04); body 14–16 px, nothing below 12 px; line-height 1.5 body, 1.2–1.3 headings |
| UXP-T2 | 1 | One focal point (proof: screenshot review): blur the screenshot 8 px (squint test) and the page title and the primary action are still the 2 most prominent things; hierarchy is built with weight and color before size |
| UXP-T3 | 1 | One h1 per page, equal to the nav label and the `<title>` (native: screen title; → UX-04); heading levels not skipped |
| UXP-T4 | 1 | Overflow is designed: single-line truncation with ellipsis and the full value on hover/focus (native: long-press, tap-to-expand or accessibility label); verified with a 60-char name, an 80-char email and a 12-digit number — no overlap, no wrap that breaks the row, no clipped text |
| UXP-T5 | 1 | Icons: one set (→ DES-07), sizes 16/20/24 only, one stroke weight; no emoji as icons; icon-only buttons limited to universal icons (close, search, more, back, copy) and always with a tooltip (→ A11Y-05) |
| UXP-T6 | 2 | Numbers that are compared or that change (tables, tiles, timers) use tabular figures; ALL CAPS only on labels of ≤ 3 words; no justified or centered paragraphs; underline only for links |

## Forms (UXP-F)

| The user must… | Control |
| --- | --- |
| Turn something on/off with immediate effect | Switch |
| Turn something on/off that applies on Save, or give consent | Checkbox |
| Pick 1 of 2–5 | Radio group (segmented control for view modes) |
| Pick 1 of 6–15 | Select |
| Pick 1 of more than 15, or from server-side data | Searchable combobox |
| Pick several of ≤ 7 | Checkbox group |
| Pick several of more than 7 | Multi-select combobox with removable chips |
| Enter a number | Numeric input (stepper only for 1–10 ranges; slider only when precision is irrelevant, paired with an input) |
| Enter a date known by heart (birth date) | Typed day/month/year fields — not a calendar |
| Enter a nearby date (due date, booking) | Date picker that also accepts typing |

| ID | L | Requirement |
| --- | --- | --- |
| UXP-F1 | 1 | Single column, one field per row; side by side only for short related pairs (city/state, expiry/CVC); field width hints at the expected length |
| UXP-F2 | 1 | Label always visible above the field; a placeholder never replaces the label and holds only an example format; help needed to fill the field is text under it, not a tooltip (field pattern → DES-07) |
| UXP-F3 | 1 | Only fields the task needs now; optional ones marked "(optional)" instead of asterisks on required; nothing derivable is asked (country from locale, name from the invite); the most common choice is pre-selected |
| UXP-F4 | 1 | Control chosen by the control table at the top of this section |
| UXP-F5 | 1 | Correct `type`, `inputmode` and `autocomplete` on every input (email, tel, numeric, one-time-code, new-password) so the right mobile keyboard and password manager appear (native: keyboard type, `textContentType`/autofill hints or equivalent; → A11Y-07; proof: lint rule or grep of the input components, or a pass over the PRD core flows); input is forgiving — trims spaces, accepts pasted formatted values (phone with spaces, decimal comma or point) and normalizes them itself (masks → UX-03) |
| UXP-F6 | 1 | Keyboard: Tab order = visual order; Enter submits single-line forms; Ctrl/⌘+Enter submits forms with a textarea; first field autofocused on desktop in dedicated form pages and dialogs; native: logical focus order and hardware-keyboard support where the platform offers it |
| UXP-F7 | 1 | One save model per form: explicit (Save + Cancel visible without scrolling — sticky footer on long forms) or autosave (with status → UXP-K5); never both in one form (settings pages → UXP-A2) |
| UXP-F8 | 1 | A dirty form is protected: leaving or closing asks "Discard changes?"; typed input survives a failed submit, a session expiry and Back/Forward |
| UXP-F9 | 2 | More than 8 fields → titled sections of ≤ 7 fields; more than 2 viewports or branching logic → multi-step with "Step 2 of 4", each step a URL, Back keeps data, review summary before the final submit |
| UXP-F10 | 2 | File upload: click and drag-and-drop (web; native: picker/share sheet); accepted types and max size stated before picking; per-file progress, cancel and retry; file name or preview plus remove after upload |

## Validation and errors (UXP-V)

| ID | L | Requirement |
| --- | --- | --- |
| UXP-V1 | 1 | Timing: validate on blur — never on focus, never while the user is still typing a field for the first time; once a field shows an error, re-validate on every change so it clears the instant it is fixed |
| UXP-V2 | 1 | Error text sits directly under its field with icon and danger border and says how to fix it (→ A11Y-03, UXP-C3); a toast is never the only place a field error appears |
| UXP-V3 | 1 | Submit stays enabled; pressing it with invalid data reveals every error, then focuses and scrolls to the first; forms taller than one viewport also get an error summary on top linking to each field |
| UXP-V4 | 1 | Server-side errors (→ SEC-06) land on the same field UI as client errors; non-field errors show as an inline alert next to the submit button and stay until the next attempt |
| UXP-V5 | 2 | Prevent instead of reject: unavailable dates disabled, min/max enforced by the control, character counter from 80% of the limit; async checks (slug or email taken, coupon) run debounced 300–500 ms and show checking / ok / taken inline before submit |

## Buttons and actions (UXP-B)

| ID | L | Requirement |
| --- | --- | --- |
| UXP-B1 | 1 | Exactly 1 primary (filled accent) button per view, dialog or card; the rest secondary (outline), ghost or link; ≤ 4 button variants and ≤ 3 button sizes in the whole app (icon sizes → UXP-T5) |
| UXP-B2 | 1 | Label = verb + object naming the outcome ("Create invoice", "Send invite"); never "OK", "Submit", "Yes", "Confirm" or "Click here" |
| UXP-B3 | 1 | Placement fixed app-wide: page primary action top-right of the header; forms on a page → actions left-aligned under the fields, primary first; dialogs → actions right-aligned, primary rightmost with Cancel to its left |
| UXP-B4 | 1 | Pending: the button shows a spinner, keeps its width and blocks re-click; double-click or Enter-spam creates exactly 1 record |
| UXP-B5 | 1 | No unexplained disabled control: tooltip or adjacent text gives the reason and the fix; an action the role can never perform is hidden (team accounts only; settings are the exception → UXP-A5) |
| UXP-B9 | 2 | Plan-gated action → visible with lock and plan name (→ BIL-01) |
| UXP-B6 | 1 | Links navigate, buttons act: whatever goes to a URL is a real `<a>` (Ctrl/⌘-click and middle-click open a new tab), including clickable rows and cards; whatever mutates is a `<button>` (web; native: navigation controls vs action controls with the matching accessibility traits/roles) |
| UXP-B7 | 1 | Every interactive element has visible default, hover, focus-visible, pressed and disabled states (→ DES-11) and reacts in < 100 ms; pointer cursor on clickable elements (hover, focus-visible and cursor: web/desktop only; native touch: pressed, disabled and focus for keyboard/switch control) |
| UXP-B8 | 2 | More than 3 actions on one object → 1–2 visible plus a "⋯" menu; menu items are icon + verb label; the destructive item is last, separated, in danger color |

## Destructive actions, undo and confirm (UXP-D)

| Action | Pattern |
| --- | --- |
| Reversible and cheap (archive, remove from a list, mark done, dismiss) | Execute at once + toast with **Undo** |
| Delete of a soft-deletable object | Execute at once + Undo toast; item goes to Trash |
| Irreversible, one item, contained impact (delete a file, revoke an invite) | Confirm dialog (UXP-D2) |
| Irreversible and cascading or high impact (delete project with children, workspace, account; rotate a live API key) | Dialog listing what is lost + **type the object's name** to enable the button (→ LGL-04) |
| Bulk destructive (more than 1 item) | Confirm dialog with the exact count, even when each item alone would only get Undo |
| Costly or external side effect (charge, send to N people, publish) | Summary + confirm (UXP-D7) |
| Initiated by an AI agent | → AI-04 |

| ID | L | Requirement |
| --- | --- | --- |
| UXP-D1 | 1 | Every destructive action is classified by the table; none runs on a single click with neither undo nor confirm |
| UXP-D2 | 1 | Confirm dialog: title = question naming the object ("Delete project 'Apollo'?"); body = consequence and irreversibility in ≤ 2 sentences with counts ("and its 14 tasks"); buttons repeat the verb ("Delete project" / "Cancel"); never "Are you sure?" with "Yes" / "No"; an inline confirm strip that meets the same rules (names the object, verb buttons, same focus and Esc behavior as UXP-D3) counts as a dialog |
| UXP-D3 | 1 | In destructive dialogs the initial focus is on Cancel, Enter does not destroy, Esc cancels; the filled danger style appears only on that final button — triggers in rows, menus and toolbars are neutral or danger text |
| UXP-D4 | 1 | Confirm dialogs are reserved for destructive, irreversible or costly actions: zero confirms on create, save, navigate or reversible actions (habituation kills the warning) |
| UXP-D5 | 1 | After a delete the user lands on the parent list with the item gone and a toast — never on a 404, a stale detail page or a list still showing the item |
| UXP-D6 | 2 | Undo toast stays ≥ 8 s, pauses on hover/focus (native: while touched or focused) and truly restores everything (position, relations, attachments); user-created primary objects are soft-deleted with restore from Trash/Archive for ≥ 30 days |
| UXP-D7 | 2 | Actions with external or costly side effects show a summary with exact counts, recipients and amounts ("Send to 312 contacts", "Charge $1,240.00") before the final button |

## Feedback: loading, success, failure (UXP-K)

| Wait | Feedback |
| --- | --- |
| < 100 ms | None beyond the control's own state change |
| 100–300 ms | Nothing new on screen (a loader here only flickers) |
| 300 ms – 1 s | In-button spinner for actions; thin top progress bar for navigation |
| 1–10 s | Skeleton shaped like the final layout (content) or spinner + specific text ("Importing 312 contacts…") |
| > 10 s | Determinate progress or named steps; user can leave; completion notified (UXP-K8) |

| Message | Channel |
| --- | --- |
| Action succeeded and the result is visible right there (toggle, inline edit, row added) | No message — the change is the feedback (optional inline "Saved") |
| Action succeeded and the result is elsewhere or invisible (sent, exported, copied) | Toast |
| Field is invalid | Inline under the field (UXP-V2) |
| Action or form failed | Inline alert next to the trigger, persistent; toast with Retry only when the trigger is no longer on screen |
| App-wide condition (offline, payment failed, trial ending, impersonation, maintenance) | Persistent banner on top of the shell, with its action |
| A decision is needed before continuing | Dialog |
| Background job finished | Toast if the user is present + notification entry (→ SUP-04) |

| ID | L | Requirement |
| --- | --- | --- |
| UXP-K1 | 1 | Waits follow the thresholds table: a loader appears only after 300 ms and, once shown, stays ≥ 300 ms; skeletons mirror the final layout (→ PERF-F10); a full-screen blocking spinner exists only at app boot or auth redirect |
| UXP-K2 | 1 | Refetch, sort, filter and pagination keep the current content on screen (dimmed or with a top progress bar); content is never swapped back to a skeleton or a blank area |
| UXP-K3 | 1 | Every message uses the channel from the table (baseline → UX-02); the Undo toast (UXP-D table) and the post-delete toast (UXP-D5) are allowed even though the result is visible |
| UXP-K4 | 1 | Toasts: one fixed position, ≤ 3 stacked, ≤ 2 lines, ≤ 1 action, success auto-dismisses in 4–6 s, errors persist until dismissed, all dismissible, never the only copy of information needed later |
| UXP-K5 | 1 | No silent outcome: with the network blocked every action ends in a visible error with Retry; autosave shows "Saving…" → "Saved" → "Couldn't save · Retry"; success names the object ("Invoice #1042 sent to ana@acme.com"), never bare "Success" or "Done"; proof: automated check with the network blocked, or a manual pass recorded with screenshots |
| UXP-K6 | 1 | Current state is readable on a still screenshot: active nav item, current tab, selected rows, applied filters, toggled options (proof: screenshots) |
| UXP-K7 | 2 | Optimistic UI for cheap frequent actions (toggle, star, check off, rename, reorder): change visible in < 100 ms, rolled back with a message on failure (→ PERF-F9) |
| UXP-K8 | 2 | Operations over 10 s run in the background (→ PERF-B7): progress or named steps, the user can navigate away, completion and failure are notified (→ SUP-04), cancel offered when feasible |

## Tables and lists (UXP-G)

| ID | L | Requirement |
| --- | --- | --- |
| UXP-G1 | 1 | Container: table when comparing ≥ 3 attributes across rows, cards for visual or browsable objects; below 640 px a table becomes stacked rows with its 2–3 key fields or scrolls horizontally with a sticky first column — never squeezed columns |
| UXP-G2 | 1 | Cells: text left; numbers and currency right with tabular figures and equal decimals; header aligned like its cells; empty value is "—" (never blank, "null" or mixed "N/A"); status is a badge with text |
| UXP-G10 | 2 | Cell details: numbers use tabular figures and equal decimals; booleans are never "true/false"; one line per cell (→ UXP-T4) |
| UXP-G3 | 1 | First column is the object's name and links to its detail; the whole row is clickable with a hover state (→ UXP-B6); ≤ 7 columns at 1280 px, the rest lives in the detail view or a column picker |
| UXP-G4 | 1 | Sorting: an intentional default (newest first for activity, A–Z for names); sortable headers show the direction arrow; sort runs server-side whenever the list is paginated (a small list loaded in full may sort client-side) |
| UXP-G5 | 1 | Sort, filters, search, page and tab live in the URL (native: restorable navigation state or deep link): reload/relaunch, share and Back reproduce the exact view; preferences (density, visible columns, collapsed panels) persist per user, not in the URL |
| UXP-G6 | 1 | Lists that can exceed 100 rows are paginated; a smaller list loaded in full needs no pagination but shows its total. Pagination: tables → pages of 25/50/100 with "1–25 of 312" when the total is cheap to count, otherwise cursor "Previous / Next" without a total (API stays cursor-based → PERF-B2); feeds → "Load more" or infinite scroll with position restored on Back; a filtered list shows "12 of 312" (→ PERF-B2) |
| UXP-G7 | 2 | Bulk actions: checkbox column, Shift-click range, header checkbox selects the page and offers "Select all 312"; an action bar shows the count and the actions; destructive bulk → UXP-D table |
| UXP-G8 | 2 | Row height 40–48 px (32–36 px in compact mode); header sticky when the table is taller than the viewport; row actions visible on hover AND focus and always visible on touch (native: swipe actions need a visible equivalent) (→ UXP-B8) |
| UXP-G9 | 3 | Where users live in the table: column show/hide/resize, saved views, density toggle, inline cell edit, CSV export of the current filtered view |

## Overlays (UXP-O)

| Need | Container |
| --- | --- |
| A decision, a confirm, or a short task of ≤ 5 fields that must not lose the page context | Modal dialog |
| Inspect or edit one item while the list stays visible; 5–15 fields; triage through items | Side drawer (right) with its own URL |
| More than 15 fields, multiple steps, tabs or tables inside, long-lived work, or something people link to | Full page (own route) |
| ≤ 4 controls tied to a trigger, nothing lost on dismiss (quick filter, color, date) | Popover |
| A list of actions | Dropdown menu |
| One non-essential sentence of explanation | Tooltip |
| Any of the above on a viewport below 640 px | Bottom sheet or full-screen page (UXP-R6) |

| ID | L | Requirement |
| --- | --- | --- |
| UXP-O1 | 1 | Container picked by the table; the same kind of task uses the same container across the app |
| UXP-O2 | 1 | Max overlay depth 1: no modal on modal, no drawer on drawer; the only allowed stack is a confirm dialog on top; a next step replaces the content or navigates |
| UXP-O3 | 1 | Every dialog and drawer: title naming the task, visible close button, Esc and scrim click close (dirty form → UXP-F8), focus trapped then returned to the trigger, page behind does not scroll (→ A11Y-02); overlay sizes → UXP-O7 |
| UXP-O7 | 2 | Overlay sizes: widths from a fixed set (dialog 400/560/720 px, drawer 400–640 px); height ≤ 90vh with the body scrolling and header + actions pinned |
| UXP-O4 | 2 | An overlay showing an entity (record drawer, detail dialog) has a URL: Back closes it, reload reopens it, the link can be shared |
| UXP-O5 | 2 | Tooltips: ≤ 1 sentence, non-essential, no interactive content, open after ~500 ms of hover and on keyboard focus (web/desktop; native touch: n/a, use visible text or a help affordance); popovers and menus flip to stay inside the viewport, one open at a time |
| UXP-O6 | 2 | No unsolicited overlay on load (what's new, survey, upsell) before the user completes a first action in the session; at most 1 per session (the ONB-05 first-visit tour is the only exception); feature announcements are a dot or dismissible callout next to the feature, gone forever once dismissed (→ SUP-03, ONB-05) |

## Navigation, URL as state, Back button (UXP-N)

| ID | L | Requirement |
| --- | --- | --- |
| UXP-N1 | 1 | Every view has its own URL — detail pages, tabs, wizard steps, settings sections; pasting it in a new tab shows the same view after auth |
| UXP-N2 | 1 | Back closes an overlay opened by navigation and returns to a list with the same filters and scroll position; it never loses form data and never loops on a redirect; a new page starts at the top; switching tab or filter does not jump the scroll |
| UXP-N3 | 1 | Login and session expiry return the user to the URL originally requested, not to the home page |
| UXP-N4 | 1 | After create → the new object (or the list with it highlighted); after edit → stay, with confirmation; after delete → UXP-D5 |
| UXP-N5 | 1 | Location always visible: active nav item + matching h1 (→ UXP-T3), breadcrumbs when depth ≥ 3 (→ `app-shell.md`); no dead ends — every screen, including error and success, offers a next action |
| UXP-N6 | 2 | Tabs only for 2–7 peer views of one object, labels of 1–2 words, each tab a URL, one tab row at most, never for sequential steps; external links open a new tab and carry an icon |

## Search and filters (UXP-S)

| ID | L | Requirement |
| --- | --- | --- |
| UXP-S1 | 1 | Any list or grid that can exceed 25 items has a search field (or visible filters when items are browsed visually): results as you type (debounce 250–300 ms) or on Enter when the backend takes over 1 s; in-field spinner and a clear "×" (global search → `app-shell.md`) |
| UXP-S2 | 1 | Where a list has filters, applied filters are always visible as removable chips with "Clear all", and the result count updates with them |
| UXP-S3 | 2 | Search matches the fields users see (name, email, code), ignoring case, accents and outer spaces, with partial matches; ≤ 4 most-used filters visible above the list, the rest behind "Filters"; desktop applies instantly, the mobile filter sheet has a "Show N results" button |
| UXP-S4 | 2 | Date-range filters offer presets (Today, Last 7 days, Last 30 days, This month, Custom) and display the resolved absolute range (→ I18N-02) |

## Copy and microcopy (UXP-C)

**Error formula:** what happened (in the user's words) + why (only if known and useful) + what to do next. "Error 422: validation failed" → "This email is already in use. Sign in or use another email." · "Something went wrong" → "We couldn't save the invoice — the connection dropped. Try again." · "Invalid input" → "Enter a date after 12 Mar 2026."

| Word | Use it only for |
| --- | --- |
| Create / New | Making an object that did not exist ("New invoice" on the trigger, "Create invoice" on the submit) |
| Add | Attaching an existing thing to a container (add a member to a project) |
| Remove | Detaching — the object still exists elsewhere |
| Delete | Destroying the object |
| Archive | Hiding, restorable |
| Save | Persisting edits to an existing object |
| Cancel | Abandoning changes |
| Close | Leaving when there is nothing to lose |

| ID | L | Requirement |
| --- | --- | --- |
| UXP-C1 | 1 | Voice: plain words, second person, active voice, present tense; one term per concept across the whole app, taken from the glossary (→ `domain.md`; proof: grep for banned synonyms → DOM-03, plus sampled screenshots); one language per locale — no mixed-language screens |
| UXP-C2 | 1 | Sentence case on every title, button, label and menu item; no final period on labels, buttons and headings; no "Oops", "Whoops", "Please note" or exclamation marks on errors |
| UXP-C3 | 1 | Errors follow the formula; never on screen: status codes, stack traces, exception text, "Something went wrong" alone, `[object Object]`, i18n keys; unexpected errors show a short reference id for support |
| UXP-C4 | 1 | No developer vocabulary on screen: `null`, `undefined`, `NaN`, "Invalid Date", enum constants (`PENDING_REVIEW`), column names, "entity", "payload", raw ISO timestamps; every enum has a human label; zero lorem ipsum, "TODO", "Test" or "John Doe" in production (proof: grep of UI source and enum label maps, plus sampled screenshots) |
| UXP-C5 | 1 | Verbs follow the verb table in this section (Create/Add/Remove/Delete/Archive/Save/Cancel/Close), extended by the app's glossary (→ `domain.md`): the same action has the same word on every screen (→ UXP-B2) |
| UXP-C6 | 2 | Dates: relative under 7 days ("5 min ago", "Yesterday 14:30"), absolute after ("12 Mar", year added when not the current one); exact timestamp with time zone on hover (→ I18N-02, UX-03); never an ambiguous all-numeric date |
| UXP-C7 | 2 | Numbers: thousands separators, currency with symbol and fixed decimals (→ UX-03), unit always present, percentages with ≤ 1 decimal, tiles abbreviate (12.4k) with the exact value on hover, real plurals ("1 item", "2 items" — never "item(s)") |
| UXP-C8 | 2 | Length budget: labels 1–3 words, buttons ≤ 3 words, headings ≤ 6 words, help text ≤ 1 sentence, dialog body ≤ 2 sentences; keyword first |

## Motion (UXP-M)

| What moves | Duration | Easing |
| --- | --- | --- |
| Hover, press, toggle, checkbox | 100–150 ms | ease-out |
| Tooltip, dropdown, popover, toast | 150–200 ms | ease-out in, ease-in out |
| Dialog, drawer, accordion, bottom sheet | 200–300 ms | ease-out in, ease-in out (exit ~25% faster) |
| Page or full-screen transition | 300–400 ms, never over 500 ms | ease-in-out |
| Spinner, progress, skeleton shimmer (1.5–2 s loop) | continuous | linear |

| ID | L | Requirement |
| --- | --- | --- |
| UXP-M1 | 2 | Durations and easings follow the table and exist as tokens in `DESIGN.md`; with `prefers-reduced-motion` (→ A11Y-06) slides and scales become ≤ 150 ms fades or cuts while progress indicators keep working |
| UXP-M2 | 2 | Only `transform` and `opacity` are animated (never width, height, top, left); animations are interruptible and never block input |
| UXP-M3 | 1 | Motion explains something — origin (drawer from its edge, popover from its trigger), a state change or feedback; none of: decorative loops, parallax, bounce/elastic, staggered fade-in of the page on every navigation (proof: grep animation definitions, plus a recorded pass over the core flows) |
| UXP-M4 | 2 | High-frequency and keyboard-driven actions (typing, row selection, command palette, tab switch) animate in ≤ 100 ms or not at all |

## Responsive and mobile (UXP-R)

| ID | L | Requirement |
| --- | --- | --- |
| UXP-R1 | 1 | One breakpoint set (e.g. 640 / 768 / 1024 / 1280), mobile-first; screens verified at 375, 768 and 1280 (native: smallest and largest supported phone and tablet sizes plus largest Dynamic Type/font scale) (→ DES-09, UX-01; proof: screenshot set or automated viewport/simulator check); no page-level horizontal scroll at any width from 320 px (→ A11Y-06) |
| UXP-R2 | 1 | Touch targets ≥ 44×44 px with ≥ 8 px between neighbours on touch layouts (the 24 px of A11Y-07 is the floor, not the target) |
| UXP-R3 | 1 | Nothing is hover-only (web/desktop; native touch: n/a by construction): row actions, tooltip content and menus are reachable by tap and by keyboard |
| UXP-R4 | 1 | Mobile web inputs have font-size ≥ 16 px (no iOS zoom on focus) and pinch-zoom is never disabled; full-height layouts use `100dvh` (native: n/a), respect safe-area insets, and neither the keyboard nor a fixed bar covers the focused field or the submit button |
| UXP-R5 | 2 | Thumb zone: below 640 px the screen's primary action sits in a sticky bottom bar or the lower half of the screen; destructive and rare actions stay at the top or in a menu (navigation → `app-shell.md`) |
| UXP-R6 | 2 | Overlays below 640 px: dialogs and drawers become bottom sheets (≤ 90% height, drag handle + close button) or full-screen pages; selects with more than 7 options become a sheet or the native picker |
| UXP-R7 | 2 | Mobile keeps every core task: secondary panels (filters, metadata, side columns) collapse behind a button instead of disappearing; swipe gestures always have a visible button equivalent and never override system back or pull-to-refresh |

## Perceived performance (UXP-P)

Budgets and techniques live in PERF-F1, PERF-F9 and PERF-F10; these items are what the user must *see*.

| ID | L | Requirement |
| --- | --- | --- |
| UXP-P1 | 1 | Navigation reacts in < 100 ms: the nav item becomes active and the route's skeleton renders at once; never more than 300 ms frozen on the old page without feedback (proof: trace timing or screen recording) |
| UXP-P2 | 1 | The shell (sidebar, header) stays mounted across navigation — no full-page flash or re-render; only the content area changes |
| UXP-P3 | 1 | No flash of wrong state on load: wrong theme, login page for a signed-in user, empty state before data arrives, unstyled or untranslated text, permission-gated UI that appears and then vanishes |
| UXP-P4 | 1 | No layout shift from late content: space reserved for images, async sections, banners and loading buttons (CLS → PERF-F1) |
| UXP-P5 | 2 | Revisits are instant: cached data shown immediately and then revalidated, Back renders without a loader (→ PERF-F9); typing never lags because of search or validation work (debounce the work, not the input) |

## Empty, zero and edge states (UXP-E)

| State | Must contain |
| --- | --- |
| First use (nothing created yet) | One sentence on what this is and why it matters + 1 primary CTA; optional import or sample data (→ ONB-04, ONB-06) |
| No results (search or filter) | The query echoed + "Clear filters" / "Clear search" button; never the first-use state |
| All done (inbox zero) | Positive confirmation; no CTA required |
| Load error | What failed + Retry + reference id; the rest of the page keeps working |
| Offline | Banner; cached content stays readable; unavailable actions say why |
| Permission denied (403) | What is restricted + who can grant it (role or admin name) + request access or go back (→ SEC-03) |
| Not found (404) | "Deleted or wrong link" + link to the parent list and home |
| Limit reached | Which limit and current usage ("5 of 5 projects") + upgrade or cleanup path (→ FIN-07) |
| Plan-gated feature | Visible with lock + the plan that unlocks it (→ BIL-01) |
| Still processing | "Processing — usually ~2 min" + auto-refresh; never a stale blank |
| Session expired | Re-auth that returns to the same screen with the work intact |

| ID | L | Requirement |
| --- | --- | --- |
| UXP-E1 | 1 | Every list, table, widget and detail view implements the applicable rows of the matrix, each with a story, a screenshot or an e2e snapshot (→ DES-09, ONB-04) |
| UXP-E2 | 1 | First use, no results and error are three different states with different copy and actions; an empty state renders only after the load has confirmed zero items |
| UXP-E3 | 1 | Failure is scoped: sections load independently, a slow or failed one shows its own skeleton or error with Retry and never blanks the page; an app-level error boundary shows "Reload" + reference id inside the shell (→ SHL-31, mark this part blocked by it) — never a white screen |
| UXP-E4 | 1 | 403 and 404 copy follows the matrix; rendering inside the shell → SHL-29, SHL-30; hidden vs disabled nav → SHL-33 |
| UXP-E5 | 1 | Data extremes verified on every list and detail: 0, 1 and 1000+ items; longest strings (→ UXP-T4); missing optional fields; missing avatar → initials; text 30% longer for translation (→ `i18n.md`) |
| UXP-E6 | 2 | Limits: usage visible before the wall ("4 of 5 projects", → BIL-10); at the limit the blocked action explains it and offers upgrade or cleanup; existing data stays accessible (→ FIN-07) |
| UXP-E7 | 2 | Connectivity: offline banner within 5 s of losing connection; every request has a client timeout (≤ 30 s) that ends in an error with Retry, never an endless spinner; session expiry re-authenticates and returns with the work intact (→ UXP-F8, UXP-N3) |

## Dashboards and data visualization (UXP-X)

| ID | L | Requirement |
| --- | --- | --- |
| UXP-X1 | 2 | Each widget answers a written question that someone acts on; ≤ 5 KPI tiles on the top row with the most important top-left; ≤ 9 widgets per dashboard; one date-range control for the whole page (→ UXP-S4) with time zone stated, state in the URL and "Updated 2 min ago" + refresh |
| UXP-X2 | 2 | KPI tile = label + value + period + delta against the previous period (arrow and %, colored by good/bad, not by up/down); clicking it opens the underlying list |
| UXP-X3 | 1 | Chart by data shape: trend over time → line or area; comparing categories → sorted bars; part of a whole with ≤ 5 parts → stacked bar or donut; never 3D, dual y-axes or a pie with more than 5 slices |
| UXP-X4 | 2 | Readability: bar axes start at 0; axis units labeled; ≤ 6 series (rest grouped as "Other") labeled directly or by legend; palette from tokens, colorblind-safe, themed for dark mode; hover/tap tooltip with exact values |
| UXP-X5 | 1 | Each widget has its own skeleton, "No data for this period" state (axes kept) and error with Retry (→ UXP-E3); a brand-new account sees onboarding (→ ONB-03), not a wall of zero charts |
| UXP-X6 | 3 | A metric has the same name, definition and number on every screen and export (definition → `domain.md`); every chart has a table or CSV alternative |

## Settings pages (UXP-A)

Pattern only — what the personal and organization settings contain is `account.md` and `organization.md`.

| ID | L | Requirement |
| --- | --- | --- |
| UXP-A1 | 1 | Settings split into named sections (≤ 7 per level): sub-nav on desktop, list → detail on mobile; each section has a URL; personal and organization settings are visibly separate groups (team accounts only) |
| UXP-A2 | 1 | Save model by control: independent toggles and selects autosave with inline "Saved"; text fields and related groups get a Save button per section card — never one Save for the whole page, never both models in one card (→ UXP-F7) |
| UXP-A3 | 1 | Each setting has a label and a one-line plain description of its effect and scope (team accounts only: "Applies to all members"); the current value is readable without opening anything; delayed effects are stated ("From the next billing cycle") |
| UXP-A4 | 1 | Danger zone: destructive settings sit in a last, separate, danger-bordered section, each with its consequence text, following the UXP-D table (→ LGL-04) |
| UXP-A5 | 2 | Settings locked by role or plan are shown read-only with the reason ("Only owners can change this", plan badge) instead of hidden (→ `organization.md`, BIL-01) |
| UXP-A6 | 2 | Secrets (API keys, tokens): full value shown once with a copy button, afterwards masked showing the last 4 characters; rotate and revoke go through a confirm (→ UXP-D table) |

## Help and discoverability (UXP-H)

| ID | L | Requirement |
| --- | --- | --- |
| UXP-H1 | 1 | Everything is discoverable on screen: no feature reachable only by shortcut, right-click, hover, long-press or gesture — each has a visible control |
| UXP-H2 | 1 | Convention over invention (Jakob's law): logo → home, standard icons, selects, date pickers and scrolling that behave natively; no scroll hijacking, custom cursor, or disabled text selection and right-click on content |
| UXP-H3 | 2 | Progressive disclosure: the default path of the core task shows ≤ 7 choices per screen; advanced options collapse under "Advanced" with defaults that work |
| UXP-H4 | 2 | Recognition over recall: recent items, autocomplete from existing values, visible format examples; IDs, URLs, keys and codes have a copy button with "Copied" feedback |
| UXP-H5 | 2 | Shortcuts are taught where they are used: hint in tooltips and menu items, `?` opens the full list (→ UX-07); non-obvious fields link "Learn more" to the exact article (→ ONB-07) |
| UXP-H6 | 2 | Help is ≤ 2 clicks from any screen, and a support request auto-attaches the page URL, user, org and last error reference id (→ SUP-02) |

## Anti-patterns (any one present = finding)

What makes an app look amateur or AI-generated, and the rule that removes it.

| Smell | Rule |
| --- | --- |
| Everything centered: titles, forms, tables in a narrow centered column | UXP-L2 |
| Inputs and buttons stretched to 1400 px; text lines of 180 characters | UXP-L3 |
| Big gradients, gradient text, glassmorphism, glow shadows in product UI; badges in 6 meaningless colors; colored left borders on cards | UXP-L6 |
| Mixed radii (sharp inputs, pill buttons, 16 px cards); card inside card inside card; border + shadow on everything | UXP-L5 |
| 5+ font sizes or 3+ weights on one screen; grids of identical cards where nothing is more important than anything else | UXP-T1, UXP-T2 |
| Emoji as icons; toolbar of mystery icons without labels | UXP-T5 |
| Near-duplicate grays, arbitrary pixel values, low-contrast "elegant" gray on gray | DES-02, DES-05, A11Y-04 |
| Placeholder used as label; asterisks everywhere; a 2-column form the eye zig-zags through | UXP-F1, UXP-F2, UXP-F3 |
| Errors shouted while still typing; errors only in a toast; form cleared after a failed submit | UXP-V1, UXP-V2, UXP-F8 |
| Two or more filled primary buttons side by side; "Submit" and "OK" buttons | UXP-B1, UXP-B2 |
| Disabled button with no reason; clickable `div` rows that do not open in a new tab | UXP-B5, UXP-B6 |
| "Are you sure?" Yes/No; a confirm on every action; red delete button next to Save | UXP-D2, UXP-D3, UXP-D4 |
| Full-page spinner on every navigation; skeleton that flashes for 80 ms; content blanking on every refetch | UXP-K1, UXP-K2, UXP-P1 |
| Success toast for everything; 5 toasts stacked; action that fails silently | UXP-K3, UXP-K4, UXP-K5 |
| Table with headers and nothing else; "No data" for first use, no results and errors alike; white screen on error | UXP-E2, UXP-E3 |
| Filters, tab or page lost on reload or Back; scroll back at the top after Back | UXP-G5, UXP-N2 |
| Modal on modal; a 20-field form inside a dialog; welcome modal + tour + survey on first load | UXP-O1, UXP-O2, UXP-O6 |
| "Error 500", "Request failed with status code 422", `[object Object]`, `undefined`, `PENDING_REVIEW`, `2026-03-12T14:30:00Z` on screen | UXP-C3, UXP-C4 |
| Title Case Mixed With sentence case; two languages on one screen; Delete and Remove used interchangeably | UXP-C1, UXP-C2, UXP-C5 |
| Fade-up on every card, bounce, parallax | UXP-M3 |
| Hover-only actions on a phone; 28 px tap targets; iOS zooming into every input; horizontal page scroll | UXP-R1 to UXP-R4 |
| Layout jumping as data arrives; flash of light theme before dark; flash of the login page | UXP-P3, UXP-P4 |
| Dashboard of zero-value charts on a new account; pie with 12 slices; green/red arrows that mean "up/down" | UXP-X2, UXP-X3, UXP-X5 |
| Custom scrollbars, scroll hijacking, features hidden behind right-click | UXP-H1, UXP-H2 |

## Screen review protocol (2 minutes per screen)

1. **Capture** (scripted, e.g. Playwright): the screen at 375, 768 and 1280 px in light and dark = 6 screenshots; plus 1 each of loading (throttled network), empty (new account), error (API request blocked) and extreme data (longest strings, 1000 rows).
2. **Answer** the 15 questions — yes/no, each "no" becomes a finding: `UXP-ID · screenshot · fix`.
3. **Gate:** any L1 "no" blocks the screen; L2 goes to the backlog.

| # | Question | Rules |
| --- | --- | --- |
| 1 | In 5 seconds, is it clear what this screen is for and what the main action is? | UXP-T2, UXP-L4 |
| 2 | Exactly one primary button, labeled verb + object, in the standard place? | UXP-B1 to UXP-B3 |
| 3 | ≤ 4 font sizes, ≤ 2 weights, 1 accent color, ≤ 3 radii? | UXP-T1, UXP-L5, UXP-L6 |
| 4 | One left edge, visible grouping, nothing centered or stretched without reason? | UXP-L1 to UXP-L3 |
| 5 | Do I know where I am, and does the URL reproduce exactly this view? | UXP-N1, UXP-N5, UXP-G5 |
| 6 | Every field has a visible label and the right control; errors appear at the field and say how to fix? | UXP-F2, UXP-F4, UXP-V1 to UXP-V3 |
| 7 | Click every button: reaction in < 100 ms, pending state, then a result that names the object? | UXP-B4, UXP-B7, UXP-K1, UXP-K5 |
| 8 | Loading, first-use, no-results and error states all exist and differ? | UXP-K2, UXP-E1 to UXP-E3 |
| 9 | Every destructive action is undoable or confirmed by a specific dialog? | UXP-D1 to UXP-D3 |
| 10 | Any word a non-developer would not understand, raw code, wrong casing or second language? | UXP-C1 to UXP-C5 |
| 11 | At 375 px: no horizontal scroll, targets ≥ 44 px, primary action reachable, nothing hover-only? | UXP-R1 to UXP-R6 |
| 12 | Dark theme: every surface, border, chart and image themed; no flash on load? | DES-03, UXP-P3 |
| 13 | Extreme data: does the layout hold with the longest values and 0 / 1 / 1000 items? | UXP-T4, UXP-E5 |
| 14 | Reload, Back, Forward: same filters, same scroll, no lost input? | UXP-N2, UXP-F8, UXP-G5 |
| 15 | Zero rows from the anti-patterns table? | Anti-patterns |

| Nielsen heuristic | Checked by |
| --- | --- |
| 1 Visibility of system status | UXP-K, UXP-P1, UXP-N5 |
| 2 Match between system and the real world | UXP-C1, UXP-C4, UXP-C6, UXP-C7 |
| 3 User control and freedom | UXP-D6, UXP-N2, UXP-O3, UXP-F8 |
| 4 Consistency and standards | UXP-B1 to UXP-B3, UXP-C5, UXP-L4, UXP-H2 |
| 5 Error prevention | UXP-V5, UXP-F4, UXP-F5, UXP-D1, UXP-D7 |
| 6 Recognition rather than recall | UXP-H4, UXP-F2, UXP-K6, UXP-S2 |
| 7 Flexibility and efficiency of use | UXP-F6, UXP-G7, UXP-G9, UXP-H5 |
| 8 Aesthetic and minimalist design | UXP-L, UXP-T, UXP-H3, Anti-patterns |
| 9 Help users recognize, diagnose and recover from errors | UXP-V2, UXP-V3, UXP-C3, UXP-E3 |
| 10 Help and documentation | UXP-H5, UXP-H6 (→ ONB-07, SUP-02) |

References: [NN/g — 10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) · [GOV.UK Design System](https://design-system.service.gov.uk/) · [Laws of UX](https://lawsofux.com/) · also grounded in Apple HIG (44 pt targets), Material 3 (motion, components), Refactoring UI (hierarchy, spacing, color) and NN/g response-time limits (0.1 s / 1 s / 10 s).
