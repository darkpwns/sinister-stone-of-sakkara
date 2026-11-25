# Monster special components (engine 7.21)

Load when a slain monster's parts are identified, harvested, preserved, sold or used for magic research (MM pp.
371-387). Never harvest by hand (S52: fireballed medusae were harvested whole).

- **Show**: `acks.sh components show "<monster>"`: its components with value, weight, kind and associated effects, the
  type's default effects, the proficiency bones/coverings/internal organs need, and every difference from its
  statblock's `spoils` (`components crosscheck` lists them all). Monstrosities and dragons are read from their notes
  (not every row confirmed in print): the line says so.
- **Identify** (1 turn each): `components identify "<monster>" --by ID --prof Alchemy|Naturalism|Magical Engineering
  |Loremastery [--target N]` (one attempt per proficiency until a level or rank is gained; a natural 20 on the hidden
  1d20 asks for an unusual component), or `--discern --target N` (a magic research throw, again each turn). A success is
  recorded in the adventure ledger; `harvest` refuses an unidentified monster unless `--known`.
- **Harvest**: `acks.sh harvest ID --by WHO [--component NAME] [--moved FT] [--great-souled]` on a slain foe still in
  the combat state (it reads what damaged it: area effects, blunt weapons, poison; `state set ID
  damaged_by=disintegration`), or `harvest LABEL --monster "<name>" --damaged-by area,blunt --by WHO` afterwards. Ruined
  components are named; appendages, exterior organs and remnants by anyone in 1 turn; bones, coverings and internal
  organs only with the type's prerequisite ranks, 1 turn per 100gp, with the craftsman's tools (asked). Each component
  takes its metamphora (5gp, 1 st per 60gp) from the harvester's inventory (`inv buy WHO "Metamphora (60gp)" N`);
  without them it spoils within a turn (its lot worthless). The clock advances by the turns. The results are goods
  lots carrying the component (monster, kind, effects).
- **Use and sale**: `sell L#` (market class and demand, sale XP as treasure); `components research "<effect>"` lists
  the lots whose effects match and their value toward a magic item's component cost.
- Not in the engine: mundane parts (pelts, horns, feathers, venoms: the tables' notes), the optional permanent-wounds
  check (`components.permanent_wounds` is off), the hunter henchman's fortnightly hunts (Rulings S47: run `harvest` on
  what he kills).

## Engine 7.24 (Sakkara run 2 requests)
- A monster with no row on its type's table (gnoll, stirge, ogre): its components are worth its XP value (MM p. 372):
  the statblock's spoils where it has them (the ogre's knucklebones, 140gp), else one part the Judge names: `harvest
  BODY --by ID --component "canine teeth" --kind "canine teeth:appendage"`. Fewer metamphora than the value needs keep
  60gp each; the rest spoils (Rulings R2 S05, R2 S13). No more `recover --goods` plus `inv remove`.
