from tkinter import Tk
from ui.ui import UI
import pygame

def main():
    window = Tk()
    window.title("Norri")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
