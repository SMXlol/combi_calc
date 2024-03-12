from tkinter import *
from tkinter import ttk

from operations import *


class Window:
    def __init__(self, stroke, n):
        self.string = stroke
        self.n = n
        self.master_window = None

    def main_window(self):
        self.master_window = Tk()
        self.master_window.title("Calculator")
        self.master_window.geometry("600x400")
        self.master_window.resizable(height=False, width=False)

    def child_window(self):
        self.master_window = Toplevel()
        self.master_window.title("Child Window")
        self.master_window.geometry("400x300")
        self.master_window.resizable(height=False, width=False)
        self.enter_data()

        self.create_button("No combinations", self.not_combinations)
        self.create_button("Yes combinations", self.yes_combinations)
        self.create_button("Exit", self.master_window.destroy)

    def create_button(self, text, func):
        button = ttk.Button(self.master_window, text=text, command=func)
        button.pack(anchor="center", expand=1)
        return button

    def enter_data(self):
        self.entry = ttk.Entry(self.master_window)
        self.entry.pack(anchor="center", expand=1)
        return self.entry

    def not_combinations(self):
        self.label = ttk.Label(self.master_window)
        self.label.pack(anchor="center", expand=1)
        self.label["text"] = self.entry.get()
        print(self.label["text"])

    def yes_combinations(self):
        self.label = ttk.Label(self.master_window)
        self.label.pack(anchor="center", expand=1)
        self.label["text"] = self.entry.get()
        print(self.label["text"])


window = Window("qwerty", 4)
window.main_window()
window.create_button("Permutations", window.child_window)
window.create_button("Combinations", window.child_window)
window.create_button("Placements", window.child_window)
window.master_window.mainloop()
