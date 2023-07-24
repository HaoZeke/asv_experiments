import numpy as np
from asv_runner.benchmarks.mark import parameterize

@parameterize({"n":[10, 100]})
def time_sort(n):
    np.sort(np.random.rand(n))

@parameterize({'n': [10, 100], 'func_name': ['range', 'arange']})
def time_ranges_multi(n, func_name):
    f = {'range': range, 'arange': np.arange}[func_name]
    for i in f(n):
        pass

@parameterize({"size": [10, 100, 200]})
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

@parameterize({'n': [10, 100], 'func_name': ['range', 'arange']})
class TimeSuiteMultiDecorator:
    def time_ranges(self, n, func_name):
        f = {'range': range, 'arange': np.arange}[func_name]
        for i in f(n):
            pass
