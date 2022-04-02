```mermaid
 classDiagram
      Pelaaja "*" --> "1" Pelinappula

      class Pelaaja{
          
      }
      class Ruutu{
          sijainti
          tyyppi
      }
      class Noppa{
          id
      }
      class Pelilauta{
          ruutu
      }
      Pelilauta "1" --> "*" Aloitusruutu
      Pelilauta "1" --> "*" Vankila
      
```
