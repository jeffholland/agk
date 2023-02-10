import tkinter as tk

from colors import colors
from effect_amplify import Amplify
from effect_echo import Echo

# Frame container for Effect widgets

class EffectContainer(tk.Frame):
    def __init__(self, master, name):
        tk.Frame.__init__(
            self, 
            master,
            bg=colors["bg1"]
        )

        self.name = name

        self.effect = None

        self.create_widgets()

    def create_widgets(self):
        match self.name:
            case "Amplify":
                self.effect = Amplify(self)
            case "Echo":
                self.effect = Echo(self)

        if self.effect == None:
            raise NameError("Effect created with invalid name")

        self.effect.grid(row=0, column=0, pady=10)