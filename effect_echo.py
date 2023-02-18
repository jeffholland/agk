import tkinter as tk

from effect import Effect

class Echo(Effect):
    def __init__(self, master):

        params = [
            {
                "name": "Delay",
                "min": 0.01,
                "max": 30.0
            },
            {
                "name": "Decay",
                "min": 0.01,
                "max": 0.99
            }
        ]

        Effect.__init__(self, master, "Echo", params)