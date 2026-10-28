#!/usr/bin/env python3
"""Matriky MZA Brno (Acta Publica) bez prohlížeče.

  mza.py obec "Název"                 – najde obec (id)
  mza.py svazky <obec_id>             – svazky obce: číslo knihy | detail_id | N/O/Z roky
  mza.py info <detail_id>             – počet snímků
  mza.py snimek <detail_id> <n> <šířka|0> out.jpg [x0,y0,x1,y1]
                                      – stáhne snímek n (od 1); šířka 0 = plné rozlišení;
                                        volitelný výřez jako zlomky 0–1
  mza.py link <detail_id> <n>         – trvalý odkaz na snímek
Stahuje přes curl (Python dostává od serveru chyby)."""
import html, json, re, subprocess, sys, urllib.parse

BASE = "https://www.mza.cz/actapublica/"
IIP = "https://www.mza.cz/iipsrv/iipsrv.fcgi"


def get(url, out=None, ajax=False):
    cmd = ["curl", "-sS", "-L", "-m", "120", "--retry", "3"]
    if ajax:
        cmd += ["-H", "X-Requested-With: XMLHttpRequest"]
    if out:
        subprocess.run(cmd + ["-o", out, url], check=True)
        return None
    return subprocess.run(cmd + [url], check=True, capture_output=True).stdout.decode("utf-8", "replace")


def detail(did):
    s = get(f"{BASE}matrika/detail/{did}")
    m = re.search(r"CreateSeadragon\(\s*(\[.*?\]),\s*(\[.*?\]),", s, re.S)
    srcs, names = json.loads(m.group(1)), json.loads(m.group(2))
    paths = [urllib.parse.unquote(x.split("Deepzoom=", 1)[1])[:-4] for x in srcs]
    return paths, names


def snimek(p, wid, out, rgn):
    """Server pustí jen dlaždice DeepZoom – stáhne potřebné a slepí je (Pillow)."""
    import math, tempfile, os
    from concurrent.futures import ThreadPoolExecutor
    from PIL import Image
    dzi = get(f"{IIP}?Deepzoom={p}.dzi")
    W, H = (int(x) for x in re.search(r'Width="(\d+)" Height="(\d+)"', dzi).groups())
    T = int(re.search(r'TileSize="(\d+)"', dzi).group(1))
    x0, y0, x1, y1 = map(float, rgn.split(","))
    top = math.ceil(math.log2(max(W, H)))
    lev = top
    while wid and lev > 0 and math.ceil(W / 2 ** (top - lev)) * (x1 - x0) / 2 > wid:
        lev -= 1
    w, h = math.ceil(W / 2 ** (top - lev)), math.ceil(H / 2 ** (top - lev))
    px0, py0, px1, py1 = int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)
    tiles = [(c, r) for c in range(px0 // T, (px1 - 1) // T + 1) for r in range(py0 // T, (py1 - 1) // T + 1)]
    tmp = tempfile.mkdtemp()
    def fetch(cr):
        f = os.path.join(tmp, f"{cr[0]}_{cr[1]}.jpg")
        get(f"{IIP}?Deepzoom={p}_files/{lev}/{cr[0]}_{cr[1]}.jpg", f)
        return cr, f
    img = Image.new("RGB", (px1 - px0, py1 - py0), "white")
    with ThreadPoolExecutor(6) as ex:
        for (c, r), f in ex.map(fetch, tiles):
            img.paste(Image.open(f), (c * T - px0, r * T - py0))
    if wid and img.width > wid:
        img = img.resize((wid, round(img.height * wid / img.width)), Image.LANCZOS)
    img.save(out, quality=90)


def main(a):
    if a[0] == "obec":
        s = get(f"{BASE}ajax/matrika/autocomplete_obec?term={urllib.parse.quote(a[1])}", ajax=True)
        for o in json.loads(s):
            if o:
                print(o["id"], "|", o["label"])
    elif a[0] == "svazky":
        s = get(f"{BASE}matrika/hledani?typ=obec&obec_id={a[1]}")
        for tr in re.findall(r"<tr.*?</tr>", s, re.S)[1:]:
            d = re.search(r"matrika/detail/(\d+)", tr)
            tds = [html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))).strip()
                   for t in re.findall(r"<td.*?</td>", tr, re.S)]
            if d and len(tds) >= 9:
                print(f"{tds[0]} | {d.group(1)} | {tds[1]} | N {tds[3]} | O {tds[5]} | Z {tds[7]} | snímků {tds[-2] if len(tds) > 10 else ''}")
    elif a[0] == "info":
        paths, names = detail(a[1])
        print(len(names), "snímků;", names[0], "…", names[-1])
    elif a[0] == "link":
        paths, names = detail(a[1])
        print(f"{BASE}matrika/detail/{a[1]}?image={names[int(a[2]) - 1]}")
    elif a[0] == "snimek":
        paths, names = detail(a[1])
        snimek(paths[int(a[2]) - 1], int(a[3]), a[4], a[5] if len(a) > 5 else "0,0,1,1")
        print(a[4])
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:] or ["?"])
