# Account and personal settings (ACC)

The signed-in person's own account: profile, credentials, security, preferences, notifications, privacy. It is NOT sign-in flows (`auth.md`), organization/member management (`organization.md`), the shell's user menu (`app-shell.md`) or generic form/feedback patterns (`ux-patterns.md`). Personal settings are per user across all orgs; org settings live elsewhere.

## Settings sections (exact order)

One route per section (`/account/<slug>`, outside the org prefix → SHL-51), deep-linkable, left sub-nav on desktop, list-then-detail on mobile (375 px).

| # | Section | Slug | Contains |
| --- | --- | --- | --- |
| 1 | Profile | `profile` | Avatar, display name, handle, job title, visibility of fields |
| 2 | Preferences | `preferences` | Theme, language, time zone, formats, start page, density, motion |
| 3 | Notifications | `notifications` | Event × channel matrix, digest frequency, quiet hours |
| 4 | Security | `security` | Email, password, passkeys, 2FA, connected accounts |
| 5 | Sessions and devices | `sessions` | Active sessions, revoke (→ AUTH-09) |
| 6 | Security log | `activity` | Account security events |
| 7 | API tokens | `tokens` | Personal access tokens |
| 8 | Organizations | `organizations` | Memberships, pending invites, leave |
| 9 | Privacy and data | `privacy` | Export, delete account |

## Which changes need what

| Change | Re-auth (sudo) | Email confirmation | Notify old email | Revoke other sessions |
| --- | --- | --- | --- | --- |
| Name, avatar, handle, preferences, notifications | No | No | No | No |
| Email change | Yes | Yes, link to new address | Yes, with revert link | Yes |
| Password change | Yes (current password) | No | Yes | Yes (→ AUTH-05) |
| Add/remove passkey, enable/disable 2FA, regenerate recovery codes | Yes | No | Yes | No |
| Link/unlink connected account | Yes | No | Yes | No |
| Create/revoke API token | Yes | No | Create only | No |
| Data export request | Yes | Link to download | No | No |
| Delete account | Yes | Yes, confirm link | Yes | Yes |

| ID | L | Requirement |
| --- | --- | --- |
| ACC-01 | 1 | Settings sections exist in the order and slugs of the table above; each is a deep link that survives reload and respects the user's org permissions (a missing section is hidden, not a 403 page) |
| ACC-02 | 1 | Settings reachable in ≤ 2 clicks from the user menu (→ SHL-21); same layout at 375/768/1280 px with no horizontal scroll (→ DES-09) |
| ACC-03 | 1 | Save model per field group → UXP-A2; unsaved text changes guarded → UXP-F8 |
| ACC-04 | 1 | Avatar: upload JPG/PNG/WebP up to 5 MB, in-browser square crop with zoom, server re-encodes to ≤ 512 px and strips EXIF; remove action; initials on a color derived from the user id as fallback (never a broken image or blank circle) |
| ACC-05 | 1 | Avatar upload validated by content sniffing, not only extension; rejected files show the reason and allowed formats; test with an SVG-with-script and a 50 MB file |
| ACC-06 | 1 | Display name required (1-80 chars, Unicode allowed, trimmed); changes reflect in the shell, mentions and audit log entries without re-login |
| ACC-07 | 2 | Optional unique handle/username if the product uses mentions or public URLs: rules shown inline, live availability check, reserved-word list, case-insensitive uniqueness, old handle held before release |
| ACC-08 | 2 | Optional job title and short bio (length counter); each profile field has a visibility control (private / org members / public) defaulting to private; a "View as others see it" preview |
| ACC-09 | 1 | Email change: sudo re-auth, verification link sent to the NEW address, change applies only after click; old address stays active until then |
| ACC-10 | 1 | After an email change, the OLD address gets a notice with a time-limited "This wasn't me" revert link that restores the old email and revokes all sessions (→ EML-05 for category rules; security mail is never opt-out) |
| ACC-11 | 1 | Email change to an address already in use does not leak account existence beyond what signup already reveals (→ AUTH-01); pending change is visible in settings with resend and cancel |
| ACC-12 | 1 | Password change requires the current password, shows a strength meter (e.g. zxcvbn) plus breached-password check, has a show/hide toggle; rules are shown before typing, not after failure |
| ACC-13 | 1 | Successful password change revokes all other sessions and tokens, keeps the current one, says so in the confirmation, and sends a notification email (→ AUTH-05) |
| ACC-14 | 1 | Users who signed up via social/magic link and have no password see "Set a password" instead of "Change password"; no section shows a field the account cannot use |
| ACC-15 | 2 | Passkeys: list with name, created, last used; add (name prompt), rename, remove; removal blocked if it is the last login method (→ AUTH-10) |
| ACC-16 | 2 | 2FA management UI: status, enable via QR + manual secret + code confirmation, disable (sudo), regenerate recovery codes (old ones invalidated, shown once with copy/download/print); backed by AUTH-07 |
| ACC-17 | 2 | Remaining recovery-code count shown, warning banner when ≤ 2 remain; org-enforced 2FA shows "Required by <org>" and the Disable action is disabled with that reason instead of failing on click |
| ACC-18 | 2 | Sessions and devices UI backed by AUTH-09: device/browser, approximate location, last active, "this device" badge, per-row revoke, "Sign out all other devices" with confirm |
| ACC-19 | 2 | Connected accounts (Google, etc.): linked state, email used, link and unlink; unlink is blocked with an explanation when it is the last login method (→ AUTH-06) |
| ACC-20 | 2 | Linking a provider whose email matches a different existing account is refused with a clear path (sign in there first), never silently merged |
| ACC-21 | 2 | Personal API tokens: name, scopes (least privilege, none preselected), expiry required (30/90/365 days or custom, no "never" by default), shown ONCE with copy button (→ UXP-A6), stored hashed; list shows prefix, last used, expiry |
| ACC-22 | 2 | Token revoke is immediate and tested (request with a revoked token returns 401 within seconds); a token loses access to an org when the user leaves it (→ API-05) |
| ACC-23 | 1 | Theme preference: light / dark / system (default system), applied before first paint with no flash, persisted per user across devices (→ DES-03) |
| ACC-24 | 1 | Language preference with native language names, default from browser, persisted on the user and applied to UI and emails (→ I18N-08) |
| ACC-25 | 1 | Time zone auto-detected from the browser at first login, shown as editable "Detected: X" with manual override searchable by city; all timestamps render in it (→ I18N-02) |
| ACC-26 | 2 | Date, time (12/24 h), number and first-day-of-week formats default from locale, overridable, with a live preview using the current date |
| ACC-27 | 2 | Start page preference (dashboard, last visited, or a module) honored on login; falls back safely if the chosen page is no longer permitted |
| ACC-28 | 2 | Density (comfortable / compact) applies to tables and lists app-wide; reduced motion defaults to the OS setting, can be forced on, and disables non-essential animation (→ `accessibility.md`) |
| ACC-29 | 1 | Notification matrix: rows = event types grouped by category, columns = in-app / email / push / each messaging channel the product uses (→ MSG-*); a channel not yet set up shows "Connect" instead of a dead toggle (→ PLT-08, EML-05) |
| ACC-30 | 1 | Security and billing notifications are locked on (lock icon with reason) and cannot be muted; all others default to a documented sensible set, not "everything on" |
| ACC-31 | 2 | Digest frequency per channel (instant / hourly / daily / weekly / off) with delivery hour in the user's time zone; optional quiet hours; "Send a test notification" button |
| ACC-32 | 2 | Notification settings can be overridden per organization with a "Same as default" state; email unsubscribe links land on this matrix pre-filtered, with no login needed for marketing categories |
| ACC-33 | 1 | Security log visible to the user: sign-ins, failed attempts, password/email/2FA/passkey/token changes, session revokes, each with time, device, IP/approx location; ≥ 90 days; not deletable by the user (org-side log is ADM-02) |
| ACC-34 | 2 | Sensitive or new-device log entries link to "Not you? Secure account", which revokes all sessions and forces a password reset (→ AUTH-04) |
| ACC-35 | 1 | Sudo mode: sensitive actions (table above) require re-auth if the last authentication is older than 10 minutes; method offered matches the account (password, passkey, 2FA code, social re-login); the action resumes after success |
| ACC-36 | 1 | Re-auth attempts are rate limited and logged; sudo state is server-side per session, never in local storage, and expires |
| ACC-37 | 1 | Data export request in Privacy section: contents and format listed, status (queued/ready/expired), download link emailed, expires in ≤ 7 days (→ LGL-03) |
| ACC-38 | 1 | Delete account: states what is deleted vs retained (e.g. invoices), the grace period length and how to cancel; requires sudo and typing the account email (→ LGL-04, MOB-02) |
| ACC-39 | 1 | Delete is blocked, with a list and action links, while the user is sole owner of any org: transfer ownership or delete the org first (→ ORG-06, ORG-07) |
| ACC-40 | 1 | During the grace period login shows "Scheduled for deletion on <date>" with a Restore action; other sessions are revoked; emails sent at start and 3 days before purge |
| ACC-41 | 2 | Organizations section lists memberships with role and a Leave action; leaving is blocked for the last owner and confirms the effect on the user's data in that org (→ ORG-07, ORG-23, ORG-25) |
| ACC-42 | 1 | Pending invites show in the Organizations section AND right after login (banner or modal with Accept / Decline), including invites addressed to the user's verified email sent before they signed up (accept flow → ORG-17, email → EML-T5) |
| ACC-43 | 1 | User in zero organizations is a designed state: no broken shell or redirect loop; shows pending invites, "Create organization", and fully working account settings (→ ONB-04) |
| ACC-44 | 2 | Many orgs: the Organizations section list is searchable above 7 entries (same threshold as the switcher, SHL-23); last-org memory and stale org URLs → SHL-24, SHL-28 |
| ACC-45 | 1 | Account mutations use only the authenticated user id (never one from the client); test proves user A cannot read or edit user B's profile, tokens, sessions or export (→ SEC-03, API-05) |
| ACC-46 | 2 | Destructive controls in settings (remove passkey, revoke all sessions, delete account) follow the UXP-D table and UXP-D2 dialog ("Remove passkey", not "OK") |
| ACC-47 | 2 | Each section has loading, error and saved states at 375/768/1280 px, with one screenshot or e2e per section attached to the release (→ DES-09, UX-02) |
| ACC-48 | 3 | Identity-provider-managed fields (email, name under SSO/SCIM) are read-only with "Managed by <org>" and the reason (→ AUTH-11) |
| ACC-49 | 3 | Lost-all-factors recovery: documented support-assisted flow with identity checks, a cooling-off delay and notifications (→ CON-12 for tooling) |

References: `auth.md`, `privacy-legal.md`, `organization.md`
