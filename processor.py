from utils import do_command

class Processor:
    def __init__(self, master):
        self.master = master

    def process(self, params, processes):
        num_iterations = int(params["num_iterations"])
        if num_iterations < 1:
            return

        if params["import"] == True:
            (do_command("ImportRaw:"))