from pathlib import Path
from entities.budget import Budget
from repositories.UserRepository import UserRepository
from config import BUDGETS_FILE_PATH


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
                start = parts[2]
                end = parts[3]
                initial = parts[4]
                date = parts[5]
                planned = parts[6]

                user = UserRepository.find_by_username(
                    user) if user else None

                budgets.append(
                    Budget(name, user, start, end, initial, date, planned)
                )

        return budgets

    def _write(self, budgets):
        self._ensure_file_exists()

        with open(self._file_path, 'w', encoding='utf-8') as file:
            for budget in budgets:
                username = budget.user.username if budget.user else ''

                row = f'{budget.name};{username};{budget.start};{budget.end};{budget.initial};{budget.date};{budget.planned};{budget.inorout};'

                file.write(row+'\n')


budget_repository = BudgetRepository(BUDGETS_FILE_PATH)