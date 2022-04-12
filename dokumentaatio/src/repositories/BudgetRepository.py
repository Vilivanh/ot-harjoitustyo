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

        return list(user_budgets)

    def create(self, budget):
        budgets = self.find_all()

        budgets.append(budget)

        self._write(budgets)

        return budgets


    def delete(self, budget_name):

        budgets = self.find_all()

        budgets_without_id = filter(lambda budget: budget.name != budget_name, budgets)

        self._write(budgets_without_id)

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

                budget_id = parts[0]
                content = parts[1]
                done = parts[2] == '1'
                username = parts[3]

                user = UserRepository.find_by_username(
                    username) if username else None

                budgets.append(
                    Budget(content, done, user, budget_id)
                )

        return budgets

    def _write(self, budgets):
        self._ensure_file_exists()

        with open(self._file_path, 'w', encoding='utf-8') as file:
            for budget in budgets:
                username = budget.user.username if budget.user else ''

                row = f'{budget.id};{budget.name};{budget.start};{budget.end};{username};'

                file.write(row+'\n')


budget_repository = BudgetRepository(BUDGETS_FILE_PATH)