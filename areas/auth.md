# Identity and accounts (AUTH)

| ID | L | Requirement |
| --- | --- | --- |
| AUTH-01 | 1 | Email + password signup, email verification, password reset, password-changed confirmation |
| AUTH-02 | 1 | Terms acceptance stored with `terms_version` and timestamp |
| AUTH-03 | 1 | Rate limit on login/signup/reset + bot protection (Turnstile/hCaptcha) |
| AUTH-04 | 1 | New-device login email |
| AUTH-05 | 1 | Session cookies `HttpOnly`, `Secure`, `SameSite`; session expiry + revoke on password change |
| AUTH-06 | 2 | Social login (Google at minimum) |
| AUTH-07 | 2 | 2FA TOTP + recovery codes; enforceable per organization |
| AUTH-08 | 2 | Magic link |
| AUTH-09 | 2 | Active sessions list with revoke |
| AUTH-10 | 3 | Passkeys |
| AUTH-11 | 3 | Enterprise SSO (SAML/OIDC) + SCIM provisioning |
