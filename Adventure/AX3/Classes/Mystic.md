---
type: custom-class
tags: [sakkara/secret]
source: "JJ ch. 12 custom class build of the ACKS I mystic (AX3 pp. 53, 139)"
build: "HD 1, Fighting 2, Thievery 1 (all four thief skills traded for powers)"
class_builds: "Adventure/AX3/Classes/ax3-class-builds-human.yaml"
key_attributes: "CON and WIL"
requirements: "None"
hit_dice: "1d6"
max_level: 14
---

# Mystic

Up: [[AX3 Hub]] · Builder: [[JJ 12 Custom Classes]], [[Creating a Custom Class]] · Build record: `Classes/ax3-class-builds-human.yaml` (`Mystic`)

## 1. Concept and role
Unarmoured ascetics of a contemplative order (in Cyfaraun, students of the Logos such as the Yali Monastery of Uttar in Somirea) who fight with staff and war rings and whose discipline gives them supernatural poise, health and insight. A light, mobile melee fighter with strong saves and a sage's divination, but no spells and no armour.
- **Nearest RR class:** the [[Bladedancer]] (graceful fighting, divine favour) — but the mystic casts no spells and does not rebuke undead; it fights and saves as a fighter (AX3 gives Lubbo "Save F5"), and its powers are bodily and mental disciplines rather than prayers. Against the [[Fighter]]: d6 Hit Dice, no armour, broad weapons, and eleven powers instead of heavy armour.

## 2. Build (JJ procedure)
1. **Build points** (4, human; [[Build Points and Class Categories]]): Hit Dice 1, Fighting 2, Thievery 1, Divine 0, Arcane 0. The brief's "divine" monastic keeps its divine flavour in its powers (Divine Health, Divine Blessing), not in Divine Value: AX3's fighter saves and fighter damage bonus (Lubbo's staff 1d6+2 at 5th) need Fighting 2 as the highest category.
2. **Hit Dice** ([[Hit Dice Value]]): HD 1 → **1d6**, Mortal Wounds +2, 500 XP.
3. **Fighting** ([[Fighting Value]]): Fighting 2 → fighter attack throws (+2 per 3 levels), damage bonus +1 at 1st and +1 more every 3 levels (melee and missile), 1 cleave per level, 1,000 XP. Trade-offs:
   - Armour Heavy → Medium → Light → Very Light → **None**: 4 custom powers (no XP). With no armour the class cannot take the weapon and shield style (JJ); no power is counted for that (Judge's call).
   - Weapons Unrestricted → **Broad**: 1 custom power, **+250 XP** (Fighting 2 weapon trade-off penalty). Broad selection: (i) any tiny, small or medium melee weapons (staff, club, dagger, cestus — AX3's war rings — short sword, sword, spear, mace…) and (vi) five weapons: bola, dart, javelin, net, sling (Judge's call). No large weapons, no bows.
   - Fighting styles: single weapon, missile weapon, **dual weapon** and **two-handed weapon** (staff two-handed for 1d6).
   - Damage bonus kept (melee and missile).
4. **Thievery** ([[Thievery Value]]): Thievery 1 → 4 selections, 250 XP; **all four traded** for custom powers (as the RR [[Explorer]] did). No thief skills.
5. **Spellcasting:** none (Divine 0, Arcane 0). Probability Trance is a once-a-day spell-like power.
6. **Saving throws** ([[Saving Throw Progression (Custom Classes)]]): Fighting 2 is highest → **fighter** progression; fighter magic items plus weapons of its selection; **+2 hp per level after 9th**. Key attribute by the progression: **CON** (STR or CON); **WIL** added (Judge's call: ACKS I's mystic prime requisite was WIS, and the JJ lets the Judge expand key attributes for flavour).
7. **Stronghold** ([[Strongholds and Followers]]): qualifies for Castle (Fighting 1+) or Hideout (Thievery 1+); takes **Castle**, renamed **Monastery**: 15,000gp; 5d6 × 10 0th-level lay brothers (mercenaries) and 1d6 mystics of 1st-3rd level. Castle bonus power at 5th: **Holy Fervor** (hirelings of his faith +1 morale while he is present; the Paladin's 5th-level power, a "similar custom power" the JJ lets the Judge approve).
8. **Custom powers:** 9 powers bought (armour 4, weapons 1, thief skills 4), all from the [[Custom Power Index]], whose entries name the mystic as a user class. Six at 1st level; three traded by [[Custom Power Trade-Offs]] (1 → 5th + 9th; 1 → 6th + 8th; 1 → two at 7th), giving **12 powers** by 9th level. Starting general proficiency power: **Theology**. No drawbacks.
9. **XP** ([[Experience Points per Level]]): 500 + 1,000 + 250 + 250 = **2,000 XP** for 2nd level (calculator `costs()`); doubled to 8th, 7th rounded to 65,000; +120,000 per level after 8th (fighter).
10. **Level limit:** human class, 14th level. (The engine's `level_limit()` reads the racial Build Point Level Limit table, which gives 13 for 4 build points; the 14th-level row is added by hand: 730,000 + 120,000.)

**Proficiency progression** (fighter): one class and one general proficiency at 1st; class proficiency at 3rd, 6th, 9th and 12th; general at 5th, 9th and 13th.

**Mystic proficiency list** (28 = 42 − 14; each Combat Trickery maneuver counts one, as on the RR lists): [[Acrobatics]], [[Beast Friendship]], [[Blind Fighting]], [[Climbing]], [[Combat Reflexes]], [[Combat Trickery]] (disarm, knock down, wrestling), [[Contemplation]], [[Contortionism]], [[Eavesdropping]], [[Fighting Style Specialization]], [[Healing]], [[Illusion Resistance]], [[Laying on Hands]], [[Martial Training]], [[Mystic Aura]], [[Passing Without Trace]], [[Prophecy]], [[Running]], [[Sensing Evil]], [[Skirmishing]], [[Skulking]], [[Swashbuckling]], [[Unarmed Fighting]] (+1 damage with war rings, as with a cestus), [[Wakefulness]], [[Weapon Finesse]], [[Weapon Focus]].

## 3. Class table
Attack and saves: engine `custom_class.py` (fighter progression). Damage bonus: JJ Fighting 2 (as the RR [[Paladin]] table).

| Level | Title | XP | HD | Attack | Paralysis | Death | Blast | Implements | Spells | Damage bonus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Novice | 0 | 1d6 | 10+ | 13+ | 14+ | 15+ | 16+ | 17+ | +1 |
| 2 | Initiate | 2,000 | 2d6 | 9+ | 12+ | 13+ | 14+ | 15+ | 16+ | +1 |
| 3 | Disciple | 4,000 | 3d6 | 9+ | 12+ | 13+ | 14+ | 15+ | 16+ | +2 |
| 4 | Seeker | 8,000 | 4d6 | 8+ | 11+ | 12+ | 13+ | 14+ | 15+ | +2 |
| 5 | Ascetic | 16,000 | 5d6 | 7+ | 10+ | 11+ | 12+ | 13+ | 14+ | +2 |
| 6 | Contemplative | 32,000 | 6d6 | 7+ | 10+ | 11+ | 12+ | 13+ | 14+ | +3 |
| 7 | Illuminate | 65,000 | 7d6 | 6+ | 9+ | 10+ | 11+ | 12+ | 13+ | +3 |
| 8 | Sage | 130,000 | 8d6 | 5+ | 8+ | 9+ | 10+ | 11+ | 12+ | +3 |
| 9 | Master | 250,000 | 9d6 | 5+ | 8+ | 9+ | 10+ | 11+ | 12+ | +4 |
| 10 | Master, 10th level | 370,000 | 9d6+2* | 4+ | 7+ | 8+ | 9+ | 10+ | 11+ | +4 |
| 11 | Master, 11th level | 490,000 | 9d6+4* | 3+ | 6+ | 7+ | 8+ | 9+ | 10+ | +4 |
| 12 | Master, 12th level | 610,000 | 9d6+6* | 3+ | 6+ | 7+ | 8+ | 9+ | 10+ | +5 |
| 13 | Master, 13th level | 730,000 | 9d6+8* | 2+ | 5+ | 6+ | 7+ | 8+ | 9+ | +5 |
| 14 | Grand Master | 850,000 | 9d6+10* | 1+ | 4+ | 5+ | 6+ | 7+ | 8+ | +5 |

\* No CON adjustment to the flat bonus. Divine Blessing (6th) adds +2 to every save from 6th level; WIL modifies all saves.

## 4. Class powers
- **1st — Graceful Fighting** ([[Custom Power Index (A-B)#Blade-Dancing|Blade-Dancing]]): +1 AC in light, very light or no armour carrying 5 stone or less; +2 at 7th, +3 at 13th.
- **1st — Meditative Focus** ([[Custom Power Index (M-P)#Meditative Focus|Meditative Focus]]): once per day per level, focused for 1 turn: +1 to attack throws, proficiency throws, saving throws and initiative.
- **1st — Mindfulness** ([[Custom Power Index (A-B)#Alertness|Alertness]]): +1 to avoid surprise; Adventuring search and listen on 14+ (+2 if separately proficient).
- **1st — Speed of Thought** ([[Custom Power Index (A-B)#Animal Reflexes|Animal Reflexes]]): +1 initiative (not when casting) and +1 to avoid surprise; stacks with Combat Reflexes.
- **1st — Strength of Spirit** ([[Custom Power Index (Q-S)#Strength of Spirit|Strength of Spirit]]): immune to natural and magical fear.
- **1st — Purity of Body and Soul** ([[Custom Power Index (C-D)#Divine Health|Divine Health]]): immune to all disease, magical included.
- **1st — Theology** (starting general proficiency power).
- **5th — Probability Trance** ([[Custom Power Index (M-P)#Probability Trance|Probability Trance]]): casts [[Divination]] (Divine 4) once per day; the Judge makes the magic research throw secretly at his class level (Judge's call for the level).
- **5th — Holy Fervor** (Castle bonus power): hirelings of his faith +1 morale while he personally leads them.
- **6th — Harmony of Spirit** ([[Custom Power Index (C-D)#Divine Blessing|Divine Blessing]]): +2 to all saving throws.
- **7th — Perceive Intentions** ([[Custom Power Index (M-P)#Perceive Intentions|Perceive Intentions]]): always knows the true reaction result of creatures he deals with; creatures with CHA above his WIL are immune.
- **7th — Command of Voice** ([[Custom Power Index (C-D)#Command of Voice|Command of Voice]]): +1 reactions with creatures he speaks to; a total of 12+ leaves them bewitched in his presence; WIL above his CHA is immune.
- **8th — Wholeness of Body** ([[Custom Power Index (T-Z)#Wholeness of Body|Wholeness of Body]]): immune to mundane poison damage and non-lethal poison effects; resistant to extraordinary poison; +2 on saves against deadly poison.
- **9th — Perfection of Body** ([[Custom Power Index (H-L)#Longeval|Longeval]]): ageless, lifespan ×3, immune to undead diseases.
- **9th — Monastery** (stronghold, above).

## 5. Converted from ACKS I
- **From AX3's text** (Lubbo, p. 139): the class name; fighter saves (F5) and fighter-like attack and damage (staff 7+, 1d6+2 at 5th with STR 10); no armour (AC 3 in a robe); staff and war rings; seven powers held by 5th level: graceful fighting, meditative focus "(5/day)" (so once per day per level), mindful, probability trance ("insights into reality … for those who seek answers"), purity of body and soul, strength of spirit, speed of thought. The build places all seven by 5th level.
- **From the JJ Custom Power Index** (not recollection): which index powers the mystic uses and their ACKS I names (mindfulness, speed of thought, graceful fighting, harmony of spirit, purity of body and soul, perfection of body, plus command of voice, perceive intentions, probability trance, strength of spirit, wholeness of body, meditative focus). The five not on Lubbo are placed at 6th-9th.
- **From recollection of the ACKS I Player's Companion (unverified):** a WIS-based, unarmoured monastic with d6 Hit Dice. The ACKS I build values, XP and the level at which each power came are not recalled reliably; none of them is quoted here.
- **Judge's calls:** the build values (HD 1, Fighting 2, Thievery 1); Broad weapons (vi) picks; the levels of the five later powers; WIL as a second key attribute; Monastery with Holy Fervor; war rings read as [[Weapons|cestus]] (ACKS II 1d3, +1 with Unarmed Fighting; AX3 6+ and 1d4+2 have no ACKS II basis); Theology as the starting power; the proficiency list and titles.

## 6. NPCs of this class in AX3
- **Lubbo the Immaculate** — [[Plaza District]] #42, Courtyard of Nine Shrines (AX3 p. 139). Revised statline: **Mystic 5**; Str 10, Int 9, Wis 17, Dex 13, Con 10, Cha 12; MV 40’ / 120’; **AC 2** (unarmoured 0, DEX +1, Graceful Fighting +1; AX3 3); HD 5, hp 20; staff 7+ (mystic 5 = 7+, STR 0), D 1d6+2 bludgeoning (two-handed 1d6, class +2), or war rings (as cestus) 7+, D 1d3+2 (AX3 6+, 1d4+2); **Save F5 with WIL +2: Paralysis 8+, Death 9+, Blast 10+, Implements 11+, Spells 12+**; +2 to avoid surprise; Meditative Focus 5/day (+1 attack, saves, proficiency throws, initiative for a turn); ML 0; AL L; XP 200 (level 5 as HD, no special abilities; RR p. 310). Powers: Graceful Fighting, Meditative Focus, Mindfulness, Speed of Thought, Strength of Spirit, Purity of Body and Soul, Probability Trance ([[Divination]] 1/day), Holy Fervor (added by the build). Proficiencies: Theology (class power), Laying on Hands, Wakefulness, Seafaring; one general proficiency (5th level) not named by AX3: Judge's call.
- **NPC Class table** (`Tables/ax3-building-npc-class.yaml`, AX3 p. 53): cleric column, 97-98.
