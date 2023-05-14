# Vaatimusmäärittely

## Sovelluksen tarkoitus

Norri-peli on korttipeli, jossa tarkoitus on päästä korteista eroon. Pelin voittaa ensimmäisenä korteistaan eroon päässyt pelaaja

### Käyttöliittymäluonnos

Pelin aloittaessa sovelluksessa on tilastonäkymä ja mahdollisuus aloittaa peli. Pelin ollessa käynnissä pelaaja näkee omat korttinsa sekä toisten, tietokoneen ohjaamien pelaajien korttien määrän. 

#### Tilanne viikon lopussa

Peli toimii graafisesti. Aloitusnäkymä päivitetty, peli toimii nyt vain 6 pelaajalla..


### Pelin toiminta

Koko pakka jaetaan pelaajille tasan. Pelaajan ollessa vuorossa, hänen tulee pelata pöytäpakkaan pöytäpakan päällimmäistä korttia suurempi kortti samaa maata. Mikäli pelaaja ei voi tai ei halua pelata korttia, hänen tulee nosta pöytäpakan pohjalla oleva kortti. Mikäli pöytäpakassa on yhtä paljon kortteja kuin pelaajia, pakka kaatuu ja pakassa olevat kortit poistuvat pelistä. Uuden pöytäpakan aloittaa pelaaja, joka löi edelliseen pakkaan viimeisen kortin ("kaatoi" edellisen pakan). Ristikakkonen aloittaa pelin. Ruutu on valttia, risti on kovaa. Tämä tarkoittaa sitä, että ristin päälle voi pelata vain ja ainoastaan ristiä. Ruutua voi pelata hertan ja padan päälle, ja pienin ruutu on suurempi kuin isoin pata tai hertta. Ensimmäisen kierroksen jälkeen pöytäpakan saa aloittaa millä tahansa kortilla. 

####Tilanne lopussa

Peli käynnistyy start-painikkeesta ja aloittaa suoraan 6 pelaajalla. 

#### Esimerkkejä pelitilanteista

Pöytäpakan päällimmäinen kortti on herttakuningas. Seuraava pelaaja voi pelata päälle herttaässän tai minkä tahansa valttikortin. 

Pöytäpakan päällimmäinen kortti on ristikymppi. Tämän päälle voi pelata vain ristijätkän, -kuningattaren, -kuninkaan tai -ässän. 

Pöytäpakan päällimmäinen kortti on pataysi. Seuraava pelaaja pelaa ruutukolmosen. Nyt ruutukolmosen päälle voi pelata vain ruutunelosen tai suuremman. 

Pelaajia on pelin alussa kuusi. Yksi pelaaja voittaa pelin, joten pelaajia jää jäljelle viisi. Nyt pöytäpakan kaatumiseen riittää viisi korttia. 
