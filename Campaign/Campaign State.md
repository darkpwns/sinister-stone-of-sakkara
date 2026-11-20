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
    day: 96
  time: 09:08
  weather: Brisk (63 to 67 F) by day, Chilly (57 to 62 F) at night; overcast; wind moderate
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
    encumbrance_st: 8.892
  - name: Lucilla
    sheet: Characters/lucilla.json
    role: pc
    hp: 10
    hp_max: 10
    conditions:
    - lost an eye and an ear (half her face mauled)
    spells_used: []
    encumbrance_st: 9.056
  - name: Sabina
    sheet: Characters/sabina.json
    role: pc
    hp: 14
    hp_max: 14
    conditions: []
    spells_used: []
    encumbrance_st: 8.227
  - name: Tarq
    sheet: Characters/tarq.json
    role: pc
    hp: 6
    hp_max: 6
    conditions:
    - raspy voice (-2 to speech throws)
    spells_used: []
    encumbrance_st: 8.217
  - name: Vettius
    sheet: Characters/vettius.json
    role: pc
    hp: 11
    hp_max: 11
    conditions: []
    spells_used: []
    encumbrance_st: 8.721
  - name: Marcia
    sheet: Characters/marcia.json
    role: pc
    hp: 8
    hp_max: 8
    conditions: []
    spells_used: []
    encumbrance_st: 4.056
  - name: Gallus
    sheet: Characters/gallus.json
    role: henchman
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 5.074
  - name: Hesper
    sheet: Characters/hesper.json
    role: henchman
    hp: 5
    hp_max: 5
    conditions: []
    spells_used: []
    encumbrance_st: 4.896
  - name: Thorcigar
    sheet: Characters/thorcigar.json
    role: henchman
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
    encumbrance_st: 2.395
  - name: Thorwell
    sheet: Characters/thorwell.json
    role: henchman
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 4.062
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
  light: torch (Lucilla) out; torch (Vettius) out; torch (hesper) out; torch (hesper) out; torch (Gallus) out; torch (Gallus) out; torch (Lucilla) out
  rations: 'Aulus: food 0 d, water 0.6 d (underfed); Sabina: food 0 d, water 1.2 d (underfed); Tarq: food 0 d, water 1 d; Lucilla: food 0 d, water 1 d (underfed); Vettius: food 0 d, water 1 d (underfed); Marcia: food 0 d, water 1.4 d (underfed); Thorwell: food 1 d, water 1 d (hungry, underfed, starving, fatigued); Thorcigar: food 1 d, water 1 d (hungry, underfed, starving); Gallus: food 0 d, water 0.8 d (underfed); Quintus the Rager: food 0 d, water 0 d (hungry, underfed); Vestus the Unlikely: food 0 d, water 0 d (hungry, underfed); Zaira the Beautiful: food 0 d, water 0 d (hungry, underfed); Donkey, Draft: fodder 0 st, water 0 st'
  tracker: {}
  threads: []
  trail:
  - '13.08'
  - '12.07'
  - '11.07'
  - '10.07'
  - '11.07'
  - '08.06'
  - '09.06'
  - '10.06'
  - '11.07'
  - '12.07'
  - '13.08'
  - '12.07'
  - '11.07'
  - '10.07'
  - '11.07'
  - '14.07'
  - '13.08'
  - '12.07'
  - '11.07'
  - '10.07'
clock_day: 96
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
