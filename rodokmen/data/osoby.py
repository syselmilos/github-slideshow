# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
    1: dict(n="Josef Sysel", y="* 1919", st="fam", sex="M", f=["* 19. 3. 1919 Kuřimská Nová Ves"], r=[],
            note="Otec uživatele. Údaje od uživatele (2026-10-28), zatím neověřeno v matrice."),
    2: dict(n="Jan Sysel", y="1883–1951", st="doc",
            f=["* 12. 4. 1883 (podle oddací matriky; rodina uvádí 14. 4. 1883 Žďárec čp. 27)",
               "zednický pomocník, 1911 Kuřimská Nová Ves čp. 10",
               "× 14. 2. 1911 Kuřimská Nová Ves Marie Moučková", "† 26. 6. 1951 Svinov"],
            r=["kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Sňatek doložen matrikou. Datum narození: matrika sňatků 12. 4., rodina 14. 4. – rozhodne křest. Úmrtí od rodiny."),
    3: dict(n="Marie Moučková", y="* 1884", st="doc",
            f=["* 14. 8. 1884 Kuřimská Nová Ves", "1911 svobodná domkařka v Kuřimské Nové Vsi čp. 18",
               "× 14. 2. 1911 Kuřimská Nová Ves Jan Sysel"],
            r=["kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Datum narození shodně v oddací matrice i od rodiny; místo narození od rodiny."),
    4: dict(n="Jan Sysel", y="", st="doc", f=["rolník v Kuřimské Nové Vsi (1911)"],
            r=["kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Otec ženicha v oddací matrice 1911; tehdy žil."),
    5: dict(n="Marie Orha (?)", y="", st="doc", f=["1911 žila"],
            r=["kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Rodné příjmení čteno „Orha“ – nejisté, ověřit v křtu syna Jana (1883)."),
    6: dict(n="Cyrill Moučka", y="† před 1911", st="doc", f=["stolař v Kuřimské Nové Vsi", "† před 14. 2. 1911"],
            r=["kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Otec nevěsty v oddací matrice 1911; tehdy už nežil."),
    7: dict(n="Marie Rábonová (?)", y="† před 1911", st="doc", f=["† před 14. 2. 1911"],
            r=["kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Rodné příjmení čteno „Rábon“ – nejisté, ověřit v křtu dcery Marie (1884)."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Kdy a kde se narodil Jan Sysel (otec Josefa)?",
     "Otevřené: oddací matrika 1911 uvádí 12. 4. 1883, rodina 14. 4. 1883 ve Žďárci čp. 27; jeho otec byl 1911 rolníkem v Kuřimské Nové Vsi. Rozhodne zápis o křtu."),
    ("Jak se za svobodna jmenovaly matky Jana Sysla a Marie Moučkové?",
     "Otevřené: v oddací matrice 1911 čteno „Orha“ a „Rábon“ – nejisté, ověřit v křestních zápisech."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
