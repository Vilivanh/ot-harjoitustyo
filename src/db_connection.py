import os
import sqlite3
from config import DATABASE_FILE_PATH, BUDGETS_FILE_PATH

dirname = os.path.dirname(__file__)

dataconnection = sqlite3.connect(DATABASE_FILE_PATH)
dataconnection.row_factory = sqlite3.Row
budgetconnection = sqlite3.connect(BUDGETS_FILE_PATH)
budgetconnection.row_factory = sqlite3.Row


def get_database_connection():
    return dataconnection

def get_budget_connection():
    return budgetconnection
