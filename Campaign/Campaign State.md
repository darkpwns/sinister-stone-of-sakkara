---
type: campaign-state
tags:
- sakkara/campaign
session: 15
mode: dungeon
location: '[[Level 2 - Catacombs]] 38-39 (the Inner Fane)'
adventure: A11 The Lady Below (Buried Temple, level 2) (open)
public:
  date:
    year: ''
    season: summer
    day: 132
  time: 09:16
  weather: Balmy (72 to 74 F) by day, Brisk (63 to 67 F) at night; clear; wind still
  place: Türos Tem
  hex: '20.19'
  party:
  - name: Callista
    sheet: Characters/callista.json
    role: pc
    hp: 8
    hp_max: 8
    conditions: []
    spells_used:
    - Slumber
    - Slumber
    encumbrance_st: 5.703
  - name: Corvus
    sheet: Characters/corvus.json
    role: pc
    hp: 16
    hp_max: 16
    conditions: []
    spells_used: []
    encumbrance_st: 7.203
  - name: Faustina
    sheet: Characters/faustina.json
    role: pc
    hp: 15
    hp_max: 15
    conditions: []
    spells_used:
    - Halt Humanoids
    - Halt Humanoids
    encumbrance_st: 4.512
  - name: Galerius
    sheet: Characters/galerius.json
    role: pc
    hp: 20
    hp_max: 20
    conditions:
    - 'gruesome scarring: nose flattened, cheek crushed, ear cauliflowered (day 87)'
    spells_used: []
    encumbrance_st: 9.036
  - name: Hrodric
    sheet: Characters/hrodric.json
    role: pc
    hp: 17
    hp_max: 17
    conditions: []
    spells_used:
    - Holy Blessing
    encumbrance_st: 5.869
  - name: Severina
    sheet: Characters/severina.json
    role: pc
    hp: 11
    hp_max: 11
    conditions: []
    spells_used: []
    encumbrance_st: 5.036
  - name: Marius
    sheet: Characters/marius.json
    role: henchman
    hp: 2
    hp_max: 6
    conditions: []
    spells_used: []
    encumbrance_st: 5.364
  - name: Varro
    sheet: Characters/varro.json
    role: henchman
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
    encumbrance_st: 9.021
  - name: Quintus
    sheet: Characters/quintus.json
    role: henchman
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 5.068
  - name: Zaira
    sheet: Characters/zaira.json
    role: henchman
    hp: 5
    hp_max: 5
    conditions: []
    spells_used: []
    encumbrance_st: 5.209
  light: lantern (Callista) out; lantern (Callista) out; lantern (Callista) out; lantern (Callista) out; torch (Marius) out; torch (Marius) out; torch (Marius) out; torch (Corvus) out; torch (Corvus) out; lantern (Callista) out; lantern (Callista) out; lantern (Callista) out; lantern (Callista) out; lantern (Callista) 22 turns 6 rounds left
  rations: 'Galerius: food 7 d, water 1 d; Faustina: food 7 d, water 1 d; Callista: food 7 d, water 1 d; Corvus: food 7 d, water 1 d; Varro: food 7 d, water 1 d; Hrodric: food 7 d, water 1 d; Quintus: food 7 d, water 1 d; Zaira: food 13 d, water 1 d; Severina: food 7 d, water 1 d; Marius: food 12 d, water 1 d'
  tracker: {}
  threads: []
  trail:
  - '22.21'
  - '22.20'
  - '21.20'
  - '22.20'
  - '21.20'
  - '20.19'
  - '19.19'
  - '20.19'
  - '21.20'
  - '21.21'
  - '22.20'
  - '21.20'
  - '20.19'
  - '19.19'
  - '20.19'
  - '21.20'
  - '22.20'
  - '21.21'
  - '21.20'
  - '20.19'
clock_day: 132
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
- **Travel until the temple is done (run 2, user, S12 rewind):** no wilderness travel except between Türos Tem and the Buried Temple (the corridor 22.20, 21.20, 20.19, 19.19) until the Buried Temple is complete (AX1's goal: the Stone of Sakkara destroyed and the Lady Below dealt with). Pilgrimages, scouting trips and other sites wait; a party that strays off the corridor while lost makes its way back to it
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
