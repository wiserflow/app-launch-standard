# Infrastructure (INF)

Assumes self-managed VPS/container cluster behind a CDN/edge proxy (e.g. Cloudflare); adapt for managed platforms.

| ID | L | Requirement |
| --- | --- | --- |
| INF-01 | 1 | SSH key-only, root login off, password auth off |
| INF-02 | 1 | Firewall default-deny; only 80/443 public; SSH and cluster ports reachable only via private network/VPN |
| INF-03 | 1 | No DB, cache or admin port on a public interface — verified with an external `nmap` (Docker bypasses UFW) |
| INF-04 | 1 | Unattended security upgrades on every node |
| INF-05 | 1 | Containers run non-root; no app container mounts `/var/run/docker.sock` |
| INF-06 | 1 | Every service has a `HEALTHCHECK` and CPU/memory limits in the stack file |
| INF-07 | 1 | No secret in git, image layers or plain stack files: Swarm/K8s secrets, SOPS+age, or a secret manager (e.g. Infisical) |
| INF-08 | 1 | TLS everywhere with auto-renewal; end to end, edge-to-origin verified (e.g. Cloudflare Full (strict)); origin reachable only from the edge/tunnel |
| INF-09 | 2 | Base images minimal (multi-stage, slim/distroless) and pinned by digest; `hadolint` in CI |
| INF-10 | 2 | DNS: CAA records, DNSSEC; SPF/DKIM/DMARC on any sending domain |
| INF-11 | 2 | Odd number of cluster managers (3) and a node-loss drill done |
| INF-12 | 2 | Host audit: e.g. `lynis` + `docker-bench-security` run, findings triaged; hardening e.g. via `dev-sec/ansible-collection-hardening` |
| INF-13 | 3 | Servers reproducible from IaC (Terraform/OpenTofu + Ansible); secret rotation documented |
