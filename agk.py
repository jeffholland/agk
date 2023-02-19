import tkinter as tk

import json

from colors import colors
from effects import Effects
from parameters import Parameters
from processor import Processor
from run import Run

class AudacityGlitchKitchen(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, bg=colors["bg1"])

        self.grid(row=0, column=0)

        self.width = 400
        self.height = 600
        
        self.create_widgets()


    # Creating and initializing the main components

    def create_widgets(self):

        # GUI sections

        self.parameters = Parameters(self)
        self.parameters.grid(row=0, column=0, padx=5, pady=5)

        self.effects = Effects(self)
        self.effects.grid(row=1, column=0, padx=5, pady=5)

        self.run_buttons = Run(self)
        self.run_buttons.grid(row=2, column=0, padx=5, pady=5)

        # Glitch processor

        self.processor = Processor(self)


    # Running the glitch process

    def run(self):
        params = self.parameters.get_params()
        processes = self.effects.get_processes()

        self.processor.process(params, processes)

    # Reset effects and params

    def reset(self):
        data = {}
        with open("data/default_settings.json", "r") as f:
            data = json.load(f)

        self.parameters.set_parameters(data["params"])
        self.effects.set_effects(data["effects"])



app = AudacityGlitchKitchen()
app.master.title("AudacityGlitchKitchen")
app.master.geometry(str(app.width) + "x" + str(app.height))
app.mainloop()