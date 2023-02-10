import tkinter as tk

from effect_amplify import Amplify
from effect_echo import Echo

# Frame container for Effect widgets

class EffectContainer(tk.Frame):
    def __init__(self, master, name):
        tk.Frame.__init__(
            self, 
            master
        )

        self.name = name

        self.effect = None

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(
            self,
            text=self.name
        )
        self.name_label.grid(
            row=0, 
            column=0,
            padx=5,
            pady=5
        )

        match self.name:
            case "Amplify":
                self.effect = Amplify(self)
            case "Echo":
                self.effect = Echo(self)

        if self.effect == None:
            raise NameError("Effect created with invalid name")

        self.effect.grid(row=1, column=0)