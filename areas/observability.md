# Observability (OBS / OPS)

| ID | L | Requirement |
| --- | --- | --- |
| OBS-01 | 1 | Error tracking (e.g. Sentry) in API, worker and browser with `release`, `environment`, user/tenant context, PII scrubbing, uploaded source maps |
| OBS-02 | 1 | Structured JSON logs with `request_id`, `tenant_id`, `user_id`, PII redaction; request id propagated API → queue → worker |
| OBS-03 | 1 | `/health/live` (process) and `/health/ready` (DB + Redis + critical deps) |
| OBS-04 | 1 | External uptime checks on site, app and API (e.g. Uptime Kuma, UptimeRobot, OpenStatus) |
| OBS-05 | 1 | Cron/job heartbeat: alert when a scheduled job did **not** run |
| OBS-06 | 2 | Metrics (e.g. Prometheus/OTel): request rate, p50/p95/p99 latency, 5xx rate, queue depth, job failures, DB pool usage. `/metrics` not public |
| OBS-07 | 2 | Distributed tracing (OpenTelemetry) across API → queue → worker → external calls |
| OBS-08 | 2 | Dashboards: one "service overview" board + one per critical flow |
| OBS-09 | 3 | SLOs per user journey (e.g. 99.9% availability, p95 < 500 ms) with error budget and owner |

## Alerting, incidents, status (OPS)

| ID | L | Requirement |
| --- | --- | --- |
| OPS-01 | 1 | Critical alerts reach a phone (e.g. push, Telegram, WhatsApp, PagerDuty): app down, 5xx > threshold, queue stalled, disk > 80%, backup failed, TLS cert < 14 days |
| OPS-02 | 1 | Every alert is **actionable** and links to a runbook (`docs/runbooks/`). Warning alerts → chat/ticket, critical → phone |
| OPS-03 | 1 | Alert path tested by breaking staging on purpose |
| OPS-04 | 1 | Rollback procedure documented and rehearsed (previous image + reversible migration) |
| OPS-05 | 2 | Public status page `status.<domain>` with components and incident history |
| OPS-06 | 2 | Incident template + blameless postmortem (`docs/incidents/YYYY-MM-DD-slug.md`) |
| OPS-07 | 2 | Known SLA of every external dependency (payment, email, LLM, messaging APIs) and behavior when it is down |
| OPS-08 | 3 | On-call rotation with escalation; scheduled-maintenance communication via email + status page |
