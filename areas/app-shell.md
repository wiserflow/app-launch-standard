# App shell and navigation (SHL)

The authenticated frame every screen lives in: regions, sidebar, top bar, user menu, org switcher, banners, URL structure, shell-level error pages, mobile navigation, role-aware menu and the settings layout. NOT: general interaction patterns (forms, tables, feedback, copy → `ux-patterns.md`), personal settings content (→ `account.md`), org/member/role content (→ `organization.md`), design tokens (→ `design.md`).

Kickoff question: one person per account or team accounts. Rows marked "(team accounts only)" apply only to team accounts. "Sidebar" means the primary navigation: a top-bar nav is an equivalent shell and the same rows apply to it; mobile-drawer rows (SHL-45) are n/a when the product uses a top row or bottom bar instead of a drawer.

## Reference sitemap (standard B2B SaaS entries and where each lives)

| Entry | Location | Visible to | Notes |
| --- | --- | --- | --- |
| Home / Dashboard | Sidebar, top section | all | Default landing after login |
| Core product sections | Sidebar, main section | per role | 1 entry per primary noun (e.g. Projects, Customers) |
| Inbox / Notifications | Bell in top bar + optional sidebar entry | all | Unread count |
| Members / Team | Sidebar or Settings → Members | per permission | Content → ORG-* |
| Settings | Sidebar bottom | per role | Sub-nav below |
| Settings → Organization | `/:org/settings/organization` | admin+ | Name, logo, slug, default locale/time zone |
| Settings → Members | `/:org/settings/members` | admin+ | Invites, roles |
| Settings → Roles & permissions | `/:org/settings/roles` | admin+ | If custom roles exist |
| Settings → Billing & plan | `/:org/settings/billing` | owner/billing role | Plan, invoices, payment method |
| Settings → Usage | `/:org/settings/usage` | admin+ | Quotas vs limits |
| Settings → Integrations | `/:org/settings/integrations` | admin+ | Connect/disconnect third parties |
| Settings → API keys | `/:org/settings/api-keys` | admin+ | Only if public API exists |
| Settings → Webhooks | `/:org/settings/webhooks` | admin+ | Only if outbound webhooks exist |
| Settings → Audit log | `/:org/settings/audit-log` | owner/admin | → ADM-02 |
| Settings → Security | `/:org/settings/security` | owner/admin | 2FA enforcement, SSO, session policy |
| Settings → Danger zone | `/:org/settings/danger` (last item) | owner | Transfer, delete org |
| Help / docs | Top bar `?` menu and sidebar footer | all | → SUP-02 |
| What's new / changelog | `?` menu | all | → SUP-03 |
| Send feedback | `?` menu | all | Opens form without leaving the page |
| Status | `?` menu or sidebar footer | all | Link to status page |
| User menu | Avatar (sidebar bottom or top bar right) | all | Personal, not org-level |

## Checklist

| ID | L | Requirement |
| --- | --- | --- |
| SHL-01 | 1 | A single shell component wraps every authenticated route (→ DES-07); regions: sidebar (or bottom nav on mobile), top bar, content, optional right panel; auth pages and public pages never render it |
| SHL-02 | 1 | Content region uses the width caps of UXP-L3, the page header anatomy of UXP-L4 and the page padding of UXP-L7 on every page type; Proof: a screenshot per page type at 375/768/1280 (UXP-L3 = width caps, UXP-L4 = header anatomy, UXP-L7 = page padding) |
| SHL-03 | 1 | Only the content region scrolls; sidebar and top bar stay fixed; scroll position resets on route change and is restored on browser back |
| SHL-04 | 1 | Sidebar (or primary nav) items are icon + text label (icon-only only in collapsed state, with a tooltip showing the label); one consistent icon set and size |
| SHL-05 | 1 | Active item is visibly highlighted (not color alone) and exposes `aria-current="page"`; parent section stays highlighted on nested routes (e.g. `/projects/42` highlights Projects) |
| SHL-06 | 1 | Sidebar groups items into at most 3-4 labeled sections (single-product apps with few entries may use one); max navigation depth is 2 levels in the sidebar (deeper hierarchy lives in the page via tabs or breadcrumbs); primary items ≤ ~8 before overflow into a "More" group |
| SHL-07 | 1 | Primary nav order is fixed and documented: Home, core product sections, then Inbox (if notifications exist), then Settings and Help pinned to the bottom; the same order for every role (items are removed, never reordered) |
| SHL-08 | 2 | Sidebar collapses to an icon rail (toggle button and shortcut, e.g. `[`); state persisted per user (local storage or user preference) and applied before first paint, no flash of the wrong state |
| SHL-09 | 2 | Sidebar sections that can expand remember open/closed state; the section of the active route is auto-opened |
| SHL-10 | 2 | Badge counts on sidebar items (unread, pending approvals) use a cap ("99+"), update without reload, expose a text alternative to screen readers, and disappear at zero |
| SHL-11 | 1 | Whole shell is keyboard operable: skip-to-content link first, logical tab order (sidebar, top bar, content), visible focus ring, menus open with Enter/Space and close with Esc returning focus to the trigger; no focus trap outside modals (→ A11Y-01..06) |
| SHL-12 | 2 | Navigation shortcuts (e.g. `g` then `h` for Home) and a shortcuts cheat sheet opened by `?`; shortcuts disabled while typing in inputs → UX-07 |
| SHL-13 | 1 | Top bar contains: breadcrumbs or page title (left), help menu, plus each of these only when the feature exists: global search trigger (→ SHL-15), notifications bell (→ SHL-17), plan badge (→ SHL-35); mobile top bar shows only back/title and the present items among search and bell |
| SHL-14 | 2 | Breadcrumbs reflect hierarchy (not history), every crumb except the last is a link, entity names are real names not IDs, long names truncate with a title tooltip; collapsed to the parent link on mobile |
| SHL-15 | 1 | (Only if the product has global search; else n/a) Global search trigger is visible (field or icon with `⌘K`/`Ctrl K` hint) and opens a palette: searches entities and navigation entries, groups results by type, shows recent items on empty query, results respect the user's permissions (→ SEC-03), full keyboard navigation, no-results state with a suggestion |
| SHL-16 | 2 | Command palette also runs actions (create X, switch org, toggle theme, go to a settings page) and displays each action's shortcut → UX-07 |
| SHL-17 | 1 | (Only if the product has in-app notifications; else n/a) Notifications bell shows unread count, opens a panel with the latest items (read/unread state, relative time with absolute time on hover, deep link per item), "mark all read" and links to the full list and to notification preferences → SUP-04, PLT-08 |
| SHL-18 | 1 | Help menu (`?`) contains: documentation, keyboard shortcuts, contact support, what's new, send feedback, status page; each opens in a new tab or an in-page panel without losing the current screen |
| SHL-19 | 2 | "What's new" shows an unread dot until opened and links to the changelog entry → SUP-03 |
| SHL-20 | 2 | Feedback entry opens a short form (type, message, optional screenshot) that attaches current URL, app version and user/org IDs automatically; confirmation shown without navigation |
| SHL-21 | 1 | User menu (avatar + name/email) lists: profile, personal settings, theme (light/dark/system → DES-03), language (→ I18N-08), keyboard shortcuts, help, log out, plus switch organization (team accounts only, if member of several); log out is last and visually separated; content of these pages → `account.md` |
| SHL-22 | 1 | Log out ends the session server-side (→ AUTH-05), clears client caches of user (and tenant) data and lands on the login page; cross-tab logout → SHL-55 |
| SHL-23 | 1 | (Team accounts only) Org/workspace switcher at the top of the sidebar shows current org logo and name; lists all orgs the user belongs to (searchable above ~7), marks the current one, has "Create organization" at the bottom → ORG-* |
| SHL-24 | 1 | (Team accounts only) Last used org is remembered per user and used on next login; with a single org the switcher still shows the name and offers only "Create organization"; switching org keeps the user on the equivalent section when it exists, otherwise Home |
| SHL-25 | 1 | (Team accounts only) Switching org fully resets tenant-scoped client state (caches, realtime subscriptions; warns on unsaved drafts); no data from the previous org is visible after the switch (→ ARC-03, API-05) |
| SHL-26 | 1 | (Team accounts only) URLs are tenant-scoped and human-readable: `/:org-slug/<section>/<id>`; slug is unique, old slug 301-redirects to the new one on rename, reserved words blocked (`settings`, `api`, `admin`, `login`, `app`, ...) |
| SHL-27 | 1 | Every screen state is deep-linkable → UXP-N1, UXP-G5; the login redirect preserves the full path → UXP-N3 |
| SHL-28 | 1 | `/` for a logged-in user redirects to their Home (team accounts only: the last used org's Home); (team accounts only) a link to an org the user is not in shows the 403 shell page with "switch organization" and "request access" actions, not a blank page |
| SHL-29 | 1 | 404 rendered inside the shell (nav and top bar intact; "shell" = the authenticated frame of SHL-01; public/guest pages use the same layout minus authenticated nav): explains the resource does not exist or was deleted, offers Home and search; no stack traces, no framework default page |
| SHL-30 | 1 | 403 rendered inside the shell: states what is missing ("you need the Admin role"), names who can grant it (org owners) with a request-access action (team accounts only; single-user apps: show 404 for another user's resource); never reveals to non-members whether a hidden resource exists |
| SHL-31 | 1 | 500/crash rendered inside the shell via a route-level error boundary: friendly message, retry button, support reference ID (matches the log, → OBS-*), "Report problem" link; one crashed widget does not take down the whole shell |
| SHL-32 | 1 | Each shell error page has a distinct `<title>` and the correct HTTP status for server-rendered routes; one test per status (404, 403, 500); Proof: automated test per status |
| SHL-33 | 1 | Role-aware menu rule (single-user apps: apply the state-gated half only): an entry the user can never access (role lacks the capability) is **hidden**; an entry reachable after an upgrade or a state change (plan limit, unverified email, missing setup) is **shown disabled with an explanation and a CTA**; a hidden entry's URL still returns 403 (→ SEC-03) |
| SHL-34 | 1 | Menu visibility is derived from one permission/entitlement source shared with server authz (→ BIL-01), not role checks duplicated per component; a test renders the menu per role (team accounts only) or per account state and snapshots the entries |
| SHL-35 | 1 | Plan badge in the shell shows the current plan; during a trial it shows days left (e.g. "Trial: 9 days left") linking to billing; clickable for owner/billing roles, plain text for others |
| SHL-36 | 1 | Upgrade entry: persistent but unobtrusive (sidebar footer or plan badge) on non-top plans; plan-gated features show a lock + "Upgrade" CTA that opens plan comparison, never a dead click; hidden on the top plan; roles that cannot change billing see "Ask an owner" |
| SHL-37 | 2 | Usage near a limit (≥ 80%, e.g. seats, storage) is surfaced in the shell as a non-blocking indicator linking to Usage → BIL-10, FIN-07 |
| SHL-38 | 1 | Trial-expired and payment-failed states show a persistent banner with the single required action (add payment method) and a clear statement of what is restricted; read-only mode stays navigable and data stays exportable (→ LGL-03) |
| SHL-39 | 1 | Impersonation banner: full-width, high-contrast, cannot be dismissed, shows impersonated user/org and an "Exit" button; shell visibly different (e.g. colored frame); every action is audit-logged with the staff actor → ADM-04, CON-12; a read-only impersonation that blocks writes still logs the session start/end and every read of personal data |
| SHL-40 | 1 | Environment indicator on every non-production environment (staging, preview): label, distinct favicon and top-bar color (all three); absent in production; Proof: a test per environment |
| SHL-41 | 2 | Maintenance/incident banner driven by a remote flag or the status page (no deploy needed): maintenance notice with start/end in the user's time zone (→ I18N-02), incident notice linking to the status page; dismissible per banner ID except during an active outage |
| SHL-42 | 1 | Offline banner appears within 5 s of network loss (→ UXP-E7), states changes may not be saved, disables or queues write actions, auto-dismisses with "Back online"; a form being edited loses no data |
| SHL-43 | 1 | Banner stacking is defined (applies once 2+ banner types exist): max 2 visible at once, priority order (impersonation, outage/maintenance, billing, offline, environment); banners push content down, never overlay the top bar or cover navigation |
| SHL-44 | 1 | Mobile < 768 px: sidebar becomes a bottom tab bar (3-5 primary destinations + "More") or a hamburger drawer; primary actions sit in the bottom half (thumb reach), touch targets ≥ 44 px, safe-area insets respected (notch, home indicator) |
| SHL-45 | 1 | (n/a if SHL-44 uses a bottom bar only, → SHL-44) Mobile drawer/sheet: opens by button (and optionally edge swipe), closes on route change, scrim tap and Esc, traps focus while open, locks background scroll; the bottom bar never overlaps content or the on-screen keyboard |
| SHL-46 | 2 | Tablet (768-1024 px) defaults to the collapsed icon rail; resizing across breakpoints preserves route, scroll and open dialogs |
| SHL-47 | 1 | Settings uses one layout (pattern → UXP-A1): left sub-nav grouped Personal / Organization (team accounts only) / Developer (only if API keys or webhooks exist) (entries per the sitemap), content on the right |
| SHL-48 | 1 | Settings page structure: page title, then sections as cards each with heading + description + controls (→ UXP-A2, UXP-A3); destructive actions isolated in the Danger zone at the bottom (→ UXP-A4) |
| SHL-49 | 1 | Settings save rule is identical on every settings page: save model → UXP-A2, saving/saved/failed states → UXP-K5, unsaved-changes guard → UXP-F8 |
| SHL-50 | 1 | Danger zone items show consequences first and require re-authentication + typing a confirmation name; single-user apps: delete/cancel account (→ ACC-*); team accounts only: transfer ownership, delete org, leave org with the org name typed (rules → ORG-06, ORG-08), visible to owner only (members leave from account settings → ORG-25) |
| SHL-51 | 1 | Personal settings (profile, security, sessions, notification prefs) are separated from organization settings (team accounts only) in the sub-nav and the URL (`/account/...` vs `/:org/settings/...`), so they survive org switching → ACC-* |
| SHL-52 | 1 | A new user with no data gets a working shell: all nav entries reachable, empty states with CTA (→ ONB-04), onboarding checklist entry in the sidebar until completed or dismissed → ONB-03 |
| SHL-53 | 3 | Light personalization of the sidebar where relevant (pinned/favorite items, recents section), persisted per user |
| SHL-54 | 2 | Route-change feedback and shell persistence → UXP-P1, UXP-P2 |
| SHL-55 | 2 | Multi-tab consistency: org switch, logout and theme change propagate to other open tabs of the same browser |
| SHL-56 | 3 | Enterprise: org-level branding in the shell (logo, accent color), custom domain per org (`app.customer.com`), SSO-only login enforced → AUTH-11 |
| SHL-57 | 3 | Second-level switcher (e.g. project or environment inside an org) in the sidebar with the same remember-last rule as SHL-24 |
| SHL-58 | 2 | Shell e2e tests cover: nav per role snapshot, collapse persistence, org switch, 403/404/500 in shell, mobile drawer, banner priority; one screenshot per breakpoint stored as evidence |

References: `design.md` (DES-07), `ux-patterns.md`, `organization.md`
