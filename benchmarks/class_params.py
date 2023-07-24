import numpy as np
from asv_runner.benchmarks.mark import *

class TimeSuite:
    params = [10, 100, 1000]
    param_names = ["size"]
    def setup(self, size):
        self.d = {}
        for x in range(size):
            self.d[x] = None

    def time_keys(self, size):
        for key in self.d.keys():
            pass

    def time_values(self, size):
        for value in self.d.values():
            pass
