# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba: Josef Sysel, * 19. 3. 1919 Kuřimská Nová Ves
- Kdo s Claudem pracuje a jak chce komunikovat: syn/dcera Josefa (uživatel), česky

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run data && npm run build`, náhled `npm run preview`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- Fáze 1: známe Josefa a rodiče (Jan Sysel * 1883 Žďárec 27, Marie Moučková * 1884). Sňatek 14. 2. 1911 Kuř. Nová Ves, Marie * Kuř. Nová Ves, Jan † 26. 6. 1951 Svinov (který Svinov? – zeptat se). Chybí úmrtí Marie a Josefa.
- Fáze 2: síť povolena. MZA Brno bez prohlížeče: `python3 -I tools/mza.py obec|svazky|info|snimek|link` (vlastní nástroj).
  Kuřimská Nová Ves = fara Deblín (obec_id 742). Knihy: N 1879–1913 = 1111 (detail 11057), N 1914–1926 = 1112 (detail 15440),
  O 1877–1944 = 1119 (detail 11567; řazená po obcích, Nová Ves cca sn. 255–275, rok 1911 = sn. 265), Z 1904–1949 = 1127 (detail 15053).
  Žďárec (obec_id 1971) = vlastní fara Žďárec.
- Doloženo: sňatek rodičů 1911, křest Marie Moučkové 1884 (kniha 1111 sn. 183), křest Jana Sysla 1883 (Žďárec, kniha 16583 = detail 7452, sn. 32).
  Křest Josefa 1919 – kniha 1112 nedigitalizovaná (archivni_dotazy.md).
  Žďárec: N 1844–1863 = detail 7451, O 1855–1949 = detail 14193 (sňatek Jan Sysel st. × Marie Orhová, asi 1875–1883), Z 1867–1926 = detail 1033.
- Doloženo navíc: sňatek Jan Sysel st. × Marie Orhová 15. 11. 1876 (O Žďárec, detail 14193, sn. 79; Rojetín sn. 67–85),
  sňatek Cyril Moučka × Marie Rábonová 10. 5. 1881 (O Deblín 1118 = detail 3880, sn. 167; Nová Ves sn. 160–168).
- Doloženy křty generace 4–7: Jan Sysel 1853 (Žďárec, detail 7451 sn. 12), Marie Orhová 1855 (Rojetín, 7451 sn. 43),
  Cyril Moučka 1856 (Rosice čp. 118, N Rosice 1835–1857 = detail 4284 sn. 112), Marie Rábonová 1853 (Nová Ves, detail 3877 sn. 200).
- Další krok: sňatky generace 8–15 (Jan Sysel × Josefa Kotová ~1845–1853 Žďárec; Josef Orha × Josefa Matysková ~1840–1855;
  Josef Moučka × Marie Sobotková ~1845–1856 Rosice/Velká Bíteš; František Rábon × Františka Chaloupková ~1840–1853 Deblín).
