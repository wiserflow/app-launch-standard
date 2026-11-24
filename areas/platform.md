# Platform building blocks (PLT)

Uploads, background jobs, cron, realtime, search, notifications, feature flags.

| ID | L | Requirement |
| --- | --- | --- |
| PLT-01 | 1 | Uploads go direct to the bucket via short-lived presigned URLs; size + MIME enforced server-side; tenant-prefixed keys |
| PLT-02 | 1 | Buckets private; downloads via signed URLs; user files served from a separate domain or with `Content-Disposition: attachment` |
| PLT-03 | 1 | Jobs idempotent with explicit attempts + backoff, `removeOnComplete`/`removeOnFail` set, failed-job alert, dead-letter |
| PLT-04 | 1 | Workers shut down gracefully on SIGTERM; Redis `maxmemory-policy noeviction` + persistence for queues |
| PLT-05 | 1 | One cron scheduler (e.g. BullMQ job schedulers), overlap-safe, monitored for missed runs (OBS-05) |
| PLT-06 | 1 | WebSocket/SSE: auth at connect, authorization per channel/tenant, heartbeat, client reconnect with backoff |
| PLT-07 | 2 | Search index sync queue-driven, full-reindex command exists, tenant filter enforced server-side with scoped keys |
| PLT-08 | 2 | Notifications: per-user channel preferences, unsubscribe, dedupe/digest, delivery log (see SUP-04) |
| PLT-09 | 2 | Feature flags: kill switch for risky features; each flag has owner + expiry; stale flags removed (ADM-05) |
| PLT-10 | 3 | Resumable uploads (tus/multipart), malware scan, realtime fan-out across instances (Redis pub/sub), per-tenant queue rate limits |

References: [OWASP File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) · [BullMQ going to production](https://docs.bullmq.io/guide/going-to-production) · [BullMQ job schedulers](https://docs.bullmq.io/guide/job-schedulers) · [R2 presigned URLs](https://developers.cloudflare.com/r2/api/s3/presigned-urls/) · [tus protocol](https://tus.io/protocols/resumable-upload).
