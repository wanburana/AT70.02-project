from time import time

class AlgorithmModule:
    def __init__(self):
        # use for counting viewed spot
        self.total_closed = 0
        self.start_time = 0
        self.stop_time = 0
        self.taken_time = 0
        self.found = False

    def count_closed(self):
        self.total_closed += 1

    def start_timer(self):
        self.start_time = time()
    
    def stop_timer(self):
        self.stop_time = time()
        self.taken_time = self.stop_time - self.start_time

    def forward(self, grid):
        pass