# Data, BI and reporting (DATA)

Small-SaaS default: read replica or nightly DuckDB/Parquet export + Metabase. ClickHouse only past ~100M event rows.

| ID | L | Requirement |
| --- | --- | --- |
| DATA-01 | 1 | BI never queries the primary: read replica or export, read-only role |
| DATA-02 | 1 | Core metrics (MRR, active tenant, activation, churn) defined once in writing, SQL in the repo |
| DATA-03 | 1 | BI/MCP credentials read-only, PII columns excluded, never the app's DB user |
| DATA-04 | 2 | Founder dashboard: signups, activation, MRR, churn, usage per tenant (ANL-04) |
| DATA-05 | 2 | Event tables append-only with `tenant_id` + `occurred_at`; time-partitioned or TTL |
| DATA-06 | 2 | Customer-facing reports tenant-scoped at the query layer and tested for cross-tenant leaks |
| DATA-07 | 2 | Exports/ELT idempotent, monitored, alert on staleness |
| DATA-08 | 3 | Semantic layer (Cube / Metabase models) as single source for BI and embedded analytics |
| DATA-09 | 3 | Columnar store for events with PII pseudonymized; privacy-law erasure propagates to the warehouse |

References: [Metabase MCP](https://www.metabase.com/docs/latest/ai/mcp) · [Evidence.dev](https://docs.evidence.dev/) · [Cube](https://cube.dev/docs).
