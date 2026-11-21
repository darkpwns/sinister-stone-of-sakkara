---
type: dungeon-level
level: 4
hex: "18.05"
tags:
  - sakkara/secret
source: "SOTN pp. 123-125 (map pp. 23, 182-183)"
---

# Nethercity R — Abyssal Level Southern Cave

A small Abyssal Level annex below the south-west corner of the Grand Chthonic Temple: a hewn corridor and a royal tomb of about 2200 BE (R1-R2), then two volcanic caverns turned into a mass grave in 2200-2100 BE (R3-R4). The occupants of R2 are the son and daughter of the king buried in G14 ([[Nethercity G - Grand Chthonic Temple]]), now mummies with the spells and arms they had in life; R3 holds the largest single throng of skeletons in the Nethercity. No blighted sinkhole is keyed here; the whole Nethercity is a shadowed sinkhole of evil ([[Nethercity Features]]). Unlit throughout. Hub [[SOTN Hub]].

Running: wandering 1d6 every 3 turns, 6+ → 2d10 on the Temple / Tomb column, `Tables/sotn-wandering-temple-tomb.yaml` (`level: 4`). Area rules: the R2 mummies stir when their stone slab door is first disturbed (torpor and door attempts per [[Nethercity Features]]); the R3 skeletons start climbing out 6 rounds after anyone enters R3 and keep coming at 2d20 a round.

## Layout
- **Entrances:** (a) from the Y-intersection **G8** ([[Nethercity G - Grand Chthonic Temple]]) a winding stair goes down south-east into **R1**; (b) from the river bank **P13** ([[Nethercity P - Sub-Abyssal River Banks]]) a stair climbs east to a boulder secret door in the tunnel between **R4** and **R3**.
- **R1** (45’ × 10’ corridor) ends at two doors: a stone slab door in the north-east wall to the tomb **R2** (a dead end), and a heavy bronze door in the south-east wall into the north-east corner of the great cave **R3**.
- **R3** (fist-shaped, the "finger" reaching south-east) runs west by a 10’ tunnel from its south-west tip to **R4** (anvil cave). The boulder secret door to the P13 stair is on the south wall of that tunnel.
- Neighbours: [[Nethercity S - Abyssal Level Hidden Tombs]] lies just east of R2 (no connection); the river caves of P are west and south.

## Encounters at a glance
| Where | Who | No. | Engine note |
| --- | --- | --- | --- |
| R2 | Mummy prince (courtier) | 1 | [[Mummy Prince (SOTN)]] (variant of [[Mummy]]) |
| R2 | Mummy princess (courtier) | 1 | [[Mummy]] (variant, inline) |
| R2 | Bronze animated statues | 4 | [[Bronze Animated Statue]] |
| R3 | Skeletons (shortswords, shields) | 288, 2d20 a round | [[Skeleton]] |
| R2 (summoned) | Berserkers from *summon berserkers* | as the spell | [[Berserker]] |

## Rooms (SOTN pp. 123-125)

### R1. Abyssal Level Corridor (2200 BE)
- **Exits:** stair up north-west to G8; stone slab door north-east to R2; heavy bronze door south-east to R3.
> [!player]
> The stair from above winds down into a corridor 10’ wide and 45’ long. It ends at two doors: a stone slab in the north-east wall and a heavy bronze door in the south-east wall.
- Doors: stone slab −12, heavy bronze −4 to force ([[Nethercity Features]]). Any work on the slab door starts the R2 mummies waking.

### R2. Abyssal Level Prince and Princess Tomb (2200 BE)
- **Exits:** stone slab door south-west to R1 only.
> [!player]
> A tomb 20’ × 30’, walls panelled in black marble flecked with red, floor of plain black marble. Mosaics on the west and east walls show an elven prince and princess hunting elephants and stranger beasts through jungle. Between them two low bronze-plated daises carry two bronze sarcophagi, partly gilded and carved in the likeness of the pair; beside each stand two bronze statues of elven warriors in old-fashioned war gear. On the north-east wall above the sarcophagi hang an engraved composite bow, a black-and-gold quiver about half full of black-fletched arrows, and a fine long spear. Next to the sarcophagi two huge ivory tusks and dozens of smaller horns and tusks are heaped on a low mound of electrum coins; beside the heap stand two sets of canopic jars and two long scrolls wound on ivory handles.
- **Monster:** the prince and princess are mummy courtiers (mummies keeping the abilities of the [[Elven Courtier]] class they had in life: classical weapons training, inspire courage, arcane spells; SOTN gives no class write-up, so the abilities are spelled out here). They begin to wake when the R1 slab door is first disturbed: depending on how long the door took, they are just rising or fully roused when the party comes in. The statues wake with them.
  - **Mummy prince** → [[Mummy Prince (SOTN)]] (variant of [[Mummy]]): MV 60’, AC 11, HD 8+1***, hp 41, touch 2+ 1d12+3 extraordinary bludgeoning and necrotic + mummy rot, or spear +1 0+ D 1d8+7 (no rot by weapon), F8, ML +4, AL C, XP 2,100. Horrific visage (Paralysis save or cower, per MM); mummy rot; damage immunities and resistances as [[Mummy]] (mundane weapons useless; extraordinary weapons resisted; mundane fire resisted, extraordinary fire full). Classical weapons training +1 to hit in melee; inspire courage 4/day (1 round of oration: Chthonic allies within 50’ get +1 to attack throws, damage, morale and saves vs magical fear for 1 turn). Arcane spells 2 1st, 2 2nd: [[Mage Missile]], *summon berserkers*; [[Necromantic Potence]], [[Ogre Strength]]. (SOTN prints touch 3+, spear 1+; ACKS II: 8+1 HD attacks as 9 HD, 2+. AC 11 with no armour named: kept as printed, Judge's call.)
  - **Mummy princess** (variant of [[Mummy]], inline): MV 60’, AC 11, HD 8+1***, hp 33, touch 2+ 1d12+3 extraordinary bludgeoning and necrotic + mummy rot, or composite bow +1 0+ D 1d6+7 (+1 more damage with arrows +1; no rot by weapon), F8, ML +4, AL C, XP 2,100. As the prince, but classical weapons training +1 to hit with missiles. Arcane spells 2 1st, 2 2nd: [[Bewitch Humanoid]] (charm person), [[Slumber]] (sleep); [[Hypnotic Sigil]] (hypnotic pattern), [[Invisibility]]. (SOTN prints touch 3+, bow 1+.)
  - **4 bronze animated statues** → [[Bronze Animated Statue]]: MV 60’, AC 6, HD 5*, hp 25, 23, 21, 20, slam 6+, D 5d4 extraordinary bludgeoning, F5, ML n/a, AL N, XP 350 each. Immune to mundane weapons, resist extraordinary ones; weak point (an action and a Searching throw to spot, +4 with Engineering; aimed attacks −4 bypass immunity; an unmodified 20 destroys it). (SOTN prints MV 30’, AC 5, HD 5**, shortsword 2d6, XP 500.)
- **Tactics:** given time to prepare, the prince takes his spear from the wall and casts [[Ogre Strength]] (ACKS II +2 to melee attack and damage: spear −2+, D 1d8+9; SOTN says +3) and [[Necromantic Potence]] (1d10+4 temporary hp, as SOTN: caster level 4 implied, Judge's call); the princess takes her bow and arrows and casts [[Invisibility]] on herself. In the fight the princess casts [[Hypnotic Sigil]] (cone 60’ × 30’, living humanoids save vs Paralysis or are mesmerized while she concentrates) and the prince casts *summon berserkers* (Judge's call: no ACKS II equivalent; use the ACKS I spell, berserkers as [[Berserker]]), then hunts the mesmerized. Both inspire courage on their allies before closing.
- **Loot:**
  - Prince: gold crown set with black sapphires (4,000gp). Long spear, bronze leaf-shaped head, masterwork look (apparent value 650gp): **spear +1**.
  - Princess: gold tiara set with tiny rubies (4,000gp). Composite bow with dragon-shaped arms (apparent value 650gp): **composite bow +1**; ebony quiver inlaid with gold (400gp, 1/6 st.) holding **10 arrows +1** (black fletching, hepatizon heads).
  - 2 bronze sarcophagi, partly gilded (1,500gp, 20 st. each).
  - Trophy heap: 2 great ivory tusks (1,000gp, 10 st. each), 1 rhinoceros horn (300gp, 4/6 st.), 15 pairs of sabre-tooth tiger tusks (4gp, 1/6 st. per pair), 20 pairs of giant boar tusks (2gp, 1/6 st. per pair), on 3,000ep.
  - 8 terracotta canopic jars of embalmed organs (25gp, 1/6 st. each).
  - The two scrolls: [[SOTN Magic Items#Prince's Spellbook]] and [[SOTN Magic Items#Princess's Spellbook]] (700gp, 1/6 st. each; SOTN p. 138). Prince's: 1 mage missile, *summon berserkers*; 2 necromantic potence, ogre strength; 3 clairvoyancy, skinchange. Princess's: 1 bewitch humanoid, slumber; 2 hypnotic sigil, invisibility; 3 flight, skinchange.
  - Tally: 15,500gp, 68 1/6 st. (magic excluded; SOTN's figures. The listed weights add to 71 st.)
- **Lore:** the pair plainly resemble the king entombed in G14, their father.

### R3. Abyssal Level Fist and Finger Cave (2200-2100 BE)
- **Exits:** heavy bronze door in the north-west wall near the north-east corner to R1; 10’ tunnel west from the south-west tip to R4 (boulder secret door to P13 on its south wall).
> [!player]
> A great cave shaped like a clenched fist with the middle finger raised. The fist is at least 60’ across from south-west to north-east and about 35’ wide; the "finger" runs off south-east into the dark. The roof, 25’ up, bristles with frozen lava stalactites. A heavy bronze door stands in the north-west wall near the north-east corner, and a 10’ tunnel leaves westward from the south-west tip. Hundreds of horizontal burial niches are cut into the walls, every one holding a skeleton with a curved bronze shortsword and a bronze shield.
- **Graves:** 288 horizontal wall graves of 2200-2100 BE with the usual inscriptions ([[Nethercity Features]]); each holds an undead skeleton. SOTN lists no grave goods (Judge's call: none).
- **Monster:** 6 rounds (1 minute) after any intruder enters, the skeletons start to climb out: **2d20 a round** until all 288 are destroyed or no intruder remains in the cave. Turning them back is the party's best hope; fleeing up R1 and closing the bronze door is the other.
  - **288 skeletons** → [[Skeleton]]: MV 120’, AC 3, HD 1*, hp 5 each, curved bronze shortsword 10+, D 1d6, F1, ML n/a, AL C, XP 13 each. Immune to enchantment, necrotic and poison. (SOTN prints AC 2; MM: AC 2 + 1 for the shield.)
- **Tally:** no treasure.

### R4. Abyssal Level Anvil Cavern (2100 BE)
- **Exits:** tunnel from the east wall of the anvil's base to R3; boulder secret door on the south wall of that tunnel, opening on the stair down to P13.
> [!player]
> A cave shaped like an anvil. Its narrow base is 15’ wide and 15’ long; north-east of it opens the head, a rough triangle about 60’ long from north-west to south-east, 30’ wide at its eastern side and narrowing to 10’ at its western point. A tunnel leaves the east wall of the base. Boulders and stalagmites of old frozen lava are scattered all through it.
- **Trick:** one boulder on the south wall of the tunnel to R3 is a secret door (Searching to find). It rolls aside like a stone slab door (−12 to force, [[Nethercity Features]]) onto steps down to P13 ([[Nethercity P - Sub-Abyssal River Banks]]). (SOTN p. 120 says the P13 stair comes out "in the vicinity of R2"; the map and this key put it by R4.)

## Treasure and XP summary
| Room | Treasure (gp) | Weight (st.) | Magic | Monster XP |
| --- | --- | --- | --- | --- |
| R1 | — | — | — | — |
| R2 | 15,500 | 68 1/6 | spear +1; composite bow +1; 10 arrows +1; [[SOTN Magic Items#Prince's Spellbook]]; [[SOTN Magic Items#Princess's Spellbook]] | 2 × 2,100 + 4 × 350 = 5,600 |
| R3 | — | — | — | 288 × 13 = 3,744 |
| R4 | — | — | — | — |
| **Area R** | **15,500** | **68 1/6** | 5 items | **9,344** (plus any summoned berserkers) |
