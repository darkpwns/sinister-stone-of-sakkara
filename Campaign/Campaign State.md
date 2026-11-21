---
type: campaign-state
tags:
- sakkara/campaign
session: 11
mode: town
location: '[[Cyfaraun]]'
adventure: Secrets of the Nethercity (AX2), between delves (A22 paid out)
public:
  date:
    year: ''
    season: fall
    day: 244
  time: 06:02
  weather: Brisk (56 to 60 F) by day, Brisk (56 to 60 F) at night; mostly cloudy; wind moderate
  place: Cyfaraun
  hex: '18.05'
  party:
  - name: Lucilla
    sheet: Characters/lucilla.json
    role: pc
    hp: 21
    hp_max: 21
    conditions:
    - minor scarring (fang mark on the hand)
    - wears a Ring of Fire Protection (L63, identified day 195)
    - 'third eye in the forehead (Tampering with Mortality, day 243): lidded; telepathy 3 times a day by unlidding it; -3 to reaction rolls with normal men who see it'
    spells_used: []
    encumbrance_st: 8.197
  - name: Vettius
    sheet: Characters/vettius.json
    role: pc
    hp: 21
    hp_max: 21
    conditions: []
    spells_used: []
    encumbrance_st: 10.502
  - name: Vestus the Unlikely
    sheet: Characters/vestus-the-unlikely.json
    role: pc
    hp: 9
    hp_max: 9
    conditions: []
    spells_used: []
  - name: Neris
    sheet: Characters/neris.json
    role: pc
    hp: 7
    hp_max: 7
    conditions:
    - ear bitten off (-1 to Listening throws and -1 to surprise rolls)
    spells_used:
    - Cure Moderate Injury
    - Cure Moderate Injury
    - Cure Light Injury
    - Cure Light Injury
    - Cure Light Injury
    encumbrance_st: 2.636
  - name: Brennus
    sheet: Characters/brennus.json
    role: pc
    hp: 25
    hp_max: 27
    conditions:
    - ear torn clean off (-1 to Listening throws and -1 to surprise rolls)
    - six teeth knocked out (-1 to reaction rolls with the opposite sex and upper-class NPCs)
    - nose flattened, cheek crushed, ear cauliflowered (gruesome scarring)
    - one toe bitten off one foot (3 lost toes on one foot make it useless)
    spells_used: []
    encumbrance_st: 8.469
  - name: Iulia
    sheet: Characters/iulia.json
    role: pc
    hp: 23
    hp_max: 23
    conditions:
    - minor scarring (puncture wound)
    spells_used:
    - Cure Light Injury
    - Cure Light Injury
    encumbrance_st: 8.469
  - name: Hrodvar
    sheet: Characters/hrodvar.json
    role: henchman
    hp: 5
    hp_max: 5
    conditions: []
    spells_used: []
    encumbrance_st: 7.264
  - name: Varro
    sheet: Characters/varro.json
    role: henchman
    hp: 8
    hp_max: 8
    conditions: []
    spells_used: []
    encumbrance_st: 8.931
  - name: Aelia
    sheet: Characters/aelia.json
    role: henchman
    hp: 9
    hp_max: 12
    conditions: []
    spells_used: []
    encumbrance_st: 5.438
  - name: Marcellus
    sheet: Characters/marcellus.json
    role: henchman
    hp: 10
    hp_max: 11
    conditions:
    - two fingers bitten off one hand (3 lost fingers on one hand make it useless)
    spells_used: []
    encumbrance_st: 8.764
  - name: Phaedra
    sheet: Characters/phaedra.json
    role: henchman
    hp: 6
    hp_max: 6
    conditions: []
    spells_used: []
    encumbrance_st: 6.103
  - name: Gnaeus
    sheet: Characters/gnaeus.json
    role: henchman
    hp: 7
    hp_max: 9
    conditions: []
    spells_used: []
    encumbrance_st: 7.264
  light: lantern (Vettius) out; torch (ottar) out; torch (ottar) out; torch (ottar) out; torch (Aelia) out; torch (ottar) out; torch (Marcellus) out; torch (Phaedra) out; torch (Phaedra) out; torch (Aelia) out; torch (Aelia) out; torch (Phaedra) out; torch (Aelia) out; torch (Phaedra) out; torch (Aelia) out; torch (Phaedra) out; torch (Aelia) out
  rations: 'Lucilla: food 7 d, water 1 d (incapacitated); Vettius: food 7 d, water 0.8 d; Vestus the Unlikely: food 7 d, water 1 d; Neris: food 6 d, water 1 d; Iulia: food 13 d, water 1 d; Varro: food 6 d, water 1 d; Hrodvar: food 6 d, water 1 d; Brennus: food 13 d, water 1 d; Aelia: food 6 d, water 1 d; Marcellus: food 6 d, water 1 d; Phaedra: food 6 d, water 1 d; Gnaeus: food 6 d, water 1 d; Donkey, Draft: fodder 0 st, water 0 st; Mule, Draft: fodder 0 st, water 0 st'
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
clock_day: 244
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
