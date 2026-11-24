# CI/CD (CI)

| ID | L | Requirement |
| --- | --- | --- |
| CI-01 | 1 | Default branch protected: PR required, required checks, no force-push |
| CI-02 | 1 | Every PR: typecheck, lint, unit tests, build, migration check, dependency audit, with frozen lockfile |
| CI-03 | 1 | Deploy only from the pipeline, from an immutable image tagged by commit SHA (never `latest`) |
| CI-04 | 1 | Workflows declare least-privilege `permissions:`; secrets only in GitHub environments; no `pull_request_target` with untrusted checkout |
| CI-05 | 1 | Rolling deploy gated by healthcheck with automatic rollback (Swarm: `update_config` `order: start-first`, `failure_action: rollback`) |
| CI-06 | 1 | Rollback is one documented command, tested once |
| CI-07 | 1 | Migrations run as an explicit step before new code and are backward compatible with the previous version |
| CI-08 | 1 | Post-deploy smoke test on a real endpoint; deploy recorded as an error-tracker release |
| CI-09 | 2 | Third-party actions pinned by SHA; `actionlint` + `zizmor` in CI |
| CI-10 | 2 | Renovate/Dependabot for packages, base images and actions |
| CI-11 | 2 | Image scan (Trivy/Grype) blocks fixable critical/high; secret scanning (gitleaks) + push protection on |
| CI-12 | 2 | Production environment requires approval; deploy job has a concurrency lock |
| CI-13 | 2 | Versioning + changelog automated (release-please, changesets or git-cliff) |
| CI-14 | 3 | SBOM (syft) + signature/provenance (cosign, `attest-build-provenance`); OpenSSF Scorecard |
| CI-15 | 3 | Preview environment per PR; blue/green or canary for risky changes; DORA metrics tracked |
