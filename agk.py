import tkinter as tk

class AudacityGlitchKitchen(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid(row=0, column=0)

        self.width = 400
        self.height = 800
        
        self.entry_width = 25
        
        self.create_widgets()

    def create_widgets(self):

        # folder name

        self.folder_name_var = tk.StringVar()
        self.folder_name_label = tk.Label(
            self,
            text="Folder name: "
        )
        self.folder_name_label.grid(row=0, column=0)
        self.folder_name_entry = tk.Entry(
            self,
            width=self.entry_width,
            textvariable=self.folder_name_var
        )
        self.folder_name_entry.grid(row=0, column=1)
        self.folder_name_var.set("gen1")

        # counter start

        self.counter_start_var = tk.StringVar()
        self.counter_start_label = tk.Label(
            self,
            text="Counter start: "
        )
        self.counter_start_label.grid(row=1, column=0)
        self.counter_start_entry = tk.Entry(
            self,
            textvariable=self.counter_start_var,
            width=self.entry_width
        )
        self.counter_start_entry.grid(row=1, column=1)
        self.counter_start_var.set(0)

        # num iterations

        self.num_iterations_var = tk.StringVar()
        self.num_iterations_label = tk.Label(
            self,
            text="Num iterations: "
        )
        self.num_iterations_label.grid(row=2, column=0)
        self.num_iterations_entry = tk.Entry(
            self,
            textvariable=self.num_iterations_var,
            width=self.entry_width
        )
        self.num_iterations_entry.grid(row=2, column=1)
        self.num_iterations_var.set(0)

        # GAPS

        self.gaps_check_var = tk.IntVar()
        self.gaps_check = tk.Checkbutton(
            self,
            variable=self.gaps_check_var,
            text="Fill gaps"
        )
        self.gaps_check.grid(row=3, column=0)

        self.gaps_entry_var = tk.StringVar()
        self.gaps_entry_label = tk.Label(
            self,
            text="gaps: "
        )
        self.gaps_entry_label.grid(row=4, column=0)

        self.gaps_entry = tk.Entry(
            self,
            width=self.entry_width,
            textvariable=self.gaps_entry_var
        )
        self.gaps_entry.grid(row=4, column=1)


app = AudacityGlitchKitchen()
app.master.title("AudacityGlitchKitchen")
app.master.geometry(str(app.width) + "x" + str(app.height))
app.mainloop()