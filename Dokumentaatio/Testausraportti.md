## Testausdokumentti

### Testauksen tavoite

Testauksella varmistetaan, että

- siirtojen vertailulogiikka toimii oikein
- eri tekoälyt käyttäytyvät odotetulla tavalla
- pääohjelma toimii kokonaisuutena

### Yksikkötestaus

Projektissa käytetään yksikkötestaukseen **pytest**-kirjastoa.  
Yksikkötestit sijaitsevat `tests/`-hakemistossa.

#### Pelin tuloslogiikka (`score_for_ai`)

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

- MultiAI luo täsmälleen 5 AI:ta
- niiden `order`-arvot ovat `[1,2,3,4,5]`
- jokainen AI tekee siirron joka kierroksella
- jokaiselle AI:lle tallentuu yksi piste jokaiselta päivitetyltä kierrokselta
- kunkin AI:n `history` kasvaa → kaikki oppivat pelaajan siirroista
- `_best_ai_index()` valitsee parhaimman AI:n viimeisen `focus_length` kierroksen perusteella.
- paras AI tunnistetaan, kun yksi AI:sta on selvästi parempi
- “focus window” toimii oikein: vain viimeiset N kierrosta vaikuttavat arvioon
- erilaiset pistelistat palauttavat oikean indeksin
- MultiAI:n palauttama siirto vastaa aina sen AI:n siirtoa, jolla on korkein nykyinen kokonaispistemäärä
- kun pistetilanne muuttuu, myös “paras AI” voi vaihtua
- MultiAI päivittää kaikki AI:t joka kierroksella

#### main.py

- hyväksyy R/P/S/Q
- virheellinen syöte tulostaa `"Invalid input."`
- pistelogiikka päivittyy oikein
- ohjelma sulkeutuu komennolla `Q`


