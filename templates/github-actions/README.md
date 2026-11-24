# GitHub Actions templates

Reference workflows for the launch standard. Copy to `.github/workflows/` and replace the `PLACEHOLDER` markers.

## Flow

PR/push -> `ci.yml` (checks only) -> green on `main` -> `deploy-staging.yml` (build once as `sha-<commit>`, deploy) -> tag `vX.Y.Z` -> `deploy-prod.yml` (verify, approval, retag, deploy).

## Placeholders

- `ORG` (lowercase), `APP`: images are `ghcr.io/<ORG>/<APP>-<service>`.
- `SERVICES`: matrix list in `ci.yml` and `deploy-staging.yml`, string in `deploy-prod.yml`. Keep all three in sync.
- Dockerfile path (`docker/Dockerfile.<service>`) and lockfile name in the `ci.yml` paths filter.
- Stack block in `ci.yml` (runtime, cache, install, check commands; bun is only the example).
- Deploy steps (ssh + script is an example; swap for compose pull, `docker service update`, etc.).

## Secrets and vars

| Name | Kind | Where |
| --- | --- | --- |
| `STAGING_SSH_KEY`, `STAGING_KNOWN_HOSTS`, `STAGING_HOST`, `STAGING_USER` | secret | environment `staging` |
| `PROD_SSH_KEY`, `PROD_KNOWN_HOSTS`, `PROD_HOST`, `PROD_USER` | secret | environment `production` |
| `STAGING_HEALTH_URL`, `PROD_HEALTH_URL` | variable | respective environment |

Create environments `staging` and `production`; add required reviewers to `production`.

## Without staging

Delete `deploy-staging.yml`. In `deploy-prod.yml`, replace the gate and promote steps with a `docker/build-push-action` matrix job at the tag checkout, pushing `:vX.Y.Z` and `:prod`. Keep the environment, concurrency and smoke test. The image is then built once, at the tag, with no earlier validation, so lean harder on CI and the approval gate.

## Cross-org deploy

If the deploy workflow lives in another repo or org, its `GITHUB_TOKEN` cannot read the other org's private packages. Create a token with `read:packages` and store it as an environment secret (staging/production); use it in `docker/login-action` instead of `GITHUB_TOKEN`.

## Requirement map

| ID | Where |
| --- | --- |
| CI-02 | `ci.yml`: typecheck, lint, unit tests, migration check, dependency audit, frozen lockfile |
| CI-03 | Deploys use the immutable `sha-<commit>` image (prod: its `vX.Y.Z` retag), never `latest` |
| CI-04 | `permissions` least privilege per workflow/job; deploy secrets live in the `staging` / `production` environments |
| CI-06 | Rollback = run `deploy-prod.yml` via `workflow_dispatch` with the previous tag |
| CI-08 | Smoke test step after each deploy |
| CI-09 | Actions on major tags here; pin to SHA before production use |
| CI-12 | `environment: production` (required reviewers; retag happens only after approval); deploy `concurrency` with `cancel-in-progress: false` |
| CI-16 | Trigger matrix: CI on PR and push; staging on `workflow_run` from `main`; prod promotes on tag or manual; missing `sha-<commit>` fails |
| CI-17 | Cost: `paths-ignore`, CI concurrency cancel, docker build only on Dockerfile/lockfile change, gha cache |
| CI-19 | Registry: GHCR `ghcr.io/<org>/<app>-<service>`, immutable `sha-<commit>` plus `vX.Y.Z` and `prod` |

Promotion only works if images are environment-agnostic (CI-16): read config at runtime per environment; never bake environment values at build (e.g. `VITE_*`/`NEXT_PUBLIC_*`), or the promoted image points prod at staging.

If the `ci.yml` checks are required on a protected branch, runs skipped by `paths-ignore` block merges: do not make them required, or filter inside the job.
