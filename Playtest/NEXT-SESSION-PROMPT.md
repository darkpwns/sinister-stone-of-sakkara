# Prompt for the next session (paste into a new cloud session)

Attach the repositories `darkpwns/sinister-stone-of-sakkara`, `darkpwns/acks2-tools`, `darkpwns/acks2-rules-vault`
and `darkpwns/kardakia-campaign`, then paste everything between the lines.

---

resume Sakkara

Continue the Secrets of the Nethercity (AX2) playtest as the Judge, using the `acks2-judge` skill in
`darkpwns/sinister-stone-of-sakkara`. Before anything else:

1. All four repositories: check out the branch `ccr-6e7c0096-7nmfvu` (the S08-S09 work is there, not on the default
   branches); `mkdir -p /home/claude` and symlink each clone from /home/user into it
   (`ln -s /home/user/<repo> /home/claude/<repo>`). Run the skill's `setup.sh`: it must print
   `engine: ready: acks 7.13.7` (config `tools.ref` is `ccr-6e7c0096-7nmfvu`, `min_version` 7.13.7).
2. Read `Playtest/HANDOFF.md` from "## S09 (2026-11-21) — start here" to the end, the S09 section of
   `Playtest/judge-notes.txt`, `Campaign/Rulings.md` (rows dated S09), `Party/party-notes.md` and
   `Session Log/S09 — The deep galleries.md`. Start session S10 (Campaign State `session: 10`, a new session log
   `S10 — <summary>.md` linked in the Campaign Log).
3. Set `party.agent.call_dir` in `Campaign/campaign.yaml` to this chat's scratchpad. The Judge plays the AI party
   by `Party/profiles/`, `Party/heuristics.md` and `Party/party-notes.md` (no party-agent calls), as in S06-S09.
   Copy `Playtest/tools/s09_j.sh` to the scratchpad and source it for the helpers.

Standing instructions from the user (S08-S09):
- Every character uses all of his class powers and proficiencies where they apply (Lucilla's venturer powers:
  Bribery, Mercantile Network, Rumormongering on a return visit, Magical Engineering on new magic items, Knowledge
  (history) where a key names it; Neris' Lay on Hands every day and Consolation; Vettius' Shadowy Senses and
  Streetwise; Brennus' Berserkergang and Healing; Iulia's Rebuke Undead and Theology; Vestus' Loremastery and Ancient
  Argollëan; Phaedra's Alchemy; Aelia's Inspire Courage, Loremastery, Magical Engineering; Hrodvar's Engineering).
  Every henchman hired gets the proficiencies his level allows at hiring.
- New PCs start at 1st level with reserve and funeral XP; higher-level help is hired as henchmen.
- Party strength floor per depth band (Upper 18, Lower 24, Deep 30, Abyssal 39, Sub-Abyssal 48): levels of PCs and
  henchmen, 0th level 1 HD, a henchman advanced from 0th 1.5 HD at 1st and 2 at 2nd. A death that drops the party
  below the floor of its band turns it back.
- Keep only the henchmen the floor needs: when the party is at strength without one, it lets him go (every henchman
  is a half share of treasure).
- The party delves as adventurers: multi-day expeditions toward the deepest, richest areas its strength allows,
  sleeping below in sealed, spiked rooms; it spikes doors and sets traps for monsters it knows about.
- The shrieker contingency (party notes): come down the far grate; keep wide of the cavern locusts.
- The test continues until a TPK.

Routine (do it every time): `eat --in-town` before each town rollover and pay the inn each night; after a delve day,
clear `sleep_due`/fatigue after the inn night (`wait` records no sleep); advance one turn at a time and relight the
torch when it burns out; hourly miasma saves near the sludge (+4 with cloths), cleared after a turn's rest away;
unsettling-event throws every 2 hours below; conditions with a read-modify-write (`cadd`/`crem`); open a new adventure
before each delve and pay out on return; equip magic weapons before going down; only military oil is a weapon; after
`sell`, receive the proceeds and split them by shares with pay/receive pairs.

Open issues: Vestus' inventory holder is still kind `hireling`; Neris and Vestus cannot be employers (retinue
members); Quirinus' enervation saves are not modelled (roll a Death save each morning by hand).

Then give the recap (at most 5 lines) and continue play from day 219 midday in Cyfaraun. Commit and push after every
state write (`save.sh`), on branch `ccr-6e7c0096-7nmfvu`.

---
