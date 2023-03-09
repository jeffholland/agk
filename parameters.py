import tkinter as tk

from colors import colors

class Parameters(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=colors["bg1"])
        
        self.entry_width = 28

        self.widgets = []
        self.entry_widgets = []

        self.create_widgets()

        self.refresh_colors()



    # Returns Parameters

    def get_params(self):

        # Return a dict containing all parameter values.

        import_bool = True
        if self.import_check_var.get() == 0:
            import_bool = False

        fill_gaps_bool = True
        if self.gaps_check_var.get() == 0:
            fill_gaps_bool = False

        gaps_str = self.gaps_entry_var.get().split(',')
        gaps = []
        for gap in gaps_str:
            try:
                gaps.append(int(gap))
            except ValueError:
                pass

        return {
            "folder_name": self.folder_name_var.get(),
            "counter_start": self.counter_start_var.get(),
            "num_iterations": self.num_iterations_var.get(),
            "import": import_bool,
            "fill_gaps": fill_gaps_bool,
            "gaps": gaps
        }


    def create_widgets(self):

        # folder name label

        self.folder_name_label = tk.Label(
            self,
            text="Folder name: "
        )
        self.folder_name_label.grid(row=0, column=0)
        self.widgets.append(self.folder_name_label)

        # folder name entry

        self.folder_name_var = tk.StringVar()
        self.folder_name_entry = tk.Entry(
            self,
            width=self.entry_width,
            textvariable=self.folder_name_var
        )
        self.folder_name_entry.grid(row=0, column=1)
        self.folder_name_var.set("gen1")
        self.entry_widgets.append(self.folder_name_entry)

        # counter start label

        self.counter_start_label = tk.Label(
            self,
            text="Counter start: "
        )
        self.counter_start_label.grid(row=1, column=0)
        self.widgets.append(self.counter_start_label)

        # counter start entry
        
        self.counter_start_var = tk.StringVar()
        self.counter_start_entry = tk.Entry(
            self,
            textvariable=self.counter_start_var,
            width=self.entry_width
        )
        self.counter_start_entry.grid(row=1, column=1)
        self.counter_start_var.set(0)
        self.entry_widgets.append(self.counter_start_entry)

        # num iterations label

        self.num_iterations_label = tk.Label(
            self,
            text="Num iterations: "
        )
        self.num_iterations_label.grid(row=2, column=0)
        self.widgets.append(self.num_iterations_label)

        # num iterations entry

        self.num_iterations_var = tk.StringVar()
        self.num_iterations_entry = tk.Entry(
            self,
            textvariable=self.num_iterations_var,
            width=self.entry_width
        )
        self.num_iterations_entry.grid(row=2, column=1)
        self.num_iterations_var.set(1)
        self.entry_widgets.append(self.num_iterations_entry)

        # import checkbox

        self.import_check_var = tk.IntVar()
        self.import_check = tk.Checkbutton(
            self,
            variable=self.import_check_var,
            text="Import"
        )
        self.import_check.grid(row=3, column=0)
        self.import_check_var.set(1)
        self.widgets.append(self.import_check)

        # gaps checkbox

        self.gaps_check_var = tk.IntVar()
        self.gaps_check = tk.Checkbutton(
            self,
            variable=self.gaps_check_var,
            text="Fill gaps"
        )
        self.gaps_check.grid(row=3, column=1)
        self.widgets.append(self.gaps_check)

        # gaps entry label

        self.gaps_entry_var = tk.StringVar()
        self.gaps_entry_label = tk.Label(
            self,
            text="gaps: "
        )
        self.gaps_entry_label.grid(row=4, column=0)
        self.widgets.append(self.gaps_entry_label)

        self.gaps_entry = tk.Entry(
            self,
            width=self.entry_width,
            textvariable=self.gaps_entry_var
        )
        self.gaps_entry.grid(row=4, column=1)
        self.entry_widgets.append(self.gaps_entry)

        for widget in self.widgets:
            widget.grid_configure(padx=5, pady=5)
        for widget in self.entry_widgets:
            widget.grid_configure(padx=5, pady=5)



    def refresh_colors(self):
        for widget in self.widgets:
            widget.configure(
                highlightbackground=colors["bg1"],
                background=colors["bg1"],
                foreground=colors["hl2"]
            )

        for widget in self.entry_widgets:
            widget.configure(
                highlightbackground=colors["bg1"],
                background=colors["bg2"],
                foreground=colors["hl2"]
            )


    def set_parameters(self, params):
        self.folder_name_var.set(params["folder_name"])
        self.counter_start_var.set(params["counter_start"])
        self.num_iterations_var.set(params["num_iterations"])
        self.import_check_var.set(int(params["import_check"]))
        self.gaps_check_var.set(int(params["gaps_check"]))
        self.gaps_entry.delete(0, tk.END)
        
        for gap in params["gaps_entry"]:
            self.gaps_entry.insert(tk.END, gap)
            self.gaps_entry.insert(tk.END, ",")

    def get_parameters(self):
        params = {}

        params["folder_name"] = self.folder_name_var.get()
        params["counter_start"] = self.counter_start_var.get()
        params["num_iterations"] = self.num_iterations_var.get()
        params["import_check"] = bool(self.import_check_var.get())
        params["gaps_check"] = bool(self.gaps_check_var.get())
        params["gaps_entry"] = self.parse_gaps_entry()

        return params
    

    def parse_gaps_entry(self, params):
        gaps = self.gaps_entry_var.get()
        if len(gaps) > 0:
            gaps = gaps.split(",")
        else:
            gaps = []

        return gaps