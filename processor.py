import json
import os

from utils import do_command

class Processor:
    def __init__(self, master):
        self.master = master

    def process(self, params, processes):
        self.counter_start = int(params["counter_start"])
        self.num_iterations = int(params["num_iterations"])

        if self.num_iterations < 1:
            return

        if params["import"] == True:
            (do_command("ImportRaw:"))

        # Get audio info
        info = (do_command("GetInfo: Type=Tracks"))

        # Trim info
        info = info[1:-26]

        # Load track data
        track_data = json.loads(info)
        first_track_end = track_data[0]["end"]

        # Set start and end
        start = 0.2
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
            (do_command("SelectAll:"))
            (do_command("Copy:"))

            # Select portion to process
            (do_command(f"SelectTime: Start={start}  End={end}"))

            for effect in processes:
                command = effect["name"] + ": "

                for param in effect["params"]:
                    value = self.get_value(
                        param["start_val"], 
                        param["end_val"],
                        i
                    )
                    command += param["name"] + "=" + str(value) + " "
                
                print(command)
                (do_command(command))

            # Select all for export
            (do_command("SelectAll:"))

            # Export
            filename = f"{filepath}/{i}.raw"
            command = f"Export2: Filename={filename}"
            (do_command(command))

            # Select all, delete, and paste original audio
            (do_command("SelectAll:"))
            (do_command("Delete:"))
            (do_command("Paste:"))



    def get_value(self, start_val, end_val, idx):
        if idx == 0:
            return start_val
        if idx == self.num_iterations:
            return end_val

        inc = (end_val - start_val) / self.num_iterations

        return start_val + (inc * idx)