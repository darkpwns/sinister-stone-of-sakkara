---
type: campaign-state
tags:
- sakkara/campaign
session: 6
mode: town
location: '[[Turos Tem]]'
adventure: none yet (AX1 The Sinister Stone of Sakkara opens at the first delve or journey)
public:
  date:
    year: ''
    season: spring
    day: 42
  time: '18:01'
  weather: Chilly (57 to 62 F) by day, Chilly (51 to 56 F) at night; overcast; wind moderate
  place: Türos Tem
  hex: '22.20'
  party:
  - name: Callista
    sheet: Characters/callista.json
    role: pc
    hp: 5
    hp_max: 5
    conditions: []
    spells_used: []
    encumbrance_st: 4.667
  - name: Corvus
    sheet: Characters/corvus.json
    role: pc
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 6.333
  - name: Faustina
    sheet: Characters/faustina.json
    role: pc
    hp: 6
    hp_max: 6
    conditions: []
    spells_used: []
    encumbrance_st: 6.448
  - name: Galerius
    sheet: Characters/galerius.json
    role: pc
    hp: 4
    hp_max: 4
    conditions: []
    spells_used: []
    encumbrance_st: 9
  - name: Hrodric
    sheet: Characters/hrodric.json
    role: pc
    hp: 6
    hp_max: 6
    conditions: []
    spells_used: []
    encumbrance_st: 7.833
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
    encumbrance_st: 3.56
  - name: Petra
    sheet: Characters/petra.json
    role: henchman
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
    encumbrance_st: 3.5
  light: lantern (Callista) out; lantern (Callista) out; lantern (Callista) out; lantern (Callista) out
  rations: 'Galerius: food 5 d, water 5.6 d; Faustina: food 5 d, water 0 d; Callista: food 5 d, water 3 d; Corvus: food 5 d, water 0 d; Severina: food 5 d, water 0 d; Marius: food 4 d, water 0 d; Hrodric: food 1 d, water 0 d; Donkey, Draft: fodder 0 st, water 0 st'
  tracker: {}
  threads: []
  trail:
  - '24.21'
  - '22.19'
  - '22.20'
  - '21.21'
  - '21.20'
  - '20.19'
  - '19.19'
  - '20.19'
  - '19.19'
  - '20.19'
  - '21.20'
  - '22.20'
  - '23.21'
  - '22.20'
  - '21.20'
  - '20.19'
  - '19.19'
  - '20.19'
  - '21.20'
  - '22.20'
clock_day: 42
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
