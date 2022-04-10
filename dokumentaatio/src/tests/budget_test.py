import unittest
from budget import Budgeting

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budgeting("Test")

    def test_budget_exists(self):
        self.assertNotEqual(self.budget, None)

    def test_budget_creation(self):
        self.budget.create_budget("Test User",10,2000)
        self.assertEqual(str(self.budget), "Daily amount: 200.0")

    def test_adding_income(self):
        self.budget.create_budget("Test User",20,2000)
        self.budget.add_income(2000)
        self.assertEqual(str(self.budget), "Daily amount: 200.0")

    def test_adding_outcome(self):
        self.budget.create_budget("Test User", 20, 3000)
        self.budget.add_outcome(1000)
        self.assertEqual(str(self.budget), "Daily amount: 100.0")

    def test_adding_outcome_and_income(self):
        self.budget.create_budget("Test User", 20, 3000)
        self.budget.add_outcome(1000)
        self.budget.add_income(400)
        self.assertEqual(str(self.budget), "Daily amount: 120.0")