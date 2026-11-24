# Architecture and decisions (ARC)

Decision records go to the repo's decisions folder (default `docs/decisions/YYYY-MM-DD-<slug>.md`; an existing equivalent folder or table counts) using MADR fields (context, options, decision, consequences).

| ID | L | Requirement |
| --- | --- | --- |
| ARC-01 | 1 | ADRs for datastore, auth, tenancy model (one person per account: per-owner filtering; team accounts: org/tenant isolation), hosting, queue, payment provider |
| ARC-02 | 1 | C4 level 1–2 diagrams (context, containers) as code (Mermaid/LikeC4) in the repo |
| ARC-03 | 1 | Ownership/tenancy strategy written (per-owner filtering for one person per account; tenant isolation for team accounts only) and enforced at one layer, e.g. app-level check or RLS, not scattered per route (see SEC-02, DB-05) |
| ARC-04 | 1 | Every external dependency has a documented failure mode (timeout, retry, fallback), kept as an inventory table: dependency / failure mode / fallback (see OPS-07) |
| ARC-05 | 1 | Data-flow diagram marks where PII is stored and where it leaves the system (feeds LGL-07) |
| ARC-06 | 2 | ADR status maintained (accepted/superseded); PR template asks for an ADR on cross-cutting changes |
| ARC-07 | 2 | Capacity assumptions (req/s, rows, queue depth) and first expected bottleneck documented |
| ARC-08 | 3 | C4 level 3 for critical containers; architecture fitness checks in CI (e.g. dependency-cruiser boundaries) |

References: [MADR](https://adr.github.io/madr/) · [C4 model](https://c4model.com/) · [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record).
