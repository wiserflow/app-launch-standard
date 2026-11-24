---
name: app-launch-standard
description: Project-agnostic standard (42 areas, ~800 checklist items with stable IDs and L1/L2/L3 levels) for building, launching and improving a production-grade app or SaaS - app shell and navigation, profile/account, organizations/members/roles, concrete UX/UI patterns, email, billing, auth, security, privacy, performance, observability, CI/CD, platforms (web, mobile, desktop, CLI, extensions, bots, MCP). Use when starting a new app (greenfield), auditing or upgrading an app already in production (brownfield), planning a launch, improving a screen or feature with a lightweight spec, or reviewing UX/UI quality.
---

# App Launch Standard

Project-agnostic standard for building and launching an app or SaaS that looks and behaves like a mature company product. 42 areas, 769 items (465 launch blockers) plus 48 target-specific PLAT items that apply only to targets in scope, each with a stable ID. Audience: agents and devs starting the next app. Tools are suggestions; the requirement is the item.

| File | Content |
| --- | --- |
| `SKILL.md` (this) | How to use, global map, launch runbook, operating cadence |
| `areas/*.md` | One checklist per area — read only the areas in play |
| `TOOLING.md` | Skills and MCP servers per area and per phase, install commands, security caveats |
| `REFERENCES.md` | Reference repositories (boilerplates, checklists, OSS tools) |

## How to use

1. **Kickoff — pick the track** (`areas/scaffold.md`):
   - **Greenfield** (new app): create the repo from the starter, then copy this folder to `<repo>/docs/launch/`.
   - **Brownfield** (app already running): never regenerate the base over it. Copy this folder to `<repo>/docs/launch/` and follow *Brownfield adoption* in `areas/scaffold.md` (gap audit → safety net → kit one package at a time).

   Then go through the global map and mark each area `applies` / `n/a (reason)` in `docs/launch/STATUS.md` — n/a areas are not deleted, so the decision is visible.
2. **Per phase:** before starting a phase, the agent reads only that phase's area files and installs that phase's tools from `TOOLING.md` (ask the user first; project scope).
3. **IDs everywhere:** plans, PRs, commits and `docs/PENDING.md` cite item IDs (`EML-03`, `PERF-B4`). Items needing a human (account, lawyer, pricing decision) go to `docs/PENDING.md → ## Needs user`.
4. **Evidence:** mark `[x]` only with evidence next to it (test name, screenshot path, URL, command output). "Deployed" is not evidence; "exercised in staging as a user" is.
5. **Reuse:** before building an item, check whether a previous app already solved it and copy that implementation.
6. **Changing an existing app** (improve a screen, add a feature): follow `areas/spec-flow.md` — a short spec + slices, acceptance by item IDs; no full launch pass.

Levels: **L1** launch blocker · **L2** within 30 days of launch · **L3** when scale or an enterprise customer requires it.

## Global map

Phases are an order of attack, not a waterfall: L1 items of every applicable area must be done before launch.

| Phase | Area | Prefix | File | Applies when | Items (L1) |
| --- | --- | --- | --- | --- | --- |
| 0. Discover | Product and requirements | PRD | `areas/product.md` | always | 9 (6) |
| 0. Discover | Architecture and decisions | ARC | `areas/architecture.md` | always | 8 (5) |
| 0. Discover | Scaffold and starter kit | SCF | `areas/scaffold.md` | always — first action (greenfield or brownfield track) | 13 (9) |
| 0. Discover | Brand, logo, positioning | BRD | `areas/brand.md` | always | 9 (7) |
| 0. Discover | Spec flow for changes and improvements | SPEC | `areas/spec-flow.md` | changing or improving an existing app | 8 (5) |
| 0. Discover | Domain and business rules | DOM | `areas/domain.md` | always | 30 (23) |
| 0. Discover | Target platforms | PLAT | `areas/platforms.md` | always — decide every surface | 19 (10) + 48 (18) per in-scope target |
| 1. Design | Design system and prototyping | DES | `areas/design.md` | always | 16 (10) |
| 1. Design | Marketing site and SEO | WEB | `areas/marketing-site.md` | public product | 13 (7) |
| 1. Design | UX polish | UX | `areas/ux-polish.md` | always | 8 (5) |
| 1. Design | UX and UI patterns | UXP | `areas/ux-patterns.md` | always (any UI) | 125 (84) |
| 1. Design | App shell and navigation | SHL | `areas/app-shell.md` | authenticated web app | 58 (41) |
| 2. Build | Identity and accounts | AUTH | `areas/auth.md` | always | 11 (5) |
| 2. Build | Account and personal settings | ACC | `areas/account.md` | always (signed-in users) | 49 (27) |
| 2. Build | Tenancy and customer-side admin | ADM | `areas/admin.md` | always | 7 (3) |
| 2. Build | Organizations, members and roles | ORG | `areas/organization.md` | multi-user / multi-tenant | 47 (31) |
| 2. Build | Owner console / backoffice | CON | `areas/owner-console.md` | always | 30 (15) |
| 2. Build | Billing | BIL | `areas/billing.md` | paid product | 12 (8) |
| 2. Build | Email infra and lifecycle | EML | `areas/email.md` | always | 32 (18) |
| 2. Build | Onboarding and activation | ONB | `areas/onboarding.md` | always | 7 (4) |
| 2. Build | API design | API | `areas/api.md` | always (internal API too) | 10 (7) |
| 2. Build | Platform blocks: uploads, jobs, cron, realtime, search, flags | PLT | `areas/platform.md` | per block used | 10 (6) |
| 2. Build | AI / LLM features | AI | `areas/ai.md` | product calls an LLM | 11 (7) |
| 2. Build | Messaging: WhatsApp, SMS | MSG | `areas/messaging.md` | sends/receives messages | 10 (6) |
| 2. Build | Mobile, PWA, push | MOB | `areas/mobile.md` | native app or PWA | 10 (6) |
| 2. Build | i18n / l10n | I18N | `areas/i18n.md` | always (I18N-01..06) | 10 (6) |
| 2. Build | Accessibility | A11Y | `areas/accessibility.md` | always | 10 (6) |
| 3. Harden | Performance | PERF | `areas/performance.md` | always | 26 (15) |
| 3. Harden | Security | SEC | `areas/security.md` | always | 12 (9) |
| 3. Harden | Privacy and legal | LGL | `areas/privacy-legal.md` | always | 10 (6) |
| 3. Harden | Testing and reliability | TST, REL | `areas/testing.md` | always | 15 (10) |
| 3. Harden | Database | DB | `areas/database.md` | always | 12 (7) |
| 3. Harden | Infrastructure | INF | `areas/infra.md` | self-hosted | 13 (8) |
| 3. Harden | CI/CD | CI | `areas/cicd.md` | always | 15 (8) |
| 4. Launch | Observability, alerting, status | OBS, OPS | `areas/observability.md` | always | 17 (9) |
| 4. Launch | Product analytics and metrics | ANL | `areas/analytics.md` | always | 6 (2) |
| 4. Launch | Support and communication | SUP | `areas/support.md` | always | 13 (5) |
| 4. Launch | Developer / API docs | DOC | `areas/dev-docs.md` | public API, SDK or webhooks | 9 (4) |
| 5. Operate | Cost and unit economics | FIN | `areas/cost.md` | always | 9 (4) |
| 5. Operate | Data, BI, reporting | DATA | `areas/data.md` | always (L1 = 3 items) | 9 (3) |
| 5. Operate | Sales, customer success, growth | CRM, GRW | `areas/sales-growth.md` | B2B or sales-led | 12 (4) |
| 5. Operate | Engineering process | ENG | `areas/engineering.md` | always | 9 (4) |

### Cross-area threads (same concern, several files)

| Thread | Items |
| --- | --- |
| Tenant isolation | SEC-02, DB-05, API-05, TST-04, DATA-06, ARC-03, ORG-* |
| Personal data / privacy law | LGL-*, ARC-05, AI-01, AI-10, DATA-09, MSG-03, MOB-02, ACC-* |
| Idempotency and retries | API-04, API-07, BIL-03, PLT-03, MSG-02, PERF-B6 |
| Cost caps | FIN-01..03, AI-02, MSG-07, BIL-10 |
| One source of truth for look and feel | DES-01..07, BRD-03..07, EML-06, WEB-*, UXP-* |
| Backups and recovery | DB-03, DB-10, REL-06, CI-06, OPS-04 |
| Secrets | INF-07, SEC-07, CI-04, MSG-05, AI-06 |
| Staff power over customer data | CON-01..06, CON-12, SEC-08, ADM-02, ORG-* |
| User-facing frame | SHL-*, ACC-*, ORG-*, UXP-*, UX-*, A11Y-* |
| Business rules and change flow | DOM-*, SPEC-*, PRD-*, ARC-* |
| Reuse across apps | SCF-*, DES-16, ENG-04 |

## Launch runbook

**T-14 days**

- [ ] All L1 items checked with evidence
- [ ] DES gates green: `design.md lint`, Tailwind lint, `impeccable detect`, visual baselines, axe
- [ ] Legal texts published after lawyer review
- [ ] DMARC at `quarantine`; EML-09 inbox test done
- [ ] PERF-B8 load test and SEC-10 scan done on staging
- [ ] INF-03 external port scan clean; DB-03 restore test passed; CI-06 rollback rehearsed

**T-1 day**

- [ ] Billing in live mode: real purchase + refund
- [ ] Production error reaches error tracker with correct release
- [ ] Alerts reach phone (OPS-03)
- [ ] Status page up
- [ ] New features behind flags where risky

**Launch day**

- [ ] End-to-end signup in incognito, phone and desktop
- [ ] Watch errors, 5xx, queue depth, Web Vitals and funnel for 2 h
- [ ] Announce: waitlist email, social, communities

**T+7 / T+30**

- [ ] Review activation funnel; tune EML-O1..O3
- [ ] Read every ticket/feedback; top 3 become tasks
- [ ] First NPS (T+30)
- [ ] Launch retrospective in `docs/decisions/`

## Operating cadence after launch

| Cadence | Activity |
| --- | --- |
| Daily | New errors, open alerts, support queue |
| Weekly | Signups, activation, MRR, churn; slow queries; changelog |
| Monthly | Email metrics (open/click/unsubscribe/complaint), NPS, infra cost, dependency updates, Web Vitals trend |
| Quarterly | Restore test, access review (who has admin), privacy review, secret rotation |
| Twice a year | DR rehearsal, terms review, pentest if enterprise customers |

---
