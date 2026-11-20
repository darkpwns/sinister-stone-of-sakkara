#!/usr/bin/env python3
"""party.py — the AI party agent's plumbing (references/party-structure.md). The agent itself is called by the
Judge with the Agent tool; this script never calls a model.

  (any command) --players id,id                     limit to a split-off group of AI players
  party.py stub --type T --step N [--impulse] [--private PLAYER]   print a scene-brief skeleton (Call, Party, Tracker,
                                                    Impulse filled from config and Campaign State public:)
  party.py impulse                                  roll impulses for active players (dice.py --hidden), print the line
  party.py build BRIEF [--rules NOTE[#Heading]]... [--note NOTE[#Heading]]... [--rules-file F]... [--site NAME] [--out F]
                                                    assemble the agent prompt; refuse on any wall breach. --note: a
                                                    campaign note's player sections (Judge-only callouts, Judge blocks
                                                    and the empty Campaign notes placeholder dropped), e.g. a class
                                                    reskin note in paths.class_notes passed with its vault note
                                                    and print the one-line Agent prompt that points the agent at it
  party.py check DECL --brief BRIEF [--prompt F] [--tokens N] [--tool-uses N] [--retry]
                                                    parse a declaration; exit 1 with the errors (send them back once).
                                                    A fresh call must show exactly 1 tool use (the agent's Read of the
                                                    prompt file) and the prompt's call code; --retry (a SendMessage
                                                    reply, which reports no usage) needs only the code
  party.py talk DECL                                compact table talk for the Judge's reply to the user
  party.py memory DECL... [--session S##]           write the declarations' memory updates into Party/ notes
  party.py costs                                    this session's agent calls, for the session log's Judge block
"""
import glob, json, os, re, secrets, subprocess, sys, textwrap, time
sys.path.insert(0, os.path.dirname(__file__))
import jlib

HERE = os.path.dirname(os.path.abspath(__file__))
TYPES = ["decide", "combat", "counsel", "hire", "split", "create-a", "create-b", "create-c", "end", "private"]
HEADS = ["Table talk", "Caller", "Marching order", "Individual actions", "Defiance", "Character choices",
         "Questions to Judge", "Memory updates"]
BRIEF_HEADS = ["Call", "Perceived", "Party", "Tracker", "Open rolls this step", "Judge answers",
               "Caller's declaration", "Impulse", "Open question"]
MEM_SECTIONS = ["Grudges", "Debts", "Lessons learned", "Opinions of NPCs", "Henchmen and hirelings"]
NOTE_SECTIONS = {"Rumours": "Rumours and what we make of them", "Plans": "Plans", "Map notes": "Map notes"}
SHINGLE = 8
TALK_MAX = 3
LINE_MAX = 1900          # the agent's Read tool may cut longer lines; build wraps them
PROMPT_MAX = 80000       # characters; one Read must return the whole prompt
CODE_RX = re.compile(r"^Call code: (K-[0-9A-F]{6})$", re.M)


def pointer(path):
    return (f"Use the Read tool once to read the file {path} (the whole file). Make no other tool call and read "
            f"nothing else. That file is your full instructions: do exactly what it says and reply with the "
            f"declaration only.")


def prompt_code(path):
    try:
        m = CODE_RX.search(open(path, encoding="utf-8").read())
    except FileNotFoundError:
        return None
    return m.group(1) if m else None


def die(msg, code=2):
    print(msg, file=sys.stderr); sys.exit(code)


def cfg_party(cfg):
    p = cfg.get("party") or {}
    a = p.get("agent") or {}
    return p, a


ONLY = None   # --players id,id : a split-off group


def players(cfg):
    p, _ = cfg_party(cfg)
    xs = [x if isinstance(x, dict) else {"id": x, "pc": ""} for x in (p.get("active_players") or [])]
    return [x for x in xs if ONLY is None or x["id"] in ONLY]


def profile(cfg, pid):
    _, a = cfg_party(cfg)
    fm, body = jlib.read_note(os.path.join(a["profiles"], pid + ".md"))
    return fm, body.strip()


VIEWS = None


def sheet(ref):
    """The player view of a character actor (an id or Characters/<id>.json): the engine's prepared view without its
    judge block (`acks actor show --player`, D8); {} when there is no such actor. The views of every actor in
    paths.characters are fetched in one engine call on first use."""
    global VIEWS
    if VIEWS is None:
        cfg = jlib.config()
        ids = [jlib.actor_id(f) for f in jlib.actor_files(cfg["paths"]["characters"])
               if jlib.load_actor(f).get("type") == "character"]
        VIEWS = jlib.actor_views(ids, player=True) if ids else {}
    v = dict(VIEWS.get(jlib.actor_id(ref)) or {})
    v.pop("judge", None)           # Judge-only, never passed to the agent
    return v


def character_ids(cfg):
    return [jlib.actor_id(f) for f in jlib.actor_files(cfg["paths"]["characters"])]


PARTY_FRESH = False


def public(cfg):
    """Campaign State front matter, `public:` and body. public.party is regenerated from the actors first (xsync.py
    --party, D7), so current hp is the actors' state, not the last save's."""
    global PARTY_FRESH
    if not PARTY_FRESH:
        subprocess.run([sys.executable, os.path.join(HERE, "xsync.py"), "--party"], capture_output=True, text=True)
        PARTY_FRESH = True
    fm, body = jlib.read_note(cfg["paths"]["state"]["campaign_state"])
    return fm, (fm.get("public") or {}), body


def pc_label(cfg, pid):
    for x in players(cfg):
        if x["id"] == pid:
            s = sheet(x.get("pc"))
            return s.get("name") or "(no PC yet)"
    return "?"


def player_name(cfg, pid):
    return profile(cfg, pid)[0].get("name", pid)


def henchmen(cfg, employer):
    out = []
    for aid in character_ids(cfg):
        s = sheet(aid)
        if s.get("role") == "henchman" and str((s.get("hired") or {}).get("employer", "")) == employer:
            out.append(s.get("name"))
    return out


def caller_text(cfg):
    p, _ = cfg_party(cfg)
    c = p.get("caller") or "user"
    if c == "user":
        u = sheet(p.get("user_pc"))
        return f"the user ({u.get('name', 'user PC')})"
    return player_name(cfg, c)


# ---------------------------------------------------------------- stub and impulse
def roll_impulses(cfg):
    parts = []
    for x in players(cfg):
        fm, _ = profile(cfg, x["id"])
        imp = fm.get("impulse")
        if not isinstance(imp, dict):
            continue
        name = fm.get("name", x["id"])
        out = subprocess.run([sys.executable, os.path.join(HERE, "dice.py"), "--hidden",
                              f"impulse {name}:1d{imp['die']}"], capture_output=True, text=True).stdout
        m = re.search(r"= (\d+)", out)
        r = int(m.group(1)) if m else 0
        hit = r in imp["fires_on"]
        parts.append(f"{name} {'FIRES' if hit else 'no'} ({r} on 1d{imp['die']})" + (f": {imp['act']}" if hit else ""))
    return "; ".join(parts) or "none"


def party_line(cfg, pub):
    rows = []
    owner = {}
    for x in players(cfg):
        s = sheet(x.get("pc"))
        if s.get("name"):
            owner[s["name"]] = player_name(cfg, x["id"])
    p, _ = cfg_party(cfg)
    u = sheet(p.get("user_pc"))
    if u.get("name"):
        owner[u["name"]] = "user"
    for m in pub.get("party") or []:
        who = owner.get(m.get("name"))
        tag = f" ({who})" if who else ""
        if m.get("role") == "henchman":
            emp = (sheet(m.get("sheet")).get("hired") or {}).get("employer")
            tag = f" (henchman of {emp})" if emp else " (henchman)"
        cond = ", ".join(m.get("conditions") or [])
        used = ", ".join(m.get("spells_used") or [])
        rows.append(f"{m.get('name')}{tag} {m.get('hp')}/{m.get('hp_max')}" + (f" {cond}" if cond else "") + (f" (spells used: {used})" if used else ""))
    tr = pub.get("tracker") or {}
    order = ", ".join(tr.get("formation") or []) or "not set"
    return f"{'; '.join(rows) or 'none'} · light {pub.get('light') or 'none'} · rations {pub.get('rations') or '?'} · marching order {order}"


def tracker_line(pub):
    tr = pub.get("tracker") or {}
    if not tr.get("round"):
        return "none"
    bits = [f"round {tr['round']}"]
    if tr.get("order"):
        bits.append("order " + ", ".join(f"{o['name']} {o['init']}" for o in tr["order"]))
    if tr.get("engaged"):
        bits.append("engaged " + "; ".join(" & ".join(map(str, e)) for e in tr["engaged"]))
    if tr.get("distances"):
        bits.append("distances " + "; ".join(f"{' – '.join(d['between'])} {d['feet']}'" for d in tr["distances"]))
    for k in ("cover", "light", "note"):
        if tr.get(k):
            bits.append(f"{k} {tr[k] if not isinstance(tr[k], list) else ', '.join(tr[k])}")
    return " · ".join(bits)


def cmd_stub(args):
    cfg = jlib.config(); fm, pub, _ = public(cfg)
    typ = val(args, "--type", "decide"); step = val(args, "--step", "1"); priv = val(args, "--private")
    if typ not in TYPES:
        die(f"--type must be one of {', '.join(TYPES)}")
    p, _ = cfg_party(cfg)
    S = f"S{int(fm.get('session') or 0):02d}"
    d = pub.get("date") or {}
    date = f"{d.get('season', '')} day {d.get('day', '')}, {d.get('year', '')}".strip()
    if priv:
        pid = pid_of(cfg, priv)
        head = f"### Private brief — {S} · step {step} · {player_name(cfg, pid)}"
        decl = f"{pc_label(cfg, pid)} ({player_name(cfg, pid)})"
        typ = "private"
    else:
        head = f"### Scene brief — {S} · step {step} · {date}, {pub.get('time', '')} · {pub.get('place', '')}"
        decl = ", ".join(f"{pc_label(cfg, x['id'])} ({player_name(cfg, x['id'])})" for x in players(cfg))
    imp = roll_impulses(cfg) if "--impulse" in args else "none"
    print(f"""{head}
**Call:** {typ} · {p.get('structure')} · caller {caller_text(cfg)} · declare for {decl}
**Perceived:** <narration of what the characters perceive>
**Party:** {party_line(cfg, pub)}
**Tracker:** {tracker_line(pub)}
**Open rolls this step:** none
**Judge answers:** none
**Caller's declaration:** {'n/a' if p.get('structure') != 'mixed' or (p.get('caller') or 'user') != 'user' else '<the user declaration, verbatim>'}
**Impulse:** {imp}
**Open question:** <the decision in front of the party, one line>""")


def cmd_impulse(args):
    print("**Impulse:** " + roll_impulses(jlib.config()))


def pid_of(cfg, name):
    for x in players(cfg):
        if name.lower() in (x["id"].lower(), player_name(cfg, x["id"]).lower()):
            return x["id"]
    die(f"{name}: not an active player")


# ---------------------------------------------------------------- wall
def norm_words(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def shingles(text, n=SHINGLE):
    w = norm_words(text)
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def callout_blocks(text, starts):
    out, on = [], False
    for ln in text.splitlines():
        s = ln.strip()
        if any(s.startswith(x) for x in starts):
            on = True; out.append(s); continue
        if on and s.startswith(">"):
            out.append(s); continue
        on = False
    return "\n".join(out)


def judge_corpus(cfg):
    """Text the agent must never see verbatim: Judge-only folders, files, tagged notes, Judge-only and Judge-block
    callouts, every actor's judge block (all actor folders), and the rules repo's bestiaries (statblocks)."""
    sec = cfg["secrecy"]; parts = []
    skip = {"campaign.yaml", "roll-log.jsonl", "snapshot.json", "party-log.jsonl", "Rulings.md", "Ledger.md"}
    for folder in sec["judge_only_folders"]:
        for f in glob.glob(jlib.path(folder) + "/**/*.md", recursive=True):
            if os.path.basename(f) not in skip:
                parts.append(open(f, encoding="utf-8").read())
    for f in sec.get("judge_only_files", []):
        if f.endswith(".md") and os.path.exists(jlib.path(f)):
            parts.append(open(jlib.path(f), encoding="utf-8").read())
    for f in glob.glob(jlib.ROOT + "/**/*.md", recursive=True):
        if "/.git/" in f or "/Party/" in f:
            continue
        t = open(f, encoding="utf-8").read()
        if sec["judge_only_tag"] in t.split("\n---", 1)[0]:
            parts.append(t)
        else:
            parts.append(callout_blocks(t, [sec["judge_only_callout"], cfg["logs"]["session_log"]["judge_block"]]))
    for d in jlib.actor_dirs(cfg):
        for f in glob.glob(os.path.join(d, "*.json")):
            j = jlib.load_actor(f).get("judge")
            if j:
                parts.append(json.dumps(j, ensure_ascii=False))
                parts += [str(x) for x in j.values() if isinstance(x, str)]
    rules = cfg["rules"]["clone_dir"]
    for f in glob.glob(os.path.join(rules, "vault/Bestiaries/**/*.md"), recursive=True):
        parts.append(open(f, encoding="utf-8").read())
    return "\n".join(parts)


def player_corpus(cfg):
    parts = []
    for f in cfg["secrecy"]["player_facing"]:
        if f.endswith(".md") and os.path.exists(jlib.path(f)):
            parts.append(open(jlib.path(f), encoding="utf-8").read())
        elif f.endswith("/"):
            for g in glob.glob(jlib.path(f) + "**/*.md", recursive=True):
                parts.append(open(g, encoding="utf-8").read())
    # rumours already told in play are in every prompt by design, even when worded as the Judge's table
    rn = cfg["logs"]["rumours"]
    if os.path.exists(jlib.path(rn["note"])):
        _, rbody = jlib.read_note(rn["note"])
        parts += [l for l in jlib.section(rbody, rn["section"]) if l.strip().startswith(("- ", "* "))]
    return "\n".join(parts)


def wall_hits(cfg, text, allow=""):
    """Judge-only note titles, markers, and any 8-word run shared with Judge-only text (not also player-facing)."""
    sec = cfg["secrecy"]; banned = []
    for folder in sec["judge_only_folders"]:
        if folder.startswith("Campaign"):
            continue
        banned += [os.path.basename(p)[:-3] for p in glob.glob(jlib.path(folder) + "/*.md")]
    banned = [b for b in banned if b not in sec.get("revealed", [])]
    banned += [sec["judge_only_tag"], "[!danger]", "Judge only", "[!judge]", "[H] "]
    hits = [f"marker/title: {b}" for b in banned if b.lower() in text.lower()]
    common = shingles(text) & shingles(judge_corpus(cfg))
    common -= shingles(player_corpus(cfg)) | shingles(allow)
    hits += [f"verbatim Judge-only text: \"{s}\"" for s in sorted(common)[:5]]
    return hits


STAT_RX = re.compile(r"\b(AC ?\d+|HD ?\d+\*?|morale [+-]?\d+|\d+ ?hp\b|hit dice|treasure type|XP value)", re.I)


# ---------------------------------------------------------------- build
def compact_sheet(s, owner, hp_now=None):
    a = s.get("attributes") or {}
    def at(k):
        v = a.get(k) or {}
        m = v.get("mod", 0)
        return f"{k} {v.get('score', '?')}" + (f"({m:+d})" if isinstance(m, int) and m else "")
    ac = s.get("ac") or {}
    sv = s.get("saves") or {}
    w = "; ".join(f"{x.get('name')} {x.get('damage', '')}".strip() + (f" range {x['range'].get('short')}/{x['range'].get('medium')}/{x['range'].get('long')}"
                  if isinstance(x.get("range"), dict) and x["range"].get("short") else "") for x in s.get("weapons") or [] if x.get("name"))
    pr = s.get("proficiencies") or {}
    profs = ", ".join(x.get("name") + (f" {x['throw']}" if x.get("throw") else "") for x in (pr.get("class") or []) + (pr.get("general") or []) if x.get("name"))
    sp = s.get("spells") or {}
    rep = "; ".join(f"L{k}: {', '.join(v)}" for k, v in (sp.get("repertoire") or {}).items() if v)
    g = s.get("gear") or {}
    gear = []
    for k, v in g.items():
        if isinstance(v, dict):
            item = v.get("item") or ", ".join(v.get("contents") or [])
            if item:
                gear.append(f"{k.replace('_', ' ')}: {item}")
    coins = ", ".join(f"{v}{k}" for k, v in (s.get("coins") or {}).items() if v)
    mv = s.get("movement") or {}
    pt = s.get("proficiency_throws") or {}
    hp = f"{hp_now}/{s.get('hp_max')}" if hp_now is not None else f"{s.get('hp_max')} max"
    lines = [f"**{s.get('name')}** ({owner}) — {s.get('class')} {s.get('level', '')}" + (f", {s.get('title')}" if s.get('title') else "")
             + (f" · {s.get('occupation')}" if s.get('occupation') else "") + (f" · XP {s.get('xp', 0)}/{s['xp_next']}" if s.get('xp_next') else "") + f" · {s.get('alignment', '')}",
             f"  hp {hp} · AC {ac.get('shield', '?')} (no shield {ac.get('no_shield', '?')}) · init {s.get('initiative', 0):+} · attack throw {s.get('attack_throw', '?')}+ · "
             + " ".join(at(k) for k in ("STR", "INT", "WIL", "DEX", "CON", "CHA")),
             f"  saves P{sv.get('paralysis', '?')} D{sv.get('death', '?')} B{sv.get('blast', '?')} I{sv.get('implements', '?')} S{sv.get('spells', '?')} · "
             + (" ".join(f"{w} {pt[k]}+" for k, w in (("listening", "listen"), ("searching", "search"), ("climbing", "climb")) if pt.get(k)) + " · " if any(pt.get(k) for k in ("listening", "searching", "climbing")) else "") + f"speed {mv.get('exploration', '?')}/{mv.get('combat', '?')}/{mv.get('running', '?')}" + (f" · enc {s['encumbrance_st']} st" if s.get('encumbrance_st') else "")]
    if w: lines.append(f"  weapons: {w}")
    if profs: lines.append(f"  proficiencies: {profs}")
    if s.get("class_features"): lines.append(f"  features: {s['class_features']}")
    if rep: lines.append(f"  spells: {rep} (per day {sp.get('per_day')})")
    if gear: lines.append("  gear: " + " · ".join(gear))
    if coins or s.get("gems"): lines.append(f"  money: {coins}" + (f"; {s['gems']}" if s.get("gems") else ""))
    tr = s.get("treasure") or []      # stage 5 player records only (the true records sit under judge:, popped above)
    if tr:
        def lot(x):
            v = (f"worth {x['value_gp']:,.0f}gp" if x.get("value_gp") is not None else
                 f"looks worth {x['apparent_value_gp']:,.0f}gp" if x.get("apparent_value_gp") is not None else "value unknown")
            k = [y for y in x.get("known") or [] if not str(y).startswith("value ")]
            return f"{x.get('id')} {x.get('looks')} ({v}{'; ' + ', '.join(k) if k else ''})"
        lines.append("  treasure carried: " + "; ".join(lot(x) for x in tr))
    if s.get("hired"):
        h = s["hired"]
        lines.append(f"  hired by {h.get('employer', '?')} on {h.get('date', '?')} at {h.get('wage_gp', '?')} gp/month" + (f"; terms: {h['terms']}" if h.get("terms") else ""))
    return "\n".join(lines)


def memory_text(cfg, pids, site):
    _, a = cfg_party(cfg); out = []
    for pid in pids:
        _, body = jlib.read_note(os.path.join(a["memory"], pid + ".md"))
        secs = [(h, [l for l in jlib.section(body, h) if l.strip().startswith("- ")]) for h in MEM_SECTIONS]
        secs = [f"  {h}: " + " ".join(l.strip()[2:] for l in ls) for h, ls in secs if ls]
        if secs:
            out.append(f"- {player_name(cfg, pid)}:\n" + "\n".join(secs))
    _, nb = jlib.read_note(a["party_notes"])
    for short, h in NOTE_SECTIONS.items():
        if short == "Map notes":
            continue
        ls = [l.strip() for l in jlib.section(nb, h) if l.strip().startswith("- ")]
        if ls:
            out.append(f"- Party notes, {short}:\n  " + "\n  ".join(ls))
    if site:   # every Map notes subsection whose name starts with the site name
        subs = [h for h in re.findall(r"^### (.+)$", "\n".join(jlib.section(nb, "Map notes")), re.M) if h.lower().startswith(site.lower())]
        ls = [f"{h}: " + " ".join(l.strip()[2:] for l in jlib.section(nb, h) if l.strip().startswith("- ")) for h in subs]
        out.append(f"- Party notes, map of {site}:\n  " + ("\n  ".join(ls) if ls else "(nothing mapped yet)"))
    rn = cfg["logs"]["rumours"]
    _, rbody = jlib.read_note(rn["note"])
    heard = [l.strip() for l in jlib.section(rbody, rn["section"]) if l.strip().startswith(("- ", "* "))]
    if heard:
        out.append("- Rumours heard (as told in play):\n  " + "\n  ".join(heard))
    return "\n".join(out) or "(no notes yet)"


def rules_note(cfg, spec):
    _, a = cfg_party(cfg)
    note, _, head = spec.partition("#")
    root = cfg["rules"]["clone_dir"]
    hits = glob.glob(os.path.join(root, "vault", "**", note if note.endswith(".md") else note + ".md"), recursive=True)
    if not hits:
        die(f"rules note not found: {note}")
    rel = os.path.relpath(hits[0], root)
    for bad in a.get("rules_refused", []):
        if rel.startswith(bad):
            die(f"REFUSED: {rel} is under {bad} (not player-side rules)")
    fm, body = jlib.read_note(os.path.relpath(hits[0], jlib.ROOT)) if False else (None, open(hits[0], encoding="utf-8").read())
    body = jlib.FM.sub("", body)
    if head:
        sec = jlib.section(body, head)
        if not sec:
            die(f"heading not found in {note}: {head}")
        body = f"## {head}\n" + "\n".join(sec)
    src = re.search(r"\*\[\[[^|\]]*\|([^\]]+)\]\]", body)
    body = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", body)
    body = re.sub(r"\[\[([^\]]*)\]\]", r"\1", body)
    body = re.sub(r"`dice:[^`]*`", "", body)
    return f"#### {os.path.basename(hits[0])[:-3]}{' — ' + head if head else ''} ({src.group(1) if src else rel})\n{body.strip()}"


def player_sections(cfg, text):
    """A campaign note without its Judge-only callouts, Judge blocks and the empty play-notes placeholder."""
    starts = [cfg["secrecy"]["judge_only_callout"], cfg["logs"]["session_log"]["judge_block"]]
    out, on = [], False
    for ln in text.splitlines():
        s = ln.strip()
        if any(s.startswith(x) for x in starts):
            on = True; continue
        if on and s.startswith(">"):
            continue
        on = False
        if s.startswith("*Add play notes here"):
            continue
        out.append(ln)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def campaign_note(cfg, spec):
    """--note NOTE[#Heading]: a campaign (not rules) note by path or title, player sections only. Refused: notes in a
    Judge-only folder or file, or tagged Judge-only. Whatever is left still goes through the wall."""
    note, _, head = spec.partition("#")
    sec = cfg["secrecy"]
    cand = [jlib.path(note)] if os.path.exists(jlib.path(note)) else \
        [f for f in glob.glob(jlib.ROOT + "/**/" + (note if note.endswith(".md") else note + ".md"), recursive=True)
         if "/.git/" not in f]
    if not cand:
        die(f"campaign note not found: {note}")
    rel = os.path.relpath(cand[0], jlib.ROOT)
    if any(rel.startswith(f.rstrip("/") + "/") for f in sec["judge_only_folders"]) or rel in sec.get("judge_only_files", []):
        die(f"REFUSED: {rel} is Judge-only")
    text = open(cand[0], encoding="utf-8").read()
    if sec["judge_only_tag"] in text.split("\n---", 1)[0]:
        die(f"REFUSED: {rel} is tagged {sec['judge_only_tag']}")
    body = player_sections(cfg, jlib.FM.sub("", text))
    if head:
        part = jlib.section(body, head)
        if not part:
            die(f"heading not found in {rel}: {head}")
        body = f"## {head}\n" + "\n".join(part)
    body = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", body)
    body = re.sub(r"\[\[([^\]]*)\]\]", r"\1", body)
    return f"#### {os.path.basename(cand[0])[:-3]}{' — ' + head if head else ''} (campaign note: {rel})\n{body.strip()}"


def cmd_build(args):
    cfg = jlib.config(); p, a = cfg_party(cfg)
    if not args or args[0].startswith("--"):
        die("usage: party.py build BRIEF [--rules NOTE[#Heading]]... [--note NOTE[#Heading]]... [--rules-file F]... [--site NAME] [--out F]")
    brief = open(args[0], encoding="utf-8").read().strip()
    errs = brief_errors(brief)
    unparty = "\n".join(l for l in brief.splitlines() if not l.startswith("**Party:**"))   # the party's own hp is fine
    ours = [m.get("name") for m in (public(cfg)[1].get("party") or []) if m.get("name")]
    for m in STAT_RX.finditer(unparty):   # allowed only after one of the party's own names, in the same line and clause
        ls = unparty.rfind("\n", 0, m.start()) + 1
        near = re.split(r"[.;:!?]", unparty[max(ls, m.start() - 60):m.start()])[-1]
        if not any(n in near for n in ours):
            errs.append(f"statistic-like term in the brief (never a creature's AC, HD, hp, morale): {m.group(0)}")
    if errs:
        die("BRIEF MALFORMED:\n- " + "\n- ".join(errs))
    priv = brief.startswith("### Private brief")
    pids = [x["id"] for x in players(cfg)]
    if priv:
        pids = [pid_of(cfg, brief.splitlines()[0].rsplit("·", 1)[1].strip())]
    rules = [rules_note(cfg, r) for r in vals(args, "--rules")]
    rules += [campaign_note(cfg, n) for n in vals(args, "--note")]
    rules += [open(f, encoding="utf-8").read().strip() for f in vals(args, "--rules-file")]
    fm, pub, sbody = public(cfg)
    hp = {m.get("name"): m.get("hp") for m in pub.get("party") or []}
    sheets = []
    for x in players(cfg):
        if x["id"] not in pids:
            continue
        s = sheet(x.get("pc"))
        if s.get("name"):
            sheets.append(compact_sheet(s, player_name(cfg, x["id"]), hp.get(s["name"])))
            for aid in character_ids(cfg):
                h = sheet(aid)
                if h.get("role") == "henchman" and (h.get("hired") or {}).get("employer") == s["name"]:
                    sheets.append(compact_sheet(h, f"henchman of {s['name']}", hp.get(h.get("name"))))
    if not priv and p.get("user_pc"):
        u = sheet(p["user_pc"])
        if u.get("name"):
            sheets.append(compact_sheet(u, "the user's PC: never speak or act for it", hp.get(u["name"])))
    table_rules = "\n".join(l for l in jlib.section(sbody, "Table rules") if l.strip().startswith("- "))
    profs = "\n\n".join(re.sub(r"^# ", "### ", profile(cfg, pid)[1], flags=re.M) for pid in pids)
    _, heur = jlib.read_note(a["heuristics"])
    base = open(jlib.path(a["base_prompt"]), encoding="utf-8").read().strip()
    variable = "\n\n".join([memory_text(cfg, pids, val(args, "--site")), "\n\n".join(sheets), "\n\n".join(rules), brief])
    allow = table_rules + "\n" + json.dumps(pub, ensure_ascii=False, default=str)   # Table rules and public: are player-facing
    hits = wall_hits(cfg, variable + "\n" + table_rules, allow=allow)
    if hits:
        die("WALL REFUSED (fix the brief, rules text or notes; never pass Judge-only text):\n- " + "\n- ".join(hits))
    code = "K-" + secrets.token_hex(3).upper()
    prompt = "\n\n".join([
        base,
        "## Table rules\n" + (table_rules or "(none recorded)"),
        "## The players\n" + profs,
        "## Shared table skill\n" + re.sub(r"^#+ .*\n", "", heur.strip(), count=1).replace("\n## ", "\n### "),
        "## Party memory (player-facing notes)\n" + memory_text(cfg, pids, val(args, "--site")),
        "## Characters (as the players see them)\n" + ("\n\n".join(sheets) or "(no characters yet)"),
        "## Rules text passed by the Judge\n" + ("\n\n".join(rules) or "none"),
        "## Scene brief\n" + brief,
        f"Call code: {code}",
        f"End the first line of your declaration with \" · code {code}\" (the call code above). "
        "Reply now with the declaration only, in the exact format above."])
    prompt = "\n".join(l if len(l) <= LINE_MAX else "\n".join(textwrap.wrap(l, LINE_MAX, break_on_hyphens=False))
                       for l in prompt.split("\n"))
    if len(prompt) > PROMPT_MAX:
        die(f"PROMPT TOO LONG: {len(prompt)} chars (max {PROMPT_MAX}, one Read must return it whole); "
            "pass less rules text or prune the memory notes")
    out = val(args, "--out") or os.path.join(a.get("call_dir", "/tmp/kardakia-party"), "prompt.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(prompt + "\n")
    out = os.path.abspath(out)
    json.dump({"path": out, "chars": len(prompt), "code": code},
              open(os.path.join(os.path.dirname(out), "last_prompt.json"), "w"))
    print(f"prompt: {out} · {len(prompt)} chars · ~{len(prompt) // 4} tokens · players {', '.join(pids)} · wall ok")
    print("agent prompt: " + pointer(out))


def brief_errors(b):
    errs = []
    first = b.splitlines()[0] if b else ""
    if not re.match(r"^### (Scene brief|Private brief) — S\d+ · step \d+ · ", first):
        errs.append("first line must be '### Scene brief — S## · step <n> · <date>, <time> · <place>' (or Private brief … · <Player>)")
    pos = -1
    for h in BRIEF_HEADS:
        m = re.search(rf"^\*\*{re.escape(h)}:\*\*", b, re.M)
        if not m:
            errs.append(f"missing **{h}:**"); continue
        if m.start() < pos:
            errs.append(f"**{h}:** out of order")
        pos = m.start()
    if "<" in b and re.search(r"<(narration|the decision|the user declaration)", b):
        errs.append("stub placeholder left in the brief")
    m = re.search(r"^\*\*Call:\*\* (\S+)", b, re.M)
    if m and m.group(1) not in TYPES:
        errs.append(f"call type {m.group(1)} unknown")
    return errs


# ---------------------------------------------------------------- check
def unfence(text):
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[1] if "\n" in t else ""
        if t.rstrip().endswith("```"):
            t = t.rstrip()[:-3]
    return t


def parse_decl(text):
    lines = unfence(text).splitlines()
    while lines and not lines[0].startswith("###"):
        lines.pop(0)
    out = {"_head": lines[0] if lines else "", "_order": []}
    cur = None
    for ln in lines[1:]:
        m = re.match(r"^\*\*([^*]+):\*\*\s*(.*)$", ln.strip())
        if m and m.group(1) in HEADS:
            cur = m.group(1); out[cur] = [m.group(2)] if m.group(2) else []; out["_order"].append(cur); continue
        if cur is not None and ln.strip():
            out[cur].append(ln.rstrip())
    return out


def bullets(v):
    return [l.strip()[2:].strip() for l in v if l.strip().startswith("- ")]


def decl_errors(cfg, d, brief, raw, code=None):
    errs = []
    tail = rf" · code {code}" if code else ""
    mb = re.match(r"^### (Scene|Private) brief — (S\d+) · step (\d+)", brief.splitlines()[0])
    call = re.search(r"^\*\*Call:\*\* (\S+) · (\S+) · caller (.*?) · declare for (.*)$", brief, re.M)
    typ = call.group(1) if call else "decide"
    if mb:
        if mb.group(1) == "Scene":
            want = rf"^### Party declaration — {mb.group(2)} · step {mb.group(3)}{tail}\s*$"
        else:
            want = rf"^### Private declaration — {mb.group(2)} · step {mb.group(3)} · .+{tail}\s*$"
        if not re.match(want, d["_head"]):
            shown = want.strip('^$').replace(chr(92) + "s*", "").replace(chr(92), "")
            errs.append("first line must match: " + (shown.replace(code, "<the call code from your prompt file>") if code else shown))
    if raw.strip() and not unfence(raw).startswith("###"):
        errs.append("text before the declaration heading")
    need = [h for h in HEADS if h != "Character choices"] + (["Character choices"] if typ.startswith("create") else [])
    for h in need:
        if h not in d:
            errs.append(f"missing **{h}:**")
    order = [h for h in HEADS if h in d]
    if d["_order"] != order:
        errs.append("headings out of order: " + ", ".join(d["_order"]))
    for h in ("Table talk", "Individual actions", "Defiance", "Character choices", "Questions to Judge", "Memory updates"):
        stray = [l for l in d.get(h, [])[1 if d.get(h) and not d[h][0].strip().startswith("- ") else 0:]
                 if l.strip() and not l.strip().startswith("- ") and not l.startswith("  ")]
        if stray:
            errs.append(f"stray text under **{h}:** (only '- ' bullets allowed): {stray[0][:60]}")
    names = {player_name(cfg, x["id"]) for x in players(cfg)}
    talk = bullets(d.get("Table talk", []))
    if not talk and [x for x in d.get("Table talk", []) if x.strip().lower() != "none"]:
        errs.append("Table talk must be bullets '- <Player>: <line>' or 'none'")
    count = {}
    for t in talk:
        who = t.split(":", 1)[0].strip()
        if who not in names:
            errs.append(f"Table talk speaker '{who}' is not an active AI player")
        count[who] = count.get(who, 0) + 1
        if len(t.split()) > 55:
            errs.append(f"Table talk line too long ({who})")
    errs += [f"{w}: {n} table-talk lines (max {TALK_MAX})" for w, n in count.items() if n > TALK_MAX]
    if call and typ not in ("counsel", "end") and not typ.startswith("create"):
        acts = bullets(d.get("Individual actions", []))
        for pc in [x.strip() for x in call.group(4).split(",") if x.strip()]:
            pcname = pc.split(" (")[0]
            if not any(a.startswith(pcname) for a in acts):
                errs.append(f"no individual action for {pc}")
    for h in ("Defiance", "Questions to Judge", "Memory updates"):
        v = d.get(h, [])
        if v and not (len(v) == 1 and v[0].strip().lower() == "none") and not bullets(v):
            errs.append(f"**{h}:** must be 'none' or bullets '- <Player>: …'")
    for m in bullets(d.get("Memory updates", [])):
        who, _, rest = m.partition(":")
        sec = rest.strip().split(":", 1)[0].strip()
        if who.strip() == "Party notes":
            if sec not in NOTE_SECTIONS:
                errs.append(f"memory update section '{sec}' (Party notes: Rumours, Plans, Map notes)")
        elif who.strip() not in names:
            errs.append(f"memory update for unknown player '{who.strip()}'")
        elif sec not in MEM_SECTIONS:
            errs.append(f"memory update section '{sec}' (use {', '.join(MEM_SECTIONS)})")
    return errs


def cmd_check(args):
    cfg = jlib.config(); _, a = cfg_party(cfg)
    if not args or "--brief" not in args:
        die("usage: party.py check DECL --brief BRIEF [--prompt F] [--tokens N] [--tool-uses N] [--retry]")
    raw = open(args[0], encoding="utf-8").read()
    brief = open(val(args, "--brief"), encoding="utf-8").read().strip()
    lp = os.path.join(a.get("call_dir", "/tmp/kardakia-party"), "last_prompt.json")
    ppath = val(args, "--prompt") or (json.load(open(lp))["path"] if os.path.exists(lp) else None)
    code = prompt_code(ppath) if ppath else None
    if not code:
        die(f"no call code found in the prompt file ({ppath}); pass --prompt with the file build wrote")
    d = parse_decl(raw)
    errs = decl_errors(cfg, d, brief, raw, code)
    tu = int(val(args, "--tool-uses", "0") or 0)
    retry = "--retry" in args
    other = sorted(set(re.findall(r"\bK-[0-9A-F]{6}\b", raw)) - {code})
    if other:
        errs.append(f"WALL: the output carries another call's code ({', '.join(other)}); discard it and call again")
    if not retry and tu != 1:
        errs.append(f"WALL: the agent made {tu} tool call(s); a fresh call must make exactly 1 (its Read of the "
                    "prompt file). Discard this output and call again")
    hits = wall_hits(cfg, raw)
    errs += ["WALL: " + h for h in hits]
    warn = sorted(set(m.group(0) for m in STAT_RX.finditer(raw)))
    fm, _, _ = public(cfg)
    mb = re.match(r"^### \w+ brief — S\d+ · step (\d+)", brief)
    call = re.search(r"^\*\*Call:\*\* (\S+)", brief, re.M)
    rec = {"session": fm.get("session"), "t": int(time.time()), "step": int(mb.group(1)) if mb else None,
           "type": call.group(1) if call else "?", "ok": not errs, "tokens": int(val(args, "--tokens", "0") or 0),
           "est_prompt": len(open(ppath, encoding="utf-8").read()) // 4, "est_output": len(raw) // 4,
           "tool_uses": None if retry else tu, "retry": retry, "code": code, "errors": errs[:5]}
    with open(jlib.path(a["call_log"]), "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    if warn:
        print("CHECK WARN: statistic-like terms (confirm they are the party's own sheet values, not a monster's): " + ", ".join(warn))
    if errs:
        print("DECLARATION MALFORMED:\n- " + "\n- ".join(errs)); sys.exit(1)
    print(f"declaration ok · type {rec['type']} · ~{rec['est_output']} output tokens" + (f" · {rec['tokens']} reported" if rec["tokens"] else ""))


def cmd_talk(args):
    d = parse_decl(open(args[0], encoding="utf-8").read())
    talk = bullets(d.get("Table talk", []))
    print("**Table** — " + (" · ".join(talk) if talk else "(quiet)"))
    print("**Call:** " + " ".join(d.get("Caller", [])).strip())
    defi = bullets(d.get("Defiance", []))
    if defi:
        print("**Defiance:** " + " · ".join(defi))
    q = bullets(d.get("Questions to Judge", []))
    if q:
        print("**Questions:** " + " · ".join(q))


# ---------------------------------------------------------------- memory
def add_bullet(rel, heading, line, sub=None):
    fm, body = jlib.read_note(rel)
    lines = body.split("\n")
    idx = next((i for i, l in enumerate(lines) if re.match(rf"^##+ {re.escape(heading)}\s*$", l)), None)
    if idx is None:
        die(f"{rel}: no section {heading}")
    if sub:   # ### <site> subsection under Map notes
        j = next((k for k in range(idx + 1, len(lines)) if lines[k].strip() == f"### {sub}"), None)
        if j is None:
            end = next((k for k in range(idx + 1, len(lines)) if re.match(r"^## ", lines[k])), len(lines))
            lines[end:end] = ["", f"### {sub}", ""]
            j = end + 1
        idx = j
    end = next((k for k in range(idx + 1, len(lines)) if re.match(r"^##", lines[k])), len(lines))
    while end > idx + 1 and not lines[end - 1].strip():
        end -= 1
    lines.insert(end, line)
    jlib.write_note(rel, fm, "\n".join(lines))


def cmd_memory(args):
    cfg = jlib.config(); _, a = cfg_party(cfg)
    fm, _, _ = public(cfg)
    S = val(args, "--session") or f"S{int(fm.get('session') or 0):02d}"
    files = [x for x in args if not x.startswith("--") and x != val(args, "--session")]
    ids = {player_name(cfg, x["id"]): x["id"] for x in players(cfg)}
    n = 0
    for f in files:
        d = parse_decl(open(f, encoding="utf-8").read())
        for m in bullets(d.get("Memory updates", [])):
            who, _, rest = m.partition(":")
            sec, _, note = rest.strip().partition(":")
            who, sec, note = who.strip(), sec.strip(), re.sub(r"^S\d+:\s*", "", note.strip())
            if who == "Party notes":
                if sec == "Map notes":
                    site, _, note = note.partition(":")
                    add_bullet(a["party_notes"], NOTE_SECTIONS[sec], f"- {S}: {re.sub(r'^S[0-9]+:[ ]*', '', note.strip())}", sub=site.strip())
                else:
                    add_bullet(a["party_notes"], NOTE_SECTIONS[sec], f"- {S}: {note}")
            elif who in ids and sec in MEM_SECTIONS:
                add_bullet(os.path.join(a["memory"], ids[who] + ".md"), sec, f"- {S}: {note}")
            else:
                print(f"skipped (unknown player or section): {m}"); continue
            n += 1
    hits = []
    for f in glob.glob(jlib.path(a["memory"]) + "/*.md") + [jlib.path(a["party_notes"])]:
        hits += wall_hits(cfg, open(f, encoding="utf-8").read())
    if hits:
        print("WALL WARNING in Party notes (remove before saving):\n- " + "\n- ".join(hits)); sys.exit(1)
    print(f"memory: {n} update(s) written")


def cmd_costs(args):
    cfg = jlib.config(); _, a = cfg_party(cfg)
    fm, _, _ = public(cfg)
    try:
        rows = [json.loads(l) for l in open(jlib.path(a["call_log"]), encoding="utf-8")]
    except FileNotFoundError:
        rows = []
    rows = [r for r in rows if r["session"] == fm.get("session")]
    tot = 0
    for r in rows:
        t = r["tokens"] or ((r["est_prompt"] or 0) + r["est_output"])
        tot += t
        print(f"- party agent step {r['step']} ({r['type']}): ~{t // 1000}k tokens"
              f"{' (reported)' if r['tokens'] else ' (estimated)'}, prompt ~{(r['est_prompt'] or 0) // 1000}k"
              f"{'' if r['ok'] else ' · MALFORMED: ' + '; '.join(r['errors'])}")
    print(f"- party agent total: {len(rows)} call(s), ~{tot // 1000}k tokens")


# ---------------------------------------------------------------- args
def val(args, k, default=None):
    return args[args.index(k) + 1] if k in args and args.index(k) + 1 < len(args) else default


def vals(args, k):
    return [args[i + 1] for i, x in enumerate(args) if x == k and i + 1 < len(args)]


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("stub", "impulse", "build", "check", "talk", "memory", "costs"):
        print(__doc__); sys.exit(1)
    a = sys.argv[2:]
    if "--players" in a:
        ONLY = set(val(a, "--players").split(","))
    globals()["cmd_" + sys.argv[1]](a)
