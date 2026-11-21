---
type: "market"
place: "[[Turos Orn]]"
market_class: "IV"
hex: "23.10"
tags:
  - "sakkara/market"
---
# Türos Orn (Market)

Class **IV** market, hex 23.10 (AX3 #15 and its domain table).

Demand modifiers: below (AX3's Borderlands table; earlier notes said AX3 gave none).

## Demand modifiers (AX3 pp. 222-223, Türos Orn column)
Adventuring gear uses the market class's availability; 0 for gear.

| Merchandise (ACKS II) | AX3 type | **Final** |
|---|---|---|
| Grain & vegetables | Grain, vegetables | **+1** |
| Preserved fish | Fish, preserved | **-1** |
| Common wood | Wood, common | **+2** |
| Salt | Salt | **0** |
| Beer & ale | Beer, ale | **-1** |
| Oils & sauces | Oil, lamp | **0** |
| Textiles | Textiles | **-1** |
| Common furs | Hides, furs | **+1** |
| Botanicals | Tea or coffee | **+1** |
| Common metal | Metals, common | **+2** |
| Preserved meat | Meats, preserved | **0** |
| Clothing | Cloth | **-1** |
| Wine & spirits | Wine, spirits | **-1** |
| Pottery | Pottery | **-1** |
| Tools | Tools | **-3** |
| Armor & weapons | Armor, weapons | **-3** |
| Dyes & pigments | Dye & pigments | **-3** |
| Glassware | Glassware | **-3** |
| Monster parts | Monster parts | **+1** |
| Rare wood | Wood, rare | **+1** |
| Rare furs | Furs, rare | **+1** |
| Precious metals | Metals, precious | **+2** |
| Ivory | Ivory | **+2** |
| Spices | Spices | **+2** |
| Fine porcelain | Porcelain, fine | **-1** |
| Rare books & art | Books, rare | **-1** |
| Silk | Silk | **-2** |
| Semiprecious stones | Semiprecious stones | **+2** |
| Gems | Gems | **+2** |

- AX3 types with no ACKS II merchandise (livestock is bought as animals, not trade goods): Animals -1; Mounts -1. Mapping of AX3's ACKS I list to the ACKS II 29 types is a Judge's call: lamp oil → oils & sauces, tea or coffee → botanicals, cloth → clothing, hides and furs → common furs.
- The engine reads the **Final** column (`inv sell … --market-note`). Modifiers apply to merchandise trade only.
