# API design (API)

| ID | L | Requirement |
| --- | --- | --- |
| API-01 | 1 | One error envelope everywhere (RFC 9457 problem details or typed contract errors) with a stable machine code; no stack/SQL leak |
| API-02 | 1 | Input schema-validated at the boundary; output schemas declared |
| API-03 | 1 | Every list endpoint paginated with a hard max (cursor for unbounded sets) — same as PERF-B2 |
| API-04 | 1 | Mutations that touch money/messages or get retried accept an `Idempotency-Key`, deduplicated server-side |
| API-05 | 1 | Object-level authorization per tenant on every route (OWASP API1 BOLA) with an automated test |
| API-06 | 1 | Rate limits per key/tenant; `429` with `Retry-After` |
| API-07 | 1 | Webhooks out: Standard Webhooks signing (id, timestamp, HMAC), retries with backoff, replay protection. Webhooks in: verify signature on the **raw** body, ack fast, process via queue, dedupe by event id |
| API-08 | 2 | OpenAPI generated from the contract (never hand-written), linted with Spectral in CI, published with Scalar |
| API-09 | 2 | Versioning + deprecation policy written; breaking changes detected in CI (oasdiff) |
| API-10 | 3 | Public API: changelog, sandbox/test mode, API keys per plan, webhook delivery log with replay UI (see ADM-06/07) |

References: [Zalando REST guidelines](https://opensource.zalando.com/restful-api-guidelines/) · [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) · [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md) · [Idempotency-Key draft](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) · [Google AIP-158 pagination](https://google.aip.dev/158) · [OWASP API Top 10 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/).
