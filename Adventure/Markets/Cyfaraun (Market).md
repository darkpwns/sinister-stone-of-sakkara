---
type: "market"
place: "[[Cyfaraun]]"
market_class: "III"
hex: "18.05"
tags:
  - "sakkara/market"
---
# Cyfaraun (Market)

Class **III** market, hex 18.05 (AX3 #10 and its domain table). A **venturer** may treat it as **Class II** or take +1 market impact; a party with market impact 0 treats it as **Class IV** (AX3 p. 56). Trading procedure, tolls (4d6+2gp per 5,000 st), customs (2d10% on imports), fees, banking and the treasure law: [[Doing Business in Cyfaraun]].

## Demand modifiers (AX3 pp. 222-223, Cyfaraun column)
Source of every value: the AX3 table; these replace the earlier partial JJ p. 202 example (wood common −3; hides, furs −3; metals common −2; grain +1; spices +1; silk +1), which AX3 contradicts on all six. Doing Business (pp. 56-57) adds no others.

| Merchandise (ACKS II) | AX3 type | **Final** |
|---|---|---|
| Grain & vegetables | Grain, vegetables | **+2** |
| Preserved fish | Fish, preserved | **-2** |
| Common wood | Wood, common | **+2** |
| Salt | Salt | **0** |
| Beer & ale | Beer, ale | **-1** |
| Oils & sauces | Oil, lamp | **0** |
| Textiles | Textiles | **-2** |
| Common furs | Hides, furs | **+1** |
| Botanicals | Tea or coffee | **+2** |
| Common metal | Metals, common | **+3** |
| Preserved meat | Meats, preserved | **-1** |
| Clothing | Cloth | **-2** |
| Wine & spirits | Wine, spirits | **-1** |
| Pottery | Pottery | **-2** |
| Tools | Tools | **-3** |
| Armor & weapons | Armor, weapons | **-3** |
| Dyes & pigments | Dye & pigments | **-3** |
| Glassware | Glassware | **-3** |
| Monster parts | Monster parts | **+2** |
| Rare wood | Wood, rare | **+2** |
| Rare furs | Furs, rare | **+2** |
| Precious metals | Metals, precious | **+2** |
| Ivory | Ivory | **+3** |
| Spices | Spices | **+3** |
| Fine porcelain | Porcelain, fine | **-2** |
| Rare books & art | Books, rare | **-2** |
| Silk | Silk | **-2** |
| Semiprecious stones | Semiprecious stones | **+2** |
| Gems | Gems | **+2** |

- AX3 types with no ACKS II merchandise (livestock is bought as animals, not trade goods): Animals -1; Mounts -1. Mapping of AX3's ACKS I list to the ACKS II 29 types is a Judge's call: lamp oil → oils & sauces, tea or coffee → botanicals, cloth → clothing, hides and furs → common furs.
- The engine reads the **Final** column (`inv sell … --market-note`). Modifiers apply to merchandise trade only.
- **AX3's own notes disagree with its table** for four goods: the arbitrage notes (p. 223) give Cyfaraun **common metals +2** (table +3), **precious metals +3** (table +2), **semiprecious stones +3** (table +2) and **gems +3** (table +2). The table values are used above (Judge's call); the notes' values are the alternative.
- AX3's summary (p. 222): Cyfaraun is the region's **major supplier** of tools, armour, weapons, dyes, glassware and rare books (all −3, rare books −2) and its **major consumer** of common metals, common and rare woods, monster parts, precious metals, ivory, spices, stones and gems.
- Modifiers apply to merchandise trade only; adventuring gear uses Class III equipment availability (Class II for venturers).
- Full regional table: `Adventure/AX3/Tables/ax3-borderlands-demand-modifiers.yaml`.

## Trade routes and partners
- **Samos** (west, about 48 miles): trade route (existing note; AX3 p. 19 calls Samos a declining Krysean town overshadowed by Cyfaraun). AX3's table gives Samos market **Class VI**, not the Class IV this note had (JJ example; Judge's call which to use; no Samos market note exists).
- **Siadanos** (south, down the Mirmen): controls the trade route between the dwarves of Azen Radokh and Cyfaraun, Pyrgos and Larisa (AX3 p. 22); Liber Faunus runs 5 barges between Siadanos and Cyfaraun (p. 74).
- **Arganos** (great coastal city): Liber Faunus's 40-wagon caravan works the trade route Cyfaraun-Arganos (p. 74); merchants from Arganos enter by the Capital Gate #76 (p. 187).
- **Arbitrage runs to Cyfaraun** named by AX3 (20%+ price difference, p. 223): grain and herbal tea from Siadanos; common and rare wood from Türos Veren (−4); common metals, precious metals, semiprecious stones and gems from Azen Radokh (−2); monster parts from Türos Aster (−2; Aster has no column in the table); ivory and spices landed at Türos Aurë (−1). The table's Siadanos column (grain 0, tea −1) does not match the notes' −2 (Türos Luin has −2 for both).
