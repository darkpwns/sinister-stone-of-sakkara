# Unprepped sites (interim, until the prep and stocking steps exist)

Load when the party reaches a site whose notes have no keyed content: `hex.py` reports **UNPREPPED** (no `prepped_by:` and an empty `## Development` section), or a dynamic lair is entered for the first time.

**Stop narrating at the threshold.** Describe only what the characters see from outside (the site note's player-perceivable description, approach, entrances), tell the user in one line that the Judge is preparing the site, build it completely, commit, then continue. **Never improvise a site room by room.**

## Build (JJ Chapter 8, `JJ 08 Dungeons`; all rolls hidden and logged)
Read the site note first: size, challenge level, type, monsters and secrets it already states are fixed facts; the procedure fills only what is missing.
1. **Size** (Step 1, JJ p. 235): from the note (`size:`); small dungeon 2–10 rooms, standard 15–25, large 60–120 per level; a lair is one monster type in its habitat.
2. **Type** (Step 2): from the note, else 1d20 on Select Dungeon Type.
3. **Map** (Step 3): a room list with connections, doors, levels and distances (feet) — enough for theater of the mind. Write it as a plain-text map in the hub.
4. **Stock** (Step 4, JJ p. 236): `acks.sh place --stock N --level L` rolls the Dungeon Stocking table for N rooms (empty / monster / trap / unique) and the treasure of the empty (15%) and trap (30%) rooms on the Unprotected Treasure table; assign each result to a room (hidden). Rooms the note already fixes (the named monster's lair, a ward-shrine) keep their content.
5. **Wandering monsters** (Step 5): the site's own table if the note implies inhabitants; else the JJ Wandering Monsters by Level tables for the dungeon level. Write in the hub's `## Running <site>` section the lines the engine reads (`acks.sh location --hub`): `- Dungeon level: N`, `- Wandering monsters: none` or `- Wandering monsters: 1d6 every 2 turns, 6+` (or the site's own frequency), and, for an own table, `- Encounter table: <file>` (an acks-table/1 JSON next to the hub with `source.campaign: true`, first column the die such as `1d12`, rows `roll range | [[Monster]] (number)`, ranges covering the die once; tools repo README "Site overrides"). Stocking rolls (Step 6) on the JJ tables: `acks.sh encounter start --level N --placed` or `encounter.py dungeon LEVEL --place`.
6. **Monsters** (Step 6): from the Monstrous Manual (`acks.sh monster NAME`), number appearing by the statblock's dungeon encounter, consistent with the site's challenge level; roll their hp now.
7. **Traps** (Step 7) and **unique encounters** (Step 8): from the JJ trap notes (`Trap Level`, `Trap Trigger Mechanisms`, the trap list) and Step 8.
8. **Treasure** (Step 9, JJ pp. 242–243; engine stage 5, `xp-treasure.md` §2): a room whose kind is fixed: `acks.sh place --room empty|trap --level L --label "<key>"`; a monster in its lair: `acks.sh treasure --monster NAME [--groups N] --label "<key>"`; unique rooms: as needed (`treasure --type X`). Each is stored as a hoard `H#` in the adventure ledger (Classic table, Table rules). Write the contents in the room note's `### Treasure` with the hoard id (`H#`) and where it is hidden; answer the engine's Judge items there (spell scroll contents, a treasure map's destination, a misc item's form). Then `acks.sh place --ratio GP XP` for the level (4gp per XP of monsters is the ideal; adjust by hand if far off).
9. **Review** (Step 10) for verisimilitude: does the ecology make sense, where do the inhabitants eat, sleep, go out.

## Write it (module-vault layout)
In a folder named after the site under config `paths.sites_folder`:
- **Hub note:** the existing site note gets `prepped_by: judge-interim` and `prepped: <date>` in its front matter, and its `## Development` section is replaced with:
  - `## Running <site>` — dungeon level, wandering frequency and table, light, alarms, how the inhabitants respond, the plain-text map;
  - `## Contents` — one link per room note, in key order.
- **Room notes:** `<Site> <key> <Name>.md`, front matter `type: room`, `site: "[[<site note>]]"`, `key:`, `prepped_by: judge-interim`; body: what is perceived on entering (2–4 lines), then `### Features`, `### Monsters` (name, number, hp each, tactics), `### Treasure` (contents and where hidden), `### Traps` (trigger, effect, source), `### Checks and saves` (every throw the room can call for, with its rule source), `### Exits`.
- Every note links back to the hub; every `[[link]]` must resolve.
- Hidden rolls of the build go in the session log's Judge block under "Site build: <site>".

Then `save.sh "S## prep <site> (judge-interim)"`, and resume at the threshold.

## build_site.py (engine 7.25 proposals, C4)
`build_site.py SPEC.yaml` runs the build: refuses while Campaign State's session is stale; rolls population (number,
hp, leaders), treasure (`treasure --type`), writes the hub (Running, Rooms, `## Route graph`), room skeletons, the
wandering table from the population, the roster, and a Rulings row; checks every [[link]]. The spec's form is in the
script's help. The Judge then writes the rooms' descriptions.
