#!/bin/bash
set -e
BASE="/root/.openclaw/workspace/aidetector-site"
KEYWORD_FILE="$BASE/scripts/batch_keywords.txt"
LOG_PREFIX="[aidetector-auto]"

echo "$LOG_PREFIX start $(date '+%F %T')"

echo "$LOG_PREFIX discovering keywords"
python3 "$BASE/scripts/discover_keywords.py"

if [ ! -f "$KEYWORD_FILE" ]; then
  echo "$LOG_PREFIX keyword file missing: $KEYWORD_FILE"
  exit 1
fi

while IFS= read -r kw; do
  [ -z "$kw" ] && continue
  echo "$LOG_PREFIX generating: $kw"
  python3 "$BASE/scripts/generate_pseo_page.py" "$kw"
done < "$KEYWORD_FILE"

echo "$LOG_PREFIX auditing generated pages"
python3 "$BASE/scripts/audit_and_rewrite_full.py"

echo "$LOG_PREFIX deploying"
"$BASE/scripts/deploy_pseo.sh"

echo "$LOG_PREFIX done $(date '+%F %T')"
