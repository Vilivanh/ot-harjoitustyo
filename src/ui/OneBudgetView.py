from tkinter import ttk, Tk, constants
from services.BudgetService import BudgetService

class OneBudgetView:
    def __init__(self, budget_name, root):
        self._root = root
        self._budget_name = budget_name
        self._frame = None
        self._initialize()

    def _initialize(self):
        budget_information = BudgetService.show_budget_information(self._budget_name)
        label = ttk.Label(master = self._root, text = f"{self._budget_name}")
        label.grid(row = 0, column = 0, columnspan = 1)
        initial = budget_information[4][5]
        planned_income_len = len(budget_information[0])
        real_income_len = len(budget_information[2])
        initial_label = ttk.Label(master = self._root, text = f"{initial}")
        initial_label.grid(row = 0, column = 1, text = f"Starting sum: {initial}")
        if planned_income_len == 0:
            plansumlabel = ttk.Label(master=self._root, text = "no planned incomes")
            plansumlabel.grid(row = 1, column = 0, columnspan = 1)
        else:
            for i in range(planned_income_len):
                sumlabel = ttk.Label(master = self._root, text = f"{budget_information[0][5]}")
                sumlabel.grid(row = i+1, column = 0, columnspan = 1)
                datelabel = ttk.Label(master = self._root, text = f"{budget_information[0][6]}")
                datelabel.grid(row = i+1, column = 1, columnspan = 1)
        if real_income_len == 0:
            realsumlabel = ttk.Label(master=self._root, text = "no incomes")
            realsumlabel.grid(row = 1, column = 0, columnspan = 1)
        else:
            for i in range(real_income_len):
                sumlabel = ttk.Label(master = self._root, text = f"{budget_information[2][5]}")
                sumlabel.grid(row = i+1, column = 2, columnspan = 1)
                datelabel = ttk.Label(master = self._root, text = f"{budget_information[2][6]}")
                datelabel.grid(row = i+1, column = 3, columnspan = 1)
        planned_outcome_len = len(budget_information[1])
        real_outcome_len = len(budget_information[3])
        if planned_outcome_len == 0:
            planoutcomelabel = ttk.Label(master=self._root, text = "no planned outcomes")
            planoutcomelabel.grid(row = 1, column = 2, columnspan = 1)
        else:
            for i in range(planned_outcome_len):
                outcomelabel = ttk.Label(master = self._root, text = f"{budget_information[1][5]}")
                outcomelabel.grid(row = i+1, column = 2, columnspan = 1)
                datelabel = ttk.Label(master = self._root, text = f"{budget_information[1][6]}")
                datelabel.grid(row = i+1, column = 3, columnspan = 1)
        if real_outcome_len == 0:
            realoutcomelabel = ttk.Label(master=self._root, text = "no outcomes")
            realoutcomelabel.grid(row = 1, column = 2, columnspan = 1)
        else:
            for i in range(real_outcome_len):
                outcomelabel = ttk.Label(master = self._root, text = f"{budget_information[3][5]}")
                outcomelabel.grid(row = i+1, column = 2, columnspan = 1)
                datelabel = ttk.Label(master = self._root, text = f"{budget_information[3][6]}")
                datelabel.grid(row = i+1, column = 3, columnspan = 1)

        date_label = ttk.Label(master = self._root, text = "Date")
        date_label.grid(row = 0, column = 1, columnspan = 1)
        self.date_entry = ttk.Entry(master = self._root)
        content_label = ttk.Label(master = self._root, text = "Category")
        content_label.grid(row = 0, column = 2, columnspan = 1)
        self.content_entry = ttk.Entry(master = self._root)
        button1 = ttk.Button(master=self._root, text="Add planned income to a budget", command=self._handle_button1_click)
        button2 = ttk.Button(master=self._root, text = "Add true income to a budget")
        button3 = ttk.Button(master=self._root, text = "Add planned outcome")
        button4 = ttk.Button(master=self._root, text = "Add true outcome")
        button1.grid(row = planned_income_len+2, column = 1, sticky=(constants.E, constants.W), padx = 30)
        button2.grid(row = real_income_len+2, column = 2, sticky=(constants.E, constants.W), padx = 30)
        button3.grid(row = planned_outcome_len+2, column = 1, sticky=(constants.E, constants.W), padx = 30)
        button4.grid(row = real_outcome_len+2, column = 2, sticky=(constants.E, constants.W), padx = 30)

    def _handle_button1_click(self):
        date_entry = self.date_entry.get()
        content_entry = self.content_entry.get()
        income = "1"
        planned = "1"
        BudgetService.add_to_budget(self._budget_name, content_entry, date_entry, income, planned)

    def _handle_button2_click(self):
        date_entry = self.date_entry.get()
        content_entry = self.content_entry.get()
        income = "1"
        planned = "0"
        BudgetService.add_to_budget(self._budget_name, content_entry, date_entry, income, planned)

    def _handle_button3_click(self):
        date_entry = self.date_entry.get()
        content_entry = self.content_entry.get()
        income = "0"
        planned = "1"
        BudgetService.add_to_budget(self._budget_name, content_entry, date_entry, income, planned)

    def _handle_button4_click(self):
        date_entry = self.date_entry.get()
        content_entry = self.content_entry.get()
        income = "0"
        planned = "0"
        BudgetService.add_to_budget(self._budget_name, content_entry, date_entry, income, planned)


window = Tk()
window.title("Bugdet app")

ui = OneBudgetView(window)

window.mainloop()