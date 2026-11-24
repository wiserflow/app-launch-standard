# Billing (BIL)

| ID | L | Requirement |
| --- | --- | --- |
| BIL-01 | 1 | Plans, limits and entitlements defined in **one** module; UI and API read from it |
| BIL-02 | 1 | Checkout with local payment methods (card + instant payment such as Pix where relevant) |
| BIL-03 | 1 | Webhooks: signature verified, idempotent (store provider event id), processed async via queue, replay-safe |
| BIL-04 | 1 | Customer portal: change card, change plan, cancel, download invoices |
| BIL-05 | 1 | Dunning: failed-payment email sequence + grace period + read-only mode + final suspension, all timed and documented |
| BIL-06 | 1 | Receipt/invoice email on every successful charge |
| BIL-07 | 1 | Cancellation flow with reason capture (1 click, required field) |
| BIL-08 | 1 | Real-money test in production (buy + refund) before launch |
| BIL-09 | 2 | Trial: `trial_will_end` email (T-3d, T-0), clear post-trial state |
| BIL-10 | 2 | Upgrade/downgrade with proration; coupons; usage warnings at 80% / 100% of limits |
| BIL-11 | 2 | Fiscal invoice issuance where legally required (e.g. NFS-e in Brazil) |
| BIL-12 | 3 | Usage-based billing, annual contracts, invoice/bank-slip payment for companies |
