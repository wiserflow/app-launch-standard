# Performance (PERF)

## Front end (app and site) — measured on a mid-range phone, 4G

| ID | L | Requirement |
| --- | --- | --- |
| PERF-F1 | 1 | Core Web Vitals at p75: **LCP < 2.5 s, INP < 200 ms, CLS < 0.1**; FCP < 1.8 s; TTFB < 800 ms |
| PERF-F2 | 1 | Lighthouse ≥ 90 (performance, SEO, accessibility, best practices) on landing and pricing; run in CI with budgets |
| PERF-F3 | 1 | Brotli/gzip compression, HTTP/2+, CDN for static assets, long `Cache-Control` + hashed filenames, `no-cache` on HTML |
| PERF-F4 | 1 | Images: AVIF/WebP, responsive `srcset`, explicit width/height, lazy below the fold, **not** lazy (and `fetchpriority="high"`) on the LCP image |
| PERF-F5 | 1 | Fonts: WOFF2, subset, `font-display: swap`, preload the main face, metric-compatible fallback |
| PERF-F6 | 1 | JS budget: initial route ≤ ~170 KB gzip; route-level code splitting; no duplicate libs; bundle analyzer in CI |
| PERF-F7 | 1 | Third-party scripts (analytics, chat, replay) async/deferred, loaded after consent or interaction |
| PERF-F8 | 2 | Long lists/tables virtualized; heavy handlers debounced/throttled; tasks > 50 ms split |
| PERF-F9 | 2 | Data fetching: cache + stale-while-revalidate, prefetch on hover/intent, optimistic updates on common mutations |
| PERF-F10 | 2 | Skeletons instead of spinners for page loads; no layout shift when data arrives |
| PERF-F11 | 2 | Real-user monitoring of Web Vitals (Sentry/PostHog/`web-vitals`) with alert on regression |
| PERF-F12 | 3 | Speculation Rules / prerender of likely next page; back/forward cache compatible |

## Back end, data and jobs

| ID | L | Requirement |
| --- | --- | --- |
| PERF-B1 | 1 | Latency budget: API p95 < 300 ms for reads, < 800 ms for writes on core endpoints (adjust per product, but **write it down**) |
| PERF-B2 | 1 | Every list endpoint paginated (cursor-based), with a max page size |
| PERF-B3 | 1 | Indexes for every foreign key and every `WHERE`/`ORDER BY` used by hot queries; `EXPLAIN ANALYZE` reviewed for top queries |
| PERF-B4 | 1 | No N+1: hot paths reviewed; query count per request visible in dev logs or traces |
| PERF-B5 | 1 | DB connection pooling sized for instances × workers (PgBouncer or driver pool); statement timeout set |
| PERF-B6 | 1 | Timeouts on **every** outbound call; retries with exponential backoff + jitter only on idempotent operations |
| PERF-B7 | 1 | Slow work (email, exports, webhooks, AI, media) off the request path, in a queue with retries, dead-letter and concurrency limits |
| PERF-B8 | 1 | Load test (k6) of the critical journey at 3× expected launch peak in staging; results recorded |
| PERF-B9 | 2 | `pg_stat_statements` enabled; slow-query log (> 200 ms) reviewed weekly |
| PERF-B10 | 2 | Caching layer (Redis) for expensive reads with explicit invalidation; cache hit rate monitored |
| PERF-B11 | 2 | Queue fairness: per-tenant concurrency caps so one customer cannot starve others; backpressure when queue depth grows |
| PERF-B12 | 2 | Circuit breaker / graceful degradation when a dependency is down (feature disabled, not whole app) |
| PERF-B13 | 2 | Graceful shutdown: stop accepting, drain in-flight requests and jobs, then exit |
| PERF-B14 | 3 | Capacity plan: known limits per instance, autoscaling or documented scale-up procedure; read replicas if needed |
