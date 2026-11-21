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
    day: 131
  time: 07:48
  weather: Hot (87 to 90 F) by day, Warm (83 to 86 F) at night; drizzle; wind moderate (drizzly)
  place: Buried Temple
  hex: '13.08'
  party:
  - name: Aulus
    sheet: Characters/aulus.json
    role: pc
    hp: 23
    hp_max: 23
    conditions:
    - bewitched by the Lady (Beguile Humanoid, until day 124 ~13:40)
    spells_used: []
    encumbrance_st: 9.01
  - name: Lucilla
    sheet: Characters/lucilla.json
    role: pc
    hp: 3
    hp_max: 10
    conditions:
    - lost an eye and an ear (half her face mauled)
    spells_used: []
    encumbrance_st: 9.556
  - name: Sabina
    sheet: Characters/sabina.json
    role: pc
    hp: 5
    hp_max: 14
    conditions: []
    spells_used: []
    encumbrance_st: 8.866
  - name: Tarq
    sheet: Characters/tarq.json
    role: pc
    hp: -1
    hp_max: 6
    conditions:
    - raspy voice (-2 to speech throws)
    - 'critically wounded: dies unless healed to 1 hp by day 124 13:40; then 1 week bed rest'
    - minor scarring (fang marks on the neck)
    spells_used: []
    encumbrance_st: 0
  - name: Vettius
    sheet: Characters/vettius.json
    role: pc
    hp: 14
    hp_max: 14
    conditions: []
    spells_used: []
    encumbrance_st: 9.851
  - name: Marcia
    sheet: Characters/marcia.json
    role: pc
    hp: 9
    hp_max: 9
    conditions: []
    spells_used: []
    encumbrance_st: 5.174
  - name: Gallus
    sheet: Characters/gallus.json
    role: henchman
    hp: 7
    hp_max: 7
    conditions: []
    spells_used: []
    encumbrance_st: 4.749
  - name: Hesper
    sheet: Characters/hesper.json
    role: henchman
    hp: 10
    hp_max: 10
    conditions: []
    spells_used: []
    encumbrance_st: 6.265
  - name: Thorcigar
    sheet: Characters/thorcigar.json
    role: henchman
    hp: 12
    hp_max: 12
    conditions: []
    spells_used: []
    encumbrance_st: 4.097
  - name: Thorwell
    sheet: Characters/thorwell.json
    role: henchman
    hp: 11
    hp_max: 11
    conditions: []
    spells_used: []
    encumbrance_st: 3.597
  - name: Quintus the Rager
    sheet: Characters/quintus-the-rager.json
    role: henchman
    hp: 2
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
    hp: 4
    hp_max: 5
    conditions:
    - 'grievously wounded: 2 weeks bed rest (healed to 1 hp in time)'
    - one leg torn off (crutch required, movement -30 feet, DEX reduced by 1/3 for AC)
    spells_used: []
  light: torch (Lucilla) out; torch (Vettius) out; torch (Hesper) out; torch (Hesper) out; torch (Gallus) out; torch (Gallus) out; torch (Lucilla) out; torch (Lucilla) out
  rations: 'Aulus: food 0 d, water 0.6 d (hungry, fatigued); Sabina: food 0 d, water 1.2 d (fatigued); Tarq: food 4 d, water 0 d; Lucilla: food 20 d, water 1 d (fatigued); Vettius: food 0 d, water 1 d (fatigued); Marcia: food 0 d, water 1.4 d (hungry, fatigued); Thorwell: food 0 d, water 1 d (hungry, fatigued); Thorcigar: food 0 d, water 1 d (fatigued); Gallus: food 0 d, water 0.8 d; Quintus the Rager: food 0 d, water 1 d (hungry, fatigued); Vestus the Unlikely: food 0 d, water 1 d (hungry, fatigued); Zaira the Beautiful: food 0 d, water 1 d (hungry, fatigued); Hesper: food 0 d, water 1 d (hungry); Donkey, Draft: fodder 0 st, water 0 st'
  tracker: {}
  threads: []
  trail:
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
  - '12.07'
  - '11.07'
  - '10.07'
  - '11.07'
  - '12.07'
  - '12.06'
  - '12.07'
  - '13.08'
clock_day: 131
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
