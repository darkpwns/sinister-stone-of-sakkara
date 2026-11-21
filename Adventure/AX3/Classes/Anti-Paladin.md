---
type: custom-class
tags: [sakkara/secret]
source: "JJ ch. 12 custom class build of the ACKS I anti-paladin (AX3 pp. 53, 182, 185)"
build: "HD 2, Fighting 2 (narrow weapons, melee damage only)"
class_builds: "Adventure/AX3/Classes/ax3-class-builds-human.yaml"
key_attributes: "STR and CHA"
requirements: "None (Chaotic alignment)"
hit_dice: "1d8"
max_level: 14
---

# Anti-Paladin

Up: [[AX3 Hub]] · Builder: [[JJ 12 Custom Classes]], [[Creating a Custom Class]] · Build record: `Classes/ax3-class-builds-human.yaml` (`Anti-Paladin`)

## 1. Concept and role
Champions of Chaos sworn to death cults and chthonic powers: heavy warriors wrapped in a tenebrous shroud, who sense the good, command the dead and fire their fellow cultists with unholy fanaticism. A front-line fighter for a Chaotic party or a villain's lieutenant.
- **Nearest RR class:** the [[Paladin]], of which it is the mirror: the same build values and trade-offs (HD 2, Fighting 2, weapons to Narrow, melee damage only) and the same XP, but Aura of Protection against *good*, Discern Good instead of Sense Evil, Command Undead and After the Flesh instead of Lay on Hands and Sanctified Body.

## 2. Build (JJ procedure)
1. **Build points** (4; [[Build Points and Class Categories]]): Hit Dice 2, Fighting 2, Thievery 0, Divine 0, Arcane 0 (the Paladin's values, [[Ready-for-Play Class Builds]]).
2. **Hit Dice** ([[Hit Dice Value]]): HD 2 → **1d8**, Mortal Wounds +4, 1,000 XP.
3. **Fighting** ([[Fighting Value]]): Fighting 2 → fighter attack throws, all armour, all fighting styles, 1 cleave per level, 1,000 XP. Trade-offs:
   - Weapons Unrestricted → Broad → **Narrow**: 3 custom powers, **+750 XP** (3 × 250, Fighting 2 weapon penalty). Narrow: (iii) any flails, hammers and maces; (iv) any swords and daggers (Judge's call; AX3's Rhankur bears a barbed sword).
   - Damage bonus: **melee only** (missile bonus eliminated): 1 custom power.
   - Armour: heavy, unchanged. Styles: all.
4. **Thievery:** none.
5. **Spellcasting:** none. Command Undead is a power, not rebuking.
6. **Saving throws** ([[Saving Throw Progression (Custom Classes)]]): Fighting 2 highest → **fighter**; fighter magic items; +2 hp per level after 9th. Key attributes **STR and CHA**, as the RR Paladin (CHA added: Judge's call, as the Paladin's book build did).
7. **Stronghold** ([[Strongholds and Followers]]): **Castle**, renamed **Dread Keep**: 15,000gp; 5d6 × 10 0th-level troops and 1d6 anti-paladins of 1st-3rd level. Castle bonus power at 5th: **Unholy Fanaticism** ([[Custom Power Index (H-L)#Holy Fervor|Holy Fervor]]).
8. **Custom powers:** 4 bought (weapons 3, damage 1), all at 1st level, all from the [[Custom Power Index]] entries that name the anti-paladin as a user class. Starting general proficiency power: **Manual of Arms**. No drawbacks. No code of behaviour is required (Divine 0); dark vows are flavour (Judge's call).
9. **XP** ([[Experience Points per Level]]): 1,000 + 1,000 + 750 = **2,750 XP** for 2nd level (calculator; identical to the RR Paladin, which cross-checks the calculator); +120,000 per level after 8th.
10. **Level limit:** human class, 14th level (14th row added by hand: 780,000 + 120,000 = 900,000, as the RR Paladin).

**Proficiency progression** (fighter): one class and one general at 1st; class at 3rd, 6th, 9th, 12th; general at 5th, 9th, 13th.

**Anti-Paladin proficiency list** (28; the Paladin's list with Beast Friendship, Diplomacy, Goblin-Slaying, Healing and Laying on Hands replaced: Judge's call): [[Alertness]], [[Berserkergang]], [[Black Lore of Zahar]], [[Blind Fighting]], [[Combat Ferocity]], [[Combat Reflexes]], [[Combat Trickery]] (force back, incapacitate, overrun, sunder), [[Command]], [[Divine Blessing]], [[Dungeonbashing Expertise]], [[Fighting Style Specialization]], [[Illusion Resistance]], [[Intimidation]], [[Kin-Slaying]], [[Leadership]], [[Manual of Arms]], [[Martial Training]], [[Military Strategy]], [[Mounted Combat (Proficiency)|Mounted Combat]], [[Mystic Aura]], [[Poisoning]], [[Riding]], [[Running]], [[Theology]], [[Weapon Focus]].

## 3. Class table
Attack and saves: engine `custom_class.py` (fighter progression). Melee damage bonus: JJ Fighting 2 (as the RR Paladin).

| Level | Title | XP | HD | Attack | Paralysis | Death | Blast | Implements | Spells | Melee damage | Commands undead as |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Despoiler | 0 | 1d8 | 10+ | 13+ | 14+ | 15+ | 16+ | 17+ | +1 | — |
| 2 | Ravager | 2,750 | 2d8 | 9+ | 12+ | 13+ | 14+ | 15+ | 16+ | +1 | crusader 1 |
| 3 | Doombringer | 5,500 | 3d8 | 9+ | 12+ | 13+ | 14+ | 15+ | 16+ | +2 | crusader 1 |
| 4 | Reaver | 11,000 | 4d8 | 8+ | 11+ | 12+ | 13+ | 14+ | 15+ | +2 | crusader 2 |
| 5 | Defiler | 22,000 | 5d8 | 7+ | 10+ | 11+ | 12+ | 13+ | 14+ | +2 | crusader 2 |
| 6 | Dread Knight | 44,000 | 6d8 | 7+ | 10+ | 11+ | 12+ | 13+ | 14+ | +3 | crusader 3 |
| 7 | Blackguard | 90,000 | 7d8 | 6+ | 9+ | 10+ | 11+ | 12+ | 13+ | +3 | crusader 3 |
| 8 | Anti-Paladin | 180,000 | 8d8 | 5+ | 8+ | 9+ | 10+ | 11+ | 12+ | +3 | crusader 4 |
| 9 | Dread Lord | 300,000 | 9d8 | 5+ | 8+ | 9+ | 10+ | 11+ | 12+ | +4 | crusader 4 |
| 10 | Dread Lord, 10th level | 420,000 | 9d8+2* | 4+ | 7+ | 8+ | 9+ | 10+ | 11+ | +4 | crusader 5 |
| 11 | Dread Lord, 11th level | 540,000 | 9d8+4* | 3+ | 6+ | 7+ | 8+ | 9+ | 10+ | +4 | crusader 5 |
| 12 | Dread Lord, 12th level | 660,000 | 9d8+6* | 3+ | 6+ | 7+ | 8+ | 9+ | 10+ | +5 | crusader 6 |
| 13 | Dread Lord, 13th level | 780,000 | 9d8+8* | 2+ | 5+ | 6+ | 7+ | 8+ | 9+ | +5 | crusader 6 |
| 14 | Lord of Doom | 900,000 | 9d8+10* | 1+ | 4+ | 5+ | 6+ | 7+ | 8+ | +5 | crusader 7 |

\* No CON adjustment. "Half his level" rounded down (Judge's call); a 1st-level anti-paladin has no command until 2nd.

## 4. Class powers
- **1st — Aura of Protection** ([[Custom Power Index (A-B)#Aura of Protection|Aura of Protection]], reversed): +1 AC and +1 on saving throws against attacks made or effects created by *good* creatures; a tenebrous shroud under discern good, discern magic or true seeing.
- **1st — Command Undead** ([[Custom Power Index (C-D)#Command Undead|Command Undead]]): commands undead as a Chaotic crusader of half his level (the control option of the [[Crusader]]'s Rebuking Undead table: controlled 1 turn per that level, 1 day per level on a "destroyed" result; undead constructs obey as if animated by him, others are bewitched).
- **1st — Detect Good** ([[Custom Power Index (C-D)#Discern Good|Discern Good]]): the [[Sensing Evil]] proficiency reversed; detects good intent, enchantments and creatures within 45’.
- **1st — After the Flesh** ([[Custom Power Index (A-B)#After the Flesh|After the Flesh]]): if he becomes intelligent undead he keeps his class powers (paid as special abilities) and can advance in HD without level limit (see [[Zaharan Custom Classes]]).
- **1st — Manual of Arms** (starting general proficiency power).
- **5th — Unholy Fanaticism** ([[Custom Power Index (H-L)#Holy Fervor|Holy Fervor]]; Castle bonus power): hirelings of his religion +1 morale whenever he is present.
- **9th — Dread Keep** (stronghold, above).

## 5. Converted from ACKS I
- **From AX3's text** (Rhankur, pp. 182, 185): the class name; a "chaotic warrior" in plate and shield; fighter saves (F3); sword 7+ and 1d6+3 at 3rd with STR 14 and Kin-Slaying (fighter attack and fighter damage bonus); class abilities at 3rd: aura of protection ("included in AC and saves"), command undead, detect good.
- **From the JJ Custom Power Index** (not recollection): the anti-paladin's index powers are After the Flesh, Aura of Protection, Command Undead (as a Chaotic crusader of half his level), Discern Good (detect good) and Holy Fervor (unholy fanaticism). Four powers at 1st plus Holy Fervor at 5th is exactly the RR Paladin's shape (four bought powers, Holy Fervor at 5th), so the Paladin's build values and trade-offs are used.
- **From recollection of the ACKS I Player's Companion (unverified):** a Chaotic counterpart to the paladin. Its exact build values are not recalled; the mirror of the Paladin is the build's own choice.
- **Judge's calls:** Narrow picks (swords/daggers, flails/hammers/maces); CHA as second key attribute; half level rounded down for Command Undead; the Dread Keep; the proficiency list (Kin-Slaying and Intimidation added for Rhankur); titles.

## 6. NPCs of this class in AX3
- **Rhankur the Doombringer** — [[Death Cult Hideout]] (Lake District #75u; AX3 p. 185), [[Rhankur the Doombringer (AX3)]]. Revised statline: **Anti-Paladin 3**; Str 14, Int 14, Wis 12, Dex 13, Con 14, Cha 14; MV 20’ / 60’ (plate); **AC 10** (black plate +1 7, black shield +1 2, DEX +1), **11 against good creatures** (aura); HD 3, hp 15; barbed sword **8+** (anti-paladin 3 = 9+, STR +1), **7+ against humans, elves, dwarves, halflings, gnomes and Nobirans** (Kin-Slaying +1), D 1d6+3 slashing (STR +1, class melee +2); **Save F3 (WIL 0): Paralysis 12+, Death 13+, Blast 14+, Implements 15+, Spells 16+**, each 1 better against good creatures' effects (aura); commands undead as a Chaotic crusader of 1st level (skeletons 10+, zombies 13+, ghouls 16+, wights 19+; 2d6 HD); detect good; After the Flesh; ML +1; AL C; XP 50 (level 3 as HD, no special abilities; RR p. 310). Proficiencies: Manual of Arms (class power), Combat Reflexes, Kin-Slaying (class, 1st and 3rd), Intimidation, Theology (general, 1st and INT 14 bonus).
- **NPC Class table** (`Tables/ax3-building-npc-class.yaml`, AX3 p. 53): thief column, 99-100.
