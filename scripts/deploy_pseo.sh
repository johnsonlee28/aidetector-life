#!/bin/bash
set -e
BASE="/root/.openclaw/workspace/aidetector-site"
HUGO_BIN="/usr/local/bin/hugo"
export PATH="/usr/local/bin:/usr/bin:/bin:$PATH"
cd "$BASE"

if [ ! -x "$HUGO_BIN" ]; then
  echo "❌ hugo binary not found at $HUGO_BIN"
  exit 1
fi

"$HUGO_BIN" --minify >/tmp/aidetector-hugo.log 2>&1 || (cat /tmp/aidetector-hugo.log && exit 1)
python3 "$BASE/scripts/site_feedback_loop.py"

git add content/detect/ content/feedback-loop-status.md public/ scripts/

if git diff --cached --quiet; then
  echo "ℹ️ No changes to deploy"
  exit 0
fi

git commit -m "chore: auto-generate pSEO pages [skip ci]"
git push origin main
echo "✅ pSEO Pages Deployed to Vercel"
