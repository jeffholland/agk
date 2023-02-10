import tkinter as tk

from effect import Effect

class Effects(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Store list of effect objects
        self.effects = []

        # Store list of buttons
        self.buttons = []

        self.create_widgets()

    def create_widgets(self):
        self.add_button = tk.Button(
            self,
            text="+",
            width=1,
            command=self.add_effect
        )
        self.add_button.grid(row=0, column=0)
        self.buttons.append(self.add_button)

    def add_effect(self):
        self.effects.append(Effect(
            self,
            "test"
        ))
        row_number = len(self.effects)
        self.effects[-1].grid(row=row_number, column=0, columnspan=5)
