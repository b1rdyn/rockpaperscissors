## Testausdokumentti

### Testauksen tavoite

Testauksella varmistetaan, että

- siirtojen vertailulogiikka toimii oikein
- eri tekoälyt käyttäytyvät odotetulla tavalla
- pääohjelma toimii kokonaisuutena

### Yksikkötestaus

Projektissa käytetään yksikkötestaukseen **pytest**-kirjastoa.  
Yksikkötestit sijaitsevat `tests/`-hakemistossa.

#### 2.1.1 Pelin tuloslogiikka (`score_for_ai`)

On testattu, että jokainen mahdollinen siirtoyhdistelmä tuottaa oikean tuloksen.  
Kaikki 9 tapausta (R/P/S × R/P/S) on käyty läpi.

| AI-siirto | Pelaaja | Odotettu tulos |
|----------:|---------|-----------------|
| R         | S       | AI voittaa      |
| R         | P       | AI häviää       |
| S         | S       | Tasapeli        |
| P         | R       | AI voittaa      |
| S         | P       | AI voittaa      |
| P         | S       | AI häviää       |

#### ai_random.py

- Jokainen siirto esiintyi välillä 20–50 %  
  → ei vinoumaa, toimii kuten satunnaisgeneraattori

#### ai_markov.py

- oppiiko AI yksinkertaisen kuvion (esim. 8×R → ennustus R)
- toistuuko ennuste todennäköisesti oikein
- päivittyvätkö Markov-taulukot oikein `update()`-metodissa

#### ai_multi.py

#### main.py

- hyväksyy R/P/S/Q
- virheellinen syöte tulostaa `"Invalid input."`
- pistelogiikka päivittyy oikein
- ohjelma sulkeutuu komennolla `Q`


