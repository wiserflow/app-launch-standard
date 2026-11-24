# Security (SEC)

| ID | L | Requirement |
| --- | --- | --- |
| SEC-01 | 1 | Headers: HSTS, CSP **enforced** (not report-only), `X-Content-Type-Options`, `Referrer-Policy`, `frame-ancestors`, `Permissions-Policy` |
| SEC-02 | 1 | Tenant isolation enforced (RLS or mandatory scoped repository) **and** covered by automated cross-tenant tests |
| SEC-03 | 1 | Authorization checked server-side on every procedure; deny by default |
| SEC-04 | 1 | Rate limits: global per IP, per user, per API key, per expensive endpoint |
| SEC-05 | 1 | CSRF protection / reject cross-origin state-changing requests; CORS allowlist |
| SEC-06 | 1 | Input validated at runtime with a schema library (e.g. Zod, Valibot) on every boundary: API, webhooks, env, storage |
| SEC-07 | 1 | Secrets outside the repo; secret scanning in pre-commit; dependency audit in CI; automated dependency updates (e.g. Dependabot, Renovate) |
| SEC-08 | 1 | Internal admin/console behind an access proxy (e.g. Cloudflare Access, VPN) **plus** app auth |
| SEC-09 | 1 | File uploads: type/size limits, private buckets, signed URLs, no executable content served inline |
| SEC-10 | 2 | DAST scan (e.g. OWASP ZAP) on staging with no High findings |
| SEC-11 | 2 | OWASP ASVS 5.0 Level 1 self-review recorded |
| SEC-12 | 3 | External pentest; vulnerability disclosure policy |
| SEC-13 | 1 | Critical provider accounts (domain registrar/DNS, cloud, git host, CI, payment, email provider, app stores): MFA on every account (phishing-resistant, e.g. passkey/security key, where the provider supports it; TOTP at minimum); at least two owners/admins (no single point of failure); shared credentials in a password manager; access review and offboarding checklist |
