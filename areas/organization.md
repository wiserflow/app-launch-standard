# Organizations, members and roles (ORG)

Everything about the tenant: the organization object, who belongs to it, what each role may do, and how that is enforced and audited. Supersedes the one-line ADM-01. NOT here: the org switcher UI (→ `app-shell.md`), personal profile and settings (→ `account.md`), the internal backoffice (→ `owner-console.md`), plan pricing (→ `billing.md`).

## Decision to record (ORG-01)

| Model | When | Consequence |
| --- | --- | --- |
| Personal workspace + optional team orgs | Individuals are a real segment | Signup creates a personal org (1 member, no invites); "upgrade to team" is the same object, not a migration |
| Team org only | B2B, collaboration is the product | Signup creates the first org with the user as Owner |

Either way: a user can belong to many orgs, every resource row carries the org id (→ ARC-03), and no UI or API path exists without an active org context.

## Role x permission matrix (template every app fills in)

Rows are the app's own permissions (add domain ones); the columns are the default roles. "own" = only resources the user created.

| Permission | Owner | Admin | Member | Viewer/Guest | Billing |
| --- | --- | --- | --- | --- | --- |
| View org resources | yes | yes | yes | yes | no |
| Create/edit resources | yes | yes | yes | no | no |
| Delete resources | yes | yes | own | no | no |
| Invite/remove members, change roles (never Owner) | yes | yes | no | no | no |
| Manage org settings, security policies | yes | yes | no | no | no |
| View audit log | yes | yes | no | no | no |
| View/manage billing, invoices, plan | yes | no | no | no | yes |
| Manage integrations, API keys | yes | yes | no | no | no |
| Transfer ownership, delete org | yes | no | no | no | no |

## Org object and lifecycle

| ID | L | Requirement |
| --- | --- | --- |
| ORG-01 | 1 | Workspace model decision (personal+team vs team-only) written in the repo, linked to the tenancy strategy (→ ARC-03) |
| ORG-02 | 1 | Org has name, unique URL-safe slug (reserved words and rename redirect → SHL-26), optional logo (type/size validated, resized server-side), default locale and time zone used for new members and emails; per-user overrides win (→ I18N-02, I18N-08) |
| ORG-03 | 1 | A user can belong to multiple orgs; active org is explicit (URL or session); switch behavior and zero-bleed test → SHL-25 |
| ORG-04 | 1 | Create-org flow: name and slug with live availability check, creator becomes Owner, lands in the new org's onboarding checklist (→ ONB-03) |
| ORG-05 | 1 | Org settings page (name, slug, logo, locale, time zone) editable by Owner/Admin only; slug change keeps the old URL redirecting (→ SHL-26) and warns that bookmarks and integrations change |
| ORG-06 | 1 | Ownership transfer: Owner picks an existing member, target must accept (email + in-app), pending transfer is cancelable and expires; old Owner becomes Admin; audited |
| ORG-07 | 1 | Last-owner protection: the sole Owner cannot leave, be removed, be demoted or have their account deleted (UI disables with explanation; server rejects, tested). An org always has at least 1 Owner |
| ORG-08 | 1 | Org deletion: Owner only, re-auth + type-the-org-name confirmation, data export offered first (→ LGL-03), subscription canceled at period end (→ BIL-01), grace period before purge with a restore link (→ LGL-04), all members emailed |
| ORG-09 | 3 | Verified domains: Owner proves DNS ownership (TXT record); users signing up with a verified-domain email can auto-join (fixed role Member/Viewer, or request-to-join) per org toggle |
| ORG-10 | 3 | Data region shown in org settings when the product offers a choice (read-only after creation) |

## Members and invitations

| ID | L | Requirement |
| --- | --- | --- |
| ORG-11 | 1 | Members list: avatar, name, email, role, status (active, invited, suspended), joined date, last active; search by name/email, filter by role and status, sortable, paginated (table patterns → UXP-G*, UXP-S*) |
| ORG-12 | 2 | Members list shows 2FA status per member to Owner/Admin (→ AUTH-07) with a "no 2FA" filter |
| ORG-13 | 1 | Invite by email with role selection; a role above the inviter's own cannot be granted (server-checked); multiple emails at once with per-address result (sent, already member, invalid) |
| ORG-14 | 1 | Seat limit checked before sending and before accepting; at the limit the invite UI explains and links to upgrade, never fails silently (→ FIN-07, BIL-10) |
| ORG-15 | 1 | Pending invitations list: email, role, inviter, sent date, expiry; actions resend (rate limited) and revoke; revoked/expired links show a clear page, not a 404 |
| ORG-16 | 1 | Invite tokens: single-use, 128-bit+ random, stored hashed, default expiry 7 days, bound to the invited email; email content per EML-T5 |
| ORG-17 | 1 | Accept flow, existing user: link opens login, then a confirm screen ("Join Acme as Member") with accept or decline. New user: signup prefilled with the invited email, email counted as verified, then joins. Both land inside the org, not a generic home |
| ORG-18 | 1 | Invite to wrong email: accepting while signed in as another address shows "this invite is for x@..., you are y@..." with switch-account; the token never joins a mismatched account silently; Owner/Admin can revoke and reissue |
| ORG-19 | 2 | Optional shareable invite link: fixed role (default Member, never above), expiry, max uses, one-click disable and regenerate; off by default per org |
| ORG-20 | 1 | Declining notifies the inviter in-app (→ SUP-04); expired invites can be reissued in one click |
| ORG-21 | 1 | Change a member's role: Owner/Admin only, confirmation shows what access changes, member notified, effective on the next request (no re-login), audited |
| ORG-22 | 1 | Remove member: confirmation names the consequences; that member's sessions and API tokens for this org are revoked immediately |
| ORG-23 | 1 | Data of a removed member: resources they own are reassigned (default to the remover or a chosen member), never orphaned or deleted; private items follow a documented rule; authorship stays shown as "former member" |
| ORG-24 | 2 | Suspend/deactivate member: blocks access, keeps data and history, reversible in one click; seat counted or freed per documented rule (→ FIN-07); suspended user sees "access suspended, contact your admin" |
| ORG-25 | 1 | Member can leave an org from their own settings (not the last Owner, ORG-07); their resources follow ORG-23 |
| ORG-26 | 2 | Guest/external collaborators: separate role scoped to explicitly shared items only, no member directory, no org settings, seat treatment documented, badged "Guest" wherever shown |

## Roles and permissions

| ID | L | Requirement |
| --- | --- | --- |
| ORG-27 | 1 | The role x permission matrix above is filled in for the app (domain permissions added) and stored in the repo; each role and permission has a one-line description shown in the UI |
| ORG-28 | 1 | Default roles shipped: Owner, Admin, Member, Viewer/Guest, Billing (drop one only with a recorded reason); Admin cannot assign or edit Owner |
| ORG-29 | 1 | Permissions enforced server-side on every route and query through one central policy function (→ SEC-03, API-05); hiding in the UI is never the control |
| ORG-30 | 1 | UI mirrors the matrix: hide vs disable per SHL-33 and UXP-B5 (disabled states name the required role); a direct URL to a forbidden page → SHL-30 |
| ORG-31 | 1 | Authorization reads the current membership row, not claims cached in a long-lived token; a role change or removal takes effect within 1 minute at most |
| ORG-32 | 3 | Custom roles: Owner composes permissions from the app's list, can clone a default, sees member count per role; a role in use cannot be deleted without reassigning |
| ORG-33 | 2 | Teams/groups inside an org (members, optional lead); resource access granted to a group; adding or removing a member updates access immediately |
| ORG-34 | 3 | Resource-level sharing (per project/folder) layered on org roles, with an "effective access" view explaining why a user can see an item |

## Security policies per org

| ID | L | Requirement |
| --- | --- | --- |
| ORG-35 | 2 | Owner can require 2FA for all members; non-compliant members get a grace period, then are forced to enroll at next login (→ AUTH-07); list of non-compliant members visible |
| ORG-36 | 3 | Session length policy per org, applied to existing sessions (→ AUTH-05, AUTH-09) |
| ORG-37 | 3 | Allowed login methods per org (password, Google, SSO only); Owner cannot lock themselves out (break-glass recovery documented and tested) |
| ORG-38 | 3 | IP allowlist per org with a "your IP" check before saving; covers API tokens too |
| ORG-39 | 3 | SSO enforcement and SCIM provisioning/deprovisioning map to org roles and the removal rules ORG-22/ORG-23 (→ AUTH-11) |

## Audit log

| ID | L | Requirement |
| --- | --- | --- |
| ORG-40 | 1 | These events are always written to the customer audit log (→ ADM-02) with actor, target, before/after, IP, time: org created/renamed/slug changed/deleted/restored; ownership transfer requested/accepted/canceled; member invited/accepted/declined/revoked/resent; member removed/left/suspended/reactivated; role changed; custom role created/edited/deleted; security policy changed (2FA, session, login methods, IP list, SSO/SCIM); invite link created/disabled; domain verified/removed; billing contact or plan changed; API key created/revoked |
| ORG-41 | 1 | Audit entries are append-only, not editable by any customer role, and survive member removal (actor kept as name/email snapshot) |
| ORG-42 | 2 | Sensitive org actions (delete org, transfer ownership, change security policy, remove an Admin) require recent re-authentication (sudo → ACC-35) and email all Owners |

## Tests

| ID | L | Requirement |
| --- | --- | --- |
| ORG-43 | 1 | Tenant isolation tests: user of org A calls every list/detail/update/delete/export endpoint with ids from org B and gets 403/404 with no data or existence leak; same for search, files, webhooks, background jobs and cache keys (→ API-05) |
| ORG-44 | 1 | Role escalation negative tests: Member/Viewer/Billing calling each Admin/Owner endpoint is denied; Admin cannot grant or edit Owner; user cannot change own role; crafted body fields (`role`, `org_id`, `owner_id`) are ignored or rejected (→ SEC-06) |
| ORG-45 | 1 | Invite abuse tests: reused, expired, revoked and wrong-email tokens fail; a token for org A cannot join org B; seat limit cannot be bypassed by parallel accepts |
| ORG-46 | 1 | Matrix test generated from the matrix file: every role x permission pair asserts the expected allow/deny at API level; a new route without a policy entry fails CI |
| ORG-47 | 2 | Lifecycle tests: leave/demote/remove of last Owner rejected, concurrent ownership transfers resolve to one Owner, deleted-org data is unreachable and the purge job runs after the grace period |

References: `auth.md` (AUTH-07, AUTH-11), `admin.md` (ADM-02), `api.md` (API-05).
