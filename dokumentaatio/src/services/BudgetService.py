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
    def __init__(self, BR = default_budget_repository, UR = default_user_repository):
        self._user = None
        self._BR = BR
        self._UR = UR
    
    def create_budget(self, name, start, end, initial, date, planned, inorout, beginning):
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
        