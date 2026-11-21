---
type: campaign-state
tags:
- sakkara/campaign
session: 7
mode: town
location: '[[Turos Tem]]'
adventure: between adventures (AX1 complete, day 161)
public:
  date:
    year: ''
    season: summer
    day: 161
  time: 06:00
  weather: Hot (87 to 90 F) by day, Warm (83 to 86 F) at night; drizzle; wind moderate (drizzly)
  place: Türos Tem
  hex: '13.08'
  party:
  - name: Lucilla
    sheet: Characters/lucilla.json
    role: pc
    hp: 19
    hp_max: 19
    conditions:
    - lost an eye and an ear (half her face mauled)
    - minor scarring (fang mark on the hand)
    spells_used: []
    encumbrance_st: 9.258
  - name: Sabina
    sheet: Characters/sabina.json
    role: pc
    hp: 16
    hp_max: 16
    conditions:
    - one eye clawed out (-2 to missile attack throws)
    spells_used: []
    encumbrance_st: 8.756
  - name: Tarq
    sheet: Characters/tarq.json
    role: pc
    hp: 13
    hp_max: 13
    conditions:
    - raspy voice (-2 to speech throws)
    - minor scarring (fang marks on the neck)
    - skull wound, brain fluid leaked (-2 on magical research and proficiency throws, -10% earned XP)
    - one hand bitten off (cannot dual-wield or use two-handed weapons)
    spells_used: []
    encumbrance_st: 9.563
  - name: Vettius
    sheet: Characters/vettius.json
    role: pc
    hp: 12
    hp_max: 12
    conditions: []
    spells_used: []
    encumbrance_st: 9.408
  - name: Hesper
    sheet: Characters/hesper.json
    role: henchman
    hp: 10
    hp_max: 10
    conditions: []
    spells_used: []
    encumbrance_st: 5.461
  light: none
  rations: 'Sabina: food 0 d, water 1.2 d; Tarq: food 1.5 d, water 1 d; Lucilla: food 0 d, water 1 d; Vettius: food 0 d, water 0.4 d; Hesper: food 0 d, water 1 d; Donkey, Draft: fodder 0 st, water 0 st'
  tracker: {}
  threads: []
  trail:
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
  - '11.07'
  - '10.07'
  - '11.07'
  - '12.07'
  - '13.08'
clock_day: 161
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
