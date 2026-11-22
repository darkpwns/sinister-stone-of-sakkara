---
type: campaign-state
tags:
- sakkara/campaign
session: 17
mode: town
location: '[[Cyfaraun]]'
adventure: Secrets of the Nethercity (AX2), between delves (A43 paid out)
public:
  date:
    year: ''
    season: winter
    day: 323
  time: '16:57'
  weather: Brisk (56 to 60 F) by day, Brisk (56 to 60 F) at night; mostly cloudy; wind moderate
  place: Cyfaraun
  hex: '18.05'
  party:
  - name: Lucilla
    sheet: Characters/lucilla.json
    role: pc
    hp: 29
    hp_max: 29
    conditions:
    - minor scarring (fang mark on the hand)
    - wears a Ring of Fire Protection (L63, identified day 195)
    - 'third eye in the forehead (Tampering with Mortality, day 243): lidded; telepathy 3 times a day by unlidding it; -3 to reaction rolls with normal men who see it'
    spells_used: []
    encumbrance_st: 9.697
  - name: Vettius
    sheet: Characters/vettius.json
    role: pc
    hp: 22
    hp_max: 22
    conditions: []
    spells_used: []
    encumbrance_st: 9.491
  - name: Vestus the Unlikely
    sheet: Characters/vestus-the-unlikely.json
    role: pc
    hp: 17
    hp_max: 17
    conditions: []
    spells_used: []
    encumbrance_st: 4.469
  - name: Neris
    sheet: Characters/neris.json
    role: pc
    hp: 15
    hp_max: 15
    conditions:
    - 'a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river'
    spells_used: []
    encumbrance_st: 4.788
  - name: Brennus
    sheet: Characters/brennus.json
    role: pc
    hp: 23
    hp_max: 23
    conditions:
    - nose flattened, cheek crushed, ear cauliflowered (gruesome scarring)
    - 'made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with those who knew Brennus before (CHA under 13)'
    spells_used: []
    encumbrance_st: 10.119
  - name: Iulia
    sheet: Characters/iulia.json
    role: pc
    hp: 31
    hp_max: 31
    conditions:
    - minor scarring (puncture wound)
    spells_used: []
    encumbrance_st: 9.81
  - name: Hrodvar
    sheet: Characters/hrodvar.json
    role: henchman
    hp: 14
    hp_max: 14
    conditions: []
    spells_used: []
    encumbrance_st: 9.666
  - name: Varro
    sheet: Characters/varro.json
    role: henchman
    hp: 23
    hp_max: 23
    conditions: []
    spells_used: []
    encumbrance_st: 9.482
  - name: Aelia
    sheet: Characters/aelia.json
    role: henchman
    hp: 15
    hp_max: 15
    conditions: []
    spells_used: []
    encumbrance_st: 6.792
  - name: Marcellus
    sheet: Characters/marcellus.json
    role: henchman
    hp: 21
    hp_max: 21
    conditions: []
    spells_used: []
    encumbrance_st: 9.476
  - name: Phaedra
    sheet: Characters/phaedra.json
    role: henchman
    hp: 19
    hp_max: 19
    conditions: []
    spells_used: []
    encumbrance_st: 7.461
  light: lantern (Vettius) out; torch (ottar) out; torch (ottar) out; torch (ottar) out; torch (Aelia) out; torch (ottar) out; torch (Marcellus) out; torch (Phaedra) out; torch (Phaedra) out; torch (Aelia) out; torch (Aelia) out; torch (Phaedra) out; torch (Aelia) out; torch (Phaedra) out; torch (Aelia) out; torch (Phaedra) out; torch (Aelia) out; lantern (Vettius) out; lantern (Vettius) out; lantern (Vettius) out; lantern (Vettius) out; lantern (Vettius) out; torch (Phaedra) out; torch (Phaedra) out; torch (Phaedra) out; lantern (Vettius) out; torch (Aelia) out; torch (Aelia) out; lantern (Vettius) out; lantern (Vettius) out; lantern (Vettius) out; lantern (Vettius) out
  rations: 'Lucilla: food 0 d, water 1 d; Vettius: food 0 d, water 1 d; Vestus the Unlikely: food 0 d, water 1.8 d; Neris: food 0 d, water 1.2 d; Iulia: food 0 d, water 0.4 d; Varro: food 0 d, water 1 d; Hrodvar: food 0 d, water 1 d; Brennus: food 0 d, water 0.8 d; Aelia: food 5 d, water 1 d; Marcellus: food 6 d, water 1 d; Phaedra: food 0 d, water 1 d; Donkey, Draft: fodder 0 st, water 0 st; Mule, Draft: fodder 0 st, water 0 st'
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
clock_day: 323
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
