# CI/CD (CI)

| ID | L | Requirement |
| --- | --- | --- |
| CI-01 | 1 | Default branch protected: PR required, required checks, no force-push |
| CI-02 | 1 | Every PR: typecheck, lint, unit tests, build (app build; image build per CI-17), migration check, dependency audit, with frozen lockfile |
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
| CI-16 | 1 | Trigger matrix applied and documented (→ table below): checks never push images; image built once per commit; staging deploy chained on green CI; prod promotes the staged image, never rebuilds; rollback = re-run prod deploy with a previous tag (→ CI-06); images are environment-agnostic: config is read at runtime per environment, nothing environment-specific baked at build (e.g. `VITE_*`/`NEXT_PUBLIC_*` → runtime `/config.json` or injected at container start), else the promoted image points prod at staging |
| CI-17 | 2 | CI cost policy: `concurrency` cancel-in-progress on check workflows (never on deploy jobs → CI-12 lock); docs-only changes skip CI (e.g. `paths-ignore: ['**.md', 'docs/**']`; required checks on a protected branch must still report, so use a no-op job or a path filter inside the job); no image build/push on branch pushes, a PR may do a local `push: false` build only when Dockerfile/dependency files change; heavy e2e runs against staging after deploy, not on every PR (→ TST); dependency and Docker layer caches (e.g. `cache-from/to: type=gha`) |
| CI-18 | 2 | Agent push policy written in the repo's agent instructions (CLAUDE.md/AGENTS.md, → SPEC-08): agents commit and push by default on lane/PR branches; agents ASK before pushing to the default branch when it deploys (staging) and before creating release tags; before any push, agents read the CI config (e.g. `.github/workflows/*`) to know what that push triggers |
| CI-19 | 1 | Images live in a registry under the app's org with a fixed naming scheme (e.g. GHCR `ghcr.io/<org>/<app>-<service>`); when the deploy workflow lives in another repo/org, the read credential it needs is documented (e.g. `GITHUB_TOKEN` cannot read another org's private package → token with `read:packages`) and stored as a deploy-environment secret (→ CI-04) |

Reference workflow templates (GitHub Actions is the worked example, not a mandate): `templates/github-actions/` (`ci.yml`, `deploy-staging.yml`, `deploy-prod.yml`).

## Trigger matrix

| Event | Runs | Image | Deploy |
| --- | --- | --- | --- |
| PR, push to any non-default branch | Checks only (CI-02) | None (local `push: false` build only if Dockerfile/deps changed, CI-17) | None |
| Merge/push to default branch, app has staging | Checks, then build | Build ONCE, tag `sha-<commit>`, push to registry | Staging, only after CI is green (chained on CI completion, e.g. `workflow_run`; never parallel with tests) |
| Release tag `vX.Y.Z` | Promote | Retag/manifest-copy the existing `sha-<commit>`; never rebuild; fail if that SHA was never built | Prod (approval + lock, CI-12) |
| App without staging: push/PR | Checks only | None | None |
| App without staging: tag | Checks, build | Build, tag `sha-<commit>` + version | Prod |
| Rollback | Manual dispatch, input = previous tag | Existing image | Prod (CI-06) |
