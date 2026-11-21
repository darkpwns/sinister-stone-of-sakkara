# Bootstrap (first session)

Load when `brief.py` says **bootstrap needed** (Campaign State `public.party` is empty). If Campaign State's `adventure:` says **between adventures**, follow the last section (A new adventure in a running campaign) instead.

1. **Table rules in one AskUserQuestion** (four questions; the first combines two settings so all five fit):
   - "Quest and discovery awards, and hidden rolls?" — options: awards off, hidden rolls in the Judge block (recommended) / awards off, hidden rolls logged openly / awards on, hidden rolls in the Judge block / awards on, hidden rolls logged openly.
   - "Henchman control?" — the player directs routine actions and combat tactics; the Judge plays personality, morale, obedience and what they do alone (recommended) / the Judge runs henchmen entirely, the player gives orders in character / the player runs henchmen like extra characters, Judge rolls loyalty and obedience.
   - "Party structure?" — solo PC plus henchmen / human party (a caller gives one declaration per round) / AI party (six AI players are the party; the user watches) / mixed (the user plays one PC and calls; AI players play the others).
   - "Month length (wages and market availability)?" — 30 days / 28 days (4 weeks) / the campaign calendar's month (read config `paths.calendar`).
   If the user is not there to answer, take the recommended or first option of each and say so at the top of the reply.
   If the structure is AI party or mixed, a second AskUserQuestion: which AI players sit at the table (multi-select from the six profiles in `Party/profiles/`, all six by default for AI party), the caller (AI party: Gideon by default; mixed: the user), Character creation (templates, RR default / no templates, optional rule), and whether AI players hire their own henchmen (yes, recommended / no). Record them in config `party` (`active_players` as `{id, pc: ""}`, `caller`) and in Table rules.
   Record the answers in Campaign State `## Table rules` and config `party.structure`, append one line per setting to Rulings.md (`Judge's ruling: table rule set at bootstrap`). If quest awards are on, ask in the same reply for the award scale or propose one, and record it in Rulings.md.
2. **The PC on the sheet** (solo, human party and mixed; not AI party). The default: build him on the Kardakia Party Map sheet with `acks.sh chargen` (characters.md → The PC: built on the sheet), one step per request, every roll open. If the user has a filled fillable PDF and prefers to import it (legacy), use `charsheet.py pdf2actor` into `Characters/<id>.json` (role pc) and report the import's differences from the rules; otherwise ask the player to use the sheet.
2b. **AI players' PCs** (AI party and mixed): party-structure.md → Making the AI players' PCs, then, if Table rules allow, the hiring session (in town, at the start location, before step 7's first scene ends).
2c. **Inventory** (engine stage 6, `inventory.md` Setup): `acks.sh inv init --month-days N`, then each PC as a holder with his PDF coins as the opening balance and his starting gear added item by item.
3. **Party entry:** set `session: 1` in Campaign State. `public.party` is generated from the actors at the save (`xsync.py`); a PC who starts wounded: `acks.sh actor set <id> state.hp N --cause …`.
4. **Start:** date, time, mode, location, hex and place from config `start`; weather not yet rolled (`acks.sh travel-init` then `acks.sh weather` when the party first goes outdoors or travels; the engine rolls each later day at dawn).
5. **Session log:** create `S01 — <summary>.md` from the template (config `logs.session_log`), link it under the index section of the campaign log, and add the PC to the log's party list (config `logs.session_log.index`, `## Party`).
6. `save.sh "S01 bootstrap: table rules, <PC name>"`.
7. Begin play at the start location: narrate the arrival or the first morning there, the visible prompts of the starting situation (the campaign's starting-point note, if the wiki has one: player-facing parts only), then stop for the player's first action.


## A new adventure in a running campaign

Load this section instead of steps 1-2c when `brief.py` says **bootstrap needed** but Campaign State's `adventure:` says
**between adventures** (Table rules, the inventory, the retinue and the rulings already exist: keep them all).
1. **The new adventure and where it lies.** Its module notes go in the wiki folders (config `paths.wiki_folders`) and
   its hub's `Running …` section (prep). Place its sites on the campaign's hex grid and extend `Data/hexes.csv` and
   `Data/places.csv` as the region note says (the campaign's fixed point and grid: `Adventure/Region Map.md` in the
   Sakkara campaign). Never renumber existing hexes. Update config `start` (location, hex) only if play begins
   somewhere else; the date stays the engine clock's.
2. **Each player's starting XP** (RR Character Death: reserve XP fund and heroic funeral, never more than the prior
   character's XP): `acks.sh death <prior id> --new-character --player <player> --prior-xp <prior character's xp>`
   (the prior actor is in `Characters/former/`). Run it only when that player's new character is made: it consumes
   the funeral XP. The players' funds are the adventure ledger's `players` block.
3. **The new PCs:** party-structure.md → Making the AI players' PCs (or `acks.sh chargen` for a human player), one per
   player, at 1st level; then `acks.sh actor set <id> xp <starting XP> --cause "reserve XP (RR Character Death)"` and
   `acks.sh level-up --sheet <id> --apply` once for each level that XP reaches. Equipment: the template's, or 3d6 × 10
   gp, unless he inherits (a relative may collect a dead character's belongings once: `death <prior> --heir <id>
   --deposits N`). Set config `party.active_players[].pc`; make each an inventory holder (inventory.md Setup) and
   `acks.sh party add <id>`.
4. **Henchmen** of former characters stay in `Characters/former/` and the retinue as dismissed; they may be recruited
   again (henchmen-hirelings.md: a new offer).
5. **Travel state:** keep the existing travel block (its hex, season start and calendar); do not run `travel-init`
   again. Check the season with `acks.sh travel-show` (it follows the calendar from engine 7.13.4).
6. **Open the adventure:** `acks.sh adventure start --name "<module>"` and `adventure join` each PC and henchman before
   the first delve or journey. Campaign State: `adventure:` the module, `mode`, `location`, `session` + 1.
7. Session log, save and the first scene as steps 5-7 above.
