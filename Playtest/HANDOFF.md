# Sakkara playtest — handoff (2026-11-20)

Playtest of AX1 *The Sinister Stone of Sakkara* as a campaign of the `acks2-judge` skill, engine 7.12.0+.
`REPORT.md` is the per-delve log; `judge-notes.txt` the voids, slips and Judge's calls; `campaign/` the full instance
(state, actors, roll log, module notes in `campaign/Adventure/`); `tools/` the playtest helpers.

## Where play stands (superseded: see the S06 update below)
- Day 95, 23:00. Party inside the Buried Temple at **L1 75** (the dead dragon's vault under the ziggurat), at the head
  of the 35' stair down to **L2 room 1** (the catacombs). Torch put out at the save; relight on resume.
- In the delve: Aulus (F2), Sabina (Cru3), Tarq (Bar2), Lucilla (Ven3), Vettius (Thf3), Marcia (Mag2, Fan of Flames,
  Blinding Flash, Sleep), Gallus (Ven2), Thorwell, Thorcigar (F1), Quintus (F1), Vestus (M1), Zaira (ElvSpellsword 1).
  Hesper (F1) keeps camp at the stream in 10.07 with the donkey.
- Adventure A6 "Buried Temple, delve 6 (the catacombs)" open. Coins banked in town (`karanos-bank` cache).
- Next: descend to L2 1; plan was 1 → rubble passage → 22 Outer Fane (Ur-Namu, 4 catechists) → Lake of Blood 20 → 36
  → 38 Inner Fane (Zakiti, the Stone). Rebuke undead untested so far (Sabina). Legate's 2,000gp reward needs the
  Stone destroyed.

## Resuming
1. Clones at /home/user/{acks2-tools,acks2-rules-vault,kardakia-campaign} on branch claude/sakkara-adventure-playtest-7kql1w;
   `mkdir -p /home/claude && ln -s /home/user/<repo> /home/claude/<repo>` for each.
2. Recreate the instance: copy `campaign/` to /home/user/sakkara-playtest, `git init`, then lay the skill in with
   `bash /home/user/acks2-tools/campaigns/new_campaign.sh <empty kit dir> /home/user/sakkara-playtest /home/user/kardakia-campaign/.claude/skills/acks2-judge`
   (or copy `.claude/skills/acks2-judge` from kardakia-campaign). Run `bash .claude/skills/acks2-judge/scripts/setup.sh`.
3. `. tools/j.sh` (edit the paths at the top: `cd /home/user/sakkara-playtest`; melee.py path) gives `t`, `r`, `loc`,
   `door`, `meet`, `brawl`, `walk`.
4. Party decisions follow `campaign/Party/heuristics.md` and the profiles; the party agent was used once (step 1).

## Engine 7.13.0 (2026-11-20)
Built: magic armor lots worn on `inv claim` (Lucilla's chain mail L28 now worn, AC 6; stand-in removed with
`actor unmod`); `spellcasting` (hired castings); `encounter start --npc` for town reactions; `disease
expose|diagnose|cure|show` with stages on the day rollover; starvation/thirst deaths ask `death` and mark the actor;
`party add` during travel warns on missing supplies (the cause of the henchman losses). Encumbrance difficulty is
intended: use mules, porters, wagons. `min_version` in the instance is 7.13.0.

## S06 update (second chat, 2026-11-20)
- Day 97, 11:08, camped in forest hex 11.07 (on course), marching to Türos Tem (13.08) via 12.07, `--retrace`. No food at all; skins full except Quintus, Vestus, Zaira, Hesper (no skins; drink at sources: `water` once a day in 11.07, 12.07, 13.08). Everyone hungry or underfed.
- Sabina is 10 st with 1.2 days of water (9 st without): she halves the column's speed unless the load is shifted.
- Hesper is now in the exploration/travel party (`party add hesper`). The location is cleared (outside the temple).
- Party agent: Table talk dropped from the declaration (Party/prompt/base.md); `party.py` wall fix (rumours heard count as player-facing) is in kardakia-campaign's skill copy; copy `.claude/skills/acks2-judge` from there when recreating the instance.
- Call dir: `campaign.yaml party.agent.call_dir` points at the current chat's scratchpad; reset it each chat.

## S06 end (2026-11-21, after the replay)
- Day 138, Türos Tem, all healed. The Lady Below (Zakiti) lives at 7 hp (heals) and holds the Stone again; she knows the party. Undead: 8 zombies (two scorched) with her; skeletons of 34 destroyed; Ur-Namu and the acolytes of 22 dead but four new acolytes there (weekly replacement rolls). Ogres dead; Black Fangs friendly.
- Party: Aulus F2, Sabina Cru3, Tarq Bar2, Lucilla Ven3, Vettius Thf3, Marcia Mag2; henchmen Hesper F1, Thorwell F1 (Tarq's), Quintus F1, Vestus M1, Zaira ES1 (one leg). Dead: Gallus, Thorcigar (Characters/former/).
- Lots carried: L58 sword +1 (Aulus, unidentified). Black Fang chest (L2 9), the Lady's chest (L2 39, needle trap), Red Eye loot (L2 15), Drusus (L1 17) all unplundered.
- The first playing of rounds 9+ (surrender, legate's reward, 10,000 Fragment XP, Tarq's death) is void; its rolls stay in the roll log (judge-notes).
- Party agent not used after S06 step 4 (user: Judge plays the party by the profiles and heuristics; no table talk).
- Helpers: tools/fight.py (melee driver with latch and first strike) and tools/day.sh.
