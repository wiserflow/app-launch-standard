# Tenancy and customer-side admin (ADM)

Customer-facing: what the customer's own owner/admin sees. The company's internal backoffice is `owner-console.md` (CON).

| ID | L | Requirement |
| --- | --- | --- |
| ADM-01 | 1 | Organizations, members, invitations and roles → see organization.md (→ ORG-*; status derived from the target area, not set independently) |
| ADM-02 | 1 | Audit log (actor, action, target, IP, time) visible to the account holder (org owner on team accounts); the account holder's own activity/security log satisfies it, separate from the staff audit log (CON-03). Retention: documented period that is actually enforced (e.g. scheduled purge) |
| ADM-03 | 1 | Internal owner console exists → see `owner-console.md` (→ CON-*; its L1 items are launch blockers, status derived from that area) |
| ADM-04 | 2 | Impersonation for support → CON-12 |
| ADM-05 | 2 | Feature flags per org/user (beta cohorts, kill switches for integrations) |
| ADM-06 | 3 | Public API with keys, per-plan limits, OpenAPI docs |
| ADM-07 | 3 | Outbound webhooks for customers: signed, retried, delivery log |
