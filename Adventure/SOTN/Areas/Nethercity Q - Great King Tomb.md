---
type: dungeon-level
level: 4
hex: "18.05"
tags:
  - sakkara/secret
source: "SOTN pp. 120-123 (map pp. 23, 182-183)"
---

# Nethercity Q — Great King Tomb

The tomb of **Marcan**, the great king who won the Bitter War against the dwarves (**1900 BE**), cut into the rock west of the sub-abyssal river and opening off its banks at **P3** (the front door) and **P4** (the builders' secret way, through Q6). It lies on the **Sub-Abyssal** level (Judge's call: the book names no level; it is entered from the river banks). Gold-streaked black marble panelling, black marble floors, gold mosaics of the king's reign, much cracked by ancient quakes. Marcan was mummified in the era when the elves kept all their power in undeath: he is a 13 HD **mummy warlord**, guarded by four mummy warlords of his elite guard and eight bronze statues. No light; no blighted sinkhole. Hub [[SOTN Hub]]; doors, slab-door waking, mummies and treasure conventions in [[Nethercity Features]]. Pages are printed pages.

**Orientation:** SOTN's text for Q (as for O and P) is written with its north where the printed map has west; the directions below are the text's.

Running: Temple / Tomb column, `level: 4` — 1d6 every 3 turns, 6+ → 2d10 on `Tables/sotn-wandering-temple-tomb.yaml`. The **P3 slab door** wakes the Q1 warlords (door rule, [[Nethercity Features#Doors (SOTN p. 11)]]); a fight in Q1 brings the Q5 statues on **round 2** and the rest with Marcan on **round 4**; entering **Q5** first (by the secret way) wakes Marcan and the statues at once, and the Q1 warlords join after 2 rounds. Both slab doors of Q2 are **glyphed** (password "Marcan").

## Layout
- **Entrances:** (a) the stone slab door in the **east** wall of **Q1** from the grotto **P3** ([[Nethercity P - Sub-Abyssal River Banks]]); (b) the **secret** way: river bank **P4** → 60’ winding tunnel north → volcanic cave **Q6** → secret panel door → burial chamber **Q5**.
- **Q1** (antechamber): a 5’ foyer from the P3 door; in the south wall, near the entrance, a glyphed slab door to the vault **Q2**; in the middle of the south wall, an opening into the gallery **Q3** (SOTN calls it a hallway in Q1 and a lion archway in Q3: Judge's call, a lion archway); in the middle of the west wall, a cracked marble archway with bronze lions to the burial chamber **Q5**.
- **Q3** runs 40’ south: halfway along, on its east wall, the second glyphed slab door into **Q2**; at its south end another lion archway into the canopic annex **Q4**.
- **Q5** → secret panel in its south mosaic → **Q6** → tunnel south to the river at **P4**.

## Encounters at a glance
| Where | Who | No. | Engine note |
|---|---|---|---|
| Q1 | mummy warlords (the king's elite guard) | 4 | [[Mummy]] + [[Elven Warlord]] 5 |
| Q5 (to Q1 on rounds 2 and 4) | bronze animated statues of elven warriors | 8 | [[Bronze Animated Statue]] |
| Q5 (to Q1 on round 4) | Marcan, the great king, mummy warlord | 1 | [[Marcan (SOTN)]] ([[Mummy]] + [[Elven Warlord]] 13) |

## Factions
- **The king's household:** Marcan, his four guards and his eight statues act as one; the statues and guards obey him. First reaction on waking is wrath (every mummy); a parley or a spared or fled-from mummy uses `Tables/sotn-mummy-reaction.yaml` ([[Nethercity Features#Necromancy and the mummies (SOTN pp. 16-17)]]). Marcan is a proud conqueror who held lizardmen as slaves and humbled the dwarves; he despises dwarves and anything that looks like a lizardman, and may hear out those who address him as a king (Judge's call).
- **Dwarves:** the egg of the earth in P8b was taken from Azen Khador in Marcan's war; a dwarf in the party is a mortal insult to him (Judge's call: −2 on any reaction).
- The **sword of command** (Q5) is a key elsewhere: the magically locked bronze door in the Northern Caves opens for whoever bears it (SOTN p. 100, [[Nethercity M - Northern Caves]]).

## Rooms (SOTN pp. 120-123)

### Q1. Great King Tomb Antechamber (1900 BE)
- **Exits:** E (through the 5’ foyer) stone slab door to P3; S wall near the entrance glyphed stone slab door to Q2; middle of the S wall opening to Q3; middle of the W wall cracked lion archway to Q5.
- > [!player]
  > Past the slab door, a short foyer of 5’ opens into an antechamber 20’ wide and 30’ long with a 10’ ceiling, panelled in black marble streaked with gold and floored in black marble tiles. The north wall is a mosaic in glittering gold, purple and red of a great king ruling a splendid realm. In the south wall, near where you came in, is a stone slab door with an Ancient Argollëan inscription; in the middle of that wall a passage leads south. In the middle of the west wall stands a marble archway inlaid with rampant bronze lions, twisted and cracked by old earthquakes, like much of the mosaic. In the centre of the room, on a long low dais plated with bronze, rest four bronze sarcophagi gilded with gold.
- **Monster:** each sarcophagus holds a **mummy warlord** of the king's elite guard, armed as in life: bronze scale armour (as chain mail), conical bronze helmets with cheek-guards and plumes, round bronze shields, curved bronze swords. They begin to wake when the P3 slab door is first disturbed; how far along they are follows the door rule (1st attempt stirring, 2nd out, 3rd+ ready).
  - **4 mummy warlords** (5th-level abilities) → [[Mummy]] + [[Elven Warlord]] 5: STR 15; MV 20’ / 60’ (SOTN 60’), AC 11 (mummy 6 + scale as chain 4 + shield 1), HD 5+1**, hp 28, 26, 25, 22, touch 4+ or sword 4+, D 1d12+3 extraordinary bludgeoning and extraordinary necrotic + mummy rot (touch) or 1d6+6 (sword: +3 armed mummy, +1 STR, +2 warlord; no rot), Save F5, ML +4, AL C, XP 660 each. Horrific visage, mummy rot (no magical healing), immunities as the MM mummy. Warlord powers at 5th level: damage +2 (included), inspire courage 1/day (+1 to attack, damage, morale and saves against magical fear for allies within 50’, 1 turn; [[Elven Warlord]]). Proficiency: Combat Reflexes (+1 to surprise and initiative).
  - **Round 2** of the fight: **4 bronze statues** come from Q5; **round 4**: the other **4 statues** and **Marcan** (statlines at Q5).
- **Lore:** Loremastery, or Knowledge (history) at −4: the king in the mosaic is **Marcan**, victor of the Bitter War against the dwarves. Knowing his name lets the party pass the glyphs on the Q2 doors.
- **Lore / Trap (slab door to Q2):** read in Ancient Argollëan: "Enter in the name of the king." A **blast rune** ([[Rune of Warding]], SOTN blast glyph of warding) fires when any creature touches the door without speaking **"Marcan"**: **24 electrical damage** (Blast save for **12**) to everyone within **10’** of the door. The door radiates magic; a Searching throw spots the faint tracery of the rune on the stone. Cast at **12th level** (for [[Dispel Magic]]). Forcing the slab: −12.
- **Loot:** the gold in the mosaic is real (**100gp**; SOTN gives no weight or removal time); 4 gilded bronze sarcophagi (**3,500gp, 20 st each**). **Tally: 14,100gp, 80 st.**

### Q2. Great King Tomb Vault (1900 BE)
- **Exits:** N glyphed stone slab door to Q1; W glyphed stone slab door to Q3.
- > [!player]
  > A vault 25’ by 25’ and 10’ high, its walls of gold-streaked black marble, its floor black marble. In it stands a throne of gold, ivory and ebony; on the seat rest a gold crown crusted with red and black gems and a collar of gold. A great black fan with golden feathers leans against the throne, and a pair of golden sandals stands at its foot. On one wall hang eight round golden shields above a golden chariot decorated with white serpents; against the opposite wall stand three cedar chests with bronze fittings.
- **Loot:** ebony throne with ivory overlay and gold-leaf panels (**2,000gp, 10 st**); gold crown set with rubies and black sapphires (**8,000gp**); collar cut from a single sheet of gold (**800gp**); large gilded ebony fan with gold-dipped lammasu plumes (**800gp, 4/6 st**); pair of ceremonial gold sandals (**1,000gp, 1 st**); gilded ebony light chariot decorated with ivory serpents (**4,000gp, 10 st**); 8 gilded cedar shields (**100gp, 1 st each**); 3 cedar chests with **1,000gp** each (**3,000gp, 3 st**). **Tally: 20,400gp, 32 4/6 st.**

### Q3. Great King Tomb Annex Hallway (1900 BE)
- **Exits:** N lion archway to Q1; E (midpoint) glyphed stone slab door to Q2; S lion archway to Q4.
- > [!player]
  > Beyond the lion archway, a gallery 40’ long, 10’ wide and 10’ high. Its west wall is a mosaic of a king in golden armour riding a chariot in triumph through cheering crowds; its east wall is panelled in black marble flecked with gold. Halfway along the east wall stands a stone slab door with an Ancient Argollëan inscription. Past it, the gallery ends at another marble archway with bronze lions.
- **Loot / Lore:** the mosaic gold is real (**100gp**); Loremastery, or Knowledge (history) at −4: the king is **Marcan**, victor of the Bitter War. **Tally: 100gp.**
- **Lore / Trap:** the slab door to Q2 bears the same inscription and the same **blast rune** as its twin in Q1 ("Marcan"; 24 electrical, Blast save for 12, within 10’; CL 12).

### Q4. Great King Tomb Annex (1900 BE)
- **Exits:** N lion archway to Q3.
- > [!player]
  > The gallery opens into an annex 30’ wide and 20’ deep with a 10’ ceiling, all its walls panelled in gold-flecked marble. In the middle stands a great canopic shrine of gilded wood decorated with gold lions. Smashed pottery covers the black marble floor around it, though about a dozen vases and jars are still whole.
- **Loot:** canopic shrine (**2,000gp, 7 st**) enclosing 4 terracotta canopic jars of embalmed organs (**25gp, 1/6 st each**); among dozens of broken vases, 6 red-figure terracotta vases (**7gp, 2/6 st each**) and 7 more canopic jars of embalmed organs (**25gp, 1/6 st each**), those of the Q1 mummies. **Tally: 2,317gp, 10 5/6 st.**
- (Marcan is a mummy, not a mummy lord: his organs here do not bring him back. Judge's call: SOTN gives them no power.)

### Q5. Great King Burial Chamber (1900 BE)
- **Exits:** E lion archway to Q1; **secret door** in a panel of the south mosaic to Q6.
- > [!player]
  > *(Entered after the fight in Q1:)* A burial chamber 30’ wide and 45’ long under a soaring 25’ ceiling. The north, west and south walls are one shining mosaic of glittering cities and golden palaces, where crowds of lizardmen toil for the pleasure of an elven nobility. On a dais rising from the black marble floor stands a sarcophagus of pure gold shaped in the likeness of the cold, arrogant king of the mosaics. Its lid has been pushed aside and the golden coffin lies empty.
  >
  > *(Entered before Q1, e.g. by the secret way:)* The same chamber, with the same mosaics and the golden sarcophagus of the king on its dais, closed. Around it, as if on guard, stand eight bronze statues of elven warriors in armour.
- **Monster:** only if Marcan and his statues have not already been met in Q1 are they fought here: they come to life **as soon as anyone enters**. The Q1 warlords, if still standing, join **2 rounds** later.
  - **8 bronze animated statues** → [[Bronze Animated Statue]]: MV 20’ / 60’ (SOTN 30’), AC 6, HD 5*, hp 30, 25, 24, 23, 22, 21, 20, 18, bronze short sword 6+, D 5d4 extraordinary bludgeoning (MM slam; SOTN short sword 2d6), F5, ML n/a, AL N, XP 350 each (SOTN AC 5, HD 5**, XP 500). Immunities, resistances and **weak point** as at [[Nethercity O - Sub-Abyssal Secret Tomb of the Hierophant#O2. Secret Tomb Guardian Chamber (1700 BE)|O2]] (Searching throw as an action; aimed attacks −4 bypass immunities; unmodified 20 destroys).
  - **Marcan, the great king, mummy warlord** → [[Marcan (SOTN)]], [[Mummy]] with the class abilities of a 13th-level [[Elven Warlord]]: STR 16, INT 13, CHA 16; MV 40’ / 120’ (SOTN 120’), AC 11 (mummy 6 + scale as chain +1; SOTN prints 12, which needs a shield he does not carry), HD 13**, hp 65, touch −4+ or short sword +2 −6+ (HD 13 = −2+, STR +2, sword +2; SOTN −1+ and −2+), D 1d12+7 extraordinary bludgeoning and extraordinary necrotic + mummy rot (touch; STR +2, warlord +5; SOTN Q5 prints +8, its Q1 copy +7) or 1d6+12 (short sword +2: +3 armed mummy, +2 STR, +5 warlord, +2 magic; no rot; SOTN 1d8+10), Save F13, ML +4, AL C, XP 3,400. Horrific visage, mummy rot, immunities as the MM mummy. Warlord powers, **Combat Reflexes** (+1 to surprise and initiative), **Weapon Focus** (swords and daggers: an extra die of damage on an unmodified 20; SOTN ×2 damage). Commands the sword's **word of command 3/day** (below). (SOTN's Q1 copy of his line says "sword +1", the Q5 copy "+2"; the item is +2.)
- **Loot (on Marcan, wherever he is fought):** bronze scale armour worked with tiny gold runes = **chain mail +1** (apparent value 650gp); boar's-tusk helmet with a great red crest = **helm of comprehending languages** → [[Helm of Comprehension]] (apparent value 100gp); sickle-shaped meteorite-iron sword with a hilt shaped like a golden crown = the **sword of command** → [[SOTN Magic Items#Sword of Command]] = [[Short Sword +2, Command]] (a short sword +2; three times a day its wielder, pointing it at a target, speaks a [[Word of Command|word of command]] with a stentorian voice; 21,000gp; apparent value 650gp). **In the room:** Marcan's pure-gold sarcophagus (**20,000gp, 20 st**). **Tally: 20,000gp, 20 st** (magic excluded; SOTN gives no room total).
- **Trick:** a **secret door** hidden in a panel of the south mosaic, the builders' way out after sealing the tomb (Searching); found, it opens by turning the panel on its vertical axis, onto Q6.

### Q6. Great King Tomb Secret Entrance (1900 BE)
- **Exits:** N secret panel door to Q5; S winding volcanic tunnel to the river at P4 ([[Nethercity P - Sub-Abyssal River Banks]]).
- > [!player]
  > *(From Q5:)* The secret door opens on a volcanic cavern about 20’ wide, from which a winding volcanic tunnel runs south. From that way comes the lapping of the underground river.
  >
  > *(From P4:)* From the river, the twisting volcanic tunnel winds north for about 40’ and ends in a volcanic cave some 25’ across.
- **Trick:** the cave's north wall hides a **secret door**, a panel carved on this side to look like natural rock (Searching); found, it turns on its vertical axis onto the burial chamber Q5. Entering Q5 this way wakes Marcan and his statues at once (Q5).
- (Tunnel length: 40’ here, 60’ at P4: SOTN inconsistency, Judge's call: 60’.)

## Treasure and XP summary
| Room | Treasure | Weight |
|---|---|---|
| Q1 | mosaic gold, 4 sarcophagi: 14,100gp | 80 st |
| Q2 | throne, crown, collar, fan, sandals, chariot, shields, 3,000gp: 20,400gp | 32 4/6 st |
| Q3 | mosaic gold, 100gp | — |
| Q4 | canopic shrine, jars, vases: 2,317gp | 10 5/6 st |
| Q5 | Marcan's gold sarcophagus, 20,000gp | 20 st |
| **Total** | **56,917gp** (magic excluded) | **143 3/6 st** |

SOTN gives no area total; this is the sum of its room tallies (Q5's from its one valued item).

**Magic:** chain mail +1 (Marcan's scale; Q5); [[Helm of Comprehension]] (helm of comprehending languages, Q5); [[SOTN Magic Items#Sword of Command]] = [[Short Sword +2, Command]] (Q5, 21,000gp).

**Monster XP:** 4 mummy warlords 2,640; 8 bronze statues 2,800 (SOTN 4,000); Marcan 3,400. **Total 8,840** (SOTN's statlines 10,040).
