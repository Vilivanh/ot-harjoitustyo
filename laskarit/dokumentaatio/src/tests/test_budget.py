import unittest
from initial import Budgeting

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budgeting("Test")

    def test_budget_exists(self):
        self.assertNotEqual(self.Budgeting, None)

    def test_budget_creation(self):
        self.budget.create_budget("Test User",10,2000)
        self.assertEqual(str(self.budget), "Daily sum: 200.0")

    def test_adding_income(self):
        self.budget.create_budget("Test User",20,2000)
        self.budget.add_income(2000)
        self.assertEqual(str(self.budget), "Daily sum: 200.0")