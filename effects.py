import tkinter as tk

import json

from effect import Effect
from add_effect import AddEffect
from colors import colors

class Effects(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=colors["bg1"])

        # Store list of effect objects
        self.effects = []

        # Store list of buttons
        self.buttons = []

        # Store canvas object ids for scrolling
        self.canvas_object_ids = []

        self.width = 300
        self.height = 300

        self.create_widgets()
        self.refresh_colors()


    def create_widgets(self):

        self.canvas = tk.Canvas(self)
        self.container = tk.Frame(self.canvas)
        self.canvas.grid(row=1, column=0)
        self.scroll_config()

        self.canvas_object_ids.append(
            self.canvas.create_window(
                (0,0),
                window=self.container,
                anchor='nw'
            )
        )

        self.container.bind("<Configure>", self.scroll_config)
        self.container.bind("<Motion>", self.scroll_config)

        # Scroll with mouse wheel

        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

        # Buttons

        self.add_button = tk.Button(
            self,
            text="+",
            width=1,
            command=self.show_add_effects
        )
        self.add_button.grid(
            row=0, 
            column=0,
            padx=10,
            pady=10
        )
        self.buttons.append(self.add_button)


    def show_add_effects(self):
        self.add_effects = AddEffect(self)

    def add_effect(self, name):
        self.get_params(name)
        self.effects.append(Effect(
            self.container,
            name,
            self.get_params(name)
        ))
        row_number = len(self.effects)
        self.effects[-1].grid(
            row=row_number, 
            column=0, 
            columnspan=5,
            padx=5,
            pady=5
        )


    def get_processes(self):
        processes = []

        for effect in self.effects:
            processes.append(
                {
                    "name": effect.name,
                    "params": effect.get_effect_params()
                }
            )

        return processes


    def scroll_config(self, event=None):
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all"),
            width=self.width,
            height=self.height
        )

    
    def on_mouse_wheel(self, event):
        # if PLATFORM == "Windows":
        #     self.canvas.yview_scroll(-1*(event.delta/120), "units")
        # else:
        self.canvas.yview_scroll(-1*(event.delta), "units")


    def refresh_colors(self):
        for button in self.buttons:
            button.configure(
                highlightbackground=colors["bg1"],
                foreground=colors["bg1"]
            )


    def get_params(self, name):
        data = []

        with open("data/effect_data.json", "r") as f:
            data = json.load(f)

        for effect in data:
            if effect["name"] == name:
                return effect["params"]


    def reset(self):
        for effect in self.effects:
            effect.grid_forget()
        self.effects.clear()

    def set_effects(self, effects):
        self.reset()

        for effect in self.effects:
            self.add_effect(effect["name"])

    def get_effects(self):
        effects = []
        
        for effect in self.effects:
            effects.append(effect)

        print(effects)
        return effects