import tkinter as tk

from effect import Effect

class Amplify(Effect):
    def __init__(self, master):
        Effect.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        
        self.start_val_var = tk.StringVar()
        self.start_val = tk.Spinbox(
            self,
            textvariable=self.start_val_var,
            width=2
        )
        self.start_val.grid(row=0, column=0, padx=5, pady=5)
        self.start_val_var.set(0.1)
        
        self.end_val_var = tk.StringVar()
        self.end_val = tk.Spinbox(
            self,
            textvariable=self.end_val_var,
            width=2
        )
        self.end_val.grid(row=0, column=1, padx=5, pady=5)
        self.end_val_var.set(0.1)