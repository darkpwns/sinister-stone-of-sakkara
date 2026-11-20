# Sakkara playtest — operating manual

Local test instance (2026-11-20): AX1 *The Sinister Stone of Sakkara* run as a campaign of the `acks2-judge` skill
(`.claude/skills/acks2-judge/`, a copy of the one in `darkpwns/kardakia-campaign`), AI party of six, to test whether
the engine and skill are adequate for running a published adventure. Kardakia's master state and display page are
not touched.

- Rules: `darkpwns/acks2-rules-vault`; engine `darkpwns/acks2-tools` on `tools.ref`; ACKS II as written, no supplements.
- Module notes (Judge only): `Adventure/` (hub `AX1 Hub.md`, town, forest, level keys, `Bestiary/`, `Tables/`, `Markets/`).
- State: `Campaign/` (Judge only), actors in `Characters/`, logs in `Session Log/`.
- Ruling order: room/area note → `Adventure/AX1 Hub.md` procedures → engine → rules → `Campaign/Rulings.md`.
- Party decisions follow `Party/profiles/` and `Party/heuristics.md`; the party agent (`party.py`) is used at a few
  decision points only (cost).
