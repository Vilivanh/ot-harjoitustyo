```mermaid
 classDiagram
      Pelaaja "*" --> "1" Pelinappula

      class Pelaaja{
      Rahat    
      }

      class Noppa{
          id
      }
      class Pelilauta{
          Ruutu
      }
      Pelilauta "1" <|--|> "*" Aloitusruutu
      Pelilauta "1" <|--|> "*" Vankila
      Pelilauta "4 kappaletta" --> Asemat
      Pelilauta "4 kappaletta" --> Laitokset
      Pelilauta "useita" --> Sattuma ja yhteismaa
      Pelilauta "useita" --> Katu
      Pelinappula --> Pelilauta
      class Katu{
      Nimi
      Rakennukset
      Omistaja
      Toiminto
      }
      Class Sattuma ja yhteismaa{
      Toiminto
      }
      Class Asemat{
      Toiminto
      Omistaja
      }
      Class Laitokset{
      Toiminto
      Omistaja
      }
```
