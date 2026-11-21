#!/usr/bin/env python3
"""The AX3 Borderlands regional map on the campaign's hex grid (see Adventure/Region Map.md).
  ax3grid.py center CC.RR            pixel centre of a hex on the map image
  ax3grid.py hex X Y                 the hex under a pixel
  ax3grid.py crop C1.R1 C2.R2 OUT    a labelled crop (hex numbers under each centre) for reading terrain and roads
  ax3grid.py tiles OUT HEX [HEX...]  one tile per hex (player map) for classifying terrain hex by hex
LIBRARY: the Library clone (default /home/user/library)."""
import json, math, os, sys
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None
G = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ax3_grid.json")))
LIB = os.environ.get("LIBRARY", "/home/user/library")
CW, X0, Y0, PAR = G["cw"], G["x0"], G["y0"], G["par"]
RH = CW * 2 / math.sqrt(3)


def center(col, row):
    c, r = col + 2, row + 3
    return X0 + c * CW, Y0 + r * RH + (RH / 2 if c % 2 == PAR else 0)


def hex_at(x, y):
    c = round((x - X0) / CW)
    r = round((y - Y0 - (RH / 2 if c % 2 == PAR else 0)) / RH)
    return f"{c - 2:02d}.{r - 3:02d}"


def _font(n):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", n)
    except OSError:
        return ImageFont.load_default()


def crop(a, b, out, player=False):
    im = Image.open(os.path.join(LIB, G["player_map" if player else "map"])).convert("RGB")
    d = ImageDraw.Draw(im); f = _font(13)
    for col in range(1, 52):
        for row in range(1, 33):
            X, Y = center(col, row); d.text((X - 18, Y + 12), f"{col:02d}.{row:02d}", fill=(220, 0, 160), font=f)
    (c1, r1), (c2, r2) = [tuple(map(int, h.split("."))) for h in (a, b)]
    p, q = center(c1, r1), center(c2, r2)
    im.crop((int(p[0] - 35), int(p[1] - 40), int(q[0] + 35), int(q[1] + 40))).save(out)


def tiles(out, hexes, T=96):
    im = Image.open(os.path.join(LIB, G["player_map"])).convert("RGB")
    sheet = Image.new("RGB", (10 * (T + 4), ((len(hexes) + 9) // 10) * (T + 20)), "white"); d = ImageDraw.Draw(sheet)
    for i, h in enumerate(hexes):
        X, Y = center(*map(int, h.split("."))); R = CW * 0.62
        t = im.crop((int(X - R), int(Y - R), int(X + R), int(Y + R))).resize((T, T))
        x, y = (i % 10) * (T + 4), (i // 10) * (T + 20)
        sheet.paste(t, (x, y + 18)); d.text((x + 2, y + 1), h, fill=(200, 0, 0), font=_font(14))
    sheet.save(out)


if __name__ == "__main__":
    cmd, *args = sys.argv[1:] or ["-h"]
    if cmd == "center":
        print("%.0f %.0f" % center(*map(int, args[0].split("."))))
    elif cmd == "hex":
        print(hex_at(float(args[0]), float(args[1])))
    elif cmd == "crop":
        crop(args[0], args[1], args[2], "--player" in args)
    elif cmd == "tiles":
        tiles(args[0], args[1:])
    else:
        print(__doc__)
