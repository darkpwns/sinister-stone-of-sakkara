# Combat (theater of the mind) — with the rules engine

Load when a fight starts. The engine (`bash $S/acks.sh CMD …`, config `tools`) decides attack throws, damage,
saves, proficiency throws, initiative, the round sequence, morale and Mortal Wounds, and names the source of every
number. Do not look those up. Look up (rules lookup skill) only what the engine's coverage table (config
`tools.coverage`) leaves to lookup: a spell's or monster ability's effect, an unusual maneuver, positions it is not
told. If setup printed `engine: UNAVAILABLE`, run the fight by Judge's Screen §2 with `dice.py` (the old procedure is
in git history of this file).

Every engine command prints one line. Parts marked `[H]` are Judge-only (monster rolls, monster hp, morale): they go
in the Judge block, never to the player. Lines with `| JUDGE:` list what the engine left to you; `| NOTE:` lists
actor differences and readings applied (book contradictions, rulings). `--json` gives every number with its source.

## Start of the fight
1. `acks.sh state init` (creates the config `tools.combat_state` file; add `--group-initiative` to roll once per
   group of identical monsters).
2. Add every combatant once:
   - PCs and henchmen: `acks.sh state add <id> --side party` (the actor id; it starts at the actor's current hp,
     `state.hp`; `--ac-mode no_shield` if no shield is in hand).
   - A named monster or NPC with its own actor (`Actors/monsters/`, `Actors/npc/`; an NPC's is made on demand,
     characters.md → NPCs): `acks.sh state add <id> --side foe --group <g> --perceived "…"`.
   - Other monsters: `acks.sh state add <id> --monster "<MM note name>" --group <g> --perceived "<what the party sees>"`
     (hp rolled hidden). The line lists any field the statblock leaves as a choice (`JUDGE: needs Judge: ac …`):
     set it with `acks.sh state set <id> ac=5` (also `hd`, `morale`, `save=F3`, `attack_throw`, `weapon=spear`,
     `size`, `armor_ac`, `running`). Leaders with their own statblock line in the
     entry: `--set ac=… --set hd=… --set attack_throw=…`. A creature with other Hit Dice than its statblock's: give
     them at `state add … --hd N` (hp rolled for them); `state set <id> hd=N` later keeps the hp unless
     `--reroll-hp` (damage taken is kept). `state set <id> perceived="…"` renames it in every line (engine 7.18.4).
   - Immunities and resistances load with the monster from its bestiary note (engine 6.20.0: typed records, mundane
     or extraordinary, with flaws such as silver; effect immunities for saves): do not read the note for them. Only a
     `needs Judge: defenses: …` line asks you (a dragon's picks, a lycanthrope's form, an elemental's element, an
     exception such as "except from the warder"). For that rare case: `acks.sh state set <id> immune=fire:mundane,all:mundane
     resist=fire:extraordinary flaw=silver immune_effects=fear` (tier mundane|extraordinary|both; no tier = both, which
     is what the old `resist=fire` means). `acks.sh monster "<name>"` shows the records.
   - Use perceived names in `--perceived`: open-roll labels use them and reach the snapshot. `acks.sh` refuses a foe
     without one (`state add` of a non-party combatant, `encounter fight`, `npc-party --to-state`).
3. Positions: `acks.sh state distance <a> <b> <feet>` (opening distance from the encounter roll),
   `state engage <a> <b>`, cover by argument at the attack. Surprised combatants: `state cond <id> surprised`.

## Each round
1. Declarations, then initiative: `acks.sh round-start [--declare <id>:spell|retreat|withdraw …] [--mod <id>:<name>:+N]`.
   It gives the order. Ties name who chooses. Show the party's initiative rolls; give the monsters only as the order.
2. Count down: `acks.sh round-next` gives the next combatant to act (it ends disordered/charging/defending and
   readied actions at their initiative, and faltering when unengaged). Then resolve that combatant's actions:
   - **Attack:** `acks.sh attack <a> <t> [--routine N --attack N] [--charge|--countercharge|--set-vs-charge]
     [--range short|medium|long] [--cover waist|chest|narrow] [--flank|--rear] [--higher] [--maneuver M] [--ambush]
     [--through-melee] [--dual dual|specialized] [--mod "<proficiency or item>:+N"]`. Damage follows
     on a hit. A PC's or henchman's weapon is the one in hand in the inventory, with its grip (one or two hands): no
     `--weapon`, `--two-handed` or `--type`. `--weapon <item or id>` only switches to the other weapon in hand
     (`--weapon unarmed` for a punch); a weapon not in hand, no weapon in hand, or `--two-handed` against the grip is
     refused. The damage line names its types and tier (mundane, or extraordinary for a magic weapon or a monster's
     extraordinary attack) and the target's records apply by themselves (RR p. 300: reduced only if protected against
     every type). Monsters fighting by weapon still take `--weapon NAME`. `--extraordinary`: an effect the engine does
     not model makes this attack extraordinary (your call).
   - **Grip and drawing:** `acks.sh inv wield <id> <item> [--two-handed] [--hand right|left]` takes a weapon in hand;
     `acks.sh inv grip <id> <item> one|two --cause "…"` changes the grip (a shield or anything else in the other hand
     refuses two hands; a large weapon is always two-handed; a lance on foot is two-handed with its die one size
     smaller, `grip … one --cause "mounted"` when mounted). Putting it away: `inv move <id> <item> --slot belt`. A missile attack uses one of the attacker's arrows, bolts or sling stones from the inventory (`--ammo "silver arrow"` to choose; hit: destroyed, miss: on the ground at the site), a thrown weapon lands at the site, and a lance, spear or polearm breaks on a natural 1 (`inventory.md`). The engine refuses illegal attacks (charge when engaged at round start, missiles at an engaging foe or
     at foes engaged with allies without Precise Shooting, beyond long range, conditions that forbid attacking).
     A monster's multiple attacks: one call per attack (`--attack 0`, `--attack 1`, …).
   - **Cleave:** when the line says "may cleave", attack another foe in reach with `--cleave` (and the same
     `--charge`/`--ambush` flags if the bonus continues).
   - **Backstab (engine 7.15.0, automatic):** a thief (any class with a Backstab column) attacking a vulnerable target
     (surprised, cowering, helpless, paralyzed, slumbering, prone, ... or `--rear`) backstabs by himself: +4 and the
     extra dice of his level, in melee or with a missile at short range. A foe already engaged by two or more of his
     allies is taken from the rear unless `--front` (corridor two abreast, thief pinned). Never pass `--ambush` or
     `--extra-dice backstab` for him; `--no-backstab` only when he chooses not to. Put the thief where the rear is: let
     the front line engage first, then send him in (the line says "takes the rear").
   - **Coup de grace:** a helpless foe (slumbering, unconscious, paralyzed) and an attacker not engaged: `acks.sh attack <a> <t> --coup-de-grace` slays it outright (RR p. 511). A sneaking thief against a sleeping monster is the classic case.
   - **Sweep:** `acks.sh sweep <a> <t1> <t2> …`.
   - **Other damage** (spells, traps, falls, oil): `acks.sh damage <t> --dice XdY --type T [--extraordinary|--mundane]
     [--half]` (spells: `--extraordinary`; refused without a tier when the target's protection differs by tier).
   - **Damage set by hand** (an area spell, a fall): `acks.sh state set <id> hp=N type=fire` (or `--dmg-type fire`)
     records the type for `state end`'s Mortal Wounds (engine 7.18.10; damage from `attack` and `damage --type`
     records itself). **Cures in a fight:** `acks.sh state set <id> hp=N` (a cure that brings a dying combatant to 1 hp or more ends the dying timer; engine 7.14.0). A rebuked or frightened foe that is engaged (`state engage`) cowers. Berserkergang: `state cond <id> berserk` (`enraged` is accepted). A power's dice of its own type: `attack … --extra-dice "Striking:1d6:luminous"`; a damage bonus (Vigor, Ogre Strength): `--damage-mod "Vigor:+2"`. A mummy's slam puts mummy rot on the combatant: copy it to the actor after the fight. A character's worn protections (a ring) are the actor's `defenses` (`actor set <id> defenses '{"resist": "fire:both", "source": "…"}' --cause …`): `state add` applies them.
   - **Saves:** `acks.sh save <id> paralysis|death|blast|implements|spells [--vs-size <id>] [--cover …] [--vs-type T
     [--extraordinary|--mundane]] [--vs-effect enchantment|fear|"death effects"|disease|…] [--vs-fear] [--vs-enemy]`
     (a maneuver's save, a spell's save, the perils of cowardice; immunity to the type or effect succeeds by itself).
   - **Defend:** `acks.sh state defend <defender> [<protected>] [--note shield]`.
   - **Conditions:** `acks.sh state cond <id> <condition> [--rounds N]` / `uncond`.
   - **Moves:** you decide what the distance allows (combat speed, running speed; Judge's Screen §4 Movement in the
     wilderness), then `state distance` / `state engage` / `state disengage`. A move the distance does not allow
     does not happen.
   - **Proficiency throws in combat:** `acks.sh throw <id> --adventuring dungeonbashing` (or `--prof`, `--guideline`).
3. End of round: `acks.sh round-end [--party-fled] [--cornered <group>] [--mod <group>:<name>:+N]`. It rolls morale
   (hidden) exactly where the rules require it, applies the result (frightened, cowering, faltering, pursuit state),
   counts down durations and kills a combatant dying "within 1 round" who was not healed. Narrate the behaviour.
   Morale modifiers from the monster entry (leader alive, war drums) go in `--mod`.

## Missiles, flasks, routines, leaving a fight (engine 7.17.5)
- **Distances first.** Record `state distance A B FT` (or `state engage A B`) for every foe when the fight starts. In
  a fight that records distances, a melee attack on a target with no distance recorded is noted ("taken as in reach")
  or refused when the attacker's recorded distances to that group are all beyond reach. `--range` belongs to missile
  attacks only; a sword cannot be made a missile with `--kind missile`.
- **Monsters with weapons**: `attack g1 vettius --weapon javelin` (or `state set g1 weapon=javelin`) reads the weapon's
  row: thrown or shot at range with the band from the recorded distance (medium −2, long −5, beyond long refused), no
  engagement from a missile. `--weapon` on a monster whose damage is not "by weapon" is refused.
- **A multi-attack routine**: `--attack N` picks the Nth attack and its own damage entry (a catfish's fourth feeler);
  a statblock whose entries do not line up is refused before the roll: `--damage-entry N`, or `--no-damage` and
  `damage --dice`.
- **Thrown flasks and torches** (RR p. 298): `attack A T --throw oil|"holy water"|torch [--range short|medium|long]`
  (`--chaotic-enchanted yes|no` for holy water, which harms only chaotic enchanted creatures; `--unlit` for unlit oil).
  The flask comes from wherever A carries it and is used up; −4 at an engaged target; a direct hit burns now and
  again at A's count next round (`round-next` applies it); splash, scatter (direction and distance rolled) and who
  stands within 5' are printed for you to apply; no STR, class or backstab bonus; a natural 1 burns the thrower.
- **Ammunition**: `--ammo "silver arrow"` counts as silver against a creature with that flaw; a magic arrow or bolt:
  `--ammo-magic N` (higher bonus to hit, both to damage, extraordinary; TT p. 251) and take one from its lot by hand.
  A NOTE names a magic bow carried but not in hand: `inv wield` it before the fight.
- **Leaving a fight**: `state remove ID --why left|absent|fled` (a party member who walks out or was never there is
  `left`/`absent`: no casualty for anyone's morale); `state return ID` brings him back. `state set ID status=` takes
  only the known statuses.

## Wards and auras (engine 7.17.6)
- **A ward** (Holy Circle, RR p. 225; an item or power that works like it): once the combat state exists, `acks.sh
  state ward add <bearer> --name "<what>" --within party --evil foes [--fall creature] --source "<rule or ruling>"`.
  From then on the engine does it: an enchanted creature (undead, construct, incarnation; a summoned one: `state set
  ID enchanted=1`) cannot make a melee attack on anyone within (refused before any roll); an attack from within on a
  blocked creature drops the barrier (the whole barrier by the RR; only against that creature with `--fall
  creature`, a campaign's ruling named in `--source`); evil foes meet +1 AC and `save ID CAT --by <foe>` gets +1.
  A spell from within resolved with `damage T --dice`: `state ward fall <bearer> T` (the JUDGE line says so).
  `state ward close <bearer> [T]` when the barrier closes again (next turn); `round-start` lists what has fallen;
  `state ward out <bearer> ID` for someone who steps outside. Rebuking does not drop the barrier.
- **An aura** with a save at each initiative (whispers, a stench, a gaze): `acks.sh state aura add <name> --sources
  ID,ID --radius FT --save death --per-extra -1 --fail <condition> [--while-failed "<what happens each initiative>"]
  --source "<module page>"`. `round-next` then rolls the save at the start of each creature's own initiative when it
  is within the radius of a source by the recorded distances (or on the list: `state aura hears <name> ID,…`): never
  roll these by hand, and record distances so the engine knows who is in range.

## Wounds
- A PC or henchman at 0 hp or less is unconscious (the line says so; a henchman at 0 hp also needs a loyalty roll
  for a calamity — henchmen-hirelings.md).
- Treat Injury (combat action) or a cure spell: `acks.sh mortal-wounds <id> [--healing-magic <spell level>]
  [--healing-ranks N] [--horsetail] [--laying-on-hands <level>] [--heavy-helm|--no-heavy-helm]`; the elapsed time
  comes from the round it fell (or `--elapsed 3t|2h|1d` outside the fight; `--untreated-24h`). Open roll. The line
  gives the condition and the permanent wound; record them in the actor: `actor set <id> state.conditions "[…]"
  --cause …` (scarring and lasting wounds also in his prose note).

## The tracker for the player and the Judge block
- Player half (`public.tracker` in Campaign State): `acks.sh state show --player` prints exactly what the
  characters perceive (perceived names, party hp, engagements, distances, initiative order). Copy those fields.
- Judge half: the engine's state file is the tracker (monster identities, hp, morale state). In the session log's
  collapsed Judge block, put the `[H]` lines of the fight (or `dice.py --dump hidden`, which includes engine rolls).

## Rulings that must stay consistent
The first time in the campaign a fight needs either of these, look for a rule first (`rl_find.sh`), then rule, and
append the ruling to Rulings.md:
- **Area effects in the mind's eye:** how many creatures a blast, cone or line catches given the distances and formation.
- **How many attackers can reach one target:** the optional *Engagement by Smaller or Larger Creatures* table
  (the engine has it as data, not enforced); state whether it is used and the limit for same-size attackers.

## End of the fight
Foes at 0 hp are unconscious and possibly slain (RR p. 302). While the fight lasts the party may slay a helpless one
(coup de grace) or treat one (`mortal-wounds <id> --elapsed …`, e.g. to take a prisoner). When it ends, first
`acks.sh state end` (a piercing-and-slashing weapon's table is a hidden 1d2; `--type <id>:<type>` only for other mixes, such as fire and bludgeoning): every foe still unconscious and
untouched rolls Mortal Wounds at once, hidden, as untreated for 24 hours (Rulings 2026-11-19). Slain, or **recovering**
at 1 hp with its wound and bed rest: note each survivor in World State `## Dungeons and lairs` (where it lies, the
wound, the bed rest; the party believes it dead) and play it from there. Then:
`state end` also does the bookkeeping (engine 7.17.0): the foes destroyed, slain or dead are recorded in the open
adventure's ledger with their XP (hidden; by the Hit Dice the monster actually had), and each party combatant's hp is
written to his actor with the fight as its cause. Never type `recover --monster` or copy hp by hand after it. What
stays yours is on its JUDGE line: foes that fled, surrendered or were captured (the exact `recover --monster …
--how outsmarted|captured` command is printed: outsmarted and captured monsters grant XP, RR pp. 310-311), and the
conditions the fight put on a character that outlast it (mummy rot, a wound): `actor set <id> state.conditions`.
`--no-xp` when no XP is due. Then: monsters slain or fled → World State; clear `public.tracker`; delete the combat
state file (`git rm` if committed); `save.sh`.

**Surprise** lasts through round 1 (engine 7.17.0): the surprised keep the condition until round 2's `round-start`,
`round-next` says they cannot act, and `attack`, `sweep`, `rebuke` refuse them. **Rebuke** (7.17.0): its line states the
2d6 Hit Dice and who was affected; Hit Dice go to undead not yet rebuked first; an undead with no rebuking row
refuses the rebuke before any roll (`state set ID rebuke_as=TYPE`, or `rebuke_as=none` to leave it out);
`rebuke ID --cornered ID,…` for undead that cannot flee (they cower). Undead at 0 hp are destroyed, also when hp is
set by `state set ID hp=N`. **Step the round with `round-next`** and act for the combatant it names: the lessons index
reminds when an action is taken out of its count.
