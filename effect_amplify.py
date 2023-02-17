import tkinter as tk

from effect import Effect

class Amplify(Effect):
    def __init__(self, master):

        Effect.__init__(self, master, "Amplify")
        self.master = master
        self.create_widgets()
        super().refresh_colors()

    def create_widgets(self):
        
        self.start_val_var = tk.StringVar()
        self.start_val = tk.Entry(
            self,
            textvariable=self.start_val_var,
            width=2
        )
        self.start_val.grid(row=1, column=0, padx=5, pady=5)
        self.start_val_var.set(0.1)
        self.widgets.append(self.start_val)
        
        self.end_val_var = tk.StringVar()
        self.end_val = tk.Entry(
            self,
            textvariable=self.end_val_var,
            width=2
        )
        self.end_val.grid(row=1, column=1, padx=5, pady=5)
        self.end_val_var.set(0.1)
        self.widgets.append(self.end_val)

        super().create_widgets()


    def get_effect_params(self):
        param = {
            "name": "Ratio",
            "start_val": self.start_val_var.get(),
            "end_val": self.end_val_var.get()
        }
        self.params.append(param)

        return self.params