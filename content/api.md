---
title: "AI Detector API — Integrate AI Detection Into Your App"
description: "Integrate AI content detection into your application. REST API for detecting AI-generated text from ChatGPT, Claude, Gemini, and more. Free tier available."
keywords: ["ai detector api", "ai detection api", "chatgpt detection api", "ai content checker api", "programmatic ai detection"]
url: "/api/"
date: 2026-04-26
lastmod: 2026-04-26
draft: false
---

## AI Detector API

Add AI content detection to your application, workflow, or platform. Our API returns word-level AI probability scores for any text input.

## What You Can Build

- **LMS integrations** — auto-flag student submissions for teacher review
- **CMS plugins** — check content before publishing
- **HR tools** — screen job applications and cover letters
- **SEO tools** — verify content quality at scale
- **Publishing workflows** — batch-check submissions

## API Overview

Send a POST request with your text. Get back an overall score plus per-word and per-sentence breakdowns.

**Endpoint:** `POST https://aidetector.life/api/v1/detect`

**Response includes:**
- `overall_score` — 0.0 (human) to 1.0 (AI)
- `label` — "human", "mixed", or "AI-generated"
- `word_scores` — per-word AI probability
- `sentences` — per-sentence breakdown with scores

## Pricing

| Tier | Requests/month | Price |
|------|---------------|-------|
| Free | 1,000 | $0 |
| Starter | 10,000 | $19/mo |
| Pro | 100,000 | $99/mo |
| Enterprise | Unlimited | Contact us |

## Key Features

- **Word-level scores** — not just a single percentage
- **Multi-model detection** — ChatGPT, Claude, Gemini, LLaMA, DeepSeek
- **Low latency** — average response under 800ms
- **No text retention** — inputs are not stored or logged

## Get API Access

API access is currently in early access. [Contact us](/about/) to request an API key.

---

*Need detection without an API? The [free web tool](/detector/) is unlimited — no sign-up required.*

## Related

- [AI Detector for Business](/business/)
- [How AI Detection Works](/how-to-detect-ai-content/)
- [AI Detector Accuracy](/posts/ai-detector-accuracy/)
