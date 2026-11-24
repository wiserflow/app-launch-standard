# AI / LLM features in the product (AI)

Applies whenever the product calls an AI model or runs an agent for customers: LLMs, and also non-LLM ML through third-party APIs (image/face recognition, speech-to-text/transcription, classification, embeddings). Items that say "LLM" or "prompt" apply to any model call; token terms map to the provider's unit (audio minutes, images, requests).

| ID | L | Requirement |
| --- | --- | --- |
| AI-01 | 1 | Every model call (LLM or other ML API) traced: tenant, user, model, tokens, cost, latency, prompt version; PII masked before export (Langfuse self-hosted or OTel GenAI semconv) |
| AI-02 | 1 | Hard per-tenant caps (tokens or money per day/month) checked **before** the call; an output cap (e.g. `max_tokens`), tool-step/loop limit and timeout on every call |
| AI-03 | 1 | No agent combines private data + untrusted content + an exfiltration channel without a gate ("lethal trifecta") |
| AI-04 | 1 | Tools least-privilege: tenant scope from the server session, never from model output; destructive/financial actions need human confirmation |
| AI-05 | 1 | Model output (generated text, transcripts, labels) untrusted: schema-validated, escaped before HTML/SQL/shell; URLs and markdown images not auto-fetched/rendered |
| AI-06 | 1 | Retrieved/user/webhook content delimited as data; no secrets in system prompts |
| AI-07 | 1 | Golden eval set (20–50 real cases per critical prompt/agent/model, e.g. labeled images or audio for recognition) run before every prompt or model change |
| AI-08 | 2 | Evals in CI with a regression threshold; production traces sampled into the dataset; LLM judges validated against human labels |
| AI-09 | 2 | Provider failure handled: retry with backoff, fallback model, graceful degradation |
| AI-10 | 2 | Users informed about AI processing; provider terms/data retention checked (privacy law, LGL-07 subprocessors) |
| AI-11 | 3 | Scheduled red-team suite (promptfoo, OWASP LLM Top 10); per-tenant cost dashboards + alerts (FIN-05); pinned model versions with a migration process |

References: [OWASP Top 10 for LLM Apps 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) · [OWASP Top 10 for Agentic Apps](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) · [OWASP prompt-injection cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) · [The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) · [Hamel Husain evals FAQ](https://hamel.dev/blog/posts/evals-faq/) · [OTel GenAI semconv](https://opentelemetry.io/docs/specs/semconv/gen-ai/).
