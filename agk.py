import tkinter as tk

import json

from colors import colors
from commands import Commands
from constants import *
from effects import Effects
from parameters import Parameters
from preset_save import SavePreset
from preset_load import LoadPreset
from processor import Processor
from settings import Settings
from write import write_json

class AudacityGlitchKitchen(tk.Frame):
    def __init__(self, master=None):
        
        self.width = 400
        self.height = 650

        if PLATFORM == "win32":
            self.width = 310
            self.height = 610

        tk.Frame.__init__(
            self, 
            master, 
            bg=colors["bg1"]
        )

        self.grid(row=0, column=0)
        
        self.create_widgets()


    # Creating and initializing the main components

    def create_widgets(self):

        # GUI sections

        self.parameters = Parameters(self)
        self.parameters.grid(row=0, column=0, padx=5, pady=5)

        self.effects = Effects(self)
        self.effects.grid(row=1, column=0, padx=5, pady=5)

        self.command_buttons = Commands(self)
        self.command_buttons.grid(row=2, column=0, padx=5, pady=5)

        # Glitch processor

        self.processor = Processor(self)


    # Running the glitch process

    def run(self):
        params = self.parameters.get_params()
        processes = self.effects.get_processes()

        self.processor.process(params, processes)

    # Set preset info according to JSON file
    def set_preset(self, filepath):
        data = {}
        with open(filepath, "r") as f:
            data = json.load(f)

        self.parameters.set_parameters(data["params"])
        self.effects.set_effects(data["effects"])

    # Get preset info in one convenient dictionary
    def get_preset(self):
        data = {}
        params = self.parameters.get_parameters()
        effects = self.effects.get_effects()
        data["params"] = params
        data["effects"] = effects

        return data

    # Save current settings to default

    def save_default(self):
        data = self.get_preset()

        write_json("data/default_settings.json", data)

    # Reset effects and params to default found in default_settings.json

    def reset(self):
        self.set_preset("data/default_settings.json")

    def save_preset(self):
        self.save_preset_window = SavePreset(self)

    def load_preset(self):
        self.load_preset_window = LoadPreset(self)

    def show_settings(self):
        self.settings_window = Settings(self)


app = AudacityGlitchKitchen()
app.master.title("AudacityGlitchKitchen")
app.master.geometry(str(app.width) + "x" + str(app.height))
app.mainloop()