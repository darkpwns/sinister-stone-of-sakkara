---
type: dungeon-level
level: 2
hex: "18.05"
tags:
  - sakkara/secret
source: "SOTN pp. 29-33 (map pp. 23, 182-183)"
---

# Nethercity C — Central Caves

The crossroads of the Nethercity: natural lava caves and tubes (3100-2900 BE) lined with commoners' wall graves, with one hidden sepulchre (C5). Most rooms are on the **Lower** level (the book names C1 and C3-C12 so); the **Huge Deep Cavern C2** lies below them (its floor is 20’ under A4's ledge and under the D7 balcony, and its bronze doors open on the Deep Level complex E: Judge's inference, the **Deep** level). The sewer sludge runs from A3 and A4 through C1 into C2 and pours east over the precipice to L1; it feeds a big population of insect swarms, cavern locusts and mustard mould, and the predators that eat them (bombardier beetles, a caecilian, the python of G18). Shrieking locusts are the area's alarm bell. Doors lead off to the Deep, Lower and Upper complexes (D, E, F, H) and the pit to G. No blighted sinkhole. No light. Hub [[SOTN Hub]]; standing rules (sludge, miasma, doors, wall graves) [[Nethercity Features]]. Pages are SOTN printed pages.

Running: wandering 1d6 every 3 turns, 6+ → 2d10 on the **Sewer Caves** column (`Tables/sotn-wandering-sewer-caves.yaml`), setting level 2 (coordinator's call; C2's own text names the Sewer Caves column). **Shrieking locusts:** every round one or more cavern locusts shriek, the Judge makes an encounter throw (1d6, 6+); in C1 wanderers arrive in **1d4 rounds**; in C2 the arrivals follow C2's sequence (troglodytes, then beetles, then the caecilian). Sludge and miasma in C1 and C2: [[Nethercity Features#Sewer sludge (SOTN p. 12)]].

## Layout
- **From above:** rough-hewn steps from A3 down into **C1**; the 20’ cliff from A4 down to **C2a**; the hidden shaft from B1 down into **C7** ([[Nethercity A - Entrance Caves]], [[Nethercity B - Early Chthonic Tomb]]).
- **The sludge river:** C1 → steps down SE → **C2a** → east → **C2b** → over the NE precipice (and down 10’ wide steps) to **L1** ([[Nethercity L - Abyssal Level Caves]]).
- **C2a:** double heavy bronze doors in the south wall to **E1** ([[Nethercity E - Deep Level Central Complex]]); stairs up W to C1 and SW to **C12**; **C6** opens off its north side (map).
- **C2b:** stairs south up to **D8** and stairs east along the north wall up to the balcony **D7** ([[Nethercity D - Warlord's Tomb and Chapel to Bel]]).
- **C1** → 15’ lava tube SW to **C3**. **C3** → annex W (**C4**); secret door behind a grave to the hidden sepulchre **C5**; 8’ tunnel N to **C8**.
- **C8** → 5’ tunnel NE to **C7** (shaft up to B1); main tunnel NW to **C9**.
- **C9** → heavy bronze door NW to **H1** ([[Nethercity H - Great Temple of Awakening]]); narrow tunnel SW to the mouth of **C10** and on S into **C11**.
- **C11** → south end: a 5’ pit dropping 10’ to **G18**, the python's lair ([[Nethercity G - Grand Chthonic Temple]]).
- **C12** → heavy bronze door in the west face of its stone block wall to **F1** ([[Nethercity F - Lower Level Central Complex]]).

## Encounters at a glance
| Where | Who | No. | Engine note |
|---|---|---|---|
| C1 | insect swarms (millipedes and cave crayfish), 3 HD | 3 | [[Insect Swarm]] |
| C1 | cavern locusts | 12 | [[Cavern Locust]] |
| C2a / C2b | mustard mould patches (SOTN "yellow mold"), 4 + 3 | 7 | [[Mustard Mold]] |
| C2a / C2b | cavern locusts, 3 per patch (12 + 9) | 21 | [[Cavern Locust]] |
| C4 | bombardier beetles | 4 | [[Bombardier Beetle]] |
| C5 | mummies (the incestuous lovers) | 2 | [[Mummy]] |
| C6 | caecilian | 1 | [[Caecilian (SOTN)]] |
| C11 (from G18 below) | python (SOTN "giant python") | 1 | [[Python Snake]] |
| C2 (called by shrieks) | troglodyte warriors from D8 | 6 | [[Troglodyte]] (statline in [[Nethercity D - Warlord's Tomb and Chapel to Bel]], D8) |

## Rooms (SOTN pp. 29-33)

### C1. Lower Level Semicircular Cave (3100 BE)
- **Exits:** steps N up to A3; steps SE down to C2a (SOTN prints "to 3b"; C2a's text and the map show C2a); 15’ lava tube SW toward C3.

> [!player]
> A rough half-circle of a cave, about 40’ across. A heavy stream of sewage comes down the steps from the north and runs off south-east down another flight. The sludge crawls with countless tiny millipedes and cave crayfish, and among them a dozen huge stone-grey grasshoppers, about 3’ long, are feeding. Beyond the sludge a lava tube 15’ wide leads south-west. The west and east walls each hold 12 horizontal wall graves, three columns of four.

- **Monster:** 3 swarms and 12 cavern locusts. The swarms attack anything moving through or near them (fliers, climbers and rope-crossers excepted). The locusts panic if anyone attacks or comes within 5’: they shriek and leap in random directions.
  **3 insect swarms** → [[Insect Swarm]]: MV 10’/30’, AC 2, HD 3*, hp 15, 14, 12, engulf (automatic in area; 20’ × 15’ each), D 2 piercing (4 if unarmoured with natural AC 3 or less; halved if warded off), F0, ML +3, AL N, XP 65 each; immune to bludgeoning, piercing and slashing. (SOTN prints HD 3, Save NM.)
  **12 cavern locusts** → [[Cavern Locust]]: MV 20’/60’, fly 60’/180’, AC 5, HD 2*, hp 9 each, slam 1d4 + bite 1d2, or spit 9+, F2, ML −3, AL N, XP 29 each; panic jump 1d6 × 10’ in a random direction (slam 1d4 on anyone in the way); spit (ignores armour) → Death save or vomiting 1 turn, and until rinsed anyone within 5’ of the victim saves vs Death or is queasy; immune to poison. (SOTN: jump 60’, spittle save vs Poison or incapacitated.)
- **Trick:** every round one or more locusts shriek, make an encounter throw; wanderers arrive in **1d4 rounds**.
- **Graves:** 24 wall graves of about 3100 BE, usual inscriptions, remains and goods. Tally: 48gp, about 3/6 st.

### C2. Huge Deep Cavern (3000 BE)
One vast cavern, too big to light at once, keyed in two halves. 30’ ceiling hung with lava formations (SOTN's "magma stalagmites"), the stink of rotten eggs (miasma) throughout. **Seven mustard mould patches** grow in the sludge (the "Y"s on the map): **four in C2a, three in C2b**. Three cavern locusts graze each patch.

### C2a. Western Huge Deep Cavern
- **Exits:** the 20’ ledge N (A4's cliff); stairs carved in the rock ascending W to C1 and SW to C12; double heavy bronze doors S to E1 (they pull open from this side; −4 to force, 2 helpers: [[Nethercity Features#Doors (SOTN p. 11)]]); C6 opens off the north side (map); E into C2b.

> [!player]
> A grand cavern, more than 50’ north to south and at least as far westward, its far reaches lost in the dark. The ceiling, 30’ up, is covered in rippled lava like a frozen sea. In the south wall, where 30’ of rock has been dressed smooth, stand a pair of heavy bronze doors covered in fretwork. Sludge falls in from a 20’ ledge on the north wall and down two rock-cut stairs from the west, joins into one flow and runs off east into the dark. Many stone-grey grasshoppers about 3’ long feed on big tawny patches of mould growing in the sludge. The air reeks of rotten eggs.

### C2b. Eastern Huge Deep Cavern
- **Exits:** W into C2a; hewn stairs S up to D8; stairs E along the north wall up to the balcony D7 (20’ above); the NE precipice (and 10’ wide rock-cut steps beside the flow) down to L1.

> [!player]
> The cavern runs 50’ to 60’ wide here and at least as long, too big to see whole. Lava teeth hang from the 30’ ceiling over a stone balcony that crosses the cavern north-south 20’ above the floor; it is split in the middle, its northern half about 6” higher than the southern, and its balustrades are carved with trees, lotuses and serpents. Hewn stairs climb out of the cavern to the south, and similar stairs run up along the north wall to the balcony. The sewage flows in from the dark west, passes under the balcony and splashes loudly down a precipice forming the north-east wall, except where it trickles down 10’ wide steps cut in the rock. Tawny mould patches float on the sludge, grazed by many stone-grey grasshoppers 3’ long. A choking stench of rotten eggs hangs over it all.

- **Monster:** 7 mustard mould patches and 21 cavern locusts. Each patch looses its spores if crossed or disturbed. The locusts around a patch panic if anyone attacks or comes within 5’ of it, shrieking and leaping at random; a panicked locust that lands near another patch can panic that group too.
  **7 mustard mould patches** → [[Mustard Mold]]: MV 0, AC n/a (always hit), HD 2**, hp 14, 12, 11, 10 (C2a), 9, 7, 6 (C2b) (Judge's call: SOTN does not say which patch has which hp), touching or striking it bodily 1d6 extraordinary acidic (dissolves non-magic fabric, leather and wood that hit it; magic items save vs Death or dissolve); spores **50%** whenever attacked, touched or entered: 10’ cube, **Death save or die after 6 rounds**, F2, ML n/a, AL N, XP 38 each; dormant in direct sunlight. (SOTN prints XP 30, damage 1d6 + death, "immune to all attacks except fire"; the MM mould is hurt by fire and physical damage alike and immune to acid, cold, electric and the like.)
  **21 cavern locusts** → [[Cavern Locust]]: as C1 (MV 20’/60’, fly 60’/180’, AC 5, HD 2*, hp 9 each, slam 1d4 + bite 1d2 or spit 9+, F2, ML −3, AL N, XP 29 each).
- **Trick:** every round one or more locusts shriek, make an encounter throw. **1st success:** the **6 troglodyte warriors of D8** arrive, camouflaged, along the balcony D7; against a strong party they fall back to their lair to warn the tribe and gather reinforcements, otherwise they attack with missiles (their barbed darts: D8). **2nd success:** the **4 bombardier beetles of C4**. **3rd success:** the **caecilian of C6**. Further successes: roll on the Sewer Caves column.

### C3. Lower Level Bean-Shaped Cave (3000 BE)
- **Exits:** NE by the lava tube to C1 (map); 8’ tunnel N toward C8; annex W (C4); secret door behind the centre grave to the curved corridor to C5.

> [!player]
> A bean-shaped volcanic cave, 25’ by 60’, with an 8’ tunnel heading north and a cave-like annex opening to the west. The southern wall is finely carved with 15 horizontal wall graves, five columns of three.

- **Trick:** a secret door is hidden in the plastered wall behind the grave in the middle column and middle row (found as a secret door: Searching, [[Searching and Listening]]). Found, the wall pushes upward like a trap door set on end, opening a 10’ wide curved corridor (30’ long) to C5.
- **Graves:** 15 wall graves of 3000 BE, usual inscriptions, remains and goods. Tally: 30gp, about 2/6 st.

### C4. Lower Level Cavernous Annex (3000 BE)
- **Exits:** E to C3.

> [!player]
> A 40’ × 25’ cave whose walls are coated in dried, resinous oils that glint in the light. The same resin oozes from the horn-like mandibles of four giant beetles scuttling over the floor.

- **Monster:** four bombardier beetles. They usually feed on the nearby insect swarms, but they are carnivores and attack any likely meal. They answer the second successful shriek throw in C2.
  **4 bombardier beetles** → [[Bombardier Beetle]]: MV 40’/120’, AC 5, HD 2, hp 13, 12, 10, 7, bite or toxic spray 9+ (spray at one foe within 5’), D 1d6 piercing or spray (queasy until washed clean, one turn and a waterskin of water, or cure injury), F1, ML 0, AL N, XP 20 each. (SOTN prints MV 120’; its spray gives −2 to attack throws for 1 day or until cured; the MM effect is used.)

### C5. Lower Level Secret Sepulcher (2900 BE)
- **Exits:** W along the 30’ secret corridor to C3.

> [!player]
> After 30’ the secret corridor ends in an arched, plaster-lined sepulchre 30’ by 20’. Its floor is uneven from old earth movements and strewn with dozens of smashed terracotta amphorae; here and there embalmed organs have spilled from broken canopic jars and dried on the floor. There is a faint smell of incense. One cedar chest has survived whole, and beside it stands an intricately engraved cauldron of dark bronze. Two limestone sarcophagi rest along the north and south walls. Between them, the east wall is carved with a pair of beautiful elven nobles, a man and a woman, in erotic play that looks very much like brother and sister.

- **Monster:** the lovers of the relief lie in the sarcophagi as mummies, and begin to wake if the sepulchre is disturbed. (Sliding the lids: [[Nethercity Features#Sarcophagi (SOTN p. 12)]]; mummy reactions: [[Nethercity Features#Necromancy and the mummies (SOTN pp. 16-17)]].)
  **2 mummies (the lovers)** → [[Mummy]]: MV 20’/60’, AC 6, HD 5+1**, hp 31 (Judge's call: the male), 22 (the female), slam 5+, D 1d12 extraordinary bludgeoning and extraordinary necrotic + mummy rot, F5, ML +4, AL C, XP 660 each; horrific visage (Paralysis save, −1 for the second mummy); immunities as the MM block. (SOTN prints MV 60’, HD 5+1*, XP 460.) Plain mummies (2900 BE): no class abilities.
- **Loot (the mummies):** the male wears a collar cut from one sheet of gold (800gp) and was buried with a silver dagger, its grip inlaid with lapis lazuli (325gp, 1/6 st), and a bronze sceptre tipped with amber (400gp, 1/6 st). The female wears a silver corselet (400gp, 1/6 st), a silver tiara set with moonstones (2,000gp) and a pair of silver and ivory armlets (200gp each).
- **Loot (the chest):** padded with thick linen, it has kept safe four vials of rose- and lavender-scented water (**philters of love** → [[Potion of Passion]], apparent value 25gp, 1/6 st each), seven vials of green oil smelling of olive and myrrh (**oils of relaxing respite** → [[SOTN Magic Items#Oil of Relaxing Respite]], ACKS II [[Oil of Relaxing Respite]]; apparent value 75gp, 1/6 st each; SOTN p. 134), and eight vials of styrax and sweet-rush perfume (100gp, 1/6 st each).
- **Loot (the cauldron):** hepatizon, engraved with scenes of forbidden pleasure; 1 st, apparent value 2,500gp, in truth the **[[SOTN Magic Items#Bathtub of the Goddess]]** (SOTN p. 130). The rest of the grave goods are broken and worthless.
- **Lore:** **Loremastery or Theology** on the cauldron (or the relief): rites of **Nasga**, the Serpent, Chthonic goddess of beauty, pain and lust.
- Tally: **5,125gp, 4 3/6 st** as SOTN gives it (magic value excluded). (The listed weights, magic items included, add up to 4 4/6 st; SOTN's 4 3/6 is 1/6 short.)

### C6. Lower Level Hourglass-Shaped Cave (2900 BE)
- **Exits:** S onto C2a (map).

> [!player]
> An hourglass-shaped volcanic cave, 60’ long and 30’ wide, just north of the great cavern. Every wall you can see is carved with horizontal graves, too many to count quickly. From the northern bulb comes the sound of something sliding over stone, and then a long, grey, sinuous shape appears at the edge of the light.

- **Monster:** a caecilian that came in through the sewers. It lives mostly on locusts that leap near it, but it is mindlessly hungry and attacks intruders. It answers the third successful shriek throw in C2.
  **1 caecilian** → [[Caecilian (SOTN)]]: MV 20’/60’, AC 3, HD 6*, hp 28, bite 5+, D 1d8 + swallow whole (on an unmodified 19-20 the victim is swallowed: 1d8 each round, may attack from inside at −4, digested after 6 turns), F3, ML +1, AL N, XP 570. (No MM caecilian; SOTN prints MV 60’.)
- **Loot:** once it is dead, a quick search finds in the north-west corner a finely made ebony and dawn-redwood ossuary coffer full of crumbling yellow bones (150gp, 1 st).
- **Graves:** 60 wall graves of about 2900 BE, usual inscriptions, remains and goods. Tally: 120gp, about 1 1/6 st.
- Room tally: 270gp, about 2 1/6 st.

### C7. Lower Level Vertical Shaft (2900 BE)
- **Exits:** the shaft in the ceiling, 8’ up, to B1's south-east corner; 5’ tunnel SW 25’ to the T-junction of C8.

> [!player]
> A shaft comes down from the ceiling 8’ overhead into a natural tunnel 5’ wide, which runs south-west about 25’ to a T-junction.

- **Trick:** if B1's floor tiles over the shaft are still whole, the shaft stops a few feet up at a thin layer of tile. Breaking through from below takes a successful door-forcing throw ([[Doors and Dungeonbashing]]). From B1 the trap opens it (B1).

### C8. Lower Level Natural Tunnel (2900 BE)
- **Exits:** cave mouth S to C3; 5’ tunnel NE to C7; main tunnel NW to C9.

> [!player]
> A natural tunnel runs 30’ north from a cave mouth. Partway along, on the east wall, a 5’ wide side tunnel branches off north-east, while the main tunnel carries on north-west.

### C9. Lower Level Y-Shaped Cave (2900 BE)
- **Exits:** 8’ wide heavy bronze door NW to H1 (−4 to force, 1 helper); main tunnel SE to C8; narrow tunnel SW 20’ to the mouth of C10, then widening to 10’ and running S to C11.

> [!player]
> A cave about 30’ long and 25’ wide. In the north-west stands an 8’ wide heavy bronze door worked with elaborate geometric fretwork. South of the door the cave splits into two tunnels: the main one runs south-east into the dark, and a narrower one heads south-west about 20’ to a cave mouth in the west wall, where it widens to 10’ and goes on south into darkness.

### C10. Lower Level Natural Tunnel (2900 BE)
- **Exits:** the 10’ cave entrance E, onto the tunnel between C9 and C11.

> [!player]
> A bulging cave running about 40’ north-west to south-east, 35’ across at its widest and narrowing to 10’ at its mouth. In the middle of the floor lies a long, discarded tube of translucent stuff, oddly patterned with scales.

- **Lore:** it is dry and crackles to the touch. **Animal Husbandry or Naturalism**: the freshly shed skin of a giant snake at least 42” around and at least 25’ long (the python of G18).

### C11. Lower Level Natural Tunnel (2900 BE)
- **Exits:** north end: cave mouth W to C10, 10’ tunnel NE to C9; south end: curves W 10’ to a 5’ pit dropping 10’ into G18.

> [!player]
> A tunnel 10’ wide runs 40’ north to south. At its north end a cave mouth opens in the west wall and a 10’ tunnel leaves to the north-east. At the south end it bends west for 10’ and collapses into a pit 5’ across that drops about 10’.

- **Monster:** the python lairs just below in G18. **Noise here brings it to the pit in 1d4 rounds.** Its XP belongs to G18 ([[Nethercity G - Grand Chthonic Temple]]).
  **1 python** → [[Python Snake]]: MV 30’/90’, AC 3, HD 5*, hp 25, bite 6+, D 1d4 piercing; a hit also constricts automatically for 2d8 bludgeoning and holds the victim, who takes 2d8 each later initiative, F3, ML −1, AL N, XP 350. (C11 prints MV 90’, hp 30 and constriction 5d6 a round; G18, the snake's own entry, prints hp 25 and 2d8 a round. Judge's call: one snake, G18's numbers and the MM's 2d8.)

### C12. Lower Level Diamond-Shaped Cave (2900 BE)
- **Exits:** rock-cut steps E down to C2a; heavy bronze door in the west face of the stone block wall to F1 (SOTN prints "to 6a"; F1's text and the map show F1); −4 to force, 1 helper.

> [!player]
> Rock-cut steps climb into a roughly diamond-shaped volcanic cave, 50’ long and 30’ across at its widest. Its south-west side is broken by an angled wall of stone blocks whose corner juts into the cave; a heavy bronze door is set in the west face of that wall. The eastern walls are pitted with dozens of horizontal wall graves stacked four high.

- **Graves:** 36 wall graves of about 2900 BE, usual inscriptions, remains and goods. Tally: 72gp, about 4/6 st.

## Treasure and XP summary
| Room | Treasure | Monster XP (ACKS II) |
|---|---|---|
| C1 | grave goods 48gp, ~3/6 st | 195 + 348 = 543 |
| C2 | — | 266 + 609 = 875 |
| C3 | grave goods 30gp, ~2/6 st | — |
| C4 | — | 80 |
| C5 | 5,125gp, 4 3/6 st (magic excluded) | 1,320 |
| C6 | coffer 150gp, 1 st + grave goods 120gp, ~1 1/6 st | 570 |
| C7-C10 | — | — |
| C11 | — | (python 350, counted at G18) |
| C12 | grave goods 72gp, ~4/6 st | — |
| **Area C** | **5,545gp, ~8 1/6 st** (SOTN gives no area total) | **3,388** (3,738 with the python) |

**Magic items (C5):**
- 4 × [[Potion of Passion]] (SOTN "philter of love", standard item; apparent value 25gp each).
- 7 × [[SOTN Magic Items#Oil of Relaxing Respite]] (SOTN p. 134; also ACKS II [[Oil of Relaxing Respite]], TT p. 61): rubbed on temples, brow and neck, it gives a peaceful night and 1 extra hp healed the next day of complete rest. Apparent value 75gp each.
- [[SOTN Magic Items#Bathtub of the Goddess]] (SOTN p. 130): a hepatizon cauldron; a living creature bathing in it for one turn turns into the opposite sex of its kind (an intersex bather, or one of a species with more than two sexes, chooses). Apparent value 2,500gp, 1 st.
