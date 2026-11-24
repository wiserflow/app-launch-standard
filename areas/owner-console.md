# Owner console / backoffice (CON)

The internal app the company uses to run the business: customers, money, communication, operations. Separate from the customer-facing admin (org settings, members, audit for the customer's owner — see `admin.md`).

Default build (for a team or a product with tenants, billing or support volume): its own app in the monorepo (e.g. `apps/console`) on the same stack, reusing packages (auth admin plugin, billing, email, audit, flags). A pre-launch or small product may meet the CON items with a minimal staff-only area inside the app (admin routes behind SEC-08 staff roles and an access proxy or equivalent control) instead of a separate app; CON L1 items still block launch, and each must be met or marked n/a (reason) per its "applies when" clause. Admin frameworks (Refine, react-admin, Appsmith) only if the team prefers them; they add a second UI stack.

## Access and safety

| ID | L | Requirement |
| --- | --- | --- |
| CON-01 | 1 | Separate origin (`console.<domain>`) or, for a minimal in-app staff area, a separate route prefix with the same controls, behind an access proxy (Cloudflare Access / VPN) **and** app auth with mandatory 2FA (SEC-08). Report the three parts (origin, proxy, 2FA) separately |
| CON-02 | 1 | Staff roles (default: owner, finance, support, read-only; a solo-founder team passes with owner plus read-only); permission checked server-side per action |
| CON-03 | 1 | Every staff action written to a staff audit log (who, what, target, reason, IP, time), visible in the console |
| CON-04 | 1 | Dangerous actions (delete, refund, plan override, data export) need explicit confirmation (type the target name) and a reason |
| CON-05 | 2 | Staff sessions listed and revocable; staff access reviewed quarterly |
| CON-06 | 3 | Four-eyes approval for refunds above a threshold and for account deletion |

## Overview

| ID | L | Requirement |
| --- | --- | --- |
| CON-07 | 1 | Home dashboard: signups (today / 7d / 30d), activation rate, paying customers, MRR, churn, failed payments, open tickets or feedback items (if SUP-01 exists) |
| CON-08 | 2 | Trends and cohorts (from ANL/DATA, read replica — never the primary for heavy queries) |

## Customers

| ID | L | Requirement |
| --- | --- | --- |
| CON-09 | 1 | Search by email, name, payment-provider id, plus organization (team accounts only), tax id and phone where collected |
| CON-10 | 1 | Customer page: plan, status, usage vs limits, payments and invoices, last activity, sessions, onboarding milestones, emails sent, audit trail; members (team accounts only); tickets (if SUP-01 exists) |
| CON-11 | 1 | Account actions: suspend/ban and reactivate, force logout, resend verification, reset 2FA (with identity check), extend trial |
| CON-12 | 1 | Applies when staff can act as a customer; n/a (reason) when no staff will view customer sessions at launch (support done from the console view only). Impersonation: reason required, time-boxed, read-only by default, visible banner for staff, audited, customer can see it happened (ADM-04) |
| CON-13 | 2 | Plan override / credits / limit bump with an expiry date (no permanent silent overrides) |
| CON-14 | 2 | Notes and tags on a customer (sales/support context), synced to CRM if one exists (CRM-01) |

## Money

| ID | L | Requirement |
| --- | --- | --- |
| CON-15 | 1 | Subscriptions list with status filters; overdue / dunning queue with days overdue and next action (BIL-05) |
| CON-16 | 1 | Applies when the product takes payments; n/a (reason) when free. Refund and cancel from the console through the payment provider (never by editing the DB); recorded as revenue lines |
| CON-17 | 2 | Revenue view: MRR movements (new, expansion, contraction, churn), revenue by plan, reconciliation with the provider's payouts |
| CON-18 | 2 | Coupons and price versions managed with history |

## Communication

| ID | L | Requirement |
| --- | --- | --- |
| CON-19 | 1 | Per-user email log (template, status, opens/bounces) with resend (EML-07) |
| CON-20 | 2 | Template previews with sample data; lifecycle rules on/off per rule (EML-08) |
| CON-21 | 2 | Broadcasts to a segment (plan, activity, tag) respecting preferences and unsubscribes; in-app announcement banner; changelog post (SUP-03) |

## Support and feedback

| ID | L | Requirement |
| --- | --- | --- |
| CON-22 | 1 | Ticket / feedback queue with status and link to the customer page; assignee (only when 2+ staff). A feedback inbox without assignee passes for a solo operator (SUP-01) |
| CON-23 | 2 | Privacy request queue (data subject requests): export and deletion requests with deadline and status (LGL-03, LGL-04) |
| CON-24 | 2 | NPS / survey results and cancellation reasons, filterable by plan (GRW-01, BIL-07) |

## Operations

| ID | L | Requirement |
| --- | --- | --- |
| CON-25 | 1 | System health page: services, queue depth and failed jobs with retry/discard, cron heartbeats (OBS) |
| CON-31 | 2 | System health page links to the error tracker and dashboards (OBS) |
| CON-26 | 1 | Per-account integration status (payment, messaging, email domain, third-party connections; per tenant on team accounts) with last error. In one-person-per-account products, payment-provider state per user plus any other connected integration is the whole requirement |
| CON-27 | 2 | Per tenant only when tenants exist, otherwise per user. Feature flags per tenant/user from the console (ADM-05); maintenance mode toggle with status-page message |
| CON-28 | 2 | Plans/limits editor versioned (BIL-01); system settings with audit |
| CON-29 | 2 | n/a (reason) with a single provider and no per-tenant cost. Cost view per tenant and per provider (FIN-05) |
| CON-30 | 3 | CSV exports with PII masking for finance/accounting; scheduled reports by email |

References: Better Auth admin plugin (ban, impersonation, sessions) · [Refine](https://github.com/refinedev/refine) · [react-admin](https://github.com/marmelab/react-admin) · [Appsmith](https://github.com/appsmithorg/appsmith).
