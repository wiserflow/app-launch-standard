# Marketing site (WEB)

| ID | L | Requirement |
| --- | --- | --- |
| WEB-01 | 1 | Landing: hero, problem, solution, how it works, social proof, primary CTA, FAQ. Social proof n/a before launch (no customers yet); missing sub-items are listed in the audit note |
| WEB-02 | 1 | Pricing page: plan comparison, limits, billing FAQ, annual vs monthly if offered |
| WEB-03 | 1 | Terms, privacy, data-deletion pages linked in footer, with version (date or semver) + effective date. May live in the app if the site footer links to them. Data deletion: dedicated page or clearly titled section in the privacy policy |
| WEB-04 | 1 | Custom 404 (and 500 where the host allows) |
| WEB-05 | 1 | Technical SEO: unique `<title>` + meta description per page, canonical, `sitemap.xml`, `robots.txt`, OG/Twitter image 1200×630, `og:locale`, `lang` attr |
| WEB-06 | 1 | Site hosted separately from the app cluster (static/CDN), so an app outage does not take marketing down |
| WEB-07 | 1 | Meets PERF-F* budgets on the marketing site's key pages (→ PERF-F1..F7; record the result there, do not re-count) |
| WEB-08 | 2 | Structured data JSON-LD: `Organization`, `SoftwareApplication`, `FAQPage`, `Product`/`Offer` on pricing |
| WEB-09 | 2 | Blog/content collection for SEO; comparison and use-case pages |
| WEB-10 | 2 | Waitlist/beta form with notification email |
| WEB-11 | 2 | Site analytics: cookieless (Umami/Plausible) or consent-gated (see LGL-05) |
| WEB-12 | 3 | Trust/security page: data location, encryption, backups, subprocessors, `/.well-known/security.txt` |
| WEB-13 | 2 | Public status page linked in footer (see OPS-05) |
