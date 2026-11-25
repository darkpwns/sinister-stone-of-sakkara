# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 1 · **day 1**, 08:00 · **Turos Tem** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Lepidus | Fighter 1 | 0 | 6/6 |  |
| Aurelia | Crusader 1 | 0 | 4/4 |  |
| Octavia | Mage 1 | 0 | 6/6 |  |
| Silvanus | Explorer 1 | 0 | 6/6 |  |
| Fulvia | Thief 1 | 0 | 5/5 |  |
| Eskil | Shaman 1 | 0 | 5/5 |  |

- **Adventure:** no adventure open
- **Wages:** no retinue; owed now: 0 gp | NOTE: wage timing: reading applied (wage.timing) - The books give monthly wages ('a monthly fee for food, lodging, and expenses') but never say when in the month they fall due. The engine takes the wage as paid in advance: the first month's on the day of hiring, then one month later each time (the campaign's month length); a ruling can set in_arrears (due at the end of each month served).
- **Schedule:** nothing due on day 1
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
<!-- generated:end -->

## Judge's notes for the next session
- **Run 3 begins.** Read `Campaign/Campaign State.md` (Table rules: finish AX1; no templates; five sets each; the corridor and combat rules kept) and `Party/heuristics.md` ("The raids first"). Runs 1 and 2 are in `Archive/`: nothing of them holds.
- Start: day 1, 08:00, Türos Tem (22.20), spring; weather rolled (warm, drizzle). No adventure open: `acks.sh adventure start --name "AX1 The Sinister Stone of Sakkara"` and `adventure join` each PC before the first delve or journey (bootstrap.md, A new adventure, step 6).
- The Judge plays the six AI players by their profiles and heuristics; Gideon calls. Their first goals: hear the legate's call at the Headquarters (18), the rumours, hire henchmen (Leadership on Lepidus), find the lair (Silvanus the explorer: 13+ per hour in the Viaspen, AX1 p. 33).
- **Loads:** Lepidus 9.7 st, Silvanus 9.2, Aurelia 8.5, Eskil 7.25, Fulvia 7.03 (all 60'); Octavia 4.7 (120'). Ingrid will redistribute or hire a porter/mule before the first march. Iron rations are in packs but not in travel supplies: `inv provision` before leaving town.
- **Purses:** Aurelia 7gp 9sp, Octavia 15gp, Fulvia 32gp, Silvanus 32gp (and a hunting dog, holder `silvanus-hound`), Lepidus 26gp, Eskil 74gp.
- **Eskil's totem dog** is the companion `eskil-dog` (HD 1/2, hp 2, 1d4; Alertness while it lives).
- **Back-ups and NPC pool:** `Characters/backups/` (two per player, attribute drafts: build one with `chargen` from its attributes when the death table rule calls for a new character) and `Campaign/npc-pool/` (twelve sets for the Judge's NPCs: use them for henchman candidates or named NPCs who need numbers).
- Notes prepped in earlier runs beyond the modules (World State prep queue) may carry their outcomes: read them as unplayed. The Troglodyte Warren is run 2's interim prep, not part of AX1.
