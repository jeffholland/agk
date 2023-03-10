import tkinter as tk

from colors import colors

class Effect(tk.Frame):
    def __init__(self, master, name, params, index):

        tk.Frame.__init__(self, master, bg=colors["hl1"])

        self.master = master
        self.name = name
        self.index = index

        # params imported from data/effect_data.json
        self.params = params

        # dimensions - height based on num params
        self.width = self.master.master.master.width - 20
        self.height = 50 + (30 * len(self.params))

        # empty arrays to store the GUI elements
        self.widgets = []
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
            columnspan=(numcolumns - 1)
        )
        self.widgets.append(self.name_label)

        # delete button

        self.delete_button = tk.Button(
            self,
            text="x",
            width=1,
            command=self.delete
        )
        self.delete_button.grid(
            row=0,
            column=(numcolumns - 1),
            padx=5,
            pady=5
        )
        self.widgets.append(self.delete_button)

        # Iterate through parameters and create fields for each

        current_row = 1

        for param in self.params:

            # Unpack expected dict values
            name = param["name"]
            start = param["start_val"]
            end = param["end_val"]

            wrap = 60

            # First label + entry: start value
            label1text = f"{name} start"
            self.widgets.append(tk.Label(
                self,
                text=label1text,
                wraplength=wrap
            ))
            self.widgets[-1].grid(row=current_row, column=0)
        
            self.vars.append(tk.StringVar())
            self.entries.append(tk.Entry(
                self,
                textvariable=self.vars[-1],
                width=4
            ))
            self.entries[-1].grid(row=current_row, column=1)
            self.vars[-1].set(start)

            # Second label + entry: end value
            label2text = f"{name} end"
            self.widgets.append(tk.Label(
                self,
                text=label2text,
                wraplength=wrap
            ))
            self.widgets[-1].grid(row=current_row, column=2)
            
            self.vars.append(tk.StringVar())
            self.entries.append(tk.Entry(
                self,
                textvariable=self.vars[-1],
                width=4
            ))
            self.entries[-1].grid(row=current_row, column=3)
            self.vars[-1].set(end)

            current_row += 1

        # Set padding
        for label in self.widgets:
            label.grid_configure(padx=5, pady=5)
        for entry in self.entries:
            entry.grid_configure(padx=5, pady=5)

    def refresh_colors(self):
        for label in self.widgets:
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

    def refresh_params(self):
        count = 0
        for var in self.vars:
            if count % 2 == 0:
                idx = int(count / 2)
                self.params[idx]["start_val"] = var.get()
            else:
                idx = int((count - 1) / 2)
                self.params[idx]["end_val"] = var.get()
            count += 1

    def delete(self):
        self.master.master.master.delete_effect(self.index)