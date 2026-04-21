#!/usr/bin/env python3
import sys
import datetime
from pathlib import Path

BASE = Path('/root/.openclaw/workspace/aidetector-site')
OUT_DIR = BASE / 'content' / 'detect'
OUT_DIR.mkdir(parents=True, exist_ok=True)

def slug_to_keyword(s: str) -> str:
    return s.strip().replace('-', ' ')

def title_case_keyword(s: str) -> str:
    return ' '.join(w.upper() if w.lower() == 'ai' else w.capitalize() for w in s.split())

raw = sys.argv[1] if len(sys.argv) > 1 else 'how-to-detect-ai-in-thesis'
slug = raw.strip().lower().replace(' ', '-')
keyword = slug_to_keyword(slug)
display = title_case_keyword(keyword)

content = f'''---
title: "{display}: Practical Detection Guide"
slug: "{slug}"
description: "A practical guide to {keyword}, with detection logic, review workflow, and real-world use cases."
date: {datetime.date.today().isoformat()}
lastmod: {datetime.date.today().isoformat()}
tags: ["AI Detection", "Content Review", "SEO"]
---

# {display}

If you're searching for **{keyword}**, you're usually not looking for theory. You want a practical way to review suspicious text, reduce false positives, and make better decisions faster.

## What makes this hard

The hardest part is not finding an AI detector. The hard part is separating:

- fluent but weak reasoning
- generic structure with no lived detail
- polished wording that hides shallow evidence

## A practical review workflow

### 1. Start with detector signals, not detector conclusions
Use the tool as a first-pass filter, not as the final judge.

### 2. Check evidence density
Look for specifics, examples, constraints, and real-world friction.

### 3. Stress-test suspicious sections
Ask: would a domain expert naturally write this exact paragraph this way?

### 4. Review revision traces
Human writing often has unevenness. Purely optimized smoothness can be a signal.

## When to use manual review

Manual review matters more when the text is:

- academic
n- high-stakes
- compliance-related
- written in a voice that claims personal experience

## Final takeaway

The best approach to **{keyword}** is not tool-only. It is tool + workflow + reviewer judgment.
'''

out = OUT_DIR / f'{slug}.md'
out.write_text(content, encoding='utf-8')
print(f'✅ Generated: {out}')
