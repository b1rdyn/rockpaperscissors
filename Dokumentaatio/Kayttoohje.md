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

Pelaaja voi kirjoittaa yhden kirjaimen:

- R – Rock (Kivi)
- P – Paper (Paperi)
- S – Scissors (Sakset)
- Q – Lopeta peli
Virheellinen syöte (muu kuin R/P/S/Q) aiheuttaa ilmoituksen “Invalid input.” ja peli pyytää uutta syötettä.



sovellus tulostaa lopullisen pistetilanteen, esimerkiksi:

Final score: You 3 - AI 5
