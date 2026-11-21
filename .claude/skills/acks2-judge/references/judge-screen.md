# AI Judge's screen — what the engine leaves to the Judge

Load at session start, beside the rules vault's `Judge's Screen.md` (core numbers: throws, combat, Mortal Wounds,
encounters, dungeon, wilderness, hirelings, XP, conditions). The engine (`acks.sh`) decides every number it covers;
this sheet holds what came up again and again in play (Sakkara playtest, AX1) and is **not** decided by the engine:
spell effects, scrolls, areas, judgement calls, and the routine an AI Judge slips on. Rules lines cite the vault; lines
marked *convention* are no rule: rule once, record in Rulings.md, then follow the record.

## 1. Spells cast most often (ACKS II names; the vault note decides anything not here)
| Spell | Lvl | Range | Area / targets | Duration | Save | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Slumber | A1 D2 | 180' | living targets <5 HD in a 10'-**diameter** sphere | 1 turn/level | Paralysis, only targets of 2+ HD | slumbering = helpless (coup de grace); waking by attack, damage, moving |
| Beguile Humanoid | A1 D2 | 90' | 1 living humanoid <5 HD | 1 day | Spells (+5 if threatened or attacked by caster's side) | bewitched: a friend, fights whoever started violence |
| Mage Missile | A1 | 360' | 1 target per round | concentration | none, no attack throw | 1d4 extraordinary arcane each |
| Fan of Flames | A1 | 0' | fan 40' long × 20' wide; **creatures of the caster's choice** | instant | Blast for half | 1d8 extraordinary fire; ignites oil |
| Blinding Flash | A1 | 90' | **every** creature within 10' of a point (allies too) | 1 round | Blast negates | 1d6 extraordinary fire + blinded to end of its next initiative |
| Choking Grip | A1 D2 | 45' | 1 living breather | concentration | Death each of caster's initiatives | 1d6 extraordinary necrotic per failure; target cannot act |
| Cure Light / Moderate / Major Injury | D1 / D2 / D3 | touch | 1 living | instant | — | 1d6+1 / 2d6 / 2d6+½ level; or end paralysis instead; reverse needs an attack throw; harms undead |
| Halt Humanoids | A2 D2 | 90' | **1d4** living humanoids (roll the count first) | 1 round/level | Paralysis negates | paralyzed = helpless, mute; a cure ends it |
| Holy Blessing | D2 | self, 15' | caster + 30 allies | 6 turns | — | +1 attack, AC, morale, saves vs magical fear; not on anyone who attacked on his last initiative: cast before the fight |
| Holy Circle | D1 | self | 10' radius | stationary concentration | — | enchanted (undead, summoned) cannot enter; ends if anyone inside attacks, casts on or forces the barrier against them; evil foes: +1 AC and saves inside |
| Holy Circle, Sustained | D3 | self | 10' radius, moves with caster | 12 turns | — | as Holy Circle, no concentration |
| Sanctuary | D1 | touch | 1 | 2 rounds + 1/level | attackers save vs Spells or pick another target | ends if the recipient attacks or engages |
| Necromantic Potence | A2 D2 | self | — | 1 hour/level | — | 1d10 + 1/level temporary hp; counts as evil summoned for Holy Circle |
| Deathless Minion | A2 D2 | 45' | 1 corpse | 1 hour | — | skeleton (baseline HD) or zombie (+1 HD, -2 initiative) |
| Counterspell | A1 D1 | 180' | 1 ongoing spell | instant | unwilling target: Spells | attack throw vs AC = caster-level difference |

Casting: declared before initiative; lost if the caster is damaged or fails a save first (Judge's Screen §2).
Spells and scrolls cast in a fight: check the target count, HD limit and save **before** rolling.

## 2. Scrolls (TT pp. 94-99, Magic Items - Scrolls)
- Reading is declared before initiative and is disrupted like spellcasting: **a disrupted reading loses the spell
  from the scroll.**
- The reader must **read the scroll's language** (unless he has Scrollreading: thieves at 10th level, after
  Deciphering it). Deciphering (thief 4th): 1 turn per page, 4+; not magical writing.
- Spell scrolls: the spell must be on the reader's class spell list (not his repertoire); cast at the minimum caster
  level. Warding and protection scrolls (e.g. Creature Warding: 10' radius moving with the reader, 6 turns, ends if
  anyone inside melees a warded creature): **anyone literate in the language.**
- A scroll's language comes from the Scroll Languages table: note it on the lot when found; nobody in a party
  usually reads Ancient Zaharan or Classical Auran.

## 3. Areas and crowds in the mind's eye (*convention*; RR gives the battlemap only: 5' squares)
- Count creatures by the area in 5' squares: 10'-diameter sphere ≈ 3 man-sized creatures; 10'-radius burst ≈ 12;
  40' × 20' fan ≈ 16. A blast centred on an engaged foe catches that foe and everyone engaged with it (they are within
  5'); allies included unless the spell lets the caster choose.
- Melee attackers on one man-sized target: up to 8 man-sized in the open (the 8 squares around it); 2 abreast in a
  10' corridor, 1 in a 5' tunnel. Larger targets: the optional Engagement by Smaller or Larger Creatures table (RR,
  Round Sequence) gives how many it takes to engage them.
- Positions are the Judge's: track distances in the combat state (`state distance`, `state engage`) and never let a
  creature act on a target it cannot reach that round (combat speed; a charge up to running speed in a straight line).

## 4. Wounds and healing the engine does not settle
- A cure on a character below 0 hp: the RR says the cure triggers the Mortal Wounds roll, not what hp follow. Rule it
  once (*Sakkara: the cure heals from 0, "healed to 1 hp" read as 1 hp after the cure*).
- Mortal Wounds rolled for a character left untreated: at treatment, or after 24 hours (`state end` does foes; party
  members untreated: `mortal-wounds ID --untreated-24h`).
- Permanent wounds and XP penalties go into the actor's conditions in the Mortal Wounds table's words (the payout
  reads "N% penalty on earned XP"); bed rest is incapacitated (max 1 hp).
- Undead and mindless guards attack helpless characters in reach (automatic hits): drag the fallen out or cover them.

## 5. Thief skills (RR Thief; the engine has them as `throw ID --prof <skill>`)
| Lvl | Climb | Hide | Listen | Locks | Pickpocket | Search | Sneak | Traps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6+ | 19+ | 14+ | 18+ | 17+ | 18+ | 17+ | 18+ |
| 2 | 5+ | 18+ | 13+ | 17+ | 16+ | 17+ | 16+ | 17+ |
| 3 | 4+ | 17+ | 12+ | 16+ | 15+ | 16+ | 15+ | 16+ |
| 4 | 3+ | 16+ | 11+ | 15+ | 14+ | 15+ | 14+ | 15+ |
| 5 | 2+ | 15+ | 10+ | 14+ | 13+ | 14+ | 13+ | 14+ |
| 6 | 1+ | 14+ | 9+ | 13+ | 12+ | 13+ | 12+ | 13+ |
A sneaking character is passed to `encounter surprise --sneaking ID` whether or not the throw succeeded; a failed
sneak is heard by anything in earshot (Judge's Screen, earshot table).

## 6. Hirelings in a fight and after
- Henchman morale rolls in combat (RR Morale and Loyalty: "loses a substantial amount of hp or the party suffers
  severe casualties or shocks"): the engine rolls them at round end on 1/3 hp lost, 1/3 of the party felled, the
  employer felled. A henchman at 0 hp queues a calamity loyalty roll: `loyalty --pending` after the fight.
- Loyalty rolls also on a missed wage (the engine rolls it at the rollover: pay before rest days and journeys), a
  level gained (`loyalty ID --trigger level`), a permanent wound.
- A henchman whose employer dies: per Table rules (see §7); otherwise he departs unless someone re-hires him.

## 7. A character dies (RR Character Death, pp. 311-313)
In this order, as Table rules allow: (1) the player **takes over a henchman** at his level and XP (`death <pc>
--successor <henchman> --player P`: he leaves the retinue and becomes a PC; he cannot use reserve XP or a heroic
funeral, can inherit); (2) a **new or back-up character** at 1st level with XP = reserve fund + heroic funeral XP,
never above the prior character's XP (`death <pc> --new-character --player P --prior-xp N`). Funds: money spent for
no tangible benefit (90%, `--reserve-spend`), a heroic funeral (90% of treasure spent or interred; a cenotaph serves
when the body is lost; not for unheroic deaths). Heirs: a will and a bank (10%); without one, one relative may collect
once. The dead man's gear is `body:<id>`; his share is lost if left behind. Characters retire only by the player's
choice or when injuries make adventuring unlikely.

## 8. Animals and loads
- Donkeys, oxen and steppe horses graze while travelling (not when force-marched); other animals need fodder or a
  dedicated grazing day (they may still travel at half speed with their ancillary hours). Water: normal load ÷ 5 per day.
- Load by stone: an overloaded member or animal sets the column's speed; shift loads to animals before marching
  (`move-rate ID`, `inv give ID donkey1 …`).

## 9. Town loop (engine: R/town.md, R/xp-treasure.md)
- Market availability is per market per month (hidden): small markets run out of rations, oil, holy water; buy at
  the first chance and split food among members (food is not pooled).
- Selling: magic items at apparent value unless identified; identified and sold unused adds sale XP. Identification:
  magic research (5th-level caster or Loremastery; 1,000gp + 1,000gp, library), a module's sage, or use.
- Spellcasting services (RR pp. 172-173): castings per day by market class (class V: divine 1st 4d6, 2nd 2d4, 3rd
  1d6, none above; class VI: divine 1st 2d4, 2nd 1d6), 5 / 10 / 45 / 185 / 900gp by level; recruit the caster by
  reaction; never for the opposite alignment; double for other faiths (`acks.sh spellcasting`).

## 10. What modules leave to the Judge (decide by a hidden roll or a recorded call, before it matters)
- Where a named NPC is now (lair, patrol, absent): set odds from the text ("most of her time" = 5 in 6 after an alarm).
- Whether guards or undead are alerted by a fight elsewhere, and how many rounds they take to arrive.
- Who presents the symbol, password or sign the module's guards check for (unholy symbols, tribal marks).
- Weekly replacement of slain monsters while the module's cause remains; stop when it is removed.
- Distances the map does not give (camp to site, room to room in a cave): rule once, record.
- Monster abilities the engine does not model (arcane strike, death healing, double damage on a natural 20): apply
  by hand with `damage --dice …` and note it in the Judge block.

## 11. Routine (the slips of the Sakkara playtest)
- Before a delve: `adventure start` + `join`; light lit, spares counted; rations and water per member; wages due
  during the trip paid in advance.
- Each turn: relight torches as they burn out; rest 1 turn after every 5 turns of exploring; wandering checks at the site's rate.
- Each fight: every foe's turn resolved, cleaves included; no attack on a target out of reach; spells' target counts
  rolled before saves; after the fight copy hp and conditions to the actors **before** deleting the combat state;
  `turn --rounds N`; `encounter end` closes the right encounter (a wandering one may have arrived meanwhile).
- Each night: watches that leave everyone 8 hours (four 3-hour watches over a 12-hour camp).
- Each march: daylight hours only unless the party chooses otherwise; `water` where the party passes water.
- After deaths: `death --dies` (body, retinue, exploration party), then the takeover or new character (§7).
