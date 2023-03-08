import json
from tkinter import messagebox

# store last used filepath
last_filename = None

def set_last_filename(filename):
    global last_filename
    last_filename = filename

def get_last_filename():
    global last_filename
    return last_filename

def write_json(filepath, data):
    try:
        with open(filepath, "w") as f:
            json.dump(data, f)
    except FileNotFoundError:
        messagebox.showerror("FileNotFoundError",
            f"Error: {filepath} does not exist.")