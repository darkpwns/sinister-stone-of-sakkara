---
type: campaign-state
tags:
- sakkara/campaign
session: 8
mode: town
location: '[[Cyfaraun]]'
adventure: Secrets of the Nethercity (AX2), the journey to Cyfaraun
public:
  date:
    year: ''
    season: summer
    day: 175
  time: 08:20
  weather: Hot (87 to 90 F) by day, Warm (80 to 82 F) at night; heavy rain; wind gentle (rainy)
  place: Cyfaraun
  hex: '18.05'
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
    encumbrance_st: 9.243
  - name: Sabina
    sheet: Characters/sabina.json
    role: pc
    hp: 16
    hp_max: 16
    conditions:
    - one eye clawed out (-2 to missile attack throws)
    spells_used: []
    encumbrance_st: 8.817
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
    encumbrance_st: 9.545
  - name: Vettius
    sheet: Characters/vettius.json
    role: pc
    hp: 3
    hp_max: 12
    conditions:
    - 'bed rest 2 weeks from day 171 (Tampering with Mortality 11: spine restored, no side effect)'
    spells_used: []
    encumbrance_st: 8.972
  - name: Hesper
    sheet: Characters/hesper.json
    role: pc
    hp: 10
    hp_max: 10
    conditions: []
    spells_used: []
    encumbrance_st: 5.425
  - name: Vestus the Unlikely
    sheet: Characters/vestus-the-unlikely.json
    role: pc
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
  - name: Neris
    sheet: Characters/neris.json
    role: henchman
    hp: 4
    hp_max: 4
    conditions: []
    spells_used: []
    encumbrance_st: 2.167
  light: none
  rations: 'Sabina: food 4 d, water 2.6 d; Tarq: food 15.5 d, water 0 d; Lucilla: food 3 d, water 1 d; Vettius: food 3 d, water 0 d (incapacitated); Hesper: food 5 d, water 1 d; Vestus the Unlikely: food 12 d, water 1 d; Neris: food 0 d, water 0 d; Donkey, Draft: fodder 0 st, water 0 st; Mule, Draft: fodder 0 st, water 0 st'
  tracker: {}
  threads: []
  trail:
  - '26.18'
  - '26.17'
  - '27.17'
  - '28.16'
  - '27.16'
  - '26.15'
  - '26.14'
  - '25.14'
  - '25.13'
  - '24.12'
  - '24.11'
  - '23.11'
  - '23.10'
  - '22.09'
  - '21.09'
  - '20.08'
  - '20.07'
  - '19.07'
  - '18.06'
  - '18.05'
clock_day: 175
---
# Campaign State

Judge-only working file. The `public:` block holds every player-facing transient value; `public.party` is generated
from the actors (`xsync.py`). Permanent values live in the actors in `Characters/`. Keep this file short.

## Table rules

Set 2026-11-20 by the user's playtest brief (user away; recommended options otherwise).

- Quest and discovery awards: off; hidden rolls in the Judge block
- Henchman control: the AI players direct routine actions and combat tactics; the Judge plays personality, morale, obedience
- Party structure: AI party (six AI players; the user watches). Caller Gideon.
- A PC's death (user, 2026-11-21): the player takes over the dead PC's henchman (RR p. 311 successor, `death <pc> --successor <henchman> --player <p>`); without one, a second-level henchman in the party; otherwise a new 1st-level character with the player's reserve XP. Characters retire only when their injuries make further adventures unlikely.
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
