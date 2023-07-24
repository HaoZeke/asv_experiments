from asv_runner.benchmarks.mark import skip_for_params
class Simple:
    params = ([False, True])
    param_names = ["ok"]

    @skip_for_params([(False, )])
    def time_failure(self, ok):
        if ok:
            x = 34.2**4.2
class Base:

    def sub_specific(self):
        raise NotImplementedError()

    def setup_cache(self):
        # load data from a file
        ret = self.sub_specific()
        print("setup_cache %s for %s" % (ret, self))


class Benchmarks:
    def time_upper(self):
        i = 1

class Suite1(Base, Benchmarks):
    def sub_specific(self):
        return "Suite1"

class Suite2(Base, Benchmarks):
    def sub_specific(self):
        return "Suite2"
