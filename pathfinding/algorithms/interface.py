class AlgorithmModule:
    def __init__(self):
        # use for counting viewed spot
        self.total_closed = 0

    def count_closed(self):
        self.total_closed += 1

    def forward(self, grid):
        pass