---
type: dungeon-level
level: 2
hex: "19.19"
tags:
  - sakkara/secret
source: "AX1 pp. 53-64 (map p. 54)"
---

# Level 2 — The Catacombs

Hewn limestone rooms (brick floors, 10’ passages and ceilings) in the north, natural caves elsewhere (5’-15’ tunnels, ceilings as wide; caverns 10’ high unless noted). The Stone's taint has covered rooms and tunnels with thick fleshy "roots" leaking harmless bloody fluid, pulsating ichorous slime, chitin growths; air hot, wet, foul — "a sinister birthing womb". The whole level is tainted: water drunk here causes mutations (see [[AX1 Magic Items]], the Stone). Pages are printed pages; "(map)" = read from the low-resolution map.

Running: hub [[AX1 Hub]]; wandering 1d6 every 2 turns (and on loud noise), 6+ → 1d8 table `Tables/level2-wandering.yaml`, standard distance, random direction. Pass these explicitly to `acks.sh location` (the hub's `--hub` read covers level 1 only).

## Layout
- **Entrances:** (a) from L1 75 (Idimmu's vault) a long stair, 35’, into **1**; (b) from L1 53 a stair into **18** (natural cavern; its door out is wizard locked) opening onto the Bloody Shore 16; (c) from L1 18 the spiral stair into **29**, whose west mouth is barred (to 28); (d) from L1 42 the well shaft into the ceiling of **20** above the large 'tree'; (e) the secret **escape tunnel 27** to the outside, far from the temple entrance (only the Lady knows it).
- **North-west, hewn block (1-4, 10-13, 21-22):** room 1 (stair) and a long east-west hewn corridor with doors: N to 10, to the cave passage up to 15, to 14; S to 2, 11, 12, 13; W end door to 4, beside the mouths of caves 3 (NE-running tunnel, weak wall into 10) and 5 (crossroads to 6 and 7). Two doors in the south side of room 1: one to a hewn passage and room that look through stone pillars into gnoll cave 8; one to a rubble-strewn passage that runs east to the Outer Fane 22 (and on east to the Lake of Blood 20; 21 opens off it) and south to 23.
- **West caves:** 8 (Black Fang guards) runs south to 9 (Black Fang cavern; chest in its southern tip).
- **North-east caves:** 15 (Red Eye cavern) joins 16 (Bloody Shore, wizard-locked door to 18, cave 17 off its north side, gap blocked by moldy boxes into 14). 16's pool is the north end of the **Lake of Blood 20** (map: continuous fluid). 19 (abomination nest) opens off the lake's east side.
- **Centre:** the **Inner Fane 38** in a whorl of curved rock ribs; between the ribs passages lead to 24 (N, from 23), 39 (NE, the Lady's chamber), 36 (SE, to the Pool of Blood 25 and on to 20), 34 (S), 35 (SW) and toward 9 (W) (map; the rib gaps are hard to read).
- **South:** 25 → 26 (crescent of bloody water with a narrow path; beach to the escape tunnel 27 in the east; 28 opens off its south-west); 29 (spiral stair) ↔ bars ↔ 28 (ghoul nest) → 30 (oozing corridor) → 31 (slime chamber) → 32 (organic tunnel north toward 35); 33 (chitin cavern) between 30/28 and 34; 37 (bone lair) off 36 (map).
- **Guard posts facing intruders:** 23 zombies (door SW), 24 abomination (doors both ends), 34 skeletons and 35 zombies (face south-east), 22 priests.

## Wandering monsters (1d8, p. 53)
| 1d8 | Monster | No. | Engine note | Module line | Treasure | Flavour |
|---|---|---|---|---|---|---|
| 1 | Brigands | 2d4 | [[Brigand]] | AC 2, HD 1, 1d6, 120’, F1, ML 0, XP 10 | 1d10sp | Drusus' patrol, trapped below when the L1 18 door was sealed; terrified, want to go home: **+1 reaction** to peaceful overtures |
| 2 | Troglodytes | 1d8 | [[Troglodyte]] | AC 4, HD 2, 3 attacks 1d4 each, 120’, F2, ML +1, XP 20 | 2d6gp | called by the Stone but **do not serve the Lady**: hate surface folk, want to murder her and take the Stone; stalk the party with chameleon skin hoping to be led to her |
| 3 | Orcs | 2d4 | [[Orc]] | AC 3, HD 1, 1d6, 120’, F1, ML 0, XP 10 | 1d12sp | raiding the weakened Black Fangs (8-9): warn off, ignore, or invite to "join in the fun" (reaction) |
| 4 | Kobolds | 2d4 | [[Kobold]] | AC 2, HD 1d4, 1d6−1, 60’, 0-lvl, ML −2, XP 5 | 1d12cp | Idimmu's messengers to the Lady, arrogant, threaten draconic doom; the message concerns the party's recent deeds (warnings of intruders, a tribe destroyed…) |
| 5 | Zombies | 2d4 | [[Zombie]] | AC 1, HD 2, 1d8, 60’, F1, ML n/a, XP 29 | — | sacrificial victims of the Inner Fane (hearts cut out): merchants, farmers, grandparents, children; missing kin may be among them |
| 6 | Ghouls | 1d6 | [[Grave Ghoul]] | AC 3, HD 2, 3 attacks 1d3+paralysis, 90’, F2, ML +1, XP 29 | — | squabbling over a pot-bellied kobold corpse; turn on the party |
| 7 | Hobgoblins | 1d6 | [[Hobgoblin]] | AC 3, HD 1+1, 1d8, 90’, F1, ML 0, XP 15 | 1d6gp | deserters who refused the attack on the goblins, exiled below, hungry and thirsty; try to **capture** the party as slaves to buy their way back to Thethamun |
| 8 | Gnolls | 1d3 | [[Gnoll]] | AC 4, HD 2, 2d4, 90’, F2, ML 0, XP 20 | 1d8gp | Red Eyes who drank from the Bloody Shore: one random mutation each (Abominable Mutation table); going to beg the Lady's forgiveness |

## Factions (level 2)
- **The Lady Below (38-39)** commands all; Ur-Namu's priests (21-22) test visitors.
- **Red Eye gnolls (10, 15):** favoured; tend the breeding vats. Visitors who convince them they are friendly to the Lady are escorted to Hepsis, then to Ur-Namu. **Attack on sight anyone with Black Fang gnolls.**
- **Black Fang gnolls (8-9):** exiled, out of favour, weakened by a failed robbery of the ogres. **+2 reaction** if approached peacefully; Ur-Shet will partner against the ogres or the Red Eyes (+2 when broached).
- **Ogres (7):** others fear them; their den is a safe resting place once they are dealt with.
- **Troglodytes (wandering):** enemies of the Lady.
- Undead (23, 34, 35) and abominations (16, 19, 20, 24, 36) serve her; undead attack anyone not presenting a (prominent) unholy symbol.

## Replacement of casualties (p. 53)
While the Lady and the Stone remain: each week roll 1d6 per cleared room; **1-3**: 1d6 similar creatures arrive. A tribe wiped out does not return; leaders killed → the rest leave within a week, taking known treasure. **Abominations, skeletons, zombies, ghouls:** replaced on **1-4**, never leave.

---

## Caves and chambers (pp. 54-63)

### 1. Catacomb Entrance
- **Exits:** stair up (35’) to L1 75 vault; the hewn E-W corridor (doors N to 10, the passage to 15, 14; S to 2, 11, 12, 13; W door to 4; W end open to caves 3 and 5); two doors in the south side (to the hewn room beside 8, and to the rubble passage to 22/23) (map).
- Behind the staircase a dozen boxes and jars of moldy food and rotted clothes (worthless).

### 2. Prisoner Room
- **Exits:** N door to the corridor (map).
- 30’ × 30’. A dozen skeletons shackled to the walls (rusted chains break easily); one has an odd torso and an elongated muzzle: Healing proficiency reveals a **Thrassian** (lizardman).

### 3. Carrion Cavern
- **Exits:** SW mouth at the west end of the corridor; long narrow tunnel running NE (map).
- Stench worsens inward. **2 carcass scavengers** at the rear → [[Carrion Horror]] (ACKS II equivalent): MV 120’, AC 2, HD 3+1, hp 15, 13, 8 attacks, paralysis, F2, ML +2, AL N, XP 135.
- Among three victims' remains: **50gp in assorted coins, silver ring (150gp)**.
- **Weak point** ~55’ up the tunnel where room 10's excavation nearly broke through the SE wall: each time the party passes, a hidden proficiency throw (hear noise) to overhear the gnolls in 10. Can be found as a secret door; broken through in one round with a blunt weapon.

### 4. Torture Room
- **Exits:** E door to the corridor's west end (map).
- 30’ square. Rusty bloodstained instruments on west shelves (whips, bronze cudgel, four-clawed breast ripper, foot-roasting plates, surgical saw, small hammer); breaking wheel and rack (W wall); unanimated skeletons chained on the south wall, bones warped and broken.

### 5. Failed Assault
- **Exits:** cavern crossroads: S toward the corridor's west end and 4's door; N to 7; NE to 6 (map).
- Four recently slain, stripped gnolls (one beheaded, one cleaved in two, two bludgeoned) — Black Fangs who tried to rob the ogres in 7; the ogres' argumentative bellowing is audible here.

### 6. Collapsed Tunnel
- **Exits:** SW to 5. Destroyed by the earthquake; clearing it is a 20gp construction project (about 3 weeks for a 6-person party). Destination left to the Judge.

### 7. Ogre Den
- **Exits:** S to 5 (map).
- **2 ogres**, loud, arguing and wrestling: the party cannot be surprised approaching, and the ogres are **Distracted** (−2 to their surprise rolls) → [[Ogre]]: MV 90’, AC 4, HD 4+1, hp 20, 15, D 1d10 (smaller: a broken stalagmite) or 1d6+4 with the larger's **sword +1** (Zaharan, backward-curved blade, cobra hilt), F4, ML +2, AL C, XP 140.
- Two bags of coins in the corner: **400gp and 600gp** (Auran and Zaharan).
- Other monsters avoid this room: once the ogres are dealt with, the party can **rest here without wandering encounters**.

### 8. Gnoll Lair (Black Fang)
- **Exits:** N toward 4/5 and the hewn block; E through gaps between massive floor-to-ceiling stone pillars into a hewn room (connected to room 1's south door); S to 9 (map).
- **3 Black Fang gnolls** guard the gaps between the pillars; leather, battle axe, shield, 3d6gp each → [[Gnoll]]: MV 90’, AC 4, HD 2, hp 10, 9, 8, D 1d6+1 (as printed here), F2, ML 0, AL C, XP 20.
- **Ulmash** (champion; ring mail, morning star, shield; broken Common) → [[Ulmash (Sakkara)]]: AC 5, HD 3, hp 16, D 1d6+2, F3, ML 0, XP 50.
- **+2 reaction if approached peacefully**; readily take the party to their leader. Fighting: reinforced from 9 in 2 rounds; morale break → retreat to 9.

### 9. Black Fang Cavern
- **Exits:** N to 8; possibly E between rock ribs toward 38 (map, unclear).
- Exiled by the Red Eyes. **Ur-Shet** (speaks Common well) → [[Ur-Shet (Sakkara)]]: AC 6, HD 4, hp 20, D 1d6+2, F4, ML 0, XP 80; **3 Black Fang gnolls** → [[Gnoll]]: hp 10, 9, 8, D 2d4 (as printed here), F2, ML 0, XP 20.
- Ur-Shet would partner with adventurers who mean to strike the ogres or the Red Eyes (+2 reaction if broached).
- **Chest hidden in the southern tip** of the cave: **650cp, 1,400sp, 340gp, scroll of ward against magic** (Ancient Zaharan; the gnolls cannot read).

### 10. Guard Room (Red Eye)
- **Exits:** S door to the corridor (kept open); the thin SE wall of tunnel 3 (map).
- 30’ square. **3 Red Eye gnolls** (printed "(3)" with four hp values 12, 10, 9, 8 — use the first three, or four (ambiguous)) → [[Gnoll]]: AC 4, HD 2, D 2d4, F2, ML 0, XP 20. Leather, spears, swords, shields, 3d6gp each.
- Demand that arrivals announce themselves. A convincing case of friendship to the Lady → escorted to the chief in 15. **Accompanied by Black Fangs → attacked on sight.**

### 11. Store Room
- **Exits:** N door to the corridor. 20’ × 30’, empty; beastman spoor; the gnolls use it as a latrine.

### 12. Store Room
- **Exits:** N door to the corridor. 30’ square: **40 bags of wheat (20gp total, 160 st), 4 barrels smoked pork (20gp total, 16 st), 18 barrels Krysean beer (180gp total, 144 st)** — about a week's supplies for the level.

### 13. Empty Room
- **Exits:** N door to the corridor. 20’ square; empty beer barrel, hemp sacks with grain kernels.

### 14. Moldy Room
- **Exits:** S door to the corridor; E wall a 6’ high, 8’ wide gap into the great natural cavern (16), **blocked by six boxes covered in yellow mold**.
- Moving the boxes releases spores → [[Mustard Mold]] (ACKS II yellow mold): MV 0’, AC n/a, HD 2**, hp 9, 1d6 + poison spores, F2, ML n/a, AL N, XP 38.

### 15. Gnoll Cavern (Red Eye)
- **Exits:** S passage to a door on the corridor (between 10 and 14); E into 16 (map).
- Red Eyes tend the breeding vats for the Lady. **Hepsis** (chief, glass eye) → [[Hepsis (Sakkara)]]: AC 4, HD 4, hp 20, D 1d6+2, F4, ML 0, XP 80; **4 Red Eye gnolls** → [[Gnoll]]: hp 12, 10, 9, 8, D 2d4, F2, ML 0, XP 20. All have long bows and 20 arrows, spears, swords, shields, leather.
- **−2 to reaction rolls** with Hepsis unless introduced by the gnolls of 10. Friendly or Neutral: a gnoll escorts the party to **Ur-Namu in 22**. Any other result: he orders the attack. Always attack if Black Fangs accompany the party.
- **Loot pile (N wall):** **1,000cp; 1,000sp; 1,000ep; 2 crates Krysean pottery (100gp, 5 st each); 87 cattle horns (2gp, 1/5 st each); 36 bottles fine Tirenean wine (15gp, 1/5 st each); crate of legionary arms (3 banded plate, 3 shields, 3 swords, 5 daggers; 225gp, 10 st).**

### 16. The Bloody Shore
- **Exits:** W to 15; N to 17; NE wizard-locked door to 18; the 14 gap (W, blocked by moldy boxes); S the pool merges into the Lake of Blood 20 (map).
- Oval cavern ~80’ × 50’, stalactite ceiling ~25’, 20’-thick central pillar; reddish "roots" everywhere bleed blood-like sap when cut. **Birthing pool** of thick blood-like fluid at the back, 5’ deep.
- **1 abomination** lurks in the pool; surfaces only if someone enters or touches it → [[Abomination (Sakkara)]]: MV 90’, AC 4, HD 3+1**, hp 18, 1d4/1d4/1d4 + paralysis, D4, ML +2, AL C, XP 135.
- **Pool effects:** a wounded creature touching the fluid heals 1d4 hp (once per day), but the wound heals twisted (scales, moving lumps, discoloration, feathers…): **−1 to all reaction rolls**, stacking with mutations. Touching has no effect on the unhurt. **Drinking:** each drink save vs Spells or roll on the **Abominable Mutation table** (below). **Full immersion:** heals 1d4 per round and one mutation per round, no save. Mutations are cumulative; total mutation reaction penalty −12 or worse → transformed into an abomination. Removal: per mutation, remove curse then restore life and limb, both from an 11th+ level Lawful caster. Fighting in the pool: −2 to attack throws and AC (abominations unaffected); a paralyzed character in the pool falls in and is immersed; abominations dunk foes with a wrestling maneuver.

**Abominable Mutation table (1d20, p. 57)**
| 1d20 | Mutation |
|---|---|
| 1 | **Deformity:** roll on the mortal wound table, modified only by CON; permanent wounds show as melting, boiling flesh |
| 2 | **Beast eyes:** infravision 60’; −2 reactions |
| 3 | **Discoloration:** −2 reactions |
| 4 | **Fur:** +1 save vs cold; −2 reactions |
| 5 | **Scales:** +2 AC; max movement −25%; −4 reactions |
| 6 | **Claws:** two claw attacks 1d4−1; magic-harming at 5th level; −2 on delicate work (traps etc.); −2 reactions |
| 7 | **Distorted muscles:** +1 STR (max 18), −1 CHA (min 3) |
| 8 | **Flexible bones:** +1 DEX (max 18), −1 CON (min 3) |
| 9 | **Bulging brain:** no normal helms; +1 INT (max 18), −1 CHA (min 3) |
| 10 | **Seductive musk:** +1 reactions with humanoids; −1 to surprise rolls downwind or vs keen-scented creatures |
| 11 | **Fish scales:** breathe water 1 turn; swim 30’/turn; −2 reactions vs non-aquatic beings |
| 12 | **Tentacles:** hold objects, no weapons; instead of normal attacks, two tentacle attacks 1d3−1 (+STR); magic-harming at 5th level; −2 reactions |
| 13 | **Third eye:** +1 to avoid surprise; −2 saves vs gaze; −2 reactions |
| 14 | **Crystal body:** +3 AC; immune to petrification; counts as stone for oozes; max movement halved; −2 saves vs sound; −4 reactions |
| 15 | **Arcane eyes:** glowing eyes; cast one random 1st level arcane spell (fixed) once per hour (Judge may reroll unbalancing spells); −2 reactions |
| 16 | **Wings:** no flight; large leaps (as jump) where there is room, if carrying ≤4 stone and wearing no normal armour (special armour ≥2× price) |
| 17 | **Viscous bile:** +2 saves vs ingested poison; once per day spit acid 30’ (ranged attack throw): 2d6, all within 10’ save vs Blast or 1d3; dissolves 1” of wood, not metal or stone; each spit −1 reactions cumulative (max −4) |
| 18 | **Bubbling skin:** −2 reactions; permanent fire resistance (+2 saves vs fire, −1 damage per die) |
| 19 | **Eye stalks:** +1 to avoid surprise; look round corners; −4 reactions |
| 20 | **Goat legs:** −2 reactions; no boots or leg armour (physical armour AC −1); +30’ base movement (+10’ combat) |


### 17. Slimy Chamber
- **Exits:** S to 16 (map).
- Humid cavern thickly covered in damp green algae and lichen. Prodding and searching: **75% each round** the green slime on the roof drops on a random character; **−3 to surprise** (it matches the plants) → [[Sage Slime]] (ACKS II green slime): MV 3’, AC n/a, HD 2**, hp 10, special, F1, ML n/a, AL N, XP 38.

### 18. Entry Chamber
- **Exits:** stair up to L1 53; door out (to 16) **wizard locked by Zakiti (caster level 3)**.
- 50’ × 30’ natural cavern; dusty stairs.

### 19. Abomination Nest
- **Exits:** W onto the east side of the Lake of Blood 20 (map).
- Narrow root-filled cave, half-eaten corpses. **2 abominations** → [[Abomination (Sakkara)]]: hp 19, 12; AC 4, HD 3+1**, 1d4/1d4/1d4 + paralysis, D4, ML +2, XP 135.
- On ten dead beastmen and humans: **750gp; 4 amber stones (100gp each); copper necklace with tiny bells (100gp); gold ring engraved "To Medoria – Eternal Love" (400gp).**

### 20. The Lake of Blood
- **Exits:** N into the Bloody Shore 16 (fluid continuous, map); narrow ledge along the west wall north toward 16 and to the tunnel west to 22 (fronds run all the way to 22, whose firelight is visible from here); E side to 19; S into the Pool of Blood 25 and Bloody Water 26; **shaft in the ceiling** above the 'tree': 50’ up and 30’ south (60°) to the floor of L1 42; a bloody canal east narrows to a trickle (extension point).
- Bean-shaped cavern ~80’ across, almost all birthing fluid: shallow by the west ledge, quickly 5’ deep. Roof 30’ up. A vast tumorous **'tree'** (intestine-coloured) in the centre; pink vein-like tendrils spread over the roof.
- **The large tree:** spoils the birthing pool if killed. Only axes, fire, magic weapons or spells harm it, and these always hit; **50 hp**. **100 XP to each character** for killing it. When attacked, **6 tendrils** drop from the roof → [[Blood Tree Tendril (Sakkara)]]: AC 3, HD 4, hp 5, 1d6, F4, ML n/a, XP —. They reach anywhere in the cavern and fight until the attackers leave, the tree dies or all tendrils are destroyed.
- **2 abominations** swim here and rise against anyone harming the tree; their tentacles reach the narrow beach → [[Abomination (Sakkara)]]: hp 19, 12.
- After **3 rounds** of fighting, **2 catechists** arrive from 22 (unless slain).
- Pool rules as in 16.

### 21. The Priests' Quarters
- **Exits:** S door to the passage east of 22 (map).
- 20’ × 20’; five couches (one upholstered, four straw), one-legged table. **Hidden in the upholstered couch lining: ruby (300gp), amethyst (75gp).** On the table a sack of legionary iron rations (two weeks) and a bottle of vinegary wine.

### 22. The Outer Fane
- **Exits:** W passage to room 1's south door and to 23; E passage to the Lake of Blood (21's door off it) (map).
- 40’ square, 10’ radius apses N and S each with a black marble statue of a dragon-winged pregnant woman (lore: Sakkara as Mother of Monsters). Lit by 10 wall torches (light visible from 20). Central altar of red-striated marble with silver runes and gold inlay. **Shadowed sinkhole of evil**: destroy the altar and bless or holy water to cleanse (Lawful characters **100 XP each**). Stripping its precious metal takes 3 turns, yields **2,000gp** of gold, and counts as destroying it.
- **Ur-Namu** → [[Ur-Namu (Sakkara)]]: Cleric 3; MV 60’, AC 7 (plate & shield), HD 3+3*, hp 14, D 1d6+1 (mace +1), C3, ML +2, AL C, XP 100; 2 1st-level spells; Battle Magic, Theology. Carries **35pp, 50gp**, iron draconic-eye holy symbol of Sakkara, **mace +1** (bronze flanged head, double-serpent haft).
- **4 catechists** → [[Catechist (Sakkara)]]: Cleric 1; AC 7, HD 1, hp 5, 4, 4, 3, D 1d6, C1, ML +2, XP 10.
- **Visitors escorted by a gnoll from 15** (printed "Black Fang gnolls from room 15", but 15 is the Red Eye cavern — Red Eye intended (inferred)) are greeted warmly and invited to pray at the altar while he casts **detect evil**. Pass: sent to the surface to **capture prisoners as a "gift"** to the Lady. Refuse or fail: attacked at once.
- **Tactics:** darkness on the most powerful-looking foe; three catechists charge; the fourth runs to warn Zakiti in 38 (reaches her in **9 rounds**). Disturbance heard in 20: two catechists sent after 3 rounds; if they do not return, one goes to warn Zakiti while Ur-Namu and the last guard the fane.

### 23. Guarded Door
- **Exits:** N to the rubble passage (toward 1 and 22); **SW door, wizard locked (caster level 3)**, to 24.
- **6 zombies** lurk round the sharp bend; attack anyone not wearing a prominent unholy symbol → [[Zombie]]: MV 60’, AC 1, HD 2*, hp 14, 12, 11, 11, 9, 5, D 1d8, F1, ML n/a, AL C, XP 29. (Zakiti gathers them if alerted.)

### 24. Guarded Passage
- **Exits:** NE door to 23 and SW door toward the Inner Fane 38; **both wizard locked (caster level 3)**.
- Narrow 5’ tunnel. **1 abomination** attacks any non-Chaotic creature that opens either door → [[Abomination (Sakkara)]]: hp 19 (printed "hp 19, 12" for one).

### 25. The Pool of Blood
- **Exits:** W into 36 (fluid a few inches deep); E into the Lake of Blood 20 (5’ deep); S toward 26 (map).
- Diamond-shaped cave ~40’ × 55’, vaulted 20’. A small foul **'tree'** (sapling) in the centre; tendrils spread to 36 and beyond. **30 hp**, harmed only by axes, fire, magic weapons or spells (which always hit); **3 tendrils** → [[Blood Tree Tendril (Sakkara)]]. Destroying it: **75 XP each**. No abominations present.

### 26. Bloody Water
- **Exits:** N/W to 25 and 20 (fluid); a 3’-5’ path around three sides; beach to the escape tunnel 27 (E); SW to 28 (map).
- Crescent ~100’ wide, ceiling ~15’, filled 5’ deep with birthing fluid. Otherwise empty.

### 27. Escape Tunnel
- **Exits:** W to 26's beach. Runs ~200’ to an apparent rock wall: **secret door** (search for secret doors) to the outside, far from the temple entrance. Only the Lady knows it; she flees this way with the Stone, wizard-locking the door behind her.

### 28. Ghoul Nest
- **Exits:** E: bars to 29; N toward 26; SW to 30 (map).
- Limestone cavern ~35’ across, ceiling 15’. **4 ghouls** in the NE corner, out of sight of the eastern (29) entrance. If they hear the party struggling with the bars in 29, they attack once the party is half in and half out → [[Grave Ghoul]]: MV 90’, AC 3, HD 2*, hp 14, 12, 9, 5, 1d3/1d3/1d3 + paralysis, F2, ML +1, AL C, XP 29.
- In their nest: **4 golden collars with silver serpent-head clasps (150gp each).**

### 29. Spiral Stair
- **Exits:** spiral stair up to L1 18; W cave mouth to 28 **blocked by iron bars**; a tail of cave south-east (map; dead end assumed).
- 30’ wide cave. The bars are mortared in, cannot be knocked aside, too thick to destroy readily. Very small or skinny creatures (unarmoured goblins, gnomes, ghouls) squeeze through automatically in one round. Unarmoured humans with **Contortionism**: proficiency throw per round. Other unarmoured characters need the bars bent: a full turn of effort then an **open doors throw at −8** (tools or contraptions may modify). Ghouls from 28 attack when about half the party is through.

### 30. Oozing Corridor
- **Exits:** NE to 28; W to 31; N toward 33 (map).
- Damp tunnel; a **grey ooze** blends into the floor: **−2 to surprise** unless the party prods the floor → [[Grey Goo]] (ACKS II grey ooze): MV 10’, AC 2, HD 3, hp 14, 2d8, F2, ML n/a, AL C (printed), XP 65.

### 31. Slime Chamber
- **Exits:** E to 30; N to 32; the far tunnel leads to an impassable cave-in after 60’ (extension point).
- Floor and roof covered in algae, fungus, mold hiding **3 green slimes** (−2 to surprise) → [[Sage Slime]]: hp 11, 10, 8; HD 2**, special, F1, ML n/a, AL N, XP 38 each.

### 32. Organic Chamber
- **Exits:** S to 31; N toward 35 (map).
- 70’ × 20’ tunnel whose walls are turning into fleshy fronds (as in 20), pulsing with fluids; no central growth yet. The fronds can be burned in one turn without incident.

### 33. Chitin Walls
- **Exits:** to 30 (S) and 34 (N) (map).
- Bean-shaped cavern; barnacle-like chitin shells on the walls, occasionally moving. Harmless; destroyed with axe or sword in one turn.

### 34. Skeleton Chamber
- **Exits:** S to 33; N to the Inner Fane 38 (map).
- 30’ semicircular cavern with chitin shells. **12 skeletons** (bronze swords, round shields) at attention facing south-east; guard the Inner Fane; attack anyone not presenting an unholy symbol → [[Skeleton]]: MV 120’, AC 2, HD 1*, hp 5 each, D 1d6, F1, ML n/a, AL C, XP 13. **Sounds of battle here bring the Lady from 38 in 2 rounds.**

### 35. Zombie Chamber
- **Exits:** S toward 32; NE to the Inner Fane 38 (map).
- 40’ cavern, fleshy tendrils along all walls, pulsing. **8 zombies** stand motionless facing south-east; attack anyone not presenting an unholy symbol → [[Zombie]]: AC 1, HD 2*, hp 9 each, D 1d8, F1, ML n/a, XP 29. Battle here also alerts Zakiti.

### 36. Abominable Chamber
- **Exits:** E into the Pool of Blood 25; NW to 38; S to 37 (map).
- Pulsing tendrils from 25 coat the walls. **1 abomination** has shambled in → [[Abomination (Sakkara)]]: hp 12.

### 37. Bone Lair
- **Exits:** N to 36 (map; its south end is the bone heap).
- Rear filled with the broken, gnawed bones of hundreds of humans and beastmen, a heap ~20’ across, ~5’ high at the back wall. **Each character searching a turn: 2 in 6** to reveal one of: rotted pouch with **39gp**; **silver ring (50gp)**; **two gold teeth (1gp each)**; **27cp**; **wand of magic missiles, 13 charges** (smooth oak, brass ram's head; command word Ancient Zaharan for ram, **"udu"**). (Roll which in order of the list or at random — order not specified.)

### 38. The Inner Fane
- **Exits:** passages between the rock ribs to 24, 34, 35, 36, 39 (and possibly 9) (map).
- 70’ egg-shaped cavern, ceiling 25’. The **Stone of Sakkara** sits atop an **altar of bone** rising from a carved dais showing a great serpent eating its own tail; veins and fleshy roots knit the bones; ring of burning braziers; tendrils spread over the floor and up the roof.
- **1d3 naked prisoners** bound to the altar by the roots at any time; any still-missing PC family members are here awaiting sacrifice. The Lady uses them as hostages to demand surrender, and may charm one or two against their rescuers.
- **Blighted sinkhole of evil:** Chaotic casters of reversed divine or necromantic spells cast as 2 levels higher; **Lawful divine casters turn undead as if 4 levels lower**. Cleansing: destroy the Stone, smash the altar, then bless or holy water: Lawful characters **200 XP each**.
- **Zakiti, The Lady Below** spends most of her time here conducting sacrifices → [[Zakiti (Sakkara)]]: Zaharan Ruinguard 5; Str 15, Int 16, Wis 8, Dex 11, Con 13, Cha 14; MV 90’, AC 7 (plate +1), hp 24, 1 attack or spells, D 1d10+4 (great axe +1), Save F5 (+2 all saves), ML +2, AL C, XP 660; infravision 60’; immune to fear; +1 surprise and initiative; double damage with axes on a natural 20; Kin-Slaying +1 vs humans, elves, dwarves, gnomes; arcane strike (+1d6 per slot level after a hit); death healing (instead of cleave, 1d6 per slot level). **Spells as a 3rd level mage, 2 1st + 1 2nd per day:** charm person, choking grip, detect magic, protection from good; deathless minion, necromantic potence, wizard lock. Necromantic spells as 5th level mage; controls undead as a 3rd level cleric. Gear: plate +1, ring of fire resistance, great axe +1, 4 vials military oil, unholy symbol (serpent eating its tail).
- **Tactics:** warned by a catechist (22) or hearing battle in 34 or 35: casts **necromantic potence** on herself (+1d10+5 temporary hp, 5 hours), gathers remaining undead from 23, 34, 35, and moves to deal with the intruders. All minions defeated: **seizes the Stone and flees via the escape tunnel 27**, wizard-locking its secret door. In a fight: **charm person on the strongest fighter**, then melee with arcane strikes. At **½ hp** she offers surrender if the party seems willing, hinting (falsely) at a bounty for her alive; she knows her cult will free her later. If she expects death or the Stone's destruction, she fights to the death. Chaotic followers she leads personally get +1 morale; intelligent chaotic monsters −2 to save vs her charms; +2 to her reactions with them.
- **The Stone:** see [[AX1 Magic Items]] (20 hp now; needs STR 16+ with a heavy implement, or a magic weapon, to damage; damaging it summons every abomination within 2,000’ (100’ × 20 hp); destroying it: striker saves vs Death or becomes an abomination; all within 5’ save vs Death or gain a mutation; leaves three Fragments).

### 39. The Resting Chamber
- **Exits:** SW to 38; its NE end may open onto the west shore of the Lake of Blood (map, unclear).
- The Lady's bedchamber: well-made couch from the surface, three-legged table, purple-upholstered folding stool. **Locked chest** at the foot of the couch, **poison needle trap (save vs Poison or die)**: her **spellbook** (iron-bound, pages of flayed human skin: charm person, choking grip, detect magic, protection from good, deathless minion, necromantic potence, wizard lock); **1,500sp; 1,000gp; 200pp; 2 black sapphires (500gp each); black diamond (1,000gp)**; among the coins a freshly drafted, unsent **letter in Ancient Zaharan to a "Lord of Secrets"**, describing her discovery and use of the Stone and offering herself and its power to the Lord's "dark mission" (campaign hook).
