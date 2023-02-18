import tkinter as tk

from effect import Effect

class Echo(Effect):
    def __init__(self, master):
        Effect.__init__(self, master, "Echo")

        self.height = 110

        self.create_widgets()
        super().refresh_colors()



    def create_widgets(self):

        # Param 1 - delay
        
        self.delay_start_val_var = tk.StringVar()
        self.delay_start_val = tk.Entry(
            self,
            textvariable=self.delay_start_val_var,
            width=2
        )
        self.delay_start_val.grid(row=1, column=0, padx=5, pady=5)
        self.delay_start_val_var.set(0.1)
        self.entries.append(self.delay_start_val)
        
        self.delay_end_val_var = tk.StringVar()
        self.delay_end_val = tk.Entry(
            self,
            textvariable=self.delay_end_val_var,
            width=2
        )
        self.delay_end_val.grid(row=1, column=1, padx=5, pady=5)
        self.delay_end_val_var.set(0.1)
        self.entries.append(self.delay_end_val)

        # Param 1 - decay
        
        self.decay_start_val_var = tk.StringVar()
        self.decay_start_val = tk.Entry(
            self,
            textvariable=self.decay_start_val_var,
            width=2
        )
        self.decay_start_val.grid(row=2, column=0, padx=5, pady=5)
        self.decay_start_val_var.set(0.1)
        self.entries.append(self.decay_start_val)
        
        self.decay_end_val_var = tk.StringVar()
        self.decay_end_val = tk.Entry(
            self,
            textvariable=self.decay_end_val_var,
            width=2
        )
        self.decay_end_val.grid(row=2, column=1, padx=5, pady=5)
        self.decay_end_val_var.set(0.1)
        self.entries.append(self.decay_end_val)

        super().create_widgets()



    def get_effect_params(self):
        delay_param = {
            "name": "Delay",
            "start_val": self.delay_start_val_var.get(),
            "end_val": self.delay_end_val_var.get()
        }
        self.params.append(delay_param)

        decay_param = {
            "name": "Decay",
            "start_val": self.decay_start_val_var.get(),
            "end_val": self.decay_end_val_var.get()
        }
        self.params.append(decay_param)

        return self.params