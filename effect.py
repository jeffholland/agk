import tkinter as tk

class Effect(tk.Frame):
    def __init__(self, master, name):
        tk.Frame.__init__(
            self, 
            master,
            bg="yellow"
        )

        self.name = name

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