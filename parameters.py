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
        self.num_iterations_var.set(0)
        self.entry_widgets.append(self.num_iterations_entry)

        # gaps checkbox

        self.gaps_check_var = tk.IntVar()
        self.gaps_check = tk.Checkbutton(
            self,
            variable=self.gaps_check_var,
            text="Fill gaps"
        )
        self.gaps_check.grid(row=3, column=0)
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