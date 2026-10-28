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
            f=["* 12. 4. 1883 Žďárec čp. 27", "zednický pomocník, 1911 Kuřimská Nová Ves čp. 10",
               "× 14. 2. 1911 Kuřimská Nová Ves Marie Moučková", "† 26. 6. 1951 Svinov u Pavlova, okres Zábřeh"],
            r=["zdarec_krest_jan_sysel_1883", "kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Narozen 12. 4., pokřtěn 13. 4. 1883 (rodina uvádí 14. 4.). Úmrtí podle rodiny i podle pozdější poznámky v křestní matrice („Svinov okres Zábřeh, dle sdělení ř. k. f. ú. Mohelnice“); Svinov u Pavlova, okres Zábřeh i Mohelnici potvrdila rodina."),
    3: dict(n="Marie Moučková", y="* 1884", st="doc",
            f=["* 14. 8. 1884 Kuřimská Nová Ves čp. 30", "1911 svobodná domkařka v Kuřimské Nové Vsi čp. 18",
               "× 14. 2. 1911 Kuřimská Nová Ves Jan Sysel"],
            r=["kurimska_nova_ves_krest_marie_mouckova_1884", "kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Narození doloženo křtem; shoduje se s údajem rodiny."),
    4: dict(n="Jan Sysel", y="* 1853", st="doc",
            f=["* 24. 7. 1853 Žďárec čp. 27", "půllánník ve Žďárci čp. 27 (1876), rolník (1883)",
               "× 15. 11. 1876 Rojetín Marie Crhová", "rolník v Kuřimské Nové Vsi (1911)"],
            r=["zdarec_krest_jan_sysel_1853", "rojetin_snatek_jan_sysel_marie_crhova_1876", "zdarec_krest_jan_sysel_1883", "kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Narozen 24., pokřtěn 25. 7. 1853. Otec mu zemřel před rokem 1875; soud v Tišnově ho 14. 12. 1875 prohlásil za zletilého, aby mohl převzít statek. Mezi 1883 a 1911 se přestěhoval do Kuřimské Nové Vsi; 1911 žil."),
    5: dict(n="Marie Crhová", y="* 1855", st="doc",
            f=["* 2. 12. 1855 Rojetín čp. 10", "1876 u otce doma v Rojetíně čp. 10", "× 15. 11. 1876 Rojetín Jan Sysel", "1911 žila"],
            r=["rojetin_krest_marie_crhova_1855", "rojetin_snatek_jan_sysel_marie_crhova_1876", "zdarec_krest_jan_sysel_1883", "kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Narozena 2., pokřtěna 3. 12. 1855. Dcera půllánníka Josefa Crhy z Rojetína."),
    8: dict(n="Jan Sysel", y="† před 1876", st="doc", f=["půllánník ve Žďárci čp. 27 (1853–1857)", "† před 15. 11. 1876"],
            r=["zdarec_krest_jan_sysel_1853", "rojetin_snatek_jan_sysel_marie_crhova_1876", "zdarec_krest_jan_sysel_1883"],
            note="Při sňatku syna 1876 už nežil (v křtu vnuka 1883 uveden jen jako rolník ve Žďárci)."),
    9: dict(n="Josefa Kotová", y="", st="doc", f=["ze Žďárce", "1876 žila"],
            r=["zdarec_krest_jan_sysel_1853", "rojetin_snatek_jan_sysel_marie_crhova_1876", "zdarec_krest_jan_sysel_1883"],
            note="Dcera půllánníka Kašpara Koty ze Žďárce (křty dětí 1853, 1855). Při sňatku syna 1876 žila."),
    22: dict(n="Josef Matyska", y="", st="doc", f=["výměnkář v Rojetíně (1855)"],
             r=["rojetin_krest_marie_crhova_1855"],
             note="Otec Josefy Matyskové, děd v křtu vnučky Marie 1855. Před jménem drobná značka – možná křížek (už nežil?), nejisté."),
    18: dict(n="Kašpar Kota", y="", st="doc", f=["půllánník ve Žďárci (1853–1857)"],
             r=["zdarec_krest_jan_sysel_1853"],
             note="Otec Josefy Kotové; v křtu vnuka 1853 čteno nejistě, v křtu vnučky Marie 1855 (sn. 16) „Kaspar Kotia(?) Halblehner in Zdiaretz“. Roku 1857 kmotr vnuka Františka."),
    10: dict(n="Josef Crha", y="", st="doc", f=["půllánník v Rojetíně čp. 10 (1855, 1876)", "1876 žil"],
             r=["rojetin_krest_marie_crhova_1855", "rojetin_snatek_jan_sysel_marie_crhova_1876", "zdarec_krest_jan_sysel_1883"],
             note="Otec nevěsty 1876, děd v křtu vnuka 1883."),
    11: dict(n="Josefa Matysková", y="", st="doc", f=["z Rojetína", "1876 žila"],
             r=["rojetin_krest_marie_crhova_1855", "rojetin_snatek_jan_sysel_marie_crhova_1876", "zdarec_krest_jan_sysel_1883"],
             note="Při sňatku dcery 1876 „Josefy Matyskovy“, v křtu vnuka 1883 „Maťýska“ – spíš Matysková."),
    6: dict(n="Cyril Moučka", y="1856 – před 1911", st="doc",
            f=["* 8. 3. 1856 Rosice čp. 118", "stolař ve Březí (1881), v Kuřimské Nové Vsi (1884, 1911)",
               "× 10. 5. 1881 Kuřimská Nová Ves Marie Ráboňová", "1884 bydlel v Kuřimské Nové Vsi čp. 30", "† před 14. 2. 1911"],
            r=["rosice_krest_cyril_moucka_1856", "kurimska_nova_ves_snatek_cyrill_moucka_marie_rabonova_1881", "kurimska_nova_ves_krest_marie_mouckova_1884", "kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Narozen 8., pokřtěn 9. 3. 1856 v Rosicích u Brna. Syn stolaře Josefa Moučky (1856 tovaryš v Rosicích, 1881 a 1884 stolař ve Březí). Roku 1911 už nežil."),
    7: dict(n="Marie Ráboňová", y="1853 – před 1911", st="doc",
            f=["* 19. 9. 1853 Kuřimská Nová Ves čp. 20",
               "× 10. 5. 1881 Kuřimská Nová Ves Cyril Moučka", "† před 14. 2. 1911"],
            r=["kurimska_nova_ves_krest_marie_rabonova_1853", "kurimska_nova_ves_snatek_cyrill_moucka_marie_rabonova_1881", "kurimska_nova_ves_krest_marie_mouckova_1884", "kurimska_nova_ves_snatek_jan_sysel_marie_mouckova_1911"],
            note="Narozena 19., pokřtěna 20. 9. 1853. Byla o dva a půl roku starší než manžel. Roku 1911 už nežila."),
    12: dict(n="Josef Moučka", y="", st="doc", f=["truhlářský tovaryš v Rosicích (1856)", "stolař ve Březí (1881, 1884)", "1881 žil"],
             r=["rosice_krest_cyril_moucka_1856", "kurimska_nova_ves_snatek_cyrill_moucka_marie_rabonova_1881", "kurimska_nova_ves_krest_marie_mouckova_1884"],
             note="Uveden jako děd z otcovy strany v křtu vnučky Marie 1884. Březí – nejspíš Březí u Kuřimi/Tišnova, ověřit."),
    13: dict(n="Marie Sobotková", y="", st="doc", f=["1881 žila"],
             r=["rosice_krest_cyril_moucka_1856", "kurimska_nova_ves_snatek_cyrill_moucka_marie_rabonova_1881", "kurimska_nova_ves_krest_marie_mouckova_1884"],
             note="Babička z otcovy strany v křtu vnučky Marie 1884."),
    14: dict(n="František Ráboň", y="", st="doc", f=["domkář a nádeník v Kuřimské Nové Vsi čp. 20 (1853)", "domkář v Kuřimské Nové Vsi (1881, 1884)"],
             r=["kurimska_nova_ves_krest_marie_rabonova_1853", "kurimska_nova_ves_snatek_cyrill_moucka_marie_rabonova_1881", "kurimska_nova_ves_krest_marie_mouckova_1884"],
             note="Děd z matčiny strany v křtu vnučky Marie 1884."),
    15: dict(n="Františka Chaloupková", y="", st="doc", f=[],
             r=["kurimska_nova_ves_krest_marie_rabonova_1853", "kurimska_nova_ves_snatek_cyrill_moucka_marie_rabonova_1881", "kurimska_nova_ves_krest_marie_mouckova_1884"],
             note="Dcera zemřelého čtvrtlánníka Františka Chaloupky (křest dcery Marie 1853)."),
    26: dict(n="Jan Sobotka", y="", st="doc", f=["domkář ve Velké Bíteši (?) (1856)"],
             r=["rosice_krest_cyril_moucka_1856"],
             note="Otec Marie Sobotkové; v křtu vnuka Cyrila 1856 „Johann, Häusler in Gr. Bitesch“ – čtení obce nejisté."),
    30: dict(n="František Chaloupka", y="† před 1853", st="doc", f=["čtvrtlánník v Rosci (?)", "† před 19. 9. 1853"],
             r=["kurimska_nova_ves_krest_marie_rabonova_1853"],
             note="Otec Františky Chaloupkové; název obce špatně čitelný."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
    8: ("Syslové", "Půllánníci (sedláci) ve Žďárci u Tišnova, statek čp. 27."),
    9: ("Kotové", "Rod Josefy Kotové, babičky Jana Sysla (* 1883)."),
    10: ("Crhové", "Půllánníci v Rojetíně čp. 10, sousední vsi Žďárce."),
    11: ("Matyskové", "Rod Josefy Matyskové z Rojetína."),
    12: ("Moučkové", "Stolaři ve Březí, později v Kuřimské Nové Vsi."),
    13: ("Sobotkové", "Rod Marie Sobotkové, manželky stolaře Josefa Moučky."),
    14: ("Ráboňové", "Domkáři v Kuřimské Nové Vsi."),
    15: ("Chaloupkové", "Rod Františky Chaloupkové, manželky Františka Ráboně."),
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
    dict(k=8, n="Marie Syslová (* 1855)", t="Sestra Jana Sysla (* 1853). Narozena 30. 7. 1855 ve Žďárci čp. 27, dcera půllánníka Jana Sysla a Josefy, dcery Kašpara Koty (N Žďárec 1844–1863, sn. 16).", r=[]),
    dict(k=8, n="František Sysel (1857)", t="Bratr Jana Sysla (* 1853). Narozen 16. 2. 1857 ve Žďárci čp. 27; kmotr Jan Malý (?) a Barbora Svobodová (N Žďárec 1844–1863, sn. 20).", r=[]),
    dict(k=7, n="František Ráboň (mladší)", t="Domkář v Kuřimské Nové Vsi čp. 20, syn Františka Ráboně a Františky roz. Chaloupkové – tedy nejspíš bratr Marie Ráboňové. Roku 1884 se mu narodila dcera Klotilda († 1890). Zapsáno na stejné stránce jako křest Marie Moučkové.",
         r=["kurimska_nova_ves_krest_marie_mouckova_1884"]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Kdy a kde se narodil Jan Sysel (otec Josefa)?",
     "Vyřešeno: 12. 4. 1883 ve Žďárci čp. 27, pokřtěn 13. 4. (rodina uváděla 14. 4.)."),
    ("Jak se za svobodna jmenovala matka Jana Sysla?",
     "Vyřešeno: Marie Crhová, dcera Josefa Crhy, rolníka v Rojetíně (křest Jana 1883)."),
    ("Kde je Svinov, kde zemřel Jan Sysel (1951)?",
     "Vyřešeno: Svinov u Pavlova, tehdy okres Zábřeh (dnes Šumperk); potvrzuje rodina i poznámka v křestní matrice. Zápis o úmrtí (fara Mohelnice) zatím nehledán – Zemský archiv Opava."),
    ("Jak se za svobodna jmenovala matka Marie Moučkové?",
     "Vyřešeno: Marie Ráboňová, dcera Františka Ráboně, domkaře v Kuřimské Nové Vsi (křest Marie 1884)."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
