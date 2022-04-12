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
    
    def create_budget(self, name, start, end, initial):
        budget = Budget(name = name, user = self._user, start= start, end = end, initial = initial)
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
