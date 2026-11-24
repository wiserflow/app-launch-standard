# Launch runbook and operating cadence

## Launch runbook

**T-14 days**

- [ ] All L1 items checked with evidence
- [ ] DES gates green: design-token lint, utility-class/CSS lint, design-rule detector in CI, visual baselines, accessibility scan (e.g. `design.md lint`, Tailwind lint, `impeccable detect`, axe)
- [ ] Legal texts published after lawyer review
- [ ] DMARC at `quarantine`; EML-09 inbox test done
- [ ] PERF-B8 load test done on staging; SEC-10 DAST scan on staging (L2 — if done; not a launch blocker)
- [ ] INF-03 external port scan clean; DB-03 restore test passed; CI-06/OPS-04 rollback rehearsed

**T-1 day**

- [ ] Billing in live mode: real purchase + refund
- [ ] Production error reaches error tracker with correct release
- [ ] Alerts reach phone (OPS-03)
- [ ] Status page up — OPS-05 (L2 — if done; not a launch blocker)
- [ ] New features behind flags where risky — PLT-09/ADM-05 (L2 — if done; not a launch blocker)

**Launch day**

- [ ] End-to-end signup in incognito, phone and desktop
- [ ] Watch errors, 5xx, queue depth, Web Vitals and funnel for 2 h
- [ ] Announce: waitlist email, social, communities

**T+7 / T+30**

- [ ] Review activation funnel; tune EML-O1..O3
- [ ] Read every ticket/feedback; top 3 become tasks
- [ ] First NPS (T+30)
- [ ] Launch retrospective in `docs/decisions/`

## Operating cadence after launch

| Cadence | Activity |
| --- | --- |
| Daily | New errors, open alerts, support queue |
| Weekly | Signups, activation, MRR, churn; slow queries; changelog |
| Monthly | Email metrics (open/click/unsubscribe/complaint), NPS, infra cost, dependency updates, Web Vitals trend |
| Quarterly | Restore test, access review (who has admin), privacy review, secret rotation |
| Twice a year | DR rehearsal, terms review, pentest if enterprise customers |

---
