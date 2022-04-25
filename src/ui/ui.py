from tkinter import Tk, ttk
from ui.LoginView import LoginView
from ui.CreateUserView import CreateUserView
from ui.BudgetView import BudgetView
from ui.CreateBudgetView import CreateBudgetView

class UI:
    def __init__(self, root):
        self.root = root

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
    
    def start(self):
        self._hide_current_view()
        self._current_view = LoginView(self.root)
    
    def start2(self):
        label = ttk.Label(master = self.root, text = "Hello world!")
        username_label = ttk.Label(master = self.root, text = "Username")
        username_entry = ttk.Entry(master = self.root)
        password_label = ttk.Label(master = self.root, text = "Password")
        password_entry = ttk.Entry(master = self.root)
        label.pack()
        username_label.pack()
        username_entry.pack()
        password_label.pack()
        password_entry.pack()

window = Tk()
window.title("Bugdet app")

ui = UI(window)
ui.start()

window.mainloop()
