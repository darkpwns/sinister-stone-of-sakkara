# Overland travel — with the rules engine (stage 4)

Load when the party travels by hex. If config `procedures.overland` names a campaign procedure note, follow it and use
this file for what it leaves to the core rules. With `core`, the engine runs the daily procedure (JJ "Sequence of Play
(Wilderness Expeditions)"); what it leaves to the Judge is in the tools repo's `engine/COVERAGE.md` (stage 4). Every
command below is `acks.sh CMD` (it adds the exploration state, the hex adapter `campaign.yaml hexes`, the retinue state
and the roll log). Narrate what the characters perceive; never the hidden rolls (navigation, encounter throws and their timing, the
true hex while lost, hunting, foraging and search throws). Open: the weather, the hex the party believes it is in, its
supplies, the party's Evasion throw, hp healed and CON lost.

## Setup (once per journey)
- `travel-init --at CC.RR --season spring` (dawn and moon from config `tools.travel`: `--dawn 06:00 --moon half`); every
  party member must be in the exploration state first (`party add ID`, the actor id).
- Supplies per member, in days. Bought rations and firewood are inventory items until packed: `inv provision ID "Rations, Iron" N`
  (`inventory.md`); `supplies add ID --food N --kind iron|standard --water N [--firewood ST]` only for food or water not
  bought (found, given by an NPC). Water carried is capped by the inventory's waterskins: 5 waterskins hold a day's water
  (RR p. 146); members whose supplies ride on one animal share its waterskins and theirs. The engine refuses water past
  that, fills only the waterskins at a river, leaves the rest of water found, and pours out what lost waterskins held. Mounts and
  pack animals: inventory animals and harnessed vehicles join the march by themselves (`inventory.md`: `inv buy … --as`,
  `inv harness`; a wheeled vehicle needs a driver: `mounts ride wagon1 --rider ID`; passengers the same way; the slowest
  vehicle sets the pace; wheeled vehicles keep to roads in desert, mountains, forest and swamp; palanquins do not);
  animals outside the inventory: `mounts add ID --kind "Horse, Light" --rider ID [--cargo ST --food ST --water ST]` (no rider: led
  pack animal); `supplies show ID --on M1` packs a member's food and water on an animal (its weight moves there).
  Carried food, water and firewood count in each member's encumbrance and a rider's weight (15 st + gear + supplies).
  Hit points the party starts with: `heal ID --hp N`. Settings: `heal ID --set protective=no|wet=yes|native=polar|resist=cold`.

## Each day
1. **Travel**: `travel --to CC.RR` (or `--dir FACE --n N`, `--route A,B,C`, `--hours H`, `--ancillary` for up to 4
   hours, `--familiar ID` for an explorer's Pathfinding, `--retrace` on a route already travelled) or `forced-march …`.
   The first travel of the day rolls the weather (open) and the Navigation throw (hidden; no throw on a road or
   navigable river); each hex entered costs 6 miles at the party's speed × terrain (× road after terrain, × weather,
   mud, snow), and makes the encounter throw (hidden; 1d6 miles in). An encounter stops the travel there with who, how
   many, lair, distance and detection rolled; then `encounter surprise …`, `evade` or `reaction`, `encounter fight`
   (encounters.md). `travel` again continues the route. A lost party strays without knowing; the line's hidden part
   says where it truly is. The day's travel hours are enforced (8, or 12 forced; ancillary hours left are 4).
2. **Ancillary activities** (1 hour each; members working side by side share the hour): `forage [--honest]` (food,
   once a day each; a Survival member feeds himself every wilderness day without it), `water [--carry N]` (party, once
   a day; free and automatic in a river or lake hex: use it there every day the party passes water; it fills each
   member's waterskins, `--carry N` only to hold fewer days), `firewood` (as often as wanted), `search [--hours N] [--specific]
   [--survey ID] [--stock]` (a hidden throw per hour, an encounter throw first). Dedicated instead of travel:
   `hunt [--dogs N]`, `fish --vessel [--who IDS]` (only from a becalmed or anchored vessel: the rules give no
   fishing on land and the engine refuses it without a ruling), `rest-day [--days N] [--healer ID --patients A,B] [--settlement]` (after a day of travel the
   rest days begin at the next dawn). Animals: fodder and water in `mounts load`; grazing is a dedicated day for most
   animals (`mounts graze`).
3. **Rations**: consumed at the day rollover; to ration, `eat --ration half|none [--who IDS]`, `drink --ration …`. A
   day in a settlement where the party buys its meals: `eat --in-town` (carried supplies untouched; animals stabled;
   the cost goes in the Ledger).
   Hunger, thirst, CON loss and recovery, spoilage, fatigue (six days, forced march, no sleep), natural healing (rest
   days only; +1d3 under a Healing character's care), bed rest, frostbite saves, disease checks, disease stages, mud and snow and
   animals' fodder all run on the rollover; read its lines in the next command's output. A member at CON 0 from hunger
   or thirst is dead: the line asks `death ID --dies --body …`; run it at once. A henchman or hireling joining during
   travel (`party add`) brings his own food and water: the engine warns when he carries less than a day's worth.
   **Disease** (JJ p. 84): on exposure (a diseased bite, a swamp, the seven-day weather chance)
   `acks.sh disease expose ID [--disease NAME] [--type-mod N] --source "…"` rolls the Death save open and, on a
   failure, the disease, its onset and symptom period (hidden). The rollover makes him symptomatic (actor condition,
   incapacitated) and then recovered or dead (asks `death`). `disease diagnose ID --by HEALER --ranks N` (hidden Healing
   throw), `disease cure ID --how "cure disease"` (spell, hired casting via town.md §7), `disease show`.
4. **Camp** at dusk (18:00 with dawn 06:00; `wait --hours N` to get there): `camp --watches "A,B;C;D" [--fire]
   [--blankets IDS] [--armored IDS]` advances the night watch by watch,
   records each member's sleep (8 hours restful), burns firewood (8 st per 4 hours), applies cold and frigid nights,
   and rolls the night encounter check by territory (hidden). A night encounter stops the camp at its hour and names
   who is awake (sleepers start slumbering: `encounter surprise --slumbering IDS`; they cannot evade until woken; with
   no one awake the camp does not see it coming); after it, `camp --resume`. A night encounter timed after a short
   camp waits while the party stays and lapses when it travels on.
5. **Weather for a place not on the route**: `weather --at CC.RR` (or `--climate C --season S`); `--reroll` only by ruling.

## Lost, found, pursued

### A module's own wilderness procedure
A published module that gives its own encounter check and table for some hexes (AX1's Viaspen: 1d6, 6 = the forest table): put it in the hex CSV's `encounters` column (config `hexes.columns.encounters`) as `1d6 6+ <table file>` (acks-table/1, `source.campaign: true`; unlinked rows are the module's scenes, run by you). `travel`, `search` and `hunt` in that hex use it instead of the RR throw and tables; night checks stay RR. When the day ends inside the hex with an encounter pending and the party stops there: `acks.sh encounter start --wild --kind pending`. A deliberate roll on the hex's table: `--kind module`.

- `navigate` shows the believed hex and today's throw; `navigate --found CC.RR` when the party fixes its position
  (doubling back, a landmark it knows). Reaching a settlement fixes it automatically (engine reading); crossing the
  hex where it expected a settlement that is not there makes it aware it is lost (forewarned). A lost party throws
  every day, even on what it believes is a road.
- After an evasion (`evade`), a failed Navigation −4 leaves the party lost and aware. If the monsters track it:
  `pursue --wilderness [--target N] [--ground soft|hard]`; the pursuers close hour by hour during travel and camp and
  the encounter begins again where they catch up (rain or snow loses the trail).

## Hexes, sites and state
- `hex.py HEX` gives the campaign's view (terrain and ACKS type, zone, classification, road, river, site and its prep
  status, climate, neighbours). Entering a site's hex: if `hex.py` reports it **UNPREPPED** and the party approaches,
  stop at the threshold and load unprepped-sites.md. Read a site note only when the party enters its hex or sees it.
- Dynamic lairs (config `paths.wiki_folders.dynamic_lairs`): when a monster encounter is IN LAIR and matches one, the
  party has found that lair; note it in World State and the lair note.
- `acks.sh travel-show` prints the travel state (Judge view).
- `save.sh` runs `xsync.py`: `public.weather`, `public.hex` (the believed hex), `public.trail` (believed hexes) and
  `public.rations` come from the engine; the snapshot refuses a lost party's true hex. World State `## Explored
  hexes` (Hex | Terrain | First visited | Notes): add the true hex only once the party knows where it was.
- Fights: `encounter fight` hands hunger and fatigue to stage 1 as conditions; `encounter end` carries the fight's hp
  back into the travel state (then `heal ID --bed-rest N` from a Mortal Wounds result). Mortal Wounds deadlines
  ("within 1 day") are the Judge's: the engine heals on whole rest days (a day with travel is not one).
- Hidden rolls and the true hex while lost go in the session log's Judge block.
