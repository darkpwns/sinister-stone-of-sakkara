# Capturing, taming and training creatures (engine 7.20)

Load when a creature is taken alive, young or eggs are found in a lair, a creature is tamed, trained, handled, hired
out or sold, or a party rides trained creatures (MM pp. 354-366, RR p. 106). The engine keeps the training state
(`tools.training_state`, default `Campaign/training-state.json`; `acks.sh` passes it as ACKS_TSTATE). Never track a
course or a captive by hand.

- **Data**: `acks.sh train data "<name as the table names it>"` (Taming and Training Tables row: size, normal load,
  lifespan, role, values, supply cost, period, TM; the trainer rank its statblock type needs; a NOTE for every number
  the statblock gives otherwise: the table's number is used). `train crosscheck` lists them all.
- **Capture** in a fight: `acks.sh capture ID --how slumbering|paralyzed|netted|restrained|bewitched|helpless|surrendered
  --by WHO` (refused unless its condition allows it; the combatant becomes `captured`: `state end` records its XP).
  Young or eggs from a lair: `train young "<species>" --adults N` (the note's % per adult, hidden), then
  `capture --how young|eggs --species "<species>" --count N --by WHO`.
- **Courses**: `train start ID --trainer WHO [--trainer-ranks N] (--role R | --tricks a,b) [--whispering]
  [--bewitched] [--affinity]`. The engine refuses a trainer without the Animal Training rank, a seventh creature, a
  second creature while whispering, a flying adult without whispering, a role beyond 2d4+TM(+2). The maximum tricks are
  rolled hidden and revealed when reached (reading `taming.tricks_revealed`); adult multipliers by the reading
  `taming.adult_multipliers` (MM ×4/×2 domestic, ×12/×6 others). A flier's mount or war-mount role waits for
  adolescence (MM p. 356): its course says from which day.
- **Progress**: `train show` (every course, its next milestone), `train due --day D --to E` (milestones passed, captives'
  escape checks and supply cost); the clock commands print the milestones they pass. The trainer away or the creature
  hurt: `train pause C# --reason R`, then `train resume C#`.
- **Handling**: `train handler ID WHO [--proficient] [--riding]` (Roles at a Glance limits); a tame creature met off the
  leash: `train meet ID WHO [--proficient]` (reaction, +2 proficient, 9+ handler).
- **Use**: `train stable ID --owner WHO` (an inventory animal holder, normal load from the table, up to twice it);
  ridden in travel with `mounts add ID --kind "<species>"`: its statblock speed, `travel --flying` its flying speed
  (every member mounted on a flier). `train value ID [--attrs STR=13,…]`, `train wage "<species>"` (hired out),
  `train lot ID` (a goods lot at its value, then `sell L#`), `train trainer-wage RANK [--size G]`.
