# Sovelluksen arkkitehtuuri

## Rakenne

Sovellus mukailee referenssinä olevan Todo-appin rakennetta, koska allekirjoittanut ei keksi parempaakaan toimintatapaa ja olettaa tämän olevan toimiva.



```mermaid
 flowchart TB;
      UI-.->Services 
      Services-.->Repositories 
      Services-.->Entities 
      Repositories-.->Entities 

```


## Käyttöliittymä

Käyttöliittymän näkymät ovat seuraavat: 
- Kirjautuminen
- Uuden käyttäjän luominen
- Uuden budjetin luominen kirjautuneelle käyttäjälle
- Budjettilistaus
- Yksittäinen budjetti



## Sovelluslogiikka

```mermaid
 classDiagram
      Budget "*" --> "1" User
      Budget --> BudgetPlan
      User --> "can have many" Budget
      BudgetPlan "1" -->  "effects" Budget
      class User{
          username
          password
      }
      class Budget{
          Name
          Startind date
          End date
          Initial sum
          Planned
          In or out
          Content
          Beginning          
      }
```

Budget-luokka on ainoa olio, jota tarvitaan. Budgettia luodessa asetetaan starting date, end date, name ja initial sum. 
Näistä start- ja end datet toistuvat. Beginning-arvo on 0 tai 1, riippuen siitä, onko kyseessä budjetin luominen vai tiedon tallennus. 
Planned saa arvon 0, jos kyseessä on suunnitelma ja arvon 1, jos kyseessä on toteutunut meno
 

## Tietojen tallennus

Repositories-pakkauksella on kaksi luokkaa: BudgetRepository (joka pitää sisällään tiedot budjeteista) ja UserRepository (joka pitää sisällään tiedot käyttäjistä). 
Molemmat luokat tallentavat tiedostot SQLite-tietokantaan. 
Tulossa on vielä kolmas luokka, joka tallentaa budjettien yksityiskohdat. Tämä luokka luo jokaiselle budjetille oman tietokannan, josta haetaan ko. budjetin yksityiskohdat.  

## Päätoiminnallisuudet

### Kirjautuminen


```mermaid
 sequenceDiagram
      actor User
      participant UI
      participant BudgetRepository
      participant UserRepository
      User->>UI: click "Login"
      UI->>BudgetRepository: login("user","password")
      BudgetRepository->>UserRepository: find_by_username("user")
      UserRepository-->>BudgetRepository: user
      BudgetRepository-->>UI: user
      UI->>UI: show_budgets() 
```

### Budjetin luominen 

```mermaid
 sequenceDiagram
      actor User
      participant UI
      participant BudgetRepository
      participant UserRepository
      User->>UI: click "Create budget"
      UI->>BudgetRepository: create_budget("name","start", "end", "initial sum")
      BudgetRepository->>UserRepository: find_by_name("name")
      UserRepository-->>BudgetRepository: none
      BudgetRepository-->>UI: budget
      UI->>UI: show_budgets()
```


### Budjetin seuranta ja toteuttaminen

```mermaid
 sequenceDiagram
      actor User
      participant UI
      participant BudgetRepository
      participant UserRepository
      User->>UI: click "show budget"
      UI->>BudgetRepository: click "add income"
      BudgetRepository-->>UI: budget
      UI->>UI: show_budgets()
```
### Tietojen lisääminen budjettiin 

```mermaid
 sequenceDiagram
      actor User
      participant UI
      participant BudgetRepository
      participant UserRepository
      participant Budget
      User->>UI: click "Add to budget"
      UI->>BudgetRepository: Current_budget
      BudgetRepository->>UI: Budget_name, start, end
      UI->>Budget: add_to_budget(Budget_name, start, end, content, sum, date, planned, inorout)      
      Budget-->>BudgetRepository: add
      BudgetRepository-->>UI: budget
      UI->>UI: show_budgets()
```


### Muut toiminnallisuudet

Budjettilistaus näyttää kaikki kyseisen käyttäjän budjetit. Tästä listauksesta on mahdollisuus valita yksittäinen budjetti syvempään tarkasteluun. 
