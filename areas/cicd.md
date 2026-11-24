# CI/CD (CI)

| ID | L | Requirement |
| --- | --- | --- |
| CI-01 | 1 | Default branch protected: PR required, required checks, no force-push |
| CI-02 | 1 | Every PR: typecheck, lint, unit tests, build, migration check, dependency audit, with frozen lockfile |
| CI-03 | 1 | Deploy only from the pipeline, from an immutable image tagged by commit SHA (never `latest`) |
| CI-04 | 1 | Pipeline jobs run with least-privilege tokens/permissions; secrets scoped to the deploy environment only; untrusted PR code never runs with secrets (e.g. GitHub `permissions:` + environments, no `pull_request_target` with untrusted checkout) |
| CI-05 | 1 | Rolling/blue-green deploy gated by healthcheck with automatic rollback (e.g. Swarm `update_config` `order: start-first`, `failure_action: rollback`; Kubernetes readiness + `maxUnavailable: 0`) |
| CI-06 | 1 | Rollback is triggerable as one command/job from the pipeline (procedure and rehearsal → OPS-04) |
| CI-07 | 1 | Migrations run as an explicit step before new code and are backward compatible with the previous version |
| CI-08 | 1 | Post-deploy smoke test on a real endpoint; deploy recorded as an error-tracker release |
| CI-09 | 2 | Third-party CI actions/plugins pinned by immutable ref (e.g. SHA); pipeline definitions linted in CI (e.g. `actionlint`, `zizmor`) |
| CI-10 | 2 | Automated updates also cover base images and CI actions, with grouped/auto-merge policy for low-risk bumps (baseline → SEC-07) |
| CI-11 | 2 | Image scan (e.g. Trivy, Grype) blocks fixable critical/high; secret scanning baseline → SEC-07, plus push protection on |
| CI-12 | 2 | Production environment requires approval; deploy job has a concurrency lock |
| CI-13 | 2 | Versioning + changelog automated (e.g. release-please, changesets, git-cliff) |
| CI-14 | 3 | SBOM + signature/provenance for artifacts (e.g. syft, cosign, `attest-build-provenance`); OpenSSF Scorecard |
| CI-15 | 3 | Preview environment per PR; blue/green or canary for risky changes; DORA → ENG-05 |
