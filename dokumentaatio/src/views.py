from tkinter import ttk, Tk, constants

class LoginView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()

    def _initialize(self):
        label = ttk.Label(master = self._root, text = "Login")
        username_label = ttk.Label(master = self._root, text = "Username")
        self.username_entry = ttk.Entry(master = self._root)
        password_label = ttk.Label(master = self._root, text = "Password")
        self.password_entry = ttk.Entry(master = self._root)
        button = ttk.Button(master=self._root, text="Login", command=self._handle_button_click)
        
        label.grid(row = 0, column = 0, columnspan = 1)
        username_label.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.username_entry.grid(row = 1, column = 1, sticky =(constants.E, constants.W), padx = 30, pady = 5)
        password_label.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.password_entry.grid(row = 2, column = 1, sticky =(constants.E, constants.W), padx = 30, pady = 5)
        button.grid(row = 3, column = 1, sticky=(constants.E, constants.W), padx = 30)
        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(1, weight=1, minsize=400)

    def _handle_button_click(self):
        username_entry_value = self.username_entry.get()
        password_entry_value = self.password_entry.get()
        print(f"Username is: {username_entry_value}")
        print(f"Password is: {password_entry_value}")


window = Tk()
window.title("Bugdet app")

ui = LoginView(window)

window.mainloop()