from xml.dom import InvalidCharacterErr
from entities.budget import Budget
from entities.user import User
from entities.info import Info

from repositories.BudgetRepository import (
    BudgetRepository as default_budget_repository
)

from repositories.UserRepository import (
    UserRepository as default_user_repository
)

class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass

class BudgetService:
    """ Luokka, joka hallitsee budjetin toimintaa.
        
        Args:
            budjetti- ja käyttäjärepositoriot, jotka huolehtivat näiden säilömisestä
        """
    def __init__(self, BR = default_budget_repository, UR = default_user_repository):
        self._user = None
        self._BR = BR
        self._UR = UR
    
    def create_budget(self, name, start, end, initial, date, planned, inorout, beginning):
        """ Luo uuden budjettitiedon annetulle käyttäjälle.
        
        Args:
            name: käyttäjän nimi
            start: budjetin suunniteltu alkuhetki
            end: budjetin päättymishetki
            initial: rahan määrä alkuhetkellä
            date: käytetään luomaan budjetille päivämäärä
            planned: kertoo, onko kyseessä suunniteltu vai toteutunut tieto
            inorout: tulo vai meno
            beginning: määrittää, onko kyseessä budgetin luominen vai tiedon lisääminen budjettiin
        """
        budget = Budget(name = name, user = self._user, content = "0", start= start, end = end, initial = initial, date = date, planned = planned, inorout = inorout, beginning = beginning)
        return self._BR.create(budget)

    def login(self, username, password):
        user = self._UR.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("incorrect user or password")
        self._user = user
        return user

    def logout(self):
        self._user = None

    def create_user(self, username, password):
        existing_user = self._UR.find_by_username(username)
        if existing_user:
            raise UsernameExistsError("Username already exists")
        user = self._UR.create(User(username, password))
        return user


    def show_budgets(self):
        budgets = self._BR.find_by_username(self._user.username)
        return budgets

    def show_one_budget(self, budget_name):
        budget = self._BR.find_by_budget_name(budget_name)
        return budget

    def add_to_budget(self, budget_name, content, date, planned, inorout):
        budgets = self._BR.find_by_budget_name(budget_name)
        budget = budgets[0]
        user = budget.user
        start = budget.start
        end = budget.end
        initial = budget.initial
        self._BR._write(budgets)
        beginning = "0"
        new = Budget(budget_name, user, content, start, end, initial, date, planned, inorout, beginning)
        self._BR._write(budgets, new)

    def remove_from_budget(self, budget_name, content, date, inorout):
        self._BR._remove(budget_name, content, date, inorout)

    def show_budget_information(self, budget_name):
        budgets = self._BR.find_by_budget_name(budget_name)
        planned_incomes = filter(lambda budget: budget.name == budget_name and budget.inorout == "1" and budget.planned == "1", budgets)
        planned_outcomes = filter(lambda budget: budget.name == budget_name and budget.inorout == "0" and budget.planned == "1", budgets)
        true_incomes = filter(lambda budget: budget.name == budget_name and budget.inorout == "1" and budget.planned == "0", budgets)
        true_outcomes = filter(lambda budget: budget.name == budget_name and budget.inorout == "0" and budget.planned == "0", budgets)
        initial_sum = planned_incomes = filter(lambda budget: budget.name == budget_name and budget.beginning == "1" and budget.planned == "1", budgets)
        return [planned_incomes, planned_outcomes, true_incomes, true_outcomes, initial_sum]



        