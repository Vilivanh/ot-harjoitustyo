Laajennettu monopoli-pelin toimintalogiikka

```mermaid
 classDiagram
        Pelilauta --> "40" Ruutu
        Pelaaja --> "1" Pelinappula
        Pelinappula --> Ruutu
        Pelilauta --> "2-8" Pelaaja
	Type "katu" <--> "omistaja" Pelaaja
	Toiminto <--> Ruutu
	Pelilauta <--> "vankila" "aloitus" Sijainti
        class Ruutu{
                seuraava ruutu
		Type
		Toiminto
		Sijainti
        }
        class pelaaja{
                pelinappula
        }
        class Noppa{
                silmäluku
        }
	class Type{
		Aloitus
		Vankila
		Sattuma ja yhteismaa
		Asema tai laitos
		Katu
	}
	class Toiminto
	
```
