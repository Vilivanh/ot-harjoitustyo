
## Käyttöliittymä

Käyttöliittymään tulee aloitusnäkymä, josta voi valita sääntö- tai tilastonäkymän tai käynnistää pelin. 
Sääntö- ja tilastonäkymästä voi palata alkuun, mahdollisesti aloittaa uuden pelin. 
Uuden pelin valittuaan pelaaja valitsee, montako pelaajaa pelissä on. Tämän valinnan jälkeen peli käynnistyy

## Toiminta

Aloitusnäkymässä pelaaja valitsee, aloittaako pelin, katsooko säännöt (vai tilastot)

```mermaid
 sequenceDiagram
 	actor player
	participant UI
	participant Rules
	participant GamePlay
	participant Stats
	user->>UI: click "Rules"
	UI->>Rules: view()
	Rules->>UI: click "Return"
	user->>UI: click "Stats"
	UI->>Stats: view()
	Stats->>UI: click "Return"
	UI->>GamePlay: click "Play"
	GamePlay->>GamePlay: choose_players(number)
	GamePlay->>UI: play(number)
	UI->UI: play(number)


```


## Pelin kulku


Tietokoneet toimivat samalla lailla, tässä siis N voi olla mikä tahansa välillä 1-6, missä N merkkaa tietokoneen numeroa

```mermaid
 sequenceDiagram
	actor Player
	participant TableDeck
	participant Computer_N
	participant UI
	UI->>Player: check_hand(2 of clubs)
	Player->>UI: starter(Boolean)
	UI->>Computer_N: check_hand(2 of clubs)
	Computer_N->>UI: starter(Boolean)
	UI->>UI: starter(computer or player)
	UI->>Player: starter()
	Player-->>Player: assuming that player has two of clubs 
	Player->>UI: click "chosen card"
	UI->>TableDeck: add(chosen_card)
	UI->>Player: when starting, has to be 2 of clubs
	UI->>Computer_N: turntoplay(Computer_N)
	UI->>UI: choose(Computers_deck)
	UI->>UI: turntoplay(Computer_N + 1)
	UI-->>UI: if turntoplay == len(players), turntoplay=player
	Player->>UI: click "chosen_card"
	UI-->>UI: check(chosen_card)
	UI->>TableDeck: add(chosen_card)
```

choose-metodissa tietokone valitsee, pelaako vai nostaako kortin pohjautun pöytäpinon sisältöön. 
Pelaaja saa itse valita, nostaako vai pelaako kortin. Kortin pitää kuitenkin pelatessa olla edellistä isompi.	
