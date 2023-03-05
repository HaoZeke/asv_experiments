# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import numpy as np

class MyBenchmark:
    params = [10, 100, 1000]

    def setup(self, n):
        self.data = np.random.rand(n)

    def time_sort(self, n):
        np.sort(self.data)

    def time_sum(self, n):
        np.sum(self.data)


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None

    def time_keys(self):
        for key in self.d.keys():
            pass

    def time_values(self):
        for value in self.d.values():
            pass

    def time_range(self):
        d = self.d
        for key in range(500):
            d[key]


class MemSuite:
    def mem_list(self):
        return [0] * 256
