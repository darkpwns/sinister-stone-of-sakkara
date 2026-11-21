---
type: custom-class
tags: [sakkara/secret]
source: "JJ ch. 12 custom class build of the ACKS I Elven Cultist (SOTN pp. 162-166)"
build: "HD 0, Fighting 0, Thievery 1, Divine 3, Elf 0"
xp_2nd: 1375
level_limit: 13
saves_as: crusader
key_attributes: "WIL"
requirements: "INT 9, Chaotic"
hit_dice: "1d4"
builds_file: "Adventure/SOTN/Classes/sotn-class-builds.yaml"
---

# Elven Cultist

Up: [[SOTN Hub]] · Builder: [[JJ 12 Custom Classes]], [[Creating a Custom Class]] · Build record: `Classes/sotn-class-builds.yaml` (`Elven Cultist`) · See also [[Nethercity History]], [[Nethercity Features]]

## Concept and role
The priest-sacrificer of the Chthonic gods who taught the elves of Southern Argollë to fear death and crave the immortality of the flesh (3000-1650 BE). A frail divine caster with more spells per day than a crusader, control of the undead, and three powers granted by his god (Bel, Dirgion, Iskara, Nasga or Telith). Whether any survive in the Ammas Aurë is unknown; Rornish tales speak of dark elves stealing children for cave sacrifices (SOTN p. 162).
- **Nearest RR class:** the [[Crusader]] of a chaotic sect (controls undead instead of rebuking, same divine magic research). It does not suffice: the cultist has d4 Hit Dice, a mage's fighting and no armour, a 133% spell progression with a list of 12 spells per level instead of 10, the elf powers, and cult powers by deity. The [[Priestess]] (Divine 4) casts more but has no undead control and no cults.

## Build (JJ ch. 12, Custom Racial Classes)
- **Build points:** HD 0, Fighting 0, Thievery 1, Divine 3, Arcane 0 = 4, plus Elf 0 = **4 build points → 13th level limit** (SOTN 13th) ([[Custom Racial Classes]]).
- **Requirements:** INT 9+ (elven classes); must be Chaotic (SOTN).
- **Hit Dice 0** ([[Hit Dice Value]]): d4, Mortal Wounds +0; +1 to the HD roll at 1st level (Connection to Nature); +1 hp per level after 9th (crusader progression). 0 XP.
- **Fighting 0 (Mage)** ([[Fighting Value]]): attack throws +2 per 6 levels, no cleaves. Restricted weapons: **dagger, sling, staff, whip** (SOTN's four). No armour, so no weapon and shield. The one optional style (dual or two-handed) is **eliminated for 1 custom power** (SOTN: "not trained to … fight two-handed, or dual wield"); a staff is used one-handed for 1d4. 0 XP.
- **Thievery 1** ([[Thievery Value]]): 4 selections, all traded for custom powers. 250 XP.
- **Divine 3** ([[Divine Value]]): rebuke undead, cast spells and research as a crusader with spells per level +33% ("more spells per day than a Lawful or Neutral cleric", SOTN); list of 12 spells per level. Rebuking takes the chaotic **control undead** form ([[Crusader#Rebuking Undead]]). 1,000 XP.
- **Arcane 0.** **Elf 0:** the four elf powers (below). 125 XP ([[Elven Custom Classes]]).
- **Code of behaviour (Divine 3, monastic-strict; Judge's call from SOTN's text):** blood sacrifice to the god at the cult's holy days; service of the Chthonic faith and its promise of bodily immortality; obedience to the cult hierarchy; preservation of the dead for the Awakening (no destroying the entombed faithful). Breaking it loses spells and control undead as a crusader's code does.
- **Custom powers (5):** the god's three cult powers + **Divine Health** + **Sensing Good** (the last two Judge's calls: SOTN names only the three cult powers; ACKS II's fighting style trade-off gives one power SOTN's build lacked, and the fourth Thievery selection is unaccounted for). Starting general proficiency power: **Theology** (as the crusader).
- **Drawbacks:** none (the corruption powers below cancel out).
- **Saving throws** ([[Saving Throw Progression (Custom Classes)]]): Divine 3 highest → **crusader**, with Connection to Nature's +1 on Paralysis and Spells. Identical to SOTN's table.
- **Magic items:** crusader items; enchanted daggers, slings, staffs, whips.
- **Key attribute:** **WIL** (crusader; SOTN WIS).
- **Proficiencies:** 42 − 13 = 29 on the class list. Crusader progression: class proficiency at 1st, 4th, 8th, 12th; general at 1st, 5th, 9th, 13th.
- **Stronghold** ([[Strongholds and Followers]]): qualifies for Cloister (Divine 3), Fortified Church (Divine 2) or Hideout (Thievery 1); takes **Cloister**, renamed **Fane of Chaos** (SOTN's fane followers are the cloister's).
- **XP** ([[Experience Points per Level]]): 0 + 0 + 250 + 1,000 + 125 = **1,375 XP for 2nd level** (SOTN 1,325); doubled to 8th (7th 44,000 rounded to 45,000); then +100,000 (crusader) + 50,000 (elf) = **+150,000 per level after 8th**.

## Class table
From `acks/custom_class.py` with this build (Elf 0 cost as `extra_costs`; elven +50,000 XP after 8th and Connection to Nature added by the JJ rules). Spells per day: JJ Divine 3 progression (133%). Row 14 only for a corrupt elf become intelligent undead (ψ, below).

| Level | Title | XP | Hit Dice | Attack | Paralysis | Death | Blast | Implements | Spells | Spells/day (1st-6th) | Caster Level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Chthonic Initiate | 0 | 1d4+1 | 10+ | 12+ | 10+ | 16+ | 13+ | 14+ | 1 | 1 |
| 2 | Chthonic Acolyte | 1,375 | 2d4 | 10+ | 12+ | 10+ | 16+ | 13+ | 14+ | 3 | 2 |
| 3 | Chthonic Cultist | 2,750 | 3d4 | 10+ | 11+ | 9+ | 15+ | 12+ | 13+ | 3/1 | 3 |
| 4 | Chthonic Curate | 5,500 | 4d4 | 9+ | 11+ | 9+ | 15+ | 12+ | 13+ | 3/3 | 4 |
| 5 | Chthonic Vicar | 11,000 | 5d4 | 9+ | 10+ | 8+ | 14+ | 11+ | 12+ | 3/3/1 | 5 |
| 6 | Chthonic Rector | 22,000 | 6d4 | 9+ | 10+ | 8+ | 14+ | 11+ | 12+ | 3/3/3 | 6 |
| 7 | Chthonic Prelate | 45,000 | 7d4 | 8+ | 9+ | 7+ | 13+ | 10+ | 11+ | 4/3/3/1 | 7 |
| 8 | Chthonic Bishop | 90,000 | 8d4 | 8+ | 9+ | 7+ | 13+ | 10+ | 11+ | 4/4/3/3 | 8 |
| 9 | Cult Leader | 240,000 | 9d4 | 8+ | 8+ | 6+ | 12+ | 9+ | 10+ | 4/4/4/3/1 | 9 |
| 10 | Cult Leader, 10th level | 390,000 | 9d4+1\* | 7+ | 8+ | 6+ | 12+ | 9+ | 10+ | 4/4/4/4/3 | 10 |
| 11 | Cult Leader, 11th level | 540,000 | 9d4+2\* | 7+ | 7+ | 5+ | 11+ | 8+ | 9+ | 5/4/4/4/3/1 | 11 |
| 12 | Cult Leader, 12th level | 690,000 | 9d4+3\* | 7+ | 7+ | 5+ | 11+ | 8+ | 9+ | 5/5/4/4/4/3 | 12 |
| 13 | Cult Leader, 13th level | 840,000 | 9d4+4\* | 6+ | 6+ | 4+ | 10+ | 7+ | 8+ | 5/5/5/4/4/3 | 13 |
| 14 | Cult Leader, 14th level ψ | special ψ | as undead ψ | 6+ | 6+ | 4+ | 10+ | 7+ | 8+ | 5/5/5/5/4/4 | 14 |

\* No CON adjustment to this flat bonus. Iskara's Dark Blessing adds +2 to every save; WIL modifies all saves.

## Class powers
**Starting (1st level)**
- **Divine Magic:** prayerful repertoire = the cultist list plus his god's spells (below), at the levels he can cast; knows both forms of each reversible spell ([[Spell Repertoires]]).
- **Control Undead:** as a chaotic crusader of his level ([[Crusader#Rebuking Undead]]): controlled 1 turn per level, or 1 day per level where the undead would have been destroyed; bewitched (undead constructs as if he made them); dispelled if a crusader rebukes them; flee as if rebuked when it ends. Dirgion lengthens it (Lordship Over the Undead).
- **Cult powers** (three, by god; [[Custom Power Index]] names, SOTN names in brackets):

| God (sobriquet; sphere) | Powers |
| --- | --- |
| **Bel** (Slaughterprince; war, conquest, bloodshed) | [[Custom Power Index (A-B)#Battle Magic\|Battle Magic]] (+1 initiative when casting; spell attack throws on the fighter progression. SOTN: +2 levels to dispel or pierce magic resistance), [[Custom Power Index (H-L)#Inspire Courage\|Inspire Courage]] (1 round of oration, up to 30 allies in 50’ inspired 1 turn, once per day per level; SOTN: only Chthonic worshippers, +1 attack, damage, morale, saves v. fear), [[Custom Power Index (Q-S)#Savage Resilience\|Savage Resilience]] (supernatural resilience: roll twice on Mortal Wounds and choose; bed rest less his level in days) |
| **Dirgion** (Doombringer; doom, death, undeath) | [[Custom Power Index (Q-S)#Strength of Spirit\|Strength of Spirit]] (inexorable: immune to natural and magical fear), [[Custom Power Index (H-L)#Inspire Dread\|Inspire Dread]] (1 round, up to 30 foes in 50’ shaken 1 turn, Paralysis save resists, once per day per level; SOTN: save v. Spells, −1 attack, damage, morale, saves v. fear), [[Custom Power Index (H-L)#Lordship Over the Undead\|Lordship Over the Undead]] (control lasts 1 day per level; a "D" result controls indefinitely) |
| **Iskara** (Demon Queen; chaos, darkness, eternity) | [[Custom Power Index (A-B)#Ancient Pacts\|Ancient Pacts]] (chthonic hegemon: +1 reactions with intelligent chaotic monsters, which take −2 on saves v. his enchantments; SOTN +2 and "charm spells"), [[Custom Power Index (C-D)#Divine Blessing\|Divine Blessing]] (dark blessing: +2 all saves), [[Custom Power Index (T-Z)#Utter Domination\|Utter Domination]] (henchmen base morale +4, no loyalty rolls on calamities; not mercenaries) |
| **Nasga** (Serpent; beauty, pain, lust) | [[Custom Power Index (E-G)#Glamorous Aura\|Glamorous Aura]] (+1 reactions to impress and intimidate, 12+ = bewitched in his presence; SOTN +2), [[Custom Power Index (M-P)#Mastery of Enchantments and Illusions\|Mastery of Enchantments and Illusions]] (mastery of charms & illusions: +2 caster levels, −2 on targets' saves, research bonuses), [[Custom Power Index (M-P)#Provoke the Passion\|Provoke the Passion]] (full round, target in 30’, Spells save; 1d4 rounds + 1 per level; reaction-dependent effect) |
| **Telith** (Great Earth Mother; earthquakes, volcanoes, wilderness) | [[Custom Power Index (A-B)#Awareness of the Earth\|Awareness of the Earth]] (1 turn, 11+: sinkholes, deadfalls, collapses, rock slides; land value and lairs as [[Land Surveying]]), [[Custom Power Index (E-G)#Elemental Connection\|Elemental Connection]] (earth: underground, regains a spent slot with 6 turns' meditation, 3 turns / 1 turn / 1 round in a minor / major / supreme [[Places of Elemental Power\|place of elemental earth]]; one slot per spell level per day), [[Custom Power Index (Q-S)#Solidity of Rock\|Solidity of Rock]] (+4 v. being grabbed, knocked down, restrained, wrestled or moved) |

- **Divine Health** (Judge's call): immune to all disease, magical included ([[Divine Health]]); the Chthonic promise of an incorruptible body.
- **Sensing Good** (Judge's call): senses good intentions, good enchantments and Lawful enchanted creatures within 45’ ([[Sensing Good]]).
- **Theology** (starting power, one rank).
- **Elf racial powers:** Animal Friendship, Attunement to Nature (+1 surprise in the wilderness; Adventuring search and listen 14+), Connection to Nature (immune to undead-caused disease, +1 Paralysis and Spells saves, +1 HD roll at 1st), Elf Tongues. (SOTN's ACKS I keen eyes and ghoul-paralysis immunity are replaced by these.) Elves of antiquity speak Ancient Argollëan; their four bonus languages are taken from Ancient Dwarven, Ancient Zaharan, Draconic, Khepri (Proto-Meniran) and Northern Meniran dialects instead of Elf, Gnoll, Hobgoblin, Orc (SOTN p. 162; Judge's call to apply it to Elf Tongues).

**Additional** (as the crusader)
- **Minor Magical Research (5th level):** scrolls and potions, spell research. **Major Magical Research (9th level):** weapons, rings, staffs. **Supreme Magical Research (11th level):** ritual divine spells, constructs; necromantic servants and undeath ([[Magic Research]], [[Performing Necromancy]]). (SOTN: ritual 6th-7th level at 11th; ACKS II casts 6th level normally from 11th.)
- **Fane of Chaos (9th level, Cloister):** 15,000gp+; draws **1d6 × 30 0th-level elven novices and 1d2 × 10 1st-level cultists** (SOTN's numbers, which match the RR priestess's cloister; the JJ custom table prints 1d20 × 10, Judge's call: use 1d2 × 10). Each year 80% of the novices go mad, kill themselves or flee and 1d6 × 20 replace them; training takes 2 years. Within six months the fane becomes a **shadowed** [[Sinkholes of Evil|sinkhole of evil]] and stays one, even if abandoned, until cleansed (SOTN p. 165).

**Class proficiency list (29):** [[Alchemy]], [[Syncretism]] (SOTN apostasy), [[Arcane Dabbling]], [[Battle Magic]], [[Black Lore of Zahar]], [[Contemplation]], [[Diplomacy]], [[Divine Blessing]], [[Divine Health]], [[Familiar]], [[Illusion Resistance]], [[Knowledge]], [[Laying on Hands]], [[Loremastery]], [[Magical Engineering]], [[Magical Music]], [[Mystic Aura]], [[Naturalism]], [[Performance]], [[Prestidigitation]], [[Profession]], [[Prophecy]], [[Quiet Magic]], [[Righteous Rebuke]] (SOTN righteous turning), [[Seduction]], [[Sensing Good]], [[Sensing Power]], [[Theology]], [[Unflappable Casting]].

**Template (SOTN p. 166): Sacrificer** (a cultist of Dirgion). Proficiencies: [[Black Lore of Zahar]], [[Theology]] (a second rank, the first being the class power). Equipment: curved dagger, black cassock, black leather backpack, 10 black wax candles, unholy symbol, prayer book, 1 week's iron rations, tinderbox, wineskin. INT 13+ adds bonus general proficiencies.

## Spell list
Divine 3: 12 spells per level, the cultist list (10) plus 2 of his god. ACKS II names by effect; each spell sits at its **ACKS II divine level** (SOTN's level noted where different). \* reversible (both forms known); † an ACKS II arcane-only spell granted to the cult at SOTN's divine level (Judge's call); *italics* = no ACKS II equivalent (Judge's call: keep SOTN's name, run it from the ACKS I text or swap it). Fill-ins marked "JC" replace spells lost to conversion so each level holds 10 (Judge's call).

| Level | Cultist list (common) |
| --- | --- |
| 1st | [[Remove Fear]]\* (cause fear), [[Cure Light Injury]]\* (cause light wounds), [[Illumination]]\* (darkness), [[Discern Evil]]\* (detect evil), [[Discern Magic]], *Faerie Fire*, [[Predict Weather]], [[Holy Circle]]\* (protection from good), [[Purify Food and Water]]\* (putrefy), [[Counterspell]] (JC) |
| 2nd | [[Augury]], [[Holy Blessing]]\* (bane), [[Cure Moderate Injury]]\*, [[Choking Grip]], *Enthrall* (nearest [[Beguile Humanoid]]), [[Halt Humanoids]] (hold person), [[Holy Chant]], [[Energy Protection]] (resist fire; resist cold, SOTN 1st), [[Noiselessness]] (silence 15’ radius), [[Spiritual Weapon]] |
| 3rd | [[Remove Curse]]\* (bestow curse), [[Cure Major Injury]]\*, [[Bewitch Humanoid]] (charm person), [[Cure Blindness]]\* (cause blindness), [[Cure Disease]]\* (cause disease), [[Illumination, Perpetual]]\* (continual darkness), *Feign Death*, [[Rune of Warding]] (glyph of warding), [[Holy Prayer]] (prayer), [[Speak with Dead]], [[Dispel Magic]] (SOTN 4th), [[Holy Circle, Sustained]]\* (SOTN 4th). (12: two spells SOTN puts at 4th are 3rd level in ACKS II; Judge's call to keep both.) |
| 4th | [[Smite Undead]]\* (as [[Animate Undead]]: animate dead), [[Cure Serious Injury]]\*, [[Death Ward]], [[Divination]], [[Indiscernibility]] (nondetection), [[Neutralize Poison]]\* (poison), [[Tongues]], [[Repair Disfigurement and Disability]]\* (JC), [[Lightless Vision]] (JC), [[Spellward Other]] (JC) |
| 5th | [[Cure Critical Injury]]\*, *Command Person* (nearest [[Dominate Humanoid]], Arcane 2), [[Communion]] (commune), [[Fiery Pillar]] (flame strike), [[Restore Life and Limb]]\* (as extinguish life: finger of death), [[Summon Insect Plague]], [[Scry]], [[True Seeing]], [[Fate]] (SOTN 4th), [[Turn to Dust]] (JC) |
| 6th | [[Quest]] (SOTN 5th), [[Torpor]] (SOTN 5th), and JC: [[Dispel Evil]]\* (dispel good), [[Flesh to Ash]], [[Fillet and Serve]], [[Slumber, Deep]], [[Hidden Host]], [[Anti-Magic Sphere]], [[Home Ward]], [[Prophetic Dream]] |

| God | Bonus spells (ACKS II level) |
| --- | --- |
| Bel | 1st [[Bane-Rune]], [[Sharpness]]†; 2nd [[Righteous Wrath]], *Summon Berserkers*; 3rd [[Deflect Ordinary Missiles]] (protection from normal missiles), [[Striking]]; 4th [[Dismember]]; 5th [[Vigor]] (SOTN 4th), [[Cone of Fear]] (fear), [[Deflect Ordinary Weapons]] (protection from normal weapons) |
| Dirgion | 1st [[Destroy Dead]], [[Unliving Puppet]]; 2nd [[Deathless Minion]], [[Necromantic Potence]]; 3rd *Enervate*, [[Strengthen the Unliving]]; 4th *Control Undead*, [[Shrieking Skull]]†; 5th [[SOTN Spells#Preservation of Antiquity]], [[Summon Shadow]]† (summon shadows) |
| Iskara | 1st [[Angelic Choir]], [[Word of Command]] (command word); 2nd [[Divine Grace]], [[SOTN Spells#Display of Power]]; 3rd [[Discern Curse]]\* (as indiscernible curse: undetectable curse), [[Winged Flight]]; 4th [[Halt Monsters]]† (hold monster), [[Inspire Awe]]\* (as inspire horror); 5th *Summon Fantastic Creature*; 6th [[Bewitch Monster]] (charm monster, SOTN 5th) |
| Nasga | 1st [[Angelic Choir]], [[Allure]] (fellowship, Judge's call by effect); 2nd [[Shimmer]], [[Bewitch Beast]] (snake charm, Judge's call: any animal), [[Dark Whisper]] (SOTN 4th); 3rd [[Adjust Self]]† (alter self), [[Phantasmal Figment]] (Judge's call: SOTN repeats charm person, already on the common list); 4th [[Snakes to Staffs]]\* (as staffs to snakes: sticks to snakes); 5th [[Guise Self]]; 6th [[Bath of the Goddess]] (SOTN 5th) |
| Telith | 1st [[Pass Without Trace]], [[Sling Stone]], [[Shatter Blade]] (SOTN 2nd); 2nd [[Earth's Excrescence]]†; 3rd [[Create Chasm]]† (earth's maw), [[Striking]]; 4th [[Battering Ram]], [[Speak with Plants]]; 5th [[Earth's Teeth]]† (fangs of the earth), [[SOTN Spells#Weave Stone]] |

## The corrupt elves of antiquity (SOTN p. 162)
By era, every elven class takes a variant of **After the Flesh** ([[Custom Power Index (A-B)#After the Flesh]]) paired with **Dark Soul** ([[Custom Drawbacks#Dark Soul]]); SOTN rules that the two cancel, so XP is unchanged (kept as a Judge's call; ACKS II prices them +1 and −1 power, the same result). Become intelligent undead, the elf keeps his racial powers and the share below of his HD and class abilities, then may advance in HD without limit and in class abilities to **14th level** regardless of the level limit. Restored to life, he takes the penalty on the 1d20 Tampering with Mortality roll ([[RR App C Wounds and Woe]]).

| Era | Corruption | Retained in undeath | Tampering with Mortality |
| --- | --- | --- | --- |
| before 2800 BE | none | nothing (a plain undead) | — |
| 2800-2500 BE | partial | ⅓ | −1 per 3 levels |
| 2500-2200 BE | moderate | ½ | −1 per 2 levels |
| 2200-1900 BE | deep | ⅔ | −2 per 3 levels (round down) |
| 1900-1650 BE | total | all | −1 per level |

**Undead XP:** class abilities count as special abilities by the build points outside Hit Dice (1-3 *, 4-5 **, 6-7 ***, 8 ****; SOTN p. 162). The elven cultist (4) adds **\*\***, applied to the ACKS II build (Judge's call; SOTN's ACKS I counts are not printed per class).

## As a mummy's abilities
A mummy "with the class abilities of an Nth-level elven cultist of X" keeps its own HD, attack throw, saves, AC and mummy powers ([[Mummy]]; [[Nethercity Features]]) and adds: Divine 3 spells per day at caster level N from the cultist list plus X's bonus spells, control undead as a chaotic crusader of level N, X's three cult powers, Divine Health, Sensing Good, Theology and the elf powers. XP: +2 asterisks (\*\*). SOTN's own printed spell counts (ACKS I) are given for comparison; use the ACKS II column.

| Level | Spells per day (ACKS II) | SOTN prints | Caster level / control undead as | Further powers in effect |
| --- | --- | --- | --- | --- |
| 4 | 3 1st, 3 2nd | 3/1 | 4th | none beyond the starting powers |
| 6 | 3/3/3 | 3/3/1/1 | 6th | minor magical research |
| 8 | 4/4/3/3 | 4/4/3/3/1 | 8th | as 6th |
| 9 | 4/4/4/3/1 | 4/4/4/3/3 | 9th | major magical research; may hold a fane |
| 12 | 5/5/4/4/4/3 | 7/7/5/5/4 | 12th | supreme magical research (necromancy, its own undeath) |

## Converted from ACKS I
- **From SOTN's text:** requirements, d4 HD, 13th level, mage attack throws, weapons (dagger, sling, staff, whip), no armour, two-handed or dual fighting; divine casting beyond a cleric's; cleric items and research; chaotic control undead; the five gods and their powers; spell lists; fane; level titles; Sacrificer template; cleric saves with the elven −1 (identical in ACKS II).
- **Judge's calls:** Divine 3 (SOTN's 133%-of-a-cleric spell counts and 12-spell lists fit it exactly) and Thievery 1 to reach 4 build points (SOTN's 1,325 XP is the same sum less ACKS I costs); Divine Health and Sensing Good as the two unassigned powers; the code of behaviour; spell mappings marked above and the fill-ins; Elf Tongues of antiquity; Cloister 1d2 × 10; the undead special-ability count on the ACKS II build.
- **Book errors and oddities:** the level text says attack and saving throws advance "as mages", but the save table printed is the cleric's (2 points per 2 levels), which this build keeps; the spell progression jumps from 5/5/5/4/4 at 11th to 7/7/5/5/4 at 12th and the XP from 685,000 to 935,000 at 13th (+250,000 against +150,000 elsewhere; probably 835,000); Nasga's list repeats charm person from the common list; Nasga's 5th-level line is printed above Dirgion's heading, out of place; Iskara's "undetectable curse*" is starred though it is itself the reversed form.
