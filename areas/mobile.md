# Mobile, PWA and push (MOB)

Other targets (native, desktop, CLI, bots...) → platforms.md (PLAT)

Skip native items if the product is web-only; PWA/push items still apply.

| ID | L | Requirement |
| --- | --- | --- |
| MOB-01 | 1 | Store accounts (Apple Developer as organization, Play Console); bundle id and signing credentials managed by EAS/CI, not a laptop |
| MOB-02 | 1 | Privacy policy URL, **in-app account deletion**, Apple privacy labels and Play data-safety form match real data collection |
| MOB-03 | 1 | Reviewer demo account works; digital goods follow store IAP rules |
| MOB-04 | 1 | Push permission asked in context (not at first launch); tokens stored per device, pruned on `DeviceNotRegistered`/410 |
| MOB-05 | 1 | Universal/app links verified (`apple-app-site-association`, `assetlinks.json`); auth callback and reset links tested on a real device |
| MOB-06 | 1 | PWA installable (manifest, icons, HTTPS, offline fallback); VAPID private key only in server env |
| MOB-07 | 2 | OTA updates: channel per environment, `runtimeVersion` policy, staged rollout + rollback tested |
| MOB-08 | 2 | Crash/ANR reporting with source maps per build; forced-update / minimum-version gate |
| MOB-09 | 2 | Play closed testing satisfied before production track; TestFlight external group in use |
| MOB-10 | 3 | Build, submit, update from CI (EAS Workflows); phased release; localized store listings |

References: [Apple review guidelines](https://developer.apple.com/app-store/review/guidelines/) · [Expo submit to stores](https://docs.expo.dev/deploy/submit-to-app-stores/) · [Expo push](https://docs.expo.dev/push-notifications/overview/) · [web.dev PWA checklist](https://web.dev/articles/pwa-checklist) · [Play data safety](https://support.google.com/googleplay/android-developer/answer/9859455).
