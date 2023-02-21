import tkinter as tk

from os import listdir

class LoadPreset(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.window = tk.Toplevel(self)

        self.listbox_var = tk.StringVar()
        self.listbox = tk.Listbox(
            self.window,
            listvariable=self.listbox_var
        )
        self.listbox.grid(row=0, column=0, padx=5, pady=5)

        files = listdir("./data/presets/")
        for i in range(len(files)):
            # remove .json extension
            files[i] = files[i][:-5]

        self.listbox_var.set(files)

        self.listbox.bind("<Double-1>", self.load)

    def load(self, event):
        index = self.listbox.curselection()[0]
        selected = self.listbox.get(index)

        filepath = "data/presets/" + selected + ".json"
        self.master.set_preset(filepath)
        self.window.destroy()