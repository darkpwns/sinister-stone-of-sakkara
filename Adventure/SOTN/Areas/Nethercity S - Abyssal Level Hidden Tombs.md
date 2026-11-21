---
type: dungeon-level
level: 4
hex: "18.05"
tags:
  - sakkara/secret
source: "SOTN pp. 125-127 (map pp. 23, 182-183)"
---

# Nethercity S — Abyssal Level Hidden Tombs

A sealed Abyssal Level crypt of about 2200 BE under the east wing of the Grand Chthonic Nave, reached only by a hidden trapdoor in G1a: a gallery and a servant tomb packed with Thrassian (lizardman) skeletons, and the tombs of a high priest of Iskara and a high priestess of Nasga, both now mummy cultists who wake as soon as the skeletons do and spend the fight preparing their doors. No blighted sinkhole is keyed here; the whole Nethercity is a shadowed sinkhole of evil ([[Nethercity Features]]). Unlit throughout. Hub [[SOTN Hub]].

Running: wandering 1d6 every 3 turns, 6+ → 2d10 on the Temple / Tomb column, `Tables/sotn-wandering-temple-tomb.yaml` (`level: 4`). Area rules: disturbing either stone slab door (S2, S3) wakes the S1 skeletons, entering S4 or opening S2/S3 wakes those of S4; the waking skeletons also wake both mummy cultists, who then cast their preparations while the party fights and forces the doors (see S2, S3).

## Layout
- **Entrance:** the hidden trapdoor under the broken tiles of **G1a** ([[Nethercity G - Grand Chthonic Temple]]; found by a proficiency throw to find secret doors, or automatically by smashing up the tiles, which triggers an immediate wandering throw). A stone ladder goes down into the north end of **S1**.
- **S1** (60’ gallery running south) has a stone slab door on each side: west to **S2**, east to **S3**. At its south end an archway opens into **S4**. No other exits.
- Neighbours: [[Nethercity R - Abyssal Level Southern Cave]] (R2) lies just west, [[Nethercity T - Sub-Abyssal Secret Alien Sepulcher]] and [[Nethercity F - Lower Level Central Complex]] (F14) just east; none connects.

## Encounters at a glance
| Where | Who | No. | Engine note |
| --- | --- | --- | --- |
| S1 | Lizardman skeletons | 56, 2d10 a round | [[Skeleton]] (lizardman) |
| S4 (joining S1 from round 2) | Lizardman skeletons | 64, 2d10 a round | [[Skeleton]] (lizardman) |
| S2 | Mummy cultist of Iskara | 1 | [[Mummy Cultist of Iskara (SOTN)]] (variant of [[Mummy]]) |
| S2 (summoned) | Greater hellhound | 1 | [[Greater Hellhound]] |
| S3 | Mummy cultist of Nasga | 1 | [[Mummy]] (variant, inline) |

## Factions
The two mummy cultists are rival Chthonic clergy in life, allies in death against intruders. Neither parleys with tomb robbers in its own tomb; the Iskaran's **chthonic hegemon** power gives him +2 to reactions with intelligent chaotic monsters (the [[Great Teacher (SOTN)]] in T2 would be his natural master). The Nasgan's **glamorous aura** gives her +2 to reaction throws to impress or intimidate; a total of 12+ leaves the subjects acting as if bewitched in her presence.

## Rooms (SOTN pp. 125-127)

### S1. Hidden Gallery (2200 BE)
- **Exits:** stone ladder up to the G1a trapdoor; stone slab doors west (S2) and east (S3); archway south to S4.
> [!player]
> A stone ladder leads down from the trapdoor into a gallery that runs 60’ south and ends in an archway onto a chamber beyond. A stone slab door faces you on each side, west and east. The floor is black marble; the walls are black marble flecked with white, pierced by scores of horizontal graves, each holding a reptilian skeleton with a curved bronze shortsword and a round bronze shield.
- **Graves:** 56 horizontal wall graves, 28 a side (seven columns of four), all holding lizardman skeletons; no grave goods listed.
- **Monster:** the skeletons start to animate the moment anyone disturbs either stone slab door (S2 or S3). Then **2d10 a round** climb out of the S1 graves, and from the second round on **another 2d10 a round** come up the gallery from the 64 graves of S4.
  - **56 lizardman skeletons** → [[Skeleton]] (non-human: HD as a living [[Lizardman]]): MV 120’, AC 3, HD 2+1*, hp 9 each, curved bronze shortsword 8+, D 1d6, F2, ML n/a, AL C, XP 47 each. Immune to enchantment, necrotic and poison. (SOTN prints AC 2, HD 2*, attack 9+, XP 29; Judge's call: the MM rules give the lizardman's 2+1 HD and +1 AC for the shield.)

### S2. Hidden Priest's Tomb (2200 BE)
- **Exits:** stone slab door east to S1.
> [!player]
> A tomb 15’ × 10’, walls lined with black marble flecked with white. Two superb mosaics on the north and south walls show a mighty elven priest ministering to a cheering crowd in a vast cave. On a low bronze-plated dais in the middle lies a bronze sarcophagus, partly gilded. Round it stand four white-and-gold statuettes, an alabaster tablet and a jewelled gold-and-ivory candelabrum full of incense sticks. Thousands of gold and silver coins lie scattered over the black marble floor among broken pottery and shrivelled organs.
- **Monster:** the occupant is a **mummy cultist of Iskara**, waking when the S1 skeletons animate. While the party fights the skeletons and forces his door he casts, in order: *summon fantastic creature* (Judge's call: no ACKS II equivalent; it brings **1 greater hellhound**), a blast [[Rune of Warding]] on the inside of his door (16 damage, 2 per caster level; Blast save for half; SOTN: glyph of warding), [[Shimmer]] (+2 AC and saves) and [[Energy Protection]] against fire (SOTN: resist fire).
  - **Mummy cultist of Iskara** → [[Mummy Cultist of Iskara (SOTN)]] (variant of [[Mummy]]): MV 60’, AC 6 (8 with shimmer), HD 8+1****, hp 37, touch 2+, D 1d12 extraordinary bludgeoning and necrotic + mummy rot, F8 (+2 dark blessing; +4 with shimmer), ML +4, AL C, XP 2,600 (ACKS II: MM mummy ** + 2 for class abilities; SOTN 2,100). Casts as an 8th-level [[Elven Cultist]] of Iskara (4 1st, 4 2nd, 3 3rd, 3 4th, 1 5th); controls undead as an 8th-level chaotic cleric. (SOTN prints touch 3+.)
  - **Summoned greater hellhound** → [[Greater Hellhound]]: MV 120’, AC 5, HD 7*, hp 32, bite 4+ D 2d6 extraordinary fire and piercing, or fire breath (one target within 15’, 7d6 extraordinary fire, Blast save for half), F7, ML +1, AL C, XP 790. Discerns invisible within 60’; immune to fire. (SOTN prints HD 5, AC 7, bite 1d6.)
- **Loot:** bronze sarcophagus, partly gilded (1,500gp, 20 st.); 4 chryselephantine statuettes of elven kings and priests (700gp, 2/6 st. each); alabaster tablet with Chthonic prayers in Ancient Argollëan (1,000gp, 1 st.); gold candelabrum inset with ivory and white topaz (4,250gp, 1 st.) holding 20 sticks of myrrh (25gp each); 2,000gp and 10,000sp loose (3,000gp, 12 st.). Tally: 13,050gp, 35 2/6 st.
- **Lore:** Loremastery or Theology throw: the mosaics show the rites of Iskara, the Demon Queen, Chthonic goddess of chaos.

### S3. Hidden Priestess's Tomb (2200 BE)
- **Exits:** stone slab door west to S1.
> [!player]
> A tomb 15’ × 10’ panelled in purple marble whorled with black. Exquisite mosaics on the north and south walls show a voluptuous elven priestess leading rites of pleasure and excess. On a low bronze-plated dais in the middle stands a partly gilded bronze sarcophagus. Among heaps of broken pottery about ten red-figure terracotta urns lie toppled, spilling thousands of silver coins over the black marble floor; a set of canopic jars lies smashed, the preserved organs showing. Still whole, on the far side of the sarcophagus: a large bronze scroll jar and a closed cedar chest.
- **Monster:** the occupant is a **mummy cultist of Nasga** wearing a gold death's-head funeral mask with jet eyes, waking when the S1 skeletons animate. While the party fights and forces her door she casts a blast [[Rune of Warding]] on the inside of her door (16 damage, Blast save for half), [[Shimmer]] and [[Energy Protection]] against fire; she keeps her 5th-level slot for [[Fiery Pillar]] (SOTN: flame strike; 6d8 extraordinary luminous and fire in a 10’ pillar, Blast save for half) on the intruders.
  - **Mummy cultist of Nasga** (variant of [[Mummy]], inline): Wis 13, Cha 13; MV 60’, AC 6 (8 with shimmer), HD 8+1****, hp 34, touch 2+, D 1d12 extraordinary bludgeoning and necrotic + mummy rot, F8 (+2 with shimmer), ML +4, AL C, XP 2,600 (ACKS II: MM mummy ** + 2 for class abilities; SOTN 2,100). Horrific visage, mummy rot and damage immunities as [[Mummy]]. Casts as an 8th-level [[Elven Cultist]] of Nasga (4 1st, 4 2nd, 3 3rd, 3 4th, 1 5th); controls undead as an 8th-level chaotic cleric. **Glamorous aura** (see Factions). **Mastery of charms and illusions:** her charm and illusion spells take effect as if cast at 10th level, and their targets save at −2. **Provoke passions:** 1 round stationary, one creature within 30’ that can see and hear her saves vs Spells or is provoked for 1d4+8 rounds (hostile: attacks her alone, heedless; unfriendly: harasses her; neutral: distracted; indifferent: friendly; friendly: acts as bewitched; attacking it makes it enraged). Proficiencies: Contemplation, Performance (dance), Quiet Magic, Seduction, Theology, Unflappable Casting. (SOTN prints touch 3+.)
- **Loot:** gold death's-head mask with jet eyes (1,000gp, 1/6 st.; on the mummy); bronze sarcophagus, partly gilded (1,500gp, 20 st.); cedar chest with 2,000ep, 1,000gp and 3 black opals (750gp each); 10 red-figure terracotta urns (10gp, 3/6 st. each) and 10,000sp spilled from them; large bronze scroll jar (25gp, 1 st.) holding 4 illuminated religious texts (675gp, 1/6 st. each). Tally: 10,575gp, 34 5/6 st. (SOTN's figures; the opals must be 750gp each to reach the total. The listed weights, urns included, add to 39 5/6 st.)
- **Lore:** Loremastery or Theology throw: the mosaics show the rites of Nasga, the Serpent, Chthonic goddess of beauty, pain and lust.
- **Lore:** the four texts are a set, the *Twelve Erotic Arts of Nasga*, in Ancient Argollëan. The Temple of Ianna bans the Twelve Arts as so pleasurable they debauch whoever practises them. Auran and dwarven historians have long argued whether the Zaharans or the Southern Argollëan elves devised them (SOTN's aside: the dwarves were right), so the books have value to scholars as well as to the prurient.

### S4. Hidden Servant Tomb (2200 BE)
- **Exits:** archway north to S1.
> [!player]
> Through the archway is a tomb 15’ wide and 20’ long, floored in black marble with white-flecked black marble walls like the gallery. Every wall is pierced by four columns of four horizontal graves, each holding a reptilian skeleton with a curved bronze shortsword and a round bronze shield.
- **Graves:** 64 horizontal wall graves, 16 a wall (four columns of four), all holding lizardman skeletons; no grave goods listed.
- **Monster:** these animate as soon as anyone opens either stone slab door (S2/S3) or enters S4: **2d10 a round** climb out (they reach S1 from the second round, see S1).
  - **64 lizardman skeletons** → [[Skeleton]]: as S1 (MV 120’, AC 3, HD 2+1*, hp 9 each, shortsword 8+, D 1d6, F2, ML n/a, AL C, XP 47 each; SOTN XP 29).

## Treasure and XP summary
| Room | Treasure (gp) | Weight (st.) | Magic | Monster XP |
| --- | --- | --- | --- | --- |
| S1 | — | — | — | 56 × 47 = 2,632 (SOTN 1,624) |
| S2 | 13,050 | 35 2/6 | — | 2,600 + hellhound 790 |
| S3 | 10,575 | 34 5/6 | — | 2,600 |
| S4 | — | — | — | 64 × 47 = 3,008 (SOTN 1,856) |
| **Area S** | **23,625** | **70 1/6** | none | **11,630** |
