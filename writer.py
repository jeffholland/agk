import json
from tkinter import messagebox

class Writer:
    def __init__(self):
        pass

    def write_json(self, filepath, data):
        print(f"writing {data} to {filepath}")

        try:
            with open(filepath, "w") as f:
                json.dump(data, f)
        except FileNotFoundError:
            messagebox.showerror("FileNotFoundError",
                f"Error: {filepath} does not exist.")