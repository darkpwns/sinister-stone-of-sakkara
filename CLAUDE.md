# Sakkara playtest — operating manual

Test instance (2026-11-20; repo `darkpwns/sinister-stone-of-sakkara` since 2026-11-21): AX1 *The Sinister Stone of Sakkara* run as a campaign of the `acks2-judge` skill
(`.claude/skills/acks2-judge/`, a copy of the one in `darkpwns/kardakia-campaign`), AI party of six, to test whether
the engine and skill are adequate for running a published adventure. Kardakia's master state and display page are
not touched.

- **Run 3 (from 2026-11-25):** a fresh campaign of AX1 with six new PCs (five attribute sets each, the best kept; no
  templates; at least one animal trainer); the party's standing goal is to finish AX1 (Campaign State Table rules).
  Runs 1 (S01-S54) and 2 (S01-S16) are archived in `Archive/Run 1 (S01-S54)/` and `Archive/Run 2 (S01-S16)/` and hold
  no state for run 3; `Playtest/` is run 1's engine-test record. Back-up characters: `Characters/backups/`; the Judge's
  NPC attribute sets: `Campaign/npc-pool/`.
- Rules: `darkpwns/acks2-rules-vault`; engine `darkpwns/acks2-tools` on `tools.ref`; ACKS II as written, no supplements.
- Module notes (Judge only): `Adventure/` (hub `AX1 Hub.md`, town, forest, level keys, `Bestiary/`, `Tables/`, `Markets/`).
- State: `Campaign/` (Judge only), actors in `Characters/`, logs in `Session Log/`.
- Ruling order: room/area note → `Adventure/AX1 Hub.md` procedures → engine → rules → `Campaign/Rulings.md`.
- Party decisions follow `Party/profiles/` and `Party/heuristics.md`; the party agent (`party.py`) is used at a few
  decision points only (cost).
- Playtest record: `Playtest/REPORT.md` (per delve), `Playtest/judge-notes.txt` (voids, slips, corrections, findings), `Playtest/HANDOFF.md` (where play stands, how to resume), `Playtest/tools/` (fight and travel helpers).
- Commit and push after every save (`save.sh`).
