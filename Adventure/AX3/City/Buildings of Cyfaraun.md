---
type: city-chapter
place: "[[Cyfaraun]]"
tags:
  - sakkara/secret
source: "AX3 pp. 46-55 (Buildings of Cyfaraun)"
---

# Buildings of Cyfaraun

Judge only. AX3's procedure for generating any of the city's ~4,000 buildings on the spot when the party walks into one that is not keyed (AX3 p. 46). Hub: [[AX3 Hub]]; city: [[Cyfaraun]]. All tables are in `Adventure/AX3/Tables/` (ids `ax3-building-…`); roll them with the engine's dice or the table tool. Keyed points of interest in the district notes always take precedence.

## Procedure (run in this order)

1. **Size.** Judge the building's size from the district map: one you squint to see is **small**, one seen in clusters **medium**, one easily seen **large**, one noticeably larger than the rest of its block **huge**. Across the city about 50% medium, 25% small, 20% large, 5% huge (p. 46).
   - Small: 100-450 sf, average 250 sf (16’ × 16’). Medium: 500-1,700 sf, average 1,000 sf (33’ × 33’). Large: 1,750-3,450 sf, average 2,500 sf (50’ × 50’); never a cot. Huge: 3,500 sf or more.
2. **Subdivided?** Medium: 25% it is split into 4 (2d3) small buildings → roll step 3 once on the **Small** table; all of them are that type. Large: 25% split into 10 (4d4) small buildings → once on Small. Huge: 25% split into 7 (2d6) medium buildings → once on **Medium** (p. 46).
3. **Type.** Roll 1d100 on the size's table: `Tables/ax3-building-type-small.yaml`, `…-medium.yaml`, `…-large.yaml`, `…-huge.yaml` (p. 46). For a shop or shophouse roll **1d6: 1-2 merchant's store, 3-6 artisan's workshop**. For a small stable roll `ax3-building-stables-small.yaml` (1d8).
4. **Occupants.** Read the type's line in **Standard Occupants** (below) and roll its dice. Then fill in who they are:
   - **Owner/tenants of cots and townhouses:** roll on `ax3-building-occupant-small-cot.yaml`, `…-medium-cot.yaml`, `…-medium-townhouse.yaml` or `…-large-townhouse.yaml` (p. 51).
   - **Merchants:** `ax3-building-merchant-occupation.yaml` (p. 53). **Artisans:** `ax3-building-artisan-occupation.yaml` (p. 54). Roll once per shop: all its merchants or artisans share the trade.
   - **Patrons, worshippers, street folk** (marked * below): `ax3-building-occupant-general-street.yaml` (also for street, bath and other public encounters, p. 51).
   - **Sub-tables** named in a result: laborer (`ax3-building-laborer-occupation`), hosteller (`…-hosteller-occupation`), specialist (`…-specialist-occupation`), mercenary/legionary (`…-military-occupation`), entertainer (`…-entertainer-occupation`), minor ecclesiastic (`…-minor-ecclesiastic-occupation`), minor magician (`…-minor-magician-occupation`).
   - **Classed NPCs:** a result naming a class, or a percentage chance of one, gives a classed NPC. Roll `ax3-building-npc-level.yaml` unless a level is given (1st 60%, 2nd 23%, 3rd 9%, 4th 4%, 5th 2%, 6th and 7th 1% each). For "fighter, mage, cleric or thief" either keep the default class or roll the sub-class on `ax3-building-npc-class.yaml` (p. 53). Several AX3 sub-classes have no ACKS II Revised Rulebook class; the table names the substitute (Judge's call).
   - **Never roll for dependents** (children, the disabled, elders, spouses keeping house): they are what they are (p. 49).
   - **Who is home** (below).
5. **Style.** Roll 1d100 once on the district's **Exterior Walls** table and once on its **Roof, Floor and Interior Walls** table, **+10** for a large villa or bathhouse, **+25** for a huge villa, bathhouse or shrine; a bathhouse is always at least concrete masonry (p. 55). Tables: `ax3-building-walls-plaza-festival`, `…-walls-old-bridge`, `…-walls-lake-palace`, `…-walls-tower-temple`; `ax3-building-roof-plaza-festival`, `…-roof-old-bridge`, `…-roof-lake-palace`, `…-roof-tower-temple`.
6. **Treasure** (only if needed, e.g. burglary; below).

## Building types and occupants (pp. 46-49)

**Standard Occupants by Building Type** (p. 50; * = roll on the General/Street occupant table as needed)

| Building | Occupants |
|---|---|
| Cot, small | 1d4: #1-2 owner/tenants*, #3-4 dependents |
| Cot, medium | 2d3: #1-2 owner/tenants*, #3-5 dependents, #6 maidservant |
| Townhouse, medium | 2d4: #1-2 owner/tenants*, #3-5 dependents, #6 maidservant, #7 scullion, #8 cook |
| Townhouse, large | 2d6: as medium, #9-12 maidservants |
| Villa, large | 2d4: #1-2 patricians (1 in 6 that one is a fighter: roll level), #3-5 dependents (#6+ siblings and cousins); plus cook, maidservant, scullion, 1d3+1 household guards |
| Villa, huge | as large, but 1d2 maidservants, 1d2 scullions, 1d3+1 guards and a guard captain (fighter, roll level) |
| Shop, small | 1 apprentice merchant (store; a guild apprentice or unlicensed peddler) or 1 journeyman artisan (workshop) |
| Shop, medium | 1 licensed merchant + 2 apprentices (store) or 1 master artisan + 2 journeymen + 4 apprentices (workshop) |
| Shop, large | 1 master merchant (25% a venturer, roll level) + 2 licensed merchants + 4 apprentices (store) or 2 master artisans + 4 journeymen + 8 apprentices (workshop) |
| Manufactory | 2d6 teams (1 master artisan, 2 journeymen, 4 apprentices) + 4d6 manual laborers |
| Shophouse, small | as small shop + 1d3 dependents |
| Shophouse, medium | as medium shop + 2d4−1: #2 spouse, #3-5 dependents, #6 maidservant, #7 scullion |
| Shophouse, large | as large shop + 2d6−1: #2 spouse, #3-5 dependents, #6 maidservant, #7 scullion, #8 cook, #9-11 maidservants |
| Bawdyhouse, small | 1 prostitute; 50% 1 patron* |
| Bawdyhouse, medium | 2d3 prostitutes, 1 brothelkeeper (thief, roll level), 1d3 patrons* |
| Bawdyhouse, large | 4d6 prostitutes, 1d6 guards (assassin or thief, 1st level), 1 brothelkeeper (thief, roll level), 2d6 patrons* |
| Cantina, small | 1 cantinakeeper, 1d3 dependents, 1d3 patrons* (at mealtimes) |
| Cantina, medium | 1 cantinakeeper, 2d6 patrons* (mealtimes), 2d4−1 others: #2-5 dependents, #6 cook, #7 scullion |
| Cantina, large | 1 cantinakeeper, 1 scullion, 4d6 patrons* (mealtimes), 2d4+1 others: #2-5 dependents, #6 cook, #7 scullion, #8-9 maids |
| Inn | 1 innkeeper, 1 cook, 1 scullion, 1d3 tavernworkers, 1d3 maidservants, 2d6+2 patrons*, 1d4 family; 2d4 guest rooms and stalls for 2d4 mounts, 1d4 × 25% of them vacant |
| Tavern | 1 tavernkeeper, 1 cook, 1 scullion, 1d3 tavernworkers, 2d6+2 patrons*, 1d4 dependents (no lodging or stables) |
| Depot | by merchandise (Depot table below) |
| Bathhouse, medium | 1d4−1 patrons* in each of atrium, cold bath, warm lounge; 1 attendant (atrium) |
| Bathhouse, large | 1d4+1 patrons* in each of atrium, cold bath, hot bath, warm lounge, sauna; 1d3 attendants (warm lounge) + 1 (atrium) |
| Bathhouse, huge | 1d4+4 patrons* in each room (adds a garden, gymnasium, latrine or library); 1d4+4 attendants (warm lounge) + 1 (atrium) |
| Public latrine | small 50% 1 patron*; large 2d6 patrons*; huge 5d6 patrons* |
| Shrine, small | 1 minor ecclesiastic caretaker (by day); 25% 1d4 worshippers* |
| Shrine, huge | 1 cleric or priestess (roll class and level) + 1d4 minor ecclesiastics; 75% 3d6 worshippers* |
| Stables/pen, small | `ax3-building-stables-small` (1d8); by day 50% 1 laborer |
| Stables/pen, large | 2d6 donkeys, 1d8 mules, 1d6 medium draft or riding horses, 1d4 heavy draft horses, 1d2 light riding horses; 1 stablehand, +1d4 by day |

**Notes by type**
- **Cots** (one-room dwellings, rowhouses, shacks) and **townhouses** (two-story, usually shared walls). Owner/tenants are the first two occupants, then up to three dependents, then servants. **By day** one owner/tenant is away 90%, the other 50%; if both are away, so are the dependents unless servants are present (p. 47).
- **Villas** (luxurious, two stories, inner courtyard; freestanding ones have walks or gardens): owners each 75% away by day, other occupants 25% (p. 47). The 1-in-6 fighter on p. 47 is printed "16%" on p. 50.
- **Shops** (single story, open to the public) and **manufactories** (huge, not open to the public; sell wholesale to dealers and long-distance traders): always occupied by day; locked and barred at night with the workers at home (p. 47). 1 in 4 master merchants is a venturer (roll level).
- **Shophouses:** shop below, dwelling above; occupied day and night (owner and family at home at night).
- **Depots** (pp. 48): small = a resident's shack; medium = a business's storage unit; large and huge = warehouses. Grain is kept in two-story lofts, wine in sunken floors (huge: both).

  | Depot | Merchandise types | Loads per type (common / precious) | Workers by day |
  |---|---|---|---|
  | Small | 1 | 1d10 / 1d4 | 1 (5%) |
  | Medium | 1 | 2d10 / 2d4 | 1d6 (5%) |
  | Large | 1d4 | 4d10 / 1d10 | 1d6 (10%) |
  | Huge | 1d8 | 4d10 / 1d10 | 2d6 (10%) |

  Roll each type on the **Common Merchandise** table (ACKS II RR, Merchandise; re-roll Animals and Mounts, which live in stables), going to the Precious sub-table when indicated. At night a depot with precious goods has **1 guard per 3 precious loads (round up)** and a **3rd-level sergeant per 10 guards (round down)**. (Example p. 48: large warehouse, 3 types → 23 loads dye, 32 loads glassware, 5 loads silk guarded by two 1st-level guards.) The "(5%)/(10%)" figures beside workers are printed without explanation (presence chance or share of workers, unclear).
- **Bawdyhouses** (p. 48): prostitution is legal but not respectable; most are run by or "protected" by a syndicate. Ordinary prices **2sp a few moments, 1gp a night**; up to 10× in upscale houses for patricians. One patron per two prostitutes.
- **Cantinas:** grab-and-go counters with food jars and a stove; large ones have tables.
- **Taverns:** made-to-order meals, beer and/or wine; may have gambling rooms and private rooms for sex; no lodging or stables.
- **Inns:** a tavern below, guest rooms above, stalls behind.
- **Bathhouses** (private, for the wealthy): **reaction rolls with bathhouse patrons +1** (p. 49).
- **Public latrines:** small = an outhouse over the sewer; large and huge = rows of seats over the sewer with a sponge-moat. **Reaction rolls in a latrine −2** (p. 49).
- **Shrines:** private shrines of patricians or wealthy merchants; small ones to an ancestor or an aspect of an Empyrean god (e.g. Calefa as goddess of fortune on Gambler's Row); huge ones to a god or the whole pantheon.

## Doing business in a shop (p. 47)
- Merchants and artisans sell goods fitting their trade (armour, weapons, clothing, equipment, mounts, vehicles). A **small shop has 10%** of Cyfaraun's equipment availability (Class III, RR Equipment Availability by Market Class), a **medium shop 25%**, a **large shop 50%**.
- Each may also buy or sell **loads of merchandise** of the kinds its occupation table names: a **master artisan 1 load a month**; a **master merchant 3d4 loads a month**; an **independent guild-licensed merchant 1d4+1 loads a month**. Each counts against the number of merchants interested in transactions with the party (see [[Doing Business in Cyfaraun]]).
- Example (p. 47): a medium shop, 1d6 = 2 (store), 1d100 = 45 (furrier): sells fur garments, buys or sells up to 1d4+1 loads of hides/furs, rare furs or monster parts a month.

## Building style (p. 55)
- **Old and Bridge Districts** (Old Cyfaraun): about half the buildings are elven work, mostly half- and full-timber (some now rendered with white stucco), a few of fine-cut limestone and marble; the rest cheap Auran wattle and daub with white stucco.
- **Plaza and Festival:** varied; most often half-timber frames infilled with Auran concrete and white stucco.
- **Lake and Palace:** luxurious; mostly concrete rendered with white or marbled stucco (fake marble); the grandest veneered with or built of limestone and marble.
- **Tower and Temple:** sturdier than Plaza/Festival, less luxurious than Lake/Palace; mostly concrete faced with patterned fired brick.
- Plaza/Festival roof table: printed 10-50 for its first row, leaving 01-09 unassigned; the YAML reads 01-50 (Judge's call).

## Building treasure (p. 55)
- **Coin** = 1.5 × the monthly wages of the **non-dependent** occupants; itinerant occupants (e.g. bath patrons) carry wages ÷ 20. Coin is in the ratio **1 : 10 : 100 gold : silver : copper** (inferred: by count of coins).
- **Shops and manufactories** also hold goods worth **1d6 × monthly earnings**.
- The rest of the occupants' wealth is the building, land, fixtures, tools and personal items.
- Example (p. 55): medium gemcutter's workshop: master 80gp + two journeymen 20gp + four apprentices 10gp a month = 160gp earnings (as printed) → 240gp coin and 1d6 × 240gp of gems (rolled 5: 1,200gp).
- Wages: use the ACKS II wage of each occupation (specialists, hirelings and craftsmen in the RR; Judge's call where none is listed).

## Tables (all `Adventure/AX3/Tables/`)
| File | Die | Page |
|---|---|---|
| `ax3-building-type-small.yaml`, `-medium`, `-large`, `-huge` | 1d100 | 46 |
| `ax3-building-stables-small.yaml` | 1d8 | 49 |
| `ax3-building-occupant-small-cot.yaml`, `-medium-cot`, `-medium-townhouse`, `-large-townhouse`, `-general-street` | 1d100 | 51 |
| `ax3-building-laborer-occupation.yaml` | 1d100 | 51 |
| `ax3-building-hosteller-occupation.yaml` | 1d100 | 51 |
| `ax3-building-specialist-occupation.yaml` | 1d100 | 52 |
| `ax3-building-military-occupation.yaml` (printed "Mercenary Occupation") | 1d100 | 52 |
| `ax3-building-entertainer-occupation.yaml` | 1d100 | 52 |
| `ax3-building-minor-ecclesiastic-occupation.yaml` | 1d100 | 52 |
| `ax3-building-minor-magician-occupation.yaml` | 1d100 | 52 |
| `ax3-building-npc-class.yaml` (printed "1d100x100": category column, then sub-class row; inferred reading) | 1d100 | 53 |
| `ax3-building-npc-level.yaml` | 1d100 | 53 |
| `ax3-building-merchant-occupation.yaml` | 1d100 | 53 |
| `ax3-building-artisan-occupation.yaml` | 1d100 | 54 |
| `ax3-building-walls-plaza-festival.yaml`, `-old-bridge`, `-lake-palace`, `-tower-temple` | 1d100 (+10/+25) | 55 |
| `ax3-building-roof-plaza-festival.yaml`, `-old-bridge`, `-lake-palace`, `-tower-temple` | 1d100 (+10/+25) | 55 |

Not printed: a "Patrician Family" sub-table (General/Street 100). Use a patrician of a house from the [[Lake District]] or [[Palace District]] notes (Judge's call); 25% are fighters.
