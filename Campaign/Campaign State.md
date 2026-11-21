---
type: campaign-state
tags:
- sakkara/campaign
session: 7
mode: dungeon
location: '[[Level 1 - Buried Temple]]'
adventure: AX1 The Sinister Stone of Sakkara
public:
  date:
    year: ''
    season: spring
    day: 142
  time: '11:00'
  weather: Hot (87 to 90 F) by day, Warm (83 to 86 F) at night; drizzle; wind moderate (drizzly)
  place: Buried Temple
  hex: '10.07'
  party:
  - name: Aulus
    sheet: Characters/aulus.json
    role: pc
    hp: 14
    hp_max: 14
    conditions: []
    spells_used: []
    encumbrance_st: 9.307
  - name: Lucilla
    sheet: Characters/lucilla.json
    role: pc
    hp: 10
    hp_max: 10
    conditions:
    - lost an eye and an ear (half her face mauled)
    - minor scarring (fang mark on the hand)
    spells_used: []
    encumbrance_st: 8.87
  - name: Sabina
    sheet: Characters/sabina.json
    role: pc
    hp: 14
    hp_max: 14
    conditions: []
    spells_used: []
    encumbrance_st: 8.356
  - name: Tarq
    sheet: Characters/tarq.json
    role: pc
    hp: 6
    hp_max: 6
    conditions:
    - raspy voice (-2 to speech throws)
    - minor scarring (fang marks on the neck)
    spells_used: []
    encumbrance_st: 9.163
  - name: Vettius
    sheet: Characters/vettius.json
    role: pc
    hp: 11
    hp_max: 11
    conditions: []
    spells_used: []
    encumbrance_st: 9.008
  - name: Marcia
    sheet: Characters/marcia.json
    role: pc
    hp: 8
    hp_max: 8
    conditions: []
    spells_used:
    - Fan of Flames
    encumbrance_st: 4.471
  - name: Hesper
    sheet: Characters/hesper.json
    role: henchman
    hp: 5
    hp_max: 5
    conditions: []
    spells_used: []
    encumbrance_st: 5.261
  - name: Thorwell
    sheet: Characters/thorwell.json
    role: henchman
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 3.751
  - name: Quintus the Rager
    sheet: Characters/quintus-the-rager.json
    role: henchman
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
  - name: Vestus the Unlikely
    sheet: Characters/vestus-the-unlikely.json
    role: henchman
    hp: 3
    hp_max: 3
    conditions: []
    spells_used:
    - Magic Missile
  - name: Zaira the Beautiful
    sheet: Characters/zaira-the-beautiful.json
    role: henchman
    hp: 5
    hp_max: 5
    conditions:
    - one leg torn off (crutch required, movement -30 feet, DEX reduced by 1/3 for AC)
    spells_used: []
  light: torch (Lucilla) out; torch (Vettius) out; torch (hesper) out; torch (hesper) out; torch (gallus) out; torch (gallus) out; torch (Lucilla) out; torch (Vettius) out; torch (Priestess Genelen) 6 turns left
  rations: 'Aulus: food 4 d, water 0.6 d; Sabina: food 4 d, water 1.2 d; Tarq: food 4 d, water 1 d; Lucilla: food 3.5 d, water 1 d; Vettius: food 4 d, water 1 d; Marcia: food 4 d, water 1.4 d; Thorwell: food 4.5 d, water 1 d; Quintus the Rager: food 4.5 d, water 1 d; Vestus the Unlikely: food 4.5 d, water 1 d; Priestess Genelen: food 4.5 d, water 1 d; Donkey, Draft: fodder 0 st, water 0 st'
  tracker: {}
  threads: []
  trail:
  - '12.07'
  - '13.08'
  - '12.07'
  - '11.07'
  - '11.08'
  - '10.07'
  - '11.07'
  - '12.07'
  - '13.08'
  - '12.08'
  - '13.08'
  - '12.07'
  - '11.07'
  - '10.07'
  - '11.07'
  - '12.07'
  - '13.08'
  - '12.07'
  - '11.07'
  - '10.07'
clock_day: 142
---
# Campaign State

Judge-only working file. The `public:` block holds every player-facing transient value; `public.party` is generated
from the actors (`xsync.py`). Permanent values live in the actors in `Characters/`. Keep this file short.

## Table rules

Set 2026-11-20 by the user's playtest brief (user away; recommended options otherwise).

- Quest and discovery awards: off; hidden rolls in the Judge block
- Henchman control: the AI players direct routine actions and combat tactics; the Judge plays personality, morale, obedience
- Party structure: AI party (six AI players; the user watches). Caller Gideon. Dead PCs replaced by new 1st-level PCs.
- Character creation: templates (RR default)
- AI players hire their own henchmen: yes
- Month length: 30 days
- Classes allowed: RR core and campaign classes, no supplements
- Adventure: AX1 The Sinister Stone of Sakkara (Auran Empire, as printed); the test ends at a TPK

## Resources

- Possessions, coins, torches, oil and ammunition: the inventory (`acks.sh inv show`)
- Mounts:
- Hirelings (non-henchmen):

## Judge notes (short)
