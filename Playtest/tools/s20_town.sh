# S20 town helpers (source after s10_j.sh): tday H -> eat --in-town, then wait H hours (one rollover at most per call)
tday(){ $A eat --in-town 2>&1 | tail -1 | f 120; $A wait --hours ${1:-24} 2>&1 | tail -1 | f 600; }
