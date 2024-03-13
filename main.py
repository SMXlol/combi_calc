from tkinter import *
from operations import *


class Window:
    def __init__(self):
        self.master_window = None
        self.label = None
        self.entry = None
        self.but_value = None

    def main_window(self):
        self.master_window = Tk()
        self.master_window.title("Calculator")
        self.master_window.geometry("600x400")
        self.master_window.resizable(height=False, width=False)

    def child_window(self, value):
        self.master_window = Toplevel()
        self.master_window.title("Child Window")
        self.master_window.geometry("400x300")
        self.master_window.resizable(height=False, width=False)
        self.enter_data()

        self.create_button("No combinations", self.not_combinations, value)
        self.create_button("Yes combinations", self.yes_combinations, value)
        button = Button(self.master_window, text="Exit", command=self.master_window.destroy)
        button.pack(anchor="center", expand=1)

    def create_button(self, text, func, value):
        button = Button(self.master_window, text=text, command=lambda: func(value))
        button.pack(anchor="center", expand=1)
        return button

    def enter_data(self):
        self.entry = Entry(self.master_window)
        self.entry.pack(anchor="center", expand=1)

    def not_combinations(self, value):
        choice = {0: combinations, 1: permutations, 2: accommodation}
        entries = list(map(int, self.entry.get().split()))
        k, elements = entries[-1], entries[:-1]
        result = choice[value](elements, k)
        self.label = Label(self.master_window)
        self.label.pack(anchor="center", expand=1)
        self.label["text"] = result

    def yes_combinations(self, value):
        choice_with = {0: combinations_with, 1: permutations_with, 2: accommodation_with}
        entries = list(map(int, self.entry.get().split()))
        k, elements = entries[-1], entries[:-1]
        result = choice_with[value](elements, k)
        self.label = Label(self.master_window)
        self.label.pack(anchor="center", expand=1)
        self.label["text"] = result


window = Window()
window.main_window()
window.create_button("Permutations", window.child_window, 0)
window.create_button("Combinations", window.child_window, 1)
window.create_button("Placements", window.child_window, 2)
window.master_window.mainloop()