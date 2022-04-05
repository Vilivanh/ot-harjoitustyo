class Budgeting:
    def __init__(self):
        self._user = None
        self._budget_repository = {}
        self._user_repository = {}
    
    def create_budget(self, name, length, initial_sum):
        self._name = name
        self._length = length
        self._initial_sum = initial_sum
        self._budget_repository["name"] = self._name
        self._budget_repository["length"] = self._length
        self._budget_repository["sum"] = self._initial_sum
    
    def add_income(self, income):
        self._income = income
        self._budget_repository["sum"] += self._income

    def add_outcome(self, outcome):
        self._outcome = outcome
        self._budget_repository["sum"] -= self._outcome

    def calculate(self):
        self._money = self._budget_repository["sum"]
        self._days = self._budget_repository["length"]
        self._daily_sum = self._money/self._days
        return self._daily_sum





