import os
import json
import sys

from tkinter import messagebox

from constants import *


if PLATFORM == 'win32':
    TONAME = '\\\\.\\pipe\\ToSrvPipe'
    FROMNAME = '\\\\.\\pipe\\FromSrvPipe'
    EOL = '\r\n\0'
else:
    TONAME = '/tmp/audacity_script_pipe.to.' + str(os.getuid())
    FROMNAME = '/tmp/audacity_script_pipe.from.' + str(os.getuid())
    EOL = '\n'

try:
  TOFILE = open(TONAME, 'w')
  FROMFILE = open(FROMNAME, 'rt')
except FileNotFoundError:
  messagebox.showerror("Pipe not found", 
    """The audacity pipe file was not found. 
    Please make sure that Audacity is open and mod-script-pipe is enabled in Audacity preferences.""")
  sys.exit()

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