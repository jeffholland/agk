import json
import os
import sys
from time import sleep
from subprocess import run

from tkinter import messagebox

from utils import do_command
import pipe_client

from constants import *

class Processor:
    def __init__(self, master):
        self.master = master

        # Check every {self.wait_time} seconds for a response
        self.wait_time = 0.1
        # Call self.timeout after {self.timeout_time} seconds with no response
        self.timeout_time = 5.0

        # Path to write files to
        self.path = os.path.expanduser('~') + "/Pictures/glitch/"

        self.client = pipe_client.PipeClient()


    def write(self, command, timeout=True):
        # custom write function for debugging
        self.client.write(command, timer=True)

        response = ''
        time_elapsed = 0
        while response == '':
            if timeout == True:
                if time_elapsed > 5.0:
                    self.timeout(command)

            sleep(self.wait_time)
            time_elapsed += self.wait_time
            
            response = self.client.read()


    def process(self, params, processes):
        self.counter_start = int(params["counter_start"])
        self.num_iterations = int(params["num_iterations"])

        if self.num_iterations < 1:
            return

        if params["import"] == True:
            command = "ImportRaw:"
            # (do_command(command))
            self.write(command, timeout=False)

        # Get audio info
        command = "GetInfo: Type=Tracks"
        info = (do_command(command))

        # Trim info
        info = info[1:-26]

        # Load track data
        track_data = json.loads(info)
        first_track_end = track_data[0]["end"]

        # Set start and end
        start = 0.2   # 0.2 secs is enough to avoid image header
        end = first_track_end

        # Create file path if does not already exist
        folder_name = params["folder_name"]
        filepath = self.path + folder_name
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        
        for i in range(self.counter_start, 
            self.num_iterations + self.counter_start):

            if params["fill_gaps"] == True:
                if i not in params["gaps"]:
                    continue

            # Copy audio
            command = "SelectAll:"
            # (do_command(command))
            self.write(command)
            command = "Copy:"
            # (do_command(command))
            self.write(command)

            # Select portion to process
            command = f"SelectTime: Start={start}  End={end}"
            # (do_command(command))
            self.write(command)

            for effect in processes:
                command = effect["name"] + ": "

                for param in effect["params"]:
                    start_val = float(param["start_val"])
                    end_val = float(param["end_val"])
                    value = self.get_value(start_val, end_val, i)
                    command += param["name"] + "=" + str(value) + " "
                
                print(command)
                # (do_command(command))
                self.write(command)

            # Select all for export
            command = "SelectAll:"
            # (do_command(command))
            self.write(command)

            # Export
            filename = f"{filepath}/{i}.raw"
            command = f"Export2: Filename={filename}"
            # (do_command(command))
            self.write(command)

            # Select all, delete, and paste original audio
            # (do_command("SelectAll:"))
            # (do_command("Delete:"))
            # (do_command("Paste:"))
            self.write("SelectAll:")
            self.write("Delete:")
            self.write("Paste:")

        if TEST_TIMEOUT:
            self.timeout(command)
        else:
            self.success(params)



    def get_value(self, start_val, end_val, idx):
        if idx == 0:
            return start_val
        if idx == self.num_iterations:
            return end_val

        inc = (end_val - start_val) / self.num_iterations

        return start_val + (inc * (idx - self.counter_start))
    

    # This function runs when a process times out
    # (usually means the application froze).
    # This is unfortunately quite common.
    # The only solution I currently have is to display an error,
    # shut down Audacity, and shut down the application.
    
    def timeout(self, command):
        messagebox.showerror("command timed out",
        f"The current command timed out: {command}\nExiting...")

        # Kill Audacity
        if PLATFORM == "win32":
            # not tested on Windows yet
            run(["taskkill","/IM","Audacity","/F"],shell=True)
        else:
            run(["killall Audacity"],shell=True)

        # Kill AGK
        sys.exit()



    # This function is called when the process completes.
    # It can easily be edited to display different info
    # at the end of the process.

    def success(self, params):
        num_iterations = params["num_iterations"]
        if params["fill_gaps"] == True:
            num_iterations = len(params["gaps"])

        full_path = self.path + params["folder_name"]

        messagebox.showinfo("Success",
            f"Done - wrote {num_iterations} files to {full_path}.")