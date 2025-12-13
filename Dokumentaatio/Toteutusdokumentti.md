# Toteutusdokumentti

Projekti toteuttaa kivi–paperi–sakset -peliä pelaavan oppivan tekoälyn Pythonilla.
Ohjelma on komentoriviltä pelattava, ja sen keskeinen tavoite on mukautua
pelaajan strategiaan.

- **main.py**
  Vastaa pelin käynnistämisestä, käyttäjän syötteen lukemisesta, tulosten
  tulostamisesta sekä tekoälyn ja pelaajan välisen pelikierroksen hallinnasta.
- **ai_markov.py**  
  Sisältää Markov-pohjaisen tekoälyn (`MarkovSingleAI`), joka:
  - seuraa pelaajan aiempia siirtoja
  - päivittää siirtymätaulukkoa (`transitions`)
  - ennustaa todennäköisimmän seuraavan siirron
  - valitsee vastasiirron ennustetta vastaan
- **ai_multi.py**  
  Sisältää MultiAI-järjestelmän, joka:
  - hallitsee viittä erillistä Markov-tekoälyä
  - päivittää kaikkien tekoälyjen pisteet jokaisella kierroksella
  - valitsee aina kulloinkin parhaiten suoriutuvan tekoälyn tekemään varsinaisen siirron
-**ai_random.py**
  Valitsee satunnaisen R, P tai S ensimmäisillä kierroksilla
- **tests/**  
  Sisältää yksikkö- ja integraatiotestit keskeisille komponenteille.
  
**Aikavaativuus per kierros:**

- Siirtojen generointi: O(k), missä k = 5
- Parhaan tekoälyn valinta: O(k)
- Kokonaisuus: O(1)

| Algoritmi              | Aikavaativuus | Tilavaativuus | Mukautuvuus |
|------------------------|---------------|---------------|-------------|
| Satunnainen AI         | O(1)          | O(1)          | Ei          |
| Yksittäinen Markov-AI  | O(1)          | O(n)          | Kyllä       |
| MultiAI (5 Markovia)   | O(1)          | O(n)          | Kyllä       |

## Puutteet ja parannusehdotukset
**Nykyiset puutteet**
- Oppiminen ei säily ohjelman sulkemisen jälkeen
- Pelaaja voi voittaa tekoälyn pelaamalla täysin satunnaisesti.
**Mahdollisia parannuksia**
- Siirtymätaulukkojen ja pistetietojen tallennus JSON-muotoon.

##Laajojen kielimallien käyttö
Projektin toteutuksessa on käytetty ChatGPT apuna:
- virheiden debuggaamisessa. Jos koodi ei ole mennyt läpi enkä löydä ratkaisua, olen kysynyt ChatGPT:ltä
- selitysten ja raporttitekstin muotoilussa (.md muoto)

Koodi on kirjoitettu ja ymmärretty tekijän toimesta.

## Lähteet
- *Multi-AI competing and winning against humans in iterated Rock-Paper-Scissors game*
- Wikipedia: Markovin ketju
- Pythonin virallinen dokumentaatio

