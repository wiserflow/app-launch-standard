# Skills and MCP servers by case

Verified 2026-11-23 (repo active, install command from vendor docs unless marked *composed*). Install commands using `claude mcp add` and `/plugin` are **Claude Code examples**; other agents install the same servers and skills with their own equivalents. "House stack" means your organization's reference stack, if any. Rules:

- **Project scope by default** (`npx skills add …` without `-g`; `claude mcp add --scope project` → `.mcp.json`). Global only for read-only generic tools (Context7). Ask the user before installing.
- **Every MCP costs context every session** → install only what the current phase uses; remove after.
- **Least privilege**: sandbox/test keys, read-only modes, scoped URLs. Never point a DB MCP at the production primary with write access.
- **OAuth on a headless server** needs a browser → SSH tunnel for the callback, or the API-key/header variant with `${ENV_VAR}` in `.mcp.json` (never commit the key).
- **Plugins (`/plugin install`) bypass `skills-lock.json`** and may install user-wide → prefer the `npx skills add` form when both exist.
- Registries: skills.sh install counts are **not** a trust signal (spam entries exist); on registry.modelcontextprotocol.io trust only vendor namespaces (`com.stripe/*`, `com.posthog/*`).

## Install by project phase (quick view)

| Phase | Areas | Install for the phase | Remove after? |
| --- | --- | --- | --- |
| 0. Discover | SCF, PRD, ARC, BRD | Better-T-Stack plugin (example), `to-spec`, `grill-me`, ADR + C4 skills | C4 once diagrams exist |
| 1. Design | DES, BRD, WEB | impeccable, shadcn skill + MCP, frontend-design, Excalidraw, Playwright CLI | Excalidraw, frontend-design |
| 2. Build | AUTH, BIL, EML, ONB, API, PLT, AI, MOB, I18N, ADM, MSG | Context7, Better Auth, oRPC, Standard Webhooks, Postgres skill + DBHub (dev, read-only), Storybook MCP, Stripe/Resend skills, Langfuse/evals, Expo, i18n lib skill | — |
| 3. Harden | PERF, SEC, LGL, TST, A11Y, DB, INF, CI | qa-skills, accessibility, Trail of Bits, Semgrep, privacy-law skill, Cloudflare/Docker, CI hardening, Chrome DevTools MCP | Most audit tools |
| 4. Launch | WEB, OBS, ANL, SUP, DOC | Front-End Checklist, web-design-guidelines, marketingskills, Sentry MCP, PostHog MCP | Audit tools |
| 5. Operate & grow | FIN, DATA, CRM, GRW, ENG | Metabase/ClickHouse MCP, CRM skills/MCP, Grafana MCP | — |

## Scaffold and owner console (SCF / CON)

| Item | Install | Use |
| --- | --- | --- |
| Better-T-Stack plugin (MCP + skills + commands; Claude Code plugin) | `/plugin marketplace add AmanVarshney01/create-better-t-stack` → `/plugin install better-t-stack@better-t-stack` | Agent plans a valid stack and generates it; `/better-t-stack:new <description>`. Plugin → bypasses `skills-lock.json`; remove after scaffolding |
| Better-T-Stack CLI | `bun create better-t-stack@latest <app> … --dry-run` | Generated base (flags in `areas/scaffold.md`) |
| Better Auth admin plugin | part of `better-auth` | Ban, impersonation, session control for the console (CON-11, CON-12) |
| Admin frameworks (optional) | Refine, react-admin, Appsmith | Only if not building `apps/console` on your reference stack |

## Base (most projects)

| Case | Item | Install | Note |
| --- | --- | --- | --- |
| Library docs | Context7 | `claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "Authorization: Bearer $CONTEXT7_KEY"` | Global OK; read-only |
| Browser verification | Playwright CLI + skills | `npm i -g @playwright/cli@latest && playwright-cli install --skills` | Cheaper in tokens than the MCP; MCP alt: `claude mcp add playwright npx @playwright/mcp@latest` |
| Perf/network/console debugging | Chrome DevTools MCP | `claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest --no-usage-statistics --headless --isolated` | `--no-usage-statistics` (telemetry on by default); `--isolated` avoids real-profile cookies |
| Security review | Trail of Bits skills | `/plugin marketplace add trailofbits/skills` | `differential-review`, `insecure-defaults`, `supply-chain-risk-auditor`; plus your agent's built-in security review (Claude Code: `/security-review`) |
| SAST | Semgrep MCP | `claude mcp add semgrep -- semgrep mcp` *(composed; needs Semgrep CLI)* | Old `semgrep/mcp` repo is archived — do not use |
| Auth | Better Auth skills | `npx skills add better-auth/skills` | best-practices, organization, twoFactor, security |

## Design, brand, front end (DES / BRD / PERF-F)

| Item | Install | Use |
| --- | --- | --- |
| impeccable | `npx impeccable install` | **Primary design guard**: `init` → `PRODUCT.md`, `document` → `DESIGN.md`, `shape` (UX before code), `critique`/`audit`/`polish`, `extract`; edit-time hook; `npx impeccable detect src/` as CI gate |
| shadcn skill | `npx skills add shadcn/ui` | Forces existing components first, semantic colors, registry authoring |
| shadcn MCP | `npx shadcn@latest mcp init --client claude` | Search/install from public and private registries |
| Storybook MCP | `npx storybook add @storybook/addon-mcp` → `npx mcp-add --type http --url "http://localhost:6006/mcp" --scope project` | Agent reads real component API/stories before writing UI (preview feature) |
| DESIGN.md linter | `npx @google/design.md lint DESIGN.md` | Broken token refs + WCAG contrast; `diff` for regressions |
| frontend-design (Anthropic) | `npx skills add anthropics/skills --skill frontend-design` | Visual direction for site/first look; does not enforce consistency |
| web-design-guidelines (Vercel) | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` | Per-screen review with `file:line` findings |
| ui-ux-pro-max | `npm i -g ui-ux-pro-max-cli && uipro init --ai claude` | Palette/type/design-system proposals; overlaps impeccable — pick one as primary |
| Excalidraw skill | `npx -y mcp-excalidraw-server install-skill --dir .claude/skills` | Lo-fi wireframes as committed `.excalidraw` + PNG render |
| Front-End Checklist skill | `npx skills add thedaviddias/front-end-checklist` | Launch audit rules (perf, SEO, a11y) |
| Front-End Checklist MCP | remote `https://mcp.frontendchecklist.io` | `audit_url`, `review_code`, `search_rules` |
| emilkowalski/skills | `npx skills add emilkowalski/skills` | Motion/interaction polish (polish phase only) |
| Figma / Penpot MCP | `claude mcp add --transport http figma https://mcp.figma.com/mcp` · `npx -y @penpot/mcp@latest` | Only with a human designer |
| Tooling (not agent) | `eslint-plugin-better-tailwindcss`, `@axe-core/playwright`, `realfavicon`, satori, oklch.com, Radix Colors | DES-05, DES-13, BRD-05, BRD-07 |

Skip: 21st.dev Magic MCP (pulls components outside the design system, third-party service), v0 / Figma Make as source of truth.

## Marketing site, copy, SEO (WEB)

| Item | Install | Use |
| --- | --- | --- |
| marketingskills | `npx skills add coreyhaines31/marketingskills --skill copywriting seo-audit cro pricing` | ~50 skills (launch, onboarding, churn, emails); install only the ones needed (`--list`) |

## Billing, email, analytics, errors (BIL / EML / ANL / OBS)

| Case | Item | Install | Caveat |
| --- | --- | --- | --- |
| Payments | Stripe MCP (remote, OAuth) | `claude mcp add --transport http stripe https://mcp.stripe.com/` | Grant **sandbox** only; from 2027-01-11 full secret keys rejected → OAuth or agent key |
| Payments | Stripe skills | `npx skills add stripe/ai --skill stripe-best-practices` | Repo renamed from `stripe/agent-toolkit` |
| Email | Resend MCP | `claude mcp add --transport http resend https://mcp.resend.com/mcp` | Sends real email → domain-restricted sending key in dev |
| Email | Resend skills | `npx skills add resend/resend-skills` · `npx skills add resend/email-best-practices` · `npx skills add resend/react-email` | Deliverability, templates |
| Errors | Sentry MCP | `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp/{org}/{project}` | Always the `{org}/{project}` scoped URL |
| Errors | Sentry SDK skills | `npx skills add getsentry/sentry-for-ai` | SDK setup, workflows |
| Analytics | PostHog MCP | `npx @posthog/wizard@latest mcp add` | Old `PostHog/mcp` archived; restrict with `?features=`; `execute-sql` reads PII |

## Infra, database, CI/CD (INF / DB / CI)

| Case | Item | Install | Note |
| --- | --- | --- | --- |
| Cloudflare | Cloudflare API MCP | `claude mcp add --transport http cloudflare https://mcp.cloudflare.com/mcp` | DNS, Pages, Access; product servers (docs, audit logs) at `*.mcp.cloudflare.com/mcp` |
| Cloudflare | Cloudflare skills | `/plugin marketplace add cloudflare/skills` | wrangler, Workers, Access, web-perf |
| Docker | Docker skills | `npx skills add docker/skills` | Build strategies, compose patterns |
| Observability | Grafana MCP | `uvx mcp-grafana` (+ `GRAFANA_URL`, service-account token) | Only if running Grafana |
| Ops skills | wshobson/agents | `/plugin marketplace add wshobson/agents` → `cicd-automation`, `observability-monitoring`, `incident-response` | Skip `cloud-infrastructure` (k8s-heavy) |
| IaC | Terraform MCP + HashiCorp skills | `claude mcp add terraform -- docker run -i --rm hashicorp/terraform-mcp-server` · `npx skills add hashicorp/agent-skills` | Only with Terraform/OpenTofu |
| Postgres rules | supabase-postgres-best-practices | `npx skills add supabase/agent-skills --skill supabase-postgres-best-practices` | Mostly vendor-neutral; best default |
| Postgres design | pg-aiguide | `npx skills add timescale/pg-aiguide --skill postgres` | Also `design-postgres-tables`, `postgres-database-migration` |
| Drizzle | postgres-drizzle | `npx skills add ccheney/robust-skills@postgres-drizzle` | No official Drizzle skill exists; low adoption |
| Postgres MCP | DBHub | `npx @bytebase/dbhub@latest --dsn "$DEV_DATABASE_URL"` + `readonly = true` config | Dev DB / read replica only |
| Postgres tuning | Postgres MCP Pro | `uvx postgres-mcp --access-mode=restricted` | Index tuning, EXPLAIN, health; releases slow |
| CI security | Sentry `gha-security-review` | `claude plugin marketplace add getsentry/skills` | Actions security review |
| CI hardening | github-actions-hardening | `npx skills add github/awesome-copilot@github-actions-hardening` | |
| CI templates | `templates/github-actions/` | copy to `.github/workflows/` | CI + staging/prod deploy base (CI-03..19) |
| GitHub | `gh` CLI | — | GitHub MCP is redundant; if used: fine-grained PAT for one repo, read-only toolsets |

Do not use: archived `modelcontextprotocol` postgres server, Hetzner community MCPs (stale → use `hcloud` CLI), Kubernetes/AWS/Supabase/Neon MCPs unless the stack uses them.

## Privacy (LGL)

| Item | Install | Note |
| --- | --- | --- |
| Privacy-law skill for your jurisdiction (e.g. GDPR, CCPA, LGPD community skills) | `npx skills add <owner>/<privacy-skill>` | Community, unreviewed: read SKILL.md first; output is a checklist, not legal advice |

## Product, architecture, API (PRD / ARC / API)

| Item | Install | Use |
| --- | --- | --- |
| mattpocock `to-spec`, `grill-me` | `npx skills add mattpocock/skills --skill to-spec --skill grill-me` | Spec from conversation; stress-test the idea. (`to-prd` was renamed `to-spec`) |
| pm-skills `create-prd` | `npx skills add phuryn/pm-skills --skill create-prd --skill outcome-roadmap` | PRD + outcome roadmap (paths not checked) |
| ADRs | `npx skills add addyosmani/agent-skills --skill documentation-and-adrs` | ADR writing; fits `docs/decisions/` |
| C4 / Mermaid | `npx skills add softaworks/agent-toolkit --skill c4-architecture --skill mermaid-diagrams` | Diagrams as code (repo 8 months without push) |
| oRPC (official) | `npx skills add middleapi/orpc --skill orpc --skill orpc-contract --skill orpc-openapi` | Contract-first API + OpenAPI generation |
| API design | `npx skills add addyosmani/agent-skills --skill api-and-interface-design` | Errors, pagination, versioning |
| Standard Webhooks (official) | `npx skills add standard-webhooks/standard-webhooks --skill receiving-webhooks` | Signature verification, replay protection |
| Tools (not agent) | Spectral (`bunx @stoplight/spectral-cli lint openapi.json`), oasdiff, Scalar | API-08, API-09 |

Skip as default: GitHub spec-kit, BMAD-METHOD (duplicate superpowers, write many files); `samber/developer-platform-skills` (install counts look inflated).

## Testing, accessibility, i18n (TST / A11Y / I18N)

| Item | Install | Use |
| --- | --- | --- |
| qa-skills | `npx skills add petrkindlmann/qa-skills --skill test-strategy --skill test-reliability --skill release-readiness` | Test strategy, flaky tests, release readiness (small repo — read first) |
| mutation-testing | `npx skills add trailofbits/skills --skill mutation-testing` | TST-09 with StrykerJS |
| web-quality accessibility | `npx skills add addyosmani/web-quality-skills --skill accessibility` | A11Y audits |
| WCAG / screen reader | `npx skills add wshobson/agents --skill wcag-audit-patterns --skill screen-reader-testing` | A11Y-07, A11Y-08 |
| Lingui (official) | `npx skills add lingui/skills --skill lingui-best-practices --skill find-unwrapped-strings` | If using Lingui |
| i18next (official) | `npx skills add i18next/i18next-cli --skill i18next-localization` | If using i18next |
| Tools (not agent) | `@axe-core/playwright`, `@faker-js/faker`, StrykerJS | Skip Deque axe MCP (paid) |

TDD: keep one TDD skill (e.g. superpowers `test-driven-development`); do not add a second.

## AI features (AI / FIN)

| Item | Install | Use |
| --- | --- | --- |
| Langfuse (official) | `npx skills add langfuse/skills --skill langfuse` | Tracing, cost, prompt management (self-host for PII) |
| evals-skills | `npx skills add ai-evals-course/evals-skills --skill evals-start --skill eval-audit` | Error analysis, LLM-judge design and validation |
| promptfoo (official) | `npx skills add promptfoo/promptfoo --skill promptfoo-evals` | Evals + red-team in CI |
| OWASP secure-agent-playbook | `npx skills add OWASP/secure-agent-playbook --skill llm-risk-assess --skill prompt-injection-test` | AI-03..06 review (nested path; may need full path) |
| claude-api (Anthropic skill, if building on Claude) | — | Claude API usage, caching, models |

Do not use: `mattpocock/evalite`, `hamelsmu/evals-skills` (both archived). Promptfoo red-team and hosted Langfuse send prompts to third parties → mask PII.

## Mobile (MOB)

| Item | Install | Use |
| --- | --- | --- |
| Expo skills (official) | `npx skills add expo/skills` (pick: `eas-app-stores`, `eas-update`, `expo-router`, `eas-workflows`) | Builds, store submission, OTA |
| Expo MCP (official) | `claude mcp add --transport http expo https://mcp.expo.dev/mcp` | EAS builds/updates; OAuth |
| React Native best practices | `npx skills add callstackincubator/agent-skills --skill react-native-best-practices` | Performance and patterns |

## Docs, support, sales, data (DOC / SUP / CRM / DATA)

| Case | Item | Install | Note |
| --- | --- | --- | --- |
| Docs | Diátaxis skill | `npx skills add sammcj/agentic-coding --skill writing-documentation-with-diataxis` | Community; low adoption |
| Docs | Mintlify | `npx skills add mintlify/docs --skill mintlify` | Only if on Mintlify; Starlight/Fumadocs → Context7 |
| SDK | hey-api/openapi-ts (tool) | `bunx @hey-api/openapi-ts` | DOC-08 |
| Support | Chatwoot CLI skill (official) | `npx skills add chatwoot/cli --skill chatwoot-cli` | Use an agent-bot token, not admin; avoid community Chatwoot MCPs |
| Support | Intercom MCP | `claude mcp add --transport http intercom https://mcp.intercom.com/mcp` *(composed)* | Only if on Intercom |
| CRM | HubSpot skills | `npx skills add hubspot/agent-cli-skills` | Ignore stale `HubSpot/mcp-server` repo |
| CRM | Attio / Twenty MCP | `https://mcp.attio.com/mcp` · `https://<workspace>.twenty.com/mcp` *(composed)* | Built-in vendor MCPs; least-privilege seat |
| BI | Metabase MCP (built in) | `claude mcp add --transport http metabase https://<metabase>/api/metabase-mcp` | Read-only DB user (DATA-03) |
| BI | ClickHouse MCP + skills | `uvx mcp-clickhouse` · `npx skills add clickhouse/agent-skills --skill clickhouse-best-practices` | Write guard "not a security boundary" → read-only user |
| BI | DuckDB skills | `npx skills add duckdb/duckdb-skills` | Local analytics over exports |

## Platform, process, messaging (PLT / ENG / MSG)

| Case | Item | Install | Note |
| --- | --- | --- | --- |
| Search | Meilisearch MCP (official) | `uvx -n meilisearch-mcp` | Give a scoped key, not master |
| Notifications | Novu skills + MCP | `npx skills add novuhq/skills` · `https://mcp.novu.co/` | `novuhq/novu-mcp-server` repo archived |
| Flags | GrowthBook / Unleash MCP | `npx -y @growthbook/mcp@latest` · `npx -y @unleash/mcp@latest` | Only if not using PostHog flags |
| Jobs | — | — | No good BullMQ skill: follow BullMQ production guide (PLT-03..05) |
| Code review | your agent's built-in review command, review skills | — | Claude Code: `/code-review` |
| Code review | CodeRabbit skills | `npx skills add coderabbitai/skills --skill code-review` | Needs CodeRabbit CLI + login |
| SMS | Twilio skills | `npx skills add twilio/ai` | Twilio MCP is alpha and exposes the whole API → API key + service filter |
| WhatsApp | — | — | No official Meta MCP/skill; call Graph API directly. Avoid `lharries/whatsapp-mcp` (unofficial, unmaintained) |

## Supply-chain warnings for skills

- skills.sh has **copycat repos** (`101-skills/*`, `magentosh/*`, `skills-shell/*`, `qu-skills/*`, `bankai-skills/*`) with inflated installs → install only from the original owner.
- Third-party SKILL.md bodies are prompt-injection surface → pin via `skills-lock.json`, review diffs on update, install single skills with `--skill`, never `'*'` from mega-collections.
- Hosted OAuth MCPs inherit the authenticating user's full permissions → authenticate with a least-privilege seat, project scope.

## Non-agent tools referenced by the checklists

Lighthouse CI (PERF-F2) · k6 (PERF-B8) · OWASP ZAP (SEC-10) · `pg_stat_statements`/`EXPLAIN ANALYZE` (PERF-B3, B9) · squawk (DB-09) · pgBackRest/WAL-G (DB-10) · actionlint, zizmor, hadolint, Trivy, gitleaks, Renovate, release-please (CI) · lynis, docker-bench-security, SOPS+age, Infisical (INF).
