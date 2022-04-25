from pathlib import Path
from entities.budget import Budget
from repositories.UserRepository import UserRepository
from config import BUDGETS_FILE_PATH
from db_connection import get_budget_connection


class BudgetRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self._read()

    def find_by_username(self, username):

        budgets = self.find_all()

        user_budgets = filter(
            lambda budget: budget.user and budgets.user.username == username, budgets)
        UB = []
        for budget in user_budgets:
            if budget not in UB:
                UB.append(budget)
        return UB

    def find_by_budget_name(self, username, name):

        budgets = self.find_all()

        the_budget = filter(
            lambda budget: budget.name==name and budgets.user.username == username, budgets)
        
        return the_budget

    def create(self, budget):
        budgets = self.find_all()

        budgets.append(budget)

        self._write(budgets)

        return budgets


    def delete(self, budget_name):

        budgets = self.find_all()

        budgets_without_name = filter(lambda budget: budget.name != budget_name, budgets)

        self._write(budgets_without_name)

    def delete_all(self):
        self._write([])

    def remove(self, budget_name, content, date, inorout):
        username = self.user
        budgets = self.find_by_budget_name(username, budget_name)
        removed_rows = filter(lambda budget: budget.name == budget_name and budget.content == content and budget.date == date and budget.inorout == inorout, budgets)

        self._write(removed_rows)



    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        budgets = []

        self._ensure_file_exists()

        with open(self._file_path, encoding='utf-8') as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(';')

                name = parts[0]
                user = parts[1]
                content = parts[2]
                start = parts[3]
                end = parts[4]
                initial = parts[5]
                date = parts[6]
                planned = parts[7]
                inorout = parts[8]
                beginning = parts[9]

                user = UserRepository.find_by_username(
                    user) if user else None

                budgets.append(
                    Budget(name, user, content, start, end, initial, date, planned, inorout, beginning)
                )

        return budgets

    def _write(self, budgets, new):
        self._ensure_file_exists()

        with open(self._file_path, 'w', encoding='utf-8') as file:
            for budget in budgets:
                username = budget.user.username if budget.user else ''

                row = f'{new.name};{username};{new.start};{new.end};{new.initial};{new.date};{new.planned};{new.inorout};{new.beginning}'

                file.write(row+'\n')


budget_repository = BudgetRepository(get_budget_connection())