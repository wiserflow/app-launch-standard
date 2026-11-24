# Privacy and legal (LGL)

Written to satisfy GDPR-style privacy laws (GDPR, UK GDPR, LGPD, CCPA/CPRA); confirm local specifics with counsel.

| ID | L | Requirement |
| --- | --- | --- |
| LGL-01 | 1 | Terms and privacy policy **reviewed by a lawyer**, versioned, dated |
| LGL-02 | 1 | Data protection officer (DPO) + privacy contact published |
| LGL-03 | 1 | Self-service data export (async, link by email) |
| LGL-04 | 1 | Account deletion with grace period → cancels subscription → anonymizes/purges data, including backups policy stated |
| LGL-05 | 1 | Cookie consent with categories if any non-essential cookie/tracker exists (orestbida/cookieconsent); none → state "essential only" |
| LGL-06 | 1 | Retention policy per data class (logs, audit, deleted accounts, messages) implemented as jobs |
| LGL-07 | 2 | Subprocessor list published (payments, email, hosting, error tracking, analytics, AI providers) |
| LGL-08 | 2 | Internal record of processing activities (ROPA) |
| LGL-09 | 2 | DPA template for B2B customers |
| LGL-10 | 3 | Sensitive data (health, biometrics, minors): specific consent, encryption at rest, access logging |
| LGL-11 | 1 | Security-incident / personal-data-breach procedure: named owner + backup decide; severity triage; evidence preserved; regulator notified within the legal deadline of each jurisdiction served (e.g. GDPR Art. 33: 72 h); affected users notified when risk is high (e.g. Art. 34); processor→controller notification; breach register kept even when not notified; pre-written templates; postmortem → OPS-06 |
