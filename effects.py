import tkinter as tk

from effect_container import EffectContainer
from add_effect import AddEffect
from colors import colors

class Effects(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=colors["bg2"])

        # Store list of effect objects
        self.effects = []

        # Store list of widgets
        self.buttons = []

        self.create_widgets()
        self.refresh_colors()

    def create_widgets(self):
        self.add_button = tk.Button(
            self,
            text="+",
            width=1,
            command=self.show_add_effects
        )
        self.add_button.grid(row=0, column=0, columnspan=5)
        self.buttons.append(self.add_button)

    def show_add_effects(self):
        self.add_effects = AddEffect(self)

    def add_effect(self, name):
        self.effects.append(EffectContainer(
            self,
            name
        ))
        row_number = len(self.effects)
        self.effects[-1].grid(row=row_number, column=0, columnspan=5)

    def refresh_colors(self):
        for button in self.buttons:
            button.configure(
                highlightbackground=colors["bg1"],
                foreground=colors["bg1"]
            )