# Encounters — with the rules engine

Load whenever the party meets creatures. Procedure (RR `Encounters`): distance → surprise → evasion (wilderness
only) → reaction (if no one attacks) → combat. The engine runs every step in dungeons (stage 2) and in the wilderness
(stage 4); it keeps the encounter in the exploration state, so later commands need no copying.

## 1. Who, how many, how far
- Dungeon wandering: rolled by `acks.sh turn` / `acks.sh wander-check` (site table or JJ p. 37 tables by dungeon
  level; number ×1.5/×0.5 per level step, round up; never in lair).
- Wilderness: rolled by `travel` (each hex entered), `search` (each hour), `hunt`, `camp` and `rest-day` (overland.md):
  the territory column (road, night), civilized / monster (rarity, MM terrain table, River tables along a river) /
  terrain encounter, the lair check and the statblock's wilderness number, the distance by terrain capped by each
  side's visibility (light, group size, terrain, weather; senses other than sight) and who has detected whom. A
  terrain encounter (dangerous, valuable, unique) names its type; `acks.sh terrain-encounter` (engine 7.19.4) runs its
  sub-procedure hidden (cache stored as a hoard, ruin, trap and hazard with the marching-order triggers `--order
  A,B,C` and the bypass hours, challenge with its dimensions, poison with doses and harvest target, ore, food,
  spoilage, magical place `--spell S`, magical resource, monster carcass, double); `--sub NAME` when you choose the
  result; anything else is still the Judge's (JJ pp. 63-68).
  Deliberate wilderness encounters: `acks.sh encounter start --wild --monster "<MM note>" [--number N]
  [--monster-terrain T]` (or `--kind civilized|monster` for a table roll in the current hex; `--at CC.RR` to roll on
  another hex's tables, engine 7.18.2: a `--hex` override for a hex that is neither the travel hex nor `--at` is
  refused).
- Keyed or deliberate: `acks.sh encounter start --monster "<MM note>" [--number N]`; a placed monster's lair check
  and lair numbers (warbands of gangs …): `--placed` (at a lair the party found by `search` there is no lair
  check: in its lair, engine 7.18.22; `--in-lair yes|no` says it outright). Entries with alternatives: `--choose <name>`.
- Distance: the line gives the maximum (2d6 × 10'); reduce it on the map until either side sees the other or its
  light, then `acks.sh encounter distance <feet>` (or `--seen-at` at start). The line lists the party's lit sources.
- Before committing to a lair (7.24): `lair-check --monster NAME --number N [--allies N:HD,...] [--floor HD]` gives
  its Hit Dice and largest blow against the party (the table rule "combat is a failure state": plainly outmatched at
  2x by default, a campaign setting).
- `acks.sh monster NAME` (the compendium's statblock) for the Judge-only fields. NPC parties: build them (hirelings
  reference) and add them to a fight with `state add`.

## 2. Surprise
Decide each side's foreknowledge and line of sight, then
`acks.sh encounter surprise --party fore,los|fore|los|none --monsters …` with, where they apply:
`--hiding <ids>`, `--sneaking <ids>` (whether or not their throw succeeded), `--monster-imposes -2` (a stealthy
monster entry), `--monster-cond blinded`, `--slumbering <ids>` / `--monsters-asleep`, `--members <ids>` (only those
present), `--group-surprise` (party by group, average bonus), `--each` (each monster rolls). Party rolls are open
(actor `avoid_surprise`, `surprise` penalties, deafened/blinded applied); monster rolls hidden. Both sides none: no
encounter. A monster note's penalty to others' surprise (a gelatinous mass's "Translucent: others -2", an orc band's
"Hunters"; engine 7.14.0) comes back as a JUDGE line with the verdicts the same dice give under it: if it applies
here, `encounter surprise --apply-note-penalty` records them. Never roll surprise again for it. A monster's own
"+N to avoid surprise" (engine 7.18.17) is applied from its note; when the note makes it conditional ("in natural
habitat", "at home"), the command refuses before rolling: give `--monster-bonus N` (it applies) or `--monster-bonus 0`.
`--party none --monsters none` warns when the party carries light and the monsters see in the dark: give `--monsters
los`.

## 3. Evasion
`acks.sh evade`: refused in a dungeon (the party can still flee in combat: `round-start --declare <id>:retreat`). In
the wilderness only when the Surprise Matrix allows and the party is not surprised (an explorer who is not surprised
can lead it away): the Evasion throw by terrain and party size (riders and large creatures count 2), with
`--explorer ID --familiar` (+5), `--monsters-fly` / `--party-flies`, `--forlorn N`, `--groups "A,B;C"` (sauve qui
peut), `--monster-speed FT` (else the statblock's); automatic if every monster is surprised. Success: distance and
direction of flight, then a hidden Navigation −4 (failure: lost and aware). Tracking pursuers: `acks.sh pursue
--wilderness`. Pursuit inside a fight: `acks.sh pursue <group> [--drop treasure|food] [--not-visible]`.

## 4. Reaction (if no one attacks)
`acks.sh reaction --tone diplomatic|intimidating|seductive [--face <id>] [--rmod <modifier>[=N] …] [--bribe
week|month|year|day]` — hidden. The face (highest CHA by default; whoever speaks first if disputed) brings CHA,
Diplomacy, Mystic Aura, Seduction, Intimidation and Bribery from the actor; wandering monsters get monster level −
dungeon level; the current attitude, outnumbering (`--party-count`, `--target-count`) and the target's morale score
(intimidation) are computed. Situational modifiers by name: `acks.sh reaction --tone diplomatic --list-mods` (e.g.
`--rmod trespassing --rmod believed_lawful_target_chaotic --rmod personally_harmed=-6`). If the whole party was
surprised, pick diplomatic or intimidating, whichever is worse for it. Narrate the behaviour, never the number.
- Attempts to influence: `acks.sh reaction --influence …` (time by attempt number in the line: advance it with
  `acks.sh turn --rounds N` / `turn N`); a bribe rides on an attempt. Not once fighting starts until weapons are laid
  down (`--weapons-down`) or the creatures must roll morale. New allies of intimidated creatures: the same roll with
  `--apply-total N`.
- Factions (7.23; `Campaign/faction-state.json`): `faction add|know|deal|rebuild|show|due`; `encounter start
  --faction ID` and `reaction` then apply what the faction knows of the party, print its standing and keep the result
  as its attitude; bribes and truces show on the clock when they end; restocking rolls of cleared rooms (`faction
  rebuild-roll ID ROOM`) when they fall due.
- Friendly monsters with fewer HD can be recruited via the hiring table (henchmen reference).

## 5. Talk or fight
NPCs and sapient monsters have wants; give unwritten ones two or three traits and a voice.
If it comes to blows: `acks.sh encounter fight [--perceived "<what the party sees>"] [--set ac=N]` creates the combat
state (config `tools.combat_state`) with the party (current hp from Campaign State), the monsters (statblock, hp rolled
hidden), the opening distance, surprised/slumbering creatures, winded PCs, intimidated (faltering) or overawed
(frightened) monsters. Then `combat-totm.md` from "Each round". After the fight: `acks.sh turn --rounds <rounds
fought>`, then `acks.sh encounter end` (it refuses an encounter that arrived and was never played without
`--unplayed "why"`; never clear an encounter in a batch).

After the encounter: hidden rolls to the Judge block; monsters slain or fled and treasure into World State and the
Ledger; `save.sh`.
