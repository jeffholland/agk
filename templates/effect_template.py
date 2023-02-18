# Template for an effect subclass


import tkinter as tk

from effect import Effect

class Template(Effect):
    def __init__(self, master):
        Effect.__init__(self, master, "Echo")
        self.master = master
        self.create_widgets()
        super().refresh_colors()



    def create_widgets(self):
        super().create_widgets()



    def get_effect_params(self):
        return self.params