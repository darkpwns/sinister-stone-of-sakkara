---
type: campaign-state
tags:
- sakkara/campaign
session: 9
mode: town
location: '[[Turos Tem]]'
adventure: none yet (AX1 The Sinister Stone of Sakkara opens at the first delve or journey)
public:
  date:
    year: ''
    season: spring
    day: 68
  time: 03:30
  weather: Brisk (63 to 67 F) by day, Chilly (57 to 62 F) at night; overcast; wind gentle
  place: Türos Tem
  hex: '19.19'
  party:
  - name: Eskil
    sheet: Characters/eskil.json
    role: pc
    hp: 5
    hp_max: 5
    conditions:
    - 'intestines mangled and ruined (Mortal Wounds, day 16): must rest 2 turns of 6, CON reduced by 1/3, -4 to save vs. poison, -4 to reaction rolls'
    - ghostly visions of lost companions (Mortal Wounds, day 45)
    spells_used: []
    encumbrance_st: 6.673
  - name: Fulvia
    sheet: Characters/fulvia.json
    role: pc
    hp: 5
    hp_max: 5
    conditions: []
    spells_used: []
    encumbrance_st: 5.557
  - name: Octavia
    sheet: Characters/octavia.json
    role: pc
    hp: 6
    hp_max: 6
    conditions: []
    spells_used: []
    encumbrance_st: 4.542
  - name: Gaius Rufo
    sheet: Characters/gaius-rufo.json
    role: pc
    hp: 5
    hp_max: 5
    conditions:
    - 'one foot chewed off (Mortal Wounds, day 16): wooden peg (day 35), movement -30 feet, DEX reduced by 1/3 for AC'
    spells_used: []
    encumbrance_st: 7.541
  - name: Ione
    sheet: Characters/ione.json
    role: henchman
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
    encumbrance_st: 1.446
  - name: Aedo
    sheet: Characters/aedo.json
    role: pc
    hp: 5
    hp_max: 5
    conditions:
    - 'grievously wounded (day 45, giant rats): 2 weeks of bed rest'
    - 'intestines mangled and ruined (Mortal Wounds, day 45): must rest 2 turns of 6, CON reduced by 1/3, -4 to save vs. poison, chronic indigestion and flatulence: -4 to reaction rolls'
    - 'calf almost chewed through (day 45): cannot force march unless mounted'
    spells_used: []
    encumbrance_st: 7.178
  - name: Septimia
    sheet: Characters/septimia.json
    role: pc
    hp: 4
    hp_max: 4
    conditions: []
    spells_used: []
    encumbrance_st: 5.023
  - name: Decimus Ruga
    sheet: Characters/decimus-ruga.json
    role: henchman
    hp: 3
    hp_max: 3
    conditions:
    - 'symptomatic: Ague (incapacitated)'
    spells_used: []
    encumbrance_st: 7.669
  - name: Herennius Bow
    sheet: Characters/herennius-bow.json
    role: henchman
    hp: 3
    hp_max: 3
    conditions: []
    spells_used: []
    encumbrance_st: 3.667
  - name: Tullus Brocchus
    sheet: Characters/tullus-brocchus.json
    role: henchman
    hp: 5
    hp_max: 5
    conditions:
    - 'in shock (day 45): magical healing and a night of bed rest (given), or a week of rest'
    - two fingers of one hand bitten off (Mortal Wounds, day 45)
    spells_used: []
    encumbrance_st: 7.677
  light: torch (Gaius Rufo) out; lantern (Octavia) out; torch (Gaius Rufo) out
  rations: 'Octavia: food 2 d, water 3 d; Fulvia: food 2 d, water 0.8 d; Eskil: food 2 d, water 2.2 d; Gaius Rufo: food 16 d, water 1 d; Septimia: food 27 d, water 1 d; Tullus Brocchus: food 2 d, water 0.4 d; Herennius Bow: food 2 d, water 1 d; Ione: food 3 d, water 1 d; Aedo: food 12 d, water 0.4 d; Donkey, Draft: fodder 0 st, water 0 st'
  tracker: {}
  threads: []
  trail:
  - '21.18'
  - '21.19'
  - '22.19'
  - '20.18'
  - '20.19'
  - '21.20'
  - '22.20'
  - '21.20'
  - '20.19'
  - '19.19'
  - '20.19'
  - '21.20'
  - '22.20'
  - '21.20'
  - '20.19'
  - '23.21'
  - '22.20'
  - '21.20'
  - '20.19'
  - '19.19'
clock_day: 68
---
# Campaign State

Judge-only working file. The `public:` block holds every player-facing transient value; `public.party` is generated
from the actors (`xsync.py`). Permanent values live in the actors in `Characters/`. Keep this file short.

Run 3 (from 2026-11-25): a fresh campaign with new characters, AX1 *The Sinister Stone of Sakkara*. Runs 1 (S01-S54)
and 2 (S01-S16) are archived in `Archive/Run 1 (S01-S54)/` and `Archive/Run 2 (S01-S16)/`: none of their events,
characters, NPC attitudes or factions' standing hold in run 3. Their Rulings carry over as precedents (Rulings.md).

## Table rules

Carried from runs 1 and 2 except where marked run 3 (user, 2026-11-25).

- Quest and discovery awards: off; hidden rolls in the Judge block (the module's own XP for an adventure's goal stands: Rulings S06)
- Henchman control: the AI players direct routine actions and combat tactics; the Judge plays personality, morale, obedience
- Party structure: AI party (six AI players; the user watches). Caller Gideon. The Judge plays the AI players by their profiles, `Party/heuristics.md` and the party notes (no party-agent calls; run 1 S06 user decision)
- **Party goal (run 3, user):** the party is focused primarily on finishing AX1: the Stone of Sakkara destroyed and the Lady Below dealt with. Session goals serve that end (strength, information, allies, coin for henchmen and healing); side ventures only when they plainly help it (Party/heuristics.md "The raids first": the players know only the legate's call)
- **Travel until the temple is done (run 2 S12, kept for run 3):** no wilderness travel except between Türos Tem and the Buried Temple (the corridor 22.20, 21.20, 20.19, 19.19) until the Buried Temple is complete (AX1's goal). A party that strays off the corridor while lost makes its way back to it
- **Combat and factions (run 2 S09, kept for run 3):** combat is a failure state: the party draws steel only when the enemy cannot fight back or is plainly outmatched (by the party and its allies); talk, trade, tribute, bribery, deception and alliances come first, and a failed edge means breaking off, not fighting it out. Dungeon and wilderness factions carry no lasting obligation and are used actively; settled factions are dealt with only when it serves the goal (Party/heuristics.md)
- **Character creation (run 3, user): no templates** (RR optional rule: 3d6 × 10 gp, gear bought at list price at creation (Rulings R2 S01), proficiencies and spells chosen), and **Generating Multiple Characters** (RR p. 13 optional rule, JJ p. 387): each player rolls five characters' attributes and selects the best one as his PC; of the other four, two are his back-ups and two go to the Judge as NPCs (Session Log S01). **At least one PC is an animal trainer** (Animal Training)
- A PC's death (user, 2026-11-21): the player takes over the dead PC's henchman (RR p. 311 successor, `death <pc> --successor <henchman> --player <p>`); without one, a second-level henchman in the party; otherwise a new 1st-level character with the player's reserve XP (built from one of his back-ups, run 3)
- AI players hire their own henchmen: yes
- Month length: 30 days
- Classes allowed: RR core and RR campaign classes, no supplements
- Adventure: AX1 The Sinister Stone of Sakkara (AX3 Borderlands and Cyfaraun as the setting); the campaign ends at a TPK
- Downtime record (engine 7.24.0, C7): each PC and henchman has one before each departure

## Resources

- Possessions, coins, torches, oil and ammunition: the inventory (`acks.sh inv show`)
- Mounts:
- Hirelings (non-henchmen):

## Judge notes (short)
