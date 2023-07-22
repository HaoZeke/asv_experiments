# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import numpy as np
from asv_runner.benchmarks.mark import skip_benchmark_if, skip_params_if
import datetime

# class MyBenchmark:
#     params = [10, 100, 1000]

#     def setup(self, n):
#         self.data = np.random.rand(n)

#     def time_sort(self, n):
#         np.sort(self.data)

#     def time_sum(self, n):
#         np.sum(self.data)

#     # def time_fake_fail(self, n):
#     #     import someone

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    params = [100, 200, 300, 400, 500]
    param_names = ["size"]

    def setup(self, size):
        self.d = {}
        for x in range(size):
            self.d[x] = None

    @skip_benchmark_if(datetime.datetime.now().hour >= 12)
    def time_keys(self, size):
        for key in self.d.keys():
            pass

    @skip_benchmark_if(datetime.datetime.now().hour >= 12)
    def time_values(self, size):
        for value in self.d.values():
            pass

    @skip_benchmark_if(datetime.datetime.now().hour >= 12)
    def time_range(self, size):
        d = self.d
        for key in range(size):
            d[key]

    # Skip benchmarking when size is either 100 or 200 and the current hour is 12 or later.
    @skip_params_if([(100,), (200,)],
                    datetime.datetime.now().hour >= 12)
    def time_dict_update(self, size):
        d = self.d
        for i in range(size):
            d[i] = i

# class TimeSuite:
#     """
#     An example benchmark that times the performance of various kinds
#     of iterating over dictionaries in Python.
#     """
#     def setup(self):
#         self.d = {}
#         for x in range(500):
#             self.d[x] = None

#     def time_keys(self):
#         for key in self.d.keys():
#             pass

#     def time_values(self):
#         for value in self.d.values():
#             pass

#     @skip_benchmark_if(datetime.datetime.now().hour >= 12)
#     def time_range(self):
#         d = self.d
#         for key in range(500):
#             d[key]

# class Simple:
#     params = ([False, True])
#     param_names = ["ok"]

#     def time_failure(self, ok):
#         if ok:
#             x = 34.2**4.2
#         else:
#             # import something
#             raise NotImplementedError

# # class MemSuite:
# #     def mem_list(self):
# #         return [0] * 256

# class ParamSuite:
#     params = ['a', 'b', 'c']

#     def setup(self, p):
#         values = {'a': 1, 'b': 2, 'c': 3}
#         self.count = 0
#         self.value = values[p]

#     def track_value(self, p):
#         return self.value + self.count

#     def teardown(self, p):
#         self.count += 1
#         del self.value
