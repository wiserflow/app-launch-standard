# App Launch Standard

A project-agnostic standard for building, launching and improving an app or SaaS that looks and behaves like a mature company product — packaged as an [agent skill](https://skills.sh).

- **42 areas, 771 checklist items (467 launch blockers) plus 48 target-specific platform items**, each with a stable ID (`UXP-F2`, `ORG-27`, `EML-03`) and a level: **L1** launch blocker · **L2** within 30 days · **L3** at scale / enterprise.
- **What the user touches, specified in detail:** app shell and sidebar, profile and account settings, organizations, members, invites and a role × permission matrix, and ~125 concrete UX/UI rules (forms, tables, destructive actions, feedback, copy, motion, mobile) with decision tables and a 2-minute screen review protocol.
- **Everything around it:** auth, email lifecycle, billing, security, privacy, performance, observability, CI/CD, database, support, analytics, cost.
- **Any target:** web, PWA, native iOS/Android, desktop, CLI, browser/IDE extensions, chat bots, MCP servers, APIs/SDKs, add-ins and more (`areas/platforms.md`).
- **Greenfield or brownfield:** start a new app from a starter, or run a gap audit on an app already in production and adopt the rest piece by piece.
- **Lightweight spec flow** (`areas/spec-flow.md`): Ask → Spec → Tasks → Verify. Acceptance criteria are the standard's item IDs, so "improve the profile page" becomes `ACC-*`, `UXP-*`, `SHL-*` instead of a spec written from scratch.

Tools mentioned are suggestions; the requirement is the item.

## Install

```bash
npx skills add wiserflow/app-launch-standard
```

Then ask your agent things like:

- "Start a new app following the app launch standard."
- "Audit this app against the launch standard and list the missing L1 items."
- "Improve the profile page using the spec flow."
- "Review this screen with the UX patterns."

Without the skill CLI, copy this folder into your repo (e.g. `docs/launch/`) and point your agent at `SKILL.md`.

## Layout

| File | Content |
| --- | --- |
| `SKILL.md` | Entry point: kickoff questions, how to use, global map of areas |
| `RUNBOOK.md` | Launch runbook and operating cadence after launch |
| `areas/*.md` | One checklist per area — agents read only the areas in play |
| `TOOLING.md` | Skills and MCP servers per area and phase |
| `REFERENCES.md` | Reference repositories (boilerplates, checklists, OSS tools) |
| `scripts/` | `init.py` copies the kit into your repo and creates `docs/launch/STATUS.md`; `status.py` reports progress; `check.py` validates IDs, levels and quoted counts (runs in CI). Python 3, stdlib only |

## Contributing

Issues and PRs welcome. Keep item IDs stable (never renumber; deprecate instead), keep requirements verifiable with evidence, and reference existing IDs instead of duplicating them.

## License

[MIT](LICENSE)
