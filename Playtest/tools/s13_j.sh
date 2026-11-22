# S13 helpers (source after s10_j.sh and s11_mend.sh): go N [turn args] -> one turn at a time, stops on anything that needs the Judge
go(){ local n=${1:-1} i o; for ((i=1;i<=n;i++)); do o=$($A turn 1 2>&1 | tail -1 | sed 's/ *(src[^)]*)//g'); echo "$o" | cut -c1-420
  if echo "$o" | grep -qiE "encounter|arriv|rest due|NONE LIT|burnt out|burns out|unconscious|dies|dead|begins|winded|expire"; then echo "-- stop after turn $i"; return; fi; done; }
