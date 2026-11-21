---
type: "market"
place: "[[Turos Tem]]"
market_class: "V"
hex: "22.20"
tags:
  - "sakkara/market"
---
# Türos Tem (Market)

Class **V** market, 110 urban families, hex 22.20 (AX1 pp. 25-28). Forum open six days in seven; Guild Merchant Aeropos Karanos at the weights table mid-morning to early afternoon. Imports grain, beer, wine, pottery from Siadanos; fish from Türos Spen; wood and rare furs from Türos Luin; monster parts from Türos Aster. Demand modifiers: below, from AX3's Borderlands table (AX1 p. 26 gives the same column).

## Demand modifiers (AX3 pp. 222-223, Türos Tem column)
Adventuring gear uses the market class's availability; 0 for gear.

| Merchandise (ACKS II) | AX3 type | **Final** |
|---|---|---|
| Grain & vegetables | Grain, vegetables | **-1** |
| Preserved fish | Fish, preserved | **0** |
| Common wood | Wood, common | **0** |
| Salt | Salt | **+1** |
| Beer & ale | Beer, ale | **0** |
| Oils & sauces | Oil, lamp | **+1** |
| Textiles | Textiles | **0** |
| Common furs | Hides, furs | **+1** |
| Botanicals | Tea or coffee | **-1** |
| Common metal | Metals, common | **0** |
| Preserved meat | Meats, preserved | **0** |
| Clothing | Cloth | **0** |
| Wine & spirits | Wine, spirits | **-1** |
| Pottery | Pottery | **-1** |
| Tools | Tools | **-2** |
| Armor & weapons | Armor, weapons | **-2** |
| Dyes & pigments | Dye & pigments | **-2** |
| Glassware | Glassware | **-2** |
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

- AX3 types with no ACKS II merchandise (livestock is bought as animals, not trade goods): Animals -1; Mounts -1. Mapping of AX3's ACKS I list to the ACKS II 29 types is a Judge's call: lamp oil → oils & sauces, tea or coffee → botanicals, cloth → clothing, hides and furs → common furs.
- The engine reads the **Final** column (`inv sell … --market-note`). Modifiers apply to merchandise trade only.
