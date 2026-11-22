# S13 helpers (source after s10_j.sh and s11_mend.sh): go N [turn args] -> one turn at a time, stops on anything that needs the Judge
go(){ local n=${1:-1} i o; for ((i=1;i<=n;i++)); do o=$($A turn 1 2>&1 | tail -1 | sed 's/ *(src[^)]*)//g'); echo "$o" | cut -c1-420
  if echo "$o" | grep -qiE "encounter|arriv|rest due|NONE LIT|burnt out|burns out|unconscious|dies|dead|begins|winded|expire"; then echo "-- stop after turn $i"; return; fi; done; }
# walk N: N turns of exploration with a rest after every 5th (rest counter read from the engine); stops on anything else
walk(){ local n=${1:-1} i o; for ((i=1;i<=n;i++)); do
  local rn; rn=$($A clock 2>&1 | tail -1 | grep -o "rest: [0-9]* turns" | grep -o "[0-9]*"); if [ "${rn:-0}" -ge 5 ] || $A clock 2>&1 | tail -1 | grep -q "winded:"; then o=$($A rest 2>&1 | tail -1 | sed 's/ *(src[^)]*)//g'); echo "REST: $o" | cut -c1-300
     echo "$o" | grep -qiE "ENCOUNTER|burns out|burnt out|NONE LIT" && { echo "-- stop (rest)"; return; }; fi
  o=$($A turn 1 2>&1 | tail -1 | sed 's/ *(src[^)]*)//g'); echo "$o" | cut -c1-300
  echo "$o" | grep -qiE "ENCOUNTER|NONE LIT|burns out|burnt out|unconscious|dies|begins|winded|expire" && { echo "-- stop after turn $i"; return; }; done; }
