import tkinter as tk

from effect import Effect

class Amplify(Effect):
    def __init__(self, master):

        params = [
            {
                "name": "Ratio",
                "min": 0.01,
                "max": 0.99
            }
        ]

        Effect.__init__(self, master, "Amplify", params)