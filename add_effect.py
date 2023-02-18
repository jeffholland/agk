import tkinter as tk
from tkinter import ttk

import json

class AddEffect(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.window = tk.Toplevel(self)

        # Select effect from a dropdown

        self.effect_names = self.get_effect_names()

        self.effect_selector_var = tk.StringVar()
        self.effect_selector = ttk.Combobox(
            self.window,
            state="readonly",
            values=self.effect_names,
            textvariable=self.effect_selector_var
        )
        self.effect_selector_var.set(self.effect_names[0])
        self.effect_selector.grid(row=0, column=0, columnspan=2)

        # Submit effect choice or cancel

        self.ok_button = tk.Button(
            self.window,
            text="OK",
            command=self.ok_pressed
        )
        self.ok_button.grid(row=1, column=0)

        self.cancel_button = tk.Button(
            self.window,
            text="Cancel",
            command=self.cancel_pressed
        )
        self.cancel_button.grid(row=1, column=1)

    def get_effect_names(self):
        data = []
        names = []

        with open("data/effect_data.json", "r") as f:
            data = json.load(f)

        for effect in data:
            names.append(effect["name"])
        
        return names

    
    def ok_pressed(self):
        name = self.effect_selector_var.get()
        self.master.add_effect(name)
        self.window.destroy()

    def cancel_pressed(self):
        self.window.destroy()