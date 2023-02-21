import tkinter as tk

from write import write_json

class SavePreset(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.window = tk.Toplevel(self)

        self.filename_entry_var = tk.StringVar()
        self.filename_entry = tk.Entry(
            self.window,
            textvariable=self.filename_entry_var
        )
        self.filename_entry.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        self.cancel_button = tk.Button(
            self.window,
            text="Cancel",
            command=self.cancel
        )
        self.cancel_button.grid(row=1, column=0)

        self.save_button = tk.Button(
            self.window,
            text="Save",
            command=self.save
        )
        self.save_button.grid(row=1, column=1)


    def save(self):
        name = self.filename_entry_var.get()
        if name[-5:] != ".json":
            name = name + ".json"

        name = "data/presets/" + name

        write_json(name, self.master.get_preset())
        self.window.destroy()
        

    def cancel(self):
        self.window.destroy()