# Characters: actors, the PDF, NPCs, henchman generation

Load when creating, changing or exporting a character, when an NPC first needs numbers, or when hiring (with
henchmen-hirelings.md).

## Actors

Every PC and henchman is an **actor**: one JSON file `Characters/<id>.json` (config `paths.characters`; folder names in
these references are Kardakia's defaults, the config's paths decide) (engine 7.x, schema `acks-actor/1` in the
tools repo, `engine/data/schema/actor-1.json`). The id is the name in lower case (`andronax`, `lykos`); it is the file
name and the id in every engine command (`state add`, `party add`, `adventure join`, `inv holder add`, `retinue
employer`, `level-up --sheet`). Actor folders (config `paths.actors`, passed by `acks.sh`): `Characters/`,
`Characters/former/`, `Campaign/candidates/`, `Actors/npc/`, `Actors/monsters/`; an id is unique across them.

- **Stored** (base data): role, name, class (a reskinned class by its campaign name, tools.class_aliases), level, XP,
  occupation, alignment, birthplace, age, gender, size, attribute scores, hp maximum, AC, initiative, surprise, avoid
  surprise, save modifier texts, movement, healing rate, Mortal Wounds, proficiency throws, class features, languages,
  spells per day and the spellcasting fields, hiring terms (`hired`), proficiencies and spells known (`items`),
  `modifiers`, `state`, `judge`, `changes` (every change of this session with its cause; earlier sessions' are in
  `Campaign/actor-changes/<id>.jsonl`, moved there by the session-end save).
- **Derived on read** (never stored, never set): attribute modifiers, title, XP for the next level, Hit Die, attack
  throw and table, saves, cleaves (0th level: Hit Die and XP to 1st level stay stored). Gear, coins, weapons and
  encumbrance of an inventory holder come from the inventory (`inventory.md`); treasure carried from the adventure
  ledger (`xp-treasure.md`).
- **`state`**: current hp, conditions, spells used. `public.party` in Campaign State is generated from it by `xsync.py`
  at every save (and before `encounter fight`); never edit `public.party` by hand. `state add ID` starts a fight at the
  actor's current hp. A level gained moves current hp by as much as the maximum.
- **`judge`**: Judge only (notes, the true treasure records); the snapshot and the party agent never see it.
  Loyalty and morale live in the retinue state (`acks.sh retinue show`), not here.
- **Prose** (background, appearance, personality, voice): an optional note `Characters/<Name>.md` with front matter
  `actor: <id>` and no numbers. Judge-only lines in it go in a `> [!danger] Judge only` callout.

Commands (`bash $S/acks.sh actor …`):
- `show ID [--player] [--sources] [--fields a,b.c]`: the prepared view; `--sources` names where each number comes
  from. `get ID FIELD`: one value and its source.
- `set ID FIELD VALUE --cause "<why>"`: a base field (YAML value): `state.hp 6`, `state.conditions "[blinded]"`,
  `state.spells_used "[Sleep]"`, `languages "[Auran, Kemeshi]"`. Derived fields are refused.
- `item ID add proficiency "<name>" --list class|general [--ranks N] [--replace]`, `item ID add spell "<name>" --level N`,
  `item ID remove proficiency|spell "<name>"` (each with `--cause`): proficiencies and spells known (a level's choices,
  an NPC's). A name not on the class or general list is reported, not refused (campaign names such as Lore).
- `mod ID TARGET VALUE --source "<item, spell, ruling>" --cause "<why>"`: a lasting change to a derived number (a ring
  of protection on `saves.spells`). It applies in every roll (engine 7.6.2), named in the roll's source. The value is
  added to the number: a bonus to an attack throw or save is negative (`saves.spells -2`), to an attribute modifier or
  cleaves positive. A magic or masterwork weapon in the inventory applies its own bonus: no modifier for it.
  Engine 7.17.2: **every worn item or standing power goes on the actor once, with its rule**, never as a prose
  condition: targets `throws.<name>` (any proficiency, class skill or adventuring throw; `--flat N` = "a throw of N+
  if he has none of his own, otherwise the value": the Cloak of the Elven Ranger is `throws.hiding -8 --flat 12`),
  `saves.all`, `damage[.melee|.missile]`, `initiative`, and `note.<command>[.<arg>] --text "…"` for an effect the
  engine cannot apply as a number (printed on every such command with the actor: `note.save.death` for a Ring of Life
  Protection); `--rule "TT p. 151"`, `--item L528` (the lot it comes from). `actor mod ID --list`; `actor unmod ID
  --item L#|--source S` when it is taken off or given away (`inv give|drop|sell` of the item says so). Typed
  protections (a Ring of Fire Protection) are the actor's `defenses`; `damage ID --dice 3d6 --type fire` works outside
  a fight too. A modifier added during a fight applies from the next `state add`.
- A character built by hand (an AI player's PC): its numbers as a sheet-shaped YAML file, then `python3 $S/charsheet.py
  import <file> <id> [--role pc|henchman]` (the engine's importer, as for the PDF).
- `check ID…` (`save.sh` checks every actor and refuses to save on an error); `render ID --md --player` only when the
  user asks for a markdown sheet (never stored).
- A character who leaves or dies: `git mv Characters/<id>.json Characters/former/` (still an actor folder, so old
  adventures and the retinue resolve him; not published).

## The PC: built on the sheet (`acks chargen`)

A PC is normally built on the interactive sheet of the Kardakia Party Map (S7); the Judge runs the engine commands,
the sheet sends one request per step, every roll is open and in the roll log. Under the hood the engine's new
`acks chargen` command (engine 7.9.0, S4a) runs the RR pp. 13-24 procedure step by step on a draft actor, and `equip`
(7.10.0, S4b) puts the template's equipment into the inventory. The steps the sheet drives (same commands when it is
not available):
- `acks.sh chargen new ID --name "<Name>" --out Characters/<id>.json [--no-templates]` creates a draft actor with a
  `chargen` block (steps done, choices, pending choice). `actor check` accepts missing fields only while that block
  exists. A draft is not in `public.party` and not in a fight; the snapshot shows it to its player.
- `chargen attr ID --5d6 ATTR`, then `--4d6 A,B`, then `--3d6`: attributes (RR p. 14). `chargen discard ID` is refused
  unless the sum of modifiers is below 0.
- `chargen class ID CLASS`: refuses an ineligible class and names the failing attribute. A class the Table plays
  under a campaign name is picked by its campaign name (tools.class_aliases maps it to the RR rules). Table-rule
  allowed classes are checked here; a class outside the Table's list is refused with that reason (open: 2026-11-19).
- `chargen hp ID`: starting hp (Hit Die; 4 or less counts as 4; plus CON).
- `chargen template ID` rolls 3d6 on the class template table; `chargen template ID --take N` takes a lower template
  (N at most the roll). Without templates (optional rule): `chargen gold ID` rolls 3d6 x 10 gp; equipment is then
  bought through the market and proficiencies and spells are entered by name.
- `chargen prof ID NAME --list class|general [--ranks N]` (INT extras, RR p. 23) and `chargen spell ID NAME [--roll]`
  fill in extras the template did not set. A Kardakia Lore proficiency ("Black Lore of Asshur", "Bright Lore of the
  Twelve") is accepted by its campaign name; `Campaign/class-overlays.yaml` `inputs.proficiencies` maps it to the
  rulebook name the engine stores, and the overlay prints the campaign name back.
- `chargen equip ID`: writes the template's equipment into the inventory (template-gear.yaml), with coins as the
  opening balance; a mount or vehicle becomes a holder with its tack. By This Axe templates stay as written
  (`--as-written`).
- `chargen age ID` rolls starting age (open); `chargen set ID FIELD VALUE` for alignment, birthplace (Kardakia names
  from the overlay), gender and size.
- `chargen finish ID` removes the `chargen` block, makes the PC an inventory holder, runs `actor check` and lets
  `xsync.py` add him to `public.party`. On the Hemithean wonderworker, the Ferine names his god at creation (open:
  2026-11-19, prayerful repertoires per god: Divine Repertoires of the Twelve). A warlock's dark path and a witch's
  tradition are not chosen at creation (open: S4 note; chosen later with `chargen set` or a ruling).

An AI player's PC goes through the same commands, run by the Judge from that player's choices (a private `party.py`
call). The draft lives in `Characters/<id>.json` (role `pc`) while unfinished; the snapshot shows it to its player.

## The PDF (legacy import and export)

The fillable PDF is kept for a sheet already filled on paper (import) and for a printed copy of a built PC (export).
- `python3 $S/charsheet.py pdf2actor <attached.pdf> <id> [--role pc]` reads the form fields once through
  `data/pdf-field-map.yaml` and writes `Characters/<id>.json` through the engine's importer. Every number the PDF
  records differently from the rules (attribute modifier, attack throw, attack table, save, cleaves, XP for the next
  level, Hit Die) becomes a modifier with source `import` and is listed in the import's notes; proficiency names not
  on the class or general lists are listed by `actor check`. Report any filled field the map does not cover. Tell
  the user every listed difference; do not silently "fix" the user's sheet.
- A class the Table plays under a campaign name is checked through its alias; its templates, holy symbols, gods,
  languages and proficiency names come from the reskin note in `paths.class_notes`, never from the vault's Auran
  wording. A PDF that names the RR class instead is corrected to the campaign name (`actor set ID class
  "<campaign name>" --cause …`; tell the user).
- The PDF's gear, coins and weapons sit in the actor's `possessions` block until `inventory.md` Setup makes him a
  holder (`--opening --discard-sheet-gear`), after which the inventory is the only record.
- Export on request: `python3 $S/charsheet.py actor2pdf <id> <out.pdf>` fills a fresh copy of `party.pc_pdf_template`
  from the actor's player view (current hp from its state) and page 5 from up to six of his henchmen in hiring order.
  Send the file to the user.

Mapping: round-trip tested 2026-11-17 on the user's sheet (read → sheet → filled PDF → read again: same values) and
2026-11-19 through the actor (actor → PDF → actor: the same prepared view).

## NPCs: numbers on demand

A wiki NPC (config `paths.wiki_folders.people`, e.g. `04 People/`) is prose until he first needs numbers: a fight, a throw, a save, a spell, an offer. Then, once:
`python3 $S/npc.py "<note name>" --class C [--level L] [--race R] [--alignment A] [--kit TROOP] [--occupation O]`.
It writes his actor `Actors/npc/<id>.json` (`acks.sh actor new --role npc`, Judge only) and `actor: <id>` in the note;
run again, it names the actor it already has. The level comes from the note's `level:` (else `--level`; 0 for a
0th-level NPC); the class is your choice from the note (or `acks.sh npc-class`), a reskinned class by its campaign name,
a demi-human with `--race`. What is not given is generated as a henchman candidate is (attributes 3d6 in order, hp by
level with CON and the flat hp above 9th, the class's throws; 0th level: occupation, package, age), every roll hidden;
`--attr STR=… ×6`, `--hp-max N` or `--method average|mixed` when the note implies a notable NPC. Its `JUDGE:` items
(proficiencies, powers, spells, equipment, morale with `--kit`) are yours: proficiencies and spells with `actor item`,
AC with `actor set <id> ac "{shield: N, no_shield: N, dex_only: N}"`, weapons with `actor set <id> possessions.weapons
"[...]"` (or make him an inventory holder), alignment, languages and features with `actor set`. In a fight: `acks.sh state add <id> --side foe --perceived "<what the party sees>"`, then `state set <id>
morale=N` from his `judge.morale` (the engine rolls a foe's morale from the combat state). An NPC
never named in the wiki who needs numbers once (a guard) needs no actor: use the encounter or NPC-party commands.

## Henchmen: generating a candidate

A reskinned class (tools.class_aliases) is sought and rolled under its campaign name: the engine maps `--class` either way, writes the campaign name on candidates, NPC parties and NPC class rolls, and keeps RR sources. The Judge's `JUDGE:` items for such a candidate (equipment, symbols, languages) come from the reskin note in `paths.class_notes`. A demi-human class's candidates are not human: pass `--race` with the people's campaign name (tools.race_aliases; the engine's default is human) to `recruit` and `candidate`, so the draft names the people and demi-human morale applies. The engine does not check the class's attribute requirements on a candidate: the Judge does.

The engine generates candidates (`acks.sh candidate <CID> --name "<Name>" --sheet Campaign/candidates/<cid>.json`, the candidate id in lower case,
engine stage 3; procedure in henchmen-hirelings.md) and writes a draft actor: 0th level — occupation (JJ p. 252,
General/Street column and its sub-table), attributes 3d6 in order (`--swap A,B` if sensible), the occupation's
proficiency package (JJ pp. 254–258), age and the number of general proficiencies, hp by race and training with CON,
AC 0, attack throw and saves as fighter 0, morale, XP to 1st level; classed — class (NPC Class table or as sought), hp
by class Hit Die, the class's throws. Its `JUDGE:` items are yours: free proficiency slots, equipment (the rules give
no list), alignment, class choices, name, two or three traits and a voice. Drafts stay in `Campaign/candidates/` (Judge
only); `hire --publish-to Characters/<id>.json` moves the hired one into `Characters/` with `hired:`.

Fallback only if the engine is UNAVAILABLE: the same steps by hand with `dice.py --hidden` and the notes named above;
write nothing into `Characters/` until the engine is back (actors are written by the engine).
- A spell's or effect's modifier that lasts a while (Holy Blessing, Bless): `actor mod ID TARGET N --source "<spell>"
  --cause "cast day N" --turns 6` (or `--rounds N`, `--until "day N HH:MM"`; engine 7.19.19): the clock removes it
  when it runs out (a timer names it); never an `actor mod` left to be remembered.
