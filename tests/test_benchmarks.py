import random

from more_containers import uniquetuple

n = 1000
unique_unordered_ints = list(range(n))
random.shuffle(unique_unordered_ints)
repeated_unordered_ints = [random.choice(unique_unordered_ints[:100]) for i in range(n)]


def test_benchmark_uniquetuple1(benchmark):

    benchmark.group = 'uniquetuple.unique_unordered'

    def f():
        lambda: uniquetuple(*unique_unordered_ints)

    return benchmark(f)


def test_benchmark_uniquetuple2(benchmark):

    benchmark.group = 'uniquetuple.repeated_unordered'

    def f():
        return uniquetuple(*repeated_unordered_ints)

    return benchmark(f)
