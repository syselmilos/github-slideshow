# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen**. Na začátku každé konverzace:
1. Načti skill `rodokmen` (pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.

## Prostředí (cloud, claude.ai)
- Skill je v repozitáři v `../.claude/skills/rodokmen/` (příkaz /plugin tu nefunguje), `SKILL_DIR` = tato složka.
- ImageMagick je jen verze 6 (`convert`), nástroje ji použijí samy. localhost uživatel nevidí – náhled webu posílej jako snímky.
- Kontejner je dočasný: po každém kroku ulož (git commit) a pošli (`git push -u origin claude/rodokmen-skill-plugin-ijuyco`).
