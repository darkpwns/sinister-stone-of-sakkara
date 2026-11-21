# Prompt for the next session (paste into a new cloud session)

Attach the repositories `darkpwns/sinister-stone-of-sakkara`, `darkpwns/acks2-tools`, `darkpwns/acks2-rules-vault`
and `darkpwns/kardakia-campaign`, then paste everything between the lines.

---

resume Sakkara

Continue the AX1 playtest campaign into Secrets of the Nethercity (AX2) as the Judge, using the `acks2-judge` skill
in `darkpwns/sinister-stone-of-sakkara`. Before anything else:

1. All four repositories: check out the branch `ccr-6e7c0096-7nmfvu` (the S08 work is there, not on the default
   branches); `mkdir -p /home/claude` and symlink each clone from /home/user into it
   (`ln -s /home/user/<repo> /home/claude/<repo>`). Run the skill's `setup.sh`: it must print
   `engine: ready: acks 7.13.7` (config `tools.ref` is `ccr-6e7c0096-7nmfvu`, `min_version` 7.13.7).
2. Read `Playtest/HANDOFF.md` from "## S08 (2026-11-21) — start here" to the end (the latest block, "day 196
   evening", is the state), then the S08 section of `Playtest/judge-notes.txt`, `Campaign/Rulings.md` (rows dated
   S08), and `Session Log/S08 — The road to Cyfaraun.md`. Start session S09 (Campaign State `session: 9`, a new
   session log `S09 — <summary>.md` linked in the Campaign Log).
3. Set `party.agent.call_dir` in `Campaign/campaign.yaml` to this chat's scratchpad. The Judge plays the AI party
   by `Party/profiles/`, `Party/heuristics.md` and `Party/party-notes.md` (no party-agent calls, no table talk),
   as in S06-S08.

Standing instructions from the user (S08):
- Every character uses all of his class powers and proficiencies where they apply (Lucilla's venturer powers in
  particular: Bribery, Mercantile Network, Rumormongering on a return visit, Magical Engineering on new magic items,
  Knowledge (history) where a key names it; Neris' Lay on Hands and Consolation; Vettius' Shadowy Senses and
  Streetwise; Brennus' Berserkergang and Healing; Iulia's Rebuke Undead and Theology; Vestus' Loremastery and
  Ancient Argollëan; Phaedra's Alchemy). Every henchman hired gets the proficiencies his level allows at hiring
  (`actor item ID add proficiency NAME --list class|general`).
- New PCs start at 1st level with reserve and funeral XP; higher-level help is hired as henchmen.
- The party's shrieker contingency (Party/party-notes.md): come down the second grate past the shrieking fungi;
  keep wide of the cavern locusts.
- The test continues until a TPK.

Routine that slipped in S08 (do it every time): `eat --in-town` before each rollover in town and pay the inn each
night; relight the torch when the line says it burns out; hourly miasma saves near the sludge (+4 with cloths) and
clear the condition after a turn's rest away from it; add a condition with a read-modify-write (`actor set
state.conditions` replaces the whole list); unsettling-event throws every 2 hours in the Nethercity; open a new
adventure (`adventure start`, `join` all nine) before each delve and pay out on return. New in 7.13.7:
`travel --care HEALER:PATIENT`, `encounter start --replace`, campaign tables by id (`table roll ax3-rumours`),
`mortal-wounds ID --type T` outside a fight; after a turn stops on an unresolvable wandering entry, run
`encounter start --monster NAME` for it.

Open issue: Vestus' inventory holder is still kind `hireling` (taken over in S07); his AC was set by hand.

Then give the recap (at most 5 lines) and continue play from day 196 evening in Cyfaraun. Commit and push after
every state write (`save.sh`), on branch `ccr-6e7c0096-7nmfvu`.

---
