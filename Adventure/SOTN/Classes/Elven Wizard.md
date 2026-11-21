---
type: custom-class
tags: [sakkara/secret]
source: "JJ ch. 12 custom class build of the ACKS I Elven Wizard (SOTN pp. 170-173)"
build: "HD 0, Fighting 0, Thievery 1, Arcane 3, Elf 1"
xp_2nd: 2750
level_limit: 12
saves_as: mage
key_attributes: "INT and CHA"
requirements: "INT 9"
hit_dice: "1d4"
builds_file: "Adventure/SOTN/Classes/sotn-class-builds.yaml"
---

# Elven Wizard

Up: [[SOTN Hub]] · Builder: [[JJ 12 Custom Classes]], [[Creating a Custom Class]] · Build record: `Classes/sotn-class-builds.yaml` (`Elven Wizard`) · See also [[Elven Enchanter]] (same build, rival tradition), [[Elven Cultist]] (the corruption rules)

## Concept and role
The scholar-mage of an elven **college of wizardry**: Artifice (magic as mechanism; friends of dwarves), Nature (magic as a force of life; friends of beasts and shamans), and the extinct colleges of **Necromancy** (life, death and undeath as tools of immortality) and **Transmogrification** (flesh reshaped; monstrous servants) whose members wove much of the Nethercity's horror. Today most elven wizards are of Nature, a few of Artifice; whether the dark colleges survive is the Judge's choice (SOTN p. 171). A full arcane caster whose college sets his four weapons and five powers.
- **Nearest RR class:** the [[Mage]] (same spells, research, saves and combat). It does not suffice: it is human, has no college powers or elf powers, and a different XP and level limit. The campaign's [[Elven Enchanter]] has the same build; SOTN calls the enchanters a rival, quicker tradition with fewer powers, and here the two differ only in their custom powers.

## Build (JJ ch. 12, Custom Racial Classes)
- **Build points:** HD 0, Fighting 0, Thievery 1, Arcane 3 = 4, plus Elf 1 = **5 build points → 12th level limit** (SOTN 12th).
- **Requirements:** INT 9 (elven classes; moot).
- **Hit Dice 0:** d4; +1 HD roll at 1st; +1 hp per level after 9th. 0 XP.
- **Fighting 0 (Mage):** +2 per 6 levels, no cleaves; restricted weapons, the **college's four** (all from the JJ restricted ten); no armour, no shields, no dual weapons (SOTN); keeps the **two-handed** style (staff 1d6). 0 XP.
- **Thievery 1:** 4 selections, all traded for custom powers. 250 XP.
- **Arcane 3** (1,875 − 125 elven = 1,750 XP) + **Elf 1** (750 XP) = effective **Arcane 4**: casts and researches as a mage.
- **Custom powers (4 → 6):** one 1st-level selection is the college's 1st-level power; one is **College Training** (Judge's call, below); one is traded for the college's **3rd + 11th** powers; one for its **5th + 9th** powers ([[Custom Power Trade-Offs]]). Starting general proficiency power: **Collegiate Wizardry** (membership of his college).
- **Saving throws:** Arcane 3 highest → **mage**, with Connection to Nature. Identical to SOTN's table.
- **Magic items:** mage items; enchanted versions of his college's weapons.
- **Key attributes:** **INT** (mage) and **CHA** (SOTN; Judge's call to add it).
- **Proficiencies:** 42 − 12 = 30, plus the college's four. Mage progression: class proficiency at 1st, 6th, 12th; general at 1st, 5th, 9th.
- **Stronghold:** Sanctum and Dungeon (Arcane + Elf 4) or Hideout; takes **Sanctum and Dungeon** (a tower).
- **XP:** 0 + 0 + 250 + 1,750 + 750 = **2,750 XP for 2nd level** (SOTN 2,700); doubled to 8th (7th 88,000 rounded to 90,000); then +150,000 (mage) + 50,000 (elf) = **+200,000 per level after 8th** (SOTN also +200,000).

## Class table
`acks/custom_class.py` (Arcane and Elf costs as `extra_costs`; elf XP and save bonus by the JJ rules). Spells: JJ Arcane 4 (= mage; identical to SOTN's table). Rows 13-14 only for a corrupt elf become intelligent undead (ψ).

| Level | Title | XP | Hit Dice | Attack | Paralysis | Death | Blast | Implements | Spells | Spells/day (1st-6th) | Caster Level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Elven Arcanist | 0 | 1d4+1 | 10+ | 12+ | 13+ | 15+ | 11+ | 11+ | 1 | 1 |
| 2 | Elven Seer | 2,750 | 2d4 | 10+ | 12+ | 13+ | 15+ | 11+ | 11+ | 2 | 2 |
| 3 | Elven Theurgist | 5,500 | 3d4 | 10+ | 12+ | 13+ | 15+ | 11+ | 11+ | 2/1 | 3 |
| 4 | Elven Magician | 11,000 | 4d4 | 9+ | 11+ | 12+ | 14+ | 10+ | 10+ | 2/2 | 4 |
| 5 | Elven Thaumaturge | 22,000 | 5d4 | 9+ | 11+ | 12+ | 14+ | 10+ | 10+ | 2/2/1 | 5 |
| 6 | Elven Sorcerer | 44,000 | 6d4 | 9+ | 11+ | 12+ | 14+ | 10+ | 10+ | 2/2/2 | 6 |
| 7 | Elven Conjurer | 90,000 | 7d4 | 8+ | 10+ | 11+ | 13+ | 9+ | 9+ | 3/2/2/1 | 7 |
| 8 | Elven Mage | 180,000 | 8d4 | 8+ | 10+ | 11+ | 13+ | 9+ | 9+ | 3/3/2/2 | 8 |
| 9 | Elven Wizard | 380,000 | 9d4 | 8+ | 10+ | 11+ | 13+ | 9+ | 9+ | 3/3/3/2/1 | 9 |
| 10 | Elven Wizard, 10th level | 580,000 | 9d4+1\* | 7+ | 9+ | 10+ | 12+ | 8+ | 8+ | 3/3/3/3/2 | 10 |
| 11 | Elven Wizard, 11th level | 780,000 | 9d4+2\* | 7+ | 9+ | 10+ | 12+ | 8+ | 8+ | 4/3/3/3/2/1 | 11 |
| 12 | Elven Wizard, 12th level | 980,000 | 9d4+3\* | 7+ | 9+ | 10+ | 12+ | 8+ | 8+ | 4/4/3/3/3/2 | 12 |
| 13 | Elven Wizard, 13th level ψ | special ψ | as undead ψ | 6+ | 8+ | 9+ | 11+ | 7+ | 7+ | 4/4/4/3/3/2 | 13 |
| 14 | Elven Wizard of the Council ψ | special ψ | as undead ψ | 6+ | 8+ | 9+ | 11+ | 7+ | 7+ | 4/4/4/4/3/3 | 14 |

\* No CON adjustment.

## Class powers
**All wizards**
- **Arcane Magic:** as a mage ([[Arcane Spell List]]); repertoire = spells per day + INT bonus ([[Spell Repertoires]]); spellbook.
- **Collegiate Wizardry** (starting power, his college) ([[Collegiate Wizardry]]).
- **College Training** (1st, Judge's call): one class proficiency from his college's four additions, free. SOTN says each college adds four proficiencies to the class list but never names them; the Judge's call lists are below.
- **Elf racial powers:** as the [[Elven Cultist#Class powers|cultist]] (Animal Friendship, Attunement to Nature, Connection to Nature, Elf Tongues of antiquity).
- **Minor Magical Research (5th)**, **Major (9th)**, **Supreme (11th)**: as the mage (ritual 7th-9th, constructs, crossbreeds; if Chaotic, necromancy and undeath) ([[Magic Research]]).
- **Sanctum (9th):** 15,000gp+; **1d6 wizards of 1st-3rd level and 2d6 0th-level elven apprentices** (many quit after 1d6 months, SOTN); fed and lodged, no wages; a dungeon draws monsters ([[Sanctums and Dungeons]]).

**Colleges** ([[Custom Power Index]] names; spell-like powers priced by [[Custom Power Creation#Spellcasting and Spell-Like Abilities]]: a 3rd-level spell once per day with 1 round casting = 1 power; caster level = his class level)

| College | Weapons | 1st | 3rd | 5th | 9th | 11th | Added proficiencies (Judge's call) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Artifice** | dagger, dart, staff, whip | [[Magical Engineering]] | [[Siege Engineering]] | [[Dispel Magic]] once per day, 1 round | [[Custom Power Index (E-G)#Flawless Precision\|Flawless Precision]] (ordinary research fails only on a natural 1) | [[Custom Power Index (M-P)#Marvelous Machines\|Marvelous Machines]] (constructs at half cost) | [[Engineering]], [[Experimenting]], [[Counterspelling]], [[Art and Craft\|Craft]] |
| **Nature** | club, dagger, sling, staff | [[Custom Power Index (E-G)#Friend of Birds and Beasts\|Friend of Birds and Beasts]] (+2 reactions with animals, animal henchmen, identifies flora and fauna 11+; stacks with [[Beast Friendship]]) | [[Martial Training]] (short bow, short sword, spear; ACKS II option 7 adds javelin, required with spear) | [[Skinchange]] once per day, 1 round | [[Custom Power Index (T-Z)#Totem Animal\|Totem Animal]] (animal companion, as a [[Shaman]]'s, with totem benefit) | Steward of the Wild: [[Passing Without Trace]] within his domain, and ordinary animals within 5 miles of his home or sanctum kind and helpful (Animal Friendship widened; 1 power, Judge's call) | [[Passing Without Trace]], [[Survival]], [[Tracking]], [[Animal Training]] |
| **Necromancy** (extinct) | club, dagger, dart, staff | [[Custom Power Index (Q-S)#Secrets of the Dark Arts\|Secrets of the Dark Arts]] (controls undead as a Chaotic crusader of half his level, round down (SOTN rounds up); −2 on targets' Death saves; necromancy +2 caster levels; stacks with [[Black Lore of Zahar]]) | [[Healing]] | [[Speak with Dead]] once per day, 1 round | [[Custom Power Index (H-L)#Lordship Over the Undead\|Lordship Over the Undead]] | [[Custom Power Index (Q-S)#Secrets of Life and Death\|Secrets of Life and Death]] (necromancy at half cost) | [[Poisoning]], [[Sensing Good]], [[Mastery of Conjuration & Summoning]], [[Intimidation]] |
| **Transmogrification** (extinct) | club, dagger, dart, whip | [[Transmogrification]] | [[Custom Power Index (A-B)#Abominable Mutation\|Abominable Mutation]] (beast eyes: Lightless Vision 60’, −2 reactions; claw-like nails: 2 × 1d4−1, −2 reactions and delicate work; scaly skin: +2 AC, −25% speed, −4 reactions; tentacles: hands free, 2 × 1d3−1, −2 reactions; or an AX1 mutation) | [[Skinchange]] once per day, 1 round | [[Custom Power Index (H-L)#Hideous Servant\|Hideous Servant]] (totem-like servant of two animals, no totem benefit) | [[Custom Power Index (Q-S)#Shape Flesh and Bone\|Shape Flesh and Bone]] (crossbreeds at half cost) | [[Animal Training]], [[Experimenting]], [[Poisoning]], [[Mastery of Conjuration & Summoning]] |

**Class proficiency list (30, plus the college's four):** [[Alchemy]], [[Battle Magic]], [[Black Lore of Zahar]], [[Beast Friendship]], [[Collegiate Wizardry]], [[Command]], [[Contemplation]], [[Art and Craft|Craft]] (crafting), [[Divine Blessing]], [[Divine Health]], [[Elementalism]], [[Familiar]], [[Healing]], [[Knowledge]], [[Language]], [[Laying on Hands]], [[Leadership]], [[Magical Engineering]], [[Mystic Aura]], [[Naturalism]], [[Performance]], [[Prophecy]], [[Profession]], [[Quiet Magic]], [[Righteous Rebuke]] (righteous turning; of use only to a necromancer's undead control, Judge's call), [[Sensing Evil]], [[Sensing Power]], [[Soothsaying]], [[Transmogrification]], [[Unflappable Casting]].

**Template (SOTN p. 173): Augur.** Proficiencies: [[Prophecy]], [[Performance]] (storytelling). Equipment: rolled papyrus spellbook with *[[Beguile Humanoid]]* (charm person) and *Magic Mouth* (Judge's call: no ACKS II equivalent; substitute [[Auditory Illusion]]), elaborately carved staff, blue robe with crescents, leather belt, low boots, backpack, ornamental crystal ball (20gp), quill and ink, 2 weeks' iron rations, 25gp. INT 13+ adds bonus general proficiencies and starting spells. SOTN names no college for it (Judge's call: Nature).

## Corruption and undeath
As every elven class: [[Elven Cultist#The corrupt elves of antiquity (SOTN p. 162)]]. **Undead XP:** 5 build points outside Hit Dice → class abilities count **\*\*** (SOTN p. 162, on the ACKS II build; Judge's call).

## As a mummy's abilities
A mummy "with the class abilities of an Nth-level elven wizard" (most often a transmogrifier or necromancer in the Nethercity) keeps its own HD, attack throw, saves, AC and mummy powers ([[Mummy]]) and adds arcane spells at caster level N (repertoire = spells per day + INT bonus, from the [[Arcane Spell List]]; SOTN's room keys give the spells), Collegiate Wizardry, College Training, the elf powers and its college's powers to level N. XP: +2 asterisks (\*\*).

| Level | Spells per day | Caster level | College powers in effect (1st + College Training always) | Research |
| --- | --- | --- | --- | --- |
| 4 | 2/2 | 4th | + 3rd-level power | — |
| 6 | 2/2/2 | 6th | + 5th-level spell-like power (1/day) | minor |
| 8 | 3/3/2/2 | 8th | as 6th | minor |
| 9 | 3/3/3/2/1 | 9th | + 9th-level power | major |
| 12 | 4/4/3/3/3/2 | 12th | + 11th-level power | supreme |

By college at 9th, for instance: Necromancy = Secrets of the Dark Arts (controls undead as a 4th-level crusader), Healing, speak with dead 1/day, Lordship Over the Undead; Transmogrification = Transmogrification, a mutation, skinchange 1/day, a hideous servant. Spell counts match SOTN's table at every level.

## Converted from ACKS I
- **From SOTN's text:** INT and CHA, INT 9, d4, 12th level, mage combat and spells, mage items, the four colleges with weapons and five powers each, research, sanctum, titles, Augur template, mage saves with the elven −1.
- **Judge's calls:** the build (as the [[Elven Enchanter]]: Thievery 1, Arcane 3, Elf 1); College Training for the fourth power selection; the four added proficiencies per college; Steward of the Wild priced as one power; Martial Training's javelin; Necromancy's undead control rounding down (ACKS II power); CHA as second key attribute; the Augur's college and Magic Mouth substitute.
- **Book errors:** the text says "An enchanter's repertoire" for the wizard's; the four college proficiencies it promises are never listed; the attack and save table's Paralysis cell at 1st-3rd level is blank (12+ by the progression); Necromancy's text calls its member "the sorcerer" (also Transmogrification's 11th).
