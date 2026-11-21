---
type: dungeon-level
level: 4
hex: "18.05"
tags:
  - sakkara/secret
source: "SOTN pp. 112-114 (map pp. 23, 182-183)"
---

# Nethercity O — Sub-Abyssal Secret Tomb of the Hierophant

The last great tomb built in the Nethercity (**1700 BE**), on the **Sub-Abyssal** level, sealed off from everything else: no door, stair or tunnel leads into it. Its only way in is a **passwall** opened from the end of the alchemists' secret corridor **N13** when the electrum orb from N10 sits in the indentation over N13's grey archway ([[Nethercity N - Sub-Abyssal Alchemic Laboratory]]). Here lies **Orthanach**, the greatest elven hierophant of the Argollëan empire, servant of Dirgion and the first elf ever made a [[Mummy Lord|mummy lord]], with his lover **Saorya** (cultist of Nasga) and his bodyguard **Cassair** (warlord), waiting for the Awakening. Black-speckled grey marble walls, black marble floors throughout; no light; no blighted sinkhole. These are the module's strongest foes. Hub [[SOTN Hub]]; doors, slab-door waking, mummies and treasure conventions in [[Nethercity Features]]. Pages are printed pages.

**Orientation:** SOTN's text for O (as for P and Q) is written with its north where the printed map has west (the map of this corner is drawn turned a quarter); the directions below are the text's.

Running: Temple / Tomb column, `level: 4` — 1d6 every 3 turns, 6+ → 2d10 on `Tables/sotn-wandering-temple-tomb.yaml` (Judge's call: the tomb is sealed, so a wandering band can only come in through N13 while the passwall stands open; otherwise there is no one to wander in). **Trapping:** the passage lasts while the electrum orb is in N13's indentation **plus 3 turns** after it is taken out; anyone inside when it closes is walled in. Escape: [[Disintegration]] or [[Earth's Mire]] (SOTN disintegrate, rock to mud) on the barrier, or cutting through as a **50gp construction project** (up to **4** characters can work on it; [[Construction Cost, Rate, and Supervision]]). The secret way cannot be detected or opened without magic. **Alarm:** disturbing the slab door of O3 or O5 wakes the bronze guardians of O2 (see O2); disturbing O3's door wakes the three mummies (door rule, [[Nethercity Features#Doors (SOTN p. 11)]]).

## Layout
- **Entrance:** the passwall from **N13** ([[Nethercity N - Sub-Abyssal Alchemic Laboratory]]) opens in the east wall of the gallery **O1**. No other way in or out.
- **O1** runs north 60’ and south 30’ from the entrance; at each end it turns west: the north branch to the guardian chamber **O2**, the south branch to a stone slab door into the annex **O5**.
- On O1's west wall, halfway between the entrance and the north end, a stone slab door opens into the burial chamber **O3**; a heavy bronze door (glyphed) in O3's west wall leads to the treasury **O4**.
- Neighbours (no connection but the passwall): [[Nethercity M - Northern Caves]] lies above, the alchemists' laboratory [[Nethercity N - Sub-Abyssal Alchemic Laboratory]] beside it.

## Encounters at a glance
| Where | Who | No. | Engine note |
|---|---|---|---|
| O2 (to O1, O3, O5) | bronze animated statues of elven warriors | 4 | [[Bronze Animated Statue]] |
| O3 | Orthanach, mummy lord hierophant | 1 | [[Orthanach (SOTN)]] ([[Mummy Lord]] + [[Elven Hierophant]] 12) |
| O3 | Saorya ("Sorya"), mummy cultist of Nasga | 1 | [[Saorya (SOTN)]] ([[Mummy]] + [[Elven Cultist]] 9) |
| O3 | Cassair, mummy warlord | 1 | [[Cassair (SOTN)]] ([[Mummy]] + [[Elven Warlord]] 9) |

## Factions
- **Orthanach's court** (O3): the hierophant, his lover Saorya and his bodyguard Cassair, one household waiting for the Awakening; the bronze statues of O2 obey Orthanach (he can call them off). First reaction on waking is wrath, as for every mummy; a parley or a spared mummy uses `Tables/sotn-mummy-reaction.yaml` ([[Nethercity Features#Necromancy and the mummies (SOTN pp. 16-17)]]). Orthanach wants the Awakening and his tomb unrobbed; he may treat with mortals who serve Dirgion, bring news of the world above or offer him a way to act on it (Judge's call). Saorya follows Orthanach in everything; Cassair obeys Orthanach and dies for him.
- Orthanach's name is the password to O3's bronze door; it is written in the cult records of the Doom Temple sacristy **J14** ([[Nethercity J - Doom Temple of Dirgion]]).

## Rooms (SOTN pp. 112-114)

### O1. Secret Tomb Gallery (1700 BE)
- **Exits:** E the passwall to N13 (only while it stands open); N 60’ then W to O2; S 30’ then W to the slab door of O5; W wall (halfway between the entrance and the north end) stone slab door to O3.
- > [!player]
  > The wall gives way onto a gallery of grey marble flecked with black, floored in black marble. It runs 60’ to the north and 30’ to the south, turning west at both ends. Halfway along to the north, a stone slab tomb door is set in the west wall.
- Nothing else here. The bronze statues of O2 come down this gallery when they are woken (O2).

### O2. Secret Tomb Guardian Chamber (1700 BE)
- **Exits:** S/E back to the north end of O1 (map).
- > [!player]
  > A chamber 30’ wide and 40’ long. By the west wall, 24 bronze ossuary urns have fallen over and spilled bones and skulls across the floor. Two stone pedestals stand against the north wall and two against the south wall. *(If neither the O3 nor the O5 slab door has been disturbed yet:)* on each pedestal stands a bronze statue of an elven warrior in armour.
- **Monster:** the four statues are **bronze animated statues**. They wake when the slab door of **O3** or **O5** is disturbed, march south down the gallery and attack every intruder they meet, unless Orthanach orders otherwise. They reach **O3 3 rounds** after its door is disturbed and **O5 4 rounds** after its door is. Left alone, they stay on their pedestals.
  - **4 bronze animated statues** → [[Bronze Animated Statue]]: MV 20’ / 60’ (SOTN 30’), AC 6, HD 5*, hp 25, 23, 21, 20, bronze short sword 6+, D 5d4 extraordinary bludgeoning (MM slam; SOTN short sword 2d6), F5, ML n/a, AL N, XP 350 each (SOTN AC 5, HD 5**, XP 500). Immune to enchantment, necrotic, poisonous and mundane bludgeoning, piercing and slashing damage; resistant to extraordinary bludgeoning, piercing and slashing. **Weak point:** an action in lieu of attacking and a Searching throw (+4 with Craft (armorer) or Engineering; SOTN "identify as a secret door") finds it; aimed attacks at −4 then bypass its immunities and an unmodified 20 with a weapon destroys it. −2 to surprise rolls against them while they stand still.
- **Loot:** 24 bronze ossuary urns (25gp, 1 st each). **Tally: 600gp, 24 st.**

### O3. Secret Burial Chamber of the Hierophant (1700 BE)
- **Exits:** E stone slab door to O1; W heavy bronze door (inscribed, glyphed) to O4.
- > [!player]
  > Behind the slab door, a burial chamber 30’ by 30’, grey marble flecked with black, black marble floor. Three bronze-plated daises rise from the floor, each bearing a bronze sarcophagus plated with gold and inlaid with lapis lazuli. In the west wall stands a heavy bronze door with a line of Ancient Argollëan engraved on it.
- **Monster:** the three sarcophagi hold **Orthanach**, **Saorya** and **Cassair**. They begin to wake when the O1 slab door is first disturbed; how far along they are when the party gets in follows the door rule (1st attempt: stirring in their sarcophagi; 2nd: out of them; 3rd or later: ready, cannot be surprised, spells cast; [[Nethercity Features#Doors (SOTN p. 11)]]). **3 rounds** after the door is disturbed, the **4 bronze statues** of O2 arrive to back them.
  - **Orthanach, mummy lord hierophant** → [[Orthanach (SOTN)]], [[Mummy Lord]] with the class abilities of a 12th-level [[Elven Hierophant]]: INT 16, WIS 16; MV 40’ / 120’ (SOTN 120’), AC 9 (MM 8, bracers +1), HD 12******, hp 55, touch −1+ (HD 12; SOTN 1+), D 1d12 extraordinary bludgeoning and extraordinary necrotic + mummy rot, or by weapon +4, Save F12, ML +4, AL C, XP 6,600 (SOTN's six asterisks already count the MM mummy lord's four plus two for the class). Horrific visage; mummy rot; immunities and resistances by damage type as the MM mummy lord; insect escape at 0 hp and return (re-forms in **O5** in **1d10 days** unless his canopic shrine is taken out of the tomb; see O5); rebuked as a vampire. Spell-like: at will [[Remove Curse|bestow curse]] and [[Bewitch Humanoid]] (SOTN charm person); 1/day [[Summon Insect Plague]]; 1/week [[Summon Weather]]. Casts arcane spells 4/4/3/3/3/2 and divine spells 5/5/4/4/3 (12th level; death and necromancy as 14th, targets −2 on saves against his death spells: [[Black Lore of Zahar]]). Repertoire, proficiencies and gear on his note.
  - **Saorya, mummy cultist of Nasga** → [[Saorya (SOTN)]], [[Mummy]] with the class abilities of a 9th-level [[Elven Cultist]] of Nasga: WIS 18, CHA 16; MV 20’ / 60’ (SOTN 60’), AC 6, HD 9+1****, hp 41, touch 1+ (attacks as HD 10, as the MM's 5+1 mummy attacks as HD 6; SOTN 2+), D 1d12 extraordinary bludgeoning and extraordinary necrotic + mummy rot, Save F9, ML +4, AL C, XP 3,100 (SOTN 9+1***, XP 2,500; coordinator's ruling: class abilities count as two more asterisks than the plain mummy's 5+1**). Glamorous aura, mastery of charms and illusions (casts them as 11th level; targets −2 on saves), provoke passions; commands undead as a 9th-level Chaotic caster. Spells 4/4/4/3/3. Details on her note.
  - **Cassair, mummy warlord** → [[Cassair (SOTN)]], [[Mummy]] with the class abilities of a 9th-level [[Elven Warlord]]: STR 17; MV 20’ / 60’ (SOTN 60’), AC 12 (mummy 6 + lamellar +1), HD 9+1****, hp 44, touch −1+ or sword +1 −2+ (SOTN 0+ / −1+), D 1d12+6 + mummy rot (touch) or 1d8+10 (sword, two-handed; no rot), Save F9, ML +4, AL C, XP 3,100 (SOTN 9+1**, XP 1,900; same ruling). Inspire courage 4/day; warlord damage +4. Details on his note.
  - **Tactics (SOTN):** given time, **Orthanach** casts [[Sphere of Invulnerability, Greater]] (globe of invulnerability), [[Giant Strength]] on Cassair (SOTN: doubles his damage dice; ACKS II: +2 to melee attack throws and an extra set of damage dice: 2d12+6 touch, 2d8+10 sword), [[Illusory Duplicates]] (mirror image) and [[Energy Protection]] against fire (resist fire); he opens the fight with [[Circle of Agony]] on up to five intruders of fewer than 9 HD (Death save, −2 from Black Lore). **Saorya**, given time, casts *prayer* (SOTN: allies +1 to attack, damage and saves, enemies −1; Judge's call: no exact ACKS II spell, run as SOTN describes, or substitute [[Holy Blessing]]), then [[Energy Protection]] against fire on herself, then on Cassair. **Cassair** inspires courage and holds the door between the party and his master. Orthanach then uses the [[Rod of Elemental Spheres]] and his spells; the statues pile in from round 3.
  - (Judge's call: the book gives none of the three any [[Sepulchral Worm|sepulchral worms]], although the MM gives a Dirgion-worshipping mummy lord 90%: none.)
- **Loot (on the mummies):**
  - *Orthanach:* gold death's-head funerary mask with black sapphire eyes (**2,675gp, 1/6 st**); obsidian ring etched with runes = **ring of fire resistance** → [[Ring of Fire Protection]] (apparent value 2,000gp); bronze bracers inlaid with lapis lazuli = **bracers of protection +1** → [[Bracers of Armor]] +1 (Judge's call; apparent value 225gp); the **rod of elemental spheres** → [[Rod of Elemental Spheres]], [[SOTN Magic Items#Rod of Elemental Spheres]] (SOTN p. 134: its four powers usable 4 times a day in all; the ACKS II rod: each power once a day).
  - *Saorya:* silver crown framed by rearing serpents with jet eyes (**3,000gp**); ebony staff topped by a bronze cobra = *staff of the serpent* (apparent value 100gp). Not a SOTN item: the standard ACKS I staff, with no ACKS II counterpart. Judge's call: run it as a **staff +1** (divine casters) that, on a hit and a command word, turns into a serpent and coils around a man-sized or smaller victim, holding it helpless for **1d4 turns** unless it saves vs **Spells**, then turns back into a staff (the classic snake staff, from memory: check the ACKS I book). Nearest ACKS II item by effect: [[Staff of Halting]] (staff +1 that paralyses, by charges).
  - *Cassair:* bronze lamellar = **lamellar armour +1** (apparent value 700gp); gilded boar's-tusk helmet with a roc-feather crest (**325gp, 1/6 st**); curved meteorite-iron sword with a screaming-skull hilt = **sword +1** (apparent value 650gp). (Judge's call: by its description this is the **sword of the deathless warlord**, [[SOTN Magic Items#Sword of the Deathless Warlord]] = [[Sword +1, Deathless]]: three times a day, when it kills a living creature, its wielder may raise it as a [[Deathless Minion|deathless minion]] in lieu of cleaving.)
- **Loot (the room):** three gold-plated sarcophagi inlaid with lapis lazuli (**6,000gp, 20 st each**). (SOTN prints "four" sarcophagi, but the room has three and its total counts three.) **Tally: 24,000gp, 60 2/6 st** (3 sarcophagi 18,000gp, mask, crown, helmet; magic excluded).
- **Lore / Trap (bronze door to O4):** read in Ancient Argollëan: "Enter in the Name of the Hierophant." A **blast rune** ([[Rune of Warding]], SOTN glyph of warding) fires when any creature touches the door without speaking the name **"Orthanach"**: **24 electrical damage** (Blast save for **12**) to everyone within **10’** of the door. The door radiates magic; a Searching throw spots the almost invisible tracery of the rune in the bronze fretwork. Cast at **12th level** (for [[Dispel Magic]]). The name is in the J14 scrolls. Forcing the heavy bronze door: −4 ([[Nethercity Features#Doors (SOTN p. 11)]]).

### O4. Secret Tomb Treasury (1700 BE)
- **Exits:** E heavy bronze door to O3.
- > [!player]
  > A vault 25’ by 20’ of black and grey marble, crowded with treasure. In the middle stands an ebony altar inlaid with gold; on it lies a long black scroll wound on golden handles, and under it are tucked golden bowls and cups. Before the altar sits a box of red and black wood. On the floor lie a toppled ebony statuette of a coiled cobra, an ivory statuette of a skull with ebony tentacles, and an ornate alabaster lamp with gold fittings. Four cedar chests stand against the walls.
- **Loot:**
  - 4 cedar chests, **locked**, **2,000gp** each (8,000gp, 8 st).
  - Dawn redwood and ebony box (**25gp, 1/6 st**) holding 12 engraved moonstones (**100gp each**), a gold pendant inlaid with black sapphire and ruby (**3,000gp**) and a dagger of pure gold inlaid with onyx (**850gp, 1/6 st**).
  - Ebony altar (**700gp, 3 st**); under it a gold libation bowl (**425gp, 1/6 st**), 3 gold cups (**100gp each**), a gold incense dish (**100gp**) and its matching gold basin (**2,500gp, 1 st**).
  - The long scroll: **the hierophant's spellbook** ([[SOTN Magic Items#Hierophant's Spellbook]], SOTN p. 138: black-dyed vellum, gold script, golden handles tipped with black sapphires; 25,900gp, **3/6 st**). It holds Orthanach's whole arcane repertoire (see [[Orthanach (SOTN)]]).
  - Ebony cobra statuette (**1,000gp, 2/6 st**); ivory skull statuette (**1,000gp, 2/6 st**); alabaster lamp (**1,000gp, 2/6 st**).
  - **Tally: 20,100gp, 14 st** (spellbook weight included, its value excluded).
- **Lore:** Loremastery or Theology throw: the cobra is **Nasga**, the tentacled skull is **Dirgion**.

### O5. Secret Tomb Annex (1700 BE)
- **Exits:** E stone slab door to the south branch of O1.
- > [!player]
  > The slab rolls aside on an annex 20’ by 15’ of black and grey marble, filled wall to wall by three canopic shrines of gilded wood: one decorated with golden skulls, one with golden serpents, one with golden swords.
- **Monster:** none here, but **4 rounds** after the slab door is disturbed the **4 bronze statues** of O2 arrive to deal with intruders.
- **Orthanach's return:** destroyed, he **re-forms here in 1d10 days** unless his canopic shrine (the golden skulls) is removed (SOTN; the MM mummy lord re-forms in 1d10 nights, and his return is also blocked if the tomb is magically sealed against insects; destroying his canopic jars before he falls, or while his spirit is in them, destroys him for good: [[Mummy Lord]]).
- **Trap:** Orthanach's shrine (golden skulls) carries a **spell rune** ([[Rune of Warding]], SOTN glyph of warding) holding **finger of death** ([[Restore Life and Limb|extinguish life]]): any creature but the mummy lord who touches the shrine saves vs **Death** or dies. The shrine radiates magic; a Searching throw spots the tracery on the skulls. Cast at **12th level** (for [[Dispel Magic]]).
- **Loot:** 3 canopic shrines (**2,000gp, 7 st each**), each holding 4 terracotta canopic jars of embalmed organs (**25gp, 1/6 st each**). Orthanach's shrine also holds a **large soul gem** charged with **5,000 divine power** ([[SOTN Magic Items#Soul Gem]], SOTN p. 135; its power pays for magic research components point for point, casts a spell from its holder's repertoire without a slot at 50/100/150/225/300/400 divine power for spell levels 1-6, casts healing on himself the same way, and lets him use [[Speak with Dead]] free on any soul inside it; it is fragile, and destroying it frees its power and drains whoever holds it of 10% of his XP unless he saves vs Death). **Tally: 6,300gp, 24 st** (SOTN; the shrines and jars come to 23 st: Judge's call, the gem is the last stone; magic excluded).
- **Lore:** the soul gem holds the spiritual residue of **Caogan**, an elven wizard and Orthanach's old rival, in his day the master of the **Oculus of the Dread Eye**, a sinister artifact the elves inherited from the khepri. Speaking with him (speak with dead through the gem) can reveal where the **Eyrie of the Dread Eye** lies (the AX5 adventure; Judge's placement) and answer questions about the Argollëan empire and the Nethercity around 1700 BE (Judge's discretion as to what he knows). Judge's call for playing him: proud, bitter at his long captivity, glad of any chance to spite Orthanach; he speaks Ancient Argollëan only, in clipped, scornful sentences.

## Treasure and XP summary
| Room | Treasure | Weight |
|---|---|---|
| O2 | 24 bronze urns, 600gp | 24 st |
| O3 | 3 sarcophagi, mask, crown, helmet: 24,000gp | 60 2/6 st |
| O4 | coin, gems, gold plate, altar, statuettes: 20,100gp | 14 st |
| O5 | 3 canopic shrines and 12 jars: 6,300gp | 24 st |
| **Total** | **51,000gp** (magic excluded) | **122 2/6 st** |

SOTN gives no area total; this is the sum of its room tallies.

**Magic:** [[Ring of Fire Protection]] (ring of fire resistance, O3); [[Bracers of Armor]] +1 (bracers of protection +1, O3); [[Rod of Elemental Spheres]] / [[SOTN Magic Items#Rod of Elemental Spheres]] (O3, 40,000gp); *staff of the serpent* (O3; ACKS I item, Judge's call: as a staff +1 that coils and holds a victim 1d4 turns, Spells save; nearest ACKS II [[Staff of Halting]]); lamellar armour +1 (O3); sword +1 = [[SOTN Magic Items#Sword of the Deathless Warlord]] / [[Sword +1, Deathless]] (O3, 17,000gp); [[SOTN Magic Items#Hierophant's Spellbook]] (O4, 25,900gp); large [[SOTN Magic Items#Soul Gem]] with 5,000 divine power (O5).

**Monster XP:** O2/O3 bronze statues 4 × 350 = 1,400 (SOTN 2,000); Orthanach 6,600; Saorya 3,100 (SOTN 2,500); Cassair 3,100 (SOTN 1,900). **Total 14,200** (SOTN's statlines 13,000).
