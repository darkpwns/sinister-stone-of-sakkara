---
type: hub
tags:
  - sakkara/secret
source: "AX3 Capital of the Borderlands (Autarch 2018, ACKS I), 226 PDF pages; printed page = PDF page − 2"
---

# Capital of the Borderlands (AX3) — Judge hub

Judge only. Page references are AX3's printed page numbers ("AX3 p. N"; PDF page N + 2). AX3 is a setting book, not a scenario:
a Borderlands sandbox of 53 points of interest and the city of **Cyfaraun** (hex 18.05) with 8 districts, 82 points of interest
and the Undercity. Statblocks and rules are converted to ACKS II (see each note; Judge's calls and AX3 errors are listed in
`Adventure/AX3/README.md` under Open items). The Nethercity beneath the city is the separate module *Secrets of the Nethercity*
(AX2; its notes are a separate job; its entrance is the collapsed cesspool #12u in the [[Old District]]).

## Running Undercity of Cyfaraun
- Dungeon level: 2
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/ax3-undercity-encounters.yaml

AX3 pp. 63-67. Judge's call for the level. Below the Old District 5+ (pass `--wandering "1d6 every 3 turns, 5+"`). Result 80+ → `Tables/ax3-undercity-special.yaml` (nearest special location). No throws inside a special location until it is cleared (p. 64).

(The engine reads only the first `Running …` section through `--hub`: `acks.sh location --hub "Adventure/AX3/AX3 Hub.md"`
sets the Undercity. For the others pass the settings explicitly, e.g. `acks.sh location --site "Death Cult Hideout" --level 2
--wandering "1d6 every 3 turns, 6+" --table Adventure/AX3/Tables/ax3-undercity-encounters.yaml`; for a site with `none`, pass
`--wandering none`. The table path is relative to this note's folder: `Adventure/AX3/Tables/`.)

## Running the Mink - Family Hideout
- Dungeon level: 3
- Wandering monsters: 1d6 every 3 turns, 5+
- Encounter table: Tables/ax3-undercity-encounters.yaml

[[The Mink - Family Hideout]] (Old District #11u). Level 3 a Judge's call (3 HD residents). Above it: [[The Mink - Tavern]] (city building, level 0, wandering none).
## Running the Shrine of the Horned Rat
- Dungeon level: 3
- Wandering monsters: 1d6 every 3 turns, 5+
- Encounter table: Tables/ax3-undercity-encounters.yaml

[[Shrine of the Horned Rat]] (Old District #13u; wererat mages of the Tower). Level a Judge's call.
## Running the Doppelganger Den
- Dungeon level: 3
- Wandering monsters: 1d6 every 3 turns, 5+
- Encounter table: Tables/ax3-undercity-encounters.yaml

[[Doppelganger Den]] (Old District #14u; the Brotherhood of Knives). Level a Judge's call.
## Running the Death Cult Hideout
- Dungeon level: 2
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/ax3-undercity-encounters.yaml

[[Death Cult Hideout]] (Lake District #75u; Malthusia, cult of Dirgion). No throws inside until cleared; the setting applies once it is.
## Running the Catacombs of the Patriarchs
- Dungeon level: 1
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/ax3-undercity-encounters.yaml

[[Catacombs of the Patriarchs]] (Bridge District #36u, under the Solar Citadel). No throws until cleared.
## Running the Crocodile Nest
- Dungeon level: 1
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/ax3-undercity-encounters.yaml

[[Crocodile Nest]] (Plaza District #45u). No throws until cleared; the crocodile is at room 2 on 5+ on 1d6 at dusk and dawn.
## Running the Lizardman Sewer Lair
- Dungeon level: 1
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/ax3-undercity-encounters.yaml

[[Lizardman Sewer Lair]] (Festival District #28u). No throws inside until cleared; the rate is for the sewers around it; at the exit (key 4) 5+ on 1d6 at dusk and dawn.
## Running the Catacombs of the Ancestors
- Dungeon level: 1
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/ax3-undercity-encounters.yaml

[[Catacombs of the Ancestors]] (Temple District #68u). No throws in the rooms while the Grey Sisters and Knights keep them; the rate is for the sewer tunnels.
## Running the Eclipse Hideout
- Dungeon level: 1
- Wandering monsters: 1d6 every 3 turns, 6+
- Encounter table: Tables/ax3-undercity-encounters.yaml

[[Eclipse Hideout]] (Temple District #69u; Order of the Eclipse). No throws while the Order holds it; the rate applies once cleared and in the canal outside.
## Running the Imperial Amphitheater Basement
- Dungeon level: 1
- Wandering monsters: none

[[Imperial Amphitheater - Basement]] (Festival District #20u): sealed and guarded; on its sewer side use the Undercity setting. Above: [[Imperial Amphitheater - Arena]] (wandering none).
## Running the Sand and Bones Hideout
- Dungeon level: 1
- Wandering monsters: none

[[Sand and Bones Hideout]] (Festival District #25u): isolated. Above: [[Silk Pony Inn - Ground Floor]], [[Silk Pony Inn - Top Floor]] (wandering none).
## Running the Tower of Knowledge
- Dungeon level: 1
- Wandering monsters: none

Inhabited building (Tower District #50): [[Tower of Knowledge - Ground Story]], [[Tower of Knowledge - Second Story]], [[Tower of Knowledge - Third Story]], [[Tower of Knowledge - Fourth Story]], [[Tower of Knowledge - Fifth Story]], [[Tower of Knowledge - Basement]]. Past the Basement's sewer gate (room 10): the Undercity setting. Level 1 is a Judge's call for treasure.
## Running the Solar Citadel
- Dungeon level: 1
- Wandering monsters: none

[[Solar Citadel]] (Bridge District #36): staffed public temple.

## Premise (AX3 pp. 5, 35-43)
- Cyfaraun, capital of the Borderlands prefecture of Southern Argollë: an elven city (Cyfarawn) conquered by the Auran Empire, built on the ash-buried ruins of older elven cities; their sewers, crypts and catacombs form the **Undercity**, and deeper, sealed, lies the Chthonic **Nethercity**. As the border forts grow isolated, the ambitious, bold and greedy gather here.
- **The city now:** Prefect **Justirius Tavicus Basilio** (Fighter 11) is going mad (raised from the dead; Court Magist **Nicodos Essir**'s curse worsens it, p. 190); **Lady Syrena** and Essir rule almost as regents. Councillor **Arjenus Drakomir** (with his son, Tribune of the City Watch, and his uncle the Exarch, who eyes the throne once the Tarkaun's death in Somirea is confirmed) plots a coup against the loyalist **Valens Ambador**. The **Argollëan Family** (the Mink) and the **Sand & Bones Guild** (Silk Pony Inn) edge toward a sewer war. Doppelgängers have replaced the **Brotherhood of Knives**; wererat scholars of the **Tower of Knowledge** serve the Horned Rat; a **death cult of Dirgion** works beneath the Lake District; escaped lizardmen and a giant crocodile haunt the sewers.
- Numbering (p. 5): **bold #N** = Borderlands regional map site; plain #N = district map POI (#Nu its Undercity part); "Room (N)" = rooms on a special-location map. The overview chapter's POI numbers are often 1-2 lower than the district chapters': the notes use the district chapters'. Unnamed NPCs: unlisted abilities 9-12; normal class powers and everyday gear.

## Notes
- City: [[Cyfaraun]] (city note, history, districts, government, the Watch, laws), [[Cyfaraun (Market)]] (class III; all AX3 demand modifiers).
- City chapters: [[Organizations of Cyfaraun]], [[Buildings of Cyfaraun]], [[Doing Business in Cyfaraun]], [[Streets of Cyfaraun]], [[Undercity of Cyfaraun]], [[Imperial Vanguard]] (rival NPC party).
- Districts: [[Old District]] (POIs 1-14u), [[Festival District]] (15-28u), [[Bridge District]] (29-36u), [[Plaza District]] (37-45u), [[Tower District]] (46-52), [[Temple District]] (53-69u), [[Lake District]] (70-75u), [[Palace District]] (76-82).
- Dungeons and special locations: [[Catacombs of the Ancestors]], [[Catacombs of the Patriarchs]], [[Crocodile Nest]], [[Death Cult Hideout]], [[Doppelganger Den]], [[Eclipse Hideout]], [[Imperial Amphitheater - Arena]], [[Imperial Amphitheater - Basement]], [[Lizardman Sewer Lair]], [[Sand and Bones Hideout]], [[Shrine of the Horned Rat]], [[Silk Pony Inn - Ground Floor]], [[Silk Pony Inn - Top Floor]], [[Solar Citadel]], [[The Mink - Family Hideout]], [[The Mink - Tavern]], [[Tower of Knowledge - Basement]], [[Tower of Knowledge - Fifth Story]], [[Tower of Knowledge - Fourth Story]], [[Tower of Knowledge - Ground Story]], [[Tower of Knowledge - Second Story]], [[Tower of Knowledge - Third Story]].
- Borderlands: [[Borderlands Gazetteer]] (all 53 sites with hexes), [[Borderlands Background]] (history, geography, military), [[Region Map]]; sites: [[Andrastem]], [[Arwia Oasis]], [[Azen Radokh]], [[Burial Mound of the Empyreans]], [[Buried Temple]], [[Collapsed Elven Keep]], [[Dragon's Tor]], [[Eyrie of the Dread Eye]], [[Fist of Telith]], [[Fortress of Gorgbad]], [[Kruantem]], [[Lair of the Manticores]], [[Lair of the Warlock]], [[Luseatum]], [[Menicos]], [[Mityethtem]], [[Morgot]], [[Nabu-Kudur]], [[Nurgarog]], [[Redoubt on the Earthway]], [[Ruined City of Cyfandir]], [[Ruined Imperial Fortress]], [[Ruined Monastery]], [[Ruined Wizard's Tower]], [[Ruins of Azen Kairn]], [[Ruins of Zahar]], [[Samos]], [[Sarotem]], [[Sepulcher of the Sorceress-Queen]], [[Shrine of the White Lady]], [[Siadanos]], [[Sinkhole of Evil]], [[Temple of the Stone Horns]], [[Turos Augil]], [[Turos Aure]], [[Turos Drav]], [[Turos Erin]], [[Turos Gundan]], [[Turos Luin]], [[Turos Morn]], [[Turos Quell]], [[Turos Telle]], [[Turos Veren]], [[Turos Zera]], [[Valley of the Sorcerer Kings]], [[Watchtower at Eammon Mor]], [[Wyvern Cliffs]], [[Zelictum]]; with notes outside AX3/: [[Cyfaraun]] (#10), [[Turos Orn]] (#15), [[Turos Spen]] (#22), [[Turos Tem]] (#28), [[Turos Aster]] (#29).
- Classes AX3 uses that ACKS II lacks: JJ ch. 12 custom builds [[Mystic]], [[Anti-Paladin]], [[Chosen]], [[Thrassian Gladiator]], [[Elven Courtier]], [[Elven Enchanter]], [[Elven Ranger]], [[Gnomish Trickster]] (`Classes/`); dwarven machinist, delver and fury from By This Axe (ACKS II, rules vault `Supplements/By This Axe/`).
- Items: [[AX3 Magic Items]].
- Bestiary: `Adventure/AX3/Bestiary/<Name> (AX3).md` — [[Abimbola (AX3)]], [[Aghilas (AX3)]], [[Aranth Faunus (AX3)]], [[Asrya Raija (AX3)]], [[Aureus Ambador (AX3)]], [[Balkar (AX3)]], [[Blade-Dancer Valara (AX3)]], [[Brother (AX3)]], [[Catechist of Ammonar (AX3)]], [[Centurion Cellë (AX3)]], [[Clitus Omnus (AX3)]], [[Cultist of Dirgion (AX3)]], [[Death Cult Enforcer (AX3)]], [[Deathbringer (AX3)]], [[Destrio (AX3)]], [[Elite Deathbringer (AX3)]], [[Gabriol Eirenikos (AX3)]], [[Gundus Jannion (AX3)]], [[Halgar Halface (AX3)]], [[Hesta Faunus (AX3)]], [[Hrad the Blood Axe (AX3)]], [[Irial Ui Aedon (AX3)]], [[Jonus Krusaro (AX3)]], [[Justirius Tavicus Basilio (AX3)]], [[Kalbo (AX3)]], [[Knight of the Winged Sun (AX3)]], [[Larce (AX3)]], [[Lazareo Ravil (AX3)]], [[Liber Faunus (AX3)]], [[Lutarius Sinorix (AX3)]], [[Maharbal Bar Abedsh (AX3)]], [[Malthusia the Diabolist (AX3)]], [[Mara Rëavus (AX3)]], [[Maximus Arjentüran (AX3)]], [[Megaravicos Eight-Fingers (AX3)]], [[Mentenus Cavie (AX3)]], [[Nicodos Essir (AX3)]], [[Nikolaus the Nicean (AX3)]], [[Ordinary Gladiator (AX3)]], [[Prelate Ezelus (AX3)]], [[Prelate Romus (AX3)]], [[Rhagodessa (AX3)]], [[Rhankur the Doombringer (AX3)]], [[Selene Nictorian (AX3)]], [[Sentonus (AX3)]], [[Sigilo (AX3)]], [[Subaltern of the Winged Sun (AX3)]], [[Terkinos (AX3)]], [[Thana Nyssand (AX3)]], [[The Kid (AX3)]], [[Una (AX3)]], [[Valenus Mirens (AX3)]], [[Valeria Victa (AX3)]], [[Veteran Gladiator (AX3)]], [[Veteran Knight of the Winged Sun (AX3)]], [[Virathos (AX3)]], [[Xandrama (AX3)]], [[Yanos (AX3)]]. Everything else is a Monstrous Manual note.

## Tables (`Adventure/AX3/Tables/`, acks-table/1)
- City and Undercity: `ax3-city-encounters.yaml` (1d100, +30 after dark), `ax3-undercity-encounters.yaml`, `ax3-undercity-special.yaml`, `ax3-rumours.yaml`, `ax3-irritating-rumours.yaml`, `ax3-borderlands-rumors.yaml`, `ax3-borderlands-demand-modifiers.yaml` (reference, not rolled), `ax3-beastman-tribe.yaml`.
- District special encounters: `ax3-old-special.yaml`, `ax3-festival-special.yaml`, `ax3-bridge-special.yaml`, `ax3-plaza-special.yaml`, `ax3-tower-special.yaml`, `ax3-temple-special.yaml`, `ax3-lake-special.yaml`, `ax3-palace-special.yaml`.
- Old District: `ax3-old-blackmail.yaml`, `ax3-old-doppelganger-1.yaml`, `ax3-old-doppelganger-2.yaml`, `ax3-old-doppelganger-3.yaml`, `ax3-old-elven-victim.yaml`, `ax3-old-emporium-vendor.yaml`, `ax3-old-exotic-animal.yaml`, `ax3-old-human-victim.yaml`, `ax3-old-mentenus-notes.yaml`, `ax3-old-mink-entertainment.yaml`, `ax3-old-mink-games.yaml`, `ax3-old-notable.yaml`, `ax3-old-special.yaml`.
- Festival District: `ax3-festival-amphitheater-daily.yaml`, `ax3-festival-amphitheater-festival-hourly.yaml`, `ax3-festival-basement-lift.yaml`, `ax3-festival-bloodmoon-amateur-reason.yaml`, `ax3-festival-bloodmoon-combatant.yaml`, `ax3-festival-bloodmoon-equipment.yaml`, `ax3-festival-bloodmoon-level.yaml`, `ax3-festival-bloodmoon-professional-reason.yaml`, `ax3-festival-bout-type.yaml`, `ax3-festival-bouts-death.yaml`, `ax3-festival-bouts-incapacitation.yaml`, `ax3-festival-epic-accompaniment.yaml`, `ax3-festival-epic-poetry.yaml`, `ax3-festival-musical.yaml`, `ax3-festival-ordinary-gladiator.yaml`, `ax3-festival-popular-entertainment.yaml`, `ax3-festival-snug-game.yaml`, `ax3-festival-special.yaml`, `ax3-festival-sporting.yaml`, `ax3-festival-theatrical.yaml`, `ax3-festival-veteran-gladiator.yaml`.
- Bridge, Plaza, Lake: `ax3-bridge-assault-victim.yaml`, `ax3-bridge-gondolas.yaml`, `ax3-bridge-jumper.yaml`, `ax3-bridge-notable.yaml`, `ax3-bridge-special.yaml`, `ax3-plaza-climber.yaml`, `ax3-plaza-graffiti.yaml`, `ax3-plaza-merchant.yaml`, `ax3-plaza-special.yaml`, `ax3-lake-cowled-figures.yaml`, `ax3-lake-drunken-mage.yaml`, `ax3-lake-family.yaml`, `ax3-lake-invitation.yaml`, `ax3-lake-patricians-want.yaml`, `ax3-lake-special.yaml`, `ax3-lake-stranger.yaml`.
- Tower and Palace: `ax3-tower-bird-omen.yaml`, `ax3-tower-notable.yaml`, `ax3-tower-special.yaml`, `ax3-palace-flogging.yaml`, `ax3-palace-mob.yaml`, `ax3-palace-notable.yaml`, `ax3-palace-patricians.yaml`, `ax3-palace-pronouncement.yaml`, `ax3-palace-special.yaml`, `ax3-palace-spy.yaml`, `ax3-prefect-dungeon-prisoners.yaml`, `ax3-courthouse-trials.yaml`.
- Temple: `ax3-temple-messenger.yaml`, `ax3-temple-notable.yaml`, `ax3-temple-special.yaml`, `ax3-orphan-gifts.yaml`, `ax3-eclipse-contracts.yaml`, `ax3-eclipse-vetting.yaml`, `ax3-retribution-petitioner.yaml`, `ax3-retribution-reason.yaml`.
- City-building system: `ax3-building-artisan-occupation.yaml`, `ax3-building-entertainer-occupation.yaml`, `ax3-building-hosteller-occupation.yaml`, `ax3-building-laborer-occupation.yaml`, `ax3-building-merchant-occupation.yaml`, `ax3-building-military-occupation.yaml`, `ax3-building-minor-ecclesiastic-occupation.yaml`, `ax3-building-minor-magician-occupation.yaml`, `ax3-building-npc-class.yaml`, `ax3-building-npc-level.yaml`, `ax3-building-occupant-general-street.yaml`, `ax3-building-occupant-large-townhouse.yaml`, `ax3-building-occupant-medium-cot.yaml`, `ax3-building-occupant-medium-townhouse.yaml`, `ax3-building-occupant-small-cot.yaml`, `ax3-building-roof-lake-palace.yaml`, `ax3-building-roof-old-bridge.yaml`, `ax3-building-roof-plaza-festival.yaml`, `ax3-building-roof-tower-temple.yaml`, `ax3-building-specialist-occupation.yaml`, `ax3-building-stables-small.yaml`, `ax3-building-type-huge.yaml`, `ax3-building-type-large.yaml`, `ax3-building-type-medium.yaml`, `ax3-building-type-small.yaml`, `ax3-building-walls-lake-palace.yaml`, `ax3-building-walls-old-bridge.yaml`, `ax3-building-walls-plaza-festival.yaml`, `ax3-building-walls-tower-temple.yaml`.

## Procedures the Judge runs

### City encounters (AX3 pp. 58-62; [[Streets of Cyfaraun]])
- Encounter throw 1d6, **6+** (5+ when the party is looking for trouble): every **hour** wandering the streets by day; every **30 minutes** (3 turns) by night or in alleys by day; every **10 minutes** (1 turn) in alleys by night.
- Roll 1d100 on `Tables/ax3-city-encounters.yaml`, **+30 after dark**; "special encounter" results → the district's 1d10 special table (`ax3-<district>-special.yaml`).
- Movement: one city block per turn at commuting speed; meandering parties throw Navigation **11+** each turn or end up 1d4+1 blocks off (details and modifiers in the note).
- Undercity: see `Running the Undercity` above and [[Undercity of Cyfaraun]] (entrances by district, sewer grates, light, sludge, random basements).

### Rumours (AX3 pp. 43-45)
- One rumour on any Friendly reaction from a Cyfaraun NPC; a PC with Loremastery starts with one; also by hijinks. Many district events give one on a Friendly reaction.
- Roll 1d20 on `Tables/ax3-rumours.yaml` (columns Truth (Judge), Behind it (Judge)): 12 true, 2 mostly true (15, 16), 1 mostly false (3), 5 false (5, 7, 11, 13, 19). Borderlands rumours: `ax3-borderlands-rumors.yaml`. About the Imperial Vanguard: `ax3-irritating-rumours.yaml` (1d10, p. 201).
- Selling rumours: Family carousers in the Old District pay 3d12gp each (Old District special encounter 6, p. 77).

### Factions (AX3 pp. 39-43; full: [[Organizations of Cyfaraun]])
- Office of the Prefect (Palace #80): Basilio (F11), Lady Syrena, Magist Nicodos Essir (M7). Prefectural Guard: Legate Jannion (F7), 600 troops, barracks #81, 18 road watchtowers.
- Municipal Council: Drakomir faction (Arjenus, F6, villa #72) vs loyalists (Valens Ambador, F6, villa #73). City Watch: Tribune Narmirio Drakomir (F5), 240 officers plus the HQ #5 reserve.
- Argollëan Family: Liber Faunus (Venturer 10), the Mink #11/#11u; smuggling 60 loads a month at 10% (5% intercepted, 2d8+3 days); fences treasure at 65% (80% to friends); no deals with obvious Lawfuls.
- Sand & Bones Guild: Selene Nictorian (Thief 9), Silk Pony #25/#25u; monthly pit fights (3d6 bouts; 50gp submission, 100gp death).
- Brotherhood of Knives (#14u): three doppelgängers. Death Cult of Dirgion (#75u): Malthusia (Warlock 4). Cult of the Horned Rat (#13u): Provost Mentenus Cavië (M9, wererat).
- Gladiator schools: Omnus Pluris #21, Celictor Nuvicus #22 (escaped lizardmen and crocodile, #28u, #45u), Maximus Arjentüran #23 (a devil boar).
- Merchant Guild: Apollonis Meteros (Venturer 9), Guildhouse #8 (bank). Mercenary Guild: Balcadur Brogitarius (F5), #10. Craft and Dockworkers' guilds.
- Temples and orders: Winged Sun (Arëtar, Crusader 10; Solar Citadel #36), Knights of the Winged Sun (Cellë, Paladin 6; #67), Keepers of the Hearth Fire (Aundëmë, Priestess 9; #58-61), Tower of Knowledge (Regent Aurëus Ambador M10; #50), Temple of Justice (Prelate Ezelus; #63), Grey Sisters (Doarë, Priestess 8; #62, #68), Order of the Eclipse (Destrio, Assassin 8; #69u), Blade and Veil (#65), Hall of Travelers (#64).
- Rival party: [[Imperial Vanguard]].

### Hiring (AX3 pp. 56-57; [[Doing Business in Cyfaraun]]; RR market class III)
- Search fee 1d8+5gp per week per type; arrivals ½ / ¼ / rest over three weeks; hiring offer by reaction.
- Henchmen available: 0th 4d8 (12gp), 1st 1d4 (25gp), 2nd 1d3 (50gp), 3rd 1 (85%) (100gp), 4th 1 (45%) (200gp).
- Where: Mercenary Guildhouse #10 contract board (join STR 9+, 12gp a year; lodging 1sp; injury payouts 100/40/40/30/10/5gp; p. 71); Hall of Travelers #64 notices 1d8+5gp, 15% a specialist guest per night (p. 165); Tower #50 monthly 1d2 apprentice mages, 25% an arcanist, alchemist or engineer, 65% a sage (p. 152); Karthas at the Emporium: 2d4+1 gladiator candidates a month at 40gp, indentured specialists at 33× monthly wage (p. 81).

### Services (AX3 pp. 56-57, 70-71, 152; [[Doing Business in Cyfaraun]])
- Trade: class III (a venturer treats it as II or takes +1 market impact; impact 0: class IV); impact = normal load of vehicles and animals ÷ 5,000 st (max 10). Demand modifiers: [[Cyfaraun (Market)]].
- Gate toll 4d6+2gp per 5,000 st; customs 2d10% on imports; moorage 1gp per 10 shp a day; stabling 2sp mule, 5sp horse, 1gp cart, 2gp wagon a day; porters 1gp per 200 st.
- Equipment: class III availability (II for venturers); commissions up to 10×.
- Investment up to 10,000gp per type per risk per month: safe 0.25%, cautious 0.5% ±1d2%, balanced 1% ±1d3%, risky 3% ±1d10%, perilous 9% ±1d20% (p. 57).
- Bank (Merchant Guildhouse #8): client on a Friendly reaction (+1 venturer, +1 per Bargaining rank); deposits 0.25% a month; loans up to 10,000gp a month at 3% a month (collateral) or 9%; exchange 0.25%.
- **Treasure law (p. 57):** half of Undercity finds to the treasury; tax-collector check 5% + 1% per 1,000gp sold or banked last month, takes 50% of assessed value; the Family fences at 65% (80% to friends); XP is full regardless.
- Tower of Knowledge #50: identify an item 2,000gp, 2 weeks; a potion 40gp, 1 turn; formulas 100/200/400/1,000gp (1st-4th). Joining the Tower: [[Tower District]].
- Lodging: Mercenary Guild 1sp; Hall of Travelers hostel 2sp; Silk Pony bed 2sp, room 5sp; Imperial Charter Inn #74 2gp (+1gp bath).
- Law: Imperial Courthouse #82 (private prosecution, 7 magistrates, citizen juries; `ax3-courthouse-trials.yaml`); Temple of Justice #63.
- Gladiatorial games and betting: [[Festival District]] (the "Running gladiatorial games and betting" section); Blood Moon bouts at the [[Sand and Bones Hideout]].

### The city-building system (AX3 pp. 45-55; [[Buildings of Cyfaraun]])
1. **Size** from the district map (25% small, 50% medium, 20% large, 5% huge); 25% are subdivided (medium → 2d3 small, large → 4d4 small, huge → 2d6 medium).
2. **Type:** `ax3-building-type-<size>.yaml` (1d100); shops 1d6: 1-2 store, 3-6 workshop.
3. **Occupants:** the Standard Occupants (in the note), then `ax3-building-occupant-*.yaml`, the occupation tables, `ax3-building-npc-class.yaml` and `ax3-building-npc-level.yaml`; who is home by day.
4. **Style:** `ax3-building-walls-<districts>.yaml`, `ax3-building-roof-<districts>.yaml`.
5. **Treasure:** 1.5 × the monthly wages of the non-dependent occupants (gp:sp:cp 1:10:100); shops add 1d6 × monthly earnings in goods.

### Borderlands (AX3 pp. 15-33; [[Borderlands Gazetteer]])
- Travel on the campaign hex grid ([[Region Map]]); sites outside columns 14-31, rows 2-24 have only their own hex in `Data/hexes.csv` so far: extend the map before overland travel there.
- Garrisons, watchtowers, fort template and beastman clanhold stocking: [[Borderlands Gazetteer]]; `ax3-beastman-tribe.yaml`.
