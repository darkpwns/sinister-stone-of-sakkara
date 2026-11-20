# Bootstrap (first session)

Load when `brief.py` says **bootstrap needed** (Campaign State `public.party` is empty).

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
