# Tenancy and customer-side admin (ADM)

Customer-facing: what the customer's own owner/admin sees. The company's internal backoffice is `owner-console.md` (CON).

| ID | L | Requirement |
| --- | --- | --- |
| ADM-01 | 1 | Organizations, members, invitations and roles → see organization.md (ORG-*) |
| ADM-02 | 1 | Audit log (actor, action, target, IP, time) visible to the org owner; retention defined |
| ADM-03 | 1 | Internal owner console exists → see `owner-console.md` (its L1 items are launch blockers) |
| ADM-04 | 2 | Impersonation for support → CON-12 |
| ADM-05 | 2 | Feature flags per org/user (beta cohorts, kill switches for integrations) |
| ADM-06 | 3 | Public API with keys, per-plan limits, OpenAPI docs |
| ADM-07 | 3 | Outbound webhooks for customers: signed, retried, delivery log |
