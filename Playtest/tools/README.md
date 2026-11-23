# Playtest tools

The helpers of S06-S28 are retired (2026-11-23, S29 engineering): what was proven lives in the Judge skill's
`scripts/` with tests (`scripts/tests/test_scripts.py`) or in the engine. Nothing in `retired/` is to be sourced or
run in play: the files are kept as the record of how sessions S06-S28 were driven.

| Retired helper | Now |
| --- | --- |
| `w N` (walk), `relight`, `lit`, `t` (s10/s22/s23_j.sh) | `python3 $S/play.py walk N --relight A,B`; the engine's `light auto on --carriers A,B`; `turn N` stops in the turn the light dies. The old `w` stopped at any timer expiry and its lit test broke twice: `walk` reads `light show --json` and goes on past a timer |
| `sup` | `play.py supplies [ID …]` |
| `bank DAY` | `play.py bank --to guildhouse-bank --keep 150` |
| `gh_balances.py` | `play.py bank-balances --bank guildhouse-bank [--day N]` |
| `tday`, `innnight`, `slept`, `dawn` (s12/s20_town.sh) | not needed: `location --settlement NAME` once, then `wait`: town meals are assumed, a town night is restful sleep, spells come back (engine 7.14.0, 7.17.2) |
| `cadd` / `crem` / `conds` | `play.py cond add|remove|list ID "TEXT"`; worn items and standing powers are `actor mod`, not conditions |
| `s15_ledger.py`, `s23_ledger.py` (payout rows into the Ledger) | `play.py payout [options]` |
| `miasma`, `clearmiasma` (hourly sludge saves) | a module procedure: `acks.sh batch` with one `save ID death --mod 4` per member, `play.py cond add` for those who fail; worth a schedule-like item if the sludge is revisited |
| `melee.py`, `melee2.py`, `fight.py`, `brawl.py`, `choke.py`, `undead_driver.py`, `s13_pudding.py`, `s22_sgrind.py`, `s23_crawl.py`, `s23_ghoul.sh` (fight drivers) | retired without replacement: they resolved actions out of initiative order and without distances. Step fights with `round-start` / `round-next` and act for the combatant it names (the lessons index reminds on an action out of its count); a moment's independent rolls go in one `acks.sh batch` |
| `s27_g10.py`, `s28_ward.py`, `s28_g13.py`, `s28_faewyrd.py` (ward and whisper drivers) | the engine's `state ward` and `state aura` (engine 7.17.6: per-creature barrier, saves at each creature's own initiative); the lessons `underwatch-ward` and `faewyrd-whispers` print the commands |
| `day.sh` (AX1 overland: march, night) | the engine's `travel`, `camp --watches` in one `acks.sh batch` |
| `s11_mend.sh`, `s13_j.sh`, `s09_j.sh`, `j.sh` | one-off session scripts |

`map/` (the AX3 grid helpers) is unchanged.
