#!/usr/bin/env python3
from pathlib import Path
import xml.etree.ElementTree as ET
import datetime

BASE = Path('/root/.openclaw/workspace/aidetector-site')
CONTENT = BASE / 'content' / 'detect'
PUBLIC = BASE / 'public' / 'detect'
REPORT = BASE / 'content' / 'feedback-loop-status.md'
SITEMAP = BASE / 'public' / 'sitemap.xml'

pages = sorted(CONTENT.glob('*.md'))
rows = []

for p in pages:
    slug = p.stem
    public_html = PUBLIC / slug / 'index.html'
    rows.append({
        'slug': slug,
        'content_exists': True,
        'public_exists': public_html.exists(),
    })

sitemap_urls = set()
if SITEMAP.exists():
    try:
        root = ET.parse(SITEMAP).getroot()
        for loc in root.iter():
            if loc.tag.endswith('loc') and loc.text:
                sitemap_urls.add(loc.text.strip())
    except Exception:
        pass

for r in rows:
    url = f'https://aidetector.life/detect/{r["slug"]}/'
    r['in_sitemap'] = url in sitemap_urls

ok = sum(1 for r in rows if r['content_exists'] and r['public_exists'] and r['in_sitemap'])

today = datetime.date.today().isoformat()
body = [
    '---',
    'title: "Feedback Loop Status"',
    f'date: {today}',
    '---',
    '',
    f'# Feedback Loop Status ({today})',
    '',
    f'- Detect 内容页: {len(rows)}',
    f'- 三项全通过(content + public + sitemap): {ok}',
    '',
    '| slug | content | public | sitemap |',
    '|---|---|---|---|',
]

for r in rows[:60]:
    body.append(f"| {r['slug']} | {'✅' if r['content_exists'] else '❌'} | {'✅' if r['public_exists'] else '❌'} | {'✅' if r['in_sitemap'] else '❌'} |")

REPORT.write_text('\n'.join(body) + '\n', encoding='utf-8')
print(f'✅ wrote {REPORT}')
