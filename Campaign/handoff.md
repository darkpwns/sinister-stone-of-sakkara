# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 8 · **day 59**, 07:01 · **Turos Tem** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Galerius | Fighter 2 | 3353 | 7/7 |  |
| Faustina | Priestess 2 | 3200 | 10/10 |  |
| Callista | Mage 2 | 3200 | 6/6 |  |
| Corvus | Explorer 2 | 3200 | 8/8 |  |
| Hrodric | Shaman 2 | 2999 | 7/7 |  |
| Severina | Venturer 1 | 567 | 7/7 |  |
| Marius | None (0th level) 0 | 78 | 4/4 |  |
| Petra | None (0th level) 0 | 0 | 3/3 |  |
| Titus | None (0th level) 0 | 0 | 3/3 |  |
| Varro | Crusader 1 | 0 | 3/3 |  |

- **Left behind:** lupa at Türos Tem (former henchman, bed rest at the inn) (since day 35)
- **Adventure:** A4 Pilgrimage to the Shrine of the White Lady (paid): Galerius (pc), Faustina (pc), Hrodric (pc), Callista (pc), Corvus (pc); lots 5; monsters 0 (0 XP); hoards unfound 0
- **Wages:** marius Marius: 12 gp/month; next due day 91; petra Petra: 12 gp/month; next due day 98; titus Titus: 12 gp/month; next due day 105; varro Varro: 25 gp/month; next due day 82; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 11; galerius[party] active hp 4/4 init 5; faustina[party] active hp 6/6 init 6; callista[party] active hp 5/5 init 6; corvus[party] active hp 6/7 init 5; severina[party] active hp 7/7 init 5; marius[party] active hp 4/4 init 6; lupa[party] active hp 3/3 init 4; st1[foe] dead hp 0/6 init 2 unconscious; st2[foe] dead hp -2/5 init 6 latched on corvus,unconscious; st3[foe] dead hp -3/4 init 3 unconscious; st4[foe] dead hp -1/8 init 2 unconscious; st5[foe] dead hp -5/3 init 5 unconscious; st6[f
- **Schedule:** day 60: month-end Month's end
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [camp-past-encounter] (1 slip): slipped on although enforced: the enforcement has a hole
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S09):** branch `claude/hopeful-ptolemy-1ea8tg` in this repo and the rules vault (the vault branch was created from its main in S08; nothing written to it yet); the tools clone on `tools.ref` (setup.sh puts it there). Set Campaign State `session:` to 9; new log `Session Log/S09 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad. Run 2 (run 1 archived: none of it holds).
- **Standing instructions (user):** unchanged from S08: the Judge plays the six AI players by profiles, heuristics and party notes (no party-agent calls); Gideon calls; the kingdom goal; the pooled purse with Faustina (`--payer faustina`); Buried Temple floors L1 6 HD, L2 12, L3 18; up to 4 henchmen (the party has 4); a downtime activity for every character between adventures; skilled old-school play (scout and count first); the fortress is a long-term goal; Hrodric's eagle by hand (`Characters/Hrodric's Eagle.md`, rescaled to 1 HD, 4 hp at his 2nd level).
- **In hand:** day 59, 07:01, Türos Tem, the whole company in town and rested. Month's end falls on day 60 (`schedule due`; `play.py month-end`). The purse with Faustina; 13,000gp with Karanos (`bank-karanos`; free withdrawal from day 82, 15% before). Henchmen: Marius, Petra, Titus (Severina), Varro (Faustina; Crusader 1, Rebuke Undead, Divine Blessing). Callista knows Slumber, Desiccate, Discern Magic. The legate's Parade Ground scroll is held (World State prep queue).
- **Next:** the party means to go down to the temple's second level (floor 12 HD: the five 2nd-level PCs, Severina, Varro and the three 0th-level henchmen make 15; without Hrodric and Severina 11, too few). Decide at the table whether the pups' trainers come (their courses pause: `train pause C21`-`C25` on leaving, `train resume` on return). Ways down the party knows: pay the purple one (100gp a head). Before leaving: `adventure start` + `join` for all ten, `play.py depart`, iron rations and water per member, metamphora, light, wages through the return plus a month (Marius due day 91, Petra 98, Titus 105, Varro 82). Weekly replacement rolls for the temple's cleared rooms (World State prep queue) run when they return.
- **Hiring:** month 3 from day 61 (0th and 1st level); the party is at its cap of 4 henchmen unless below the floor.
- **Town attitudes:** the legate Friendly (day 52); Genelen Friendly; Malyn Neutral (Callista); Malyn's apprentices Indifferent; Karanos, Socolo, Ilarion, Miren Unfriendly; Thales Hostile. Türos Aster's legate Indifferent.
- **Engine gaps to work around by hand** (Playtest/judge-notes.txt): harvest refuses monsters without a component row (R2 S02); captives sold after a payout earn XP by hand (R2 S03); a latched stirge's drain; round-auto stops when the only foe cowers; goods lots made with `--goods` cannot be split. S08: `camp` without `--hours` ran 16 hours on the road (pass `--hours 12`); `dice.py --dump hidden` lists only the current session number's rolls (set `session:` before the first roll of a chat).
