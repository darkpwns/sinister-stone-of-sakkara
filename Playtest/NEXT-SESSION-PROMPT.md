# Prompt for the next session (paste into a new cloud session)

Attach the repositories `darkpwns/sinister-stone-of-sakkara`, `darkpwns/acks2-tools`, `darkpwns/acks2-rules-vault`
and `darkpwns/kardakia-campaign`, then paste everything between the lines.

---

resume Sakkara

Continue the Secrets of the Nethercity (AX2) playtest as the Judge, using the `acks2-judge` skill in
`darkpwns/sinister-stone-of-sakkara`. Before anything else:

1. All four repositories: check out the branch `ccr-6e7c0096-7nmfvu` (the S08-S10 work is there, not on the default
   branches); `mkdir -p /home/claude` and symlink each clone from /home/user into it
   (`ln -s /home/user/<repo> /home/claude/<repo>`). Run the skill's `setup.sh`: it must print
   `engine: ready: acks 7.13.7` (config `tools.ref` is `ccr-6e7c0096-7nmfvu`, `min_version` 7.13.7).
2. Read `Playtest/HANDOFF.md` from "## S10 (2026-11-21) — start here" to the end, the S10 section of
   `Playtest/judge-notes.txt`, `Campaign/Rulings.md` (rows dated S10), `Party/party-notes.md` and
   `Session Log/S10 — Return to the temple.md`. Start session S11 (Campaign State `session: 11`, a new session log
   `S11 — <summary>.md` linked in the Campaign Log).
3. Set `party.agent.call_dir` in `Campaign/campaign.yaml` to this chat's scratchpad. The Judge plays the AI party
   by `Party/profiles/`, `Party/heuristics.md` and `Party/party-notes.md` (no party-agent calls), as in S06-S10.
   Source `Playtest/tools/s10_j.sh` for the helpers; `Playtest/tools/melee2.py` runs a plain melee round.

What the party does next (user's instructions for S11):
1. Find someone to regenerate the lost ear, fingers and toes (Neris' ear, Marcellus' two fingers, Brennus' toe; the
   older wounds too if it can: Brennus' ear and teeth, Lucilla's eye and ear). Leads are in the handoff: Repair
   Disfigurement and Disability (divine 4th), the Solar Citadel's Prelate Romus and Patriarch Arëtar, the temples'
   spellcasting services, `restore ... --limbs N`.
2. Then the party really brainstorms a way to get around the mummies' horrific visage: it has caused trouble in every
   mummy fight and is getting dangerous. Play the brainstorm by the profiles (each player's idea and how the caller
   settles it), look up every rule the ideas touch before ruling, record any new ruling, and write the party's plan
   into the party notes.

Standing instructions from the user (S08-S10):
- Every character uses all of his class powers and proficiencies where they apply (Lucilla's venturer powers:
  Bribery (proficient row), Mercantile Network, Rumormongering once a month per city, Magical Engineering on new magic
  items, Diplomacy, Knowledge (history) where a key names it; Neris' Lay on Hands every day and Consolation; Vettius'
  Shadowy Senses and Streetwise; Brennus' Berserkergang and Healing; Iulia's Rebuke Undead, Theology and her prayers;
  Vestus' Loremastery and Ancient Argollëan; Phaedra's Alchemy; Aelia's Inspire Courage, Loremastery, Magical
  Engineering; Hrodvar's Engineering and Healing). Every henchman hired gets the proficiencies his level allows.
- New PCs start at 1st level with reserve and funeral XP; higher-level help is hired as henchmen.
- Party strength floor per depth band (Upper 18, Lower 24, Deep 30, Abyssal 39, Sub-Abyssal 48): levels of PCs and
  henchmen, 0th level 1 HD, a henchman advanced from 0th 1.5 HD at 1st and 2 at 2nd. A death that drops the party
  below the floor of its band turns it back.
- The party keeps the henchmen it has; it hires again only when its strength falls below the floor of the band it is
  working.
- The party delves as adventurers: multi-day expeditions toward the deepest, richest areas its strength allows,
  sleeping below in sealed, spiked rooms; it spikes doors and sets traps for monsters it knows about.
- Taxes: one selling day a month, early in the month, for coin and gems; elven relics go to Liber Faunus at 80%.
- The shrieker contingency (party notes): come down the far grate; keep wide of the cavern locusts.
- The test continues until a TPK.

Routine (do it every time): `eat --in-town` before each town rollover and pay the inn each night; after a delve day,
clear `sleep_due`/fatigue after the inn night (`wait` records no sleep); advance one turn at a time, rest every 5
turns, relight torches when they burn out; hourly miasma saves near the sludge (+4 with cloths), cleared after a
turn's rest away; unsettling-event throws every 2 hours below; conditions with a read-modify-write (`cadd`/`crem`);
mummy rot by hand (no magical healing until Cure Disease); open a new adventure before each delve and pay out on
return; equip magic weapons before going down; only military oil is a weapon; after `sell`, receive the proceeds and
split them by shares (`inv give` moves coins between holders); never let a scripted loop run past an arriving
encounter or a fallen character.

Open issues: Vestus' inventory holder is still kind `hireling`; Neris and Vestus cannot be employers (retinue
members); the Silk Pony stalls are owed from day 243.

Then give the recap (at most 5 lines) and continue play from day 243 morning in Cyfaraun. Commit and push after every
state write (`save.sh`), on branch `ccr-6e7c0096-7nmfvu`.

---
