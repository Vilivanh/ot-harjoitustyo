from calendar import day_abbr, month
from tkinter import ttk, Tk, constants
from datetime import time, timedelta, date
from services.BudgetService import BudgetService

class CreateBudgetView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()

    def _initialize(self):
        label = ttk.Label(master = self._root, text = "Create Budget")
        budget_label = ttk.Label(master = self._root, text = "Budget")
        self.budget_entry = ttk.Entry(master = self._root)
        start_label = ttk.Label(master = self._root, text = "Start date in form dd.mm.yyyy")
        self.start_entry = ttk.Entry(master = self._root)
        end_label = ttk.Label(master = self._root, text = "End date in form dd.mm.yyyy")
        self.end_entry = ttk.Entry(master = self._root)
        initial_label = ttk.Label(master = self._root, text = "Starting sum")
        self.initial_entry = ttk.Entry(master = self._root)
        button = ttk.Button(master=self._root, text="Create Budget", command=self._handle_button_click)
        
        label.grid(row = 0, column = 0, columnspan = 1)
        budget_label.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.budget_entry.grid(row = 1, column = 1, sticky =(constants.E, constants.W), padx = 30, pady = 5)
        start_label.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.start_entry.grid(row = 2, column = 1, sticky =(constants.E, constants.W), padx = 30, pady = 5)
        end_label.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.end_entry.grid(row = 3, column = 1, sticky =(constants.E, constants.W), padx = 30, pady = 5)
        initial_label.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.initial_entry.grid(row = 4, column = 1, sticky =(constants.E, constants.W), padx = 30, pady = 5)
        button.grid(row = 5, column = 1, sticky=(constants.E, constants.W), padx = 30)
        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(1, weight=1, minsize=400)

    def _handle_button_click(self):
        budget_entry_value = self.budget_entry.get()
        start_entry_value = self.start_entry.get()
        end_entry_value = self.end_entry.get()
        initial_entry_value = self.initial_entry.get()
        d1 = int(start_entry_value[0:2])
        m1 = int(start_entry_value[3:5])
        y1 = int(start_entry_value[6:])
        start = date(y1,m1,d1)
        print(start)
        d2 = int(end_entry_value[0:2])
        m2 = int(end_entry_value[3:5])
        y2 = int(end_entry_value[6:])
        end = date(y2,m2,d2)
        Budget_length = (end - start).days + 1
        if Budget_length < 1:
            label2 = ttk.Label(master = self._root, text = "Error! End date can't be smaller than start date")
            label2.grid(row = 0, column = 0, columnspan = 1)
        print(end)
        print((end - start).days + 1)
        BudgetService.create_budget(budget_entry_value, start, end, initial_entry_value, start, 0, 0, 1)
        


window = Tk()
window.title("Bugdet app")

ui = CreateBudgetView(window)

window.mainloop()