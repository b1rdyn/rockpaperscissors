# Käyttöohje
## Asennus ja käynnistys

Kun olet kloonannut repositorion omalle koneellesi, siirry projektin juurihakemistoon ja käynnistä poetry komennolla

```bash
poetry shell
```

Tämä vaatii siis, että koneelle on asennettu poetry. Tämän jälkeen luo virtuaaliympäristö ja lataa projektin riippuvuudet komennolla

```bash
poetry install
```

Sovelluksen voi tämän jälkeen käynnistää komennolla

```bash
poetry run python main.py
```	

Peli pyörii tällöin terminaalissa. Pelin saa suljettua antamalla terminaaliin Q ja painamalla Enter.

## Käyttö

Peli on tekstipohjainen kivi–paperi–sakset -peli, jossa vastustajana toimii tekoäly. Kun sovellus käynnistyy, terminaaliin tulostuu ohje:

Welcome to Rock Paper Scissors!
Choose [R]ock [P]aper or [S]cissors. [Q]uit.

Pelaaja voi syöttää yhden komennon:

- R – Rock (Kivi)
- P – Paper (Paperi)
- S – Scissors (Sakset)
- Q – Lopeta peli
Virheellinen syöte (muu kuin R/P/S/Q) aiheuttaa ilmoituksen “Invalid input.” ja peli pyytää uutta syötettä.

Joka kierroksella:

tekoäly valitsee siirtonsa MultiAI-järjestelmän avulla. 
Terminaali tulostaa tekoälyn siirron ja kierroksen tuloksen
Pistetilanne päivittyy
Peli tulostaa lopuksi lopputuloksen, esimerkiksi:

Final score: You 3 - AI 5

## Debug-tila

Sovelluksessa on valinnainen **debug-moodi**, jonka avulla voi seurata,
mikä viidestä Markov-tekoälystä (order 1–5) on kullakin kierroksella käytössä.
Tämä on hyödyllistä erityisesti testauksessa ja tekoälyn oppimisen havainnoinnissa.

Debug-tila otetaan käyttöön määrittämällä MultiAI seuraavasti:

```python
ai = MultiAI(focus_length=5, debug=True)
```

## Testit

Projektissa käytetään yksikkötestaukseen **pytest**-kirjastoa.  
Testit sijaitsevat `tests/`-hakemistossa.

### Testien ajaminen

Aja kaikki testit komennolla:
```bash
poetry run pytest
```
Tai jos olet jo Poetry-ympäristössä (poetry shell), riittää:
```bash
pytest
```
