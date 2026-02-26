# Praktiskais darbs PB1_PD18 - CI pamati un uzdevumu pārvaldība

Deniss Šablinskis, 26.02.2026
## Apraksts

Šis projekts ir izveidots, lai iegūtu pamatzināšanas par **CI**, izmantojot **GitHub Actions** automatizētai testēšanai, kā arī padziļinātu zināšanas par versiju kontroles sistēmu **Git** un tās repozitoriju platformu **GitHub**.
## Failu struktūra

Failā `.github/workflows/main.yml` tiek glabāta GitHub Actions CI konfigurācija. Fails `kalkulators.py` satur testējamo kodu, savukārt `test_kalkulators.py` ietver pašu testu loģiku. Failā `.gitignore` ir norādīti faili un mapes, kuru izmaiņām Git sistēmai nav jāseko.
## Kā palaist

Veicot `push` komandu, testu fails tiek **automātiski** palaists, lai pārbaudītu galvenā faila funkcionalitāti.
## Piemērs

Sadaļā `Actions` var redzēt, vai tests ir **veiksmīgi izpildīts**.
## Izmantotās tehnoloģijas

- Python 3.14.2
- Windows 10
- VS Code
## Definition of Done

Uzdevums ir pabeigts, ja:

- Funkcija darbojas;
- Tests iziets;
- CI ir zaļš;
- Issue pārvietots uz Done.
 