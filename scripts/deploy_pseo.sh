#!/bin/bash
set -e
cd /root/.openclaw/workspace/aidetector-site/

git add content/detect/ scripts/

if git diff --cached --quiet; then
  echo "ℹ️ No changes to deploy"
  exit 0
fi

git commit -m "chore: auto-generate pSEO pages [skip ci]"
git push origin main
echo "✅ pSEO Pages Deployed to Vercel"
