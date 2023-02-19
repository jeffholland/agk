import tkinter as tk

from colors import colors

# Base class for the Effect module

class Effect(tk.Frame):
    def __init__(self, master, name, params):

        # params - we expect a list of dictionaries in the format:
        # {
        #   "name": "Amplify",
        #   "min": 0.01,
        #   "max": 0.99
        # }
        #
        # this info is imported from data/effect_data.json in effects.py

        tk.Frame.__init__(self, master, bg=colors["hl1"])

        self.master = master
        self.name = name
        self.params = params

        # dimensions - height based on num params
        self.width = self.master.master.master.width - 20
        self.height = 50 + (30 * len(self.params))

        # empty arrays to store the GUI elements
        self.labels = []
        self.entries = []
        self.vars = []

        self.create_widgets()
        self.refresh_colors()

    def create_widgets(self):
        self.configure(width=self.width, height=self.height)

        numcolumns = 4
        for i in range(numcolumns):
            self.columnconfigure(i, minsize=self.width / numcolumns)

        # name

        self.name_label = tk.Label(
            self,
            text=self.name
        )
        self.name_label.grid(
            row=0, 
            column=0,
            columnspan=numcolumns
        )
        self.labels.append(self.name_label)

        current_row = 1

        for param in self.params:

            # Unpack expected dict values
            name = param["name"]
            min = param["min"]
            max = param["max"]

            wrap = 60

            # First label + entry: start value
            label1text = f"{name} start"
            self.labels.append(tk.Label(
                self,
                text=label1text,
                wraplength=wrap
            ))
            self.labels[-1].grid(row=current_row, column=0)
        
            self.vars.append(tk.StringVar())
            self.entries.append(tk.Entry(
                self,
                textvariable=self.vars[-1],
                width=4
            ))
            self.entries[-1].grid(row=current_row, column=1)
            self.vars[-1].set(min)

            # Second label + entry: end value
            label2text = f"{name} end"
            self.labels.append(tk.Label(
                self,
                text=label2text,
                wraplength=wrap
            ))
            self.labels[-1].grid(row=current_row, column=2)
            
            self.vars.append(tk.StringVar())
            self.entries.append(tk.Entry(
                self,
                textvariable=self.vars[-1],
                width=4
            ))
            self.entries[-1].grid(row=current_row, column=3)
            self.vars[-1].set(max)

            current_row += 1

        # Set padding
        for label in self.labels:
            label.grid_configure(padx=5, pady=5)
        for entry in self.entries:
            entry.grid_configure(padx=5, pady=5)

    def refresh_colors(self):
        for label in self.labels:
            label.configure(
                bg=colors["hl1"],
                fg=colors["bg1"],
                highlightbackground=colors["hl1"]
            )
        for entry in self.entries:
            entry.configure(
                bg=colors["bg2"],
                fg=colors["hl2"]
            )



    def get_effect_params(self):
        output = []

        for i in range(len(self.params)):
            # Iterate through self.vars array 2 at a time
            # for the start and end vals
            var_idx_1 = i * 2
            var_idx_2 = var_idx_1 + 1

            new_param = {
                "name": self.params[i]["name"],
                "start_val": self.vars[var_idx_1].get(),
                "end_val": self.vars[var_idx_2].get()
            }

            output.append(new_param)

        print(output)
        return output