import time


class StopWatch:

    def __init__(self):
        self.start = time.time()

    def elapsed_time(self):
        return round(time.time() - self.start, 2)
