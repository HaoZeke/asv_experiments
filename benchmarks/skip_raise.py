from asv_runner.benchmarks.mark import skip_for_params, parameterize, SkipNotImplemented

# Fast because no setup is called
class SimpleFast:
    params = ([False, True])
    param_names = ["ok"]

    @skip_for_params([(False, )])
    def time_failure(self, ok):
        if ok:
            x = 34.2**4.2

@parameterize({"ok": [False, True]})
class SimpleSlow:
    def time_failure(self, ok):
        if ok:
            x = 34.2**4.2
        else:
            raise SkipNotImplemented(f"{ok} is skipped")
