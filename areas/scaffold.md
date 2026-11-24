# Scaffold and starter kit (SCF)

Goal: day 1 of a new app starts from a working monorepo with the reference stack and the house layers already in place — not from an empty folder, and not by copying files by hand from the last app. "House" means your organization's reference stack and starter, if any; with none, the ADR (SCF-02, SCF-11) records the chosen stack and the kit is built per app. The stack below is an **example reference stack** (TypeScript web SaaS); any stack works — pick per target (→ `platforms.md`) and record it (SCF-02, SCF-11).

Two layers:

1. **Generated base** — example: [Better-T-Stack](https://github.com/AmanVarshney01/create-better-t-stack) (`create-better-t-stack`, ~5.9k stars, active): type-safe monorepo with chosen frontend, backend, API, ORM, auth, addons. Minimal on purpose; no billing/email/admin.
2. **House kit** — everything the base lacks and every app needs (this standard's L1 items that are code). Lives in **one** maintained starter repo and in a private shadcn registry, never re-copied from a previous product.

## Base command (example reference stack)

```bash
# validate first, then run without --dry-run
bun create better-t-stack@latest <app> \
  --frontend tanstack-router --backend hono --runtime bun --api orpc \
  --database postgres --orm drizzle --auth better-auth --db-setup docker \
  --addons turborepo biome lefthook pwa starlight \
  --examples none --package-manager bun --git --install --dry-run
```

Change flags per app (`--frontend tanstack-start`, `native-uniwind` for Expo, `fumadocs` instead of `starlight`). Visual builder: better-t-stack.dev. Agent plugin (MCP + skills that plan a valid stack; Claude Code example): see `TOOLING.md`.

## House kit (layered on top of the base)

| Layer | Contents | Covers |
| --- | --- | --- |
| `apps/site` | Astro: landing, pricing, legal pages, 404, sitemap, robots, OG template | WEB, BRD-07 |
| `apps/console` | Owner console skeleton (see `owner-console.md`) | CON |
| `apps/worker` | Queue worker + scheduler + lifecycle rule engine | PLT-03..05, EML |
| `packages/email` | Provider adapters (real + log driver), layout, suppression, unsubscribe, categories, send log | EML-01..08 |
| `packages/billing` | Plans/entitlements module, checkout, idempotent webhook, portal, dunning | BIL-01..07 |
| `packages/observability` | Error tracker, structured logger with redaction, OTel, metrics, health, heartbeat | OBS-01..07 |
| `packages/flags`, `packages/audit`, `packages/notifications` | Feature flags, audit log, in-app + push notifications | ADM-02, ADM-05, SUP-04 |
| `packages/privacy` | Data export, deletion with grace period, anonymization, retention jobs | LGL-03, LGL-04, LGL-06 |
| `packages/shell` (app-shell + account + organization UI) | Shell regions, sidebar, user menu, org switcher, settings layout, account pages, members/roles/invitations screens | SHL, ACC, ORG (L1) |
| `packages/ui` / registry | Theme (`@theme` tokens) + components + blocks from the private shadcn registry | DES-02, DES-06, DES-16 |
| Root files | `DESIGN.md`, `PRODUCT.md`, `CLAUDE.md` (rule block + area index), `docs/launch/` (this standard), `docs/PENDING.md`, `.env.example` | DES-10, PRD-01, ENG-04 |
| Dev env | `scripts/dev.sh` (`bun run up` / `bun run down`), per-app Redis, Docker Compose | — |
| CI/CD | PR workflow, staging/prod deploy (base: `templates/github-actions/`), backup + restore-check scripts, Renovate, actionlint/zizmor | CI, DB-03 |
| Tests | Playwright setup with auth fixture, tenant-isolation test, axe check, visual baseline helper | TST-04, A11Y-01, DES-12 |

## Checklist

| ID | L | Requirement |
| --- | --- | --- |
| SCF-01 | 1 | New app created from the starter (base + house kit) in ≤ 1 hour, including `bun run up` working locally |
| SCF-02 | 1 | Generator flags recorded in the repo's decisions folder (default `docs/decisions/`; ADR "stack") so the base can be regenerated/compared later |
| SCF-03 | 1 | Starter has zero product-specific code, names or secrets; app name/domain set by one init script |
| SCF-04 | 1 | `.env.example` complete (every env var the code reads is listed, with no real values); init script creates DB, Redis container, ports block, and copies the standard to `docs/launch/` |
| SCF-05 | 1 | Starter CI green on a fresh clone (lint, types, tests, build, e2e smoke) |
| SCF-06 | 2 | Improvements made in a product that are generic are **upstreamed** to the starter (PR to starter repo), not left in the product |
| SCF-07 | 2 | Starter dependencies kept current (Renovate) and re-validated against a fresh Better-T-Stack output each quarter |
| SCF-08 | 2 | UI shared via the private shadcn registry; apps pull updates with `shadcn add @house/<item>` instead of copying |
| SCF-09 | 3 | Starter versioned with a changelog; each product records which starter version it started from |

## Brownfield adoption (app already running)

The generated base is **not** run over an existing repo — it overwrites structure. The standard (checklists) applies in full; the house kit is adopted piece by piece.

In `scripts/status.py`, mark SCF-01, SCF-03, SCF-05 `n/a` (replaced) in brownfield and audit SCF-10..13 instead.

| Greenfield item | In brownfield |
| --- | --- |
| SCF-01, SCF-03, SCF-05 | n/a — replaced by SCF-10..13 |
| SCF-02 | becomes SCF-11 (stack diff ADR) |
| SCF-04 | partial: `.env.example` complete, `docs/launch/` copied; DB/Redis already exist |
| SCF-06..09 | apply; SCF-09 records which kit packages (and versions) were adopted |

Order of attack follows **risk, not phase**: safety net (SCF-13) → L1 gaps that can lose data or money (SEC, DB, BIL, LGL) → the rest by phase.

How much of the kit fits depends on the stack: same stack as the kit (e.g. Hono + Drizzle + Better Auth + Bun) → packages drop in; different stack → the checklist still applies, items are implemented in the app's own idiom.

| ID | L | Requirement |
| --- | --- | --- |
| SCF-10 | 1 | Gap audit: every item of each applicable area marked in `docs/launch/STATUS.md` (`scripts/init.py`, `scripts/status.py`) as `ok (evidence)` / `missing` / `diverges (ADR link)`; `missing` L1 items become tasks citing their IDs |
| SCF-11 | 1 | Stack diff vs the reference stack (if none: the chosen stack and why) recorded in the repo's decisions folder (default `docs/decisions/`; ADR): what stays, what converges, what never will and why |
| SCF-12 | 1 | Kit adopted one package per PR, behind a flag where it changes runtime behavior, with a rollback path; the affected journey has a smoke/e2e test **before** the swap; schema changes are additive first (expand → migrate → contract) |
| SCF-13 | 1 | Safety net before any kit adoption: OBS-01 error tracking, OBS-03 health checks, DB-03 backup with restore tested, SEC-07 secrets out of the repo, CI-06 rollback command. Proof: `ok` only when all five are `ok` (→ OBS-01, OBS-03, DB-03, SEC-07, CI-06); otherwise `missing`, naming the open sub-items |

References: [Better-T-Stack docs](https://better-t-stack.dev) · [shadcn registry](https://ui.shadcn.com/docs/registry) · comparable full starters to borrow patterns from: open-saas, ixartz SaaS-Boilerplate, BoxyHQ saas-starter-kit (see `REFERENCES.md`).
