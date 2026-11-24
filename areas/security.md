# Security (SEC)

| ID | L | Requirement |
| --- | --- | --- |
| SEC-01 | 1 | Headers on every HTML response of the web app (API: those that apply to its responses): HSTS, CSP **enforced** (not report-only), `X-Content-Type-Options`, `Referrer-Policy`, `frame-ancestors`, `Permissions-Policy`. Proof: header scanner or automated test against the deployed URL, covering web app and API; or `curl -sI <url>` output pasted by whoever can reach it, with date and host; the code/config saying so alone is not proof |
| SEC-02 | 1 | Tenant isolation (one-person-per-account apps: per-user data isolation, user A never reads user B's rows) enforced (RLS or mandatory scoped repository) **and** covered by automated cross-tenant (or cross-user) tests |
| SEC-03 | 1 | Authorization checked server-side on every procedure; deny by default. Proof: route/procedure inventory with each guard, or an automated test that every route rejects an unauthenticated and an unauthorized call |
| SEC-04 | 1 | Rate limits: global per IP, per user, per API key (only if the product issues API keys), per expensive endpoint. Proof: config or load-test showing each limit; a sub-clause that does not apply is n/a |
| SEC-05 | 1 | CSRF protection / reject cross-origin state-changing requests; CORS allowlist |
| SEC-06 | 1 | Input validated at runtime with a schema library (e.g. Zod, Valibot) on every boundary: API, webhooks, env, storage. Proof: list of boundaries with their schema (lint rule or grep over handlers) |
| SEC-07 | 1 | Secrets outside the repo; secret scanning in pre-commit; dependency audit in CI (→ CI-02) |
| SEC-08 | 1 | Internal admin/console behind an access proxy (e.g. Cloudflare Access, VPN) **plus** app auth. Applies when an internal admin/console or staff-only routes exist (admin-only API routes inside the main app count as a console); with neither: n/a (reason), and CON tracks building one |
| SEC-09 | 1 | File uploads: type/size limits, private buckets, signed URLs, no executable content served inline |
| SEC-10 | 2 | DAST scan (e.g. OWASP ZAP) on staging with no High findings |
| SEC-11 | 2 | OWASP ASVS 5.0 Level 1 self-review recorded |
| SEC-12 | 3 | External pentest; vulnerability disclosure policy |
| SEC-13 | 1 | Critical provider accounts (domain registrar/DNS, cloud, git host, CI, payment, email provider, app stores): MFA on every account (phishing-resistant, e.g. passkey/security key, where the provider supports it; TOTP at minimum); at least two owners/admins (no single point of failure). Proof: owner attestation (account list, MFA type, owners, date) kept in the repo's ops docs or pending list, since it cannot be read from the repo |
| SEC-14 | 2 | Automated dependency updates (e.g. Dependabot, Renovate) |
| SEC-15 | 2 | Provider accounts (SEC-13): shared credentials in a password manager; access review and offboarding checklist |
