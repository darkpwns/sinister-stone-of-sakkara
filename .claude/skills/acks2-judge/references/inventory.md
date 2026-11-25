# Inventory (engine stage 6)

Load when anything is bought, sold, found, given, dropped, picked up, used up, lost, broken or paid for, or when a
character, henchman, hireling or animal joins.

The inventory `Campaign/inventory-state.json` (config `tools.inventory_state`, Judge only) is the only record of who
holds what: every possession and coin of every holder, kept as a log of events, each with its cause. An actor's
`gear`, `coins`, `weapons` and `encumbrance_st` are generated from it on read (`acks.sh actor show <id>`); the actor
file stores none of them. `save.sh` refuses to save while the log does not replay (`acks.sh inv check`). Prices, weights, packs, container capacities and market availability
come from the print-checked equipment tables (`acks.sh inv catalog WORDS` finds an item); the engine names its source.

## Setup (once per campaign, at bootstrap after the Table rules)
- `acks.sh inv init --month-days N` (N = Table rules "Month length", the same as the retinue's).
- For each PC actor: `acks.sh inv holder add <id> --kind pc --opening --discard-sheet-gear` (the id is the actor's).
  The coins of its `possessions` block become the opening balance, and the gear written on the PDF is recorded in the
  event and cleared (the block goes; from now on the inventory is the record).
  Then add each item from that list: `acks.sh inv add <id> "<catalog item>" N --cause "starting equipment" [--slot S]`.
  The ids are the same as in the exploration party (`acks.sh party add <id>`).
- Henchmen and hirelings become holders on `acks.sh hire … --publish-to` (the engine does it). Their equipment (the
  candidate's `JUDGE:` items) goes in with `inv add … --cause "equipment on hiring"`.

## Commands (`acks.sh inv …`; every change needs `--cause`)
| Situation | Command |
| --- | --- |
| Buying in a market (availability per party and month, payment with change) | `inv buy <id> "<item>" [PACKS] --market "<Place>" --market-note "07 Markets/<note>.md" [--payer ID] [--price 2gp for a listed range] [--slot S]` |
| Buying an animal (it becomes a holder that carries a load, up to its maximum load) | `inv buy <id> "Mule, Draft" --as mule1 --market … --market-note …` |
| Buying a vehicle (cart, wagon, chariot, palanquin: one vehicle, whatever its team) | `inv buy <id> Wagon --as wagon1 --market … --market-note …` |
| Harnessing a team (the team decides the configuration: one ox, two mules or two medium horses for each heavy horse on a large cart or wagon; a team between two rows pulls as the smaller) | `inv harness wagon1 mule1 mule2 mule3 mule4`; a palanquin: `inv harness pal1 --bearers 4`; a team the rules do not list: `--config "<Vehicles row>" --cause "…"`; `inv unharness wagon1` (passengers dismount first) |
| Selling an animal or vehicle (empty, unharnessed) | `inv sell <id> mule1 --market … --market-note …` |
| Selling equipment in good condition (same limits; list price unless `--price`) | `inv sell <id> "<item>" [UNITS] --market … --market-note …` |
| A bargainer haggles (Bargaining proficiency or a venturer's Expert Bargaining, RR p. 107) | add `--bargainer ID` to `inv buy` / `inv sell` (10% off / 10% more; an opposed bargainer is your reaction rolls first) |
| Found, given by an NPC, made, starting gear (not treasure: treasure is stage 5's `recover`) | `inv add <id> "<item>" N --cause "…"` |
| Used up, lost, broken, stolen, given away to an NPC, eaten | `inv remove <id> "<item>" N --why used\|lost\|broken\|stolen\|destroyed\|"given away"\|eaten\|spent --cause "…"` |
| Between holders (characters, animals, caches) | `inv give <from> <to> "<item>" N --cause "…"`; coins: `inv give <from> <to> 5gp --cause "…"` |
| Readying or stowing (hands, belt, back, backpack, sack, pouch, hidden, worn, armor) | `inv move <id> "<item>" N --slot right_hand`; a weapon: `inv wield <id> "<item>"` (below) |
| Left behind / picked up | `inv drop <id> "<item>" N [--at camp-ford]` (default: the ground at the current site); `inv take <id> "<item>" N --from <cache>` |
| Lodging, food, services, tolls, bribes, fees, ransoms | `inv pay <id> 3gp 5sp --to "<who>" --cause "…"`; money received: `inv receive <id> 20gp --from "<who>" --cause "…"` |
| Money-changer | `inv exchange <id> 300cp --into gp` (fee, if any: `inv pay`) |
| Rations or firewood into the stage 4 supplies before a trip | `inv provision <id> "Rations, Iron" N` |
| An item not on the lists, or a list row whose weight or price is the Judge's ("By Weight", "1+", "Varies") | once: `inv define "<name>" --items N \| --stone N [--value 5gp] [--base "<row>"]`, then use it like any item |
| Looking | `inv show [<id>]`, `inv history <id> [--item X]`, `inv holder list`, `inv check` |

## Weapons (engine 6.20.0)
- Every weapon is its own item with an id (`w1`, `w2`, … in `inv show`); ammunition and darts stay counted stacks. Its
  dice, damage types, size and specials are copied once from its weapon table row; magic bonus, masterwork, silvered and
  extraordinary are per weapon, each with its source (the catalog row, a treasure lot and its TT note, or your entry).
  Name a weapon by its row ("Sword") when they are all alike, else by its id (the engine refuses to choose).
- In hand: `inv wield <id> <item> [--two-handed] [--hand right|left]`; `inv grip <id> <item> one|two --cause "…"`. Two
  hands need the other hand empty (a shield in the left hand refuses); large weapons are always two-handed.
- Your entries, with their cause: `inv set <id> <item> magic=1|masterwork=attack|damage|both|silvered=yes|extraordinary=yes
  --cause "…" [--hidden]` (magic makes it extraordinary; `--hidden`: the players do not know it yet).
- A silver version of a weapon: `inv buy <id> Sword --silvered …` (10× the price, rule `weapon.silver_version`).
- Selling a magic, masterwork or silvered weapon needs `--price`; a treasure lot's weapon is refused (sold off the books,
  `xp-treasure.md`).

## Broken shafts, stabling, animals (engine 7.17.4)
- A spear, polearm or lance whose shaft breaks on a natural 1 stays in hand as a broken weapon (its magic kept): it
  fights as a dagger or a staff at −1 (`inv use ID ITEM dagger|staff` picks the end) until `inv repair ID ITEM
  [--payer ID]` (1gp, RR p. 127; where a repair can be had is yours).
- Animals and vehicles left behind: `inv stable ID… --at "<place>" --cause "…"` (they no longer march, eat from the
  party's fodder, or can be ridden, loaded or harnessed; engine 7.18.8: its riders dismount and the members'
  supplies packed on it go back onto them, said in the output: check their loads), `inv unstable ID…` (it counts the nights; the fee per night
  is on the JUDGE line, RR p. 131: pay it with `inv pay`). An animal or vehicle gained without buying:
  `inv add ID "<row>" 1 --as NEWID --cause "…"`. An animal killed: `inv animal dies ID --cause "…"` (engine
  7.18.12: its load and tack dropped on the ground cache of the site, riders dismounted, packs back on their members,
  its team unharnessed, the holder closed as dead); never `inv holder remove` for it.
- A purchase refused for want of room or stock says how many packs and units were asked (`inv buy ID torch 2` buys two
  packs of six); a refused purchase keeps the month's availability roll: asking again does not roll again.

## What the other commands take on their own
- `light on --kind torch|candle|lantern --carrier <id>`: a torch or candle burns, a lantern needs the lantern and burns a
  flask of common oil; `light refuel`: a flask. Refused if the carrier has none.
- `attack` with a missile weapon: one arrow, bolt or sling stone (`--ammo "silver arrow"` to choose); a hit destroys it,
  a miss leaves it on the ground at the site (reading `inventory.fired_ammunition`); a thrown weapon lands at the site,
  a flask of oil or holy water breaks. A lance, spear or polearm breaks on a natural 1. Refused before rolling if the
  attacker has nothing to shoot or throw.
- `explore spike --spikes N --by <id>` uses his iron spikes; `force-door --crowbar` and `search|trap-trigger --pole` need
  the tool in the actor's possession.
- `wages pay <MID> --payer <id>` takes the wages from the payer's coins; `recruit` takes the week's fee from the
  employer; `appraise --fee` from `--by`.
- `payout --apply` puts each share's coins into the inventory; `death --dies` moves everything the dead man held to
  `body:<id>` (take from it with `inv take`).
- An inventory animal's or vehicle's stage 4 cargo is its inventory: load it with `inv give <id> mule1 …` or
  `inv give <id> wagon1 …`, never `mounts load --cargo`. Inventory animals and harnessed vehicles join the march
  (stage 4) by themselves; a harnessed animal carries no pack and no rider (its fodder rides in the vehicle).
- A wheeled vehicle needs a driver: `mounts ride wagon1 --rider <id>` (passengers the same way; each weighs 15 st plus
  his gear). `supplies show <id> --on wagon1` packs a member's supplies in it. Barrels (20 days of water each, weighed
  empty) and waterskins in a vehicle hold the water of the members whose supplies ride in it.
- Water carried on the march (stage 4 supplies, in days) is capped by waterskins: 5 to a day's water (RR p. 146); members
  whose supplies ride on one animal (`supplies show ID --on mule1`) share the waterskins they and the animal hold.
  `supplies add|give --water` past it is refused; `water` at a river fills the waterskins; water found past them is left;
  selling, losing or giving away waterskins pours out what they held. Buy waterskins before a dry crossing.

## Before save.sh
`save.sh` runs `actor check` on every actor and `inv check` (the log replays to the stored holdings; actor holders,
lights, animal loads, lot carriers and henchmen agree) and rewrites the Ledger's "Purchases and sales" table from the
log. If it refuses: record the missing event.
- A bag of holding or other container whose contents weigh nothing past its own weight (engine 7.19.17): its own
  holder, `inv holder add bag1 --kind container --cap 10 --weighs 6 --carrier lucilla --name "<what it is>"` (the
  note's capacity and weight); `inv give lucilla bag1 ITEM` puts things in (refused past --cap), and the carrier's
  encumbrance counts only --weighs. Never a cache holder plus an item.

## Engine 7.23-7.24 (Sakkara run 2 requests)
- `recover --goods "jar of oil" --value 100 --stone 5 --pieces 10`: a lot of like pieces that `--split L#:N` divides;
  `recover --undo L#` voids a loose find (no hoard).
- `train lot` of a creature captured in an adventure already paid out: its sale's XP goes to that payout's share-holders
  by `payout --sale L#`.
- `restore ID … --apply` (no roll without `--apply`) makes a restored character an active holder again with his
  possessions back from `body:ID`.
