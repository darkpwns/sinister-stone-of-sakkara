#!/bin/bash
# setup.sh : once per chat, after the campaign and rules repos are cloned. Installs Python deps if missing,
# prepares the rules lookup (rules repo tools/rl_setup.sh), puts the tools clone on the engine branch campaign.yaml
# names (tools.ref), installs and checks the rules engine (tools repo setup.sh) and requires tools.min_version (actors:
# engine 7.x). After a rules vault sync the engine's check fails until the monster data are re-extracted: setup then
# runs `acks extract --defenses`, `acks extract --monsters` and the check again. Prints "engine: ready ..." or
# "engine: UNAVAILABLE ..." and checks the campaign config. Ends with "ready".
D="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
python3 -c "import yaml, pypdf" 2>/dev/null || pip install -q --break-system-packages pyyaml pypdf >/dev/null 2>&1 || { echo "error: cannot install pyyaml/pypdf"; exit 1; }
RULES=$(python3 -c "import sys; sys.path.insert(0,'$D'); import jlib; print(jlib.config()['rules']['clone_dir'])") || { echo "error: campaign.yaml unreadable"; exit 1; }
[ -x "$RULES/tools/rl_setup.sh" ] || { echo "error: rules repo not cloned at $RULES"; exit 1; }
O=$("$RULES/tools/rl_setup.sh") || { echo "$O"; exit 1; }
echo "rules: $(echo "$O" | grep '^notes:')"
eval "$(python3 - "$D" <<'PY'
import sys, shlex
sys.path.insert(0, sys.argv[1])
import jlib
t = jlib.config().get("tools", {}) or {}
for k, v in (("TOOLS", "clone_dir"), ("REF", "ref"), ("MINV", "min_version")):
    print(f"{k}=" + shlex.quote(str(t.get(v) or "")))
PY
)"
engine() {
  if [ -z "$TOOLS" ] || [ ! -x "$TOOLS/setup.sh" ]; then
    echo "engine: UNAVAILABLE - tools repo not cloned at ${TOOLS:-?} (fallback: dice.py and rules lookups)"; return; fi
  if [ -n "$REF" ] && [ -d "$TOOLS/.git" ] && [ "$(git -C "$TOOLS" rev-parse --abbrev-ref HEAD)" != "$REF" ]; then
    if [ -n "$(git -C "$TOOLS" status --porcelain)" ]; then
      echo "engine: UNAVAILABLE - the tools clone has local changes on $(git -C "$TOOLS" rev-parse --abbrev-ref HEAD); campaign.yaml tools.ref is $REF (fallback: dice.py and rules lookups)"; return; fi
    git -C "$TOOLS" fetch -q origin "$REF" 2>/dev/null && git -C "$TOOLS" checkout -q -B "$REF" FETCH_HEAD 2>/dev/null \
      || { echo "engine: UNAVAILABLE - cannot check out tools.ref $REF in $TOOLS (fallback: dice.py and rules lookups)"; return; }
  fi
  E=$("$TOOLS/setup.sh" "$RULES" 2>&1)
  if ! echo "$E" | grep -q '^ready'; then        # a vault sync since the data were checked: re-extract the monster data
    . "$HOME/acks_env.sh" 2>/dev/null
    if command -v acks >/dev/null && acks extract --defenses >/dev/null 2>&1 && acks extract --monsters >/dev/null 2>&1; then
      E=$("$TOOLS/setup.sh" "$RULES" 2>&1)
      echo "$E" | grep -q '^ready' && echo "  engine data: defenses and monster compendium re-extracted from the synced vault (local clone)"
    fi
  fi
  if ! echo "$E" | grep -q '^ready'; then
    echo "engine: UNAVAILABLE - $(echo "$E" | tail -1) (fallback: dice.py and rules lookups)"; return; fi
  V=$(python3 -c "import acks; print(acks.__version__)" 2>/dev/null)
  if [ -n "$MINV" ] && ! python3 -c "import sys; t=lambda s: tuple(int(x) for x in s.split('.')); sys.exit(0 if t('$V') >= t('$MINV') else 1)"; then
    echo "engine: UNAVAILABLE - acks $V is older than tools.min_version $MINV (tools.ref ${REF:-default branch}) (fallback: dice.py and rules lookups)"; return; fi
  echo "engine: $(echo "$E" | grep '^ready')"
}
engine
python3 "$D/snapshot.py" --check && echo ready
