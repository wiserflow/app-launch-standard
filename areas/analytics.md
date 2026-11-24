# Product analytics and business metrics (ANL)

| ID | L | Requirement |
| --- | --- | --- |
| ANL-01 | 1 | Tracking plan written in the repo's docs (default `docs/analytics.md`): event name, when it fires, properties. A plan alone passes this item; implementation is ANL-02 |
| ANL-02 | 1 | Product analytics (e.g. PostHog, OpenPanel; self-hosted or privacy-first is fine) with `identify` (user; plus org/group on team accounts only) firing the events from ANL-01 (→ ANL-01): signup, activation, conversion, cancellation; list any missing event |
| ANL-03 | 2 | Funnels (signup → activation → paid) and cohort retention |
| ANL-04 | 2 | SaaS metrics board: MRR, new/expansion/churned MRR, logo churn, ARPA, LTV, trial→paid conversion |
| ANL-05 | 2 | Session replay with input masking |
| ANL-06 | 3 | Experiments / A/B (PostHog, GrowthBook) |
