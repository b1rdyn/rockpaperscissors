Opinto-ohjelma: Matemaattisten tieteiden kandi

Projekti on kivi-paperi-sakset peliä pelaava tekoäly.

Projekti toteutetaan Pythonilla ja dokumentaation kieli on suomi.

Projektissa käytetään ja tutkitaan seuraavia algoritmisia lähestymistapoja:

Satunnaisvalinta-algoritmi: tekoäly valitsee kiven, paperin tai sakset tasatodennäköisesti (1/3 todennäköisyys jokaiselle).

Tilastollinen ennustusalgoritmi: tekoäly seuraa pelaajan aiempia valintoja ja pyrkii ennustamaan seuraavan siirron Markovin ketjun tai taajuuslaskennan avulla.

Päätöksenteko: tekoäly valitsee seuraavan siirtonsa sen perusteella, mikä vastasi todennäköisesti pelaajan edellisiä valintoja vastaan parhaiten.

Tavoitteena on kehittää tekoäly, joka pystyy pelaamaan kivi-paperi-sakset -peliä ja mukautumaan pelaajan strategiaan sen sijaan, että se valitsisi siirtonsa täysin satunnaisesti.

Syötteet ja niiden käyttö:
Käyttäjän syöte: pelaajan valinta.
Ohjelman syöte: Tekoälyn edelliset ja pelaajan aiemmat siirrot.
Näiden perusteella ohjelma laskee todennäköisyydet pelaajan seuraavalle valinnalle ja päättää tekoälyn siirron.

Aikavaatimukset: 
Satunnaisvalinta O(1)
Tilastollinen ennuste O(n)
Markovin ketju O(1)

Lähteet: TBA