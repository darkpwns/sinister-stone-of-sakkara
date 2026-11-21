---
type: custom-class
tags: [sakkara/secret]
source: "JJ ch. 12 custom class build of the ACKS I Elven Enchanter (AX3 pp. 53, 96)"
build: "HD 0, Fighting 0, Thievery 1, Arcane 3, Elf 1"
xp_2nd: 2750
level_limit: 12
saves_as: mage
key_attributes: "INT"
requirements: "INT 9 (elf)"
builds_file: "Adventure/AX3/Classes/ax3-class-builds-demihuman.yaml"
---

# Elven Enchanter

## Concept and role
The elven magician of glamour and dream: a full arcane caster whose enchantments and illusions bite harder than a human mage's, who dazzles mortals with a presence that edges into bewitchment, and who keeps the old elven lore. Enchanters adventure to recover lost arts of elven magic (Nara, AX3 p. 96) or to test their glamours on the wider world. Nearest RR class: the [[Mage]] (same spells per day and research), but the enchanter trades a little XP and a lower level limit for elven traits, d4+1 at 1st, and four enchantment-themed powers; unlike the [[Elven Spellsword]] it has no fighting ability or armour.

## Build (JJ ch. 12, Custom Racial Classes)
- **Build points:** HD 0, Fighting 0, Thievery 1, Arcane 3 = 4 in the human categories, plus Elf 1 = **5 build points → 12th level limit** (Custom Racial Classes, JJ pp. 299-300).
- **Requirements:** INT 9+ (elven classes; moot, INT is the key attribute).
- **Hit Dice 0** ([[Hit Dice Value]]): d4; +1 to the HD roll at 1st level (Connection to Nature); +1 hp per level after 9th (mage progression). 0 XP.
- **Fighting 0 (Mage)** ([[Fighting Value]]): attack throws +2 per 6 levels, no cleaves. Restricted weapons: dagger, dart, sling, staff. No armour (the elven right to cast in permitted armour has nothing to apply to). Fighting styles: single weapon, missile weapon, and **two-handed weapon** (staff). 0 XP.
- **Thievery 1** ([[Thievery Value]]): 4 selections, all traded for custom powers. 250 XP.
- **Divine 0.**
- **Arcane 3** ([[Arcane Value]]): 1,875 XP less the elven 125 XP discount = 1,750 XP ([[Elven Custom Classes]]).
- **Elf 1:** the four elf powers; Arcane 3 + Elf 1 = effective **Arcane 4**: casts and researches as a [[Mage]] (Arcane 4 progression). 750 XP.
- **Trade-offs taken:** Thievery 1 → 4 custom powers. None in Fighting (Fighting 0 has only its single optional style).
- **Custom powers:** Glamorous Aura (1), Mastery of Enchantments and Illusions (1), Prestidigitation (1), Loremastery (1). Starting general proficiency power: **Collegiate Wizardry** (as the mage and spellsword).
- **Drawbacks:** none.
- **Saving throws:** Arcane 3 is the highest category → **mage**, with Connection to Nature's +1 on Paralysis and Spells.
- **Magic items:** mage items (mage progression; Arcane 3 + Elf 1); enchanted daggers, darts, slings and staffs.
- **Key attribute:** **INT** (mage progression; Arcane 3 adds INT again).
- **Proficiencies:** 42 − 12 = 30 on the class list. Progression as mage-progression classes: class proficiency at 1st, 6th, 12th; general at 1st, 5th, 9th.
- **Stronghold:** qualifies for Sanctum and Dungeon (Arcane + Elf 4) and Hideout (Thievery 1); takes **Sanctum and Dungeon**, renamed **Enchanted Bower** (a tower or hall in a wild, beautiful place).
- **XP:** 0 + 0 + 250 + 1,750 + 750 = **2,750 XP for 2nd level**; doubled to 8th (7th rounded to 90,000); then +150,000 (mage) + 50,000 (elf) = **+200,000 per level after 8th**.

## Class table
From `acks/custom_class.py` with this build (Arcane Value cost entered as `extra_costs`, which the calculator lacks; Elf 1 build point, elven +50,000 XP after 8th and Connection to Nature added by the JJ rules). Spells per day: JJ Arcane 4 progression (= mage).

| Level | Title | XP | Hit Dice | Attack | Paralysis | Death | Blast | Implements | Spells | Spells/day (1st-6th) | Caster Level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Dreamer | 0 | 1d4+1 | 10+ | 12+ | 13+ | 15+ | 11+ | 11+ | 1 | 1 |
| 2 | Weaver | 2,750 | 2d4 | 10+ | 12+ | 13+ | 15+ | 11+ | 11+ | 2 | 2 |
| 3 | Glamourist | 5,500 | 3d4 | 10+ | 12+ | 13+ | 15+ | 11+ | 11+ | 2/1 | 3 |
| 4 | Charmer | 11,000 | 4d4 | 9+ | 11+ | 12+ | 14+ | 10+ | 10+ | 2/2 | 4 |
| 5 | Beguiler | 22,000 | 5d4 | 9+ | 11+ | 12+ | 14+ | 10+ | 10+ | 2/2/1 | 5 |
| 6 | Spellsinger | 44,000 | 6d4 | 9+ | 11+ | 12+ | 14+ | 10+ | 10+ | 2/2/2 | 6 |
| 7 | Mesmerist | 90,000 | 7d4 | 8+ | 10+ | 11+ | 13+ | 9+ | 9+ | 3/2/2/1 | 7 |
| 8 | Fey-Seer | 180,000 | 8d4 | 8+ | 10+ | 11+ | 13+ | 9+ | 9+ | 3/3/2/2 | 8 |
| 9 | Enchanter | 380,000 | 9d4 | 8+ | 10+ | 11+ | 13+ | 9+ | 9+ | 3/3/3/2/1 | 9 |
| 10 | Enchanter, 10th level | 580,000 | 9d4+1\* | 7+ | 9+ | 10+ | 12+ | 8+ | 8+ | 3/3/3/3/2 | 10 |
| 11 | Enchanter, 11th level | 780,000 | 9d4+2\* | 7+ | 9+ | 10+ | 12+ | 8+ | 8+ | 4/3/3/3/2/1 | 11 |
| 12 | Enchanter, 12th level | 980,000 | 9d4+3\* | 7+ | 9+ | 10+ | 12+ | 8+ | 8+ | 4/4/3/3/3/2 | 12 |

\* No CON adjustment to this flat bonus.

## Class powers
**Starting (1st level)**
- **Arcane Magic:** learns and casts arcane spells as a mage ([[Arcane Spell List]]); repertoire = spells per day per level + INT bonus ([[Spell Repertoires]]); spellbook.
- **Collegiate Wizardry** (starting general proficiency power): as the mage's ([[Collegiate Wizardry]]); Argollëan enchanters' schools.
- **Glamorous Aura:** +1 on reaction rolls to impress and intimidate; a total of 12+ leaves the subjects acting as if bewitched in his presence (the [[Mystic Aura]] proficiency as a power).
- **Mastery of Enchantments and Illusions:** enchantment and illusion spells calculated at +2 caster levels, targets −2 on their saves; +2 caster levels for research eligibility, +2 on research throws and +10% research rate for that magic. With the [[Mastery of Enchantments & Illusions]] proficiency as well: +3 caster levels and −3 on saves.
- **Prestidigitation:** at-will petty illusions and tricks; magical pickpocketing as a thief of half his level ([[Prestidigitation]]).
- **Loremastery:** 18+ −1 per level to decipher occult runes, recall ancient history, identify artefacts and special monster parts; identifies magic items as a 5th-level mage ([[Loremastery]]).
- **Elf racial powers:** Animal Friendship (at a fastness only), Attunement to Nature, Connection to Nature, Elf Tongues.

**Additional** (as the mage)
- **Minor Magical Research (5th level)**, **Major Magical Research (9th level)**, **Supreme Magical Research (11th level)** ([[Magic Research]]).
- **Enchanted Bower (9th level):** a sanctum worth 15,000gp+ draws 2d6 0th-level apprentices and 1d6 enchanters of 1st-3rd level within 1d3 months; a dungeon beneath it draws monsters ([[Sanctums and Dungeons]]).

**Class proficiency list (30):** [[Alchemy]], [[Battle Magic]], [[Beast Friendship]], [[Black Lore of Zahar]], [[Bright Lore of Aura]], [[Collegiate Wizardry]], [[Counterspelling]], [[Diplomacy]], [[Elementalism]], [[Expanded Repertoire]], [[Experimenting]], [[Familiar]], [[Healing]], [[Illusion Resistance]], [[Knowledge]], [[Language]], [[Magical Engineering]], [[Magical Music]], [[Mastery of Conjuration & Summoning]], [[Mastery of Enchantments & Illusions]], [[Mystic Aura]], [[Naturalism]], [[Performance]], [[Quiet Magic]], [[Seduction]], [[Sensing Power]], [[Soothsaying]], [[Transmogrification]], [[Unflappable Casting]], [[Wakefulness]].

**Templates:** AX3 names one, *Antiquarian* (Nara). Judge's call for it: Knowledge (history), Sensing Power, and Language (Ancient Elven) as the INT 13-15 bonus proficiency; spellbook with *[[Discern Magic]]* and *[[Beguile Humanoid]]*. Other templates as needed, modelled on the [[Elven Spellsword]]'s.

## Converted from ACKS I
- **From AX3's text:** only the class name, the Antiquarian template name, and Nara's 1st level and motive (AX3 p. 96); the class's place on the NPC Class table (AX3 p. 53, Mage type 95-96). AX3 gives no enchanter statline.
- **From the JJ Custom Power Index's class lists** (powers it says the ACKS I Elven Enchanter used): Glamorous Aura, Keen Eyes, Mastery of Enchantments and Illusions, Prestidigitation. Keen eyes was removed in ACKS II (Attunement to Nature replaces it).
- **From my recollection of ACKS I** (uncertain, not a quotation): the enchanter as the elven specialist in charm and illusion magic, spellcasting at about a mage's power; I do not recall its build, XP or level limit.
- **Judge's calls:** Arcane 3 + Elf 1 (full mage casting); Loremastery as the fourth power (fits the antiquarian scholars AX3 names); Enchanted Bower; Antiquarian template contents; level titles.

## NPCs of this class in AX3
- **Nara** (AX3 p. 96; `Tables/ax3-old-elven-victim.yaml` 11-12, [[Doppelganger Den]] 4-5): elven enchanter from Northern Argollë, come to learn lost elven arts; dead in the abattoir or a captive in the cell. Revised statline (Judge's call; AX3 gives none): **Elven Enchanter 1** (Antiquarian); attributes unrolled (assume INT 13-15); AC 0 (captive: no armour or gear, spellbook lost to the doppelgängers); HD 1, hp 1d4+1; dagger (if armed) **10+** (enchanter 1, no STR/DEX known), D 1d4; saves (mage 1 + Connection to Nature, WIL unknown): **Paralysis 12+, Death 13+, Blast 15+, Implements 11+, Spells 11+**; 1 1st-level spell per day from her repertoire (1 + INT bonus: [[Discern Magic]], [[Beguile Humanoid]]); the lost spellbook matters only for changing the repertoire ([[Spell Repertoires]]); ML 0; AL L (Judge's call); XP 10 (level 1 as HD, no special abilities; RR p. 310). Rescued, she is a natural henchman candidate.
