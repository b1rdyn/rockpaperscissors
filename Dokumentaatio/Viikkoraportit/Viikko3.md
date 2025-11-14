### Tällä viikolla olen
- Rakentanut komentorivipohjaisen käyttöliittymän (main.py), jossa peliä voi pelata nopeasti
- Aloittanut Markov-pohjaisen tekoälyn (ai_markov.py) suunnittelun ja toteutuksen
- Suunnitellut “multi-AI”-kehikon (MultiAI), jossa useampi eri tekoäly kilpailevat keskenään ja peli käyttää sitä AI:ta, joka on viime kierroksilla pärjännyt parhaiten.

Peli käynnistyy komentoriviltä
Jokaisella kierroksella:
- pelaaja syöttää siirron (R/P/S)
- tekoäly valitsee oman siirtonsa
- ohjelma tulostaa AI:n siirron sekä kierroksen tuloksen ja päivitetyn pistetilanteen.
- Ensimmäiset kierrokset voidaan pelata satunnaisella tekoälyllä, samalla kun dataa kerätään, ja sen jälkeen voidaan käyttää oppivaa mallia

### Tällä viikolla olen oppinut ja kerrannut erityisesti:
- Miten Markov-pohjainen malli voidaan rakentaa
- Miten useita tekoälyjä voi yhdistää

### Epäselvyyksiä ja selvitettävää
- Multi-AI:n ja artikkelissa (Lähteet) kuvatun menetelmän (useita Markov-malleja + focus length) yksityiskohdat ovat vielä osittain epäselviä
- Miten pitkä focus-ikkuna (esim. 5 kierrosta) vaikuttaa käytännössä
- Markov ketjut vaativat vielä paljon hiomista ja kokeiltavaa

### Seuraavaksi:
- Viimeistellä Markov AI
- Varmistaa, että siirtymätaulukko päivittyy oikein
- Testikattavuuden seuranta
- Multi AI-valintalogiikka

Käytetty aika: 15h
