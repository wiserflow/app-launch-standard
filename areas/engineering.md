# Engineering process (ENG)

| ID | L | Requirement |
| --- | --- | --- |
| ENG-01 | 1 | Main protected; every change via PR with CI green and ≥1 review (human or agent) before merge (CI-01) |
| ENG-02 | 1 | Written **definition of done**: tests, verified as a user, docs/changelog, flag or rollback plan, no open placeholder |
| ENG-03 | 1 | PR template: what, why, how tested, risk/rollback; conventional commits enforced (e.g. commitlint) |
| ENG-04 | 1 | Open dependencies tracked in one file (`docs/PENDING.md`) with ids, closed at session end |
| ENG-05 | 2 | DORA four keys tracked: deploy frequency, lead time, change-fail rate, time to restore |
| ENG-06 | 2 | Blameless postmortems in the repo with tracked action items (OPS-06) |
| ENG-07 | 2 | Work shaped before building (appetite, scope, no-gos); small PRs (< ~400 lines) as the norm; automated review on every PR |
| ENG-08 | 3 | Engineering handbook in the repo (onboarding, on-call, release, review norms); CODEOWNERS |
| ENG-09 | 3 | Error budgets/SLOs gate feature work vs reliability work (OBS-09) |

References: [Google eng practices — code review](https://google.github.io/eng-practices/review/) · [GitLab engineering handbook](https://handbook.gitlab.com/handbook/engineering/) · [PostHog handbook](https://posthog.com/handbook) · [Shape Up](https://basecamp.com/shapeup) · [DORA four keys](https://dora.dev/guides/dora-metrics-four-keys/) · [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
