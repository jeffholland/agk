import tkinter as tk

class Settings(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.window = tk.Toplevel(self)

        self.autosave_var = tk.IntVar()
        self.autosave_checkbox = tk.Checkbutton(
            self,
            text="autosave",
            variable=self.autosave_var
        )
        self.autosave_checkbox.grid(row=0, column=0)