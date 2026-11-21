---
type: campaign-state
tags:
- sakkara/campaign
session: 8
mode: town
location: '[[Turos Tem]]'
adventure: Secrets of the Nethercity (AX2), the journey to Cyfaraun
public:
  date:
    year: ''
    season: summer
    day: 170
  time: 06:00
  weather: Warm (83 to 86 F) by day, Balmy (75 to 79 F) at night; drizzle; wind gentle (drizzly)
  place: Türos Tem
  hex: '25.13'
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
    encumbrance_st: 9.252
  - name: Sabina
    sheet: Characters/sabina.json
    role: pc
    hp: 16
    hp_max: 16
    conditions:
    - one eye clawed out (-2 to missile attack throws)
    spells_used: []
    encumbrance_st: 8.896
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
    encumbrance_st: 9.554
  - name: Vettius
    sheet: Characters/vettius.json
    role: pc
    hp: 3
    hp_max: 12
    conditions:
    - 'spine broken at the neck: paralyzed (cannot move, fight, use items or cast spells; Death save each month or die of complications) — RR p. 519 Mortal Wounds'
    - bed rest 1 month (incapacitated, max 1 hp)
    spells_used: []
    encumbrance_st: 9.408
  - name: Hesper
    sheet: Characters/hesper.json
    role: pc
    hp: 10
    hp_max: 10
    conditions: []
    spells_used: []
    encumbrance_st: 5.443
  - name: Vestus the Unlikely
    sheet: Characters/vestus-the-unlikely.json
    role: pc
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
  light: none
  rations: 'Sabina: food 3 d, water 2.6 d; Tarq: food 8.5 d, water 0 d; Lucilla: food 0 d, water 1 d; Vettius: food 0 d, water 0 d; Hesper: food 4 d, water 1 d; Vestus the Unlikely: food 10 d, water 1 d; Donkey, Draft: fodder 0 st, water 0 st'
  tracker: {}
  threads: []
  trail:
  - '21.20'
  - '20.19'
  - '19.19'
  - '20.19'
  - '19.19'
  - '20.19'
  - '21.20'
  - '22.20'
  - '23.20'
  - '24.19'
  - '25.19'
  - '26.18'
  - '26.17'
  - '27.17'
  - '28.16'
  - '27.16'
  - '26.15'
  - '26.14'
  - '25.14'
  - '25.13'
clock_day: 170
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
