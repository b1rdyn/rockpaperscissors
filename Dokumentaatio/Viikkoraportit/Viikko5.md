# Viikko 5

Tällä viikolla kirjoitin vertauspalautteen ja luin saamani vertaispalautteen ja käytin sitä hyväksi projektini kehityksessä.
Keskityin erityisesti tekoälyjärjestelmän parantamiseen, testauksen laajentamiseen sekä dokumentaation viimeistelyyn.  
Suurimmat työvaiheet olivat:

- MultiAI:n logiikan selkeyttäminen ja uudelleenrakentaminen niin, että
  - viisi Markov-tekoälyä oppivat yhtä aikaa
  - MultiAI valitsee sen AI:n, jolla on paras ajantasainen pisteytys
- Testauksen laajentaminen ja korjaaminen palautteen perusteella:
  - lisäsin puuttuvat testit `score_for_ai`-funktiolle
  - lisäsin`test_ai_multi.py` -testit
- Päivitin testausdokumentin
- Lisäsin debug-tulosteen, josta näkee pelin aikana, mikä AI parhaillaan pelaa (lähinnä omaksi mielenkiinnoksi)

### Opin
- Opin rakentamaan tekoälyjärjestelmän, jossa useat AI:t oppivat yhtä aikaa ja niiden suoritusta vertaillaan reaaliaikaisesti.

### Ongelmia
Kaikki ongelmat saatiin ratkaistua, mutta MultiAI:n rakenteen ja testien yhteensovittaminen oli viikon haastavin osa.

### Seuraavaksi
- projektin dokumentaation viimeistely
- mahdollisesti visuaalisen analyysin testidatasta
- varmistaa tekoälyn oppiminen
- koodin viimeistely ja hionta
- kokeilla lisätä uuden AI-strategian MultiAI:n rinnalle


Arvioitu työaika tällä viikolla: 12 tuntia
