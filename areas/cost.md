# Cost and unit economics (FIN)

| ID | L | Requirement |
| --- | --- | --- |
| FIN-01 | 1 | Every paid provider (cloud, LLM, messaging, SMS, email) has a billing alert and a hard cap or budget. Alert is mandatory; where the provider offers only an alert, the alert alone passes if a manual cutoff step is documented. Covers non-LLM per-use services too (e.g. media analysis, GPU, email) |
| FIN-02 | 1 | (n/a if the product has no LLM) LLM keys per environment; provider-side monthly limit + app-side per-tenant (per-account if one person per account) daily cap that **fails closed** (AI-02) |
| FIN-03 | 1 | (n/a if none of these are used; other paid per-use services follow the same rule) Every LLM / messaging / SMS call logged with `tenant_id` (account id if one person per account), model/units and cost |
| FIN-04 | 1 | Unit economics known: cost per active tenant (account if one person per account; active = definition recorded, e.g. used the core feature in 30 days; costs = infra share + payment fees + variable provider spend) vs plan price; margin positive on the cheapest paid plan (a free tier is a cost to budget, not the cheapest plan). Free product with no paid plan: cost per active tenant known and a monthly budget cap recorded; payment fees and the margin clause apply once a paid plan exists |
| FIN-05 | 2 | Per-tenant cost dashboard (infra share + variable) with top-10 tenants by cost |
| FIN-06 | 2 | Anomaly alert when spend > 2× the 7-day average, per provider and per tenant |
| FIN-07 | 2 | Plan limits (messages, seats, storage, AI credits) enforced in code, not only on the pricing page (BIL-01); n/a with reason while the product is free with no limited plans |
| FIN-08 | 2 | TTL/retention on logs, object storage and Redis; unused volumes and snapshots swept monthly |
| FIN-09 | 3 | Resources tagged (env/service/tenant), automated showback; cheaper-model routing for simple tasks; commitment discounts reviewed |

References: [FinOps framework](https://www.finops.org/framework/) · [FinOps for AI](https://www.finops.org/wg/finops-for-ai-overview/) · [LiteLLM budgets](https://docs.litellm.ai/docs/proxy/users) · [Langfuse cost tracking](https://docs.langfuse.com/docs/observability/features/token-and-cost-tracking).
