---
type: build-checklist
tags:
  - sakkara/secret
source: "AX2 Secrets of the Nethercity (Autarch, ACKS I), 186 PDF pages; printed page = PDF page − 2"
---

# AX2 Secrets of the Nethercity — Judge notes: build checklist

Judge only. Prep for the Sakkara campaign, not play: no `Campaign/` state, actors, roll log or inventory are touched, and
the adventure is not opened in the engine. Source: Library `Adventures/_source/Secrets_of_the_Nethercity.pdf` (186 PDF
pages; page references are printed pages, "SOTN p. N" = PDF page N + 2; the whole map is on pp. 23 and 182-183).
Statblocks and rules converted from ACKS I to ACKS II by the acks2-conversion method with the rules vault's Monstrous
Manual notes and the engine's tables (the skill's scripts are not in the cloud container); notes structured by the
module-vault method. The city above is AX3 (`Adventure/AX3/`), linked, not repeated.

## Layout
| Path | Contents |
| --- | --- |
| `SOTN Hub.md` | premise, getting in, procedures, links, four `Running …` sections (sewer caves first, read by `--hub`) |
| `Nethercity History.md` | background, the three cities, timeline, the Awakening, the gods (SOTN pp. 5-10, 174-175) |
| `Nethercity Features.md` | standing rules: doors, inscriptions, sarcophagi, sludge and miasma, sinkholes, teleport wards, wall graves, necromancy by era, treasure (pp. 10-18) |
| `Nethercity Factions.md` | groups inside and above, their NPCs (traits, voice) |
| `Areas/` | one note per area A-T, room by room (`Nethercity X - Name.md`, hex 18.05) |
| `Tables/` | acks-table/1 YAML (`source.campaign: true`) |
| `Bestiary/` | `<Name> (SOTN).md` statblock notes (new monsters, named NPCs) |
| `Classes/` | JJ ch. 12 builds of the corrupt-elf classes, `sotn-class-builds.yaml` |
| `SOTN Magic Items.md`, `SOTN Spells.md` | Appendices A and C |

## Parts (SOTN PDF pages)
- [x] Hub (`SOTN Hub.md`), `Nethercity History.md`, `Nethercity Features.md` — PDF 6-24, 176-177
- [x] Tables: 4 wandering columns (2d10), unsettling events, mummy reaction, 5 wall-grave tables — PDF 16-22
- Areas (PDF 26-130):
  - [x] A, B, C (PDF 26-35): A1-A4, B1-B5, C1-C12; A 30 gp / 517 XP, B 3,603 gp / 1,050 XP, C 5,545 gp / 3,388 XP
  - [x] D, E (PDF 35-44): D1-D9, E1-E9 with sub-keys; D 11,216 gp / 1,864 XP, E 6,616 gp / 3,680 XP
  - [x] F (PDF 45-53): F1-F19 (+F11a-c); 18,290 gp, 6,759 XP
  - [x] G (PDF 53-65): G1-G27 with sub-keys; 70,195 gp / 16,365 XP
  - [x] H (PDF 65-79): H1-H26 with sub-keys; 32,550 gp + ~2,232 gp graves / 11,363 XP (+ up to 6,240 for the 480 H14 skeletons)
  - [x] I, J (PDF 79-92): I1-I14, J1-J15; I 13,172 gp as printed (9,497 corrected) / 3,725 XP, J 24,300 gp / 6,904 XP
  - [x] K, L (PDF 92-102): K1-K12, L1-L20; K 43,688 gp / 8,240 XP, L 3,789 gp / 4,504 XP
  - [x] M, N (PDF 102-113): M1-M22, N1-N13; M 37,290 gp / 4,840 XP, N 79,850 gp / 3,800 XP
  - [x] O, P, Q (PDF 113-125): O1-O5, P1-P14 (P8a-b), Q1-Q6; O 51,000 gp / 14,200 XP, P 53,336 gp / 8,750 XP, Q 56,917 gp / 12,440 XP
  - [x] R, S, T (PDF 125-130): R1-R4, S1-S4, T1-T2; R 15,500 gp / 10,344 XP, S 23,625 gp / 11,630 XP, T 15,000 gp / 5,000 XP
- [x] New monsters (Appendix B, PDF 143-153): 17 notes in `Bestiary/` (plus named NPCs from the area writers)
- [x] Magic items and spells (Appendices A and C, PDF 131-142, 154-162): 47 item entries, 42 spells
- [x] Classes (Appendix D, PDF 163-175): [[Elven Cultist]] (Bel, Dirgion, Iskara, Nasga, Telith), [[Elven Hierophant]], [[Elven Warlord]], [[Elven Wizard]] (four colleges); `Classes/sotn-class-builds.yaml`; JJ ch. 12 numbers from `custom_class.py`
- [x] `Nethercity Factions.md`: groups inside and above, 27 NPCs with traits and voice
- [x] Merges into the AX3 notes: Old District #12u, Organizations of Cyfaraun (Brotherhood = Family), Undercity of Cyfaraun (SOTN p. 6), Cyfaraun, AX3 Hub, AX3 README, Borderlands Background, Tower District
- [x] Final checks: 11 tables load (`load_campaign_table`); hub through `read_hub` (sewer caves, level 2, 1d6 every 3 turns 6+); every wandering entry resolves to a statblock with `Adventure/SOTN/Bestiary/` and `Adventure/AX3/Bestiary/` as extra folders; all 38 bestiary notes parse (`monsters.statblocks`); `hex.py 18.05` and `brief.py` run; wikilinks resolve (repo + rules vault). Independent check (sample: A1-A4, G9, G12, H13, J2, L4, O3, Q5; the four wandering tables and unsettling events; Eolande, Great Teacher, Orthanach, Troglodyte Chieftain, Marcan; Features): fixed the J2 martyr's XP (6+1****, 1,580; area J 6,904), H13's wording, the troglodyte chieftain's AC (9 with leather), summon berserkers made uniform, the A3 prawn speed, Cassair's inspire courage note, the slab-door "found open" cell; flagged SOTN's p. 19 example error and the giant ants reading. Values, weights, tallies, hp lists, tables and Features found correct.

## Work in progress
Unticked parts may already have files on main (snapshots of parts still being written). A part is done only when ticked.

## Open items
Each area note marks its own Judge's calls and book errors inline ("(Judge's call: …)", "(SOTN prints …)"); the list
below gathers the ones that matter across notes.

### Before play (not done here: Campaign/ is not touched in prep)
- `Campaign/campaign.yaml` `tools.bestiary` lists only `Adventure/Bestiary/`: add `Adventure/SOTN/Bestiary/` (and
  `Adventure/AX3/Bestiary/`) so `encounter`/`monster` find the SOTN and AX3 statblocks (all 38 SOTN notes parse with
  the engine's `monsters.statblocks`; the wandering tables resolve when those folders are passed).
- The SOTN classes (Elven Cultist, Hierophant, Warlord, Wizard) are campaign builds, not engine class data.
- Open the adventure (`adventure start --name "Secrets of the Nethercity"`, `adventure join` each PC) before the first delve.

### Conversion rules applied throughout (Judge's calls)
- **Wandering column per area:** sewer caves A, C, L; volcanic caves I, M; temple/tomb B, D-H, J, K, N, O, Q-T; river P.
  **Dungeon levels** 2 / 3 / 4 / 5 by the columns' threat (SOTN p. 19: 1-2, 2-3, 3-4, 4-6). Wandering "faewyrd" = lesser
  faewyrd; "jackals of shadow" = jackals of darkness. Area N with its doors shut counts as a sealed tomb.
- **Monsters with an MM equivalent** use the MM numbers (AC, HD, attack throw, damage, save, morale, XP) with SOTN's
  numbers appearing, hp and gear; SOTN's printed figures are given beside them. Renames as in AX3 (carcass scavenger →
  Carrion Horror, ochre jelly → Ochre Ooze, gray ooze → Grey Goo, green slime → Sage Slime, gelatinous cube → Gelatinous
  Mass, black pudding → Black Blob, yellow mold → Mustard Mold, shrieker → Shrieking Fungus, pit viper → Viper Snake,
  giant python → Python Snake, spectre → Specter, ghoul → Grave Ghoul), plus white ape → Cave Gorilla, sarcophagal worm
  → Sepulchral Worm, giant rhagodessa → [[Rhagodessa (AX3)]] (SOTN prints AC 4, ML +1; the AX3 note has AC 5, ML 0).
- **Mummies:** MM [[Mummy]] (5+1**, 660 XP; SOTN 5+1*, 460) with SOTN's HD by era; **classed mummies count two more
  asterisks for class abilities** (5+1**** 1,060; 6+1**** 1,580; 8+1**** 2,600; 9+1**** 3,100; Marcan 13**** 5,400;
  Orthanach 12****** 6,600). Horrific visage (cower) replaces SOTN's paralysis; x+1 HD attack as the next HD.
- **Skeletons:** human/elf warriors with bronze shields AC 3 (SOTN AC 2); non-human skeletons keep their HD in life
  (lizardman skeleton 2+1*, 8+, XP 47; SOTN 2*, 9+, 29; ape skeletons as cave gorillas).
- **SOTN bestiary XP** recounted with ACKS II weights (`Bestiary/` notes give SOTN's figures): bronze cobra 2* 29 (SOTN
  38), iron cobra 3* 65 (80), lesser faewyrd 4*** 245 (190), flailing spirit 5-8**** (SOTN 800-1,600), jackal of
  darkness 4* 135 (190; room lines 285), baboon and crocodile mummy 5** 500 (350), rat mummy 1+2** 27 (21). The area
  statlines follow the bestiary notes.
- **Class asterisks for mummies:** SOTN p. 162 counts class abilities as asterisks by build points outside Hit Dice
  (on the ACKS II builds: cultist **, hierophant ***, warlord *, wizard **). The area notes add a flat two (above):
  right for cultists and wizards; warlord mummies (D, E, I, M8, Q) would be one fewer, hierophants one more. Reconcile.
- **Mummy spells per day:** SOTN's room keys give ACKS I counts; the class notes give the ACKS II counts beside them
  (a 4th-level cultist 3/1 in SOTN, 3/3 in ACKS II). The area notes mostly keep SOTN's counts: use the class notes'
  ACKS II column in play.
- **Class builds (Judge's calls):** build allocations, spare powers, the warlord at 2,375 XP to 2nd (SOTN 2,125:
  ACKS II charges for the weapon trade-off), hierophant divine spells from 1st level, fastness troops paid. SOTN errors:
  warlord XP column shifted and its saves captioned "Elven Hierophant"; cultist save table vs text, spells and XP jumps
  at 12th-13th; wizard college proficiencies never listed.
- **Sepulchral worms:** MM −1 per 3 worms to the visage save and save F1 (SOTN −1 per worm, F4).
- **Spells:** ACKS II names by effect. No ACKS II equivalent, kept in italics: *unseen servant*, *knock*, *ventriloquism*,
  *summon berserkers*, *summon fantastic creature* (one [[Greater Hellhound]]), *glitterdust*, *control undead*,
  *prayer*, *fellowship*, *snake charm*, *gate*, *temporal stasis*, *wizard eye*, *oblivion*, *bane* (run as the mirror of
  Holy Blessing, −1). **Summon berserkers** summons MM [[Berserker]]s in every SOTN note
  (AX3 maps the spell to Summon Manes: the two books' notes differ; reconcile if a campaign-wide rule is wanted).
- **Potions:** "potion of healing" run as one dose of Cure Light Injury (ACKS II has no potion of that name);
  invulnerability → Necromantic Invulnerability; longevity → Potion of Youth; philter of love → Potion of Passion.
- **Items:** run the ACKS II version where one exists ([[SOTN Magic Items]] gives both); item effects saved vs Spells
  become Implements saves. SOTN's Iron Masks alignment roll kept; the Heroic Fantasy Handbook corruption option dropped;
  Shadowcowl Robe 25,000 gp (TT 5,000). *Staff of the serpent* (O3, Saorya) is the ACKS I item, described from memory
  (nearest [[Staff of Halting]]): check it against the ACKS I book. Collar of Conversation, Earring of Protection and
  Woodwind of the Woodlands are not placed in any room.
- **P8b** "resilient edifice" (Heroic Fantasy Handbook) linked to the JJ's minor edifice of elemental earth.
- **Teleport destinations:** L4's far platform in the Istrith Forest east of the Krysivor (no hex in SOTN: fix at first
  use); the N5 disc lands on a street of the Thieves' Quarter (Old District #9).
- **No restocking rate** for living groups in SOTN; the hub suggests AX1's as a model.
- Sludge: SOTN's middle rules (not the cinematic or "cruel realism" options, p. 12).
- Level placement where SOTN names none (B Upper; C2 Deep; D Upper; G Lower with G14 Abyssal; K Abyssal; I all Deep).
- O, P, Q: SOTN's text has north where the printed map has west; the notes follow the text.

### Book errors (SOTN)
- p. 10 "329 BE" for the cesspit collapse (329 IY). p. 5 "fifty miles northwest of Türos Tem" (campaign map: 18.05 vs
  22.20, 138 road miles; the map stands). p. 138 spellbook intro "pp. 137-138" (new spells pp. 152-160).
- Cross-references: C1 "to 3b" (C2a); C12 "to 6a" (F1); E9 "from 5f" (E6b); F17 "as noted in F14" (F15) and
  "Reliquary (F14)" (F17); H11 "towards 8u" (H23); I12 "northwest" (northeast); J10 "Sacrarium (J12)" (J11);
  K4 "door from J3" (K3); L6 "southeast" (north-west); M10 exit "M6" (M7); p. 120 P13 stair "vicinity of R2" (R4 on the
  map); spellbooks "F8" (F9) and "R3" (R2) on pp. 137-138; G20 faewyrd "haunts G6a" (G6e); G2a "greater faewyrd in G2b"
  (five lesser).
- The same monster printed twice differently: C11 python hp 30, 5d6 vs G18 hp 25, 2d8 (G18 and MM used); D5/J jackals MV
  140’, XP 285 vs appendix 150’, 190; faewyrd 4* in rooms vs 4** in the appendix; H14 bone golems XP 110 vs 190;
  tunnel prawn ML +1 vs +2; Marcan's Q1 and Q5 statlines; courtier 6+1* with the XP of 6+1***; cat mummies Chaotic vs
  Neutral; chryselephantine statue 8** for 1,100 XP in SOTN and the MM (the table gives 1,600).
- Tallies that do not match their items: C5, D5 (4,100 vs 5,300), E3, I2 (5,025 printed, 1,350 listed: 1,350 used),
  H6-H8, H16, H17, H21 (5,525 vs 5,025), J14, M9, M10, N7, N10, O5, P6, P12 (gold coral), R2, S3 (opals read as 750 gp).
- Counts: H3 360 graves vs 268 counted (92 put in H3c); H10a/b; O3 "four" sarcophagi (three); N3 13 jars, 19 scrolls;
  M17 graves priced 4.5 gp at 2000 BE (book value kept).
- Other: E2 dated 2700 BE with 2800 BE graves; H20 2300/2400 BE; T2 stasis "about 1700 BE" vs the timeline's late
  21st c. BE (timeline used); Saorya (O3) vs "Sorya" (p. 7); Sword of Valor a "shortsword" with a 36” blade; the D2
  short sword 1d8; the hydropion saves as "the hydra's" HD; "STATUTE, ANIMATED"; spell-text gaps (Circle of Agony,
  Forgetfulness, Mirage, Shrieking Skull MV).

### AX3 / SOTN
- SOTN p. 18 "Argollëan Brotherhood" = AX3's Argollëan Family (merged into [[Organizations of Cyfaraun]]).
- A1 = Old District #12u: the two books agree (frescoes of Mityara, the hole, the carrion horror); AX3 adds that the
  latrine has no man-sized way down and that the horror climbs the pipes. The carrion horror uses MM numbers in both.
- SOTN p. 6 lists the Undercity's underground parts (Palace, Solar Citadel, Amphitheater, Tower, Hall of Mourning,
  Merchant Guild vaults, Bathhouse cisterns): merged into [[Undercity of Cyfaraun]].
- The rhagodessa: AX3's note (AX3 gives no stats) has AC 5, ML 0; SOTN's F19 line prints AC 4, ML +1.
- Summon berserkers: AX3 → Summon Manes; SOTN notes → MM Berserkers (above).
- Remaining small items for a later pass: the hydropion's sting kills "instantly" (N9) vs "at the end of its initiative"
  (bestiary note); the D5 tally (printed 4,100 vs listed 5,300) is given both ways in the D note.
