from tkinter import ttk, Tk, constants

class OverView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)
        label = ttk.Label(master = self._frame, text = "Home")
        budgets_button = ttk.Button(master=self._root, text="Show Budgets", command=self._handle_button_click)
        create_button = ttk.Button(master=self._root, text="Create New Budget", command=self._create_button_click)
        exit_button = ttk.Button(master=self._root, text="Exit", command=self._exit_button_click)
        label.grid(row = 0, column = 0, columnspan = 1)

        budgets_button.grid(row = 2, column = 1, sticky=(constants.E, constants.W), padx = 30, pady = 10)
        create_button.grid(row = 3, column = 1, sticky=(constants.E, constants.W), padx = 30, pady = 10)
        exit_button.grid(row = 4, column = 1, sticky=(constants.E, constants.W), padx = 30, pady = 10)
        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(1, weight=1, minsize=100)

    def _exit_button_click(self):
        self._root.destroy()

    def _create_button_click(self):
        self._root.destroy()

    def _handle_button_click(self):
        username_entry_value = self.username_entry.get()
        password_entry_value = self.password_entry.get()
        password_entry2_value = self.password_entry2.get()
        if password_entry_value != password_entry2_value:
            print("Error! Wrong password")
        else:
            print(f"Username is: {username_entry_value}")
            print(f"Password is: {password_entry_value}")


window = Tk()
window.title("Bugdet app")

ui = OverView(window)

window.mainloop()