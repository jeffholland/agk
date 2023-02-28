import json
import os
from time import sleep

from utils import do_command
import pipe_client

class Processor:
    def __init__(self, master):
        self.master = master

        self.client = pipe_client.PipeClient()


    def write(self, command):
        # custom write function for debugging
        self.client.write(command, timer=True)

        response = ''
        while response == '':
            sleep(0.1)
            response = self.client.read()

        print(f"pipe client reply: {response}")


    def process(self, params, processes):
        self.counter_start = int(params["counter_start"])
        self.num_iterations = int(params["num_iterations"])

        if self.num_iterations < 1:
            return

        if params["import"] == True:
            command = "ImportRaw:"
            # (do_command(command))
            self.write(command)

        # wait for import raw command to finish
        sleep(0.1)
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
        filepath = f"/Users/jholland/Pictures/glitch/{folder_name}"
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



    def get_value(self, start_val, end_val, idx):
        if idx == 0:
            return start_val
        if idx == self.num_iterations:
            return end_val

        inc = (end_val - start_val) / self.num_iterations

        return start_val + (inc * (idx - self.counter_start))