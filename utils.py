import os
import json
from sys import exit

from tkinter import messagebox

TONAME = '/tmp/audacity_script_pipe.to.' + str(os.getuid())
FROMNAME = '/tmp/audacity_script_pipe.from.' + str(os.getuid())

try:
  TOFILE = open(TONAME, 'w')
  FROMFILE = open(FROMNAME, 'rt')
except FileNotFoundError:
  messagebox.showerror("Pipe not found", 
    """The audacity pipe file was not found. 
    Please make sure Audacity is open before launching the application.""")
  exit()

def send_command(command):
  TOFILE.write(command + "\n")
  TOFILE.flush()


def get_response():
    """Return the command response."""
    result = ''
    line = ''
    while True:
        result += line
        line = FROMFILE.readline()
        if line == '\n' and len(result) > 0:
            break
    return result


def do_command(command):
  """Send one command, and return the response."""
  send_command(command)
  response = get_response()
  return response



def get_track_end(track_index):

    # Get audio info
    info = (do_command("GetInfo: Type=Tracks"))

    # Trim info
    info = info[1:-26]

    # Load track data
    track_data = json.loads(info)
    return track_data[track_index]["end"]