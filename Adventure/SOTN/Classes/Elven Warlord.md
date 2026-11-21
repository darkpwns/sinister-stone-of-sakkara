---
type: custom-class
tags: [sakkara/secret]
source: "JJ ch. 12 custom class build of the ACKS I Elven Warlord (SOTN pp. 169-170)"
build: "HD 2, Fighting 2, Elf 0"
xp_2nd: 2375
level_limit: 13
saves_as: fighter
key_attributes: "STR and CHA"
requirements: "INT 9"
hit_dice: "1d8"
builds_file: "Adventure/SOTN/Classes/sotn-class-builds.yaml"
---

# Elven Warlord

Up: [[SOTN Hub]] · Builder: [[JJ 12 Custom Classes]], [[Creating a Custom Class]] · Build record: `Classes/sotn-class-builds.yaml` (`Elven Warlord`) · See also [[Elven Cultist]] (the corruption rules), [[Nethercity History]]

## Concept and role
The war-leader of Argollë's conquering youth, who led rangers and spellswords against men, dwarves and orcs through Rorn, Southern Argollë, Meniri, Krysea and Zahar, and came home to a memorial or a triumph and a lordship. Northern Argollë has made no war in two centuries since losing the south in 166 IY (SOTN p. 169). A pure elven fighter: d8 Hit Dice, fighter attacks, damage and cleaves, medium armour, and leadership powers from 5th level.
- **Nearest RR class:** the [[Fighter]] (same Hit Dice, attacks, damage, cleaves, Battlefield Prowess) for a human, or the [[Elven Spellsword]] for an elf. Neither suffices: the RR has no non-casting elven fighter; the spellsword trades d8 and leadership for spells and stops at 10th; the fighter is human, unrestricted in armour and weapons, and lacks Inspire Courage, Student of War and Lion-Hearted Leader.

## Build (JJ ch. 12, Custom Racial Classes)
- **Build points:** HD 2, Fighting 2 = 4, plus Elf 0 = **4 build points → 13th level limit** (SOTN 13th).
- **Requirements:** INT 9 (elven classes).
- **Hit Dice 2:** d8, Mortal Wounds +4; +1 HD roll at 1st (Connection to Nature); +2 hp per level after 9th (fighter). 1,000 XP.
- **Fighting 2 (Fighter):** +2 attack per 3 levels; damage bonus +1 at 1st and +1 every 3 levels (melee and missile; SOTN's +1 at 3rd, 6th, 9th, 12th is the same); 1 cleave per level; all three optional styles (weapon and shield, two-handed, dual: SOTN's). Trade-offs:
  - Armour Heavy → **Medium** (chain mail or lighter, SOTN): 1 custom power, no XP.
  - Weapons Unrestricted → **Broad** with (iv) any swords, daggers, spears and polearms and (v) all missile weapons (exactly SOTN's list; meets the elven two-of-bows/swords/daggers rule): 1 custom power, **+250 XP**.
  - 1,000 + 250 = 1,250 XP.
- **Elf 0:** the four elf powers. 125 XP.
- **Custom powers (2), both level-locked:** 1 → **Armor or Martial Training (3rd) + Lion-Hearted Leader (11th)**; 1 → **Inspire Courage (5th) + Student of War (9th)**. Plus **Battlefield Prowess** at 5th as the stronghold bonus power (below). Starting general proficiency power: **Manual of Arms** (as the fighter).
- **Saving throws:** Fighting 2 → **fighter**, with Connection to Nature (+1 Paralysis and Spells).
- **Magic items:** fighter items; enchanted swords, daggers, spears, polearms, missile weapons, medium or lighter armour, shields.
- **Key attributes:** **STR** (fighter) and **CHA** (SOTN; Judge's call to add it for flavour, as the JJ allows).
- **Proficiencies:** 42 − 13 = 29. Fighter progression: class proficiency at 1st, 3rd, 6th, 9th, 12th; general at 1st, 5th, 9th, 13th.
- **Stronghold:** Castle (Fighting 1+) or Elven Fastness (Elf 0 + Fighting 2); takes **Elven Fastness** (SOTN). Having no spells and qualifying for Castle, it also gains the Castle morale power: **Battlefield Prowess** at 5th ([[Strongholds and Followers]]).
- **XP:** 1,000 + 1,250 + 125 = **2,375 XP for 2nd level** (SOTN 2,125: ACKS I had no weapon trade-off penalty); doubled to 8th (7th 76,000 rounded to 75,000); then +120,000 (fighter) + 50,000 (elf) = **+170,000 per level after 8th** (SOTN's increment is also 170,000).

## Class table
`acks/custom_class.py` (Elf 0 as `extra_costs`, weapon trade-off 1; elf XP and save bonus by the JJ rules). Row 14 only for a corrupt elf become intelligent undead (ψ).

| Level | Title | XP | Hit Dice | Attack | Paralysis | Death | Blast | Implements | Spells | Damage bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Elven Man-at-Arms | 0 | 1d8+1 | 10+ | 12+ | 14+ | 15+ | 16+ | 16+ | +1 |
| 2 | Elven Warrior | 2,375 | 2d8 | 9+ | 11+ | 13+ | 14+ | 15+ | 15+ | +1 |
| 3 | Elven Swordmaster | 4,750 | 3d8 | 9+ | 11+ | 13+ | 14+ | 15+ | 15+ | +2 |
| 4 | Elven Hero | 9,500 | 4d8 | 8+ | 10+ | 12+ | 13+ | 14+ | 14+ | +2 |
| 5 | Elven Exemplar | 19,000 | 5d8 | 7+ | 9+ | 11+ | 12+ | 13+ | 13+ | +2 |
| 6 | Elven Myrmidon | 38,000 | 6d8 | 7+ | 9+ | 11+ | 12+ | 13+ | 13+ | +3 |
| 7 | Elven Champion | 75,000 | 7d8 | 6+ | 8+ | 10+ | 11+ | 12+ | 12+ | +3 |
| 8 | Elven Epic Hero | 150,000 | 8d8 | 5+ | 7+ | 9+ | 10+ | 11+ | 11+ | +3 |
| 9 | Elven Warlord | 320,000 | 9d8 | 5+ | 7+ | 9+ | 10+ | 11+ | 11+ | +4 |
| 10 | Elven Warlord, 10th level | 490,000 | 9d8+2\* | 4+ | 6+ | 8+ | 9+ | 10+ | 10+ | +4 |
| 11 | Elven Warlord, 11th level | 660,000 | 9d8+4\* | 3+ | 5+ | 7+ | 8+ | 9+ | 9+ | +4 |
| 12 | Elven Warlord, 12th level | 830,000 | 9d8+6\* | 3+ | 5+ | 7+ | 8+ | 9+ | 9+ | +5 |
| 13 | Elven Warlord, 13th level | 1,000,000 | 9d8+8\* | 2+ | 4+ | 6+ | 7+ | 8+ | 8+ | +5 |
| 14 | Elven Overlord, 14th level ψ | special ψ | as undead ψ | 1+ | 3+ | 5+ | 6+ | 7+ | 7+ | +5 |

\* No CON adjustment. Attack throws match SOTN's; saves are ACKS II fighter values (SOTN prints ACKS I's: 14/14/16/16/16 at 1st).

## Class powers
**Starting (1st level)**
- **Fighter combat:** damage bonus, 1 cleave per level ([[Cleaving]]), Mortal Wounds +4.
- **Manual of Arms** (starting power): trains troops as the fighter's ([[Manual of Arms]]).
- **Elf racial powers:** as the [[Elven Cultist#Class powers|cultist]] (Animal Friendship, Attunement to Nature, Connection to Nature, Elf Tongues of antiquity).

**Additional**
- **3rd — Armor or Martial Training** (choose once): [[Custom Power Index (A-B)#Armor Training|Armor Training]] (heavy armour: banded, lamellar, plate) or [[Martial Training]] (one more weapon group, e.g. axes, maces, staffs; SOTN "any weapons not already on his list", read as one group, Judge's call).
- **5th — Inspire Courage** ([[Custom Power Index (H-L)#Inspire Courage|Inspire Courage]]): 1 round of oration, up to 30 allies within 50’ inspired for 1 turn (+1 attack, AC, morale, saves v. magical fear); once per day per class level; not on those already fighting. (SOTN: +1 damage instead of AC; once per day at 5th, +1 per level after; not on other alignments.)
- **5th — Battlefield Prowess** ([[Custom Power Index (A-B)#Battlefield Prowess|Battlefield Prowess]]): henchmen and mercenaries +1 morale while he leads them.
- **9th — Student of War** ([[Custom Power Index (Q-S)#Student of War|Student of War]]): one of [[Command]], [[Military Strategy]], [[Leadership]], [[Siege Engineering]].
- **9th — Elven Fastness:** 15,000gp+ in a place of beauty outside human or dwarven lands; **3d6 × 10 1st-level elven troops** within 1d3 months, paid at ordinary rates (RR; SOTN says "at no cost", Judge's call: follow the RR); animals within 3 miles friendly ([[Followers and Strongholds]]).
- **11th — Lion-Hearted Leader** ([[Custom Power Index (H-L)#Lion-Hearted Leader|Lion-Hearted Leader]]): his army automatically stands firm on its first morale roll (or rallies); lost if he routs, flees or leads from the rear ([[RR 11 Battles]]; SOTN cites Domains at War).

**Class proficiency list (29; each Combat Trickery maneuver counts one):** [[Acrobatics]], [[Alertness]], [[Berserkergang]], [[Beast Friendship]], [[Blind Fighting]], [[Combat Reflexes]], [[Combat Trickery]] (disarm, force back, knock down, overrun, sunder), [[Command]], [[Dungeonbashing Expertise]], [[Endurance]], [[Fighting Style Specialization]], [[Gambling]], [[Intimidation]], [[Leadership]], [[Manual of Arms]], [[Military Strategy]], [[Precise Shooting]], [[Riding]], [[Running]], [[Siege Engineering]], [[Skirmishing]], [[Survival]], [[Swashbuckling]], [[Weapon Finesse]], [[Weapon Focus]].

**Template (SOTN p. 170): Marshal.** Proficiencies: [[Weapon Focus]] (spears), [[Manual of Arms]]; since Manual of Arms is the class's starting power, the second becomes [[Leadership]] (Judge's call). Equipment: leaf-bladed spear, curved sword and dagger, elven composite bow, quiver of 20 arrows, chain mail, embroidered cloak, boots, backpack, a week's iron rations. INT 13+ adds bonus general proficiencies.

## Corruption and undeath
As every elven class: [[Elven Cultist#The corrupt elves of antiquity (SOTN p. 162)]]. **Undead XP:** 2 build points outside Hit Dice → class abilities count **\*** (SOTN p. 162, on the ACKS II build; Judge's call).

## As a mummy's abilities
A mummy "with the class abilities of an Nth-level elven warlord" keeps its own HD, attack throw, saves, AC and mummy powers ([[Mummy]]) and adds the warlord's damage bonus to weapon blows (on top of the armed mummy's +3, [[Nethercity Features]]), cleaves, and the powers below. A mummy made before 2800 BE (e.g. Eolande, D2) keeps nothing. XP: +1 asterisk (\*).

| Level | Damage bonus | Cleaves per round | Powers in effect |
| --- | --- | --- | --- |
| 4 | +2 | 4 | Armor or Martial Training, Manual of Arms |
| 6 | +3 | 6 | + Inspire Courage (6/day), Battlefield Prowess |
| 8 | +3 | 8 | as 6th (Inspire Courage 8/day) |
| 9 | +4 | 9 | + Student of War (one proficiency) |
| 12 | +5 | 12 | + Lion-Hearted Leader (Inspire Courage 12/day) |

## Converted from ACKS I
- **From SOTN's text:** STR and CHA, INT 9, d8, 13th level, fighter attacks, damage bonus, styles, armour and weapons, fighter items, the 3rd, 5th, 9th and 11th-level powers, fastness, titles, Marshal template.
- **Judge's calls:** the build (HD 2, Fighting 2, Elf 0, two trade-offs); level locks for SOTN's powers; Battlefield Prowess as the fastness's castle bonus; CHA as second key attribute; Martial Training read as one group; paid fastness troops; Leadership in the Marshal template.
- **Book errors:** the XP column is shifted and over-doubled (2,125 printed at 1st level, doubling continued to 270,000 at 8th, then +170,000; read 0 at 1st, 2,125 at 2nd … 135,000 at 8th); the save table is captioned "Elven Hierophant (Mage) Attack and Saving Throws" though it is the fighter's.
