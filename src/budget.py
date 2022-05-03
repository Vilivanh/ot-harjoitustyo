class Budgeting:
    """Luokka, joka vastaa budjettien hallinnasta.
    
    Attributes: 
        user: käyttäjä, jonka tiedoissa budjetti on
    
    """

    def __init__(self, user):
        self._user = user
        self._initial_sum = 0
        self._length = 0
        self._income = 0
        self._outcome = 0
    
    def create_budget(self, name, length, initial_sum):
        """ Luo uuden budjetin annetulle käyttäjälle.
        
        Args:
            name: käyttäjän nimi
            length: budjetin suunniteltu ajanjakso
            initial sum: rahan määrä alkuhetkellä
        """
        self._user = name
        self._length = length
        self._initial_sum = initial_sum

    
    def add_income(self, income):
        self._income += income

    def add_outcome(self, outcome):
        self._outcome += outcome

    def calculate(self):
        self._money = self._initial_sum + self._income + self._outcome
        self._days = self._length
        self._daily_sum = self._money/self._days
        return self._daily_sum

    def __str__(self):
        self._money = self._initial_sum + self._income - self._outcome
        self._days = self._length
        self._daily_sum = self._money/self._days

        return f"Daily amount: {self._daily_sum}"





