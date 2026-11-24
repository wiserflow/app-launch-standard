# Target platforms (PLAT)

Goal: decide **where the product ships** (every surface, not just web) and what each surface adds or changes. NOT the web shell (→ `app-shell.md`), store/PWA/push basics (→ `mobile.md`, MOB-*), or the API contract itself (→ `api.md`).

**Rule: requirements are universal, stack is chosen per target.** Auth, tenancy, authz, audit, privacy, billing and observability apply on every surface; only the implementation changes. The target list and the stack per target are recorded in an ADR (→ SCF-11, ARC-*). Platform-specific items (PLAT-xx-nn) apply **only to targets the ADR lists as in scope**; an unlisted target is out of scope, not forgotten.

Think wider than the seed list: ask "where does the user already spend their day?" (chat, inbox, spreadsheet, IDE, terminal, AI assistant, marketplace) before defaulting to "build another web page".

## Surfaces catalog

| Group | Targets |
| --- | --- |
| Web | web app, PWA, marketing site, embeddable widget / iframe / JS SDK, customer portal on custom domain |
| Mobile | native iOS (Swift/SwiftUI), native Android (Kotlin/Compose), cross-platform (Expo/React Native, Flutter), home-screen widgets, share-sheet/App Clips/Instant Apps |
| Desktop | Tauri, Electron, native macOS/Windows/Linux, menu-bar/tray utility, OS share/context-menu integration |
| Developer | CLI, TUI, public REST/GraphQL API + SDKs, webhooks-only/headless, Terraform/GitHub Action/CI plugin, IDE/editor extension |
| In-context | browser extension, chat bots (Slack, Teams, Discord, WhatsApp, Telegram), email as interface (inbound parsing, reply-to-act), SMS/USSD, spreadsheet/office add-ins (Google Workspace, Microsoft 365), Figma/Notion/Linear-style plugins |
| AI | MCP server, agent tool/skill, GPT-style / assistant app, llms.txt + machine-readable docs |
| Marketplaces | Shopify, Zapier/Make/n8n, HubSpot/Salesforce, Atlassian, Slack/Teams app directories, WordPress plugin |
| Devices | smartwatch, TV, car (CarPlay/Android Auto), voice assistants, kiosk/POS, IoT/hardware companion, offline-first field app, AR/VR |

## Applicability matrix

C = applies but changes (see notes), Y = as-is, - = not applicable. SHL = app shell, ACC = account, ORG = organization.

| Target | SHL (shell/nav) | ACC (profile/settings) | ORG (tenant/roles) | Auth flow | A11Y | i18n | Distribution / update | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Web app | Y | Y | Y | session cookie | Y | Y | deploy | baseline |
| PWA | C | Y | Y | cookie | Y | Y | deploy + SW update | MOB-06; SW cache = version skew |
| Native iOS/Android | C (tabs, not sidebar) | C (OS settings link) | Y | PKCE + system browser, passkeys | OS screen readers | Y | store review | MOB-*; PLAT-IOS/AND |
| Desktop app | C (menu bar, tray) | C | Y | PKCE + loopback/deep link | OS a11y APIs | Y | signed installer, auto-update | PLAT-DSK |
| CLI | - | C (`whoami`, `config`) | C (`--org`) | device code | C (no color-only, `NO_COLOR`) | C | package managers | PLAT-CLI; telemetry opt-in, `--help`/man |
| TUI | C (keyboard-first panes) | C | C | device code | C (screen-reader fallback) | C | package managers | PLAT-CLI |
| Browser extension | - (popup/side panel) | C | C | PKCE via `identity` API / web handoff | Y | Y | store review, auto-update | PLAT-EXT; minimal permissions |
| IDE extension | - | C | C | device code / editor auth | Y (editor themes) | C | marketplace | PLAT-EXT |
| Chat bot | - (messages, modals) | C (link to web) | Y (workspace = tenant) | OAuth install + user linking | C (alt text, no emoji-only) | Y | directory review | PLAT-BOT |
| MCP / agent tool | - | - | Y (token scoped to org) | OAuth 2.1 / scoped API key | - | - | registry listing | PLAT-MCP; AI-04 for destructive tools |
| Public API / SDK | - | C (key mgmt page) | Y | API key / OAuth client credentials | - | - | semver, package registries | PLAT-API; → api.md |
| Embeddable widget | - | - | Y (public key + origin) | signed token from host | Y (host page focus) | Y | CDN versioned snippet | PLAT-EMB |
| Email as interface | - | C (EML-05) | Y | signed per-user address/token | Y (plain-text, dark mode) | Y | n/a | PLAT-EML |
| Office add-in | - (task pane) | C | Y | SSO of host suite + link | Y | Y | marketplace review | PLAT-ADD |
| Marketplace app | - | C | Y (shop/portal = tenant) | host OAuth install | C | Y | marketplace review | PLAT-MKT; billing may be host-owned |
| Watch/TV/car/voice | - | - | C | pairing code / link to phone | C (strict platform rules) | Y | store review | PLAT-DEV |
| Kiosk/POS/IoT | - | - | C (device = tenant resource) | device credential + pairing | C | C | fleet update | PLAT-DEV |
| Webhooks-only/headless | - | - | Y | signed requests | - | - | contract versioning | API-07 |

## Universal items (every in-scope target)

| ID | L | Requirement |
| --- | --- | --- |
| PLAT-01 | 1 | Target list in a `docs/decisions/` ADR: each target marked in scope / later / never with one-line reason, owner, and the stack chosen per target (→ SCF-11); a new target requires an ADR update before work starts |
| PLAT-02 | 1 | Every target consumes the **same** API/contract and the same authz (→ SEC-03, API-05); no target keeps its own copy of business rules (→ DOM-*); a test calls a protected route from each client type and gets 403 cross-tenant |
| PLAT-03 | 1 | Auth flow fits the surface and is documented per target: browser = cookie (→ AUTH-05); native/desktop = OAuth + PKCE via system browser (never embedded webview, never a client secret in the binary); CLI/TV/IoT = device code; bot/marketplace = OAuth install + user linking; headless = scoped key. Org-enforced 2FA (→ AUTH-07) is honored on every flow |
| PLAT-04 | 1 | Tokens stored in the platform secure store (Keychain, Keystore, OS credential manager), not plain files/localStorage; revocable per device and listed in active sessions (→ AUTH-09); logout and password change revoke them (→ AUTH-05) |
| PLAT-05 | 1 | Distribution channel and **signing** defined per target (store, notarized/signed installer, signed packages with checksums, marketplace listing); signing keys live in CI secrets/HSM with a documented rotation and loss procedure |
| PLAT-06 | 1 | Version skew policy: each client sends its version (header/User-Agent); the API supports N-1 minimum; a deprecated or unsafe client gets a clear "update required" response, tested; stale web assets (service worker, CDN) cannot break against a new API |
| PLAT-07 | 1 | Auto-update or update notice per target (store, Sparkle/Tauri updater, package manager, CLI version nag) with signed update artifacts and a rollback path |
| PLAT-08 | 1 | Crash/error reporting on every client with release + platform + version tags and symbols/source maps uploaded in CI (→ OBS-01, MOB-08); opt-out respected for local/dev-tool targets (→ PLAT-CLI-04) |
| PLAT-09 | 1 | Account deletion and data removal reachable from the surface or clearly linked from it (→ MOB-02, LGL-03, LGL-04); uninstall instructions exist and revoke (or offer to revoke) local tokens, caches and webhooks |
| PLAT-10 | 1 | Permission prompts (camera, notifications, location, clipboard, host permissions, OAuth scopes) requested in context after an explanation, minimal, and the denied state has a working fallback (→ MOB-04) |
| PLAT-11 | 2 | Deep links/URL schemes/protocol handlers from emails, shares and notifications open the right target and fall back to web when the app is absent; params validated as untrusted input (→ MOB-05, SEC-06) |
| PLAT-12 | 2 | Offline/flaky-network behavior declared per target (online-only / read-cache / offline-first with sync); queued writes idempotent (→ API-04), conflict resolution defined, sync state visible to the user |
| PLAT-13 | 2 | Accessibility checked with the platform's own tooling (VoiceOver/TalkBack, Narrator/NVDA, Accessibility Inspector, terminal screen reader) and recorded per target (→ `accessibility.md`) |
| PLAT-14 | 2 | Store/marketplace review readiness per target: reviewer test account (→ MOB-03), data-use disclosures matching real collection, listing assets, and a named owner for rejection responses |
| PLAT-15 | 2 | Feature parity table per target (what each surface can and cannot do) linked from the help center (→ SUP-02); features missing on a target deep-link to web instead of dead-ending |
| PLAT-16 | 2 | Analytics events carry `platform` and `client_version`; funnels and retention can be split by target (→ `analytics.md`) |
| PLAT-17 | 2 | Plan limits and entitlements enforced server-side for every target (→ FIN-07, BIL-01); purchases made in a store/marketplace reconcile with the billing source of truth, IAP rules honored where required |
| PLAT-18 | 3 | Support window per target documented (supported OS/browser/runtime versions, end-of-support notice lead time) |
| PLAT-19 | 3 | Design tokens shared across targets (→ DES-*); where the platform has native conventions (HIG, Material, OS dialogs) conventions beat brand, and the exceptions are listed |

## Native iOS/Android (extends MOB-*)

| ID | L | Requirement |
| --- | --- | --- |
| PLAT-IOS-01 | 1 | Privacy manifest and required-reason API declarations match the SDKs in use; Sign in with Apple offered whenever other third-party social login is (→ AUTH-06) |
| PLAT-IOS-02 | 2 | Native affordances used where users expect them: share extension, widgets, Shortcuts/App Intents, Live Activities, Spotlight; each in scope or listed "never" in the ADR |
| PLAT-IOS-03 | 2 | Dynamic Type at largest size, dark mode and Reduce Motion verified with screenshots on smallest and largest supported devices |
| PLAT-AND-01 | 1 | Target SDK meets the current Play requirement; runtime permissions, foreground-service types and exact-alarm use justified in the Play form |
| PLAT-AND-02 | 2 | Predictive back, edge-to-edge, 200% font scale and TalkBack verified; no UI breakage on foldables/tablets if listed as supported |
| PLAT-AND-03 | 2 | Background work (WorkManager) survives OS limits (Doze, low power); verified on one aggressive-OEM device if a feature depends on it |

## Desktop (Tauri, Electron, native)

| ID | L | Requirement |
| --- | --- | --- |
| PLAT-DSK-01 | 1 | macOS build signed + notarized, Windows build code-signed; installs on a clean machine without Gatekeeper/SmartScreen bypass |
| PLAT-DSK-02 | 1 | Electron: `contextIsolation` on, `nodeIntegration` off, strict CSP, IPC channels allowlisted and validated, remote content never gets Node; Tauri: command allowlist and capability scopes minimal |
| PLAT-DSK-03 | 1 | Auto-updater verifies signatures, supports staged rollout and rollback; update-server outage does not block the app |
| PLAT-DSK-04 | 2 | Native integration: menu bar, OS-convention shortcuts, window state restore, tray/dock behavior, system dark mode, deep-link protocol handler |
| PLAT-DSK-05 | 2 | Local data location, size and encryption documented; sign-out can wipe it; multiple windows and a second running instance behave correctly |
| PLAT-DSK-06 | 3 | Enterprise install: MSI/pkg with silent flags, MDM-friendly config, proxy and custom-CA support |

## CLI and TUI

| ID | L | Requirement |
| --- | --- | --- |
| PLAT-CLI-01 | 1 | `--help` on every command with examples, `--version`, man page or `help` topic; exit codes documented; errors say what failed and what to do next |
| PLAT-CLI-02 | 1 | Login via device code or browser handoff (no password flag, no secret in shell history); token in OS credential store; `logout` revokes server-side; `whoami` shows user + org |
| PLAT-CLI-03 | 1 | Scriptable: stable `--json` output, quiet mode, no interactive prompt when stdin is not a TTY (`--yes`/env for CI), non-interactive auth via scoped token, honors `NO_COLOR` and pipes |
| PLAT-CLI-04 | 1 | Telemetry is opt-in or clearly disclosed with a documented off switch (`DO_NOT_TRACK`/env); never sends file contents, secret-bearing args or paths without consent |
| PLAT-CLI-05 | 2 | Install paths: package manager (brew/winget/apt/npm/pip) and checksummed single binary; `update` command or version nag; deprecation warnings appear before breaking changes |
| PLAT-CLI-06 | 2 | Destructive commands require confirmation or `--force` and offer `--dry-run` (→ AI-04 when an agent drives the CLI) |
| PLAT-CLI-07 | 2 | Shell completions (bash/zsh/fish/PowerShell), config precedence documented (flag > env > file), works behind a proxy |
| PLAT-CLI-08 | 3 | TUI: full keyboard navigation with visible key hints, resize handling, graceful degradation without color/unicode, terminal restored cleanly on crash |

## Browser and IDE extensions

| ID | L | Requirement |
| --- | --- | --- |
| PLAT-EXT-01 | 1 | Minimal permissions (optional/host permissions requested at use, no `<all_urls>` without justification), written justification per permission for store review |
| PLAT-EXT-02 | 1 | No remote code execution; content scripts treat page DOM as untrusted; tokens never exposed to page context; MV3 service-worker suspend/restart tested |
| PLAT-EXT-03 | 2 | Single-purpose store listing; privacy policy and data-use disclosure match behavior; supported browsers (Chrome, Firefox, Edge, Safari) stated in the ADR |
| PLAT-EXT-04 | 2 | The API tolerates the previous extension version for ≥ 30 days after a new one is published (store review and rollout lag), tested against the API |
| PLAT-EXT-05 | 2 | IDE extension: lazy activation, never blocks editor startup, works in remote/WSL/dev-container sessions, respects workspace trust, secrets in editor secret storage |

## Chat bots (Slack, Teams, Discord, WhatsApp, Telegram)

| ID | L | Requirement |
| --- | --- | --- |
| PLAT-BOT-01 | 1 | Install maps a workspace/guild/number to exactly one org and each chat user to a product user (link flow); unlinked users get a link prompt, never another tenant's data (→ API-05) |
| PLAT-BOT-02 | 1 | Incoming events verified (signing secret/signature), deduplicated by event id, acknowledged within the platform deadline and processed async; replays are harmless |
| PLAT-BOT-03 | 1 | Minimal OAuth scopes with justification; uninstall/token-revoked events disable the integration and delete or schedule deletion of stored tokens/data |
| PLAT-BOT-04 | 2 | Messaging policy respected: WhatsApp templates + 24h window with opt-in/opt-out, Slack/Teams rate limits with backoff, no unsolicited DMs; opt-out command works |
| PLAT-BOT-05 | 2 | Native components (buttons, modals, slash commands) with a text-only fallback; destructive actions confirm (→ AI-04); long output links to the web app |
| PLAT-BOT-06 | 3 | Directory listing (Slack App Directory, Teams store) review passed, with support URL and privacy policy |

## MCP servers and AI-agent integration

| ID | L | Requirement |
| --- | --- | --- |
| PLAT-MCP-01 | 1 | Auth via OAuth 2.1 (or scoped keys) bound to user + org; tools can never exceed the caller's role (→ SEC-03, API-05); tokens revocable in the account UI (→ AUTH-09) |
| PLAT-MCP-02 | 1 | Small set of task-oriented tools with precise descriptions, typed input schemas, bounded/paginated output; destructive or costly tools flagged and confirmed (→ AI-04) |
| PLAT-MCP-03 | 1 | Tool output and fetched content treated as untrusted (prompt injection): a test covers a poisoned record; agent-initiated actions are rate-limited and audit-logged (→ ADM-02) |
| PLAT-MCP-04 | 2 | Transport per use: remote streamable HTTP when hosted, stdio when local; health and per-tool metrics (→ OBS-06) |
| PLAT-MCP-05 | 3 | Discoverability: `llms.txt`/machine-readable docs, registry listing, example prompts; tool suite evaluated on at least one real agent client |

## Public API and SDKs

| ID | L | Requirement |
| --- | --- | --- |
| PLAT-API-01 | 2 | SDKs generated from OpenAPI (→ API-08) for the languages the ADR lists; semver, changelog, typed errors, retries with idempotency (→ API-04), published from CI |
| PLAT-API-02 | 2 | Quickstart reaches a first successful call in under 10 minutes, with copy-paste examples per SDK language and a test-mode key |
| PLAT-API-03 | 3 | Deprecating a client/SDK version is announced by email and response header ahead of removal (→ API-09, PLAT-06) |

## Embeddable widgets and iframes

| ID | L | Requirement |
| --- | --- | --- |
| PLAT-EMB-01 | 1 | Public key bound to allowed origins; server-signed tokens for identified users; `frame-ancestors`/CSP and `postMessage` origin checks tested |
| PLAT-EMB-02 | 2 | Isolated from the host page (Shadow DOM or iframe), versioned CDN snippet, size budget (→ `performance.md`), works with third-party cookies blocked (tested in Safari/Firefox) |
| PLAT-EMB-03 | 2 | Widget errors never throw into the host; loads async; kill switch via flag (→ ADM-05) |

## Email-as-interface, add-ins, marketplaces, devices

| ID | L | Requirement |
| --- | --- | --- |
| PLAT-EML-01 | 2 | Inbound email parsing: per-user/per-object signed address, SPF/DKIM checked, attachment size/type limits and virus scan, quoted reply stripped, sender matched to a user before acting |
| PLAT-ADD-01 | 2 | Office/Workspace add-in: SSO with the host suite or account link, task pane works in web and desktop clients, manifest scopes reviewed, nothing cached outside the user's tenant |
| PLAT-MKT-01 | 2 | Marketplace app: install/uninstall webhooks handled (including mandatory data-erasure hooks where the marketplace requires them), review checklist done, billing path (host-billed vs own) decided in the ADR |
| PLAT-MKT-02 | 2 | Zapier/Make/n8n: triggers via webhooks (not only polling), actions idempotent, sample payloads provided, errors human-readable |
| PLAT-DEV-01 | 3 | Watch/TV/car/voice: platform-mandated safety and brevity rules (no typing while driving, 10-foot UI, voice intents confirm before acting) checked; heavy flows hand off to phone/web |
| PLAT-DEV-02 | 3 | Kiosk/POS/IoT: revocable device credential per unit (never shared), pairing flow, signed OTA updates with rollback, remote lock/wipe, defined behavior when offline for days |

References: [OAuth 2.0 for Native Apps (RFC 8252)](https://datatracker.ietf.org/doc/html/rfc8252) · [Device Authorization Grant (RFC 8628)](https://datatracker.ietf.org/doc/html/rfc8628) · [Command Line Interface Guidelines](https://clig.dev)
