#!/bin/bash
# acks.sh CMD [args] : the rules engine (acks2-tools, `acks`) with this campaign's roll log, session number,
# engine rulings file, combat state and exploration state (all from campaign.yaml). Every roll is logged like
# dice.py's. Stage 2 commands (turn, rest, light, timer, explore, location, party, wander-check, encounter, reaction,
# evade, pursue, move-rate, clock) get the exploration state; `encounter fight` also gets the party's current hp
# from Campaign State (public.party). Stage 3 (retinue, recruit, candidate, offer, hire, dismiss, transfer, wages, loyalty,
# obey, npc-party, wait) gets the retinue state and the exploration clock (the day); `turn`, `rest`, `encounter` and the
# combat commands get the retinue state too (wage days on day rollovers; hireling morale and 0-hp calamities at round end).
# Stage 4 (travel-init, travel, forced-march, navigate, weather, forage, water, firewood, hunt, fish, eat, drink, supplies,
# camp, rest-day, heal, mounts, search, travel-show) gets the exploration state (one clock), the hex adapter (campaign.yaml
# `hexes`) and the retinue state (wage days falling during the trip); `encounter` and `evade` get the hex adapter too.
# Stage 5 (adventure, treasure, place, item, recover, appraise, identify, use, sell, payout, level-up, advance-0th, death,
# restore) gets the adventure ledger (campaign.yaml tools.adventure_state), the exploration state (the day; treasure
# carried into encumbrance) and the retinue state (loyalty for a level gained); `adventure init` gets the placement
# setting and the arms-and-armor column from tools.treasure. Every command but check gets campaign.yaml as --aliases when
# its tools block has class_aliases or race_aliases (engine 6.16.0: reskinned classes keep their RR rules).
# Stage 6 (inv) gets the inventory (tools.inventory_state), the exploration clock, the adventure ledger and the retinue.
# Every other command runs with the inventory too (ACKS_ISTATE): once it exists, light, missile attacks, spikes, tools,
# wages, recruiting and appraisal fees, the payout, death, hiring and pack animals take from it what they use and refuse
# what is not there (engine 6.17.0; ACKS_INV_XSTATE/ASTATE/RETINUE tell those hooks where the other state files are).
# Engine 7.x: every command gets the actor folders (campaign.yaml paths.actors) as ACKS_ACTORS: an actor id names
# <folder>/<id>.json (Characters, Characters/former, Campaign/candidates, Actors/npc, Actors/monsters). `encounter fight`
# first regenerates Campaign State public.party from the actors' state (xsync.py --party), which it reads for current hp.
D="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
[ -f "$HOME/acks_env.sh" ] && . "$HOME/acks_env.sh"
command -v acks >/dev/null || { echo "error: engine not installed (run the tools repo setup.sh; fallback: dice.py)"; exit 2; }
eval "$(python3 - "$D" <<'PY'
import os, sys, shlex
sys.path.insert(0, sys.argv[1])
import jlib
cfg = jlib.config()
fm, _ = jlib.read_note(cfg["paths"]["state"]["campaign_state"])
t = cfg.get("tools", {})
print("LOG=" + shlex.quote(jlib.path(cfg["paths"]["state"]["roll_log"])))
print("SES=" + shlex.quote(str(fm.get("session", 0))))
print("STATE=" + shlex.quote(jlib.path(t.get("combat_state", "Campaign/combat-state.json"))))
print("XSTATE=" + shlex.quote(jlib.path(t.get("exploration_state", "Campaign/exploration-state.json"))))
print("CSTATE=" + shlex.quote(jlib.path(cfg["paths"]["state"]["campaign_state"])))
print("RSTATE=" + shlex.quote(jlib.path(t.get("retinue_state", "Campaign/retinue-state.json"))))
print("HEXES=" + shlex.quote(jlib.path(t.get("hexes", "Campaign/campaign.yaml"))))
print("ASTATE=" + shlex.quote(jlib.path(t.get("adventure_state", "Campaign/adventure-state.json"))))
print("ISTATE=" + shlex.quote(jlib.path(t.get("inventory_state", "Campaign/inventory-state.json"))))
print("ACTORS=" + shlex.quote(os.pathsep.join(jlib.actor_dirs(cfg))))
# campaign bestiary folders (tools.bestiary): module creatures' statblock notes, parsed fresh by the engine (WP4)
print("BEST=(" + " ".join(shlex.quote(jlib.path(b)) for b in (t.get("bestiary") or [])) + ")")
# campaign item folders (tools.items): a module's magic items that the vault lacks (notes with base_cost, apparent_value)
print("ITEMS=" + shlex.quote(os.pathsep.join(jlib.path(b) for b in (t.get("items") or []))))
# S5: the term map holds the input aliases a later consumer applies (the sheet's request channel, S6):
# kardakia term -> rulebook value, for proficiencies, monsters, items, barbarian people (beside class_aliases
# and race_aliases). Exposed to subcommands that would use them, as ACKS_INPUT_ALIASES.
print("TMAP=" + shlex.quote(jlib.path(t.get("term_map", "Campaign/term-map.yaml"))))
tt = t.get("treasure") or {}
print("TSET=" + shlex.quote(str(tt.get("setting", ""))))
print("ARMS=" + shlex.quote(str(tt.get("arms_setting", ""))))
r = t.get("engine_rulings")
print("RUL=" + shlex.quote(jlib.path(r) if r and os.path.exists(jlib.path(r)) else ""))
# class and race aliases (reskinned classes): the engine reads them from campaign.yaml's tools block
print("ALI=" + shlex.quote(jlib.path("Campaign/campaign.yaml") if (t.get("class_aliases") or t.get("race_aliases")) else ""))
PY
)"
CMD="$1"; shift
export ACKS_ISTATE="$ISTATE" ACKS_INV_XSTATE="$XSTATE" ACKS_INV_ASTATE="$ASTATE" ACKS_INV_RETINUE="$RSTATE" ACKS_ACTORS="$ACTORS" ACKS_INPUT_ALIASES="$TMAP"
ACKS_BESTIARY=$(IFS=:; echo "${BEST[*]}"); export ACKS_BESTIARY
# campaign tables (acks-table/1) for `table roll|show|find ID` (engine 7.13.7): every Tables/ folder under Adventure/
ACKS_TABLES=$(find "$(dirname "$(dirname "$LOG")")/Adventure" -type d -name Tables 2>/dev/null | paste -sd: -); export ACKS_TABLES
export ACKS_ITEMS="$ITEMS"   # module magic items for recover, identify, sell   # module creatures for every command (travel, turn, search too)
# open-roll labels reach the snapshot: a foe joins a fight only under the name the party perceives (SKILL.md §4)
needs_perceived() { case " $* " in *" --perceived "*|*" --perceived="*) return 1;; esac; return 0; }
if { [ "$CMD" = "encounter" ] && [ "$1" = "fight" ]; } || { [ "$CMD" = "npc-party" ] && [[ " $* " == *" --to-state "* ]]; } \
   || { [ "$CMD" = "state" ] && [ "$1" = "add" ] && [[ " $* " != *" --side party "* ]]; }; then
  needs_perceived "$@" && { echo "NOT ALLOWED: pass --perceived \"<what the party sees>\" (open-roll labels use it and reach the snapshot; a monster's true name only once the party knows it)"; exit 2; }
fi
[ "$CMD" = "actor" ] && [ "$1" = "import" ] && [ ! -f "$ISTATE" ] && unset ACKS_ISTATE   # no inventory yet: import keeps possessions (D10)
EXTRA=(--log "$LOG" --session "$SES")
[ -n "$RUL" ] && EXTRA+=(--rulings "$RUL")
[ -n "$ALI" ] && [ "$CMD" != "check" ] && EXTRA+=(--aliases "$ALI")
case "$CMD" in state|encounter|monster) for b in "${BEST[@]}"; do EXTRA+=(--bestiary "$b"); done ;; esac
case "$CMD" in
  roll|version|check|monster) ;;
  explore-init|party|location|light|timer|explore|wander-check|reaction|move-rate|clock|disease)
    EXTRA+=(--state "$STATE" --xstate "$XSTATE") ;;
  evade|pursue)
    EXTRA+=(--state "$STATE" --xstate "$XSTATE" --hexes "$HEXES") ;;
  turn|rest)
    EXTRA+=(--state "$STATE" --xstate "$XSTATE" --retinue "$RSTATE") ;;
  encounter)
    EXTRA+=(--state "$STATE" --xstate "$XSTATE" --retinue "$RSTATE" --hexes "$HEXES")
    [ "$1" = "fight" ] && { python3 "$D/xsync.py" --party >&2; EXTRA+=(--party-hp "$CSTATE"); } ;;
  travel-init|travel|forced-march|navigate|weather|forage|water|firewood|hunt|fish|eat|drink|supplies|camp|rest-day|heal|mounts|search|travel-show)
    EXTRA+=(--xstate "$XSTATE" --hexes "$HEXES" --retinue "$RSTATE") ;;
  adventure)
    EXTRA+=(--astate "$ASTATE" --xstate "$XSTATE")
    [ "$1" = "init" ] && { [ -n "$TSET" ] && EXTRA+=(--setting "$TSET"); [ -n "$ARMS" ] && EXTRA+=(--arms-setting "$ARMS"); } ;;
  treasure|place|item|recover|appraise|identify|use|sell)
    EXTRA+=(--astate "$ASTATE" --xstate "$XSTATE") ;;
  payout|level-up|advance-0th|death)
    EXTRA+=(--astate "$ASTATE" --xstate "$XSTATE" --retinue "$RSTATE") ;;
  restore) ;;
  inv)
    EXTRA+=(--xstate "$XSTATE" --astate "$ASTATE" --retinue "$RSTATE") ;;
  retinue|recruit|candidate|offer|hire|dismiss|transfer|wages|loyalty|obey|npc-party|npc-class|wait|spellcasting)
    EXTRA+=(--state "$STATE" --xstate "$XSTATE" --retinue "$RSTATE") ;;
  chargen)
    # S5: creation on a draft actor (RR pp. 13-24). No combat state; retinue for 0th-level draws; istate for `equip`
    # via ACKS_ISTATE. Class and race aliases apply via --aliases so campaign names resolve to RR rules.
    EXTRA+=(--retinue "$RSTATE") ;;
  class)
    # S5: class sheet profiles (`acks class profile|list`): rules data, rulings and aliases, no combat state.
    : ;;
  *) EXTRA+=(--state "$STATE" --retinue "$RSTATE") ;;
esac
exec acks "$CMD" "$@" "${EXTRA[@]}"
