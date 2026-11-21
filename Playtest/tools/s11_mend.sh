# S11 helper: one day's attempt to buy Repair Disfigurement and Disability (source after s10_j.sh)
# mendask DAY -> prints ACCEPTED or TRY; one plain request, then one sweetened retry (donation = fee, Rulings S09)
mendask(){ local d=$1 o
  $A roll --hidden "Matriarch Aundemë's whereabouts day $d (01-15 Temple, 16-30 Hospital, 31-45 Almshouse, 46-60 Orphanage, else away):1d100" 2>&1 | tail -1
  o=$($A spellcasting --payer lucilla --market Cyfaraun --market-class II --type divine --level 4 --spell "Repair Disfigurement and Disability" --prof diplomacy --day $d 2>&1 | tail -1)
  echo "$o" | cut -c1-140; echo "$o" | grep -q "casts Repair" && { echo ACCEPTED; return; }
  o=$($A spellcasting --payer lucilla --market Cyfaraun --market-class II --type divine --level 4 --spell "Repair Disfigurement and Disability" --prof diplomacy --day $d --mod "sweetened: a donation equal to the fee (Rulings S09):+1" 2>&1 | tail -1)
  echo "$o" | cut -c1-140; echo "$o" | grep -q "casts Repair" && { $A inv pay lucilla 185gp --to "Temple of the Hearth Fire" --cause "donation with the request (sweetened offer, Rulings S09), day $d" >/dev/null; echo ACCEPTED-SWEETENED; return; }
  echo TRY; }
# night: inn beds for eleven, Lucilla's pallet, town meals, rollover to 06:02
night(){ local d=$1 n=${2:-eleven} c=${3:-2gp2sp}
  $A wait --hours 12 >/dev/null 2>&1; $A eat --in-town >/dev/null 2>&1
  $A inv pay lucilla 1gp --to "Hospital of the Keepers" --cause "donation for her pallet in the courtyard (bed rest), night of day $d" >/dev/null 2>&1
  $A inv pay vettius $c --to "Silk Pony Inn (#25)" --cause "beds for $n, night of day $d" 2>&1 | tail -1 | cut -c1-80
  $A wait --hours 12 2>&1 | tail -1 | grep -o "day [0-9]* begins\|[a-z-]*: bed rest, [0-9]* day(s) left\|[a-z-]* heals [0-9]* hp[^;]*\|wage[^;]*\|loyalty[^;]*" | tr '\n' ';'; echo; }
