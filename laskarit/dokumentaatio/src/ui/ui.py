from tkinter import Tk, ttk

class UI:
    def __init__(self, root):
        self.root = root
    def start(self):
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
