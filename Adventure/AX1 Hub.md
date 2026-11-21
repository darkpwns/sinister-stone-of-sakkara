---
type: hub
tags:
  - sakkara/secret
source: "AX1 The Sinister Stone of Sakkara (Autarch 2015, ACKS I), 80 pp."
---

# The Sinister Stone of Sakkara (AX1) — Judge hub

Judge only. Page references are the module's printed page numbers ("p. N"); the PDF page is N + 1.
Party of 6-10 characters of 1st-3rd level, 8-12 total levels (p. 3).

## Running the Buried Temple
- Dungeon level: 1
- Wandering monsters: 1d6 every 2 turns, 6+
- Encounter table: Tables/level1-wandering.yaml

(The table path is relative to this note's folder, which is how `acks.sh location --hub Adventure/Sakkara.md` resolves it: it is `Adventure/Tables/level1-wandering.yaml`. The engine reads only the first `Running …` section of a hub.)

## Running the Catacombs
- Dungeon level: 2
- Wandering monsters: 1d6 every 2 turns, 6+
- Encounter table: Tables/level2-wandering.yaml

(For level 2 pass the settings explicitly, since `--hub` reads only the section above: `acks.sh location --site "Catacombs" --level 2 --wandering "1d6 every 2 turns, 6+" --table Adventure/Tables/level2-wandering.yaml`.)

## Notes
- [[Turos Tem]] — the starting stronghold (hex 22.20): services, prices, NPCs, rewards, rumours.
- [[Viaspen Forest]] — finding the temple; forest encounter table.
- [[Level 1 - Buried Temple]] — areas 1-6, rooms 1-75.
- [[Level 2 - Catacombs]] — rooms 1-39, The Lady Below.
- [[AX1 Magic Items]] — magic items, the Stone of Sakkara, new equipment; where each lies.
- Bestiary: `Adventure/Bestiary/<Name> (Sakkara).md`; everything else is a Monstrous Manual note.

## Premise (p. 3-4)
- A Zaharan temple to Chthonic gods, buried by the clerics of Law under a dome of black granite during the Empyrean War, held the **Stone of Sakkara**, an artifact that births abominations and commands chaotic creatures.
- Two years ago an earthquake cracked the dome open; the Stone woke. Brigands, then beastman warbands, then the Zaharan ruinguard **Zakiti, "The Lady Below"**, answered its call. She subjugated the warbands and sends them to raid hamlets and caravans for sacrifices to power the Stone's birthing pools.
- **Legate Ulrand Valerian** of Türos Tem offers **2,000gp** to whoever uncovers and ends the threat. He does not know of the Stone. Raids continue until the Stone is destroyed.

## Region (AX1 Region Map; since S07 the campaign uses the AX3 Borderlands sheet numbering: AX1 module hex CCRR ≈ (CC+9).(RR+12), see [[Region Map]])
- Türos Tem: module hex 1308 = **22.20** (AX3 #28). Buried temple: module 1007 = **19.19** (AX3 #27). Crossing hex (module 1107, the forest edge on the way): **20.19**.
- Route Türos Tem → temple: **22.20 → 21.20 → 20.19 → 19.19** (3 hexes, 18 miles).
- Viaspen Forest edge: about 9 miles NW of Türos Tem through lightly settled farmland (1.5-6 hours). The temple is 9 miles deeper into thick forest (movement ×½).
- Other sites on the Region Map (p. 65, seeds only, not stocked): Sinkhole of Evil (13.23), Shrine of the White Lady (23.16; unicorn, 20 hp; pool: a Lawful drinker loses one Tampering with Mortality side effect once per lifetime and gains a geas to destroy Chaotic creatures in Southern Argollë), Ruined Imperial Fortress (26.19; bugbear tribe under a war-chief), Watchtower at Eammon Mór (26.26; ogre warlord with ~170 beastmen), Ruined Monastery (31.17; beastmen and chthonic cultists), the Dark Wall (cliffs of rock-cut Thrassian and Zaharan structures).

## Module procedures for the Judge

### Finding the temple (p. 33)
- Party does not know where the lair is. **Each hour of searching** the Viaspen: Judge makes a hidden proficiency throw for the party: **17+**, or **13+** if the party has an explorer, an elven ranger, or a character with Tracking. Success = tracks or evidence leading to the temple.
- **Each hour** also an encounter throw: **1d6, on 6** a wilderness encounter: roll **1d6** on the Viaspen table ([[Viaspen Forest]]). Encounters 3 (ambush site, via searching the underbrush), 5 (dwarves) and 6 (Antonius) can lead the party straight to the temple.
- Once found, the party travels to and from it without searching: 18 miles, 4.5-18 hours by movement rate.

### Travel after the temple is found (p. 34)
- **Hex 20.19:** each time the party crosses it, wilderness encounter throw **1d6, on 6** an encounter by the core rules (ACKS p. 244-246; use the engine's wilderness encounter for forest).
- **Night in the Viaspen:** navigation throw **7+** or become lost (ACKS p. 94).

### Dungeon (both levels)
- **Wandering:** encounter throw every 2 turns, and whenever the party makes a lot of noise: 6 on 1d6 → encounter at standard distance, direction random. Roll 1d8 on the level's table (or the core tables at the Judge's discretion). Wanderer flavour and loot: see each level note.
- **Area-specific rates (level 1):** Area 1 (kobold territory, rooms 1-13): **5-6 on 1d6 each turn**. Room 19 (Crossroads): **5-6 each turn**. Area 4 (former goblin territory, rooms 33-44): **5-6 every turn**.
- **Rooftops (level 1, p. 35):** open-air rooms **13, 18, 19, 42 and 61** can be climbed out of / into (a 12’5” climb up the wall) and the party can travel across the temple roofs between them. On the roofs the only wandering encounters are **giant rats or stirges** (ignore other results). Beastmen never use the roofs.
- **Doors (p. 35):** heavy hardwood with bronze fittings. Single doors hinged interior left; all doors push inward from halls and courtyards into rooms. Doors are **stuck** when adventurers first meet them (forcing as core rules). Denizens use secret knocks within their own areas. Where doors rotted, occupants hung **curtains** of stitched hides.
- **Frescoes, mosaics, carvings (p. 35):** the room text gives what anyone sees; the bracketed lore is given only on a successful Loremastery, Knowledge (Ancient History), Knowledge (Occult), Theology or similar proficiency throw. In town, Annalist Socolo interprets carvings and frescoes with Loremastery 15+ (free if Friendly, 40gp each if Indifferent/Neutral).
- **Light:** brigands (level 1 Area 2) keep their rooms lit; everyone else sees in the dark.
- **Empty rooms** are deliberate buffers and resting places.
- **Factions:** the tribes feud as much as the Lady permits. Few on level 1 attack strangers outright (reaction roll); they may demand tribute in their turf, or ask for news if the party seems to come from an enemy's area; they know the Lady has called more allies, so the party could pass as recruits. Brigands will readily tell captors about the feuds.

### Replacement of casualties
- **Level 1 (p. 35):** while The Lady Below and the Stone remain, roll 1d6 each week for each "cleared" room: on **1-3** the tribe gains **1d6** members (usually back in that room; deployed intelligently if under regular assault). If a tribe is wiped out nothing returns; if its **leaders are killed**, the rest drift away within a week, taking whatever known treasure is in their chambers. **Skeletons, zombies, ghouls:** replaced on **1-4**, never leave, must be destroyed.
- **Level 2 (p. 53):** same, 1-3 → 1d6 similar creatures arrive; leaders killed → rest leave in a week with known treasure. **Abominations, skeletons, zombies, ghouls:** replaced on **1-4**, never leave.

### Sinkholes and cleansing XP
- L1 75 shrine and vault: shadowed sinkhole (smash altar + bless or holy water: Lawful characters 100 XP each).
- L2 22 Outer Fane: shadowed sinkhole (destroy altar + bless/holy water: 100 XP each; stripping its gold, 3 turns, yields 2,000gp and counts as destroying it).
- L2 38 Inner Fane: blighted sinkhole (destroy the Stone, smash the altar, then bless/holy water: 200 XP each).
- L2 20 large tree killed: 100 XP each; L2 25 small tree: 75 XP each.
- Turning over the three Fragments of the Tablet of Destiny to Lawful clergy: 10,000 XP divided among participants (see [[AX1 Magic Items]]).

### Rewards
- Legate: 2,000gp on evidence the raids are stopped (see [[Turos Tem]] for what he accepts and what follows).
- Drusus, dead or alive: 750gp from the Quartermaster.
- Merchants Daros Thenes and Odysios Panas (L1 65): 250gp each alive, 50gp each for bodies (Guildmaster Karanos).
- Family members (Motivation 2) in L1 73 / L2 38: no cash reward listed.
