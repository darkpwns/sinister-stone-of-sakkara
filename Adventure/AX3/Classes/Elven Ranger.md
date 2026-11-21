---
type: custom-class
tags: [sakkara/secret]
source: "JJ ch. 12 custom class build of the ACKS I Elven Ranger (AX3 pp. 53, 95)"
build: "HD 1, Fighting 2, Thievery 1, Elf 1"
xp_2nd: 2500
level_limit: 12
saves_as: fighter
key_attributes: "STR"
requirements: "INT 9 (elf)"
builds_file: "Adventure/AX3/Classes/ax3-class-builds-demihuman.yaml"
---

# Elven Ranger

## Concept and role
Elven wardens of the forest marches: deadly archers and skirmishers in green-dyed leather, trackers and scouts who move unseen, friends of bird and beast, with a little woodland magic. They range the borderlands their ancestors lost (Tomman's guise, AX3 p. 95: "elves obsessed with ancestral relics"). Nearest RR class: the [[Explorer]] (same HD 1 / Fighting 2 / Thievery 1 chassis, Animal Reflexes and Natural Stealth), but the ranger keeps unrestricted weapons, specialises in the bow (Accuracy, Precise Shot), adds elf traits and 33% arcane spellcasting, and costs 500 XP more with a 12th level limit. Unlike the [[Elven Spellsword]] it is a light-armoured woodsman with modest magic.

## Build (JJ ch. 12, Custom Racial Classes)
- **Build points:** HD 1, Fighting 2, Thievery 1 = 4 in the human categories, plus Elf 1 = **5 build points → 12th level limit**.
- **Requirements:** INT 9+ (elven classes).
- **Hit Dice 1:** d6; +1 to the HD roll at 1st level (Connection to Nature); +2 hp per level after 9th (fighter). 500 XP.
- **Fighting 2 (Fighter):** attack throws +2 per 3 levels, +1 damage at 1st and every 3 levels (melee and missile), 1 cleave per level. Unrestricted weapons; all three optional fighting styles. **Armour traded Heavy → Medium → Light for 2 custom powers** (armour trade-offs add no XP, [[Fighting Value]]). 1,000 XP.
- **Thievery 1:** 4 selections, all traded for custom powers (as the Explorer). 250 XP.
- **Divine 0, Arcane 0.**
- **Elf 1:** the four elf powers and **33% Arcane** (effective Arcane 1: Arcane 1 progression, spells from 2nd level, castable in his light armour). 750 XP.
- **Trade-offs taken:** armour (2 powers), Thievery 1 (4 powers). No weapon trade-off, so no +250 XP.
- **Custom powers:** Accuracy (1), Skirmishing (1), Animal Reflexes (1), Natural Stealth (1), Friend of Birds and Beasts (1), Precise Shot (1). Starting general proficiency power: **Tracking**.
- **Drawbacks:** none.
- **Saving throws:** Fighting 2 is the highest category → **fighter**, with Connection to Nature's +1 on Paralysis and Spells.
- **Magic items:** fighter items and all enchanted weapons; leather or lighter magic armour. Arcane + Elf = 1, so no mage-only items.
- **Key attribute:** **STR** (fighter progression: STR or CON, chosen STR). No second key: Arcane + Elf is only 1.
- **Proficiencies:** 42 − 12 = 30 on the class list. Fighter-progression classes: class proficiency at 1st, 3rd, 6th, 9th, 12th; general at 1st, 5th, 9th.
- **Stronghold:** qualifies for Castle (Fighting 1+), Hideout (Thievery 1+) and **Elven Fastness** (Elf 0+, Fighting 2+); takes the Elven Fastness with the RR's fastness benefits and limits. No Castle morale power (the ranger casts spells, [[Strongholds and Followers]]).
- **XP:** 500 + 1,000 + 250 + 750 = **2,500 XP for 2nd level**; doubled to 8th (7th = 80,000); then +120,000 (fighter) + 50,000 (elf) = **+170,000 per level after 8th**.

## Class table
From `acks/custom_class.py` with this build (Elf 1 build point, elven +50,000 XP after 8th and Connection to Nature added by the JJ rules). Damage bonus: +1 at 1st, +2 at 3rd, +3 at 6th, +4 at 9th, +5 at 12th (Fighting 2). Spells per day: JJ Arcane 1 progression.

| Level | Title | XP | Hit Dice | Attack | Paralysis | Death | Blast | Implements | Spells | Spells/day (1st-6th) | Caster Level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Fledgling | 0 | 1d6+1 | 10+ | 12+ | 14+ | 15+ | 16+ | 16+ | - | 0 |
| 2 | Woodsman | 2,500 | 2d6 | 9+ | 11+ | 13+ | 14+ | 15+ | 15+ | 1 | 1 |
| 3 | Pathfinder | 5,000 | 3d6 | 9+ | 11+ | 13+ | 14+ | 15+ | 15+ | 1 | 1 |
| 4 | Strider | 10,000 | 4d6 | 8+ | 10+ | 12+ | 13+ | 14+ | 14+ | 2 | 2 |
| 5 | Warden | 20,000 | 5d6 | 7+ | 9+ | 11+ | 12+ | 13+ | 13+ | 2 | 2 |
| 6 | Wayfarer | 40,000 | 6d6 | 7+ | 9+ | 11+ | 12+ | 13+ | 13+ | 2/1 | 3 |
| 7 | Forester | 80,000 | 7d6 | 6+ | 8+ | 10+ | 11+ | 12+ | 12+ | 2/2 | 4 |
| 8 | Wildmaster | 160,000 | 8d6 | 5+ | 7+ | 9+ | 10+ | 11+ | 11+ | 2/2/1 | 5 |
| 9 | Ranger-Lord | 330,000 | 9d6 | 5+ | 7+ | 9+ | 10+ | 11+ | 11+ | 2/2/2 | 6 |
| 10 | Ranger-Lord, 10th level | 500,000 | 9d6+2\* | 4+ | 6+ | 8+ | 9+ | 10+ | 10+ | 3/2/2 | 6 |
| 11 | Ranger-Lord, 11th level | 670,000 | 9d6+4\* | 3+ | 5+ | 7+ | 8+ | 9+ | 9+ | 3/2/2/1 | 7 |
| 12 | Ranger-Lord, 12th level | 840,000 | 9d6+6\* | 3+ | 5+ | 7+ | 8+ | 9+ | 9+ | 3/3/2/2 | 8 |

\* No CON adjustment to this flat bonus.

## Class powers
**Starting (1st level)**
- **Tracking** (starting general proficiency power): finds tracks on 11+ (with the usual modifiers) and follows them at half speed ([[Tracking]]).
- **Accuracy:** +1 to all missile attack throws.
- **Precise Shot:** missile attacks on unengaged targets through a melee at no penalty, on engaged targets at −4; ignores up to 4 points of cover. Ranks of the [[Precise Shooting]] proficiency reduce the −4 by 2 each.
- **Skirmishing:** withdraws or retreats from melee without declaring it before initiative; no AC penalty for charging or running in medium or lighter armour with 7 st or less ([[Skirmishing]]).
- **Animal Reflexes:** +1 to initiative and +1 to avoid surprise (not when casting); stacks with [[Combat Reflexes]].
- **Natural Stealth:** opponents −2 on surprise rolls when he approaches from outside line of sight or lies in wait in cover or darkness.
- **Friend of Birds and Beasts:** identifies plants and fauna on 11+, understands simple animal messages, handles trained animals, +2 reactions with normal animals, animal henchmen without Animal Training. With the [[Beast Friendship]] proficiency too: identifies on 7+, and one extra henchman if one is an animal.
- **Elf racial powers:** Animal Friendship (ordinary animals within 3 miles of his fastness kind and helpful), Attunement to Nature (+1 surprise in the wilderness; Adventuring search/listen on 14+), Connection to Nature, Elf Tongues.

**Additional**
- **Arcane Magic (2nd level):** casts arcane spells from a repertoire at the table's rate and caster level; casts in light armour. Woodland spells suit the class (e.g. *[[Chameleon]]*, *[[Slumber]]*), Judge's discretion.
- **Minor Magical Research (8th level):** at caster level 5 (the level at which the Arcane 1 progression reaches it), can research spells, scribe scrolls and brew potions ([[Magic Research]]).
- **Elven Fastness (9th level):** a fastness worth 15,000gp+ in a place of natural beauty outside human or dwarven civilized or borderland areas draws 3d6×10 1st-level elven troops within 1d3 months, paid normal rates; animals within 3 miles become friendly ([[Followers and Strongholds]]).

**Class proficiency list (30):** [[Alertness]], [[Ambushing]], [[Battle Magic]], [[Beast Friendship]], [[Blind Fighting]], [[Climbing]], [[Combat Ferocity]], [[Combat Reflexes]], [[Combat Trickery]], [[Eavesdropping]], [[Elementalism]], [[Fighting Style Specialization]], [[Illusion Resistance]], [[Land Surveying]], [[Mapping]], [[Mountaineering]], [[Mounted Combat (Proficiency)|Mounted Combat]], [[Naturalism]], [[Navigation]], [[Passing Without Trace]], [[Precise Shooting]], [[Riding]], [[Running]], [[Sniping]], [[Survival]], [[Swimming (Proficiency)|Swimming]], [[Trapping]], [[Unflappable Casting]], [[Weapon Finesse]], [[Weapon Focus]].

## Converted from ACKS I
- **From AX3's text:** only the name, the look of Tomman's guise (green-dyed leather and cloak, curved sword and dagger; AX3 p. 95) and the class's place on the NPC Class table (Fighter type 95-96, AX3 p. 53). AX3 gives no ranger statline.
- **From the JJ Custom Power Index's class lists** (powers it says the ACKS I Elven Ranger used): Accuracy, Animal Friendship, Animal Reflexes, Difficult to Spot, Friend of Birds and Beasts, Keen Eyes, Precise Shot. *Difficult to spot* was removed in ACKS II and the Index says to assign Natural Stealth instead; *keen eyes* was removed (Attunement to Nature replaces it).
- **From my recollection of ACKS I** (uncertain, not a quotation): an elven archer-woodsman, fighter-like, with light armour; I do not recall whether the ACKS I ranger cast spells or its exact build and level limit.
- **Judge's calls:** Elf 1 (a little arcane magic, as elves in ACKS II get Arcane with any Elf Value above 0) rather than Elf 0; Skirmishing for the second armour trade-off; Tracking as the starting general power; STR as key attribute; level titles.

## NPCs of this class in AX3
- **Tomman** (one of doppelgänger #3's assumed identities, AX3 p. 95; `Tables/ax3-old-doppelganger-3.yaml`, [[Doppelganger Den]]; named among the Brotherhood's victims paid for by Mentenus): a [[Doppelgänger]] posing as an elven ranger; it fights with the doppelgänger's statline, not this class.
- NPC Class table (`Tables/ax3-building-npc-class.yaml`, AX3 p. 53): Fighter type 95-96.
