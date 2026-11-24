# Testing and reliability (TST / REL)

## Reliability (REL)

| ID | L | Requirement |
| --- | --- | --- |
| REL-01 | 1 | Staging identical to prod topology, deployed automatically on merge |
| REL-02 | 1 | E2E tests on critical journeys: signup, login, payment, core action |
| REL-03 | 1 | Error pages / error boundary in the app; user never sees a stack trace |
| REL-04 | 1 | Stateless app servers; config only via env vars |
| REL-05 | 2 | Gradual rollout via feature flags (ADM-05) or canary |
| REL-06 | 3 | DR plan with RPO/RTO, rehearsed every 6 months |

## Test strategy (TST)

| ID | L | Requirement |
| --- | --- | --- |
| TST-01 | 1 | Written test strategy: what is covered at unit, integration and e2e; e2e limited to critical journeys |
| TST-02 | 1 | CI blocks merge on unit/integration failure |
| TST-03 | 1 | Integration tests run against real database, cache and queue backends (same engines as production), not mocks |
| TST-04 | 1 | Tenant-isolation test proves tenant A cannot read tenant B (SEC-02) |
| TST-05 | 1 | Test data from factories; no shared mutable fixtures, no dependence on dev DB state |
| TST-06 | 1 | Pre-release smoke checklist run on staging; results recorded |
| TST-07 | 2 | Flaky-test policy: quarantine tag, owner, fix or delete within N days, no blind retries |
| TST-08 | 2 | External APIs covered by contract or recorded-fixture tests; webhook handlers tested with real payloads |
| TST-09 | 3 | Mutation testing (StrykerJS) on domain and billing modules with a score threshold |

References: [Practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) · [Flaky tests at Google](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html) · [StrykerJS](https://stryker-mutator.io/docs/stryker-js/introduction/).
