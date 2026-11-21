---
type: custom-class
tags: [sakkara/secret]
source: "JJ ch. 12 custom class build of the Heroic Fantasy Handbook chosen, from AX3's text (AX3 pp. 163, 196, 200-201)"
build: "HD 2, Fighting 2 (very light armour, narrow weapons, no dual weapon style, melee damage only)"
class_builds: "Adventure/AX3/Classes/ax3-class-builds-human.yaml"
key_attributes: "STR and CHA"
requirements: "None"
hit_dice: "1d8"
max_level: 14
---

# Chosen

Up: [[AX3 Hub]] · Builder: [[JJ 12 Custom Classes]], [[Creating a Custom Class]] · Build record: `Classes/ax3-class-builds-human.yaml` (`Chosen`)

## 1. Concept and role
Heroes marked by the gods from birth: untouched by plague, poison, fear and age, trained to arms but armoured lightly, and growing into a destiny the gods reveal one gift at a time. A fighter with a hero's resilience and, from 6th level, a widening choice of god-given powers.
- **Nearest RR class:** the [[Fighter]] or [[Paladin]] (same Hit Dice, attack, saves and XP as the Paladin), but very light armour, no sense evil or lay on hands, and a set of immunities at 1st level and chosen powers from 5th. The Heroic Fantasy Handbook (not used in this campaign) is not needed: AX3 says each of Nikolaus's powers works as the proficiency or mystic ability of the same name, and the [[Custom Power Index]] gives every chosen power an ACKS II form.

## 2. Build (JJ procedure)
1. **Build points** (4; [[Build Points and Class Categories]]): Hit Dice 2, Fighting 2, Thievery 0, Divine 0, Arcane 0.
2. **Hit Dice** ([[Hit Dice Value]]): HD 2 → **1d8**, Mortal Wounds +4, 1,000 XP (Nikolaus: 35 hp at 5th with CON 16 fits d8).
3. **Fighting** ([[Fighting Value]]): Fighting 2 → fighter attack throws, damage bonus, 1 cleave per level, 1,000 XP (Nikolaus's spear +2 4+, 1d6+5 at 5th with STR 13). Trade-offs:
   - Armour Heavy → Medium → Light → **Very Light**: 3 custom powers (no XP). With the [[Armor Training]] proficiency a chosen wears leather (AX3: Nikolaus's "Armor Training (leather)" and linothorax as leather).
   - Weapons Unrestricted → Broad → **Narrow**: 3 custom powers, **+750 XP**. Narrow: (iv) any swords and daggers; (v) any spears and pole arms — AX3's two "martial training" abilities become the class's weapon selection.
   - Fighting style **dual weapon** eliminated: 1 custom power (keeps single, missile, two-handed, weapon and shield).
   - Damage bonus **melee only**: 1 custom power.
4. **Thievery:** none.
5. **Spellcasting:** none (Eldritch Talent can be picked as a chosen power).
6. **Saving throws** ([[Saving Throw Progression (Custom Classes)]]): **fighter**; fighter magic items; +2 hp per level after 9th. Key attribute **STR** by the progression; **CHA** added (Judge's call: the god-marked hero, as the Paladin).
7. **Stronghold** ([[Strongholds and Followers]]): **Castle**: 15,000gp; 5d6 × 10 0th-level troops and 1d6 chosen of 1st-3rd level. Castle bonus power at 5th: **Battlefield Prowess**.
8. **Custom powers:** 8 bought (armour 3, weapons 3, style 1, damage 1). Four at 1st level; four traded by [[Custom Power Trade-Offs]] (1 → 5th + 9th; 1 → 6th + 8th, twice; 1 → two at 7th), giving **12 powers** by 9th. The 1st- and 5th-level powers are fixed (AX3's Nikolaus); the seven at 6th-9th are **chosen powers**, each picked when it unlocks from the Custom Power Index entries that name the Chosen (list below; Judge's call, after the HFH menu). Starting general proficiency power: **Manual of Arms**. No drawbacks.
9. **XP** ([[Experience Points per Level]]): 1,000 + 1,000 + 750 = **2,750 XP** for 2nd level (calculator); +120,000 per level after 8th.
10. **Level limit:** human class, 14th (14th row by hand: 780,000 + 120,000).

**Proficiency progression** (fighter): one class and one general at 1st; class at 3rd, 6th, 9th, 12th; general at 5th, 9th, 13th.

**Chosen proficiency list** (28): [[Alertness]], [[Armor Training]], [[Blind Fighting]], [[Combat Ferocity]], [[Combat Reflexes]], [[Combat Trickery]] (disarm, force back, knock down), [[Command]], [[Diplomacy]], [[Fighting Style Specialization]], [[Illusion Resistance]], [[Laying on Hands]], [[Leadership]], [[Manual of Arms]], [[Martial Training]], [[Military Strategy]], [[Mounted Combat (Proficiency)|Mounted Combat]], [[Mystic Aura]], [[Prophecy]], [[Riding]], [[Running]], [[Sensing Evil]], [[Siege Engineering]], [[Skirmishing]], [[Swashbuckling]], [[Weapon Finesse]], [[Weapon Focus]].

## 3. Class table
Attack and saves: engine `custom_class.py` (fighter). Melee damage bonus: JJ Fighting 2.

| Level | Title | XP | HD | Attack | Paralysis | Death | Blast | Implements | Spells | Melee damage | Powers gained |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Foundling | 0 | 1d8 | 10+ | 13+ | 14+ | 15+ | 16+ | 17+ | +1 | 4 fixed + Manual of Arms |
| 2 | Favoured | 2,750 | 2d8 | 9+ | 12+ | 13+ | 14+ | 15+ | 16+ | +1 | — |
| 3 | Marked | 5,500 | 3d8 | 9+ | 12+ | 13+ | 14+ | 15+ | 16+ | +2 | — |
| 4 | Blessed | 11,000 | 4d8 | 8+ | 11+ | 12+ | 13+ | 14+ | 15+ | +2 | — |
| 5 | Anointed | 22,000 | 5d8 | 7+ | 10+ | 11+ | 12+ | 13+ | 14+ | +2 | Divine Blessing; Battlefield Prowess |
| 6 | Destined | 44,000 | 6d8 | 7+ | 10+ | 11+ | 12+ | 13+ | 14+ | +3 | 2 chosen powers |
| 7 | Paragon | 90,000 | 7d8 | 6+ | 9+ | 10+ | 11+ | 12+ | 13+ | +3 | 2 chosen powers |
| 8 | Chosen | 180,000 | 8d8 | 5+ | 8+ | 9+ | 10+ | 11+ | 12+ | +3 | 2 chosen powers |
| 9 | Hero | 300,000 | 9d8 | 5+ | 8+ | 9+ | 10+ | 11+ | 12+ | +4 | 1 chosen power; Castle |
| 10 | Hero, 10th level | 420,000 | 9d8+2* | 4+ | 7+ | 8+ | 9+ | 10+ | 11+ | +4 | — |
| 11 | Hero, 11th level | 540,000 | 9d8+4* | 3+ | 6+ | 7+ | 8+ | 9+ | 10+ | +4 | — |
| 12 | Hero, 12th level | 660,000 | 9d8+6* | 3+ | 6+ | 7+ | 8+ | 9+ | 10+ | +5 | — |
| 13 | Hero, 13th level | 780,000 | 9d8+8* | 2+ | 5+ | 6+ | 7+ | 8+ | 9+ | +5 | — |
| 14 | Chosen of the Gods | 900,000 | 9d8+10* | 1+ | 4+ | 5+ | 6+ | 7+ | 8+ | +5 | — |

\* No CON adjustment. Divine Blessing adds +2 to all saves from 5th; WIL modifies all saves.

## 4. Class powers
- **1st — Divine Health** ([[Custom Power Index (C-D)#Divine Health|Divine Health]]): immune to all disease.
- **1st — Wholeness of Body** ([[Custom Power Index (T-Z)#Wholeness of Body|Wholeness of Body]]): immune to mundane poison damage and non-lethal poison effects; +2 on saves against deadly poison; resists extraordinary poison.
- **1st — Mystical Bloodline** ([[Custom Power Index (H-L)#Longeval|Longeval]]): ageless, lifespan ×3, immune to undead diseases, +1 to the 1st-level HD roll.
- **1st — Courage** ([[Custom Power Index (Q-S)#Strength of Spirit|Strength of Spirit]]): immune to natural and magical fear.
- **1st — Manual of Arms** (starting general proficiency power).
- **5th — Divine Blessing** ([[Custom Power Index (C-D)#Divine Proficiency|Divine Proficiency]]: Divine Blessing): +2 to all saving throws.
- **5th — Battlefield Prowess** (Castle bonus power): henchmen and mercenaries +1 morale when he leads them.
- **6th-9th — seven chosen powers**, one per slot, from: [[Custom Power Index (A-B)#Armor Training|Armor Training]], [[Custom Power Index (A-B)#Blood of Kings|Scion of Kings]], [[Custom Power Index (C-D)#Chosen Weapon|Chosen Weapon]], [[Custom Power Index (C-D)#Divine Proficiency|Divine Proficiency]] (up to ×3), [[Custom Power Index (E-G)#Eldritch Talent|Eldritch Talent]] (and [[Custom Power Index (E-G)#Eldritch Warrior|Eldritch Warrior]]), [[Custom Power Index (E-G)#Friend of Birds and Beasts|Friend of Birds and Beasts]], [[Custom Power Index (H-L)#Inspire Courage|Inspire Courage]], [[Custom Power Index (H-L)#Invulnerable|Invulnerable]] (up to ×3), [[Custom Power Index (H-L)#Lion-Hearted Leader|Lion-Hearted Leader]], [[Custom Power Index (M-P)#Magical Proficiency|Magical Proficiency]], [[Custom Power Index (M-P)#Martial Proficiency|Martial Proficiency]], [[Custom Power Index (M-P)#Martial Talent|Martial Talent]] (×2), [[Custom Power Index (M-P)#Meditative Focus|Meditative Focus]], [[Custom Power Index (M-P)#Military Genius|Military Genius]], [[Custom Power Index (Q-S)#Savage Resilience|Hard to Kill]], [[Custom Power Index (Q-S)#Second Sight|Second Sight]], [[Custom Power Index (Q-S)#Student of War|Student of War]], [[Custom Power Index (Q-S)#Sworn Foe|Sworn Foe]], [[Custom Power Index (T-Z)#Thievery Proficiency|Thievery Proficiency]], [[Custom Power Index (C-D)#Ceremonial Magic|Ceremonial Magic]]. **Fate Point powers** (Boon Companion, Cleansing Touch, Destined, Determined, Farseeing, Healing Touch, Lucky, Tribulating Adversary) need the optional [[Heroic Fate]] rules (JJ ch. 16) and are not available unless the Judge adopts them. **Default picks for NPCs** (Judge's call): 6th Hard to Kill, Martial Talent (melee); 7th Inspire Courage, Lion-Hearted Leader; 8th Invulnerable, Military Genius; 9th Scion of Kings.
- **9th — Castle** (stronghold, above).

## 5. Converted from ACKS I
- **From AX3's text** (Nikolaus, p. 200; "chosen of the gods" rumour, p. 201; IV overview, p. 196): the class name and that it is an HFH class; fighter saves (F5) and fighter attack and damage (spear +2 4+, 1d6+5; falcata 5+, 1d6+3 at 5th); d8-sized hit points; Armor Training (leather) as a proficiency (so the class's own armour is lighter than leather); class abilities at 5th: courage (immunity to fear), divine blessing (+2 saves), divine health (immunity to disease), martial training (swords and daggers), martial training (spears and pole arms), mystic bloodline (longevity and immunity to paralysis), wholeness of body (immunity to poison); AX3's note that each works as the proficiency or mystic ability of the same name.
- **From the JJ Custom Power Index** (not recollection): the ACKS II form of each power, and the list of index powers that name the Chosen (the chosen power menu above), several of them selectable more than once.
- **From recollection of the Heroic Fantasy Handbook (unverified):** the HFH chosen picks its powers from a menu as it rises in level and draws on Fate Points. Its build values, XP and power schedule are not recalled; none is quoted.
- **Changed:** the two "martial training" abilities are the class's Narrow weapon selection, not powers. "Immunity to paralysis" (part of ACKS I mystic bloodline / elven bloodline) is not in ACKS II Longeval and is **dropped** (Judge's call; keep it as a quirk of Nikolaus if wanted). Divine Blessing comes at 5th, not 1st, so Nikolaus (5th) keeps it.
- **Judge's calls:** build values; CHA key attribute; Castle with Battlefield Prowess; the 6th-9th menu and the NPC defaults; Fate Point powers excluded by default; proficiency list; titles.

## 6. NPCs of this class in AX3
- **Nikolaus the Nicean** — [[Imperial Vanguard]] (AX3 p. 200), [[Nikolaus the Nicean (AX3)]]. Revised statline: **Chosen 5**; Str 13, Int 18, Wis 13, Dex 14, Con 16, Cha 17; MV 40’ / 120’; AC 6 (linothorax +1 — leather, via Armor Training — 3, shield +1, acacia +1, DEX +1); HD 5, hp 35; spear +2 **4+** (chosen 5 = 7+, STR +1, +2 magic), D 1d6+5 piercing (+2 magic, STR +1, class +2); masterwork falcata (as sword; masterwork +1 to hit) **5+**, D 1d6+3; **Save F5, all +4 (WIL +1, Divine Blessing +2, acacia +1): Paralysis 6+, Death 7+, Blast 8+, Implements 9+, Spells 10+**; immune to fear, disease and mundane poison (+2 vs deadly poison), ageless; Battlefield Prowess; ML +2; AL L; XP 200 (level 5 as HD, no special abilities; RR p. 310). Proficiencies: Manual of Arms (class power), Armor Training (leather), Command (class, 1st and 3rd), Leadership, Military Strategy 3 (general: 1st, 5th and INT 18's three bonus; one general left open).
- **Orphan gifts** (`Tables/ax3-orphan-gifts.yaml`, AX3 p. 163): result 12, "chosen character class", now this class.
