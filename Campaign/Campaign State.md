---
type: campaign-state
tags:
- sakkara/campaign
session: 6
mode: dungeon
location: '[[Level 1 - Buried Temple]]'
adventure: AX1 The Sinister Stone of Sakkara
public:
  date:
    year: ''
    season: spring
    day: 122
  time: 06:00
  weather: Brisk (63 to 67 F) by day, Chilly (57 to 62 F) at night; overcast; wind moderate
  place: Buried Temple
  hex: '13.08'
  party:
  - name: Aulus
    sheet: Characters/aulus.json
    role: pc
    hp: 14
    hp_max: 14
    conditions: []
    spells_used: []
    encumbrance_st: 9.284
  - name: Lucilla
    sheet: Characters/lucilla.json
    role: pc
    hp: 10
    hp_max: 10
    conditions:
    - lost an eye and an ear (half her face mauled)
    spells_used: []
    encumbrance_st: 9.376
  - name: Sabina
    sheet: Characters/sabina.json
    role: pc
    hp: 14
    hp_max: 14
    conditions: []
    spells_used: []
    encumbrance_st: 8.306
  - name: Tarq
    sheet: Characters/tarq.json
    role: pc
    hp: 6
    hp_max: 6
    conditions:
    - raspy voice (-2 to speech throws)
    spells_used: []
    encumbrance_st: 8.79
  - name: Vettius
    sheet: Characters/vettius.json
    role: pc
    hp: 11
    hp_max: 11
    conditions: []
    spells_used: []
    encumbrance_st: 9.625
  - name: Marcia
    sheet: Characters/marcia.json
    role: pc
    hp: 8
    hp_max: 8
    conditions: []
    spells_used: []
    encumbrance_st: 4.448
  - name: Gallus
    sheet: Characters/gallus.json
    role: henchman
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 4.881
  - name: Hesper
    sheet: Characters/hesper.json
    role: henchman
    hp: 5
    hp_max: 5
    conditions: []
    spells_used: []
    encumbrance_st: 5.897
  - name: Thorcigar
    sheet: Characters/thorcigar.json
    role: henchman
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
    encumbrance_st: 2.562
  - name: Thorwell
    sheet: Characters/thorwell.json
    role: henchman
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 4.229
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
    spells_used: []
  - name: Zaira the Beautiful
    sheet: Characters/zaira-the-beautiful.json
    role: henchman
    hp: 5
    hp_max: 5
    conditions: []
    spells_used: []
  light: torch (Lucilla) out; torch (Vettius) out; torch (Hesper) out; torch (Hesper) out; torch (Gallus) out; torch (Gallus) out; torch (Lucilla) out
  rations: 'Aulus: food 0 d, water 0 d; Sabina: food 1 d, water 0.2 d; Tarq: food 2 d, water 0 d; Lucilla: food 10 d, water 0 d; Vettius: food 1 d, water 0 d; Marcia: food 1 d, water 0.4 d; Thorwell: food 1 d, water 0 d; Thorcigar: food 1 d, water 0 d; Gallus: food 1 d, water 0 d; Quintus the Rager: food 1 d, water 0 d; Vestus the Unlikely: food 1 d, water 0 d; Zaira the Beautiful: food 1 d, water 0 d; Hesper: food 1 d, water 0 d; Donkey, Draft: fodder 0 st, water 0 st'
  tracker: {}
  threads: []
  trail:
  - '11.07'
  - '10.07'
  - '11.07'
  - '14.07'
  - '13.08'
  - '12.07'
  - '11.07'
  - '10.07'
  - '11.07'
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
clock_day: 122
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
