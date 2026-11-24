# Sakkara playtest — operating manual

Test instance (2026-11-20; repo `darkpwns/sinister-stone-of-sakkara` since 2026-11-21): AX1 *The Sinister Stone of Sakkara* run as a campaign of the `acks2-judge` skill
(`.claude/skills/acks2-judge/`, a copy of the one in `darkpwns/kardakia-campaign`), AI party of six, to test whether
the engine and skill are adequate for running a published adventure. Kardakia's master state and display page are
not touched.

- **Run 2 (from 2026-11-24):** a fresh campaign (AX1, then AX2 SOTN) with six new PCs; the party's standing goal is a
  magical kingdom (Campaign State Table rules). Run 1 (S01-S54) is archived in `Archive/Run 1 (S01-S54)/` and holds no
  state for run 2; `Playtest/` is run 1's engine-test record.
- Rules: `darkpwns/acks2-rules-vault`; engine `darkpwns/acks2-tools` on `tools.ref`; ACKS II as written, no supplements.
- Module notes (Judge only): `Adventure/` (hub `AX1 Hub.md`, town, forest, level keys, `Bestiary/`, `Tables/`, `Markets/`).
- State: `Campaign/` (Judge only), actors in `Characters/`, logs in `Session Log/`.
- Ruling order: room/area note → `Adventure/AX1 Hub.md` procedures → engine → rules → `Campaign/Rulings.md`.
- Party decisions follow `Party/profiles/` and `Party/heuristics.md`; the party agent (`party.py`) is used at a few
  decision points only (cost).
- Playtest record: `Playtest/REPORT.md` (per delve), `Playtest/judge-notes.txt` (voids, slips, corrections, findings), `Playtest/HANDOFF.md` (where play stands, how to resume), `Playtest/tools/` (fight and travel helpers).
- Commit and push after every save (`save.sh`).
