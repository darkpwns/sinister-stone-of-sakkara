---
type: campaign-state
tags:
- sakkara/campaign
session: 9
mode: town
location: '[[Cyfaraun]]'
adventure: Secrets of the Nethercity (AX2), between delves (A10 paid out)
public:
  date:
    year: ''
    season: fall
    day: 199
  time: '13:11'
  weather: Brisk (61 to 65 F) by day, Brisk (61 to 65 F) at night; clear; wind still
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
    - wears a Ring of Fire Protection (L63, identified day 195)
    spells_used: []
    encumbrance_st: 9.982
  - name: Vettius
    sheet: Characters/vettius.json
    role: pc
    hp: 8
    hp_max: 12
    conditions: []
    spells_used: []
    encumbrance_st: 9.631
  - name: Vestus the Unlikely
    sheet: Characters/vestus-the-unlikely.json
    role: pc
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
  - name: Neris
    sheet: Characters/neris.json
    role: pc
    hp: 4
    hp_max: 4
    conditions: []
    spells_used:
    - Holy Circle
    encumbrance_st: 2.668
  - name: Ottar
    sheet: Characters/ottar.json
    role: henchman
    hp: 2
    hp_max: 2
    conditions: []
    spells_used: []
    encumbrance_st: 5.926
  - name: Brennus
    sheet: Characters/brennus.json
    role: pc
    hp: 1
    hp_max: 6
    conditions:
    - ear torn clean off (-1 to Listening throws and -1 to surprise rolls)
    - 'critically wounded day 198 (B3 skeletons): 1 week of bed rest, incapacitated'
    - six teeth knocked out (-1 to reaction rolls with the opposite sex and upper-class NPCs)
    spells_used: []
    encumbrance_st: 6.454
  - name: Iulia
    sheet: Characters/iulia.json
    role: pc
    hp: 13
    hp_max: 13
    conditions:
    - minor scarring (puncture wound)
    spells_used: []
    encumbrance_st: 8.312
  - name: Phaedra
    sheet: Characters/phaedra.json
    role: henchman
    hp: 5
    hp_max: 5
    conditions: []
    spells_used: []
    encumbrance_st: 1.426
  - name: Quirinus
    sheet: Characters/quirinus.json
    role: henchman
    hp: 11
    hp_max: 18
    conditions: []
    spells_used: []
    encumbrance_st: 6.759
  - name: Hrodvar
    sheet: Characters/hrodvar.json
    role: henchman
    hp: 4
    hp_max: 4
    conditions: []
    spells_used: []
    encumbrance_st: 6.364
  - name: Septima
    sheet: Characters/septima.json
    role: henchman
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
    encumbrance_st: 4.555
  - name: Varro
    sheet: Characters/varro.json
    role: henchman
    hp: 4
    hp_max: 4
    conditions: []
    spells_used: []
    encumbrance_st: 7.03
  light: lantern (Vettius) out; torch (Ottar) out; torch (Ottar) out; torch (Ottar) out
  rations: 'Lucilla: food 10 d, water 1 d; Vettius: food 10 d, water 0 d; Vestus the Unlikely: food 19 d, water 1 d; Neris: food 7 d, water 1 d; Ottar: food 7 d, water 1 d; Iulia: food 14 d, water 0.2 d; Quirinus: food 7 d, water 1 d; Phaedra: food 7 d, water 1 d; Varro: food 7 d, water 0.4 d; Hrodvar: food 7 d, water 0.4 d; Septima: food 7 d, water 0.4 d; Donkey, Draft: fodder 0 st, water 0 st; Mule, Draft: fodder 0 st, water 0 st'
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
clock_day: 199
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
