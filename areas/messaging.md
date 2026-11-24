# Messaging channels: WhatsApp, SMS (MSG)

For products that send/receive WhatsApp or SMS on behalf of customers.

| ID | L | Requirement |
| --- | --- | --- |
| MSG-01 | 1 | Production on the **official** WhatsApp Cloud API (or a BSP): verified Business Manager, approved display name, two-step PIN |
| MSG-02 | 1 | Webhooks verify `X-Hub-Signature-256`, return 200 fast, process via queue, dedupe by message id |
| MSG-03 | 1 | Opt-in recorded per contact (purpose, timestamp, source — privacy-law evidence); opt-out keywords honored immediately |
| MSG-04 | 1 | 24-hour window enforced in code; outside it only approved templates, category matching content |
| MSG-05 | 1 | System-user token with minimal scopes, stored as secret, never in a client; rotation plan |
| MSG-06 | 1 | Quality rating and messaging-tier limits monitored; alert on quality drop or paused template |
| MSG-07 | 2 | Cost per conversation/message logged per tenant (FIN-03) with per-tenant send caps |
| MSG-08 | 2 | Delivery/read/failed statuses persisted; retry on transient errors; fallback channel (SMS/email) for critical messages |
| MSG-09 | 2 | Media downloaded before URL expiry and stored in own bucket; inbound rate limit per contact |
| MSG-10 | 3 | Multi-number / multi-WABA per tenant (embedded signup), throughput tier upgrades, template-management UI |

Unofficial WhatsApp Web libraries (Baileys-based, e.g. Evolution API, `whatsapp-mcp`) carry ToS/ban risk and full message-history exposure → never on a customer's primary production number.

References: [WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api) · [Pricing](https://developers.facebook.com/docs/whatsapp/pricing) · [Messaging limits](https://developers.facebook.com/docs/whatsapp/messaging-limits) · [Message templates](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates).
