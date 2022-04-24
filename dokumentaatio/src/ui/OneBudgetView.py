from tkinter import ttk, Tk, constants
from services.BudgetService import BudgetService

class OneBudgetView:
    def __init__(self, budget, user, root):
        self._root = root
        self.budget = budget
        self._user = user
        self._frame = None
        self._initialize()

    def _initialize(self):
        budget_list = BudgetService.show_budgets
        
        for i in range(len(budget_list)):
            label = ttk.Label(master = self._root, text = f"{budget_list[i].name}")
            label.grid(row = i, column = 0, columnspan = 1)
            button = ttk.Button(master=self._root, text="Show Budget", command=self._handle_button_click)
            button.grid(row = i, column = 1, sticky=(constants.E, constants.W), padx = 30)
            self.name_entry = ttk.Entry(master = self._root)
            
        
        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(1, weight=1, minsize=400)

    def _handle_button_click(self):
        name_entry_value = self.name_entry.get()
        BudgetService.show_one_budget(name_entry_value)

    


window = Tk()
window.title("Bugdet app")

ui = OneBudgetView(window)

window.mainloop()