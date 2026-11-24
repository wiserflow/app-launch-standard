# Spec flow for changes (SPEC)

Turns "I want to improve X in my app" into a short spec, a few slices and a verified result. The acceptance criteria are item IDs from this standard, so you don't rewrite them for every change. It is NOT product discovery or the launch PRD (`product.md`, PRD), the business rules register (`domain.md`, DOM), or the UX rules themselves (`ux-patterns.md`, UXP). It is the lightweight path that applies them to one change, in a brownfield app first.

Applicability: this file governs HOW changes are made, not what the app must be. During a pure audit (Kickoff goal = audit) mark SPEC-* n/a with that reason; it applies once changes start.

## Size rule (decide before step 1)

| Size | Signal | Artifacts |
| --- | --- | --- |
| Tiny | ≤ 2 files, no new screen, behavior, rule or schema; easy to revert (copy, spacing, an obvious bug) | None. The commit cites any IDs it closes |
| Small | 1 screen or ≤ ~3 files, one session (~500 LOC), no one-way door | 1 file: `docs/specs/<yyyy-mm-dd>-<slug>.md` (spec + tasks sections) |
| Feature | New screen or pattern, more than one layer, or more than one session | Folder `docs/specs/<yyyy-mm-dd>-<slug>/` with `spec.md`, `tasks.md`, `evidence/` |

A one-way door is a schema migration, data deletion, an auth or permission change, billing, or the public API. A change with one is never Tiny.

## The 4 steps

| # | Step | Output | Done when |
| --- | --- | --- | --- |
| 1 | **Ask**: the agent reads the affected code and captures the current screens, then asks product questions one at a time, each with a recommendation | `## Request` (user's words, verbatim) + `## Current behavior` with "before" screenshots | No open question left that changes scope |
| 2 | **Spec**: a delta against the current behavior, with acceptance criteria picked from the standard | `spec.md` (template below) | The user approves it once. `Status: approved <date>` |
| 3 | **Tasks**: vertical slices. S1 is thin and end-to-end, one commit per slice, each slice cites the IDs it closes | `tasks.md` ticked while building | All slices ticked |
| 4 | **Verify**: a fresh reviewer who did not write the code checks every acceptance row against evidence | Evidence column filled. Verdict `verified` / `partial` / `failed` | `verified`. `partial` adds slices and repeats 3→4. `failed` goes back to 2 |

## The standard is the requirements library

Map what the change touches to the areas below, then copy the **ID + a few words**, never the full text. The area file stays the source of truth. Write local criteria (`LOC-n`, Given/When/Then) only where no ID fits.

| Change touches | Pull criteria from |
| --- | --- |
| Any screen | UXP screen review protocol (15 questions), DES-09, A11Y-* |
| Profile, preferences, personal security | ACC-*, SHL-47..51, UXP-A* |
| Sidebar, menus, top bar, org switcher, error pages | SHL-*, UXP-N* |
| Forms / lists and tables / deletes | UXP-F*, UXP-V* / UXP-G*, UXP-S*, UXP-E* / UXP-D* |
| Members, invites, roles | ORG-*, SEC-03, API-05 |
| A business rule or state | DOM-* (register entry before code → DOM-23) |
| Plans, limits, upgrade | BIL-*, FIN-07, SHL-35..38 |
| Another target (mobile, desktop, extension) | PLAT-*, MOB-* |
| An email or notification | EML-*, ACC-29..32 |

## Templates

`spec.md` (a Small change uses this plus a `## Tasks` section in the same file):

```markdown
# <Title>
Size: small | feature · Status: draft | approved <date> | done <date> · PR: <link>

## Request (verbatim)
> <user's words>

## Current behavior (observed)
- <what it does today> (evidence/before-375.png)

## Delta
- ADDED: <new behavior>
- MODIFIED: <old> → <new>
- REMOVED: <behavior dropped; what happens to existing data>
- Out of scope: <named, so it is not done by accident>

## Acceptance (from the standard)
| ID | Applies as | Evidence |
| --- | --- | --- |
| <AREA-NN> | <a few words> | <test name / screenshot path / URL> |

## Local criteria (gaps only)
- LOC-1: Given <state>, When <action>, Then <result>

## Decisions
- <question> → <answer> (user, <date>)
- Pattern break: <what> because <why> (ADR link if it lasts)

## Verdict
<verified | partial | failed> · reviewer: <fresh agent / person> · <date>
```

`tasks.md`:

```markdown
# Tasks: <slug>
- [ ] S1 <thin end-to-end slice> (closes <IDs>) · commit <sha>
- [ ] S2 ...
- [ ] Verify: fresh reviewer, verdict recorded in spec.md
```

## Worked example: "improve the profile page" (brownfield)

**Ask.** The agent reads `/account/profile` and captures it at 375 and 1280 px. What it finds today: one page-wide form with a single Save; the avatar is a URL text field and shows a broken image when empty; a new display name shows in the user menu only after a reload; nothing warns before losing unsaved edits. Question: "Does the product use @mentions? I recommend no handle for now." Answer: no, so ACC-07 is out. Size: **Feature** (new upload endpoint, storage, UI).

**Delta.**
- MODIFIED: one page-wide form → section cards, each with its own Save
- MODIFIED: avatar URL field → upload with crop, remove and initials fallback
- MODIFIED: display name change → visible in the shell right away
- ADDED: leave-page guard; loading, error and saved states
- REMOVED: avatar URL field. Existing URLs keep showing until the user replaces them
- Out of scope: email and password change (ACC-09..14), which get their own spec

**Acceptance.** ACC-02 · ACC-03 · ACC-04 · ACC-05 · ACC-06 · ACC-45 · ACC-47 · SHL-21 · SHL-48 · SHL-49 · UXP-A2 · UXP-F8 · UXP-F10 · UXP-V2 · the UXP screen review protocol on the page. One local gap: **LOC-1** Given a user whose legacy avatar URL returns 404, When the profile loads, Then the initials fallback shows and there is no broken image.

**Tasks.** S1 display-name card with its own Save, shell refresh and guard (ACC-06, SHL-49, UXP-F8) · S2 upload endpoint with content sniffing, re-encode, EXIF strip and an owner-only test (ACC-05, ACC-45) · S3 crop, remove and fallback UI (ACC-04, UXP-F10, LOC-1) · S4 states at 375/768/1280 (ACC-47, UXP-E1).

**Verify.** The first verdict is `partial` (ACC-05 has no 50 MB file test). S5 adds it, the reviewer runs again and the verdict is `verified`.

## Running it with an AI agent

| Step | Type this |
| --- | --- |
| Ask | "Spec flow: I want to improve <screen/area>. Read `docs/launch/areas/spec-flow.md` and the areas it maps to, look at the current code and screens, then ask me questions one at a time with your recommendation. No code yet." |
| Spec | "Write the spec. Size it by the size rule; acceptance = standard IDs, LOC only for gaps." |
| Tasks | "Approved. Write the tasks and implement them slice by slice, one commit each, citing IDs." |
| Verify | "Verify with a fresh reviewer that didn't write the code: evidence for every acceptance row, then the verdict." |
| Tiny | "Tiny change, no spec: <change>. Cite any IDs in the commit." |

Agent rules:
- Save the request verbatim first, so it survives context compaction.
- Follow the repo's existing conventions, and record any deliberate pattern break with its reason.
- Approval covers local edits and commits only. Push and deploy follow the repo's own rules.

## Evidence and archive

- Evidence goes into the spec's Evidence column: a test name, a path under `evidence/` (screenshots from the screen review capture), a URL, or command output. "Deployed" does not count.
- When the verdict is `verified`, set `Status: done <date>` and add the PR link. Add one line to `docs/specs/README.md` (date, slug, size, status, PR).
- The folder is not moved, so links in PRs keep working, and the dated names already sort by time. After done, the code, its tests and the area files are the truth; the spec is history.
- Before closing the PR, move anything that lasts out of the spec. See SPEC-07.

## What we borrowed / what we left out

| Framework | Borrowed | Left out |
| --- | --- | --- |
| GitHub Spec Kit | Prioritized stories with Given/When/Then (our LOC); bug triad verdict `verified`/`partial`/`failed`; the converge loop; entry points are independent | `specify` CLI (Python + uv) and `.specify/`; the 6+ step pipeline per feature; 170-350 line prompts; extensions, presets and catalogs; numbered per-feature branches |
| BMAD Method | Smallest process that fits (one session ~500 LOC); brownfield: investigate the code first, follow its conventions, record pattern breaks; UX step only when screens or patterns change | Persona agents; PRD, brief and epic/story ceremony; installer and Python tooling; the elicit-only UX stance (we use opinionated UXP rules instead) |
| Superpowers | Small change agreed in chat with no document; one question at a time; evidence before claiming done | A hard gate on every change; plans of 2-5 minute tasks; per-task subagent with two-stage review; mandatory TDD |
| OpenSpec | Delta spec (ADDED/MODIFIED/REMOVED) for only the slice you touch; read the area first (explore); no phase gates | CLI and `openspec/` tree; 4 artifacts per change; archive and merge machinery; SHALL prose |
| TLC (spec-driven / spec-lean) | Plan → Build → Review with one human approval; auto-sizing; request saved verbatim; vertical slices with one commit each; a fresh reviewer; "before" captures; approval allows local commits only | EARS and requirement IDs of its own; a proof per criterion and Python gate scripts; quoted-approval lines; always-on Verifier and lessons system |

None of the five ships opinionated UX/UI, app shell or roles criteria. BMAD's `bmad-ux` comes closest: it asks for your vision but gives no rules. Here those criteria are ACC, SHL, ORG and UXP, and a spec only cites them.

| ID | L | Requirement |
| --- | --- | --- |
| SPEC-01 | 1 | `docs/specs/` exists with a `README.md` index (date, slug, size, status, PR) and the two templates above. A PR that is not Tiny links its spec (→ PRD-06) |
| SPEC-02 | 1 | Each spec has the request verbatim, the observed current behavior (a "before" screenshot when a screen changes), and a Delta with ADDED/MODIFIED/REMOVED and Out of scope |
| SPEC-03 | 1 | Acceptance rows are standard item IDs picked with the mapping table. `LOC-n` Given/When/Then appears only for gaps. A spec with zero IDs states why no area applies |
| SPEC-04 | 1 | Size follows the size rule (a one-way door is never Tiny). `Status: approved <date>` comes before the first code commit of the change (check it in git log) |
| SPEC-05 | 1 | Verify is run by a reviewer who did not write the code. Every acceptance row has evidence (test name, screenshot path, URL). The verdict is recorded, and only `verified` sets `Status: done` |
| SPEC-06 | 2 | Tasks are vertical slices with S1 end-to-end. One commit per slice, and the commit message cites the IDs it closes |
| SPEC-07 | 2 | On done: closed IDs are marked in `docs/launch/STATUS.md` with the spec as evidence (→ SCF-10); lasting decisions go to `docs/decisions/`; rule changes go to `docs/domain/rules.md` (→ DOM-21); user-visible changes go in the changelog (→ SUP-03) |
| SPEC-08 | 2 | The repo's agent instructions (CLAUDE.md / AGENTS.md) carry the size rule and point to this file, so "improve X" starts step 1 instead of jumping to code |

References: [OpenSpec (delta specs, brownfield)](https://github.com/Fission-AI/OpenSpec) · [GitHub Spec Kit](https://github.com/github/spec-kit) · [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) · [tech-leads-club agent-skills (tlc-spec-lean)](https://github.com/tech-leads-club/agent-skills)
