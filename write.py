import json
from tkinter import messagebox

def write_json(filepath, data):

    print(data)
    try:
        with open(filepath, "w") as f:
            json.dump(data, f)
    except FileNotFoundError:
        messagebox.showerror("FileNotFoundError",
            f"Error: {filepath} does not exist.")