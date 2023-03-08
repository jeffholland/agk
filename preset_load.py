import tkinter as tk

import os

class LoadPreset(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.selected = None
        self.filepath = None
        self.rename_window = None

        self.create_widgets()

    def create_widgets(self):
        self.window = tk.Toplevel(self)

        self.listbox_var = tk.StringVar()
        self.listbox = tk.Listbox(
            self.window,
            listvariable=self.listbox_var,
            width=15
        )
        self.listbox.grid(row=0, column=0, padx=5, pady=5, rowspan=3)

        self.refresh_files()

        self.listbox.bind("<Double-1>", self.load)
        self.listbox.bind("<<ListboxSelect>>", self.select)

        # Buttons!

        self.select_button = tk.Button(
            self.window,
            text="Select",
            command=self.load
        )
        self.select_button.grid(row=0, column=1)

        self.delete_button = tk.Button(
            self.window,
            text="Delete",
            command=self.delete
        )
        self.delete_button.grid(row=1, column=1)

        self.rename_button = tk.Button(
            self.window,
            text="Rename",
            command=self.rename
        )
        self.rename_button.grid(row=2, column=1)

    def load(self, event=None):
        self.master.set_preset(self.filepath)
        self.window.destroy()

    def select(self, event=None):
        index = self.listbox.curselection()[0]
        self.selected = self.listbox.get(index)
        self.filepath = "data/presets/" + self.selected + ".json"

    def delete(self):
        os.remove(self.filepath)
        self.refresh_files()

    def rename(self):
        self.rename_window = tk.Toplevel(self)
        self.rename_entry_var = tk.StringVar()
        rename_entry = tk.Entry(
            self.rename_window,
            textvariable=self.rename_entry_var
        )
        rename_submit_button = tk.Button(
            self.rename_window,
            text="Submit",
            command=self.rename_submit
        )
        rename_entry.grid(row=0, column=0)
        rename_entry.focus_set()
        rename_submit_button.grid(row=1, column=0)

        rename_entry.bind("<KeyPress>", self.rename_keypress)

    def rename_submit(self):
        new_filepath = "data/presets/" + self.rename_entry_var.get() + ".json"
        os.rename(self.filepath, new_filepath)
        self.refresh_files()

        self.rename_window.destroy()
        self.rename_window = None

    def rename_keypress(self, event):
        if event.keysym == "Return":
            self.rename_submit()
        

    def refresh_files(self):
        files = os.listdir("./data/presets/")
        for i in range(len(files)):
            # remove .json extension
            files[i] = files[i][:-5]
        files.sort()
        self.listbox_var.set(files)