import tkinter as tk

from effects import Effects
from parameters import Parameters

class AudacityGlitchKitchen(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid(row=0, column=0)

        self.width = 400
        self.height = 800
        
        self.create_widgets()

    def create_widgets(self):
        self.parameters = Parameters(self)
        self.parameters.grid(row=0, column=0)

        self.effects = Effects(self)
        self.effects.grid(row=1, column=0)

app = AudacityGlitchKitchen()
app.master.title("AudacityGlitchKitchen")
app.master.geometry(str(app.width) + "x" + str(app.height))
app.mainloop()