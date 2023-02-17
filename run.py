import tkinter as tk

from colors import colors

# This class is actually for a few buttons at the end - Run, Reset...

class Run(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=colors["bg1"])
        self.master = master
        self.widgets = []
        self.create_widgets()
        self.refresh_colors()

    def create_widgets(self):
        self.run_button = tk.Button(
            self,
            text="Run"
        )
        self.run_button.grid(row=0, column=0)
        self.widgets.append(self.run_button)

        self.reset_button = tk.Button(
            self,
            text="Reset"
        )
        self.reset_button.grid(row=0, column=1)
        self.widgets.append(self.reset_button)

    def refresh_colors(self):
        for widget in self.widgets:
            widget.configure(
                highlightbackground=colors["bg1"],
                foreground=colors["bg1"]
            )