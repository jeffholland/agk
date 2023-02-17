import tkinter as tk

from effect import Effect

class Echo(Effect):
    def __init__(self, master):
        Effect.__init__(self, master, "Echo")
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        super().create_widgets()


    def get_effect_params(self):
        return self.params