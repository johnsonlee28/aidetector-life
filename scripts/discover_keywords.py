#!/usr/bin/env python3
from pathlib import Path

OUT = Path('/root/.openclaw/workspace/aidetector-site/scripts/batch_keywords.txt')

# MVP 版：先用规则生成可打词池，后面再接搜索数据源
roles = [
    'students', 'teachers', 'researchers', 'professors', 'editors'
]
objects = [
    'thesis', 'essay', 'research-paper', 'code', 'academic-writing'
]
patterns = [
    'how-to-detect-ai-in-{obj}',
    'ai-detection-for-{role}',
    'detecting-ai-generated-{obj}',
]

keywords = []
for role in roles:
    for obj in objects:
        for p in patterns:
            kw = p.format(role=role, obj=obj)
            keywords.append(kw)

# 简单去重 + 取前12个，避免一晚上打太多页
final = []
seen = set()
for kw in keywords:
    if kw not in seen:
        seen.add(kw)
        final.append(kw)

selected = final[:12]
OUT.write_text('\n'.join(selected) + '\n', encoding='utf-8')
print(f'✅ discovered {len(selected)} keywords -> {OUT}')
for kw in selected:
    print(kw)
