# Developer and API documentation (DOC)

Only when the product exposes an API, SDK, webhooks or integrations. End-user help center is SUP-02.

| ID | L | Requirement |
| --- | --- | --- |
| DOC-01 | 1 | OpenAPI generated from code, never hand-written; CI fails on drift (API-08) |
| DOC-02 | 1 | Quickstart reaches a first successful call in < 5 min: copy-paste curl + test key |
| DOC-03 | 1 | Auth, errors (codes + shape), rate limits, pagination and webhooks (signature verification, retries) documented |
| DOC-04 | 1 | Docs in the repo, deployed from CI, link checker in CI |
| DOC-05 | 2 | Content split by Diátaxis: tutorial / how-to / reference / explanation — no mixed pages |
| DOC-06 | 2 | Changelog + versioning/deprecation policy published; `llms.txt` and per-page markdown served |
| DOC-07 | 2 | Code samples tested (extracted and run in CI) |
| DOC-08 | 2 | Typed TS SDK generated from the spec (hey-api/openapi-ts), published with semver |
| DOC-09 | 3 | Multi-language SDKs, interactive playground with sandbox keys, docs search analytics, stability tiers (beta/GA) |

References: [Diátaxis](https://diataxis.fr/) · [Starlight](https://starlight.astro.build/) · [Fumadocs](https://fumadocs.dev/docs) · [hey-api/openapi-ts](https://heyapi.dev/openapi-ts/get-started).
