---
type: companion
owner: hrodric
tags:
- sakkara/characters
---
# Hrodric's eagle (totem animal)

Hrodric's totem animal (RR Shaman, Totem Animal; chosen at creation, S01). Kept by hand until the engine models totem
animals (the user, 2026-11-24: to be added after the Sakkara playtest, before SOTN). Its current hp are kept on this
note: update the line below after every fight or injury.

**Dead** (day 66, the ogre den on the temple's second level: a sword blow, then grievously wounded with no healing magic able to reach it within the turn). Hrodric saved vs Death (no damage) and lost Command. A new eagle comes to him when he next gains a level (RR Shaman).

## Numbers (Hrodric at 2nd level, from day 52)

| | Value | Source |
| --- | --- | --- |
| Hit Dice | 1 (one less than Hrodric's 2; it was 1/2 at his 1st level) | RR Shaman, Hit Dice |
| hp | 4 (4 per HD) | RR Shaman, Hit Dice |
| AC | 3 | Totem table AC 3; difference from an ordinary eagle (HD 1+1) is 1/2 HD, rounded to even = 0: no change |
| Attacks | 2 talons, 10+ (as a monster of 1 HD) | RR Shaman ("attack throws as a monster of its HD"); RR p. 296 Attack Throws by Level and HD (1 HD: 10+) |
| Damage | 1d3 / 1d3 slashing | Totem table; at 1 HD the difference from 1 HD is 0: no adjustment |
| Dive | double damage dice (2d3 per talon) in open terrain; both talons on a smaller foe: its size-adjusted Paralysis save or grabbed (talons automatic each round while grabbed) | MM p. 17 Dive Attack; MM Medium Raptor |
| Saves | as a Fighter of 1/2 HD: F0 (as a normal man) | RR Shaman ("saving throws as a Fighter of half its HD") |
| Morale | none: utterly loyal while Hrodric keeps his tribal traditions; fights for him and obeys | RR Shaman, Mind and loyalty |
| Speed | 480' flying (totem table); 20'/60' on the ground (Medium Raptor) | RR Shaman table; MM Medium Raptor |
| Senses | acute vision; +2 to avoid surprise in the open (alert) | MM Medium Raptor |
| Intellect | 5 (half Hrodric's INT 11); human-like intelligence; Hrodric and it understand each other's speech | RR Shaman |
| Normal load | 2/6 st (cannot carry a man) | MM Medium Raptor |
| Totem benefit | Hrodric has **Command** while the eagle lives (on his actor as a class proficiency, cause "totem benefit") | RR Shaman table |

Rescale at each of Hrodric's levels: HD = Hrodric's HD - 1, hp = 4 x HD; AC +/-1 per 2 HD of difference from 1 HD
(minimum 0, maximum the greater of 1 or AC 3 x 1.25 = 3.75, so 4 at most); average damage of the routine +/-2 per HD of
difference from 1 HD (Judge decides the dice); attack throw as a monster of its HD; saves as a Fighter of half its HD.

## Running it without the engine's support

- **In a fight:** add it as a party combatant on the Medium Raptor statblock with its own numbers:
  `state add hrodric-eagle --monster "Medium Raptor" --side party --perceived "Hrodric's eagle"`, then
  `state set hrodric-eagle hp=<current> hp_max=4 ac=3 damage=1d3 attack_throw=10 save=F0`. Ignore the JUDGE line on
  the desert vulture's defenses (an eagle has none). Its two talons: `attack hrodric-eagle T --attack 0`, then
  `--attack 1`. A dive: `attack … --no-damage` for each talon, then `damage T --dice 2d3 --type slashing --mundane`
  per hit; on two hits against a smaller foe, the foe's size-adjusted Paralysis save (`save T paralysis`) or
  `state cond T grabbed`. Its rolls are open (it is the party's). It never checks morale.
- **Outside a fight** (scouting, carrying a message, watching a camp): the Judge's call by its senses and speed;
  hidden rolls for what it finds, told to Hrodric in its own words (Intellect 5).
- **Healing:** as a creature of its HD (natural healing, cure spells); update the hp line above.
- **Death:** Hrodric saves vs Death (`acks.sh save hrodric death`, need 10+ at 1st level) or takes damage equal to
  the eagle's maximum hp at once (`damage hrodric --dice 1d1 --mod <max hp - 1>` or `state set`); he loses Command
  (`actor item hrodric remove proficiency "Command" --cause "totem slain"`). It cannot be restored; a new eagle
  appears when Hrodric next gains a level (Command returns then).
- **Tribal traditions:** if Hrodric breaks them, the eagle's loyalty is no longer assured (Judge's call when it
  arises).
- Not an inventory animal, a retinue member or a training course; it takes no share of treasure or XP.
