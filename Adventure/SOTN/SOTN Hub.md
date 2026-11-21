---
type: hub
hex: "18.05"
tags:
  - sakkara/secret
source: "AX2 Secrets of the Nethercity (Autarch, ACKS I), 186 PDF pages; printed page = PDF page − 2"
---

# Secrets of the Nethercity (AX2) — Judge hub

Judge only. Page references are SOTN's printed pages ("SOTN p. N"; PDF page N + 2). Statblocks and rules are converted to
ACKS II (see each note); Judge's calls, book errors and AX3/SOTN disagreements are in `Adventure/SOTN/README.md` under
Open items. The city above is AX3 ([[AX3 Hub]]): this module's notes link those notes and do not repeat them.

## Running the Nethercity sewer caves
- Dungeon level: 2
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/sotn-wandering-sewer-caves.yaml

The entry level: areas **A, C, L** (the sludge river from the cesspit down to the abyssal caves). SOTN pp. 18-19: one
encounter throw every 3 turns anywhere in the Nethercity, 6+ on 1d6, then 2d10 on the column for the kind of area the
party is in. The column per area and the dungeon levels are Judge's calls (SOTN gives the columns by terrain and an
average threat level per column, not a column per area); the level follows each column's threat (sewer 1-2, volcanic
2-3, temple/tomb 3-4, river 4-6). Sewer caves never clear: new creatures keep arriving.

(The engine reads only the first `Running …` section through `--hub`: `acks.sh location --hub "Adventure/SOTN/SOTN Hub.md"`
sets the sewer caves. For the others pass the settings explicitly, e.g. `acks.sh location --site "Nethercity G - Grand
Chthonic Temple" --level 4 --wandering "1d6 every 3 turns, 6+" --table Adventure/SOTN/Tables/sotn-wandering-temple-tomb.yaml`.
Moving between areas of different columns inside one delve: `acks.sh location --level N --table …` changes only those
settings. Table paths are relative to this note's folder: `Adventure/SOTN/Tables/`.)

## Running the Nethercity volcanic caves
- Dungeon level: 3
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/sotn-wandering-volcanic-caves.yaml

Areas **I** (troglodytes) and **M** (white apes). Optional clearing applies (below).

## Running the Nethercity temples and tombs
- Dungeon level: 4
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/sotn-wandering-temple-tomb.yaml

Areas **B, D, E, F, G, H, J, K, N, O, Q, R, S, T**. A party **sealed in a temple or tomb** (resting) meets only the
entries marked "enters a sealed temple or tomb"; ignore the rest (about one entry in three: ~0.9 encounters in an 8-hour
rest, SOTN p. 18). Optional clearing applies.

## Running the Nethercity underground river
- Dungeon level: 5
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/sotn-wandering-underground-river.yaml

Area **P** (the river banks, the funerary barge P11). Optional clearing applies.

## Premise (SOTN pp. 5-10; full story: [[Nethercity History]])
- 60’ under **[[Cyfaraun]]** (hex 18.05) lies the **Nethercity**: lava caves that the elves of Cyfarawn I turned, over
  1,500 years (33rd-17th c. BE), into temples, tombs and catacombs of the **Chthonic** gods, taught by a **[[Khepri Hierarch]]**
  they called the **Great Teacher**. There they embalmed their dead, made their great ones **mummies** to wait for the
  **Awakening**, bred the **Thrassians** — and were destroyed by an earthquake and their own slaves. The quake sealed it.
- Above it, layer on layer: **Ancient Cyfaraun** (Cyfarawn II, buried in ash in 245 BE), whose avenues are now the Auran
  sewers of the **Undercity** ([[Undercity of Cyfaraun]]); then **Old Cyfaraun** and the Auran city ([[Old District]] and
  the other districts). The elves of Cyfarawn II sealed the way down under a **Temple of Demara**; the Aurans made that
  buried temple the agora's great cesspit. In **329 IY** its floor gave way: for fifty years the city's sewage has poured
  into the Nethercity, feeding a new ecology of slimes, vermin, troglodytes, giant ants and white apes among the undead.
- **Module scope** (SOTN p. 5): a deep exploration delve for a party of six of **3rd-5th level**, stocked to carry it from
  **4th to 8th**. A novice party gains experience in the Undercity first (AX3). It introduces the **Awakening** as a
  setting-wide threat (droppable). The campaign's party (four 4th-level PCs, two low-level, AX1 finished) fits the bottom
  of the band.
- **SOTN vs the campaign map:** SOTN p. 5 puts Cyfaraun "some fifty miles northwest of Türos Tem"; on the campaign's AX3
  sheet Cyfaraun (18.05) is 15 rows north of Türos Tem (22.20), 138 miles by road ([[Region Map]]). The map stands.

## Getting in (SOTN pp. 10, 24; AX3 pp. 63-73)
- **The only known way in: the leaking cesspool under the agora latrines**, Old District **#12u** = Nethercity **A1**
  ([[Old District]] "12U. Leaking Cesspool"; [[Nethercity A - Entrance Caves]]). There is no man-sized way down from the
  latrine (#12) itself: the party reaches the cesspool **through the Undercity**. Old District sewer grates lift out
  freely (an action instead of movement: the Argollëan Family's smuggling routes); elsewhere a Dungeonbashing throw.
  Other ways into the sewers: the AX3 Undercity entrance list ([[Undercity of Cyfaraun]], "Entrances": the Mink's
  basement #11u and the other districts' basements and sewer gates). Below the Old District the Undercity throw is **5+**
  ([[AX3 Hub]] "Running Undercity of Cyfaraun"). The Family claims the Old District sewers: see Factions.
- In the cesspool the sludge pours through a **door-sized hole** into a tunnel and down rough steps to A2; a
  [[Carrion Horror]] lurks below (+1 to surprise those coming down).
- **Other ways, found from inside:** the **teleportation platform** (L4; troglodytes and one ape exile know of it; random
  visitors arrive through it), the **teleportation disc** (N5) and the **funerary barge** (P11): see those area notes.
  None is a way in until the party has found and learnt it (Judge's call).
- **Rivals searching for the way in:** Provost Mentenus's **Horned Rat wererats** tap the sewer walls for it day and night
  ([[Shrine of the Horned Rat]], Old District #13u; AX3 Undercity special 13u); the **Argollëan Family** knows the
  Nethercity lies in its territory and wants it ([[Organizations of Cyfaraun]]).

## Procedures the Judge runs

### Wandering monsters (SOTN pp. 18-19)
- Throw **1d6 every 3 turns, 6+**; **2d10** on the column of the area (Running sections above; each area note's
  `Running:` line names it). Encounter distance and surprise by the ACKS II rules (engine `encounter`).
- **Sealed rest:** only marked entries enter a sealed temple or tomb (Temple / Tomb column; 2 throws an hour).
- **Clearing (optional, used):** in volcanic, temple/tomb and river areas, a wandering group that was **slain** is not met
  again in that area (ignore repeats); one fled from or turned may return. Sewer caves never clear.
- **Noise and lures** that force extra throws are in the room notes (shrieking cavern locusts in C2, shriekers, etc.).

### Unsettling events (SOTN pp. 19-20)
Every **12 turns (2 hours)** in the Nethercity: event throw 1d6, **6+** → `Tables/sotn-unsettling-events.yaml` (1d20),
played at the next fitting moment; re-roll a repeat. Event 1 (songbird) forces an encounter throw.

### Standing rules ([[Nethercity Features]])
Doors (stone slab −12 with up to 3 helpers adding STR bonuses, bronze −4, cedar), how long it takes to open a tomb and
what the undead inside are doing; inscriptions (Ancient Argollëan; 11+ / 16+ with fumbles); sarcophagi and lids; **sewer
sludge** (half-rate charges, −2 Acrobatics/Sneaking, fungal infection, miasma save every turn, **fireballs over the sludge
in area L**); **sinkholes of evil** (the whole place shadowed; blighted spots; the dead rise); teleport wards; **wall
graves** (contents, grave goods by era, looting rate, detail tables) and the **undead skeleton** guard groups; mummies by
era, armed mummies, the **mummy reaction** table; treasure conventions, **attracting attention** (1% per 2,000 gp spent,
sold or banked), white ape pelts.

### Factions ([[Nethercity Factions]])
Inside: the **troglodyte tribe** (I, D8), the **giant ant colony** (L), the **white apes** (M), the wakeful undead and
the **Great Teacher** in cryostasis (T). Above: the **Argollëan Family** (AX3; SOTN calls it the Argollëan Brotherhood)
fences elven antiquities and hunts their source; the **Cult of the Horned Rat** seeks the entrance; the tax collectors
want half of Undercity finds ([[Doing Business in Cyfaraun]]).

### Rumours
SOTN prints no rumour table. The city's rumours that point down: [[Undercity of Cyfaraun]] and `Adventure/AX3/Tables/ax3-rumours.yaml`
(#10 the rat-loving wizards; #20 Tavus Ionicus's dreams of the Nethercity). One rumour on any Friendly reaction from a
Cyfaraun NPC ([[AX3 Hub]] "Rumours"). Damanos of the House of Curiosities (Old District #4) and the Family's fences
recognise ancient Argollëan coin.

### Replacement of casualties (SOTN pp. 12, 19)
- SOTN has no weekly restocking roll. Instead: **sewer caves never clear** (wandering entries keep coming); in other areas
  slain wandering groups stay gone (clearing rule).
- **The dead rise:** anything killed in the Nethercity has a **10% chance to rise as undead after 1d12 months**; in a
  **blighted sinkhole 20% after 1d4 days** — unless burned or consumed. Track bodies the party leaves (Judge's call: use
  the MM undead of the creature's size: [[Skeleton]] or [[Zombie]]).
- Undead skeleton groups return to torpor in their graves a turn after the last living creature leaves their sight.
- Woken mummies left alive act on `Tables/sotn-mummy-reaction.yaml`.
- Keyed intelligent groups (troglodytes, apes, ants) that lose members: Judge's call (SOTN gives no rate); AX1's rule (1d6
  per week per cleared room, 1-3 → 1d6 return) is a reasonable model for the troglodyte tribe and the ant colony.

### Special rules of the Nethercity (summary)
- **Light:** none anywhere unless a room says so.
- **Sludge miasma:** save vs Death each turn near the sludge (once an hour at +4 with a cloth over the face) or −1 to
  attack throws and damage; **in area L torches over the sludge explode on 1 in 6 per turn (6d6)**.
- **Treasure is conspicuous:** ancient Argollëan coin; sell, smelt or launder (Features). Half of Undercity finds are
  owed to the treasury; the Family fences at 65% (80% to friends) ([[AX3 Hub]] "Services").
- **Teleportation** in or out: +20 on the teleport table; dimension door as "seen casually"; not the L4, N5, P11 devices.
- **XP:** treasure XP by the ACKS II rules (magic items give XP only when sold); monster XP as converted in each note.

## Notes
- Background and rules: [[Nethercity History]] (history, timeline, gods), [[Nethercity Features]] (standing rules),
  [[Nethercity Factions]] (groups and NPCs).
- Areas (`Areas/`, room by room): [[Nethercity A - Entrance Caves]], [[Nethercity B - Early Chthonic Tomb]],
  [[Nethercity C - Central Caves]], [[Nethercity D - Warlord's Tomb and Chapel to Bel]],
  [[Nethercity E - Deep Level Central Complex]], [[Nethercity F - Lower Level Central Complex]],
  [[Nethercity G - Grand Chthonic Temple]], [[Nethercity H - Great Temple of Awakening]],
  [[Nethercity I - Deep Level Southern Cave Complex]], [[Nethercity J - Doom Temple of Dirgion]],
  [[Nethercity K - Hallowed Hall of Heroes]], [[Nethercity L - Abyssal Level Caves]], [[Nethercity M - Northern Caves]],
  [[Nethercity N - Sub-Abyssal Alchemic Laboratory]], [[Nethercity O - Sub-Abyssal Secret Tomb of the Hierophant]],
  [[Nethercity P - Sub-Abyssal River Banks]], [[Nethercity Q - Great King Tomb]],
  [[Nethercity R - Abyssal Level Southern Cave]], [[Nethercity S - Abyssal Level Hidden Tombs]],
  [[Nethercity T - Sub-Abyssal Secret Alien Sepulcher]].
- Items and spells: [[SOTN Magic Items]], [[SOTN Spells]].
- Classes SOTN uses that ACKS II lacks (JJ ch. 12 builds, `Classes/`): [[Elven Cultist]], [[Elven Hierophant]],
  [[Elven Warlord]], [[Elven Wizard]]; build record `Classes/sotn-class-builds.yaml`.
- Bestiary (`Bestiary/<Name> (SOTN).md`): BESTIARY-LIST. Everything else is a Monstrous Manual note.
- The city above (AX3): [[Cyfaraun]], [[Cyfaraun (Market)]] (class III), [[Old District]] (#12/#12u: the entrance),
  [[Undercity of Cyfaraun]], [[Organizations of Cyfaraun]], [[Doing Business in Cyfaraun]], [[Streets of Cyfaraun]],
  [[Imperial Vanguard]] (rival party), [[Shrine of the Horned Rat]], [[The Mink - Family Hideout]]; hub [[AX3 Hub]].

## Tables (`Adventure/SOTN/Tables/`, acks-table/1)
- Wandering monsters (2d10): `sotn-wandering-sewer-caves.yaml`, `sotn-wandering-volcanic-caves.yaml`,
  `sotn-wandering-temple-tomb.yaml`, `sotn-wandering-underground-river.yaml`.
- Events and reactions (rolled by the Judge, not by `encounter`): `sotn-unsettling-events.yaml` (1d20),
  `sotn-mummy-reaction.yaml` (1d20).
- Wall graves: `sotn-wall-grave-male-name.yaml`, `sotn-wall-grave-female-name.yaml`, `sotn-wall-grave-death-decade.yaml`,
  `sotn-wall-grave-death-year.yaml`, `sotn-wall-grave-goods.yaml`.
