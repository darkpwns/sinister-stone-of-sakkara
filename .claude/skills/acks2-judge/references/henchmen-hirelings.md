# Henchmen and hirelings (engine stage 3)

Load when the party seeks hirelings, an offer is made, wages fall due, or a hireling's loyalty, obedience or morale is
tested. Every roll and number comes from the engine (`bash $S/acks.sh <command>`; it adds the retinue state
`Campaign/retinue-state.json`, the exploration clock for the day, the roll log and the engine rulings). Do not look these
rules up: the engine names the source of each number. What it leaves to you comes back as `JUDGE:` items. Coverage:
the tools repo's `engine/COVERAGE.md` (Stage 3).

## Setup (once per campaign)
- `acks.sh retinue init --month-days N`: N from Campaign State Table rules "Month length" (settle it first if
  UNSET; record it there and in Rulings).
- `acks.sh retinue employer <PC id>` (the PC's actor id) for each PC who hires (`--domain-ruler` when he rules a
  domain). It prints his henchman limit and the highest henchman level he may hire.

## Recruiting (a week of searching per type)
- Market class from the settlement's market note (`market_class:` in its front matter, config `paths.wiki_folders.markets`); never guess it.
- One search a month for each specification at a market (engine 7.17.4, JJ p. 118): a second `recruit` of the same kind, class and level there in the same month is refused before any fee (`--again` on the Judge's word); a market's totals renew each month. `candidate --level N --class C` writes its draft actor to `Campaign/candidates/` by itself.
- `acks.sh recruit --employer <PC> --market-class V --market "<Place>" --region "<Place>" --kind henchman --level 0 --week 1`
  - mercenaries: `--kind mercenary --type "Light Infantry"`; specialists: `--kind specialist --type "Laborer – Unskilled"`
    (porters for roads and civilized areas are laborers; the rules name no torchbearer: in a dungeon that is a 0th-level
    henchman).
  - a class or proficiency: `--class Fighter [--level N]`, `--general-prof Healing --ranks 2`, `--class-prof Mage:Loremastery`,
    `--commission` (a month's fees, one rarity row more common).
- The fee is an open roll; the engine takes it from the employer's coins (inventory). Availability is hidden. A week's arrivals come back as the players
  would learn of them (`player` in `--json`; name, race, apparent occupation or class, level, wage asked) plus the full
  hidden details. Searching is a week's ancillary activity: `acks.sh wait --days 7` (wage days run inside it).

## Interviews
- `acks.sh candidate <CID> --name "<Name>" --sheet Campaign/candidates/<cid>.json` fills in a candidate and writes a draft
  actor (Judge only), named by the candidate id in lower case (`c3.json`): the hired actor takes the name's id. `--swap A,B` when two attributes suit the occupation better (JJ p. 252: your choice, say so in the
  Judge block). `--kit "Heavy Infantry"` sets a classed candidate's morale once his gear is known.
- Present each as a person: looks, voice, what he says he can do (occupation and its skills). Never show attributes, hp,
  age dice, morale or proficiency ranks unless the party tests them; loyalty and morale scores are never shown.
- Work through the `JUDGE:` items: free proficiency slots, equipment (the rules give no list), alignment, class choices.
  Once hired he is an inventory holder (the engine registers him): his equipment goes in with
  `acks.sh inv add <MID> "<item>" N --cause "equipment on hiring"`, or the employer gives it (`inv give`). Mercenaries
  come with their troop type's arms and armor plus the kit the rules list for all mercenaries (`Mercenaries (Hirelings)`:
  tunic, cloak, sandals, backpack, laborer's tools, stakes and mallet, mess kit, small tent, 2 blankets, a waterskin).

## The offer
- The player states the terms: wage (the table wage is the asking wage), share (henchmen: half), signing bonus, anything else.
- `acks.sh offer <CID> --employer <PC> --wage N [--signing week|month|year] [--prof diplomacy] [--region "<Place>"] [--mod "NAME:+1"]`
  (mercenaries and specialists: `--count N` of the pool; one roll for the group offered, reading `hire.group_offer`)
  - `--prof`: the approach the player takes (diplomacy, intimidation or seduction, and mystic aura); the engine checks the
    employer's actor. Anything the rules leave to you (more pay than the table wage, reputation, a shared language) is a named `--mod`,
    and a ruling if it may recur.
  - Try Again: only a better offer gets another roll (`--sweetened "what was added"`). Refusal: another party member may
    try (cumulative −1). Refuse and slander: −1 to that adventurer's reaction rolls in that region, recorded by the engine;
    add `--jmod "slandered (RR p. 162):-1"` to his stage 2 `reaction` rolls there.
  - Monsters: `offer --monster NAME --reaction neutral|indifferent|friendly` at the start of an encounter, or `--captured`
    after a fight (Irrefusable Offer; Betrayal and Escape look like acceptance to the players).
- The roll is hidden. Narrate the answer.

## Hiring and leaving
- `acks.sh hire <CID> --employer <PC> --publish-to Characters/<id>.json [--count N]`: the engine refuses past the henchman
  limit or the level limit (the rules: hiring past the limit costs an existing henchman; `--accept-loss <MID>` only if the
  player insists). The draft actor moves to `Characters/` (published as the player view; its `judge` block never is); his
  member id is the actor id. The
  first month's wage falls due today (reading `wage.timing`): pay it at once (`wages pay <MID> --payer <PC>`) unless the employer
  refuses; an unpaid wage is a calamity at the next day rollover (a hidden loyalty roll).
- Then: the wage to the Ledger, the hiring roll to the Judge block; `save.sh` (it lists him in `public.party`).
- `dismiss <MID> --why "…"` (a death on an adventure: `acks.sh death <ID> --dies` does it); `transfer <MID> --to <PC>` (recalculated, and a calamity).
- When a henchman leaves or dies: `git mv Characters/<id>.json Characters/former/` (still an actor folder; not published,
  and out of `public.party` at the next save).

## Wages
- `acks.sh wages show` (due by date), `acks.sh wages pay <MID> --payer <PC> [--months N | --all]` when the employer pays (from his coins in the inventory).
- A henchman's monthly wage follows his level (engine 7.17.3, RR p. 168): when he gains a level (`level-up --member`, `advance-0th --member`) a table wage becomes the new level's from his next wage day, said in the line; agreed terms off the table are left alone with a JUDGE line. `retinue set ID wage=N --cause "…"` sets an agreed wage (`wage` is `wage_gp`; unknown keys are refused; the cause and day go into the member's history, engine 7.18.11). A hireling group's losses: `retinue lose ID N --cause "…"` (the count falls, wages follow; the last of them ends the group), never `retinue set ID count=N`. A wage is due on the hiring day + k × the month (`wages show`: "next due day N"); "paid through day N−1" is not the due day.
- Wage days run on every day rollover (`turn`, `rest`, `wait`): a wage still unpaid at the end of its day is missed — a
  calamity: loyalty −1 and a hidden loyalty roll, applied by the engine. Away from civilization the rule is the same.

## Loyalty, obedience, morale
- Calamities: `acks.sh loyalty <MID> --trigger calamity --why "curse"`; a level gained: `--trigger level --to-level N`;
  a henchman who thinks himself above his employer: `--trigger outclassed --levels N`; permanent wounds:
  `--event wound-grievous` (and `--cured` later). After a fight: `acks.sh loyalty --pending` rolls the 0-hp calamities the
  round end queued. Hostility or Resignation: he leaves (narrate it; move his actor to `Characters/former/`).
- Risky orders (new dungeon, unexplored hexes, notably dangerous task, overtime): `acks.sh obey <MID> --order "…"
  --with employer|adventurer|hirelings|alone --risk small|more|great|extraordinary [--customary] [--henchmen-lost]
  [--kind dungeon --adventure "<site>"]`. Refuses: if the employer insists, `--insist`. Begrudging on a journey or dungeon:
  −1 to that adventure's loyalty rolls until `acks.sh retinue end-adventure`.
- In a fight, add henchmen to the combat state by their actor ids (`state add <id> --side party`); the round end rolls their morale when a trigger is met
  (1/3 hp lost, 1/3 of the party felled, the employer felled) and applies the result to the henchman alone.
- Henchmen are independent people. Table rules (Henchman control) say how much the player directs; by default the
  player directs routine actions and combat tactics, you decide personality, speech, morale, obedience and what they do
  when the employer is absent or unconscious.

## NPC parties
- A wandering "NPC Party (Lvl N)" entry: `acks.sh npc-party --from-encounter` (hidden): classes, levels, alignment;
  `--henchmen 2` replaces NPC 2 by two henchmen two levels lower; `--to-state` adds them to the combat state (set AC,
  weapons and morale with `state set`). In a settlement: `--settlement-class V`; wilderness: `--nearest-dungeon-max N
  --wilderness` (mounts). Treasure: the Treasure Type is reported (rolled with stage 5, or by lookup until then).
- One NPC's class: `acks.sh npc-class [--table party|building]` (hidden): a roll on the NPC Class table (JJ p. 259) or
  the building occupants' copy (JJ p. 230), named as the campaign names the class.

## State
Retinue state `Campaign/retinue-state.json` (Judge only): the only record of loyalty and morale (`retinue show`). Draft
actors in `Campaign/candidates/` (Judge only). On hiring: `Characters/<id>.json`, Ledger wage line, Judge block. `save.sh` after each hiring, payment or loyalty change.
