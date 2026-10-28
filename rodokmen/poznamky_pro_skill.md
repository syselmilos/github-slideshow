# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


## MZA Brno (Acta Publica) bez prohlížeče – nový nástroj tools/mza.py
- Hledání obce: `ajax/matrika/autocomplete_obec?term=…` funguje jen s hlavičkou `X-Requested-With: XMLHttpRequest` (jinak 404).
- Seznam svazků obce: `matrika/hledani?typ=obec&obec_id=<id>` (HTML tabulka, odkazy `matrika/detail/<id>`).
- Detail svazku obsahuje v `CreateSeadragon([...dzi], [...jména snímků], …)` seznam snímků.
- Obrazový server iipsrv pouští jen DeepZoom (`iipsrv.fcgi?Deepzoom=<cesta>.jp2.dzi` a `…_files/<level>/<x>_<y>.jpg`);
  FIF/CVT (celý JPEG) vrací 403 → nástroj stahuje dlaždice a slepí je (Pillow). curl funguje, actapublica.eu je za Cloudflare (403), www.mza.cz ne.
- Cloud (claude.ai): /plugin nefunguje → skill zkopírován do repozitáře `.claude/skills/`; síť je třeba povolit v nastavení prostředí (www.mza.cz).
- Starší oddací knihy (Žďárec 1813–1854) psané rychlou německou kurzívou: procházení po stránkách je pomalé a málo spolehlivé; lepší začít rejstříkem (u Žďárce kniha 16594, 1784–1853) nebo křty sourozenců.
