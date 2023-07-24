import numpy as np
from asv_runner.benchmarks.mark import parameterize_func_with

def time_sort(n):
    np.sort(np.random.rand(n))
time_sort.params = ([10, 100])
time_sort.param_names = ['n']

@parameterize_func_with({"n":[10, 100]})
def time_sort(n):
    np.sort(np.random.rand(n))

def time_ranges_multi(n, func_name):

    f = {'range': range, 'arange': np.arange}[func_name]
    for i in f(n):
        pass
time_ranges_multi.params = ([10, 100], ['range', 'arange'])
time_ranges_multi.param_names = ['n', 'function']

@parameterize_func_with({'n': [10, 100], 'func_name': ['range', 'arange']})
def time_ranges_multi(n, func_name):
    f = {'range': range, 'arange': np.arange}[func_name]
    for i in f(n):
        pass
