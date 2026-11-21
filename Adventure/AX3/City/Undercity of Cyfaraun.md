---
type: dungeon-level
level: 2
hex: "18.05"
place: "[[Cyfaraun]]"
tags:
  - sakkara/secret
source: "AX3 pp. 63-67"
---

# Undercity of Cyfaraun

Judge only. The sewers, crypts and cellars under [[Cyfaraun]], tunnelled through the soft volcanic tuff along the streets of the ancient elven city. Pages are AX3 printed pages. Hub: [[AX3 Hub]]; above ground: [[Streets of Cyfaraun]]. The deeper Nethercity is a separate module: see SOTN (separate module notes).

Running: wandering 1d6 every 3 turns, 6+ (**5+ below the Old District**); none inside an uncleared special location. Table: 1d100 `Tables/ax3-undercity-encounters.yaml`. The 80-00 results use `Tables/ax3-undercity-special.yaml`.

## Running the Undercity
- Dungeon level: 2 (Judge's call: AX3 does not state one; most of the table is level 1-2 vermin and oozes, with level 4+ outliers: acanthaspis, tarantula, python, black blob, skittering maw)
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/ax3-undercity-encounters.yaml

(Below the Old District use 5+: `acks.sh location --site "Undercity of Cyfaraun" --level 2 --wandering "1d6 every 3 turns, 5+" --table Adventure/AX3/Tables/ax3-undercity-encounters.yaml`; elsewhere the same with `6+`.)

## Construction (pp. 63-64)
- After the conquest the Aurans dug sewers along the lines of Ancient Cyfaraun's streets, through soft tuff rather than masonry. The **main tunnels under the Old City follow the ancient avenues**. Beyond the old elven limits, newer tunnels were cut straight through the tuff. The Aurans also dug **dungeons, crypts, basements and sub-cellars** in and around the ancient city.
- Ceilings: usually cut tuff. Floors: gently sloped tuff. Inside the ancient limits the floor slopes down to the **original pavement of rubble set in mortar**. Walls: tuff and ancient stone slabs, often painted with sylvan scenes or written in **Ancient Argollëan** (a Loremastery hook).
- **Large sewer tunnels:** **13.5’ high × 13.5’ wide** (wide enough for a chariot), with **2’ ledges** on both sides and **torch sconces every 60’**. Characters move single file along a ledge without penalty. **Anyone struck while on a ledge saves vs Paralysis or falls into the sewer channel.**
- **Small sewer tunnels:** **7.5’ high and wide**, no ledges.

## Entering the Undercity (p. 63)
Points of interest with direct access:

| POI | District | Access |
| --- | --- | --- |
| #11 The Mink | [[Old District]] | basement |
| #20 Imperial Amphitheater | [[Festival District]] | cells and slave pits |
| #36 Solar Citadel | [[Bridge District]] | crypts (Catacombs of the Patriarchs, #36u) |
| #50 Tower of Knowledge | [[Tower District]] | vaults |
| #51 Public Baths | [[Tower District]] | hypocausts |
| #68 Shrine of the Ancestors | [[Temple District]] | crypts (Catacomb of the Ancestors, #68u) |
| #78 Prefectural Palace | [[Palace District]] | dungeons (prisons) |
| #81 Prefectural Guard Barracks | [[Palace District]] | dungeons (Barracks Vault, #81u) |

- The Judge may add more entrances and special locations: much of the Undercity is unkeyed (p. 63).
- **Sewer grates:** a **2’ × 2’ lead grate** in every block. **Old District** grates lift out freely as **an action in lieu of movement** (the Argollëan Family's smuggling routes). Elsewhere it takes a **Dungeonbashing throw** (ACKS I Open Doors): 18+, ±4 per point of STR adjustment, a pair +4 (RR p. 266) (p. 63).
- **Random basements** (below).

## Illumination (p. 63)
By day, light through the grates reaches a **30’ radius** below each one. At night, and away from the grates, the tunnels are dark. Some locations are lit by their occupants, as the location keys say.

## Sewer sludge (p. 64)
- Sludge fills the sewer channels. It does **not slow exploration movement**, but characters in it **charge or run at half rate**, and **Acrobatics and Sneaking** (ACKS I Move Silently) throws are at **-2**.
- **Fungal infection:** anyone **knocked down or falling prone** in the sludge is infected unless he saves **vs Death at +4** (ACKS I "vs Poison"). **Eating** sludge infects automatically, with no save.
  - Scabs appear **1d8 hours** later as white pulpy patches (on the skin, or on the tongue, lips and mouth if eaten). From then on: **-2 to reaction rolls**, **-1 to surprise and initiative rolls** (itching).
  - **Each day** after that the scabs spread: save **vs Death**. A failure leaves a **permanent scar** ("minor scarring" on the Mortal Wounds tables). A success means no scar, but he is still infected.
  - Cure: a **Healing** proficiency treatment or magic (e.g. cure disease).
- **Miasma** (rotten-egg stink): anyone exposed saves **vs Death every turn**. A failure gives headache, bleary eyes and shortness of breath: **-1 to attack throws and damage rolls** until he **rests 1 turn away from the sludge**. A bandana over nose and mouth, or a similar precaution: save **once per hour at +4**.
- AX3 options: a cinematic game ignores the sludge. A "cruel realism" game adds permanent ability-score loss from sulphide gas (no numbers given; Judge's call if used).

## Random basements (p. 63)
- In the **Bridge, Lake and Old Districts**, many elven buildings stand on the jutting foundations of older ones. Some builders dug basements or vaults beneath them.
- **Any city building in those districts that sits over an Undercity chamber: 10% chance** of a stair down to a basement joined to the Undercity.
- The door from that basement into the rest of the Undercity has usually been **sealed and stuccoed over**. Find it as a **secret door** (Searching).
- AX3 gives an example map of Lake District buildings connected below (p. 63). It is not reproduced here.

## Encounters (p. 64)
- The Undercity is mostly empty, so explore it like a dungeon (just a few feet below safety). Throw **1d6 every 3 turns (30 minutes)**: an encounter on **6+**, or **5+ below the Old District**.
- **No throws inside a special location until it has been cleared:** its occupants keep wanderers out.
- On an encounter roll **1d100** on `Tables/ax3-undercity-encounters.yaml`. On **80-00**, use the special encounter of the **nearest special location** (`Tables/ax3-undercity-special.yaml`). **If the party is more than 120’ from every special location, no encounter occurs.**
- **Noise-makers:** cavern locusts (30-31) shriek while the party advances: make a wandering throw **each round**, arrivals in **1d4 rounds**. Shriekers (42-43) scream **1d3 rounds**: each round, **50%** that a nearby wandering monster arrives within **2d6 rounds**. Either way, creatures in nearby special locations are **alerted** (pp. 65-66).

## Wandering monsters (1d100, pp. 64-67)
Statlines are the ACKS II MM's (short form: MV, AC, HD, attacks, damage, save, ML, XP).

| d100 | Monster | No. | Engine note | Statline / module line |
| --- | --- | --- | --- | --- |
| 01 | Ankheg | 1d6 | [[Giant Acanthaspis]] (inferred rename: burrowing acid-spitting bug) | 40’/120’, burrow 20’/60’, AC 8, HD 5**, bite 6+ 3d6 + grab/acid, F5, ML -1, XP 500. Very hungry: **-5 reaction** |
| 02 | Giant ants | 2d4 | [[Giant Ant Worker]] | 60’/180’, AC 6, HD 4, bite 7+ 2d6, F2, ML -1, XP 80. Hauling sludge to their burrow |
| 03-04 | Giant fire beetles | 1d8 | [[Luminous Beetle]] | 40’/120’, AC 5, HD 1+2, bite 9+ 2d4, F1, ML -1, XP 15. Their glow is visible down the tunnel |
| 05 | Bombardier beetles | 1d8 | [[Bombardier Beetle]] | 40’/120’, AC 5, HD 2, bite or spray 9+, F1, ML 0, XP 20 |
| 06 | Tiger beetles + giant rats | 1d6 + 3d6 | [[Tiger Beetle]], [[Giant Rat]] | beetle 50’/150’, AC 6, HD 3+1, bite 7+ 2d6, F1, ML +1, XP 65; rat AC 2, HD ½, bite 12+ 1d3 + disease, XP 5. Both attack anyone within 10’. Undisturbed, the rats flee at half numbers |
| 07 | Black pudding | 1 | [[Black Blob]] | 20’/60’, AC 5, HD 10**, 1+ 3d8 acid, F5, XP 2,250. A 30’-wide "black mould" layer |
| 08-09 | Carcass scavengers | 1d3 | [[Carrion Horror]] | 40’/120’, AC 2, HD 3+1***, 8 stingers 7+ 1 + paralysis, F2, ML +2, XP 170. On the ceiling: reach characters on the ledges, but not those crouching in the channel |
| 10-14 | Giant centipedes | 2d4 | [[Giant Centipede]] | 20’/60’, AC 0, HD ½*, bite 12+ 1 + poison, F0, ML -1, XP 6. Spread across the tunnel, no way past |
| 15-16 | Giant carnivorous flies | 1d6 | [[Giant Fly]] | 30’/90’, AC 3, HD 2*, bite 9+ 1d8, F1, ML 0, XP 29. Laying eggs |
| 17-18 | Gelatinous cube | 1 | [[Gelatinous Mass]] | 20’/60’, AC 1, HD 4***, 7+ 2d4 acid + ingurgitation, F2, XP 245. Full of rat skeletons ("a ghostly wall") |
| 19 | Ghouls | 1d6 | [[Grave Ghoul]] | 30’/90’, AC 3, HD 2**, 2 claws/bite 9+ 1d3 each + paralysis, F2, ML +1, XP 38. Feeding on a living City Watch officer (below) |
| 20-24 | Gray ooze | 1 | [[Grey Goo]] | AC 2, HD 3***, slam 8+ 2d8 acid, F2, XP 95. Looks like fresh cement over a hidden door |
| 25-29 | Green slime | 1 | [[Sage Slime]] | AC n/a, HD 2****, engulf 9+, F1, XP 56. On the ceiling |
| 30-31 | Cavern locusts | 1d10 | [[Cavern Locust]] | 20’/60’, AC 5, HD 2*, slam/bite or spit 9+, F2, ML -3, XP 29. Feeding on a mustard mold patch; they shriek (see Encounters) |
| 32-34 | Wererats | 1d8 | [[Wererat]] | 40’/120’, AC 2, HD 3*, bite or weapon 8+, F3, ML 0, XP 65. Mad Horned Rat cultists who do not know where the Shrine is |
| 35 | Ochre jelly | 1 | [[Ochre Ooze]] | 10’/30’, AC 1, HD 5**, 6+ 2d6 acid, F3, XP 500. Hungry |
| 36 | Rhagodessa | 1d4 | [[Rhagodessa (AX3)]] | 50’/150’, AC 5, HD 4+2*, leg 6+ grab / bite 6+ 2d8, F2, ML 0, XP 215 (inferred statline). Feeding |
| 37-41 | Rot grubs | 5d4 | [[Murder Maggot]] | AC 0, HD ½*, burrow, XP 5 each. In a refuse mound (below) |
| 42-43 | Shriekers | 1d8 | [[Shrieking Fungus]] | AC 2, HD 3, F1, XP 50. Scream (see Encounters) |
| 44 | Skeletons | 3d4 | [[Skeleton]] | 40’/120’, AC 2, HD 1*, 10+ 1d6 or weapon, F1, XP 13. Fresh, with improvised weapons. Made by a sinkhole of evil |
| 45 | Skittering maw | 1 | [[Skittering Maw]] | 20’/60’, AC 5, HD 8**, bite 3+ 2d10 + poison, F4, ML +4, XP 1,600. Bursts from stagnant water, attacks at once, **fights to the death** |
| 46-47 | Pit vipers | 1d8 | [[Viper Snake]] | 30’/90’, AC 3, HD 2*, bite 9+ 1d4 + poison, F1, ML -1, XP 29. **Automatically win initiative** |
| 48 | Giant pythons | 1d3 | [[Python Snake]] | 30’/90’, AC 3, HD 5*, bite/constrict 6+ 1d4/2d8, F3, ML -1, XP 350. Floating like logs |
| 49 | Giant black widows | 1d3 | [[Giant Black Widow]] | 20’/60’, AC 3, HD 3*, bite 8+ 2d6 + poison, F2, ML 0, XP 65. Webs block the tunnel |
| 50 | Giant crab spiders | 1d4 | [[Giant Crab Spider]] | 40’/120’, AC 2, HD 2*, bite 9+ 1d8 + poison, F1, ML -1, XP 29. Drop from above: **-2 to the party's surprise rolls** |
| 51 | Tarantulas | 1d3 | [[Giant Tarantula]] | 40’/120’, AC 4, HD 4**, 7+ 1d8 + poison or barbs, F2, ML 0, XP 190. Attack anyone who comes near their silk |
| 52-56 | Insect swarm | 1 (4 HD) | [[Insect Swarm]] | 10’/30’, AC 2, HD 4*, engulf, F0, ML +3, XP 135. 300+ sq ft blanket blocking the way, drawn to light |
| 57-62 | Rat swarms | 1d4 (each 1d3+1 HD) | [[Rat Swarm]] | 20’/60’, AC 0, HD 2*-4*, engulf 1d6 + prone, F0, ML -3, XP 29/65/135 by HD |
| 63-64 | Giant toads | 1d4 | [[Giant Toad]] | 30’/90’, AC 2, HD 2+2*, tongue or bite 8+, F1, ML -2, XP 47. One just snatched a sewer rat |
| 65-70 | Giant rats | 3d6 | [[Giant Rat]] | as 06 |
| 71-72 | Giant shrews | 1d4 | [[Giant Shrew]] | 60’/180’, AC 5, HD 1, 2 bites 10+ 1d6, F1, ML +2, XP 10. Burrows in the tuff |
| 73-74 | Giant ferrets + giant rats | 1d8 + 3d6 | [[Giant Ferret]], [[Giant Rat]] | ferret 50’/150’, AC 4, HD 1+1, bite 9+ 1d8, F1, ML 0, XP 15. Both attack anyone within 10’. Undisturbed, the rats flee at half numbers |
| 75-78 | Yellow mold | 1d4 | [[Mustard Mold]] | AC n/a, HD 2**, spores, F2, XP 38. A garden of coloured fungus and slime under a yellow haze |
| 79 | Zombies | 2d4 | [[Zombie]] | 40’/120’, AC 1, HD 2*, 9+ 1d8, F1, XP 29. Red-eyed vagabonds, made by a sinkhole of evil |
| 80-00 | Special encounter | — | `Tables/ax3-undercity-special.yaml` | nearest special location; none beyond 120’ |

### Encounters needing more than the table
- **19 Ghouls and the officer (p. 65):** the paralysed watch officer is at **-7 hp of 5**. If the party kills the ghouls quickly and treats his mortal wounds, it has a friend in the City Watch. He was trailing a member of the Argollëan Family ("Brotherhood" in the text) into the sewers.
- **37-41 Refuse mound (p. 66):** a knee-high heap with coins and bones. **Searching it** exposes the searcher to the brood of **5d4 rot grubs**. **Crossing it:** Paralysis save, or one grub gets in through trouser leg or sandal. Holds **2d100gp** from a dead adventurer.
- **44 / 79 Sinkhole of evil (p. 66):** the fresh skeletons and red-eyed zombies show that a sinkhole of evil somewhere in the Undercity is raising the dead (location not given: Judge's call to place one).
- **45 Skittering maw (p. 66):** described as the apex predator of the Undercity. It never checks morale.
- **06 / 73-74 Vermin fights (pp. 64, 66):** anyone within 10’ is attacked by both sides. Left alone, the rats flee once they lose half their number, and the winners eat the rest.

## Special locations (pp. 66-67)
The keyed lairs below, with their special-encounter rows in `Tables/ax3-undercity-special.yaml`. The keys themselves are in the district notes (and their `Dungeons/` notes):

| # | Location | District (note) | AX3 key |
| --- | --- | --- | --- |
| 11u | The Mink / Argollëan Family | [[Old District]] | p. 73 |
| 13u | Shrine of the Horned Rat | [[Old District]] | p. 88 |
| 14u | Doppelgänger Den | [[Old District]] | p. 92 |
| 28u | Lizardman Lair | [[Festival District]] | p. 102 |
| 36u | Catacombs of the Patriarchs | [[Bridge District]] | under the Solar Citadel (#36) |
| 45u | Crocodile Nest | [[Plaza District]] | p. 138 |
| 50u | Tower of Knowledge (basement) | [[Tower District]] | p. 145 |
| 68u | Catacomb of the Ancestors | [[Temple District]] | under the Shrine of the Ancestors (#68) |
| 69u | Eclipse Hideout | [[Temple District]] | p. 166 |
| 75u | Vagrant Colony and Death Cult Hideout | [[Lake District]] | p. 179 |
| 78u | Prefect's Dungeon | [[Palace District]] | p. 187 |
| 81u | Barracks Vault | [[Palace District]] | p. 188 |

Special-encounter highlights (full rows in the YAML):
- **13u:** the 8 wererats search for the way into the Nethercity: Terkinos (Mage 3 wererat) from noon to midnight, Abimbola (Fighter 4 wererat) from midnight to noon. A lead into SOTN (separate module notes).
- **78u:** the escaped hood. His employer on 1d10: 1-4 Argollëan Family, 6-8 Sand & Bones, 9-10 lone wolf. **5 is not assigned in AX3** (Judge's call: Argollëan Family). While the party escorts him, throw 1d6 every minute: **5+** brings **1d4+1 Watch officers**. Turning him in pays **40gp**.
- **81u:** 2d4 Prefectural Guards. Statline inferred: the legionaries of city encounter 81-84 (Fighter 1; AC 7, HD 1, hp 6, 10+, 1d6+1, F1, ML +3, XP 10). They carry torches.

## Hooks
- The sealed grate of city encounter 65-68 opens onto the Undercity, and so do the 10% random basements in the Bridge, Lake and Old Districts.
- The Horned Rat wererats are searching for the Nethercity entrance. Their wandering packs (32-34) do not know where the Shrine is.
- The ghouls' victim (19) and the Prefect's Dungeon escapee (78u) can earn favour with the Watch or with a syndicate.
- Ancient Argollëan writing and sylvan paintings on the old slabs are lore of the elven city.
