# Billing (BIL)

| ID | L | Requirement |
| --- | --- | --- |
| BIL-01 | 1 | Plans, limits and entitlements defined in **one** module; UI and API read from it |
| BIL-02 | 1 | Checkout with local payment methods: recurring subscriptions use methods the provider supports for recurring charges (card, debit mandates); one-off payments may add instant methods (e.g. Pix) per Kickoff market; document which is which |
| BIL-03 | 1 | Webhooks: signature verified; idempotent (store provider event id); replay-safe; acknowledged fast, then processed via queue or inline (either passes if retries are safe) |
| BIL-04 | 1 | Customer portal: change card, change plan, cancel, download invoices |
| BIL-05 | 1 | Dunning: failed-payment email sequence + grace period + read-only mode + final suspension, all timed and documented |
| BIL-06 | 1 | Receipt/invoice email on every successful charge |
| BIL-07 | 1 | Cancellation flow with reason capture in a single step (required choice, free text optional); if cancel also deletes data, its destructive confirmation wins and the reason is asked in that same step |
| BIL-08 | 1 | Real-money test in production (buy + refund) before launch |
| BIL-09 | 2 | Trial: `trial_will_end` email (T-3d, T-0), clear post-trial state |
| BIL-10 | 2 | Upgrade/downgrade with proration; coupons; usage warnings at 80% / 100% of limits |
| BIL-11 | 2 | Fiscal invoice issuance where legally required (e.g. NFS-e in Brazil) |
| BIL-12 | 3 | Usage-based billing, annual contracts, invoice/bank-slip payment for companies |
