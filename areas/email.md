# Email infrastructure and lifecycle (EML)

## Infrastructure

| ID | L | Requirement |
| --- | --- | --- |
| EML-01 | 1 | Own sending domain with SPF, DKIM, DMARC (`p=none` → `p=quarantine` after 2 clean weeks). Proof: headers of a real sent message show spf/dkim/dmarc=pass; DMARC policy read via DNS lookup |
| EML-02 | 1 | Separate senders/subdomains for transactional vs marketing (reputation isolation); if the product sends no marketing mail yet, a distinct sender/stream per mail kind (a kind field) is enough, and the marketing subdomain is needed before the first campaign |
| EML-03 | 1 | Provider webhooks (bounce, complaint) → suppression list checked before every send |
| EML-04 | 1 | Unsubscribe link + `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click) on non-transactional mail |
| EML-05 | 1 | Preferences by category (account, billing, product, marketing), stored per user and honored at send time (EML-04 covers the per-message link). Security and billing are not unsubscribable |
| EML-06 | 1 | Single layout: logo, footer with legal name/address, preferences link; plain-text part; dark-mode checked |
| EML-07 | 1 | Every send logged (e.g. `email_sends`: user, template, trigger, provider id, status; the trigger may live in a related lifecycle table) to dedupe and audit. Logged = a row exists per send, status updated from provider webhooks |
| EML-08 | 1 | Dev/staging use a log/dry driver; lifecycle sending behind a flag in prod |
| EML-09 | 1 | Inbox placement tested: Gmail, Outlook, iCloud, one corporate domain (not spam, renders correctly) |
| EML-10 | 2 | Templates in a component system (react-email / MJML / maizzle) with previews |

## Lifecycle map

Rules: max **1 product email per day** per user; a sequence stops as soon as the target action happens; every rule is idempotent.

| ID | L | Trigger | Email | Category |
| --- | --- | --- | --- | --- |
| EML-T1 | 1 | Signup | Verify your email | account |
| EML-T2 | 1 | Email verified | Welcome: one primary action, link to first step | account |
| EML-T3 | 1 | Reset requested / password changed | Reset link / change confirmation | security |
| EML-T4 | 1 | Login from new device | New login detected | security |
| EML-T5 | 1 | Member invited (team accounts only) | Invitation | account |
| EML-T6 | 1 | Data export ready / account deleted | Download link (in-app download counts) / confirmation | account |
| EML-B1 | 1 | Payment succeeded | Receipt (platform subscription; provider-hosted receipts count; marketplace/Connect receipts only if the app takes such payments) | billing |
| EML-B2 | 1 | Payment failed | Update card: D0, D3, D7 (final) | billing |
| EML-B3 | 2 | Trial ending | T-3d, T-0 | billing |
| EML-B4 | 2 | Annual renewal | T-7d notice | billing |
| EML-B5 | 1 | Subscription canceled | Confirmation + feedback ask | billing |
| EML-O1 | 2 | D+1 not activated | First-step tip | product |
| EML-O2 | 2 | D+3 not activated | Use case / short video | product |
| EML-O3 | 2 | D+7 not activated | Human offer: "reply to this email" | product |
| EML-O4 | 2 | Activation milestone reached | Congrats + next level | product |
| EML-E1 | 2 | Weekly | Usage digest | product |
| EML-E2 | 2 | 80% of plan limit | Upgrade prompt | billing |
| EML-R1 | 2 | 14 days inactive | We miss you + what's new | reengagement |
| EML-R2 | 2 | 30 days inactive | Last touch, then stop | reengagement |
| EML-N1 | 2 | D+30 paying | NPS | product |
| EML-W1 | 3 | 30 days after cancel | Win-back | marketing |
| EML-M1 | 3 | Feature launch | Newsletter / changelog | marketing |
