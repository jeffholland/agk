import tkinter as tk

# Base class for the Effect module

class Effect(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.info_button = tk.Button(
            self,
            bitmap="info"
        )
        self.info_button.grid(
            row=0, 
            column=6, 
            sticky=tk.E, 
            padx=5, 
            pady=5
        )