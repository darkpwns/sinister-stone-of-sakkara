# Party structure

Read config `party.structure` (also in Campaign State Table rules). Load this file at session start if it is not `solo-henchmen`. The agent calls themselves (when to call, how, the wall, the brief and declaration formats, memory updates, making the AI players' PCs and their hiring session) are in `party-agent.md`: load it only when a call is about to be made.

## solo-henchmen
One player with one PC and henchmen. The player declares for his PC and, as Table rules (Henchman control) allow, for henchmen; the Judge plays henchmen's personalities, morale, obedience and loyalty (henchmen-hirelings.md). Replies end where the PC must act.

## human-party
Several players. One player is the **caller**: each round (combat) or step (exploration) he gives one consolidated declaration for the party: marching order, the group's action, and each character's individual action as the players told him. The Judge resolves from that declaration only, asks the caller (not each player) when a declaration is incomplete, and lets players speak in character in between. Initiative and individual open rolls are shown per character. A human caller may use the party declaration format below; nothing requires it.

## ai-party
The whole party is AI players (config `party.active_players`, each `{id, pc}`; profiles in `Party/profiles/`). The caller is the AI player named in config `party.caller`. At each decision point the Judge calls the party agent once; its declaration holds every AI player's table talk, the caller's consolidated decision, the marching order and each PC's individual action. The user watches: each Judge reply runs the game on to a natural stop (scene end, fight end, a PC at 0 hp, a decision that cannot be undone, or 4 agent calls in the reply), then ends with one line on the situation; the user says "continue" or steps in.

## mixed
The user plays one PC (config `party.user_pc`) and is the caller by default (config `party.caller: user`); the AI players play the other PCs. Per decision point:
1. The Judge narrates and stops for the user, as in solo play. The reply shows the AI players' table talk from the last call.
2. The user declares as caller (the party's plan plus his own PC's action).
3. The Judge calls the agent with the user's declaration verbatim in **Caller's declaration** (type `decide`, or `combat` each round). The AI players react in table talk and declare their PCs' individual actions under the call; one whose profile breaking point is reached defies, named under **Defiance**.
4. The Judge resolves everything and replies.
When the user asks the table for opinions before deciding ("what do you all think?"), make a `counsel` call first and show its talk; then continue at step 2. In combat each AI player declares its own PC's action every round.

## The Judge plays the AI players (no agent calls)
When Table rules say so (a cost decision), the Judge decides for each AI player at each decision point from `Party/profiles/` (temperament, priorities, breaking points), `Party/heuristics.md` and `Party/party-notes.md`, with the same wall the agent has: only what the characters perceived, their memory notes and the party notes, never Judge-only material. The caller's consolidated decision, marching order and each PC's individual action are settled before any roll, exactly as a declaration would give them; table talk is shown as one short line per player where it matters. Players' memory and party notes are written by the Judge as the agent's Memory updates would be (`party-agent.md` → Memory: nothing the party could not know; mistakes stay). `party-agent.md` is not loaded in these chats.
