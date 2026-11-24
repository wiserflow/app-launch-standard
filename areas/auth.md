# Identity and accounts (AUTH)

| ID | L | Requirement |
| --- | --- | --- |
| AUTH-01 | 1 | Email + password signup, email verification, password reset, password-changed confirmation; password policy per NIST SP 800-63B-4: min length 15 when the password is the only factor (so always 15 until 2FA exists, AUTH-07), min 8 only when it is used together with MFA; allow ≥ 64 and paste; checked against a breached/common-password blocklist; no composition rules; no forced periodic rotation |
| AUTH-02 | 1 | Terms acceptance stored with `terms_version` and timestamp |
| AUTH-03 | 1 | Rate limit on login/signup/reset (→ SEC-04 for the general limits) |
| AUTH-04 | 1 | New-device login email |
| AUTH-05 | 1 | Session cookies `HttpOnly`, `Secure`, `SameSite`; session expiry; revoke on password change (→ ACC-13) |
| AUTH-06 | 2 | Social login (Google at minimum) |
| AUTH-07 | 2 | 2FA TOTP + recovery codes; enforceable per organization |
| AUTH-08 | 2 | Magic link |
| AUTH-09 | 2 | Active sessions list with revoke |
| AUTH-10 | 2 | Passkeys (WebAuthn) offered as a sign-in method, including synced passkeys (NIST SP 800-63B-4); register, list and remove from account settings; password/recovery fallback remains |
| AUTH-11 | 3 | Enterprise SSO (SAML/OIDC) + SCIM provisioning |
| AUTH-12 | 2 | Bot protection on login/signup/reset (e.g. Turnstile, hCaptcha); wired in code and on in production, may be off locally without keys |
