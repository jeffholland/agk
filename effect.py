import tkinter as tk

from colors import colors

# Base class for the Effect module

class Effect(tk.Frame):
    def __init__(self, master, name):
        tk.Frame.__init__(self, master, bg=colors["bg1"])

        self.master = master
        self.name = name

        self.widgets = []

        self.create_widgets()
        self.refresh_colors()

    def create_widgets(self):
        self.name_label = tk.Label(
            self,
            text=self.name
        )
        self.name_label.grid(
            row=0, 
            column=0
        )

        self.info_button = tk.Button(
            self,
            bitmap="info"
        )
        self.info_button.grid(
            row=1, 
            column=6, 
            sticky=tk.E
        )
        self.widgets.append(self.info_button)

        for widget in self.widgets:
            widget.grid_configure(padx=5, pady=5)

    def refresh_colors(self):
        for widget in self.widgets:
            widget.configure(
                highlightbackground=colors["bg1"],
                background=colors["bg1"]
            )