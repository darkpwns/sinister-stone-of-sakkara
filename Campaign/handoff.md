# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 7 · **day 50**, 18:01 · **24.19** (wilderness)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Galerius | Fighter 1 | 647 | 4/4 |  |
| Faustina | Priestess 1 | 617 | 6/6 |  |
| Callista | Mage 1 | 617 | 5/5 |  |
| Corvus | Explorer 1 | 617 | 7/7 |  |
| Hrodric | Shaman 1 | 453 | 6/6 |  |

- **Left behind:** lupa at Türos Tem (former henchman, bed rest at the inn) (since day 35); severina at Türos Tem (Severina training her pups) (since day 46); marius at Türos Tem (Severina training her pups) (since day 46); titus at Türos Tem (since day 46)
- **Adventure:** A4 Pilgrimage to the Shrine of the White Lady (open): Galerius (pc), Faustina (pc), Hrodric (pc), Callista (pc), Corvus (pc); lots 5; monsters 0 (0 XP); hoards unfound 0
- **Wages:** marius Marius: 12 gp/month; next due day 91; petra Petra: 12 gp/month; next due day 98; titus Titus: 12 gp/month; next due day 105; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 11; galerius[party] active hp 4/4 init 5; faustina[party] active hp 6/6 init 6; callista[party] active hp 5/5 init 6; corvus[party] active hp 6/7 init 5; severina[party] active hp 7/7 init 5; marius[party] active hp 4/4 init 6; lupa[party] active hp 3/3 init 4; st1[foe] dead hp 0/6 init 2 unconscious; st2[foe] dead hp -2/5 init 6 latched on corvus,unconscious; st3[foe] dead hp -3/4 init 3 unconscious; st4[foe] dead hp -1/8 init 2 unconscious; st5[foe] dead hp -5/3 init 5 unconscious; st6[f
- **Schedule:** nothing due on day 50
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [camp-past-encounter] (1 slip): slipped on although enforced: the enforcement has a hole
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S08):** branch `claude/hopeful-ptolemy-1ea8tg` in this repo and the rules vault; the tools clone on `tools.ref` (`ccr-6e7c0096-7nmfvu`, engine 7.22.1; setup.sh puts it there). Set Campaign State `session:` to 8; new log `Session Log/S08 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad. Run 2 of the campaign (run 1 archived in `Archive/Run 1 (S01-S54)/`: none of it holds).
- **Standing instructions (user):** the Judge plays the six AI players by `Party/profiles/`, `Party/heuristics.md` and `Party/party-notes.md` (no party-agent calls); Gideon calls. The party's goal is a magical kingdom (Table rules; heuristics "The kingdom"). Finances pooled: the company purse with Faustina (`--payer faustina`), the company chest at the Traveler's Inn (Rulings R2 S03); henchmen keep their own shares. Delve floors for the Buried Temple: L1 6 HD, L2 12, L3 18 (Rulings R2 S02); up to 4 henchmen as the purse allows, more only below the floor. **Every character has a downtime activity between adventures** (S05). Play the AI party as skilled old-school players: count the enemy and scout before committing; no fair fights (S07 end).
- **In hand:** day 50, 18:01, camp on the imperial road in 24.19, about 9 miles from Türos Tem. The pilgrims: Galerius (F1), Faustina (Pr1), Hrodric (Sh1; his eagle by hand, `Characters/Hrodric's Eagle.md`, 2/2 hp), Callista (M1), Corvus (Ex1), both donkeys. Adventure A4 (pilgrimage) open: L38 6,000gp on donkey1 (bearer), L34-L37 four pieces of jewelry with Faustina (6,300gp true). In Türos Tem: Severina (Ven1) with her henchmen Marius, Petra, Titus (0th level), all `party remove --stays`; former henchman Lupa at the inn (one leg, bed rest to day 47).
- **On arrival in Türos Tem (day 51):** `location --settlement "Turos Tem"`; `adventure return`; sell or keep the jewelry; `payout --ledger --apply` (about 12,300 XP over five shares: each pilgrim to 2nd level, the one-level cap); `level-up --sheet ID --apply` for each; Ledger rows; pool the PCs' coin with Faustina; `party add` Severina and the henchmen; `train resume` C21-C23 (paused day 46; tricks from day 76 once resumed; Severina's C24-C25 tamed day 49, running). Hrodric's eagle rescales with his level (its note gives the formulas: HD = his HD - 1).
- **Next adventures the party knows:** the Buried Temple (L1 explored in part: World State; L2 reached by the stairs at 18 or 53, the well at 42, or 75 under the ziggurat; Idimmu the purple wyrm takes 100gp a head to go below); the Shrine of the White Lady (23.16, unicorn; never reached: the party got lost twice, so take a guide or follow the river); the Ruined Imperial Fortress (26.19): the **long-term** kingdom goal only (about 180 HD of bugbears; World State prep queue); the party scouts and builds up first (levels, 1st-level henchmen once its PCs are 2nd, mercenaries much later).
- **Hiring:** month 2 searches done (Marius, Petra, Titus); month 3 from day 61. Once the PCs are 2nd level they may seek 1st-level henchmen (`recruit … --level 1`).
- **Town attitudes:** Genelen Friendly; the legate Indifferent; Malyn's apprentices Indifferent (Miren will speak against the party to Malyn); Karanos, Socolo, Ilarion, Miren Unfriendly; Thales Hostile. Türos Aster's legate Indifferent.
- **Engine gaps to work around by hand** (Playtest/judge-notes.txt): harvest refuses monsters without a component row (Rulings R2 S02: their XP value, `recover --goods`); captives sold after a payout earn XP by hand (R2 S03); a latched stirge's drain; round-auto stops when the only foe cowers; goods lots made with `--goods` cannot be split.
