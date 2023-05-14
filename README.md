# OT-HARJOITUSTYÖ

## NORRI-PELI

Norri on korttipeli, jossa pelaajan tehtävä on päästä korteistaan eroon. Pelaaja saa joka vuorollaan päättää, nostaako pöytäpakasta kortin vai pelaako kortin. Pelattavan kortin on oltava edellistä korttia suurempi. Jos pelaaja nostaa (riippumatta siitä, voisiko hän pelata vai ei) kortin, hän nostaa pöytäpakan pohjimmaisen kortin. Jos pöydällä on pataa tai herttaa, voi pelaaja pelata päälle suuremman padan tai hertan, tai minkä tahansa ruudun. Jos pöydässä päällimmäinen kortti on ruutu, voi pelata vain suuremman ruudun. Ristin päälle voi pelata vain ristiä. Kun pöydällä on saman verran kortteja kuin pelaajia, pöydällä oleva pakka "kaatuu" eli pöydällä olevat kortit poistuvat pelistä. Pelaaja, joka on kaatanut pakan, saa jatkaa peliä lyömällä kortin tyhjään pöytään. Pelaajan nostaessa kortin, vuoro siirtyy seuraavalle pelaajalle.  

### VIIKON 5 RELEASE

[Release](https://github.com/Vilivanh/ot-harjoitustyo/releases/tag/viikko5)

### LOPPULAUTUKSEN RELEASE

[Release](https://github.com/Vilivanh/ot-harjoitustyo/releases/tag/Loppupalautus)

#### Ohjelman käynnistäminen

1. Asenna riippuvuudet komennolla poetry install
2. Käynnistä peli komennolla poetry run invoke start

(Ohjelman käynnistäminen komentorivin kautta saattaa tuottaa virheen, sovellus aukeaa esim. Visual Studio Coden kautta, suorittamalla game_loop.py -tiedoston)

#### Testit

Testit voi suorittaa komennolla poetry run invoke test

Testikattavuusraportin saa komennolla poetry run invoke coverage-report

Pylint-raportin saa komennolla poetry run invoke lint

### DOKUMENTAATIO


### Vaatimusmäärittely

[Vaatimusmäärittely](https://github.com/Vilivanh/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

### Tuntikirjanpito

[Tuntikirjanpito](https://github.com/Vilivanh/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

### Changelog

[Changelog](https://github.com/Vilivanh/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

### Arkkitehtuuri

[Arkkitehtuuri](https://github.com/Vilivanh/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
