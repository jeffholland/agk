import tkinter as tk

from constants import *
from colors import colors

# This class is actually for a few buttons at the end - Run, Reset...

class Commands(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=colors["bg1"])
        self.master = master
        self.widgets = []

        self.button_width = 7
        if PLATFORM == "win32":
            self.button_width = 10

        self.create_widgets()
        self.refresh_colors()

    def create_widgets(self):
        self.run_button = tk.Button(
            self,
            text="Run",
            command=self.master.run
        )
        self.run_button.grid(row=0, column=0)
        self.widgets.append(self.run_button)

        self.reset_button = tk.Button(
            self,
            text="Reset",
            command=self.master.reset
        )
        self.reset_button.grid(row=0, column=1)
        self.widgets.append(self.reset_button)

        self.save_default_button = tk.Button(
            self,
            text="Save default",
            command=self.master.save_default
        )
        self.save_default_button.grid(row=0, column=2)
        self.widgets.append(self.save_default_button)

        self.save_preset_button = tk.Button(
            self,
            text="Save preset",
            command=self.master.save_preset
        )
        self.save_preset_button.grid(row=1, column=0)
        self.widgets.append(self.save_preset_button)

        self.load_preset_button = tk.Button(
            self,
            text="Load preset",
            command=self.master.load_preset
        )
        self.load_preset_button.grid(row=1, column=1)
        self.widgets.append(self.load_preset_button)


        # Configure space
        for widget in self.widgets:
            widget.configure(width=self.button_width)
            widget.grid_configure(padx=5, pady=5)



    def refresh_colors(self):
        for widget in self.widgets:
            widget.configure(
                highlightbackground=colors["bg1"],
                foreground=colors["bg1"]
            )