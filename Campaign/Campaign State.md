---
type: campaign-state
tags:
- sakkara/campaign
session: 12
mode: town
location: '[[Turos Tem]]'
adventure: none yet (AX1 The Sinister Stone of Sakkara opens at the first delve or journey)
public:
  date:
    year: ''
    season: spring
    day: 82
  time: '11:36'
  weather: Chilly (57 to 62 F) by day, Chilly (51 to 56 F) at night; mostly cloudy; wind strong
  place: Türos Tem
  hex: '22.20'
  party:
  - name: Callista
    sheet: Characters/callista.json
    role: pc
    hp: 1
    hp_max: 6
    conditions:
    - You feel blessed by your god and recover 1d6 days quicker than you normally would. All negative side effects are removed. (Tampering with Mortality, day 82)
    - 'bed rest: 2 weeks less the blessing 4 days = 10 days, from day 82 to day 92 (incapacitated)'
    spells_used: []
    encumbrance_st: 4.667
  - name: Corvus
    sheet: Characters/corvus.json
    role: pc
    hp: 8
    hp_max: 8
    conditions: []
    spells_used: []
    encumbrance_st: 6.333
  - name: Faustina
    sheet: Characters/faustina.json
    role: pc
    hp: 10
    hp_max: 10
    conditions: []
    spells_used: []
    encumbrance_st: 3.196
  - name: Galerius
    sheet: Characters/galerius.json
    role: pc
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 8
  - name: Hrodric
    sheet: Characters/hrodric.json
    role: pc
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 6.833
  - name: Severina
    sheet: Characters/severina.json
    role: pc
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 5
  - name: Marius
    sheet: Characters/marius.json
    role: henchman
    hp: 4
    hp_max: 4
    conditions: []
    spells_used: []
    encumbrance_st: 5.655
  - name: Varro
    sheet: Characters/varro.json
    role: henchman
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
    encumbrance_st: 7.312
  - name: Quintus
    sheet: Characters/quintus.json
    role: henchman
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 2.525
  - name: Zaira
    sheet: Characters/zaira.json
    role: henchman
    hp: 5
    hp_max: 5
    conditions: []
    spells_used: []
    encumbrance_st: 3.5
  light: lantern (Callista) out; lantern (Callista) out; lantern (Callista) out; lantern (Callista) out; torch (Marius) out; torch (Marius) out
  rations: 'Galerius: food 11 d, water 5.4 d; Faustina: food 11 d, water 0 d; Corvus: food 11 d, water 0 d; Marius: food 8 d, water 0 d; Varro: food 11 d, water 0 d; Hrodric: food 10 d, water 0 d; Quintus: food 7 d, water 0.2 d; Zaira: food 7 d, water 0.2 d; Callista: food 11 d, water 3 d (incapacitated); Donkey, Draft: fodder 0 st, water 0 st'
  tracker: {}
  threads: []
  trail:
  - '23.16'
  - '22.16'
  - '25.19'
  - '24.19'
  - '23.20'
  - '22.20'
  - '21.20'
  - '20.19'
  - '21.20'
  - '20.19'
  - '19.19'
  - '20.19'
  - '21.20'
  - '22.20'
  - '21.20'
  - '20.19'
  - '19.19'
  - '20.19'
  - '21.20'
  - '22.20'
clock_day: 82
---
# Campaign State

Judge-only working file. The `public:` block holds every player-facing transient value; `public.party` is generated
from the actors (`xsync.py`). Permanent values live in the actors in `Characters/`. Keep this file short.

Run 2 (from 2026-11-24): a fresh campaign with new characters, AX1 *The Sinister Stone of Sakkara* then AX2 *Secrets of
the Nethercity* (SOTN). Run 1 (S01-S54, day 1-859) is archived in `Archive/Run 1 (S01-S54)/`: none of its events,
characters, NPC attitudes or factions' standing hold in run 2. Its Rulings carry over as precedents (Rulings.md).

## Table rules

Carried from run 1 (user's choices 2026-11-20 to 2026-11-21) except where marked run 2 (user, 2026-11-24).

- Quest and discovery awards: off; hidden rolls in the Judge block (the module's own XP for an adventure's goal stands: Rulings S06)
- Henchman control: the AI players direct routine actions and combat tactics; the Judge plays personality, morale, obedience
- Party structure: AI party (six AI players; the user watches). Caller Gideon. The Judge plays the AI players by their profiles, `Party/heuristics.md` and the party notes (no party-agent calls; run 1 S06 user decision)
- **Party goal (run 2, user):** the players' primary, standing goal is to found a magical kingdom the like of which the world has not seen since ancient times. They always keep Animal Training (magical beasts as mounts, guards and war-beasts) and the harvesting proficiencies (Alchemy, Animal Husbandry, Healing, Naturalism, Magical Engineering: monster special components) in the party, and every session goal they set advances that goal. They engage factions only when a faction brings them closer to it or costs no recurring obligation (Party/heuristics.md "The kingdom")
- **Combat and factions (run 2, user, S09 rerun):** combat is a failure state: the party draws steel only when the enemy cannot fight back or is plainly outmatched (by the party and its allies); talk, trade, tribute, bribery, deception and alliances come first, and a failed edge means breaking off, not fighting it out. Dungeon and wilderness factions carry no lasting obligation and are used actively (allies, guides, cat's paws, safe passage); settled factions (guilds, temples, legions, cults) make members and are dealt with only for the kingdom. The delve floors are minimums, not a measure of strength (Party/heuristics.md)
- **Character creation (run 2, user): no templates** (RR optional rule: 3d6 × 10 gp, gear bought at the market, proficiencies and spells chosen). The players build as they wish, balancing competence with progress toward the goal
- A PC's death (user, 2026-11-21): the player takes over the dead PC's henchman (RR p. 311 successor, `death <pc> --successor <henchman> --player <p>`); without one, a second-level henchman in the party; otherwise a new 1st-level character with the player's reserve XP. Characters retire only when their injuries make further adventures unlikely
- AI players hire their own henchmen: yes
- Month length: 30 days
- Classes allowed: RR core and RR campaign classes, no supplements
- Adventure: AX1 The Sinister Stone of Sakkara, then AX2 Secrets of the Nethercity (AX3 Borderlands and Cyfaraun as the setting); the campaign ends at a TPK

## Resources

- Possessions, coins, torches, oil and ammunition: the inventory (`acks.sh inv show`)
- Mounts:
- Hirelings (non-henchmen):

## Judge notes (short)
