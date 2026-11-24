# Database (DB)

| ID | L | Requirement |
| --- | --- | --- |
| DB-01 | 1 | App connects with a non-superuser role that does not own the tables; migrations use a separate role |
| DB-02 | 1 | Postgres not reachable from the internet; connections over TLS or private overlay network |
| DB-03 | 1 | Daily backup: (a) off-site, (b) encrypted, (c) retention ≥ 30 days, (d) **automated restore test** into a scratch DB, timed; score each part |
| DB-04 | 1 | Every migration committed and applied by the pipeline, or by a scripted, logged deploy step when no CI exists (→ CI-02), never by hand; ORM drift check passes (`drizzle-kit check`) |
| DB-05 | 1 | Every tenant-scoped table has the owner/tenant key `NOT NULL` (`tenant_id`; owner `user_id` for one person per account; n/a only if the app has no per-owner data); isolation by RLS or tested scoped query layer (see SEC-02) |
| DB-06 | 1 | Conventions: `timestamptz`, money as integer cents or `numeric`, `text` over `varchar(n)`, identity/UUIDv7 keys, index on every FK |
| DB-07 | 1 | Pool size × replicas < `max_connections`; `statement_timeout` and `idle_in_transaction_session_timeout` set for the app role |
| DB-08 | 2 | Zero-downtime migrations (expand/contract): `CREATE INDEX CONCURRENTLY`, constraints `NOT VALID` → `VALIDATE`, `lock_timeout` set, no rename/drop in the same deploy as the code change |
| DB-09 | 2 | `squawk` lints the generated migration SQL in CI and blocks the merge |
| DB-10 | 2 | PITR via WAL archiving (pgBackRest or WAL-G) to object storage, RPO/RTO stated, quarterly restore drill; backups with object lock |
| DB-11 | 2 | Alerts: disk, connection count, long transactions, replication lag, autovacuum/bloat |
| DB-12 | 3 | PgBouncer (transaction mode), read replica / failover plan, partitioning + retention for large tables |

Related: PERF-B2..B5, PERF-B9 (indexes, N+1, pooling, `pg_stat_statements`). Rule list worth reading: Postgres wiki "Don't Do This", `ankane/strong_migrations` README.
