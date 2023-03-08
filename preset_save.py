import tkinter as tk

from write import *

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
        self.filename_entry.focus_set()
        self.filename_entry.bind("<KeyPress>", self.filename_entry_keypress)

        last = get_last_filename()
        if last != None:
            self.filename_entry.insert(0, last)
            self.filename_entry.selection_range(0, tk.END)

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
        set_last_filename(name)

        if name[-5:] != ".json":
            name = name + ".json"

        name = "data/presets/" + name

        preset = self.master.get_preset()
        write_json(name, preset)
        self.window.destroy()
        

    def cancel(self):
        self.window.destroy()


    def filename_entry_keypress(self, event):
        if event.keysym == "Return":
            self.save()