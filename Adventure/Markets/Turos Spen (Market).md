---
type: "market"
place: "[[Turos Spen]]"
market_class: "VI"
hex: "28.16"
tags:
  - "sakkara/market"
---
# Türos Spen (Market)

Class **VI** market, hex 28.16 (AX3 #22).

Demand modifiers: below (AX3's Borderlands table; earlier notes said AX3 gave none).

## Demand modifiers (AX3 pp. 222-223, Türos Spen column)
Adventuring gear uses the market class's availability; 0 for gear.

| Merchandise (ACKS II) | AX3 type | **Final** |
|---|---|---|
| Grain & vegetables | Grain, vegetables | **0** |
| Preserved fish | Fish, preserved | **-1** |
| Common wood | Wood, common | **+1** |
| Salt | Salt | **+1** |
| Beer & ale | Beer, ale | **+1** |
| Oils & sauces | Oil, lamp | **+1** |
| Textiles | Textiles | **+1** |
| Common furs | Hides, furs | **+1** |
| Botanicals | Tea or coffee | **-1** |
| Common metal | Metals, common | **+1** |
| Preserved meat | Meats, preserved | **+1** |
| Clothing | Cloth | **+1** |
| Wine & spirits | Wine, spirits | **0** |
| Pottery | Pottery | **0** |
| Tools | Tools | **-2** |
| Armor & weapons | Armor, weapons | **-1** |
| Dyes & pigments | Dye & pigments | **-1** |
| Glassware | Glassware | **-1** |
| Monster parts | Monster parts | **-1** |
| Rare wood | Wood, rare | **0** |
| Rare furs | Furs, rare | **0** |
| Precious metals | Metals, precious | **0** |
| Ivory | Ivory | **+1** |
| Spices | Spices | **+1** |
| Fine porcelain | Porcelain, fine | **+1** |
| Rare books & art | Books, rare | **0** |
| Silk | Silk | **0** |
| Semiprecious stones | Semiprecious stones | **0** |
| Gems | Gems | **0** |

- AX3 types with no ACKS II merchandise (livestock is bought as animals, not trade goods): Animals 0; Mounts -1. Mapping of AX3's ACKS I list to the ACKS II 29 types is a Judge's call: lamp oil → oils & sauces, tea or coffee → botanicals, cloth → clothing, hides and furs → common furs.
- The engine reads the **Final** column (`inv sell … --market-note`). Modifiers apply to merchandise trade only.
