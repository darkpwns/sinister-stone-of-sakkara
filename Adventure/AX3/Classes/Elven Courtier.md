---
type: custom-class
tags: [sakkara/secret]
source: "JJ ch. 12 custom class build of the ACKS I Elven Courtier (AX3 pp. 53, 95, 192, 196, 200)"
build: "HD 1, Fighting 1a, Thievery 2, Elf 2"
xp_2nd: 2875
level_limit: 11
saves_as: thief
key_attributes: "CHA and INT"
requirements: "INT 9 (elf)"
builds_file: "Adventure/AX3/Classes/ax3-class-builds-demihuman.yaml"
---

# Elven Courtier

## Concept and role
Elven diplomats, heralds and gallants of the Argollëan courts: swordsmen trained in the classical style, poets whose music bends a hall's mood, and envoys who read a room and remember every secret told in it. They adventure as emissaries, as exiles from court intrigue, or (like Irial Ui Aedon) to give a courtly life a purpose. Nearest RR class: the [[Bard]] (music, inspire courage), but the courtier is an elf with arcane spells and a crusader's narrow weapons and heavy armour instead of fighter combat; next nearest, the [[Elven Nightblade]], which is the same build chassis (HD 1, Fighting 1, Thievery 2, Elf 2) spent on murder instead of manners.

## Build (JJ ch. 12, Custom Racial Classes)
- **Build points** (Custom Racial Classes, JJ pp. 299-300): HD 1, Fighting 1, Thievery 2 = 4 in the human categories (the maximum), plus Elf 2 = **6 build points → 11th level limit**.
- **Requirements:** INT 9+ (all elven classes, Elven Custom Classes, JJ p. 301).
- **Hit Dice 1** ([[Hit Dice Value]]): d6; +1 to the HD roll at 1st level (Connection to Nature); +2 hp per level after 9th (thief progression). 500 XP.
- **Fighting 1a (Crusader)** ([[Fighting Value]]): attack throws +2 per 4 levels (thief table), 1 cleave per 2 levels, no damage bonus. Narrow weapons: (ii) any bows and crossbows and (iv) any swords and daggers (meets the elf rule of at least two of bows, crossbows, swords, daggers). Heavy armour (no armour trade-off). Fighting styles: single weapon and missile weapon, plus **weapon and shield** and **dual weapon** (the curved sword and dagger of AX3's courtiers). 500 XP.
- **Thievery 2** ([[Thievery Value]]): 8 selections, every one traded for a custom power (Thievery Value custom power trade-off; no thief skills kept): six at 1st level, and two each traded for two locked powers ([[Custom Power Trade-Offs]]: 1 initial → 4th + 10th; 1 initial → 6th + 8th). 500 XP.
- **Divine 0, Arcane 0.** Spellcasting comes from the Elf Value.
- **Elf 2** ([[Elven Custom Classes]]): the four elf powers (Animal Friendship, Attunement to Nature, Connection to Nature, Elf Tongues) and **50% Arcane** (Arcane 0 + Elf 2 = effective Arcane 2: the Arcane 2 progression, spells from 2nd level, cast in any armour the class may wear). 1,375 XP.
- **Trade-offs taken:** Thievery 2 → 8 custom powers (no XP); no Fighting trade-offs, so no weapon trade-off XP.
- **Custom powers** (Custom Power Index name, cost): Performance (1), Magical Music (1), Inspire Courage (1), Martial Talent (melee) (1), Perceive Intentions (1), Bonus Languages (1); locked: Rumormongering (4th) and Blood of Kings (10th) for 1; Magical Music again (6th) and Martial Talent (missile) (8th) for 1. The starting general proficiency power (every custom class has one, [[Saving Throw Progression (Custom Classes)]]): **Diplomacy**. Castle bonus power at 5th: **Chronicles of Battle**.
- **Drawbacks:** none.
- **Saving throws** ([[Saving Throw Progression (Custom Classes)]]): Fighting 1, Thievery 2, Divine 0, Arcane 0 → **thief** (the racial value is not counted), with Connection to Nature's +1 on Paralysis and Spells.
- **Magic items:** thief items; mage items too, because Arcane + Elf = 2 (Custom Racial Classes); enchanted bows, crossbows, swords, daggers and any armour.
- **Key attributes:** **CHA** (the thief progression's DEX or CHA, chosen CHA for the class) and **INT** (Arcane + Elf 2).
- **Proficiencies:** 42 − 11 = 31 on the class list (below). Proficiency progression as thief-progression classes: class proficiency at 1st, 4th, 8th; general at 1st, 5th, 9th.
- **Stronghold** ([[Strongholds and Followers]]): qualifies for Castle (Fighting 1+), Hideout (Thievery 1+) and Sanctum (Arcane + Elf 2); not Elven Fastness (needs Fighting 2). Takes **Castle**, renamed **Elven Court**, with its 5th-level morale power.
- **XP** ([[Experience Points per Level]]): 500 + 500 + 500 + 1,375 = **2,875 XP for 2nd level**; doubled to 8th (7th rounded to the nearest 5,000); then +100,000 (thief) + 50,000 (elf) = **+150,000 per level after 8th**.

## Class table
From `acks/custom_class.py` (acks2-tools) driven with this build; the Elf 2 build points, the elven +50,000 XP after 8th and Connection to Nature's save bonus added by the JJ rules (the calculator knows dwarf values only). Spells per day: JJ Arcane 2 progression.

| Level | Title | XP | Hit Dice | Attack | Paralysis | Death | Blast | Implements | Spells | Spells/day (1st-6th) | Caster Level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Page | 0 | 1d6+1 | 10+ | 12+ | 13+ | 13+ | 14+ | 14+ | - | 0 |
| 2 | Herald | 2,875 | 2d6 | 10+ | 12+ | 13+ | 13+ | 14+ | 14+ | 1 | 1 |
| 3 | Envoy | 5,750 | 3d6 | 9+ | 11+ | 12+ | 12+ | 13+ | 13+ | 2 | 2 |
| 4 | Courtier | 11,500 | 4d6 | 9+ | 11+ | 12+ | 12+ | 13+ | 13+ | 2 | 2 |
| 5 | Gallant | 23,000 | 5d6 | 8+ | 10+ | 11+ | 11+ | 12+ | 12+ | 2/1 | 3 |
| 6 | Emissary | 46,000 | 6d6 | 8+ | 10+ | 11+ | 11+ | 12+ | 12+ | 2/2 | 4 |
| 7 | Chamberlain | 90,000 | 7d6 | 7+ | 9+ | 10+ | 10+ | 11+ | 11+ | 2/2/1 | 5 |
| 8 | Seneschal | 180,000 | 8d6 | 7+ | 9+ | 10+ | 10+ | 11+ | 11+ | 2/2/2/1 | 7 |
| 9 | Elf-Lord | 330,000 | 9d6 | 6+ | 8+ | 9+ | 9+ | 10+ | 10+ | 3/2/2/1 | 7 |
| 10 | Elf-Lord, 10th level | 480,000 | 9d6+2\* | 6+ | 8+ | 9+ | 9+ | 10+ | 10+ | 3/2/2/2 | 8 |
| 11 | Elf-Lord, 11th level | 630,000 | 9d6+4\* | 5+ | 7+ | 8+ | 8+ | 9+ | 9+ | 3/2/2/2/1 | 9 |

\* No CON adjustment to this flat bonus.

## Class powers
**Starting (1st level)**
- **Diplomacy** (starting general proficiency power): +1 on reaction rolls when parleying ([[Diplomacy]]). AX3's "diplomacy and protocol".
- **Performance:** one rank of [[Performance]] in a courtly art (epic poetry, song, harp...); AX3's "perform".
- **Magical Music:** two musical effects (Drowsiness, Goodwill, Horror, Outrage), throw 11+ −1 per level, +1 per extra Performance rank up to +2 ([[Magical Music]]).
- **Inspire Courage:** one round of oration before battle inspires up to 30 allies within 50' (+1 attack, AC, morale, saves vs magical fear) for 1 turn; once per day per class level; not on allies already engaged (as the [[Bard]]).
- **Martial Talent (melee)**, "classical weapons training": +1 to melee attack throws.
- **Perceive Intentions:** always knows the true reaction result of creatures he interacts with; creatures whose CHA exceeds his WIL are immune.
- **Bonus Languages:** three extra languages (court tongues), on top of Elf Tongues.
- **Elf racial powers:** Animal Friendship (only on building a fastness, so unused by an Elven Court), Attunement to Nature, Connection to Nature, Elf Tongues ([[Elven Custom Classes]]).

**Additional**
- **Arcane Magic (2nd level):** casts arcane spells from a repertoire (spells per day and caster level as in the table; repertoire = that number per spell level + INT bonus, [[Spell Repertoires]]); casts in any armour he may wear. Uses caster level for spell effects and research.
- **Rumormongering (4th level):** revisiting a settlement where he has moved in society, he learns 1d4 rumours from old contacts after a day there; once per month per settlement.
- **Chronicles of Battle (5th level, Castle bonus power):** henchmen and mercenaries he hires gain +1 morale while he is there to witness and record their deeds.
- **Magical Music (6th level):** two more musical effects.
- **Minor Magical Research (7th level):** at caster level 5, can research spells, scribe scrolls and brew potions, as the [[Elven Nightblade]] on the same progression ([[Magic Research]]).
- **Martial Talent (missile) (8th level):** +1 to missile attack throws.
- **Elven Court (9th level):** on acquiring a court-castle worth 15,000gp+, 5d6×10 0th-level elven troops and 1d6 courtiers of 1st-3rd level arrive within 1d3 months, to be paid normal rates ([[Followers and Strongholds]]).
- **Blood of Kings (10th level):** one more henchman than his CHA allows; his henchmen's base loyalty +1.

**Class proficiency list (31):** [[Battle Magic]], [[Beast Friendship]], [[Combat Reflexes]], [[Combat Trickery]], [[Command]], [[Counterspelling]], [[Disguise]], [[Eavesdropping]], [[Elementalism]], [[Expanded Repertoire]], [[Familiar]], [[Fighting Style Specialization]], [[Leadership]], [[Lip Reading]], [[Magical Engineering]], [[Magical Music]], [[Mastery of Enchantments & Illusions]], [[Mimicry]], [[Mounted Combat (Proficiency)|Mounted Combat]], [[Mystic Aura]], [[Precise Shooting]], [[Prestidigitation]], [[Quiet Magic]], [[Riding]], [[Seduction]], [[Sensing Power]], [[Skirmishing]], [[Swashbuckling]], [[Unflappable Casting]], [[Weapon Finesse]], [[Weapon Focus]].

## Converted from ACKS I
- **From AX3's text** (Irial's statline, AX3 p. 200): the class name and level; d6-scale hit points (21 hp at 5th); chain and shield; composite bow and sword; *classical weapons training (+1 with melee attacks)* → Martial Talent (melee) (the JJ Custom Power Index itself names Martial Talent "classical weapons training (elven courtiers)"); *diplomacy and protocol* → Diplomacy; *inspire courage (5/day)* → Inspire Courage, once per day per level (5/day at 5th, matching AX3); *magical music* → Magical Music; *perform* → Performance; *spellcasting* at 2 1st and 1 2nd at 5th level, which is exactly the JJ Arcane 2 (50%) progression at 5th, so Elf 2 reproduces it. Her attack throws (5+ with sword +1 and with masterwork bow at STR 13, DEX 16) also come out exactly on the thief (+2 per 4 levels) progression with Martial Talent.
- **From the JJ Custom Power Index's class lists** (powers it says the ACKS I Elven Courtier used): Animal Friendship, Inspire Courage, Keen Eyes, Martial Talent. *Keen eyes* (partial thief searching) was removed in ACKS II; the strengthened Attunement to Nature replaces it.
- **From my recollection of the ACKS I Player's Companion** (not a quotation, and uncertain): the courtier as an elven diplomat-bard with elven spellcasting and a CHA-centred prime requisite. I do not recall its exact build points, saving throw table or level limit.
- **Judge's calls (this build):** thief saves and Thievery 2 as the source of the social powers (giving CHA as a key attribute by rule, and the Nightblade's 2,875 XP); Perceive Intentions, Bonus Languages, Rumormongering, Blood of Kings and the second Magical Music and Martial Talent as the remaining selections (Irial "collects other people's secrets", AX3 p. 200); the Elven Court stronghold; level titles.

## NPCs of this class in AX3
- **[[Irial Ui Aedon (AX3)]]** (Imperial Vanguard, AX3 p. 200; [[Imperial Vanguard]]). Revised statline: **Elven Courtier 5**; Str 13, Int 13, Wis 12, Dex 16, Con 11, Cha 18; AC 8 (chain mail +1 5, shield +1, DEX +2); HD 5, hp 21; sword +1 **5+** (courtier 5 = 8+, STR +1, magic +1, Martial Talent +1), D 1d6+2 slashing (+1 magic, +1 STR); masterwork composite bow **5+** (8+, DEX +2, masterwork +1), masterwork arrows D 1d6+1 piercing; saves (thief 5, Connection to Nature, WIL 12 +0): **Paralysis 10+, Death 11+, Blast 11+, Implements 12+, Spells 12+**; ML +3; AL L; XP 200 (level 5 as HD, no special abilities; RR p. 310). Spells per day **2 1st, 1 2nd** (caster level 3; as AX3 printed). Class powers at 5th: Diplomacy, Performance (epic poetry), Magical Music (Goodwill, Drowsiness: Judge's call), Inspire Courage 5/day, Martial Talent (melee), Perceive Intentions, Bonus Languages, Rumormongering, Chronicles of Battle, elf powers. Proficiencies unchanged (AX3: Eavesdropping, Knowledge (history), Mystic Aura, Performance (epic poetry) as her second rank, Riding = 2 class + 2 general + 1 INT bonus at 5th).
- **Fionntan** (one of doppelgänger #3's assumed identities, AX3 p. 95; `Tables/ax3-old-doppelganger-3.yaml`, [[Doppelganger Den]]): a doppelgänger posing as an elven courtier; it uses the [[Doppelgänger]]'s statline, not this class.
- The elven courtier in leaf-embossed leather of the Palace District special encounters (AX3 p. 192, `Tables/ax3-palace-special.yaml` 11) is the same doppelgänger.
- NPC Class table (`Tables/ax3-building-npc-class.yaml`, AX3 p. 53): Thief type 97-98.
