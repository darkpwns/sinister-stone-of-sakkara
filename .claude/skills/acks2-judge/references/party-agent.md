# The AI party agent: calls, formats, PC creation and hiring by call

Load this only when the Judge makes a party-agent call (the Table rules do not say the Judge plays the AI players
itself), or when the AI players make their PCs or hire by call. The structures and who declares are in
`party-structure.md`. `P` = `python3 $S/party.py`, `$CALL` = config `party.agent.call_dir`.

## The wall
The agent gets only what `party.py build` assembles: the base instructions (`Party/prompt/base.md`), the Table rules lines, the active players' profiles, `Party/heuristics.md`, the players' memory notes and party notes (`Party/`), the PCs' and their henchmen's actors as players see them (the engine's player view, without the `judge` block), rumours heard (the rumours note's heard section), rules text the Judge passes, and the scene brief. `build` refuses if the variable part contains a Judge-only note title, marker or callout, or any 8-word run shared with Judge-only text (Judge-only folders and files, tagged notes, Judge-only and Judge-block callouts, every actor's `judge` block, the rules repo's bestiaries) that is not also in player-facing text; it refuses rules notes under config `party.agent.rules_refused`. `check` runs the same scan on the agent's output and flags statistic-like terms for the Judge to confirm. The scene brief follows secrecy exactly as narration does (SKILL.md §4): perceived descriptions, never true names before they are learned, never AC, hp, morale, hidden rolls or key contents.

The agent reads its prompt from the file `build` wrote and makes no other tool call: the Agent prompt is one line pointing at that file, the file says to use no other tool, and `check` accepts a fresh call's output only with exactly 1 tool use and the file's call code in the declaration's first line (a random code that exists only in that file, so the one tool use was the read of it). `check` also rejects another call's code. The check cannot tell which tool made that one call: a single command that read the prompt and other files at once would pass the count; the output scan still runs on every declaration.

## When to call
- Every decision point where AI players must act: a town step, a travel day's choices, each exploration turn that needs a decision, each encounter after distance and surprise (talk, fight, flee), each parley exchange, hiring offers (`hire`), dividing treasure (`split`), and the session end (`end`).
- **Combat:** once per round for all AI PCs, at the start of the round (declarations come before initiative): type `combat`, the Tracker line filled.
- **Not** for narration without a choice, rolls the rules make automatic, or routine turns under standing orders the caller has given ("search each room for 1 turn, listen at every door"): resolve those turns and call at the next real decision. Say in the brief which standing orders are in force.
- **Impulses:** add `--impulse` to `stub` for `decide`, `combat`, `hire` and `split` calls. It rolls each active player's impulse die with `dice.py --hidden` (logged, so it goes to the Judge block) and writes the result line.

## How to call
1. `P stub --type T --step N [--impulse] > $CALL/brief-N.md`. Fill the placeholders (Perceived, Open rolls this step, Judge answers, Caller's declaration in mixed, Open question); correct the Party line if needed. Step numbers run through the session.
2. Rules text, only when the decision turns on a player-side rule the players might not have in mind: `--rules "Note name#Heading"` (from the rules vault) or `--rules-file F` (a short Judge-written answer, with its source). Never monster rules, bestiaries, adventure text or the Judges Journal.
3. `P build $CALL/brief-N.md [--rules …] [--site "<site as the party knows it>"] --out $CALL/prompt-N.md` → its first line must end `wall ok`; its second line is `agent prompt: <one line>`. `--site` adds the party's map notes for that site. `build` wraps lines over 1,900 characters and refuses a prompt over 80,000 characters.
4. Call the **Agent** tool: `subagent_type: general-purpose`, `model: sonnet`, `run_in_background: false`, `description: "Party step N"`, `prompt`: the `agent prompt:` line's text after the label, unchanged. Never Read `prompt-N.md` and never type its text into the call: the agent reads it. (Agent definitions in `.claude/agents/` do not load in claude.ai chats; tested 2026-11-17.)
5. Write the reply text to `$CALL/decl-N.md`, then `P check $CALL/decl-N.md --brief $CALL/brief-N.md --prompt $CALL/prompt-N.md --tokens <subagent_tokens> --tool-uses <tool_uses>` (both from the Agent result's usage block). This logs the call. A fresh call must show `tool_uses` 1.
6. **Malformed** (exit 1): one retry. SendMessage to the same agent: "Your declaration is malformed: <the error lines>. Reply again with the corrected declaration only, no tools." Check again with `--retry --tokens 0` (a SendMessage reply reports no usage). If the corrected reply differs from `decl-N.md` only by lines removed or moved, make that change to the file with a short edit instead of writing the whole reply again. Still malformed, or a WALL error: stop and ask the user with AskUserQuestion: resolve from the best reading of it / call again fresh / the user writes the declaration. A WALL error also means: discard the output; fix the brief first if the error names brief text.
7. Resolve the declaration like a human caller's (check every action against the rules and the tracker; an impossible action becomes what the character manages). Questions to Judge are answered out of character in the next brief's **Judge answers**, from player-side rules (with the source) or by narration, never from Judge-only material. A rules question goes through the same order as the Judge's own (SKILL.md §3 item 4: engine, table row, cache, full lookup); the Judge still decides what a player may be told.

## Split party and private calls
- **Split party:** each group out of contact gets its own brief and call: add `--players id,id` to `stub`, `build` and `check` for a group of AI players. A group of one AI player gets a private call; the user's group in mixed play is handled as usual.
- **Private call** (`stub --private <Player>`): a player has information the others must not share: a secret action (pickpocketing a companion, a hidden deal), a private conversation with an NPC, a charmed or possessed PC (the brief says what the PC now feels and wants, as the player would be told), a split party. The prompt holds only that player's profile and memory, that PC's and its henchmen's actors and the private brief; `check` expects a `### Private declaration`. What the others could notice goes into the next party brief as narration.

## Showing it to the user
Never paste a whole declaration into the reply. `P talk $CALL/decl-N.md` prints the compact form: one **Table** line (speaker: line · …), the **Call**, any **Defiance** and **Questions**; show it before the narration of the result. In combat, show only the lines that matter and the individual actions as they resolve.

## Memory
At each state save (§7 of SKILL.md), run `P memory $CALL/decl-*.md` for the declarations since the last save (keep a list; never apply one twice), then read the changed notes: drop any suggested note the party could not know, keep the players' mistakes as they are (never correct them from hidden knowledge), then `save.sh`. Map notes are written as the mapper described them. At session end make an `end` call, apply its memory updates, and prune each player's sections to about 8 bullets.

## Cost
Each call's `subagent_tokens` (from the Agent result) is logged by `check`; a SendMessage retry reports no usage, so check it with `--retry --tokens 0`. At session end `P costs` prints one line per call and the total; put them in the session log's Judge block. Measured in the 2026-11-17 dry run (24 calls): 86–98k subagent tokens per call (mean 92k), of which the general-purpose subagent's own context is about 80k; the party prompt itself was about 4.3–4.6k tokens with two AI players and 6.8–8.6k with six. Until 2026-11-18 the Judge read the prompt file and typed it into the Agent call, so each call put the prompt into the Judge's context twice (13.6–17.2k tokens with six players), and that dry run's chat ran out of context; now the agent reads the file and the Judge's context takes only the one-line pointer, the brief and the declaration. Measured in the 2026-11-18 dry run (24 calls, 17 with six AI players, 7 mixed with two): about 1.7k tokens of Judge context per call (brief text, pointer, the declaration as received and as written to `decl-N.md`, script output), against about 13.6k more per call that the old two prompt copies would have added (327k over the 24 calls). The declaration, about 2.4k characters, is now the largest part. Subagent cost is unchanged: 94–108k Sonnet tokens per call (mean 99k).

## Scene brief (Judge → party)
Exactly these headings, nothing else (`stub` writes the skeleton):
```
### Scene brief — S## · step <n> · <date>, <time> · <place>
**Call:** <type> · <structure> · caller <AI player, or "the user (<PC>)"> · declare for <PC (Player), ...>
**Perceived:** <narration: what the characters see, hear, smell; no Judge-only content>
**Party:** <name (player or "henchman of X") hp/max conditions; ...> · light <...> · rations <...> · marching order <...>
**Tracker:** <round, order, engaged, distances — only in combat; else "none">
**Open rolls this step:** <one line per open roll, or "none">
**Judge answers:** <answers to the last declaration's questions, out of character; or "none">
**Caller's declaration:** <mixed: the user's declaration verbatim; else "n/a">
**Impulse:** <from stub --impulse, or "none">
**Open question:** <the decision in front of the party, one line, no hidden options>
```
Types: `decide`, `combat`, `counsel`, `hire`, `split`, `create-a`, `create-b`, `create-c`, `end`, `private`. A private brief starts `### Private brief — S## · step <n> · <Player>` and has the same headings. Standing orders in force go at the end of Perceived.

## Party declaration (party → Judge)
Exactly these headings, in this order:
```
### Party declaration — S## · step <n>
**Table talk:**
- <Player>: <line>
**Caller:** <the consolidated decision for the party, one or two lines>
**Marching order:** <front to back, or "unchanged">
**Individual actions:**
- <PC> (<Player>): <action, target, movement; spell named and target if casting>
**Defiance:** none | - <Player>: <what, and which breaking point>
**Character choices:** (create-a/b/c calls only) - <Player>: <choices>
**Questions to Judge:** none | - <Player>: <question>
**Memory updates:** none | - <Player>: <Grudges|Debts|Lessons learned|Opinions of NPCs|Henchmen and hirelings>: <note> | - Party notes: <Rumours|Plans|Map notes>: <note> (Map notes: <site>: <note>)
```
At most 3 table-talk lines per player. Every PC after "declare for" has one individual action (except `counsel`, `end`, `create-*`). In mixed play the Caller line restates the user's call ("Following <caller>: …"); in `counsel` it is "Awaiting the caller." A private declaration starts `### Private declaration — S## · step <n> · <Player>` and has the same headings (Caller "n/a").

Changes from step 3: the brief gained step numbers, **Call**, **Judge answers**, **Caller's declaration** and **Impulse**; the declaration gained **Defiance**, **Character choices**, **Questions to Judge** and **Memory updates**, and table talk became one bullet per line with the player's name.

## Making the AI players' PCs
Rules: RR Creating a Character (pp. 13–14), Character Attributes (pp. 14–15), the class notes (`03 Classes/`), Character Templates and Intellect (RR pp. 23–24), Hit Points, Starting Age, Languages. Table rule **Character creation**: templates (RR default) or no templates (the optional rule: 3d6 × 10 gp, buy gear, choose proficiencies and spells). Each AI player makes one 1st-level PC; the agent chooses, the Judge rolls and builds.
1. **`create-a`.** Pass `--rules "Character Attributes#Generating Attributes"` and `--rules "Creating a Character"`, plus the class list (`--rules "Core Classes"` / `"Campaign Classes"` as the Table allows; the Table rule "Classes allowed" is in the prompt already). For each class the Table plays under a campaign name (`campaign.yaml` tools.class_aliases), add its reskin note from `paths.class_notes` with `--note "<campaign class>#Who they are"`: the players choose it by its campaign name. The Player Reference Guide's homelands and backgrounds are in the base knowledge of the players only through the brief: summarise the PC backgrounds paragraph in Perceived. Each player names the 5d6 attribute, the two 4d6 attributes, a hoped-for class and a fallback, and a homeland.
2. **Judge rolls** attributes open, per player: `dice.py --open "<Player> STR:5d6"`… then drop the lowest dice as the rule says; record scores and modifiers.
3. **`create-b`.** The brief lists each player's six scores and modifiers (Open rolls). Pass the chosen classes' notes up to `## Templates` (`--rules "Fighter#Requirements…"` as needed, or a Judge summary of key attributes and minimums with `--rules-file`). A reskinned class goes as a pair: the RR class's vault note for the rules (`--rules "<RR class>"`) together with its reskin note (`--note "<campaign class>"`; `party.py build` passes only the note's player sections and refuses it if anything Judge-only is left). Never pass a reskin note with `--rules-file`: that sends its Judge-only callouts (the wall refuses it). Each player picks a class meeting its minimums, name, sex, alignment, one-line background, and whether to keep a character whose modifiers sum below 0 (if no, re-roll from step 2 for that player).
4. **Judge rolls** hp (class Hit Die, 4 or less counts as 4, + CON), template 3d6, starting age, all open.
5. **`create-c`.** The brief's Open rolls restate each player's six scores (the sheets do not exist yet, so the prompt has no other copy; without INT the players cannot choose INT proficiencies), with the hp and template rolls. Pass each class's template table (`--rules "<Class>#Templates"`; for a reskinned class `--note "<campaign class>#Templates"` instead, whose rows carry the campaign's gods and devices) and Character Templates and Intellect. Each player keeps the rolled template or takes a lower one, and picks the extra general proficiencies (and spells, for studious casters) their INT gives. With no templates: gear bought from the gp rolled, proficiencies and spells chosen (pass the equipment and proficiency lists the Table allows).
6. **Judge builds** each PC's actor `Characters/<id>.json`: his numbers as a sheet-shaped YAML file in the call dir (the keys `acks.sh actor show` prints), then `charsheet.py import <file> <id>` (characters.md, role pc; a reskinned class under its campaign name, its template from the reskin note) under the rules, checks it, sets config `party.active_players[].pc`, makes him an inventory holder and puts in his template's equipment item by item (`inventory.md` Setup; with no templates, each purchase is an `inv buy` paid from the gp rolled), commits.
A replacement PC after a death goes through the same three calls for that player alone (private calls) at the next point where a new character can join.

## Hiring session for the AI players
Only if Table rules let AI players hire their own henchmen. In town, after creation:
1. A `decide` call: which hirelings each player wants (henchman, men-at-arms, torch-bearers), how many, how much they will spend. Pass `--rules "Hirelings, Henchmen, Mercenaries, and Specialists"` and `--rules "Henchmen"` (wages, number, maximum level) as needed.
2. The Judge runs henchmen-hirelings.md: search fees (taken from the employer's coins), availability (hidden), candidates generated (characters.md) and presented as people.
3. A `hire` call: each player makes offers to the candidates in front of them (wage, share, signing bonus, terms); Rosa-style haggling and Ingrid-style contracts are expected. One candidate can be wanted by two players: the caller settles it in the declaration.
4. The Judge rolls each hiring reaction hidden and narrates the answers; a further `hire` call for re-offers if any. Henchman actors get `hired.employer: <PC name>`; the employer's player directs them as Table rules (Henchman control) say.
5. Wage and share arguments later (a `split` or `decide` call) are normal table talk; the agreed terms go in the employer's memory (Henchmen and hirelings) and the Ledger.
