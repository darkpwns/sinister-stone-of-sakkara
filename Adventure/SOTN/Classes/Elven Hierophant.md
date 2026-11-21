---
type: custom-class
tags: [sakkara/secret]
source: "JJ ch. 12 custom class build of the ACKS I Elven Hierophant (SOTN pp. 166-169)"
build: "HD 0, Fighting 0, Divine 2, Arcane 2, Elf 2"
xp_2nd: 3000
level_limit: 11
saves_as: mage
key_attributes: "INT and WIL"
requirements: "INT 13, WIL 13"
hit_dice: "1d4"
builds_file: "Adventure/SOTN/Classes/sotn-class-builds.yaml"
---

# Elven Hierophant

Up: [[SOTN Hub]] · Builder: [[JJ 12 Custom Classes]], [[Creating a Custom Class]] · Build record: `Classes/sotn-class-builds.yaml` (`Elven Hierophant`) · See also [[Elven Cultist]] (the corruption rules), [[Nethercity History]]

## Concept and role
Disciples of the ancient mystery cults descended from the great teachers of the Day Without Night, who balance reason and faith to wield both arcane and divine magic; among men the like are called wonderworkers. Always rare and ascetic, now nearly forgotten: a few last hierophants teach small, unworthy congregations (SOTN p. 166). Lawful hierophants pray from their own list; Chaotic ones (the Nethercity's, e.g. Orthanach, the first Argollëan mummy lord) from the cultists' list.
- **Nearest RR class:** the [[Nobiran Wonderworker]] (full arcane and divine casting, d4, mage combat). It does not suffice: it is a Nobiran class with six 11+ requirements and Nobiran powers (Divine Health, Lay on Hands), its divine casting runs on its own table, and it lacks the hierophant's scholar powers (Loremastery, read languages, esoteric meaning, lore of stars and spheres) and elf powers.

## Build (JJ ch. 12, Custom Racial Classes)
- **Build points:** HD 0, Fighting 0, Thievery 0, Divine 2, Arcane 2 = 4, plus Elf 2 = **6 build points → 11th level limit** (SOTN 11th).
- **Requirements:** INT 13, WIL 13 (SOTN INT 13, WIS 13; the elven INT 9 is moot).
- **Hit Dice 0:** d4, Mortal Wounds +0; +1 HD roll at 1st (Connection to Nature); +1 hp per level after 9th. 0 XP.
- **Fighting 0 (Mage):** +2 per 6 levels, no cleaves; restricted weapons **dagger, sling, staff, whip**; no armour; the optional style **eliminated for 1 custom power** (SOTN: no two-handed, no dual). 0 XP.
- **Thievery 0.**
- **Divine 2** ([[Divine Value]]): casts and researches as a crusader; list of 10 spells per level. **Rebuke undead traded for 2 custom powers** (SOTN gives none). 500 XP.
- **Arcane 2** + **Elf 2** = effective **Arcane 4**: learns, casts and researches arcane spells as a [[Mage]]. Arcane 1,250 − 125 (elven) = 1,125 XP; Elf 2 = 1,375 XP ([[Elven Custom Classes]]).
- **Code of behaviour (Divine 2; Judge's call from SOTN):** the ascetic discipline of the mysteries: daily rites and study, poverty of person, secrecy of the mysteries from the uninitiated.
- **Custom powers (3):** one at 1st (**Sensing Power**, Judge's call); one traded for **Loremastery (3rd) + Lore of Stars and Spheres (11th)**; one for **Read Languages (5th) + Unveil Esoteric Meaning (9th)** ([[Custom Power Trade-Offs]]). Starting general proficiency power: **Theology** (Judge's call; the Astrologer template already spends a proficiency on Collegiate Wizardry).
- **Saving throws:** Divine and Arcane tie at 2 → **mage** (Arcane first; Elf not counted), with Connection to Nature. Identical to SOTN's table.
- **Magic items:** mage items (mage progression) and crusader items (Divine 2), as SOTN; enchanted daggers, slings, staffs, whips.
- **Key attributes:** **INT** (mage) and **WIL** (Divine 2).
- **Proficiencies:** 42 − 11 = 31. Mage progression: class proficiency at 1st, 6th; general at 1st, 5th, 9th.
- **Stronghold:** Sanctum and Dungeon (Arcane + Elf 4) or Fortified Church (Divine 2); takes **Sanctum and Dungeon**, renamed **Telesterion** (initiation hall), SOTN's followers.
- **XP:** 0 + 0 + 0 + 500 + 1,125 + 1,375 = **3,000 XP for 2nd level** (SOTN 3,000); doubled to 8th (7th 96,000 rounded to 95,000); then +150,000 (mage) + 50,000 (elf) = **+200,000 per level after 8th**.

## Class table
`acks/custom_class.py` (Arcane and Elf costs as `extra_costs`; elf XP and save bonus by the JJ rules). Arcane: JJ Arcane 4 progression; divine: JJ Divine 2 (= crusader). Rows 12-14 only for a corrupt elf become intelligent undead (ψ).

| Level | Title | XP | Hit Dice | Attack | Paralysis | Death | Blast | Implements | Spells | Arcane (1st-6th) | Divine (1st-6th) | Caster Level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Catechumen of the Secret Mysteries | 0 | 1d4+1 | 10+ | 12+ | 13+ | 15+ | 11+ | 11+ | 1 | 1 | 1 |
| 2 | Initiate of the Secret Mysteries | 3,000 | 2d4 | 10+ | 12+ | 13+ | 15+ | 11+ | 11+ | 2 | 2 | 2 |
| 3 | Acolyte of the Secret Mysteries | 6,000 | 3d4 | 10+ | 12+ | 13+ | 15+ | 11+ | 11+ | 2/1 | 2/1 | 3 |
| 4 | Catechist of the Secret Mysteries | 12,000 | 4d4 | 9+ | 11+ | 12+ | 14+ | 10+ | 10+ | 2/2 | 2/2 | 4 |
| 5 | Disciple of the Secret Mysteries | 24,000 | 5d4 | 9+ | 11+ | 12+ | 14+ | 10+ | 10+ | 2/2/1 | 2/2/1 | 5 |
| 6 | Sectator of the Secret Mysteries | 48,000 | 6d4 | 9+ | 11+ | 12+ | 14+ | 10+ | 10+ | 2/2/2 | 2/2/2 | 6 |
| 7 | Votary of the Secret Mysteries | 95,000 | 7d4 | 8+ | 10+ | 11+ | 13+ | 9+ | 9+ | 3/2/2/1 | 3/2/2/1 | 7 |
| 8 | Mystagogue of the Secret Mysteries | 190,000 | 8d4 | 8+ | 10+ | 11+ | 13+ | 9+ | 9+ | 3/3/2/2 | 3/3/2/2 | 8 |
| 9 | Hierophant of the Secret Mysteries | 390,000 | 9d4 | 8+ | 10+ | 11+ | 13+ | 9+ | 9+ | 3/3/3/2/1 | 3/3/3/2/1 | 9 |
| 10 | Hierophant, 10th level | 590,000 | 9d4+1\* | 7+ | 9+ | 10+ | 12+ | 8+ | 8+ | 3/3/3/3/2 | 3/3/3/3/2 | 10 |
| 11 | Hierophant, 11th level | 790,000 | 9d4+2\* | 7+ | 9+ | 10+ | 12+ | 8+ | 8+ | 4/3/3/3/2/1 | 4/3/3/3/2/1 | 11 |
| 12 | Hierophant, 12th level ψ | special ψ | as undead ψ | 7+ | 9+ | 10+ | 12+ | 8+ | 8+ | 4/4/3/3/3/2 | 4/4/3/3/3/2 | 12 |
| 13 | Hierophant, 13th level ψ | special ψ | as undead ψ | 6+ | 8+ | 9+ | 11+ | 7+ | 7+ | 4/4/4/3/3/2 | 4/4/4/3/3/2 | 13 |
| 14 | Hierophant, 14th level ψ | special ψ | as undead ψ | 6+ | 8+ | 9+ | 11+ | 7+ | 7+ | 4/4/4/4/3/3 | 4/4/4/4/3/3 | 14 |

\* No CON adjustment. SOTN titles are prefixed "Elven" (e.g. Elven Catechumen of the Secret Mysteries).

## Class powers
**Starting (1st level)**
- **Arcane Magic:** as a mage ([[Arcane Spell List]]); repertoire = arcane spells per day + INT bonus ([[Spell Repertoires]]); spellbook.
- **Divine Magic:** prayerful repertoire: Lawful, the hierophant list below; Chaotic, the cultist common list ([[Elven Cultist#Spell list]], without a god's bonus spells). ACKS II Divine 2 casts from **1st level** (SOTN: from 2nd, "Initiate of the Secret Mysteries").
- **Sensing Power** (Judge's call): senses magic and spellcasters ([[Sensing Power]]).
- **Theology** (starting power).
- **Elf racial powers:** as the [[Elven Cultist#Class powers|cultist]] (Animal Friendship, Attunement to Nature, Connection to Nature, Elf Tongues of antiquity).

**Additional**
- **3rd — Loremastery** ([[Custom Power Index (H-L)#Loremastery|Loremastery]]): 18+ −1 per level for occult runes, ancient history, artefacts, monster parts; identifies magic items as a 5th-level mage.
- **5th — Read Languages** ([[Custom Power Index (C-D)#Deciphering|Deciphering]]): ciphers, treasure maps, dead languages (not magic writing), 1 turn per page, **4+** (SOTN 5+); a failed page waits for the next level.
- **5th — Minor Magical Research; 9th — Major; 11th — Supreme** (as mage and crusader: ritual arcane and divine spells, constructs, crossbreeds; if Chaotic, necromancy and undeath).
- **9th — Unveil Esoteric Meaning** ([[Custom Power Index (T-Z)#Unveil Esoteric Meaning|Unveil Esoteric Meaning]]): library value doubled for research; library bonus up to +5.
- **9th — Telesterion** (Sanctum and Dungeon): 15,000gp+; **1d6 hierophants of 1st-3rd level and 2d6 0th-level elven aspirants** (INT/WIL above average; 80% quit within 1d6 months, SOTN); fed and lodged, no wages; a dungeon beneath draws monsters ([[Sanctums and Dungeons]]).
- **11th — Lore of Stars and Spheres** ([[Custom Power Index (H-L)#Lore of Stars and Spheres|Lore of Stars and Spheres]]): ritual magic at half material and research cost.

**Class proficiency list (31):** [[Alchemy]], [[Syncretism]] (apostasy), [[Battle Magic]], [[Beast Friendship]], [[Black Lore of Zahar]], [[Collegiate Wizardry]], [[Command]], [[Contemplation]], [[Art and Craft|Craft]], [[Diplomacy]], [[Elementalism]], [[Familiar]], [[Healing]], [[Illusion Resistance]], [[Knowledge]], [[Language]], [[Laying on Hands]], [[Leadership]], [[Loremastery]], [[Magical Engineering]], [[Mystic Aura]], [[Naturalism]], [[Prestidigitation]], [[Profession]], [[Prophecy]], [[Quiet Magic]], [[Sensing Evil]], [[Sensing Power]], [[Theology]], [[Transmogrification]], [[Unflappable Casting]].

**Template (SOTN p. 169): Astrologer** (INT 13, one bonus general proficiency). Proficiencies: [[Contemplation]], [[Knowledge]] (astrology), [[Collegiate Wizardry]]. Equipment: bronze-framed spellbook with *[[Slumber]]* (sleep) and *[[Discern Magic]]* (detect magic), holy symbol, rune-etched staff, blue cassock, leather belt, low boots, backpack, flask of holy water, astrologer's journal of constellations, quill and ink, 1 week's iron rations, 20gp. INT 16+ adds bonus general proficiencies.

## Divine spell list (Lawful)
Divine 2: 10 spells per level, at **ACKS II divine levels** (SOTN level noted). \* reversible; † ACKS II arcane-only, granted at SOTN's level (Judge's call); JC = Judge's call fill-in.

| Level | Spells |
| --- | --- |
| 1st | [[Word of Command]] (command word), [[Cure Light Injury]]\*, [[Discern Evil]]\*, [[Discern Magic]], [[Illumination]]\* (light), [[Holy Circle]]\* (protection from evil), [[Purify Food and Water]], [[Remove Fear]]\*, [[Sanctuary]], [[Salving Rest]] (JC) |
| 2nd | [[Augury]], [[Holy Blessing]]\* (bless), [[Bewitch Beast]] (charm animal), [[Cure Moderate Injury]], [[Divine Grace]], [[SOTN Spells#Display of Power]], [[Energy Protection]] (resist fire; resist cold, SOTN 1st), [[Righteous Wrath]], [[Noiselessness]] (silence 15’ radius), [[Speak with Beasts]] (speak with animals) |
| 3rd | [[Illumination, Perpetual]]\* (continual light), [[Cure Blindness]], [[Cure Disease]]\*, [[Cure Major Injury]], [[Rune of Warding]] (glyph of warding), [[Growth, Beast]] (growth of animals), [[Locate Object]]†, [[Holy Prayer]] (prayer), [[Remove Curse]]\*, [[Speak with Dead]], [[Holy Circle, Sustained]]\* (SOTN 4th). (11: Judge's call to keep the extra.) |
| 4th | [[Create Water]], [[Cure Serious Injury]]\*, [[Divination]], [[Inspire Awe]]\*, [[Neutralize Poison]]\*, [[Smite Undead]]\*, [[Speak with Plants]], [[Tongues]], [[Crafting]] (SOTN 5th), [[Spirit of Healing]] (JC) |
| 5th | [[Atonement]], [[Communion]] (commune), [[Cure Critical Injury]], [[Create Food]], [[Restore Life and Limb]]\*, [[Strength of Mind]]\*, [[True Seeing]], [[Fate]] (SOTN 4th), [[Healing Circle]] (JC), [[Lay of the Land]] (JC) |
| 6th | [[Dispel Evil]]\* (SOTN 5th), [[Quest]] (SOTN 5th), and JC: [[Banner of Invincibility]], [[Clairvoyancy, Greater]], [[Home Ward]], [[Prophetic Dream]], [[Locate Place of Power]], [[Spellwarded Zone]], [[Summon Winged Herald]], [[Salvific Rain]] |

## Corruption and undeath
As every elven class: [[Elven Cultist#The corrupt elves of antiquity (SOTN p. 162)]] (era table, 14th-level advancement in undeath, Tampering with Mortality penalties). **Undead XP:** 6 build points outside Hit Dice → class abilities count **\*\*\*** (SOTN p. 162, on the ACKS II build; Judge's call).

## As a mummy's abilities
A mummy "with the class abilities of an Nth-level elven hierophant" keeps its own HD, attack throw, saves, AC and mummy powers ([[Mummy]]) and adds the spells and powers below (Chaotic: divine spells from the cultist common list; Lawful: the list above). Levels above 11th exist only for corrupt elves in undeath. XP: +3 asterisks (\*\*\*).

| Level | Arcane per day | Divine per day (ACKS II) | SOTN divine prints | Caster level | Powers in effect |
| --- | --- | --- | --- | --- | --- |
| 4 | 2/2 | 2/2 | 2/1 | 4th | Sensing Power, Theology, Loremastery (15+) |
| 6 | 2/2/2 | 2/2/2 | 2/2/1/1 | 6th | + Read Languages (4+), minor magical research |
| 8 | 3/3/2/2 | 3/3/2/2 | 3/3/2/2/1 | 8th | as 6th (Loremastery 11+) |
| 9 | 3/3/3/2/1 | 3/3/3/2/1 | 3/3/3/2/2 | 9th | + Unveil Esoteric Meaning, major magical research |
| 12 ψ | 4/4/3/3/3/2 | 4/4/3/3/3/2 | 5/5/4/4/3 | 12th | + Lore of Stars and Spheres, supreme magical research (Loremastery 7+) |

Arcane counts match SOTN's table at every level; the ACKS II divine column replaces SOTN's.

## Converted from ACKS I
- **From SOTN's text:** requirements, d4, 11th level, mage combat and weapons, arcane as a mage, divine as a cleric (from 2nd), Lawful and Chaotic lists, mage and cleric items, Loremastery (3rd), read languages (5th, 5+), esoteric meaning and telesterion (9th), lore of stars and spheres (11th), titles, Astrologer template, mage saves with the elven −1 (identical in ACKS II).
- **Judge's calls:** Divine 2 + Arcane 2 + Elf 2 (gives SOTN's exact 3,000 XP and 11th level); rebuke undead traded; divine casting from 1st (JJ Divine 2) instead of 2nd; Sensing Power for the fighting-style power; Theology as starting power; the code; spell mappings and fill-ins; Read Languages at ACKS II's 4+.
- **Book errors:** the divine paragraph reads "The number and level of divine spells an use" (word missing); the warlord's save table on p. 170 is captioned "Elven Hierophant (Mage)" (see [[Elven Warlord]]).
