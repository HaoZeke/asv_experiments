import numpy as np
from asv_runner.benchmarks.mark import parameterize_class_with, skip_benchmark

@skip_benchmark
class TimeSuiteStandardSingle:
    params = [10, 100, 200]
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

@skip_benchmark
@parameterize_class_with({"size": [10, 100, 200]})
class TimeSuiteDecoratorSingle:
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

@skip_benchmark
class TimeSuiteMulti:
    params = ([10, 100], ['range', 'arange'])
    param_names = ['n', 'func_name']
    def time_ranges(self, n, func_name):
        f = {'range': range, 'arange': np.arange}[func_name]
        for i in f(n):
            pass

@skip_benchmark
@parameterize_class_with({'n': [10, 100], 'func_name': ['range', 'arange']})
class TimeSuiteMultiDecorator:
    def time_ranges(self, n, func_name):
        f = {'range': range, 'arange': np.arange}[func_name]
        for i in f(n):
            pass
